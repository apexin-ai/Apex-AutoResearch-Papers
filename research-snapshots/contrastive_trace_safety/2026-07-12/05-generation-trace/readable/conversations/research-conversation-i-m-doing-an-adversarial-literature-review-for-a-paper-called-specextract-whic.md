# Research conversation: I'm doing an adversarial literature review for a paper called "SpecExtract" which proposes: training a model to extract 

**Layer Selection Sensitivity in Hidden-State Safety Probes for Reasoning Models (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 47
- **Recorded user turns:** 1
- **Tool calls:** 20
- **Original source:** `logs/chats/exported-trajectories/account-1/agent-a3d6359a710b9a6ec.jsonl`
- **Structured JSON:** [`39a5112deee64b9716c9.json`](../../sessions/39/39a5112deee64b9716c9.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

47 recorded events

### User

_source line 1 · 2026-05-10T06:57:27.900Z_

I'm doing an adversarial literature review for a paper called "SpecExtract" which proposes: training a model to extract structured behavioral specifications from bug report text (stack traces, error messages, test assertions) to guide automated program repair. The model extracts: affected interface, observed behavior, expected behavior, and behavioral delta. It's trained on SWE-bench test patch assertions.

Please search for concurrent or competing work that the authors might have missed:

1. **Bug report information extraction / specification extraction**:
   - Search: "bug report" "specification extraction" NLP 2025 2026
   - Search: site:arxiv.org structured information extraction bug reports program repair 2025

2. **Issue-to-spec methods for code repair**:
   - Search: site:arxiv.org "issue description" specification "program repair" 2025 2026
   - Search: "behavioral specification" "bug report" automatic extraction 2026

3. **Test assertion-based specification mining**:
   - Search: "test assertions" specification mining program repair 2025 2026
   - Search: site:arxiv.org test patch specification behavioral constraints repair

4. **SWE-bench training data approaches**:
   - Search: site:arxiv.org SWE-bench training data specification structured 2025 2026
   - Search: SWE-bench fine-tuning specifications behavioral extraction 2026

5. **Information extraction for debugging/repair**:
   - Search: site:arxiv.org "stack trace" NLP information extraction repair 2025
   - Search: site:paperswithcode.com bug report structured extraction program repair

Report any papers that directly overlap with SpecExtract's approach of (a) extracting structured specs from bug report text, (b) using test assertions as training signal for spec learning, or (c) injecting specs into fault localization or patch generation pipelines.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "97188be6-5245-47ba-9011-c98eaa31631a",
  "agentId": "a3d6359a710b9a6ec",
  "type": "user",
  "uuid": "741434a9-a3d0-44c3-8cfe-7a8cd621d0c3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "78f395f4-5c6b-48f5-b7df-f42fdf4d4c8a",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 2 · 2026-05-10T06:57:29.155Z_

I'll conduct a thorough adversarial literature review for SpecExtract by searching for competing work across multiple dimensions. Let me run these searches systematically.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "741434a9-a3d0-44c3-8cfe-7a8cd621d0c3",
  "isSidechain": true,
  "agentId": "a3d6359a710b9a6ec",
  "requestId": "req_011CatTEfX7C2ZBJkcBZWSqg",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "a7d74b30-6a76-4c41-b0a4-2c2c8509baca",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "78f395f4-5c6b-48f5-b7df-f42fdf4d4c8a",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01JzKqimLyqiY7oGXJHTntR2",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 852,
      "cache_read_input_tokens": 16155,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 852,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 3,
      "service_tier": "standard",
      "inference_geo": "not_available"
    }
  }
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-10T06:57:29.341Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01KyNSTWvcuoNkhoPZX7uX2s`</summary>

```json
{
  "query": "bug report specification extraction NLP 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a7d74b30-6a76-4c41-b0a4-2c2c8509baca",
  "isSidechain": true,
  "agentId": "a3d6359a710b9a6ec",
  "requestId": "req_011CatTEfX7C2ZBJkcBZWSqg",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "3e1c33ae-0e43-4300-85bc-aedc29012d9a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "78f395f4-5c6b-48f5-b7df-f42fdf4d4c8a",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01JzKqimLyqiY7oGXJHTntR2",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 852,
      "cache_read_input_tokens": 16155,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 852,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 3,
      "service_tier": "standard",
      "inference_geo": "not_available"
    }
  }
}
```

</details>

---

### Tool call

_source line 4 · 2026-05-10T06:57:29.712Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01Jxu2MtrBESdzV7ErkHro3a`</summary>

```json
{
  "query": "site:arxiv.org structured information extraction bug reports program repair 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3e1c33ae-0e43-4300-85bc-aedc29012d9a",
  "isSidechain": true,
  "agentId": "a3d6359a710b9a6ec",
  "requestId": "req_011CatTEfX7C2ZBJkcBZWSqg",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "c7a56d4f-89a4-46fa-9e2c-93f7ca9a9c53",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "78f395f4-5c6b-48f5-b7df-f42fdf4d4c8a",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01JzKqimLyqiY7oGXJHTntR2",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 852,
      "cache_read_input_tokens": 16155,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 852,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 3,
      "service_tier": "standard",
      "inference_geo": "not_available"
    }
  }
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-10T06:57:29.716Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01AhEebEs4fS9Br6Z9k3ia8j`</summary>

```json
{
  "query": "issue description specification program repair 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c7a56d4f-89a4-46fa-9e2c-93f7ca9a9c53",
  "isSidechain": true,
  "agentId": "a3d6359a710b9a6ec",
  "requestId": "req_011CatTEfX7C2ZBJkcBZWSqg",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "01252178-b4a9-4339-84b5-3ab074c932c4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "78f395f4-5c6b-48f5-b7df-f42fdf4d4c8a",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01JzKqimLyqiY7oGXJHTntR2",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 852,
      "cache_read_input_tokens": 16155,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 852,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 3,
      "service_tier": "standard",
      "inference_geo": "not_available"
    }
  }
}
```

</details>

---

### Tool call

_source line 6 · 2026-05-10T06:57:29.719Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01NmJW7KvEkdVAWYWc4TPNLM`</summary>

```json
{
  "query": "behavioral specification bug report automatic extraction 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "01252178-b4a9-4339-84b5-3ab074c932c4",
  "isSidechain": true,
  "agentId": "a3d6359a710b9a6ec",
  "requestId": "req_011CatTEfX7C2ZBJkcBZWSqg",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "d12b2147-6688-4b2a-8c81-c16f5fb402be",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "78f395f4-5c6b-48f5-b7df-f42fdf4d4c8a",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01JzKqimLyqiY7oGXJHTntR2",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 852,
      "cache_read_input_tokens": 16155,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 852,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 3,
      "service_tier": "standard",
      "inference_geo": "not_available"
    }
  }
}
```

</details>

---

### Tool result

_source line 7 · 2026-05-10T06:57:36.632Z_

<details><summary>↩ Tool result · `toolu_01AhEebEs4fS9Br6Z9k3ia8j`</summary>

```text
Web search results for query: "issue description specification program repair 2025 2026"

Links: [{"title":"WINTER 2025 VOLUME #26, ISSUE 4 INSPECTION UPDATE Program News","url":"https://app.mavehiclecheck.com/newsletters/newsletters/InspectionUpdate_Volume26-Issue04_Winter2025.pdf"},{"title":"Windows Server 2025 Known Issues and Workarounds – April 22, 2026","url":"https://www.askvg.com/windows-server-2025-known-issues-and-workarounds/"},{"title":"An empirical evaluation of pre-trained large language models for repairing declarative formal specifications | Empirical Software Engineering | Springer Nature Link","url":"https://link.springer.com/article/10.1007/s10664-025-10687-1"},{"title":"March 2025 National Operations & Maintenance Specification","url":"https://www.gsa.gov/system/files?file=2025+National+OM+Spec-030525.pdf"},{"title":"Gradient-Based Program Repair: Fixing Bugs in Continuous Program Spaces","url":"https://arxiv.org/html/2505.17703v3"},{"title":"FDL: Forum on specification and Design Languages 2027 2026 2025 ...","url":"http://www.wikicfp.com/cfp/program?id=1024"},{"title":"arXiv:2506.08311v1 [cs.SE] 10 Jun 2025","url":"https://arxiv.org/pdf/2506.08311"},{"title":"Right to Repair 2026: Complete Advocacy Guide for Tech Repair","url":"https://techcareassociation.org/2025/12/15/right-to-repair-2026-action-guide/"},{"title":"The 2025-2026 State of Heavy-Duty Repair | Construction Equipment","url":"https://www.constructionequipment.com/sponsored/whitepaper/55368327/the-2025-2026-state-of-heavy-duty-repair"},{"title":"Towards practical program repair with on-demand candidate generation | Proceedings of the 40th International Conference on Software Engineering","url":"https://dl.acm.org/doi/10.1145/3180155.3180245"}]

Based on the search results, here's what I found related to your query about issue description, specification, and program repair in 2025-2026:

## Academic Research on Program Repair

Automatic Program Repair (APR) has garnered significant attention as a practical research domain focused on automatically fixing bugs in programs. While existing APR techniques primarily target imperative programming languages like C and Java, there is a growing need for effective solutions applicable to declarative software specification languages. Research has investigated the capacity of Large Language Models (LLMs) to repair declarative specifications in Alloy, a declarative formal language used for software specification.

Recent years have seen dramatic improvements in the quality and complexity of patches thanks to learning-based program repair, with frontier LLMs making progress on benchmarks like SWE-Bench and RepairBench, which have demonstrated that real-world bugs can be fixed automatically.

## Program Repair Using Issue Descriptions

Tasks involve natural language issue descriptions, requiring the generation of candidate patches that resolve the issue. Evaluation is conducted via test execution, including fail-to-pass tests that confirm issue resolution and pass-to-pass tests that check for regression safety.

## 2026 Developments

The 2026 IEEE/ACM 46th International Conference on Software Engineering is scheduled for April 10-19, 2026 in Rio de Janeiro, Brazil.

The search results show active research and development in automated program repair, with increasing sophistication in handling complex bug repairs using specification and issue descriptions as input for the repair process.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "01252178-b4a9-4339-84b5-3ab074c932c4",
  "isSidechain": true,
  "promptId": "97188be6-5245-47ba-9011-c98eaa31631a",
  "agentId": "a3d6359a710b9a6ec",
  "type": "user",
  "uuid": "cc4a7cee-f9c2-4383-ac6e-fcd4b2deb5f2",
  "sourceToolAssistantUUID": "01252178-b4a9-4339-84b5-3ab074c932c4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "78f395f4-5c6b-48f5-b7df-f42fdf4d4c8a",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-10T06:57:36.654Z_

<details><summary>↩ Tool result · `toolu_01KyNSTWvcuoNkhoPZX7uX2s`</summary>

```text
Web search results for query: "bug report specification extraction NLP 2025 2026"

Links: [{"title":"GitHub - kenneym/bug_classification_research: An NLP Model used for automated assignment of bug reports to the relevant engineering team. Utilizes a novel confidence bounding approach - Monte Carlo Dropout, and assigns underconfident predictions to a queue for human review. Built for Pegasystems Inc.","url":"https://github.com/kenneym/bug_classification_research"},{"title":"Past, Present, and Future of Bug Tracking in the Generative AI Era","url":"https://arxiv.org/html/2510.08005v2"},{"title":"Identifying non-natural language artifacts in bug reports Thomas Hirsch","url":"https://arxiv.org/pdf/2110.01336"},{"title":"Detecting non-natural language artifacts for de-noising bug reports | Automated Software Engineering","url":"https://link.springer.com/article/10.1007/s10515-022-00350-0"},{"title":"Research Paper on Enhanced Bug Report Classification using XGBoost and Transformer-based NLP Models | IJIRT.org apply for ugc care approved journal, UGC Approved Journal, ugc approved journal, ugc approved list of journal, ugc care journal, care journal, UGC-CARE list, New UGC-CARE Reference List, UGC CARE Journals, ugc care list of journal, ugc care list 2020, ugc care approved journal, ugc care list 2020, new ugc approved journal in 2020,Low cost research journal, Online international research journal, Pe","url":"https://ijirt.org/article?manuscript=175786"},{"title":"[2503.20578] LLPut: Investigating Large Language Models for Bug Report-Based Input Generation","url":"https://arxiv.org/abs/2503.20578"},{"title":"Learning Software Bug Reports: A Systematic Literature ...","url":"https://dl.acm.org/doi/pdf/10.1145/3750040"},{"title":"[2212.06334] Auto-labelling of Bug Report using Natural Language Processing","url":"https://arxiv.org/abs/2212.06334"},{"title":"GitHub - logpai/bughub: A collection of free-text bug reports for duplicate issue identification · GitHub","url":"https://github.com/logpai/bughub"},{"title":"GitHub - somillko/Bug-Report-Classification: Determining the type of Bug so that relevant developer can be applied.","url":"https://github.com/somillko/Bug-Report-Classification"}]

I've completed the web search for "bug report specification extraction NLP 2025 2026". Here are the key findings from the results:

## Recent Research on Bug Report Analysis with NLP (2025-2026)

**Recent Developments:**

AI agents now enhance bug reports by filling missing details or rephrasing ambiguous descriptions, with recent research published in 2025-2026 focusing on this area. Recent studies have leveraged LLM capabilities to enhance bug report quality, with LLM-driven approaches that can semantically analyze bug reports and detect missing fields.

**Extraction Techniques:**

Bug reports are written in natural language, and prior research has leveraged various NLP techniques for automated input extraction, with an important research question being how effectively generative LLMs can extract failure-inducing inputs from bug reports. Recent research proposes techniques to evaluate the performance of open-source generative LLMs like LLaMA, Qwen, and Qwen-Coder in extracting relevant inputs from bug reports.

**Classification and Analysis:**

Recent work in 2025 has focused on enhanced bug report classification using XGBoost and transformer-based NLP models. Modern research bridges traditional ML techniques with deep learning and NLP approaches for bug report analysis, with CNN, LSTM, and k-NN becoming the leading algorithms and a marked increase in deep learning techniques from 2020 to 2023.

**Bug Report Enhancement:**

Critical information such as system state, error messages, and execution logs can be added by AI agents, which can also ensure steps-to-reproduce are complete.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "3e1c33ae-0e43-4300-85bc-aedc29012d9a",
  "isSidechain": true,
  "promptId": "97188be6-5245-47ba-9011-c98eaa31631a",
  "agentId": "a3d6359a710b9a6ec",
  "type": "user",
  "uuid": "5ebd7788-f049-48f2-acfa-966a1509828e",
  "sourceToolAssistantUUID": "3e1c33ae-0e43-4300-85bc-aedc29012d9a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "78f395f4-5c6b-48f5-b7df-f42fdf4d4c8a",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 9 · 2026-05-10T06:57:37.173Z_

<details><summary>↩ Tool result · `toolu_01NmJW7KvEkdVAWYWc4TPNLM`</summary>

```text
Web search results for query: "behavioral specification bug report automatic extraction 2026"

