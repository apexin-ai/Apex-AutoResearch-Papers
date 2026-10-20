# Research conversation: Fetch the arXiv paper at https://arxiv.org/abs/2311.09807 using WebFetch. First fetch the HTML version at https://arxiv.

**Characterizing the Detectability Landscape of Iterative Model Collapse (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 8
- **Recorded user turns:** 1
- **Tool calls:** 2
- **Original source:** `logs/chats/exported-trajectories/account-2/agent-a9d9703ccc0d5ee09.jsonl`
- **Structured JSON:** [`9d4f331daa33e47ef47c.json`](../../sessions/9d/9d4f331daa33e47ef47c.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

8 recorded events

### User

_source line 1 · 2026-05-20T15:00:49.650Z_

Fetch the arXiv paper at https://arxiv.org/abs/2311.09807 using WebFetch.

First fetch the HTML version at https://arxiv.org/html/2311.09807v2 with the prompt:
"Extract the full paper content in detail. I need:
1. Complete introduction section with all paragraphs
2. The contribution statement (usually end of intro)
3. Complete experiment/results section including all tables and figures descriptions
4. Limitations and future work section
5. All figure and table captions
6. All references to figures/tables in the main text
7. Method section key details
8. Baselines, metrics, datasets used
9. Training recipe details (optimizer, lr, hardware, etc.)
Return as much detail as possible."

If the HTML version fails, try https://arxiv.org/abs/2311.09807 with the same prompt.

Then report EVERYTHING you extracted - do not summarize, give me the full extracted content. This is "The Curious Decline of Linguistic Diversity: Training Language Models on Synthetic Text" (NAACL 2024 Findings).

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "1da41794-e339-4608-bf95-c667636bcab8",
  "agentId": "a9d9703ccc0d5ee09",
  "type": "user",
  "uuid": "94185b66-d2dc-42ff-ba5c-a2994ee4d5cf",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/.claude/sessions/distiller_3275b75a",
  "sessionId": "e1199c41-0624-4bbe-a3c3-3e8c7b3fc1ae",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Runtime record

_source line 2 · 2026-05-20T15:00:49.654Z_

```json
{
  "parentUuid": "94185b66-d2dc-42ff-ba5c-a2994ee4d5cf",
  "isSidechain": true,
  "agentId": "a9d9703ccc0d5ee09",
  "attachment": {
    "type": "deferred_tools_delta",
    "addedNames": [
      "EnterWorktree",
      "ExitWorktree",
      "Monitor",
      "NotebookEdit",
      "TaskStop",
      "WebFetch",
      "WebSearch",
      "mcp__agent-ml-research__load_project_config",
      "mcp__agent-ml-research__read_project_file",
      "mcp__agent-ml-research__save_project_file"
    ],
    "addedLines": [
      "EnterWorktree",
      "ExitWorktree",
      "Monitor",
      "NotebookEdit",
      "TaskStop",
      "WebFetch",
      "WebSearch",
      "mcp__agent-ml-research__load_project_config",
      "mcp__agent-ml-research__read_project_file",
      "mcp__agent-ml-research__save_project_file"
    ],
    "removedNames": []
  },
  "type": "attachment",
  "uuid": "b5b87a4b-4093-4a1f-8dbb-807c5875f8fc",
  "timestamp": "2026-05-20T15:00:49.654Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/.claude/sessions/distiller_3275b75a",
  "sessionId": "e1199c41-0624-4bbe-a3c3-3e8c7b3fc1ae",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

---

### Tool call

_source line 3 · 2026-05-20T15:00:54.164Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01EH1E1o91xmgMZbE3wtXdbU`</summary>

```json
{
  "query": "select:WebFetch",
  "max_results": 1
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b5b87a4b-4093-4a1f-8dbb-807c5875f8fc",
  "isSidechain": true,
  "agentId": "a9d9703ccc0d5ee09",
  "requestId": "req_011CbE2BffczyAxSGHyuL7C9",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "444039be-b4f3-408e-860a-d62eb35717bc",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/.claude/sessions/distiller_3275b75a",
  "sessionId": "e1199c41-0624-4bbe-a3c3-3e8c7b3fc1ae",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01PsU6z58cm8vzurSreVFWoS",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 9047,
      "cache_read_input_tokens": 8155,
      "output_tokens": 77,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 9047
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 77,
          "cache_read_input_tokens": 8155,
          "cache_creation_input_tokens": 9047,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 9047,
            "ephemeral_1h_input_tokens": 0
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

_source line 4 · 2026-05-20T15:00:54.167Z_

<details><summary>↩ Tool result · `toolu_01EH1E1o91xmgMZbE3wtXdbU`</summary>

````text
```json
{
  "type": "tool_reference",
  "tool_name": "WebFetch"
}
```
````

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "444039be-b4f3-408e-860a-d62eb35717bc",
  "isSidechain": true,
  "promptId": "1da41794-e339-4608-bf95-c667636bcab8",
  "agentId": "a9d9703ccc0d5ee09",
  "type": "user",
  "uuid": "66b87067-5bf2-45c4-9124-35fab8e840f3",
  "sourceToolAssistantUUID": "444039be-b4f3-408e-860a-d62eb35717bc",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/.claude/sessions/distiller_3275b75a",
  "sessionId": "e1199c41-0624-4bbe-a3c3-3e8c7b3fc1ae",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Assistant

_source line 5 · 2026-05-20T15:00:57.065Z_

I'll fetch the HTML version of the paper first, then fall back to the abstract page if needed.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "66b87067-5bf2-45c4-9124-35fab8e840f3",
  "isSidechain": true,
  "agentId": "a9d9703ccc0d5ee09",
  "requestId": "req_011CbE2BzpnxwqFFuWifu9E4",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "9e73173a-f1aa-4ec2-a95f-0c2890cffbde",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/.claude/sessions/distiller_3275b75a",
  "sessionId": "e1199c41-0624-4bbe-a3c3-3e8c7b3fc1ae",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01QsLGK9nQ3pdrctahtdaCNt",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1432,
      "cache_read_input_tokens": 17202,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1432,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 1,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool call

_source line 6 · 2026-05-20T15:00:57.876Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01VbbpRd6Yp8QY5kBnjPeaeb`</summary>

```json
{
  "url": "https://arxiv.org/html/2311.09807v2",
  "prompt": "Extract the full paper content in detail. I need:\n1. Complete introduction section with all paragraphs\n2. The contribution statement (usually end of intro)\n3. Complete experiment/results section including all tables and figures descriptions\n4. Limitations and future work section\n5. All figure and table captions\n6. All references to figures/tables in the main text\n7. Method section key details\n8. Baselines, metrics, datasets used\n9. Training recipe details (optimizer, lr, hardware, etc.)\nReturn as much detail as possible."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9e73173a-f1aa-4ec2-a95f-0c2890cffbde",
  "isSidechain": true,
  "agentId": "a9d9703ccc0d5ee09",
  "requestId": "req_011CbE2BzpnxwqFFuWifu9E4",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "db67be6b-7909-4fb8-be5a-c1635e2ed035",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/.claude/sessions/distiller_3275b75a",
  "sessionId": "e1199c41-0624-4bbe-a3c3-3e8c7b3fc1ae",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01QsLGK9nQ3pdrctahtdaCNt",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1432,
      "cache_read_input_tokens": 17202,
      "output_tokens": 225,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1432
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 225,
          "cache_read_input_tokens": 17202,
          "cache_creation_input_tokens": 1432,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1432,
            "ephemeral_1h_input_tokens": 0
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

_source line 7 · 2026-05-20T15:01:23.404Z_

<details><summary>↩ Tool result · `toolu_01VbbpRd6Yp8QY5kBnjPeaeb`</summary>

```text
# Paper Summary: The Curious Decline of Linguistic Diversity

## 1. INTRODUCTION

The paper addresses a critical challenge in language model development: exhaustion of high-quality training data. As noted, "the world's entire supply of high-quality text ranges up to 17 trillion tokens, with a 4-5% yearly growth rate," while major models like Llama 2 consumed roughly 2 trillion tokens. This scarcity has led practitioners to train models on synthetic text generated by predecessors—either through pretraining on web-sourced model outputs or via data augmentation techniques like self-instruct.

The authors identify two concerning failure modes: (1) irreversible flaws where distribution tails vanish (model collapse), and (2) convergence to uniform behavior through recursive sampling of high-probability events.

**Core Research Questions:**
- How can linguistic diversity be quantified effectively?
- Does recursive training on synthetic text reduce linguistic diversity in outputs?

**Key Contribution:** The paper introduces "the first comprehensive set of metrics assessing three linguistic diversity aspects: lexical, semantic, and syntactic," evaluated across recursive finetuning experiments on three NLG tasks with varying creativity demands.

## 2. METHODOLOGY

### 2.1 Recursive Training Simulation

The experimental design follows this cycle:
1. Finetune Base(1) on human Data(0) → Model(1)
2. Generate synthetic Data(1) from Model(1)
3. Finetune Base(2) on Data(1) → Model(2)
4. Repeat for n=6 iterations

Each generation uses fresh base model instances (simplified assumption). The authors justify using only Data(n-1) rather than accumulated data based on prior work showing model collapse is inevitable regardless.

### 2.2 Tasks Evaluated

**News Summarization (XL-SUM):** 306,522 training samples, ~386-token articles summarized to ~28 tokens. Classified as "low entropy" (constrained).

**Scientific Abstract Generation (ACL Anthology):** 40,512 training samples. Model receives title + first sentence (~42 tokens) and generates remaining abstract (~145 tokens total). "Medium entropy" task.

**Story Generation (WritingPrompts):** 272,600 training samples. ~30-token prompts generate ~389-token stories. "High entropy" (most creative).

### 2.3 Decoding Strategy

Task-specific sampling parameters:
- News summarization: p=0.1, τ=0.3 (emphasis on precision)
- Scientific abstract: p=0.5, τ=0.5 (balanced)
- Story generation: p=0.9, τ=0.7 (emphasis on creativity)

Max tokens: 50 (news), 300 (abstracts), 500 (stories)

## 3. LINGUISTIC DIVERSITY METRICS

### 3.3.1 Lexical Diversity

**Type-Token Ratio (TTR):** Unique words divided by total words. Text truncated to fixed lengths (20 words for news, 50 for abstracts, 150 for stories) to normalize for length bias.

**Distinct-n:** Ratio of unique n-grams to total n-grams. Reported for n=2 and n=3.

**Self-BLEU:** Average BLEU similarity between each sentence and others in generated set. Reported as 1-Self-BLEU (higher = more diverse).

### 3.3.2 Semantic Diversity

Sentence embeddings generated via Sentence-BERT (all-mpnet-base-v2). Diversity measured as average pairwise cosine-distance across 2,000 randomly sampled sentences (mean of 5 runs).

### 3.3.3 Syntactic Diversity

**Novel contribution:** Uses Weisfeiler-Lehman graph kernels on dependency trees. Process:
1. Parse sentences using Stanza dependency parser
2. Convert to graph representations (nodes=words, edges=dependencies)
3. Embed via WL-kernel (2 iterations)
4. Calculate average pairwise distances

## 4. RESULTS

### Table 2 Summary: Key Findings

**News Summarization:**
- Perplexity: 12.5→2.48 (improving through iterations)
- TTR: 5.99%→3.66% (↓49% from human)
- Distinct-2: 37.9%→25.6%
- Syntactic diversity: 1.65→0.82 (↓74% from human 3.17)
- Semantic diversity: relatively stable

**Scientific Abstract Generation:**
- TTR: 2.06%→1.69% (↓45% from human 3.09)
- Distinct-2: 20.7%→13.3%
- Syntactic diversity: 3.80→4.10 (slight increase initially, then decline)

**Story Generation (most pronounced decline):**
- TTR: 0.84%→0.61% (↓73% from human 2.23)
- Distinct-2: 13.8%→11.4%
- Syntactic diversity: 4.23→1.96 (↓60%)
- Semantic diversity: 41.4→42.5 (most stable)

### Key Observations

**Finding 1:** High-entropy tasks show steeper diversity decline. Story generation exhibits the "fastest decline" and largest gap from human-generated text.

**Finding 2:** Even constrained tasks eventually lose diversity. Scientific abstract generation initially shows higher syntactic diversity than humans (due to mismatch from pretraining distribution) but eventually falls below human levels via "catastrophic forgetting."

**Finding 3:** Syntactic diversity "suffers remarkably"—comparable lexical decline but more severe than semantic changes. This is "the first to highlight the decrease in syntactic diversity."

**Finding 4:** Semantic diversity remains "most stable." Authors hypothesize synthetic data impacts form more than content, with issues manifesting as coherence loss rather than diversity loss.

### 4.3 Mitigation Strategies

**Filtering Synthetic Data:** Using RoBERTa-CoLA acceptability filter to remove bottom 20% of samples actually *amplifies* diversity decline. Quality filtering favors common, less inventive samples.

**Mixing Fresh Human Data:** Holding out 60% human data and mixing 10% fresh human data at each iteration only "minimally mitigates" the observed decrease.

**Conclusion on mitigation:** Neither strategy effectively prevents diversity loss.

## 5. LIMITATIONS

**Language scope:** English-only evaluation. "Linguistic diversity metrics may not perform optimally for languages apart from English" due to reliance on language-specific tokenization and dependency parsing.

**Model scale:** OPT-350M used (avoiding OPT-125M due to quality degradation across 6 iterations). "Could not perform experiments on an extensive range of models." Story generation alone required ~700 GPU hours on NVIDIA RTX A6000.

**Realistic web setting:** Authors acknowledge infeasibility of true web-scale synthesis simulation. Synthetic web text dataset construction poses copyright issues; no reliable LLM-detection algorithm exists.

## 6. EXPERIMENTAL SETUP DETAILS

**Base model:** OPT-350M
**Optimizer:** AdamW
**Hardware:** 2× NVIDIA RTX A6000 GPUs
**Training:** 5 epochs per iteration
**Perplexity:** Monitored to ensure output quality (all results <20)

## 7. FIGURE/TABLE DESCRIPTIONS

**Table 1 (Model Outputs Example):** Shows scientific abstract generation across iterations. Observable pattern: model begins generating artificial URLs and code links repeatedly by Iteration 5, mimicking high-probability training patterns from ACL papers.

**Figure 1 (Recursive Process):** Diagram illustrating cycle: Data(0)→Model(1)→Data(1)→Model(2)...

**Figure 2 (Mitigation Strategies):** Distinct-3 and syntactic diversity tracking across filtering and mixed-human settings. Shows minimal improvement.

**Figure 3 (Word Frequency Histograms):** Demonstrates "diminishing presence of low-frequency, 'unique' words" across iterations, with pattern intensifying.

**Figure 4 (Syntactic Embeddings t-SNE):** Shows increasing spatial compactness of dependency tree embeddings across iterations.

**Figure 5 (Semantic Embeddings t-SNE):** Demonstrates reduced dispersion in sentence embeddings, but less pronounced than syntactic changes.

## 8. ETHICAL CONSIDERATIONS

**Datasets:** XL-SUM and ACL Anthology use CC BY-NC-SA 4.0; WritingPrompts uses MIT license. No personally identifiable information involved.

**Potential risks:** Authors caution against overgeneralization of findings beyond specific experimental contexts; findings validated on specific datasets only.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "db67be6b-7909-4fb8-be5a-c1635e2ed035",
  "isSidechain": true,
  "promptId": "1da41794-e339-4608-bf95-c667636bcab8",
  "agentId": "a9d9703ccc0d5ee09",
  "type": "user",
  "uuid": "96b972df-5af0-45ec-94f6-983276f65901",
  "sourceToolAssistantUUID": "db67be6b-7909-4fb8-be5a-c1635e2ed035",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/.claude/sessions/distiller_3275b75a",
  "sessionId": "e1199c41-0624-4bbe-a3c3-3e8c7b3fc1ae",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Assistant

_source line 8 · 2026-05-20T15:01:47.951Z_

Here is everything extracted from the paper "The Curious Decline of Linguistic Diversity: Training Language Models on Synthetic Text" (arXiv 2311.09807v2, NAACL 2024 Findings):

---

## 1. INTRODUCTION

The paper addresses a critical challenge in language model development: exhaustion of high-quality training data. As noted, "the world's entire supply of high-quality text ranges up to 17 trillion tokens, with a 4-5% yearly growth rate," while major models like Llama 2 consumed roughly 2 trillion tokens. This scarcity has led practitioners to train models on synthetic text generated by predecessors — either through pretraining on web-sourced model outputs or via data augmentation techniques like self-instruct.

The authors identify two concerning failure modes: (1) irreversible flaws where distribution tails vanish (model collapse), and (2) convergence to uniform behavior through recursive sampling of high-probability events.

**Core Research Questions:**
- How can linguistic diversity be quantified effectively?
- Does recursive training on synthetic text reduce linguistic diversity in outputs?

**Contribution Statement:** "The first comprehensive set of metrics assessing three linguistic diversity aspects: lexical, semantic, and syntactic," evaluated across recursive finetuning experiments on three NLG tasks with varying creativity demands.

---

## 2. METHODOLOGY

### Recursive Training Simulation

Experimental design cycle:
1. Finetune Base(1) on human Data(0) → Model(1)
2. Generate synthetic Data(1) from Model(1)
3. Finetune Base(2) on Data(1) → Model(2)
4. Repeat for n=6 iterations

Each generation uses fresh base model instances. The authors justify using only Data(n-1) rather than accumulated data based on prior work showing model collapse is inevitable regardless.

### Tasks Evaluated

**News Summarization (XL-SUM):** 306,522 training samples, ~386-token articles summarized to ~28 tokens. Low-entropy (constrained).

**Scientific Abstract Generation (ACL Anthology):** 40,512 training samples. Model receives title + first sentence (~42 tokens), generates remaining abstract (~145 tokens total). Medium-entropy.

**Story Generation (WritingPrompts):** 272,600 training samples. ~30-token prompts → ~389-token stories. High-entropy (most creative).

### Decoding Strategy

Task-specific sampling parameters:
- News summarization: p=0.1, τ=0.3
- Scientific abstract: p=0.5, τ=0.5
- Story generation: p=0.9, τ=0.7

Max tokens: 50 (news), 300 (abstracts), 500 (stories)

---

## 3. LINGUISTIC DIVERSITY METRICS

### Lexical Diversity
- **Type-Token Ratio (TTR):** Unique words / total words. Text truncated to fixed lengths (20 words news, 50 abstracts, 150 stories) to normalize length bias.
- **Distinct-n:** Ratio of unique n-grams to total n-grams. Reported for n=2 and n=3.
- **Self-BLEU:** Average BLEU similarity between each sentence and others in set. Reported as 1-Self-BLEU (higher = more diverse).

### Semantic Diversity
Sentence embeddings via Sentence-BERT (all-mpnet-base-v2). Average pairwise cosine-distance across 2,000 randomly sampled sentences (mean of 5 runs).

### Syntactic Diversity (Novel Contribution)
Uses Weisfeiler-Lehman graph kernels on dependency trees:
1. Parse sentences using Stanza dependency parser
2. Convert to graph representations (nodes=words, edges=dependencies)
3. Embed via WL-kernel (2 iterations)
4. Calculate average pairwise distances

---

## 4. RESULTS

### Table 2: Key Findings

**News Summarization:**
- Perplexity: 12.5 → 2.48 (improving)
- TTR: 5.99% → 3.66% (↓49% from human)
- Distinct-2: 37.9% → 25.6%
- Syntactic diversity: 1.65 → 0.82 (↓74% from human 3.17)
- Semantic diversity: relatively stable

**Scientific Abstract Generation:**
- TTR: 2.06% → 1.69% (↓45% from human 3.09%)
- Distinct-2: 20.7% → 13.3%
- Syntactic diversity: 3.80 → 4.10 (slight initial increase, then decline)

**Story Generation (most pronounced):**
- TTR: 0.84% → 0.61% (↓73% from human 2.23%)
- Distinct-2: 13.8% → 11.4%
- Syntactic diversity: 4.23 → 1.96 (↓60%)
- Semantic diversity: 41.4 → 42.5 (most stable)

### Key Findings

**Finding 1:** High-entropy tasks show steeper diversity decline. Story generation exhibits fastest decline and largest gap from human-generated text.

**Finding 2:** Even constrained tasks eventually lose diversity. Scientific abstract generation initially shows higher syntactic diversity than humans (due to pretraining distribution mismatch) but eventually falls below human levels via "catastrophic forgetting."

**Finding 3:** Syntactic diversity "suffers remarkably" — more severe than lexical or semantic changes. This is claimed as "the first to highlight the decrease in syntactic diversity."

**Finding 4:** Semantic diversity remains "most stable." Synthetic data impacts form more than content; issues manifest as coherence loss rather than diversity loss.

### Mitigation Strategies

**Filtering Synthetic Data:** Using RoBERTa-CoLA acceptability filter to remove bottom 20% of samples actually *amplifies* diversity decline. Quality filtering favors common, less inventive samples.

**Mixing Fresh Human Data:** Holding out 60% human data and mixing 10% fresh human data at each iteration only "minimally mitigates" the observed decrease.

**Conclusion:** Neither strategy effectively prevents diversity loss.

---

## 5. LIMITATIONS

- **Language scope:** English-only. "Linguistic diversity metrics may not perform optimally for languages apart from English" due to language-specific tokenization and dependency parsing reliance.
- **Model scale:** OPT-350M used (avoiding OPT-125M due to quality degradation across 6 iterations). "Could not perform experiments on an extensive range of models." Story generation alone required ~700 GPU hours on NVIDIA RTX A6000.
- **Realistic web setting:** Infeasibility of true web-scale simulation. Synthetic web text dataset construction poses copyright issues; no reliable LLM-detection algorithm exists.

---

## 6. EXPERIMENTAL SETUP

- **Base model:** OPT-350M
- **Optimizer:** AdamW
- **Hardware:** 2× NVIDIA RTX A6000 GPUs
- **Training:** 5 epochs per iteration
- **Perplexity monitoring:** All results kept <20 to ensure output quality

---

## 7. FIGURES AND TABLES

**Table 1 (Model Outputs Example):** Scientific abstract generation across iterations. By Iteration 5, model begins generating artificial URLs and code links repeatedly, mimicking high-probability training patterns from ACL papers.

**Figure 1 (Recursive Process):** Diagram of cycle: Data(0)→Model(1)→Data(1)→Model(2)...

**Figure 2 (Mitigation Strategies):** Distinct-3 and syntactic diversity tracking across filtering and mixed-human settings. Shows minimal improvement.

**Figure 3 (Word Frequency Histograms):** "Diminishing presence of low-frequency, 'unique' words" across iterations, pattern intensifying over time.

**Figure 4 (Syntactic Embeddings t-SNE):** Increasing spatial compactness of dependency tree embeddings across iterations.

**Figure 5 (Semantic Embeddings t-SNE):** Reduced dispersion in sentence embeddings, less pronounced than syntactic changes.

---

## 8. DATASETS AND LICENSES

- XL-SUM: CC BY-NC-SA 4.0
- ACL Anthology: CC BY-NC-SA 4.0
- WritingPrompts: MIT license

No personally identifiable information involved.

---

## 9. BASELINES

No external baseline models compared — the study is intrinsic: each iteration's outputs are compared against human-generated text (the ground-truth distribution) and against prior iteration outputs. The "baseline" is Generation 0 (human data).

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "96b972df-5af0-45ec-94f6-983276f65901",
  "isSidechain": true,
  "agentId": "a9d9703ccc0d5ee09",
  "requestId": "req_011CbE2E9r5fRzbMjEgvj7fb",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "2bf260da-9980-4ec8-a3ea-b9422e833228",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/.claude/sessions/distiller_3275b75a",
  "sessionId": "e1199c41-0624-4bbe-a3c3-3e8c7b3fc1ae",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_0142ihY5zGMXpFPhmX1W9tr2",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2313,
      "cache_read_input_tokens": 18634,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2313,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 1,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null
  }
}
```

</details>

---