Links: [{"title":"CodeSpecBench: Benchmarking LLMs for Executable Behavioral Specification Generation","url":"https://arxiv.org/html/2604.12268v1"},{"title":"Past, Present, and Future of Bug Tracking in the Generative AI Era","url":"https://arxiv.org/html/2510.08005v2"},{"title":"Uncovering the iceberg from the tip: Generating API Speciﬁcations for Bug","url":"https://www.ndss-symposium.org/wp-content/uploads/2025-2001-paper.pdf"},{"title":"Learning Software Bug Reports: A Systematic Literature ...","url":"https://dl.acm.org/doi/pdf/10.1145/3750040"},{"title":"5 Best Bug Finder Tools in 2025 | Bug Tracking Blog @ Bird Eats Bug","url":"https://birdeatsbug.com/blog/best-bug-finder-tools"},{"title":"ChatBR: Automated assessment and improvement of bug ...","url":"https://dl.acm.org/doi/pdf/10.1145/3691620.3695518"},{"title":"Feedback-Driven Automated Whole Bug Report Reproduction for Android Apps","url":"https://zhaoxu-zhang.github.io/files/issta2024.pdf"},{"title":"Current Trends and Insights in Bug Reporting: A Systematic Literature Review","url":"https://www.scitepress.org/Papers/2026/144543/144543.pdf"},{"title":"17 Excellent Open Source Bug Tracking Tools in 2026","url":"https://usersnap.com/blog/open-source-bug-tracking/"},{"title":"Automated bug report field reassignment and refinement prediction","url":"https://research.monash.edu/en/publications/automated-bug-report-field-reassignment-and-refinement-prediction/"}]

Based on the web search results, I found several relevant papers and resources related to behavioral specification and bug report extraction from 2026:

## Key Findings:

**CodeSpecBench (2026)**: CodeSpecBench requires models to understand repository structure, module dependencies, and broader execution behavior when generating specifications, and for repository-level evaluation, it adopts SWE-bench Verified, which provides challenging real-world software issues grounded in large, multi-file Python repositories. The best model on CodeSpecBench attains only a 20.2% pass rate on repository-level tasks, and specification generation is substantially more challenging than code generation, indicating that strong coding performance does not necessarily reflect deep understanding of intended program semantics.

**Bug Tracking in the AI Era (2026)**: Recent studies have leveraged LLM capabilities to enhance bug report quality through semantic analysis to detect missing fields and suggest enhancements for incomplete or ambiguous descriptions. Techniques have emerged to extract reproduction steps from natural language descriptions.

**ChatBR Approach**: ChatBR is a novel approach based on ChatGPT to improve the accuracy of assessing bug reports by adopting pre-trained models that rely on the attention mechanism to capture the deep semantics of natural language context effectively.

**Automated Bug Report Enhancement**: Agents propose enhancements to bug reports, filling missing details or rephrasing ambiguous descriptions.

These resources show active research in 2026 on automating the extraction and generation of behavioral specifications from bug reports using advanced language models and machine learning approaches.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d12b2147-6688-4b2a-8c81-c16f5fb402be",
  "isSidechain": true,
  "promptId": "97188be6-5245-47ba-9011-c98eaa31631a",
  "agentId": "a3d6359a710b9a6ec",
  "type": "user",
  "uuid": "0399322e-e0ab-4b89-8c8a-4c48d4a8e8a4",
  "sourceToolAssistantUUID": "d12b2147-6688-4b2a-8c81-c16f5fb402be",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "78f395f4-5c6b-48f5-b7df-f42fdf4d4c8a",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-10T06:57:37.347Z_

<details><summary>↩ Tool result · `toolu_01Jxu2MtrBESdzV7ErkHro3a`</summary>

```text
Web search results for query: "site:arxiv.org structured information extraction bug reports program repair 2025"

Links: [{"title":"Repeton: Structured Bug Repair with ReAct-Guided Patch-and-Test Cycles","url":"https://arxiv.org/html/2506.08173"},{"title":"Better Automatic Program Repair by Using Bug Reports and Tests Together","url":"https://arxiv.org/pdf/2011.08340"},{"title":"Agentic Bug Reproduction for Effective Automated Program Repair at Google","url":"https://arxiv.org/html/2502.01821v2"},{"title":"Past, Present, and Future of Bug Tracking in the Generative AI Era","url":"https://arxiv.org/pdf/2510.08005"},{"title":"[2304.12494] BugMentor: Generating Answers to Follow-up Questions from Software Bug Reports using Structured Information Retrieval and Neural Text Generation","url":"https://arxiv.org/abs/2304.12494"},{"title":"Knowledge-Enhanced Program Repair for Data Science Code","url":"https://arxiv.org/html/2502.09771v1"},{"title":"[2504.18804] Can We Enhance Bug Report Quality Using LLMs?: An Empirical Study of LLM-Based Bug Report Generation","url":"https://arxiv.org/abs/2504.18804"},{"title":"From Bugs to Benchmarks: A Comprehensive Survey of Software Defect Datasets","url":"https://arxiv.org/pdf/2504.17977"},{"title":"A Survey of LLM-based Automated Program Repair: Taxonomies, Design Paradigms, and Applications","url":"https://arxiv.org/html/2506.23749v1"},{"title":"Explaining Software Bugs Leveraging Code Structures in ...","url":"https://arxiv.org/pdf/2212.04584"}]

I've successfully performed the web search with your query. Here are the most relevant results from arxiv.org related to structured information extraction, bug reports, and program repair from 2025:

## Key Results:

1. **Repeton: Structured Bug Repair** - A method that operates through a structured patch-and-test pipeline, iteratively diagnosing issues, proposing code changes, and validating each patch through automated testing, guided by lightweight heuristics and development tools. Published June 2025.

2. **Agentic Bug Reproduction for Automated Program Repair** - A dataset constructed via automated extraction and filtering phases as well as manual curation, containing bugs from a wide array of Google projects spanning seven programming languages: Java, C++, Go, Python, Kotlin, Dart, and TypeScript. Published March 2025.

3. **Knowledge-Enhanced Program Repair for Data Science Code** - A method that organizes information obtained from previous steps into a structured prompt fed to an LLM for code repair, with the final prompt including problem description, incorrect code, stderr information, API knowledge, bug knowledge, fact-checking, and response format. Published February 2025.

4. **LLM-Based Bug Report Generation** - Research highlighting the potential of instruction fine-tuning in automating structured bug report generation, reducing manual effort for developers and streamlining the software maintenance process. Published April 2025.

5. **Survey of LLM-based Automated Program Repair** - A survey discussing how retrieval-augmented generation can retrieve repository structure information, security-fix templates, or domain-specific API knowledge encoded in a graph. Published June 2025.

These papers cover various aspects of using structured information extraction techniques for automated bug analysis and program repair in 2025.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c7a56d4f-89a4-46fa-9e2c-93f7ca9a9c53",
  "isSidechain": true,
  "promptId": "97188be6-5245-47ba-9011-c98eaa31631a",
  "agentId": "a3d6359a710b9a6ec",
  "type": "user",
  "uuid": "c22341fd-5c58-4fb7-b156-93dbdf2bd6b8",
  "sourceToolAssistantUUID": "c7a56d4f-89a4-46fa-9e2c-93f7ca9a9c53",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "78f395f4-5c6b-48f5-b7df-f42fdf4d4c8a",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 11 · 2026-05-10T06:57:40.194Z_

Excellent start. Let me continue with more targeted searches on test assertion-based approaches and SWE-bench specific work.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c22341fd-5c58-4fb7-b156-93dbdf2bd6b8",
  "isSidechain": true,
  "agentId": "a3d6359a710b9a6ec",
  "requestId": "req_011CatTFMuEWEvHZtisoLBPK",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "815b54a6-23dd-4d1b-916f-3e3290c5ec2f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "78f395f4-5c6b-48f5-b7df-f42fdf4d4c8a",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01WdBdMpnLmmUadw67yuigqK",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1792,
      "cache_creation_input_tokens": 2925,
      "cache_read_input_tokens": 17007,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2925,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 3,
      "service_tier": "standard",
      "inference_geo": "not_available"
    }
  }
}
```

</details>

---

### Tool call

_source line 12 · 2026-05-10T06:57:40.682Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01HMRJXffZXMkCfbf4zyQZqP`</summary>

```json
{
  "query": "test assertions specification mining program repair 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "815b54a6-23dd-4d1b-916f-3e3290c5ec2f",
  "isSidechain": true,
  "agentId": "a3d6359a710b9a6ec",
  "requestId": "req_011CatTFMuEWEvHZtisoLBPK",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "1bcc5227-79e6-4cf7-bdbd-3a8cbfb7c300",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "78f395f4-5c6b-48f5-b7df-f42fdf4d4c8a",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01WdBdMpnLmmUadw67yuigqK",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1792,
      "cache_creation_input_tokens": 2925,
      "cache_read_input_tokens": 17007,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2925,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 3,
      "service_tier": "standard",
      "inference_geo": "not_available"
    }
  }
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-10T06:57:40.895Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01NoGhuWAqSWqdjhZLuL6MCF`</summary>

```json
{
  "query": "site:arxiv.org test patch specification behavioral constraints repair"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1bcc5227-79e6-4cf7-bdbd-3a8cbfb7c300",
  "isSidechain": true,
  "agentId": "a3d6359a710b9a6ec",
  "requestId": "req_011CatTFMuEWEvHZtisoLBPK",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "06c17821-55ce-41f1-9c55-754d7e50181a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "78f395f4-5c6b-48f5-b7df-f42fdf4d4c8a",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01WdBdMpnLmmUadw67yuigqK",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1792,
      "cache_creation_input_tokens": 2925,
      "cache_read_input_tokens": 17007,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2925,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 3,
      "service_tier": "standard",
      "inference_geo": "not_available"
    }
  }
}
```

</details>

---

### Tool call

_source line 14 · 2026-05-10T06:57:41.069Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01UGiWh4xN4LoJ3QmEGb6C3v`</summary>

```json
{
  "query": "site:arxiv.org SWE-bench training data specification structured 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "06c17821-55ce-41f1-9c55-754d7e50181a",
  "isSidechain": true,
  "agentId": "a3d6359a710b9a6ec",
  "requestId": "req_011CatTFMuEWEvHZtisoLBPK",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "c05b6250-dec9-4ec6-823b-eb2d27460ec4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "78f395f4-5c6b-48f5-b7df-f42fdf4d4c8a",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01WdBdMpnLmmUadw67yuigqK",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1792,
      "cache_creation_input_tokens": 2925,
      "cache_read_input_tokens": 17007,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2925,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 3,
      "service_tier": "standard",
      "inference_geo": "not_available"
    }
  }
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-10T06:57:41.233Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_0152pscyqtKWZSMYghQPinCr`</summary>

```json
{
  "query": "stack trace NLP information extraction program repair 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c05b6250-dec9-4ec6-823b-eb2d27460ec4",
  "isSidechain": true,
  "agentId": "a3d6359a710b9a6ec",
  "requestId": "req_011CatTFMuEWEvHZtisoLBPK",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "9874ab7f-9301-4253-8991-c9f9ac47ccef",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "78f395f4-5c6b-48f5-b7df-f42fdf4d4c8a",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01WdBdMpnLmmUadw67yuigqK",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1792,
      "cache_creation_input_tokens": 2925,
      "cache_read_input_tokens": 17007,
      "output_tokens": 236,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2925
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1792,
          "output_tokens": 236,
          "cache_read_input_tokens": 17007,
          "cache_creation_input_tokens": 2925,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2925,
            "ephemeral_1h_input_tokens": 0
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    }
  }
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-10T06:57:48.813Z_

<details><summary>↩ Tool result · `toolu_01UGiWh4xN4LoJ3QmEGb6C3v`</summary>

```text
Web search results for query: "site:arxiv.org SWE-bench training data specification structured 2025 2026"

Links: [{"title":"SWE Context Bench: A Benchmark for Context Learning in Coding","url":"https://arxiv.org/html/2602.08316"},{"title":"SWE Context Bench: A Benchmark for Context Learning in Coding Jared Zhu","url":"https://www.arxiv.org/pdf/2602.08316"},{"title":"SWE-rebench V2: Language-Agnostic SWE Task Collection at Scale","url":"https://arxiv.org/html/2602.23866"},{"title":"SWE-rebench: An Automated Pipeline for Task Collection ...","url":"https://arxiv.org/pdf/2505.20411"},{"title":"SWE-bench Goes Live!","url":"https://arxiv.org/html/2505.23419v2"},{"title":"What’s in a Benchmark? The Case of SWE-Bench in Automated Program Repair","url":"https://arxiv.org/pdf/2602.04449"},{"title":"The SWE-Bench Illusion: When State-of-the-Art LLMs Remember Instead of Reason","url":"https://arxiv.org/html/2506.12286v3"},{"title":"2026-2-12 SWE-AGI: Benchmarking Specification-Driven Software","url":"https://www.arxiv.org/pdf/2602.09447"},{"title":"SWE-Bench 5G: Benchmarking AI Coding Agents on Telecom Network Engineering Tasks","url":"https://arxiv.org/html/2604.26278"},{"title":"[2310.06770] SWE-bench: Can Language Models Resolve Real-World GitHub Issues?","url":"https://arxiv.org/abs/2310.06770"}]

Based on the web search results, here are the relevant findings about SWE-bench training data specifications from arxiv.org in 2025-2026:

## Key Results

Recent automated pipelines such as SWE-rebench, SetUpAgent, SWE-bench-Live, SWE-Factory, and SWE-Bench++ have improved scalability by automating environment setup and instance validation.

### SWE-rebench V2: Language-Agnostic Approach
SWE-bench Pro adds structured requirements and explicit interface specifications, reducing false negatives where models produce functionally correct fixes but misname symbols expected by tests.

### SWE-bench-Live Dataset
SWE-bench-Live adopts the same task definition as SWE-bench and introduces a novel, fully automated pipeline that enables scalable and continuously updatable benchmark construction, with the initial release consisting of 1,319 task instances created between January 2024 and April 2025, spanning 93 real-world repositories.

### SWE-AGI Benchmark
Each SWE-AGI task provides normative specifications (specs/), an explicit task statement (TASK.md), and a visible public test subset for local iteration, while benchmark scoring is performed solely on final submissions evaluated against hidden private tests.

### Data Structure Details
Context trajectories are parsed to extract a structured representation comprising a high-level summary, the complete user/assistant message history, and associated metadata (repository name, instance ID).

The search results show significant evolution in SWE-bench training data specifications during 2025-2026, with emphasis on automation, scalability, structured specifications, and deterministic testing approaches.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c05b6250-dec9-4ec6-823b-eb2d27460ec4",
  "isSidechain": true,
  "promptId": "97188be6-5245-47ba-9011-c98eaa31631a",
  "agentId": "a3d6359a710b9a6ec",
  "type": "user",
  "uuid": "21bb1f8d-48bd-4af6-9910-07a9256f258f",
  "sourceToolAssistantUUID": "c05b6250-dec9-4ec6-823b-eb2d27460ec4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "78f395f4-5c6b-48f5-b7df-f42fdf4d4c8a",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 17 · 2026-05-10T06:57:48.873Z_

<details><summary>↩ Tool result · `toolu_01NoGhuWAqSWqdjhZLuL6MCF`</summary>

```text
Web search results for query: "site:arxiv.org test patch specification behavioral constraints repair"

Links: [{"title":"Beyond Fixed Tests: Repository-Level Issue Resolution as Coevolution of Code and Behavioral Constraints","url":"https://arxiv.org/html/2604.04580"},{"title":"Identifying Patch Correctness in Test-Based Program Repair","url":"https://arxiv.org/pdf/1706.09120"},{"title":"Specification Vibing for Automated Program Repair","url":"https://arxiv.org/html/2602.08263"},{"title":"[2008.02944] Evaluating Representation Learning of Code Changes for Predicting Patch Correctness in Program Repair","url":"https://ar5iv.labs.arxiv.org/html/2008.02944"},{"title":"PathFix: Automated Program Repair with Expected Path","url":"https://arxiv.org/html/2510.14341"},{"title":"ComPass: Contrastive Learning for Automated Patch Correctness Assessment in Program Repair","url":"https://arxiv.org/html/2602.07561"},{"title":"When Automated Program Repair Meets Regression Testing – An Extensive Study on 2 Million Patches","url":"https://arxiv.org/html/2105.07311"},{"title":"arXiv:2105.07311v1 [cs.SE] 15 May 2021","url":"https://arxiv.org/pdf/2105.07311v1"},{"title":"Patch Validation in Automated Vulnerability Repair","url":"https://arxiv.org/pdf/2603.06858"},{"title":"Are Benchmark Tests Strong Enough? Mutation-Guided Diagnosis and Augmentation of Regression Suites","url":"https://arxiv.org/html/2604.01518v1"}]

I found several relevant papers on arXiv related to test patches, specifications, behavioral constraints, and repair. Here are the key results:

## Top Results

1. **"Beyond Fixed Tests: Repository-Level Issue Resolution as Coevolution of Code and Behavioral Constraints"** (April 2026)
   - Proposes Agent-CoEvo, a coevolutionary multi-agent framework that jointly explores code patches and test patches, modeling tests as dynamic constraints that both guide and are revised by the repair process.
   - Suggests that enabling repair agents to revise behavioral constraints during search is critical for reliable issue resolution.

2. **"Specification Vibing for Automated Program Repair"** (February 2026)
   - VibeRepair transforms buggy code and failing test cases into a test-based flawed behavior specification, and through iterative interaction with validation failure feedback, the LLM accurately captures intended behavior and refines this behavior specification.

3. **"Are Benchmark Tests Strong Enough? Mutation-Guided Diagnosis and Augmentation of Regression Suites"** (April 2026)
   - STING framework uses semantically modified program variants to uncover weaknesses in test suites, requiring candidate tests to pass on the reference patch, fail on at least one surviving variant, and remain robust under behavior-preserving transformations.

4. **"Identifying Patch Correctness in Test-Based Program Repair"** (2018)
   - Addresses how to identify correct patches using dynamic information and test behavior analysis.

5. **"Patch Validation in Automated Vulnerability Repair"** (2026)
   - Discusses formal verification approaches that offer mathematically rigorous alternatives to test-suite based patch validation, with SemFix formulating repair requirements as constraints solved by SMT solvers.

These papers explore the intersection of test generation, patch correctness validation, and behavioral specification in automated program repair.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "06c17821-55ce-41f1-9c55-754d7e50181a",
  "isSidechain": true,
  "promptId": "97188be6-5245-47ba-9011-c98eaa31631a",
  "agentId": "a3d6359a710b9a6ec",
  "type": "user",
  "uuid": "2e522018-f736-460f-916e-480f21773c77",
  "sourceToolAssistantUUID": "06c17821-55ce-41f1-9c55-754d7e50181a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "78f395f4-5c6b-48f5-b7df-f42fdf4d4c8a",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-10T06:57:49.285Z_

<details><summary>↩ Tool result · `toolu_01HMRJXffZXMkCfbf4zyQZqP`</summary>

```text
Web search results for query: "test assertions specification mining program repair 2025 2026"

Links: [{"title":"Specification Mining for Verification | Download Scientific Diagram","url":"https://www.researchgate.net/figure/Specification-Mining-for-Verification_fig1_221059788"},{"title":"Mining specifications | Proceedings of the 29th ACM SIGPLAN-SIGACT symposium on Principles of programming languages","url":"https://dl.acm.org/doi/10.1145/503272.503275"},{"title":"WSDM: Web Search and Data Mining 2027 2026 2025 .. ...","url":"http://www.wikicfp.com/cfp/program?id=3158"},{"title":"Scalable Specification Mining for Verification and Diagnosis","url":"https://sites.bu.edu/depend/files/2017/02/specmine-dac10.pdf"},{"title":"On the Impact of Formal Verification on Software Development","url":"https://ranjitjhala.github.io/static/oopsla25-formal.pdf"},{"title":"Mining and Mineral Processing - PE Exam","url":"https://ncees.org/exams/pe-exam/mining-and-mineral-processing/"},{"title":"Your 2026 mobile mining improvement plan starts with an honest site diagnostic - Mining Doc","url":"https://www.miningdoc.tech/question/your-2026-mobile-mining-improvement-plan-starts-with-an-honest-site-diagnostic/"},{"title":"2026 Mining and Metals Industry Outlook | Deloitte Insights","url":"https://www.deloitte.com/us/en/insights/industry/mining-metals/mining-and-metals-industry-outlook.html"},{"title":"Predictive Maintenance in Underground Mining Equipment Using Artificial Intelligence","url":"https://www.mdpi.com/2673-4117/6/10/261"},{"title":"[1311.3414] Mining Software Repair Models for Reasoning on the Search Space of Automated Program Fixing","url":"https://arxiv.org/abs/1311.3414"}]

Based on the web search results, I found several relevant research areas related to test assertions, specification mining, and program repair from 2025-2026:

## Recent Research (2025-2026)

Recent work includes "NADA: Neural Acceptance-Driven Approximate Specification Mining" published in the Proceedings of the ACM on Software Engineering in June 2025, and "Constrained LTL Specification Learning from Examples" published at the IEEE/ACM 47th International Conference on Software Engineering in April 2025.

Additionally, there is "A Baseline Framework for the Qualification of LTL Specification Miners" presented at the 2025 Design, Automation & Test in Europe Conference in March 2025.

## Related Research Areas

The broader context of this research involves:

- Specification mining, which is the process of extracting specifications, either statically from the description of a system, or dynamically from its executions

- Tools like SAM (Scalable Assertion Miner) that efficiently mine non-trivial specifications and can handle designs with large numbers of signals

- Research on mining software repair models by analyzing bug fix transactions from software repositories and applying this knowledge to automated program repair

These areas represent active research in automated specification generation, formal verification, and program repair techniques.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "1bcc5227-79e6-4cf7-bdbd-3a8cbfb7c300",
  "isSidechain": true,
  "promptId": "97188be6-5245-47ba-9011-c98eaa31631a",
  "agentId": "a3d6359a710b9a6ec",
  "type": "user",
  "uuid": "ab006efc-4654-4184-b143-73d69db1449c",
  "sourceToolAssistantUUID": "1bcc5227-79e6-4cf7-bdbd-3a8cbfb7c300",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "78f395f4-5c6b-48f5-b7df-f42fdf4d4c8a",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 19 · 2026-05-10T06:57:49.991Z_

<details><summary>↩ Tool result · `toolu_0152pscyqtKWZSMYghQPinCr`</summary>

```text
Web search results for query: "stack trace NLP information extraction program repair 2025"

Links: [{"title":"GitHub - iSEngLab/AwesomeLLM4SE: [SCIS 2025] A Survey on Large Language Models for Software Engineering · GitHub","url":"https://github.com/iSEngLab/AwesomeLLM4SE"},{"title":"A Survey of LLM-based Automated Program Repair: Taxonomies, Design Paradigms, and Applications","url":"https://arxiv.org/html/2506.23749v1"},{"title":"Knowledge-Enhanced Program Repair for Data Science Code | Proceedings of the IEEE/ACM 47th International Conference on Software Engineering","url":"https://dl.acm.org/doi/10.1109/ICSE55347.2025.00246"},{"title":"Information Extraction in NLP - GeeksforGeeks","url":"https://www.geeksforgeeks.org/nlp/information-extraction-in-nlp/"},{"title":"RAGFix: Enhancing LLM Code Repair Using RAG and ...","url":"https://par.nsf.gov/servlets/purl/10570230"},{"title":"NLP Information Extraction: An Overview","url":"https://www.astera.com/type/blog/nlp-information-extraction/"},{"title":"The Natural Language Processing / Information Extraction Program (NLP/IE) | Institute for Health Informatics","url":"https://healthinformatics.umn.edu/natural-language-processing"},{"title":"information-extraction · GitHub Topics · GitHub","url":"https://github.com/topics/information-extraction"},{"title":"How To Implement Information Extraction Systems Made Simple","url":"https://spotintelligence.com/2023/10/10/information-extraction/"},{"title":"The Stanford NLP Group","url":"https://nlp.stanford.edu/software/openie.html"}]

Based on the search results, here's what I found about stack trace, NLP information extraction, and program repair in 2025:

## Stack Trace and Program Repair with NLP

RAGFix targets Python errors by mining a six-million-post Stack Overflow vector knowledge graph: after an initial failure, it extracts the stack trace, retrieves the most relevant discussions, summarizes them, and prepends the advice to a follow-up GPT-3.5 or Llama-3 prompt.

The approach demonstrates how NLP and information extraction techniques are being integrated into automated program repair systems. The methodology involves constructing a specialized database populated with technical solutions from Stack Overflow complemented with key extracted features of these posts, which are then used to inform and improve the LLM's performance in bug localization and code repair tasks, with an iterative feature extraction, search, and database expansion process.

## Recent Developments in 2025

FormHe combines an ASP solver with a fine-tuned LLM for student assignments, where the solver first computes Minimal Strongly Inconsistent Correction Subsets and other hints, identifying the rules that violate the reference specification, and these hints form a compact prompt for the LLM, which rewrites only the suspicious rules.

More broadly, the field is advancing with various techniques, including parameter-efficient fine-tuning that freezes most of the backbone and learns small adapter modules, and reinforcement learning fine-tuning that trains the model with execution or security rewards.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "9874ab7f-9301-4253-8991-c9f9ac47ccef",
  "isSidechain": true,
  "promptId": "97188be6-5245-47ba-9011-c98eaa31631a",
  "agentId": "a3d6359a710b9a6ec",
  "type": "user",
  "uuid": "7d845d0c-72a1-438a-b0b7-028cdcb77b6c",
  "sourceToolAssistantUUID": "9874ab7f-9301-4253-8991-c9f9ac47ccef",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "78f395f4-5c6b-48f5-b7df-f42fdf4d4c8a",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 20 · 2026-05-10T06:57:51.702Z_

Excellent results. Let me continue with a few more targeted searches for fine-tuning on specs, behavioral delta extraction, and Papers with Code resources.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7d845d0c-72a1-438a-b0b7-028cdcb77b6c",
  "isSidechain": true,
  "agentId": "a3d6359a710b9a6ec",
  "requestId": "req_011CatTGHzcJrfKpEvGii2Hm",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "0b1dbf20-e1a5-4644-9eaa-5683096e5be5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "78f395f4-5c6b-48f5-b7df-f42fdf4d4c8a",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_015xHKkvGXuPap8RzynY7j56",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 5592,
      "cache_read_input_tokens": 19932,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 5592,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 3,
      "service_tier": "standard",
      "inference_geo": "not_available"
    }
  }
}
```

</details>

---

### Tool call

_source line 21 · 2026-05-10T06:57:51.955Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_018FkkiS8cEmimC3pfqjrYVf`</summary>

```json
{
  "query": "SWE-bench fine-tuning specifications behavioral extraction 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0b1dbf20-e1a5-4644-9eaa-5683096e5be5",
  "isSidechain": true,
  "agentId": "a3d6359a710b9a6ec",
  "requestId": "req_011CatTGHzcJrfKpEvGii2Hm",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "af261f6f-e77e-4af6-a6d6-0350fc308c29",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "78f395f4-5c6b-48f5-b7df-f42fdf4d4c8a",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_015xHKkvGXuPap8RzynY7j56",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 5592,
      "cache_read_input_tokens": 19932,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 5592,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 3,
      "service_tier": "standard",
      "inference_geo": "not_available"
    }
  }
}
```

</details>

---

### Tool call

_source line 22 · 2026-05-10T06:57:52.529Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01MS9B9doKyUs6oNHEZqXDWn`</summary>

```json
{
  "query": "site:paperswithcode.com bug report structured extraction program repair"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "af261f6f-e77e-4af6-a6d6-0350fc308c29",
  "isSidechain": true,
  "agentId": "a3d6359a710b9a6ec",
  "requestId": "req_011CatTGHzcJrfKpEvGii2Hm",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "4e2ffd0f-f9fd-4993-9ff1-e2bc558d98aa",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "78f395f4-5c6b-48f5-b7df-f42fdf4d4c8a",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_015xHKkvGXuPap8RzynY7j56",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 5592,
      "cache_read_input_tokens": 19932,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 5592,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 3,
      "service_tier": "standard",
      "inference_geo": "not_available"
    }
  }
}
```

</details>

---

### Tool call

_source line 23 · 2026-05-10T06:57:52.541Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01VXsNVF6AU9JdKy53hEqXDD`</summary>

```json
{
  "query": "expected behavior observed behavior specification mining 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4e2ffd0f-f9fd-4993-9ff1-e2bc558d98aa",
  "isSidechain": true,
  "agentId": "a3d6359a710b9a6ec",
  "requestId": "req_011CatTGHzcJrfKpEvGii2Hm",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "c76db837-9255-4587-860f-b723bf096a9f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "78f395f4-5c6b-48f5-b7df-f42fdf4d4c8a",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_015xHKkvGXuPap8RzynY7j56",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 5592,
      "cache_read_input_tokens": 19932,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 5592,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 3,
      "service_tier": "standard",
      "inference_geo": "not_available"
    }
  }
}
```

</details>

---

### Tool call

_source line 24 · 2026-05-10T06:57:52.718Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01KquQeWFLqtdWXTVRPTZM97`</summary>

```json
{
  "query": "site:arxiv.org test failure error message specification extraction 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c76db837-9255-4587-860f-b723bf096a9f",
  "isSidechain": true,
  "agentId": "a3d6359a710b9a6ec",
  "requestId": "req_011CatTGHzcJrfKpEvGii2Hm",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "cd9e63e3-fa37-491d-83bd-24fca5793662",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "78f395f4-5c6b-48f5-b7df-f42fdf4d4c8a",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_015xHKkvGXuPap8RzynY7j56",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 5592,
      "cache_read_input_tokens": 19932,
      "output_tokens": 244,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 5592
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 7,
          "output_tokens": 244,
          "cache_read_input_tokens": 19932,
          "cache_creation_input_tokens": 5592,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 5592,
            "ephemeral_1h_input_tokens": 0
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    }
  }
}
```

</details>

---

### Tool result

_source line 25 · 2026-05-10T06:57:58.838Z_

<details><summary>↩ Tool result · `toolu_01MS9B9doKyUs6oNHEZqXDWn`</summary>

```text
Web search results for query: "site:paperswithcode.com bug report structured extraction program repair"

Links: [{"title":"iFixR: Bug Report driven Program Repair | Papers With Code","url":"https://cs.paperswithcode.com/paper/ifixr-bug-report-driven-program-repair"},{"title":"Program Repair | Papers With Code","url":"https://paperswithcode.com/task/program-repair/codeless?page=2"},{"title":"9 dataset results for Program Repair","url":"https://paperswithcode.com/datasets?page=1&task=program-repair"},{"title":"Paper page - Self-Supervised Bug Detection and Repair","url":"https://paperswithcode.com/paper/self-supervised-bug-detection-and-repair"},{"title":"Papers with Code - Applying CodeBERT for Automated Program Repair of Java Simple Bugs","url":"https://cs.paperswithcode.com/paper/applying-codebert-for-automated-program"},{"title":"Program Repair","url":"https://paperswithcode.com/task/program-repair"},{"title":"Papers with Code - Machine Learning Datasets","url":"https://paperswithcode.com/datasets?o=cited&task=program-repair&v=lst"},{"title":"Papers with Code - Neural Program Repair by Jointly Learning to Localize and Repair","url":"https://paperswithcode.com/paper/neural-program-repair-by-jointly-learning-to-1"},{"title":"DeepFix Benchmark (Program Repair)","url":"https://paperswithcode.com/sota/program-repair-on-deepfix"},{"title":"Papers with Code - Fault localization","url":"https://paperswithcode.com/task/fault-localization"}]

I've performed the web search with the query: `site:paperswithcode.com bug report structured extraction program repair`

The search results returned several relevant papers from Papers with Code related to program repair and bug reports:

1. **iFixR: Bug Report driven Program Repair** - A new repair pipeline driven by bug reports, which addresses the challenge that common assumptions on the existence of relevant test cases does not hold in practice for most development settings.

2. **Self-Supervised Bug Detection and Repair (BugLab)** - BugLab uses self-supervised learning to enhance bug detection and repair by co-training a detector and selector model.

3. **Neural Program Repair by Jointly Learning to Localize and Repair** - A model that jointly and directly localizes and repairs variable-misuse bugs using multi-headed pointer networks.

4. **Applying CodeBERT for Automated Program Repair of Java Simple Bugs** - A novel automated program repair approach based on CodeBERT, a transformer-based neural architecture pre-trained on large corpus of source code.

The search also revealed various datasets for program repair research, including the ManySStuBs4J corpus, a collection of simple fixes to Java bugs with single statement fixes classified into 16 syntactic templates.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "4e2ffd0f-f9fd-4993-9ff1-e2bc558d98aa",
  "isSidechain": true,
  "promptId": "97188be6-5245-47ba-9011-c98eaa31631a",
  "agentId": "a3d6359a710b9a6ec",
  "type": "user",
  "uuid": "ed9e2188-93c2-407a-85e2-469a9669e3fd",
  "sourceToolAssistantUUID": "4e2ffd0f-f9fd-4993-9ff1-e2bc558d98aa",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "78f395f4-5c6b-48f5-b7df-f42fdf4d4c8a",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 26 · 2026-05-10T06:57:58.987Z_

<details><summary>↩ Tool result · `toolu_018FkkiS8cEmimC3pfqjrYVf`</summary>

```text
Web search results for query: "SWE-bench fine-tuning specifications behavioral extraction 2026"

Links: [{"title":"SWE-bench Verified","url":"https://www.vals.ai/benchmarks/swebench"},{"title":"Introducing SWE-bench Verified | OpenAI","url":"https://openai.com/index/introducing-swe-bench-verified/"},{"title":"What’s in a Benchmark? The Case of SWE-Bench in Automated Program Repair","url":"https://arxiv.org/pdf/2602.04449"},{"title":"SWE-Bench++: A Framework for the Scalable Generation of Software Engineering Benchmarks from Open-Source Repositories","url":"https://arxiv.org/html/2512.17419v1"},{"title":"Overview - SWE-bench","url":"https://www.swebench.com/SWE-bench/"},{"title":"SWE-bench","url":"https://www.swebench.com/original.html"},{"title":"SWE-bench Verified | Epoch AI","url":"https://epoch.ai/benchmarks/swe-bench-verified"},{"title":"SWE-bench Leaderboard 2026: All Model Scores, Rankings & What They Actually Mean","url":"https://www.codeant.ai/blogs/swe-bench-scores"},{"title":"GitHub - SWE-bench/SWE-bench: SWE-bench: Can Language Models Resolve Real-world Github Issues? · GitHub","url":"https://github.com/SWE-bench/SWE-bench"},{"title":"SWE-Bench Pro Leaderboard (2026): Why 46% Beats 81%","url":"https://www.morphllm.com/swe-bench-pro"}]

Based on the search results, here's what I found about SWE-bench fine-tuning specifications and behavioral extraction in 2026:

## Fine-tuning on SWE-bench

Fine-tuning on SWE-Bench++ instances yields measurable improvements on the SWE-bench Multilingual benchmark. Approaches based solely on fine-tuned open-source LLMs tend to yield more modest precision but offer benefits in terms of transparency, reproducibility and adaptability.

## Behavioral Extraction and Specifications

Recent 2026 frameworks include detailed specifications for behavioral extraction. Requirements definition involves annotators creating specification lists grounded in unit tests and gold patches (the reference solution code), detailing expected behavior without prescribing implementation, and interface specification documents class and function signatures to prevent false negatives from naming mismatches.

The pipeline analyzes the ground-truth patch to extract critical function signatures and dependency graphs, which are injected as "Hints" into the agent's system prompt to bound search space.

## Test Validation Framework

Each task must pass fail2pass tests (tests that should fail before the fix and pass after, verifying the issue is resolved) and pass2pass tests (existing tests that must continue to pass, ensuring the fix does not break other functionality). Gold patches are validated across 3 test runs before inclusion in the benchmark.

These specifications represent advances in making SWE-bench benchmarking more rigorous and better suited for training and evaluating models in 2026.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "af261f6f-e77e-4af6-a6d6-0350fc308c29",
  "isSidechain": true,
  "promptId": "97188be6-5245-47ba-9011-c98eaa31631a",
  "agentId": "a3d6359a710b9a6ec",
  "type": "user",
  "uuid": "3bc02d12-4c86-42e9-8d51-627ec2929ee7",
  "sourceToolAssistantUUID": "af261f6f-e77e-4af6-a6d6-0350fc308c29",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "78f395f4-5c6b-48f5-b7df-f42fdf4d4c8a",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 27 · 2026-05-10T06:57:59.369Z_

<details><summary>↩ Tool result · `toolu_01VXsNVF6AU9JdKy53hEqXDD`</summary>

```text
Web search results for query: "expected behavior observed behavior specification mining 2025 2026"

Links: [{"title":"Contents lists available at ScienceDirect Information Systems","url":"https://d-nb.info/1378256107/34"},{"title":"SpecMiner: Heuristic-based mining of service behavioral models from interaction traces - ScienceDirect","url":"https://www.sciencedirect.com/science/article/abs/pii/S0167739X2033017X"},{"title":"Regression in Realtime API Model Behavior – Loss of Determinism with Structured Data - API - OpenAI Developer Community","url":"https://community.openai.com/t/regression-in-realtime-api-model-behavior-loss-of-determinism-with-structured-data/1376392"},{"title":"Autonomous Agents on Blockchains: Standards, Execution ...","url":"https://arxiv.org/pdf/2601.04583"},{"title":"Mining Specifications for Predictive Safety Monitoring | Proceedings of the ACM/IEEE 16th International Conference on Cyber-Physical Systems (with CPS-IoT Week 2025)","url":"https://dl.acm.org/doi/10.1145/3716550.3722021"},{"title":"Mining in 2025: emerging trends and predictions for 2026","url":"https://www.mining-technology.com/features/mining-in-2025-emerging-trends-and-predictions-for-2026/"},{"title":"Specification Mining With Few False Positives","url":"https://web.eecs.umich.edu/~weimerw/students/claire-ms.pdf"},{"title":"Conformance checking: a state-of-the-art literature review | Request PDF","url":"https://www.researchgate.net/publication/333796767_Conformance_checking_a_state-of-the-art_literature_review"},{"title":"Scenario-based and value-based specification mining | Proceedings of the 25th IEEE/ACM International Conference on Automated Software Engineering","url":"https://dl.acm.org/doi/10.1145/1858996.1859081"},{"title":"Specification Mining for Smart Contracts with Trace Slicing ...","url":"https://arxiv.org/pdf/2403.13279"}]

Based on the web search results, here are the key findings related to expected behavior, observed behavior, and specification mining in 2025-2026:

## Process Mining and Conformance Checking

Conformance checking is a sub-discipline of process mining, which compares observed process traces with a process model to analyze whether the process execution conforms with or deviates from the process design. It identifies deviations between the process instances' actual behaviour ("as-is") and its modelled behaviour ("to-be").

Recent research in 2025-2026 has focused on improving visualization and communication of conformance checking results. A 2025 article published in Information Systems 136 (2026) examined visualizations used to communicate conformance checking results.

## Specification Mining Research

A 2025 approach for learning interpretable monitors characterized by concise Signal Temporal Logic (STL) formulas that can predict safety property violations from observable sensor data combines a grammar-based method and two novel ensemble techniques. This work, presented at the ACM/IEEE 16th International Conference on Cyber-Physical Systems in 2025, addresses specification mining for safety-critical autonomous systems.

## Related Areas

A 2025 systematic literature review on mining LTL specifications was published in IEEE Access. Additionally, specification mining techniques continue to be applied to emerging domains like smart contracts and software behavior modeling.

The search results indicate that specification mining combining expected and observed behavior analysis remains an active research area in 2025-2026, with applications in process mining, cyber-physical systems, and formal verification.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c76db837-9255-4587-860f-b723bf096a9f",
  "isSidechain": true,
  "promptId": "97188be6-5245-47ba-9011-c98eaa31631a",
  "agentId": "a3d6359a710b9a6ec",
  "type": "user",
  "uuid": "4d8a2944-51a2-4364-b8e7-6e1d51aaa002",
  "sourceToolAssistantUUID": "c76db837-9255-4587-860f-b723bf096a9f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "78f395f4-5c6b-48f5-b7df-f42fdf4d4c8a",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 28 · 2026-05-10T06:57:59.488Z_

<details><summary>↩ Tool result · `toolu_01KquQeWFLqtdWXTVRPTZM97`</summary>

```text
Web search results for query: "site:arxiv.org test failure error message specification extraction 2025 2026"

Links: [{"title":"Willful Disobedience: Automatically Detecting Failures in Agentic Traces","url":"https://arxiv.org/html/2603.23806v1"},{"title":"Easy over Hard: A Simple Baseline for Test Failures Causes Prediction","url":"https://arxiv.org/html/2405.02922"},{"title":"[1504.02443] Potential Errors and Test Assessment in Software Product Line Engineering","url":"https://arxiv.org/abs/1504.02443"},{"title":"Conversational Error Recovery with Reasoning Inception","url":"https://arxiv.org/pdf/2602.17022"},{"title":"Studying the Impact of Early Test Termination Due to Assertion Failure on Code Coverage and Spectrum-based Fault Localization","url":"https://arxiv.org/html/2504.04557"},{"title":"Automatic Generation of Formal Specification and ...","url":"https://arxiv.org/pdf/2601.12845"},{"title":"Published as a conference paper at ICLR 2026 MECHANISTIC INTERPRETABILITY","url":"https://arxiv.org/pdf/2510.02917"},{"title":"1 Introduction","url":"https://arxiv.org/html/2604.27132"},{"title":"[2505.04108] In-Situ Hardware Error Detection Using Specification-Derived Petri Net Models and Behavior-Derived State Sequences","url":"https://arxiv.org/abs/2505.04108"},{"title":"arXiv:2505.00212v3 [cs.MA] 2 Jun 2025","url":"https://arxiv.org/pdf/2505.00212"}]

I've completed the web search with your query. Here are the results I found on arxiv.org related to test failure, error messages, and specification extraction from 2025-2026:

## Key Findings:

**1. AgentPex - Automated Agent Evaluation (2026)**
AgentPex extracts behavioral rules from agent prompts and system instructions, then uses these specifications to automatically evaluate traces for compliance, automatically extracting behavioral rules from agent prompts and evaluating compliance across multi-turn interactions.

**2. Test Failure Analysis Studies**
- One approach uses log abstraction techniques to parse unstructured log lines into structured log events, extracting useful patterns from raw log messages.
- Research on test failures involves examining testing reports to identify assertion failures and extracting failure locations by analyzing log information and matching keywords like "AssertionFailedError".

**3. Multi-Agent Failure Attribution (2025)**
Failure logs consist of entries where each entry specifies actions taken at time steps by agents, with research aimed at identifying which agent is responsible for task failure and the decisive error step.

**4. Specification Issues in AI Systems**
Recent empirical analyses reveal failure rates of 41% to 87% on standard benchmarks, with failures clustering into specification issues, inter-agent misalignment, and inadequate task verification.

The search returned several papers from 2025-2026 that address extraction of specifications and error messages from test failures, particularly in the context of agent systems and automated evaluation.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "cd9e63e3-fa37-491d-83bd-24fca5793662",
  "isSidechain": true,
  "promptId": "97188be6-5245-47ba-9011-c98eaa31631a",
  "agentId": "a3d6359a710b9a6ec",
  "type": "user",
  "uuid": "018d2025-3324-4e61-b14f-5a1162eb5f17",
  "sourceToolAssistantUUID": "cd9e63e3-fa37-491d-83bd-24fca5793662",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "78f395f4-5c6b-48f5-b7df-f42fdf4d4c8a",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 29 · 2026-05-10T06:58:01.037Z_

Let me run a few more searches to capture work on semantic analysis, interface/API specification, and any work that combines test-based learning with repair guidance.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "018d2025-3324-4e61-b14f-5a1162eb5f17",
  "isSidechain": true,
  "agentId": "a3d6359a710b9a6ec",
  "requestId": "req_011CatTGzYesAUuznp3UsDiD",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "197df2a4-98d9-4ece-b1e9-bc21286a254f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "78f395f4-5c6b-48f5-b7df-f42fdf4d4c8a",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_0126x2pvhTVs7EYSkwTKRwP8",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 3541,
      "cache_read_input_tokens": 25524,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3541,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 1,
      "service_tier": "standard",
      "inference_geo": "not_available"
    }
  }
}
```

</details>

---

### Tool call

_source line 30 · 2026-05-10T06:58:01.470Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01PxCpX3LNHBCdfG1k1btWVP`</summary>

```json
{
  "query": "site:arxiv.org semantic interface specification API repair 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "197df2a4-98d9-4ece-b1e9-bc21286a254f",
  "isSidechain": true,
  "agentId": "a3d6359a710b9a6ec",
  "requestId": "req_011CatTGzYesAUuznp3UsDiD",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "9c88061e-808f-4de5-a3ad-2d482fe37d0a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "78f395f4-5c6b-48f5-b7df-f42fdf4d4c8a",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_0126x2pvhTVs7EYSkwTKRwP8",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 3541,
      "cache_read_input_tokens": 25524,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3541,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 1,
      "service_tier": "standard",
      "inference_geo": "not_available"
    }
  }
}
```

</details>

---

### Tool call

_source line 31 · 2026-05-10T06:58:01.673Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01KWMVydMJQzmP4VbMeSuQ7u`</summary>

```json
{
  "query": "fault localization specification test assertion guidance 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9c88061e-808f-4de5-a3ad-2d482fe37d0a",
  "isSidechain": true,
  "agentId": "a3d6359a710b9a6ec",
  "requestId": "req_011CatTGzYesAUuznp3UsDiD",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "b7ab59b0-47c5-42e3-b5e7-bc4a86779b12",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "78f395f4-5c6b-48f5-b7df-f42fdf4d4c8a",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_0126x2pvhTVs7EYSkwTKRwP8",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 3541,
      "cache_read_input_tokens": 25524,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3541,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 1,
      "service_tier": "standard",
      "inference_geo": "not_available"
    }
  }
}
```

</details>

---

### Tool call

_source line 32 · 2026-05-10T06:58:02.304Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01RiGjuM2eu6chiBPQiUQg5u`</summary>

```json
{
  "query": "site:arxiv.org LLM specification generation code repair benchmark 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b7ab59b0-47c5-42e3-b5e7-bc4a86779b12",
  "isSidechain": true,
  "agentId": "a3d6359a710b9a6ec",
  "requestId": "req_011CatTGzYesAUuznp3UsDiD",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "401e27c0-97c2-4edb-9701-66ecf090040a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "78f395f4-5c6b-48f5-b7df-f42fdf4d4c8a",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_0126x2pvhTVs7EYSkwTKRwP8",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 3541,
      "cache_read_input_tokens": 25524,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3541,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 1,
      "service_tier": "standard",
      "inference_geo": "not_available"
    }
  }
}
```

</details>

---

### Tool call

_source line 33 · 2026-05-10T06:58:02.491Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_019AFELt3SANvYJDdSBDYWNM`</summary>

```json
{
  "query": "\"behavioral specification\" \"test generation\" code repair LLM 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "401e27c0-97c2-4edb-9701-66ecf090040a",
  "isSidechain": true,
  "agentId": "a3d6359a710b9a6ec",
  "requestId": "req_011CatTGzYesAUuznp3UsDiD",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "a32a97d2-1a4a-4025-aa09-0e48be56d865",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "78f395f4-5c6b-48f5-b7df-f42fdf4d4c8a",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_0126x2pvhTVs7EYSkwTKRwP8",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 3541,
      "cache_read_input_tokens": 25524,
      "output_tokens": 252,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 3541
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 7,
          "output_tokens": 252,
          "cache_read_input_tokens": 25524,
          "cache_creation_input_tokens": 3541,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 3541,
            "ephemeral_1h_input_tokens": 0
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    }
  }
}
```

</details>

---

### Tool result

_source line 34 · 2026-05-10T06:58:06.783Z_

<details><summary>↩ Tool result · `toolu_01PxCpX3LNHBCdfG1k1btWVP`</summary>

```text
Web search results for query: "site:arxiv.org semantic interface specification API repair 2025 2026"

Links: [{"title":"Refonte Learning : API Developer Engineering in 2026: Trends, Skills & Best Practices","url":"https://www.refontelearning.com/blog/api-developer-engineering-in-2026-trends-skills-best-practices"},{"title":"Characterising harmful API uses and repair techniques: Insights from a systematic review - ScienceDirect","url":"https://www.sciencedirect.com/science/article/pii/S1574013725000097"},{"title":"API Design Best Practices in 2025: Trends and Techniques - MyAppAPI Blog","url":"https://myappapi.com/blog/api-design-best-practices-2025"},{"title":"What the Open Semantic Interchange (OSI) spec means for metrics, semantics, and AI | dbt Labs","url":"https://www.getdbt.com/blog/the-osi-spec-updates"},{"title":"The Top 8 API Specifications to Know in 2025 | Nordic APIs |","url":"https://nordicapis.com/the-top-8-api-specifications-to-know-in-2025/"},{"title":"From Open API to Semantic Specifications and Code Adapters | IEEE Conference Publication | IEEE Xplore","url":"https://ieeexplore.ieee.org/document/8029798/"},{"title":"Open Semantic Interchange (OSI) Specification Finalized | Unified Semantics","url":"https://www.snowflake.com/en/blog/open-semantic-interchanges-specs-finalized/"},{"title":"Semantic enrichment of APIs: an OpenAPI case study | Interoperable Europe Portal","url":"https://interoperable-europe.ec.europa.eu/collection/semic-support-centre/semantic-enrichment-apis-openapi-case-study"},{"title":"Open Semantic Interchange - OSI | SBI","url":"https://www.sbi-group.com/blog/open-semantic-interchange-osi"},{"title":"Best Semantic Layer Tool 2026: No Vendor Bias | Unwind Data","url":"https://unwinddata.com/best-semantic-layer-tool"}]

Based on the search results, I couldn't find papers specifically from arxiv.org matching your query about "semantic interface specification API repair" from 2025-2026. The web search returned results from broader sources about API specifications and design trends, but not the arXiv research papers you were looking for.

The results do show some relevant industry developments:

- There are open challenges in API repair, including the lack of generalization of repair techniques and poor investment in studying semantic-related errors

- Service grounding establishes links between semantic and syntactic specifications, which is relevant to the intersection of semantics and API interfaces

- The Open Semantic Interchange (OSI) specification is now finalized, introducing an open standard for sharing semantic models

If you're specifically looking for arXiv research papers on this topic, you may want to:
1. Visit arxiv.org directly and search for these terms
2. Refine your search with author names if you have them
3. Use more specific technical terminology if available

Would you like me to help you search for something else, or provide more information about the industry standards and specifications related to APIs?


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "9c88061e-808f-4de5-a3ad-2d482fe37d0a",
  "isSidechain": true,
  "promptId": "97188be6-5245-47ba-9011-c98eaa31631a",
  "agentId": "a3d6359a710b9a6ec",
  "type": "user",
  "uuid": "3f6a7f9e-ea94-4a26-ab28-254559eaa4f1",
  "sourceToolAssistantUUID": "9c88061e-808f-4de5-a3ad-2d482fe37d0a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "78f395f4-5c6b-48f5-b7df-f42fdf4d4c8a",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 35 · 2026-05-10T06:58:09.111Z_

<details><summary>↩ Tool result · `toolu_01KWMVydMJQzmP4VbMeSuQ7u`</summary>

```text
Web search results for query: "fault localization specification test assertion guidance 2025 2026"

Links: [{"title":"Accepted at the 2026 IEEE International Conference on Software Testing, Verification and Validation (ICST 2026) Assessing the Impact of Code Changes on the Fault Localizability of Large Language Models","url":"https://arxiv.org/html/2504.04372"},{"title":"The Effects of Soft Assertion on Spectrum-Based Fault Localization | Springer Nature Link","url":"https://link.springer.com/chapter/10.1007/978-3-031-49266-2_26"},{"title":"Optimising Spectrum Based Fault Localisation for Single Fault Programs Using Specifications | Springer Nature Link","url":"https://link.springer.com/chapter/10.1007/978-3-319-89363-1_14"},{"title":"Coverage Isn't Enough: SBFL-Driven Insights into Manually ...","url":"https://arxiv.org/pdf/2512.11223"},{"title":"An empirical evaluation of pre-trained large language models for repairing declarative formal specifications | Empirical Software Engineering | Springer Nature Link","url":"https://link.springer.com/article/10.1007/s10664-025-10687-1"},{"title":"Test suite reduction for fault detection and localization: A combined approach | IEEE Conference Publication | IEEE Xplore","url":"https://ieeexplore.ieee.org/document/6747172/"},{"title":"arXiv:2506.15227v1 [cs.SE] 18 Jun 2025 1","url":"https://arxiv.org/pdf/2506.15227"},{"title":"CoverFL: Enhancing Fault Localization via Deep Coverage Relation | ACM Transactions on Software Engineering and Methodology","url":"https://dl.acm.org/doi/10.1145/3787964"},{"title":"Fault localization in software testing using soft computing approaches | IEEE Conference Publication | IEEE Xplore","url":"https://ieeexplore.ieee.org/document/8269753/"},{"title":"An Investigation into Spectrum-Based Fault Localization ...","url":"https://article.isarpublisher.com/download/1241"}]

Based on the web search results, here are relevant findings related to fault localization, specification, test assertions, and guidance from 2025-2026:

## Recent Research on Fault Localization and Specifications

A 2026 IEEE conference paper investigates LLM-based fault localization by injecting unseen faults into real-world programs with specifications while filtering out underspecified programs where correct fault localization is inherently ambiguous.

## Specifications and Assertions in Fault Localization

Unlike traditional fault localization techniques that rely primarily on test suites, LLMs often require explicit specifications in addition to code to perform fault localization effectively. Programs used in fault localization benchmarks must have an explicit, formally stated specification that can be given as an assertion statement.

## Test Assertions and Soft Assertions

Research investigates the negative effects of soft assertion on the accuracy of Spectrum-based Fault Localization, where soft assertion is a kind of test assertion which continues test case execution even after an assertion failure occurs.

## Fault Localization and Test Quality (2025-2026)

A recent study compares the Spectrum-Based Fault Localization (SBFL) score and code coverage of automatically generated tests with those of manually created tests. Research shows that automatically generated tests achieve higher branch coverage than manually created tests, but their SBFL score is lower, especially for code with deeply nested structures.

## Assertion Generation with LLMs

Recent work introduces CLAP, which prompts LLMs to generate assertions based on chain-of-thought reasoning and iteratively refines its predictions through interactions with both LLMs and a Python interpreter.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "b7ab59b0-47c5-42e3-b5e7-bc4a86779b12",
  "isSidechain": true,
  "promptId": "97188be6-5245-47ba-9011-c98eaa31631a",
  "agentId": "a3d6359a710b9a6ec",
  "type": "user",
  "uuid": "da95424c-ac9f-4cc9-9050-02df8cbf0fe4",
  "sourceToolAssistantUUID": "b7ab59b0-47c5-42e3-b5e7-bc4a86779b12",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "78f395f4-5c6b-48f5-b7df-f42fdf4d4c8a",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 36 · 2026-05-10T06:58:11.302Z_

<details><summary>↩ Tool result · `toolu_01RiGjuM2eu6chiBPQiUQg5u`</summary>

```text
Web search results for query: "site:arxiv.org LLM specification generation code repair benchmark 2025 2026"

Links: [{"title":"CodeSpecBench: Benchmarking LLMs for Executable Behavioral Specification Generation","url":"https://arxiv.org/html/2604.12268v1"},{"title":"Understanding Specification-Driven Code Generation with LLMs: An Empirical Study Design**This paper is a Stage 1 Registered Report. The study protocol and analysis plan were peer reviewed and accepted at SANER 2026 with a Continuity Acceptance (CA) score for Stage 2.","url":"https://arxiv.org/html/2601.03878v1"},{"title":"Bridging the Gap between User Intent and LLM: A Requirement Alignment Approach for Code Generation","url":"https://arxiv.org/html/2604.16198v1"},{"title":"ReCode: Improving LLM-based Code Repair with Fine-Grained Retrieval-Augmented Generation","url":"https://arxiv.org/html/2509.02330v1"},{"title":"ChipBench: A Next-Step Benchmark for Evaluating LLM Performance in AI-Aided Chip Design","url":"https://arxiv.org/html/2601.21448v1"},{"title":"Automated Repair of Ambiguous Problem Descriptions for LLM-Based Code Generation","url":"https://arxiv.org/html/2505.07270"},{"title":"PATCHEVAL: A New Benchmark for Evaluating LLMs on Patching","url":"https://arxiv.org/pdf/2511.11019"},{"title":"Where Do LLMs Still Struggle? An In-Depth Analysis of Code Generation Benchmarks","url":"https://arxiv.org/html/2511.04355v1"},{"title":"Understanding Specification-Driven Code Generation with ...","url":"https://arxiv.org/pdf/2601.03878"},{"title":"arXiv:2404.11050v2 [cs.SE] 12 Jun 2025","url":"https://arxiv.org/pdf/2404.11050"}]

I found several highly relevant papers on arxiv.org related to LLM specification generation, code repair, and benchmarks from 2025-2026:

## Key Results:

1. **CodeSpecBench: Benchmarking LLMs for Executable Behavioral Specification Generation** - This benchmark found that generating executable behavioral specifications is substantially more challenging for LLMs than generating code solutions, suggesting that strong code generation performance does not necessarily imply a deep understanding of intended program behavior.

2. **Understanding Specification-Driven Code Generation with LLMs: An Empirical Study Design** - This paper presents an empirical study design using CURRANTE, a Visual Studio Code extension that enables a human-in-the-loop workflow for LLM-assisted code generation, guiding developers through three sequential stages—Specification, Tests, and Function—allowing them to define requirements, generate and refine test suites, and produce functions that satisfy those tests.

3. **Bridging the Gap between User Intent and LLM: A Requirement Alignment Approach for Code Generation** - This work discusses post-processing paradigms like SpecFix, μFix, and Specine that aim to fix generated code through execution feedback or detecting semantic misalignment between requirements and output code.

4. **Automated Repair of Ambiguous Problem Descriptions for LLM-Based Code Generation (SpecFix)** - SpecFix modified 43.58% of descriptions, improving Pass@1 on the modified set by 30.9%, yielding a 4.09% absolute improvement across the entire benchmark.

5. **Where Do LLMs Still Struggle? An In-Depth Analysis of Code Generation Benchmarks** - This analysis examined LiveCodeBench (LCB-V6, which consists of 175 programming problems released between January and April 2025) along with other benchmarks.

These papers cover recent advances in specification generation, code repair techniques, and comprehensive benchmarking of LLM capabilities in code generation tasks.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "401e27c0-97c2-4edb-9701-66ecf090040a",
  "isSidechain": true,
  "promptId": "97188be6-5245-47ba-9011-c98eaa31631a",
  "agentId": "a3d6359a710b9a6ec",
  "type": "user",
  "uuid": "3b432c0c-b442-4348-afe1-32d2fe7a8db4",
  "sourceToolAssistantUUID": "401e27c0-97c2-4edb-9701-66ecf090040a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "78f395f4-5c6b-48f5-b7df-f42fdf4d4c8a",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 37 · 2026-05-10T06:58:12.288Z_

<details><summary>↩ Tool result · `toolu_019AFELt3SANvYJDdSBDYWNM`</summary>

```text
Web search results for query: ""behavioral specification" "test generation" code repair LLM 2025"

Links: [{"title":"CodeSpecBench: Benchmarking LLMs for Executable Behavioral Specification Generation","url":"https://arxiv.org/html/2604.12268v1"},{"title":"Validating Formal Specifications with LLM-generated Test Cases","url":"https://arxiv.org/html/2510.23350v1"},{"title":"Bridging the Gap between User Intent and LLM: A Requirement Alignment Approach for Code Generation","url":"https://arxiv.org/html/2604.16198v1"},{"title":"Multi-Step Generation of Test Specifications using Large ...","url":"https://aclanthology.org/2025.acl-industry.11.pdf"},{"title":"Large Language Models for Unit Test Generation: Achievements, Challenges, and the Road Ahead","url":"https://arxiv.org/html/2511.21382v1"},{"title":"Navigating Challenges with LLM-based Code Generation ...","url":"http://reports-archive.adm.cs.cmu.edu/anon/s3d2025/CMU-S3D-25-101.pdf"},{"title":"CVE-Bench: Benchmarking LLM-based Software ...","url":"https://aclanthology.org/2025.naacl-long.212.pdf"},{"title":"GitHub - iSEngLab/AwesomeLLM4SE: [SCIS 2025] A Survey on Large Language Models for Software Engineering · GitHub","url":"https://github.com/iSEngLab/AwesomeLLM4SE"},{"title":"FeedbackEval: A Benchmark for Evaluating Large Language Models in Feedback-Driven Code Repair Tasks","url":"https://arxiv.org/html/2504.06939v2"},{"title":"Towards LLM-Driven Code Generation: The Impact of Process ...","url":"https://spectrum.library.concordia.ca/id/eprint/995585/1/LIN_MA_S2025.pdf"}]

I've completed the web search for your query on behavioral specification, test generation, code repair, and LLMs in 2025. Here are the key findings:

## Key Research Areas

**Behavioral Specification Generation:**
Generating executable behavioral specifications is substantially more challenging for LLMs than generating code solutions, suggesting that strong code generation performance does not necessarily imply a deep understanding of intended program behavior. Executable behavioral specifications characterize program behavior through preconditions and postconditions, where preconditions formally delimit the set of admissible inputs and program states, whereas postconditions prescribe the properties that the outputs and resulting program states must satisfy upon termination.

**Test Generation with LLMs:**
GPT-5 is effective at generating positive and negative test cases that are syntactically correct and that satisfy or not the given requirement, and can detect many wrong specifications written by humans. Empirical studies consistently indicate that iterative refinement approaches can substantially increase the valid pass rate of generated tests from as low as 24% to over 70%.

**Code Repair Approaches:**
SpecFix analyzes behavioral divergence among generated solutions and produces minimal textual patches to repair ambiguous problem descriptions. Recent advancements include NTR, a two-stage template-guided framework enhancing LLM fine-tuning, and ChatRepair, a conversation-driven approach that iteratively refines patches.

**Feedback-Driven Repair:**
Iterative validation and repair loops have become the standard mechanism to ensure robust usability and lead to significant improvements in compilation and execution.

The research indicates that combining behavioral specifications with test generation and iterative repair mechanisms is becoming a standard practice for improving LLM-based code generation reliability.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a32a97d2-1a4a-4025-aa09-0e48be56d865",
  "isSidechain": true,
  "promptId": "97188be6-5245-47ba-9011-c98eaa31631a",
  "agentId": "a3d6359a710b9a6ec",
  "type": "user",
  "uuid": "022db475-d8c0-4b2a-94df-b0523352ea76",
  "sourceToolAssistantUUID": "a32a97d2-1a4a-4025-aa09-0e48be56d865",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "78f395f4-5c6b-48f5-b7df-f42fdf4d4c8a",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 38 · 2026-05-10T06:58:13.936Z_

Excellent. Let me run a few final searches to capture any work on prompting strategies, extraction from logs, and recent foundational work on APR that might be competing approaches.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "022db475-d8c0-4b2a-94df-b0523352ea76",
  "isSidechain": true,
  "agentId": "a3d6359a710b9a6ec",
  "requestId": "req_011CatTHwJDncSBgnVxtpFMf",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "df4f324e-a359-4639-bb28-45e6d2614ced",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "78f395f4-5c6b-48f5-b7df-f42fdf4d4c8a",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01W2XjsHZqLzxNEexFKAKiZ7",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 4072,
      "cache_read_input_tokens": 29065,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4072,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 3,
      "service_tier": "standard",
      "inference_geo": "not_available"
    }
  }
}
```

</details>

---

### Tool call

_source line 39 · 2026-05-10T06:58:14.366Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01TePZM4VovdgNFttqE5twF7`</summary>

```json
{
  "query": "site:arxiv.org prompt engineering bug report error specification repair 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "df4f324e-a359-4639-bb28-45e6d2614ced",
  "isSidechain": true,
  "agentId": "a3d6359a710b9a6ec",
  "requestId": "req_011CatTHwJDncSBgnVxtpFMf",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "dc99d8f8-3bec-4ed9-9f64-963f892a0c07",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "78f395f4-5c6b-48f5-b7df-f42fdf4d4c8a",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01W2XjsHZqLzxNEexFKAKiZ7",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 4072,
      "cache_read_input_tokens": 29065,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4072,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 3,
      "service_tier": "standard",
      "inference_geo": "not_available"
    }
  }
}
```

</details>

---

### Tool call

_source line 40 · 2026-05-10T06:58:14.611Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01X6ua61Ya2qPpGVUoDtk1Sg`</summary>

```json
{
  "query": "site:arxiv.org automated program repair neural specification learning 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "dc99d8f8-3bec-4ed9-9f64-963f892a0c07",
  "isSidechain": true,
  "agentId": "a3d6359a710b9a6ec",
  "requestId": "req_011CatTHwJDncSBgnVxtpFMf",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "8b74bdc2-3189-45ae-848f-8fba8661b1df",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "78f395f4-5c6b-48f5-b7df-f42fdf4d4c8a",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01W2XjsHZqLzxNEexFKAKiZ7",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 4072,
      "cache_read_input_tokens": 29065,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4072,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 3,
      "service_tier": "standard",
      "inference_geo": "not_available"
    }
  }
}
```

</details>

---

### Tool call

_source line 41 · 2026-05-10T06:58:15.056Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_0162q41sTdzNtStrddxZXAEc`</summary>

```json
{
  "query": "\"behavioral delta\" OR \"behavioral difference\" specification extraction 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8b74bdc2-3189-45ae-848f-8fba8661b1df",
  "isSidechain": true,
  "agentId": "a3d6359a710b9a6ec",
  "requestId": "req_011CatTHwJDncSBgnVxtpFMf",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "de594b8e-3d41-4ff1-a07f-e02d8f573be6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "78f395f4-5c6b-48f5-b7df-f42fdf4d4c8a",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01W2XjsHZqLzxNEexFKAKiZ7",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 4072,
      "cache_read_input_tokens": 29065,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4072,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 3,
      "service_tier": "standard",
      "inference_geo": "not_available"
    }
  }
}
```

</details>

---

### Tool call

_source line 42 · 2026-05-10T06:58:15.198Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01PTXGW2gqqgY1VeCYoYchyG`</summary>

```json
{
  "query": "site:arxiv.org test suite specification patch generation repair 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "de594b8e-3d41-4ff1-a07f-e02d8f573be6",
  "isSidechain": true,
  "agentId": "a3d6359a710b9a6ec",
  "requestId": "req_011CatTHwJDncSBgnVxtpFMf",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "7d05fbd6-351d-4886-a5f5-b41421efccb3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "78f395f4-5c6b-48f5-b7df-f42fdf4d4c8a",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01W2XjsHZqLzxNEexFKAKiZ7",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 4072,
      "cache_read_input_tokens": 29065,
      "output_tokens": 257,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 4072
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 7,
          "output_tokens": 257,
          "cache_read_input_tokens": 29065,
          "cache_creation_input_tokens": 4072,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 4072,
            "ephemeral_1h_input_tokens": 0
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    }
  }
}
```

</details>

---

### Tool result

_source line 43 · 2026-05-10T06:58:20.492Z_

<details><summary>↩ Tool result · `toolu_01TePZM4VovdgNFttqE5twF7`</summary>

```text
Web search results for query: "site:arxiv.org prompt engineering bug report error specification repair 2025 2026"

Links: [{"title":"The Ultimate Guide to Prompt Engineering in 2026 | Lakera – Protecting AI teams that disrupt the world.","url":"https://www.lakera.ai/blog/prompt-engineering-guide"},{"title":"Prompt Engineering Basics (2026): A Practical Guide | Medium","url":"https://medium.com/@mjgmario/prompt-engineering-basics-2026-93aba4dc32b1"},{"title":"A Practitioner’s Guide to Prompt Engineering in 2025","url":"https://www.getmaxim.ai/articles/a-practitioners-guide-to-prompt-engineering-in-2025/"},{"title":"GPT-4.1 Prompting Guide","url":"https://developers.openai.com/cookbook/examples/gpt4-1_prompting_guide"},{"title":"Prompt Engineering in 2025: The Latest Best Practices","url":"https://www.news.aakashg.com/p/prompt-engineering"},{"title":"A Taxonomy of Prompt Defects in LLM Systems","url":"https://arxiv.org/html/2509.14404v1"},{"title":"The Ultimate Prompt Engineering Guide for 2026: From Basics to Agentic Workflows","url":"https://sarifulislam.com/blog/prompt-engineering-2026/"},{"title":"Advanced Prompt Engineering Techniques in 2025","url":"https://www.getmaxim.ai/articles/advanced-prompt-engineering-techniques-in-2025/"},{"title":"Prompt Engineering 2026 — Series 0: Introduction | by Xue Langping | CodeToDeploy | Medium","url":"https://medium.com/codetodeploy/prompt-engineering-2026-series-0-introduction-3e331e955433"},{"title":"Context-aware prompting for LLM-based program repair | Automated Software Engineering","url":"https://link.springer.com/article/10.1007/s10515-025-00512-w"}]

I found search results related to prompt engineering and some relevant topics from 2025-2026. The most relevant result appears to be from arxiv.org:

A research paper titled "A Taxonomy of Prompt Defects in LLM Systems" examines how defects surface in real development workflows and their downstream effects, distilling mitigation strategies spanning prompt engineering patterns, automated guardrails, testing harnesses, and evaluation frameworks, and summarizes these in a master taxonomy linking defect, impact, and remedy.

Additionally, there are results discussing related topics:

- A paper on "Context-aware prompting for LLM-based program repair" published in Automated Software Engineering in 2025, which addresses how LLMs can be prompted more effectively for bug repair tasks.

- Practical guides from 2025 recommend using validators and repair strategies for handling errors and structured outputs in prompts.

- GPT-4.1 achieves state-of-the-art performance for non-reasoning models on SWE-bench Verified, solving 55% of problems, which involves bug specification and repair.

Note that your search query included `site:arxiv.org`, but the web search tool found broader results. The arxiv.org result I cited appears most directly relevant to your interests in prompt engineering, bug reports, and error specification/repair.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "dc99d8f8-3bec-4ed9-9f64-963f892a0c07",
  "isSidechain": true,
  "promptId": "97188be6-5245-47ba-9011-c98eaa31631a",
  "agentId": "a3d6359a710b9a6ec",
  "type": "user",
  "uuid": "df950165-800e-47ff-9f9b-78ccc712be68",
  "sourceToolAssistantUUID": "dc99d8f8-3bec-4ed9-9f64-963f892a0c07",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "78f395f4-5c6b-48f5-b7df-f42fdf4d4c8a",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 44 · 2026-05-10T06:58:21.183Z_

<details><summary>↩ Tool result · `toolu_01X6ua61Ya2qPpGVUoDtk1Sg`</summary>

```text
Web search results for query: "site:arxiv.org automated program repair neural specification learning 2025"

Links: [{"title":"A Survey of LLM-based Automated Program Repair: Taxonomies, Design Paradigms, and Applications","url":"https://arxiv.org/html/2506.23749v1"},{"title":"[2202.10868] Neural Program Repair: Systems, Challenges and Solutions","url":"https://arxiv.org/abs/2202.10868"},{"title":"A Systematic Literature Review on Large Language Models","url":"https://arxiv.org/pdf/2405.01466"},{"title":"Specification Vibing for Automated Program Repair","url":"https://arxiv.org/html/2602.08263"},{"title":"Gradient-Based Program Synthesis with Neurally Interpreted Languages","url":"https://arxiv.org/html/2604.18907"},{"title":"Gradient-Based Program Repair: Fixing Bugs in Continuous Program Spaces","url":"https://arxiv.org/pdf/2505.17703"},{"title":"Automated Repair of Ambiguous Problem Descriptions for LLM-Based Code Generation","url":"https://arxiv.org/html/2505.07270"},{"title":"RelRepair: Enhancing Automated Program Repair by Retrieving Relevant Code","url":"https://arxiv.org/html/2509.16701v1"},{"title":"[1904.01720] Neural Program Repair by Jointly Learning to Localize and Repair","url":"https://arxiv.org/abs/1904.01720"},{"title":"[2506.23749v1] A Survey of LLM-based Automated Program Repair: Taxonomies, Design Paradigms, and Applications","url":"https://arxiv.org/abs/2506.23749v1"}]

Based on the search results from arXiv, here are the key findings related to automated program repair and neural specification learning in 2025:

## Recent Survey and Research

A comprehensive survey reviewing 63 recent state-of-the-art APR systems published between January 2022 and June 2025 summarizes their design trade-offs, common trends, and open questions. The systems are categorized into four paradigms, demonstrating how retrieval- or analysis-augmented contexts strengthen automated program repair approaches.

## Key Approaches in 2025

Current research revolves around multiple fine-tuning strategies, including fully supervised fine-tuning that updates all parameters of the backbone for strong accuracy, and parameter-efficient fine-tuning that freezes most of the backbone and learns small adapter modules while reducing memory costs. Reinforcement learning fine-tuning trains models with execution or security rewards to optimize for functional correctness instead of log likelihood.

## Notable Recent Works

A 2025 work by Tian and Chen addresses aligning requirements for large language model code generation. Additionally, learning-based APR techniques have been proposed that formulate patch generation as a neural machine translation task, learning latent bug-fixing patterns from large-scale code repositories.

## Challenges and Future Directions

Key trade-offs include fine-tuning delivering strong task alignment at high training cost versus prompting enabling rapid deployment but limited by prompt design; persistent challenges include verifying semantic correctness beyond test suites, repairing repository-scale defects, and lowering LLM costs, with future work combining lightweight human feedback, repository-aware retrieval, code analysis, and cost-aware planning.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "8b74bdc2-3189-45ae-848f-8fba8661b1df",
  "isSidechain": true,
  "promptId": "97188be6-5245-47ba-9011-c98eaa31631a",
  "agentId": "a3d6359a710b9a6ec",
  "type": "user",
  "uuid": "789ea52b-59bb-4a98-b424-59b538597226",
  "sourceToolAssistantUUID": "8b74bdc2-3189-45ae-848f-8fba8661b1df",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "78f395f4-5c6b-48f5-b7df-f42fdf4d4c8a",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 45 · 2026-05-10T06:58:22.639Z_

<details><summary>↩ Tool result · `toolu_0162q41sTdzNtStrddxZXAEc`</summary>

```text
Web search results for query: ""behavioral delta" OR "behavioral difference" specification extraction 2025"

Links: [{"title":"Behavioral inhibition and EEG delta-beta correlation in early childhood: Comparing a between-subjects and within-subjects approach - PubMed","url":"https://pubmed.ncbi.nlm.nih.gov/31628975/"},{"title":"Learning Program Behavioral Models from Synthesized Input-Output Pairs","url":"https://arxiv.org/pdf/2407.08597"},{"title":"CodeSpecBench: Benchmarking LLMs for Executable Behavioral Specification Generation","url":"https://arxiv.org/html/2604.12268v1"},{"title":"BASIS: A behavioral approach to the specification of information systems - ScienceDirect","url":"https://www.sciencedirect.com/science/article/abs/pii/030643798390025X"},{"title":"DeltaCCS: A Core Calculus for Behavioral Change | Springer Nature Link","url":"https://link.springer.com/chapter/10.1007/978-3-662-45234-9_23"},{"title":"Delta-Learning Approach","url":"https://www.emergentmind.com/topics/delta-learning-approach"},{"title":"The Delta Learning Hypothesis: Preference Tuning on Weak Data can Yield Strong Gains","url":"https://arxiv.org/html/2507.06187v1"},{"title":"Delta Behavioral | SpringHealth","url":"https://springhealthbehavioral.com/delta-behavior/"},{"title":"Behavioral Specification Theories: An Algebraic Taxonomy | Springer Nature Link","url":"https://link.springer.com/chapter/10.1007/978-3-030-61362-4_14"},{"title":"Deployment Variability in Delta-Oriented Models | Springer Nature Link","url":"https://link.springer.com/chapter/10.1007/978-3-662-45234-9_22"}]

Based on the search results, here are the key findings related to "behavioral delta" or "behavioral difference" and specification extraction in 2025:

## Specification Extraction with Behavioral Focus

Recent work in 2025 includes CodeSpecBench, which benchmarks LLMs for executable behavioral specification generation, departing from solution generation to focus on specification generation by requiring models to produce explicit, executable preconditions and postconditions that capture intended program behavior.

Executable behavioral specifications characterize program behavior through preconditions and postconditions: preconditions formally delimit the set of admissible inputs and program states under which a function is intended to execute, whereas postconditions prescribe the properties that the outputs and resulting program states must satisfy upon termination.

## Delta-Learning Approaches in 2025

Delta-learning exploits differences between predictions and models to optimize efficiency and accuracy across AI, neuroscience, and physical sciences. In preference tuning, pairing self-generated responses with weaker responses creates a positive delta that drives learning beyond the baseline model's performance, yielding small but consistent gains on nearly all benchmarks.

## Theoretical Frameworks

DeltaCCS proposes a delta-oriented extension to Milner's process calculus CCS that allows for modular reasoning about behavioral variability, where modular change directives are applied to core processes by altering term rewriting semantics in a determined way.

The search results show that 2025 research is actively exploring how to extract, specify, and learn from behavioral differences and deltas in both software systems and machine learning contexts.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "de594b8e-3d41-4ff1-a07f-e02d8f573be6",
  "isSidechain": true,
  "promptId": "97188be6-5245-47ba-9011-c98eaa31631a",
  "agentId": "a3d6359a710b9a6ec",
  "type": "user",
  "uuid": "bf9a774a-44b0-4b40-97b4-7c06f731e780",
  "sourceToolAssistantUUID": "de594b8e-3d41-4ff1-a07f-e02d8f573be6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "78f395f4-5c6b-48f5-b7df-f42fdf4d4c8a",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 46 · 2026-05-10T06:58:24.245Z_

<details><summary>↩ Tool result · `toolu_01PTXGW2gqqgY1VeCYoYchyG`</summary>

```text
Web search results for query: "site:arxiv.org test suite specification patch generation repair 2025 2026"

Links: [{"title":"Root-Cause-Driven Automated Vulnerability Repair","url":"https://arxiv.org/html/2605.04251"},{"title":"PAFT: Preservation-Aware Fine-Tuning for Minimal-Edit Program Repair","url":"https://arxiv.org/html/2604.03113v2"},{"title":"Identifying Patch Correctness in Test-Based Program Repair","url":"https://arxiv.org/pdf/1706.09120"},{"title":"REFINE: Enhancing Program Repair Agents through Context-Aware Patch Refinement","url":"https://arxiv.org/pdf/2510.03588"},{"title":"Test-based Patch Clustering for Automatically-Generated Patches Assessment","url":"https://arxiv.org/html/2207.11082"},{"title":"Alleviating Patch Overﬁtting with Automatic Test","url":"https://arxiv.org/pdf/1810.10614"},{"title":"Heterogeneous Prompting and Execution Feedback for SWE Issue Test Generation and Selection","url":"https://arxiv.org/html/2508.06365"},{"title":"ComPass: Contrastive Learning for Automated Patch Correctness Assessment in Program Repair","url":"https://arxiv.org/html/2602.07561"},{"title":"[2301.01113] Invalidator: Automated Patch Correctness Assessment via Semantic and Syntactic Reasoning","url":"https://ar5iv.labs.arxiv.org/html/2301.01113"},{"title":"[1408.2103] A Critical Review of “Automatic Patch Generation Learned from Human-Written Patches”: Essay on the Problem Statement and the Evaluation of Automatic Software Repair","url":"https://ar5iv.labs.arxiv.org/html/1408.2103"}]

I've successfully performed the web search with your specified query on arxiv.org. Here are the key results:

The search returned several recent papers (from 2025-2026) related to test suite specification, patch generation, and repair:

1. **Root-Cause-Driven Automated Vulnerability Repair** (4 days ago) - This paper discusses PatchAgent (2025) which relies on LLMs for agentic fault localization and patch synthesis using the original PoC and developer test suite, and LoopRepair (2026) which augments LLM-based repair with symbolic execution.

2. **PAFT: Preservation-Aware Fine-Tuning for Minimal-Edit Program Repair** (April 6, 2026) - This work notes that most APR pipelines are optimized primarily for test-suite passing, and discusses how patches often introduce redundant code or disrupt the original code structure, with a study finding that 41.5% of Claude Code-generated patches required manual revision.

3. **REFINE: Enhancing Program Repair Agents through Context-Aware Patch Refinement** - Candidates are validated against a suite of tests, with successful patches being those that pass all relevant test cases.

4. **Heterogeneous Prompting and Execution Feedback for SWE Issue Test Generation and Selection** (January 22, 2026) - Agentless automatically generates reproduction tests and combines them with regression tests to select the best patch via majority voting.

5. **ComPass: Contrastive Learning for Automated Patch Correctness Assessment** (February 7, 2026) - Discusses the patch overfitting issue due to weak test suites, where patches may pass available test suites but fail to generalize to unseen test suites.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "7d05fbd6-351d-4886-a5f5-b41421efccb3",
  "isSidechain": true,
  "promptId": "97188be6-5245-47ba-9011-c98eaa31631a",
  "agentId": "a3d6359a710b9a6ec",
  "type": "user",
  "uuid": "d99c5ef3-688c-4590-8b23-d5b1f7d2829e",
  "sourceToolAssistantUUID": "7d05fbd6-351d-4886-a5f5-b41421efccb3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "78f395f4-5c6b-48f5-b7df-f42fdf4d4c8a",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 47 · 2026-05-10T06:59:11.975Z_

Perfect. Now let me compile a comprehensive report of all the relevant competing work I've found for the SpecExtract paper. This is substantial, so let me organize it by research category and direct overlap.

## Adversarial Literature Review for SpecExtract

Based on my systematic search of recent literature (2025-2026), I've identified significant competing and overlapping work across multiple research dimensions. Here are the key findings organized by research theme:

---

## **DIRECTLY OVERLAPPING WORK: Specification Generation and Extraction from Bug Reports**

### 1. **CodeSpecBench: Benchmarking LLMs for Executable Behavioral Specification Generation (2026)**
- **URL:** https://arxiv.org/html/2604.12268v1
- **Direct Overlap:** This work explicitly benchmarks specification generation (preconditions, postconditions) from code and requirements. The paper finds that specification generation is substantially more challenging than code generation (20.2% pass rate on repository-level SWE-bench Verified tasks).
- **Key Difference:** Focuses on generating specifications FROM code/requirements rather than FROM bug reports specifically, but uses same SWE-bench Verified training data.

### 2. **Specification Vibing for Automated Program Repair (February 2026)**
- **URL:** https://arxiv.org/html/2602.08263
- **Direct Overlap:** VibeRepair transforms buggy code and failing test cases into "test-based flawed behavior specification" through iterative interaction with validation feedback. This is almost directly parallel to SpecExtract's core idea of extracting behavioral specifications from test failures.
- **Key Difference:** VibeRepair focuses on iterative refinement through feedback loops rather than upfront extraction training.

### 3. **Understanding Specification-Driven Code Generation with LLMs: An Empirical Study Design (2026)**
- **URL:** https://arxiv.org/html/2601.03878v1
- **Direct Overlap:** This registered report studies LLM-driven specification engineering with the CURRANTE workflow (Specification → Tests → Function pipeline). The work demonstrates the importance of explicit specification stages in code generation.
- **Key Difference:** Studies human-in-the-loop specification engineering rather than automatic extraction from bug reports.

---

## **HIGH-OVERLAP WORK: Test-Based Specification and Behavioral Constraint Extraction**

### 4. **Beyond Fixed Tests: Repository-Level Issue Resolution as Coevolution of Code and Behavioral Constraints (April 2026)**
- **URL:** https://arxiv.org/html/2604.04580
- **High Overlap:** Agent-CoEvo models tests as dynamic behavioral constraints that guide repair. The paper explicitly recognizes that "enabling repair agents to revise behavioral constraints during search is critical," directly overlapping with SpecExtract's use of test assertions to guide repair.
- **Critical Claim:** Proposes that behavioral constraints should be coevolved with patches rather than fixed, which is a competing design choice to SpecExtract's pre-trained spec extraction approach.

### 5. **Can We Enhance Bug Report Quality Using LLMs?: An Empirical Study of LLM-Based Bug Report Generation (April 2025)**
- **URL:** https://arxiv.org/abs/2504.18804
- **High Overlap:** Investigates instruction fine-tuning for automated structured bug report generation. Shows LLMs can enhance bug report quality by filling missing details and semantic analysis of descriptions.
- **Key Difference:** Focuses on improving bug report quality itself rather than extracting specifications from existing reports.

### 6. **BugMentor: Generating Answers to Follow-up Questions from Software Bug Reports using Structured Information Retrieval and Neural Text Generation (2023-2025)**
- **URL:** https://arxiv.org/abs/2304.12494
- **High Overlap:** Extracts and reasons over structured information from bug reports using neural methods.

---

## **COMPETING APPROACHES: Specification-Driven Repair Pipelines**

### 7. **Automated Repair of Ambiguous Problem Descriptions for LLM-Based Code Generation (SpecFix, 2025)**
- **URL:** https://arxiv.org/html/2505.07270
- **Competing Approach:** SpecFix analyzes behavioral divergence among generated solutions and produces patches to repair ambiguous problem descriptions. Modified 43.58% of descriptions, improving performance by 4.09% overall—this is a different approach to handling specification quality.
- **Key Insight:** Shows that specification quality/ambiguity directly affects code generation success (30.9% improvement when specs are fixed).

### 8. **Knowledge-Enhanced Program Repair for Data Science Code (February 2025)**
- **URL:** https://arxiv.org/html/2502.09771v1
- **Competing Approach:** Organizes problem description, incorrect code, stderr, and API knowledge into a structured prompt. This is a prompting-based approach to leverage specification information rather than learning to extract it.

### 9. **Repeton: Structured Bug Repair with ReAct-Guided Patch-and-Test Cycles (June 2025)**
- **URL:** https://arxiv.org/html/2506.08173
- **Competing Approach:** Uses structured patch-and-test cycles guided by lightweight heuristics rather than learned specifications. Tests are treated as dynamic constraints in the repair loop.

---

## **RELATED WORK: Agentic Bug Reproduction and Information Extraction**

### 10. **Agentic Bug Reproduction for Effective Automated Program Repair at Google (March 2025)**
- **URL:** https://arxiv.org/html/2502.01821v2
- **Related:** Describes automated extraction and curation of bug reproduction information from Google projects (7 languages). Shows how structured bug information improves repair.

### 11. **LLPut: Investigating Large Language Models for Bug Report-Based Input Generation (2025)**
- **URL:** https://arxiv.org/abs/2503.20578
- **Related:** Specifically investigates extracting failure-inducing inputs from bug reports using generative LLMs. Tests Qwen, LLaMA, and other models on this extraction task.

### 12. **ChatBR: Automated assessment and improvement of bug reports (2024-2025)**
- **URL:** https://dl.acm.org/doi/pdf/10.1145/3691620.3695518
- **Related:** Uses pre-trained models with attention mechanisms to assess and improve bug report quality by detecting missing fields.

### 13. **Uncovering the iceberg from the tip: Generating API Specifications for Bug (2025)**
- **URL:** https://www.ndss-symposium.org/wp-content/uploads/2025-2001-paper.pdf
- **Related:** Extracts API specifications from bug reports, specifically targeting interface-level specifications.

---

## **METHODOLOGICALLY RELEVANT: SWE-bench Training and Structured Data Approaches**

### 14. **SWE-bench Verified and SWE-Bench Pro (2025-2026)**
- **URLs:** 
  - https://arxiv.org/html/2602.04449 (What's in a Benchmark?)
  - https://openai.com/index/introducing-swe-bench-verified/
- **Relevance:** SWE-bench Pro explicitly adds structured interface specifications and behavioral requirements to reduce false negatives from naming mismatches. This is the same benchmark/training data SpecExtract uses, but with additional structured annotations.

### 15. **SWE-rebench V2: Language-Agnostic SWE Task Collection at Scale (2025)**
- **URL:** https://arxiv.org/html/2602.23866
- **Relevance:** Automates task collection at scale and includes structured specification annotations (interface specs, behavioral requirements).

### 16. **SWE-bench Goes Live! (April 2025)**
- **URL:** https://arxiv.org/html/2505.23419v2
- **Relevance:** SWE-bench-Live provides 1,319 continuously updated benchmark instances with explicit behavioral test validation. This competing data source might have better specification annotations.

### 17. **SWE-AGI: Benchmarking Specification-Driven Software (February 2026)**
- **URL:** https://www.arxiv.org/pdf/2602.09447
- **Critical Relevance:** Each task provides explicit normative specifications (specs/), task statements (TASK.md), and test subsets. This is a direct competitor providing better structured specification annotations than raw SWE-bench.

### 18. **SWE-Bench 5G: Benchmarking AI Coding Agents on Telecom Network Engineering Tasks (2026)**
- **URL:** https://arxiv.org/html/2604.26278
- **Relevance:** Domain-specific variant showing SWE-bench can be extended with specialized specifications.

---

## **FAULT LOCALIZATION WITH SPECIFICATIONS**

### 19. **Assessing the Impact of Code Changes on the Fault Localizability of Large Language Models (2026 ICST)**
- **URL:** https://arxiv.org/html/2504.04372
- **Competing Use of Specs:** Shows that LLMs require explicit, formally stated specifications (assertion statements) to perform effective fault localization, filtering out underspecified programs. This validates SpecExtract's premise about spec importance but offers a competing approach (specs as explicit assertions in localization).

### 20. **Coverage Isn't Enough: SBFL-Driven Insights into Manually Written Tests (2025)**
- **URL:** https://arxiv.org/pdf/2512.11223
- **Related:** Investigates spectrum-based fault localization (SBFL) guided by test suite quality, showing test quality directly impacts localization effectiveness.

---

## **NEURAL PROGRAM REPAIR SURVEYS AND FRAMEWORKS**

### 21. **A Survey of LLM-based Automated Program Repair: Taxonomies, Design Paradigms, and Applications (June 2025)**
- **URL:** https://arxiv.org/html/2506.23749v1
- **Comprehensive Baseline:** Surveys 63 recent APR systems (Jan 2022 - June 2025), covering retrieval-augmented and analysis-augmented approaches. SpecExtract should position itself relative to this taxonomy (likely under "specification-augmented" repair).

### 22. **Neural Program Repair: Systems, Challenges and Solutions (2022, updated context 2025)**
- **URL:** https://arxiv.org/abs/2202.10868
- **Foundational Context:** Foundational survey on neural program repair approaches.

### 23. **A Taxonomy of Prompt Defects in LLM Systems (2025)**
- **URL:** https://arxiv.org/html/2509.14404v1
- **Relevant:** Distills prompt engineering patterns and evaluation frameworks relevant to how specifications are communicated in repair prompts.

---

## **PATCH GENERATION AND VALIDATION STRATEGIES**

### 24. **PAFT: Preservation-Aware Fine-Tuning for Minimal-Edit Program Repair (April 2026)**
- **URL:** https://arxiv.org/html/2604.03113v2
- **Competing Concern:** Notes 41.5% of LLM-generated patches require manual revision. Specification quality likely affects this overfitting problem.

### 25. **ComPass: Contrastive Learning for Automated Patch Correctness Assessment (February 2026)**
- **URL:** https://arxiv.org/html/2602.07561
- **Related:** Addresses patch overfitting due to weak test suites. Specifications could help validate patches beyond test suite passing.

### 26. **Are Benchmark Tests Strong Enough? Mutation-Guided Diagnosis and Augmentation of Regression Suites (April 2026)**
- **URL:** https://arxiv.org/html/2604.01518v1
- **Related:** STING framework uses semantic program variants to uncover test suite weaknesses. Specifications could validate behavioral correctness beyond weak test suites.

### 27. **REFINE: Enhancing Program Repair Agents through Context-Aware Patch Refinement (2025)**
- **URL:** https://arxiv.org/pdf/2510.03588
- **Related:** Context-aware refinement of patches validated against test suites.

### 28. **Root-Cause-Driven Automated Vulnerability Repair (Recent 2026)**
- **URL:** https://arxiv.org/html/2605.04251
- **Related:** Combines agentic fault localization with root-cause analysis to guide patch synthesis.

---

## **SPECIFICATION MINING AND VERIFICATION (Classical APR Context)**

### 29. **Mining Specifications for Predictive Safety Monitoring (CPS-IoT Week 2025)**
- **URL:** https://dl.acm.org/doi/10.1145/3716550.3722021
- **Historical Context:** Classical specification mining for safety properties using Signal Temporal Logic (STL). Shows specification extraction is a long-studied problem in formal methods.

---

## **TEST GENERATION AND BEHAVIORAL VALIDATION**

### 30. **Multi-Step Generation of Test Specifications using Large Language Models (2025 ACL Industry)**
- **URL:** https://aclanthology.org/2025.acl-industry.11.pdf
- **Related:** Generates test specifications using iterative refinement with LLMs.

### 31. **Large Language Models for Unit Test Generation: Achievements, Challenges, and the Road Ahead (2025)**
- **URL:** https://arxiv.org/html/2511.21382v1
- **Context:** Comprehensive study on LLM-based test generation. Shows iterative refinement approaches increase valid test generation from 24% to 70%+.

### 32. **Validating Formal Specifications with LLM-generated Test Cases (October 2025)**
- **URL:** https://arxiv.org/html/2510.23350v1
- **Reciprocal Work:** Uses LLMs to generate test cases that validate formal specifications (reverse direction from SpecExtract, but related).

### 33. **Heterogeneous Prompting and Execution Feedback for SWE Issue Test Generation and Selection (January 2026)**
- **URL:** https://arxiv.org/html/2508.06365
- **Related:** Agentless approach automatically generates reproduction tests from SWE issue descriptions and selects best patches via voting.

---

## **DELTA/DIFFERENCE LEARNING APPROACHES**

### 34. **The Delta Learning Hypothesis: Preference Tuning on Weak Data can Yield Strong Gains (2025)**
- **URL:** https://arxiv.org/html/2507.06187v1
- **Methodological Relevance:** Shows pairing responses with weaker responses (creating a delta) drives learning. SpecExtract's behavioral delta (observed vs. expected) is conceptually similar.

### 35. **Learning Program Behavioral Models from Synthesized Input-Output Pairs (2024-2025)**
- **URL:** https://arxiv.org/pdf/2407.08597
- **Related:** Learns behavioral models from I/O pairs, conceptually related to specification extraction.

---

## **ADVERSARIAL ISSUES: Claims to Address**

The authors should specifically discuss:

1. **Why train a separate spec extractor vs. end-to-end repair?** (SpecFix, VibeRepair, Repeton use different strategies)
2. **Why pre-train specs vs. coevolve them?** (Agent-CoEvo argues dynamic constraint revision is critical)
3. **Why SWE-bench test assertions as training signal vs. SWE-AGI's explicit specifications?** (SWE-AGI provides gold-standard specs, making comparison necessary)
4. **How does this compare to prompting-based approaches?** (Knowledge-Enhanced Repair shows prompting can work without explicit extraction)
5. **Patch overfitting risk:** PAFT (2026) shows 41.5% of patches still need manual revision despite test passage—do specifications help here?

---

## **SUMMARY: Key Competitive Gaps**

**Most Direct Competitors:**
- CodeSpecBench (2026) - Specification generation benchmark using same SWE-bench data
- VibeRepair (2026) - Specification refinement through test-based feedback loops
- Agent-CoEvo (2026) - Dynamic behavioral constraint coevolution during repair
- SWE-AGI (2026) - Explicit, gold-standard specification annotations on SWE-bench tasks

**Methodological Alternatives:**
- SpecFix - Specification repair via execution feedback
- Knowledge-Enhanced Repair - Prompting-based specification leverage
- SWE-Bench Pro/V2 - Structured specification annotations at benchmark level

**Critical for Positioning:** The SWE-AGI benchmark and CodeSpecBench were published in 2026 (recent/concurrent with likely SpecExtract timeline). These represent significant competing and complementary work that should be prominently addressed.

---

## **Sources:**

- [CodeSpecBench: Benchmarking LLMs for Executable Behavioral Specification Generation](https://arxiv.org/html/2604.12268v1)
- [Specification Vibing for Automated Program Repair](https://arxiv.org/html/2602.08263)
- [Understanding Specification-Driven Code Generation with LLMs](https://arxiv.org/html/2601.03878v1)
- [Beyond Fixed Tests: Repository-Level Issue Resolution as Coevolution of Code and Behavioral Constraints](https://arxiv.org/html/2604.04580)
- [Can We Enhance Bug Report Quality Using LLMs?](https://arxiv.org/abs/2504.18804)
- [Automated Repair of Ambiguous Problem Descriptions for LLM-Based Code Generation](https://arxiv.org/html/2505.07270)
- [Knowledge-Enhanced Program Repair for Data Science Code](https://arxiv.org/html/2502.09771v1)
- [Repeton: Structured Bug Repair with ReAct-Guided Patch-and-Test Cycles](https://arxiv.org/html/2506.08173)
- [Agentic Bug Reproduction for Effective Automated Program Repair at Google](https://arxiv.org/html/2502.01821v2)
- [LLPut: Investigating Large Language Models for Bug Report-Based Input Generation](https://arxiv.org/abs/2503.20578)
- [SWE-Bench Pro Leaderboard (2026): Why 46% Beats 81%](https://www.morphllm.com/swe-bench-pro)
- [SWE-rebench V2: Language-Agnostic SWE Task Collection at Scale](https://arxiv.org/html/2602.23866)
- [SWE-bench Goes Live!](https://arxiv.org/html/2505.23419v2)
- [SWE-AGI: Benchmarking Specification-Driven Software](https://www.arxiv.org/pdf/2602.09447)
- [Assessing the Impact of Code Changes on the Fault Localizability of Large Language Models](https://arxiv.org/html/2504.04372)
- [A Survey of LLM-based Automated Program Repair: Taxonomies, Design Paradigms, and Applications](https://arxiv.org/html/2506.23749v1)
- [A Taxonomy of Prompt Defects in LLM Systems](https://arxiv.org/html/2509.14404v1)
- [PAFT: Preservation-Aware Fine-Tuning for Minimal-Edit Program Repair](https://arxiv.org/html/2604.03113v2)
- [ComPass: Contrastive Learning for Automated Patch Correctness Assessment](https://arxiv.org/html/2602.07561)
- [Are Benchmark Tests Strong Enough? Mutation-Guided Diagnosis and Augmentation of Regression Suites](https://arxiv.org/html/2604.01518v1)
- [REFINE: Enhancing Program Repair Agents through Context-Aware Patch Refinement](https://arxiv.org/pdf/2510.03588)
- [Root-Cause-Driven Automated Vulnerability Repair](https://arxiv.org/html/2605.04251)
- [Mining Specifications for Predictive Safety Monitoring](https://dl.acm.org/doi/10.1145/3716550.3722021)
- [Multi-Step Generation of Test Specifications using Large Language Models](https://aclanthology.org/2025.acl-industry.11.pdf)
- [Large Language Models for Unit Test Generation: Achievements, Challenges, and the Road Ahead](https://arxiv.org/html/2511.21382v1)
- [Validating Formal Specifications with LLM-generated Test Cases](https://arxiv.org/html/2510.23350v1)
- [Heterogeneous Prompting and Execution Feedback for SWE Issue Test Generation and Selection](https://arxiv.org/html/2508.06365)
- [The Delta Learning Hypothesis: Preference Tuning on Weak Data can Yield Strong Gains](https://arxiv.org/html/2507.06187v1)
- [Learning Program Behavioral Models from Synthesized Input-Output Pairs](https://arxiv.org/pdf/2407.08597)
- [iFixR: Bug Report driven Program Repair](https://cs.paperswithcode.com/paper/ifixr-bug-report-driven-program-repair)
- [ChatBR: Automated assessment and improvement of bug reports](https://dl.acm.org/doi/pdf/10.1145/3691620.3695518)
- [Uncovering the iceberg from the tip: Generating API Specifications for Bug](https://www.ndss-symposium.org/wp-content/uploads/2025-2001-paper.pdf)
- [What's in a Benchmark? The Case of SWE-Bench in Automated Program Repair](https://arxiv.org/pdf/2602.04449)
- [Introducing SWE-bench Verified](https://openai.com/index/introducing-swe-bench-verified/)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d99c5ef3-688c-4590-8b23-d5b1f7d2829e",
  "isSidechain": true,
  "agentId": "a3d6359a710b9a6ec",
  "requestId": "req_011CatTJpQGBHucS3kytbC9f",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "f8a82d56-3a43-4211-93e3-6e28a6be2a5c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "78f395f4-5c6b-48f5-b7df-f42fdf4d4c8a",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01JG7huHgdtN7RPRJNYrbp1u",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 3726,
      "cache_read_input_tokens": 33137,
      "output_tokens": 5363,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 3726
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 7,
          "output_tokens": 5363,
          "cache_read_input_tokens": 33137,
          "cache_creation_input_tokens": 3726,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 3726,
            "ephemeral_1h_input_tokens": 0
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    }
  }
}
```

</details>

---
