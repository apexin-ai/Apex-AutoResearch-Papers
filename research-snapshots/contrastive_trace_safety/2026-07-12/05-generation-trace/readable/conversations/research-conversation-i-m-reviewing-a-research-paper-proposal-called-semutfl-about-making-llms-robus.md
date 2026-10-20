# Research conversation: I'm reviewing a research paper proposal called "SeMutFL" about making LLMs robust to semantic-preserving code mutations 

**Layer Selection Sensitivity in Hidden-State Safety Probes for Reasoning Models (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 24
- **Recorded user turns:** 1
- **Tool calls:** 10
- **Original source:** `logs/chats/exported-trajectories/account-1/agent-a26c135a0a7f11d02.jsonl`
- **Structured JSON:** [`8a16faf6b83b31477254.json`](../../sessions/8a/8a16faf6b83b31477254.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

24 recorded events

### User

_source line 1 · 2026-05-10T05:38:36.701Z_

I'm reviewing a research paper proposal called "SeMutFL" about making LLMs robust to semantic-preserving code mutations for fault localization. I need to find any competing or related work.

Please search for:

1. "semantic preserving mutation LLM code robustness training 2025 2026" on arXiv
2. "contrastive code representation fault localization 2025 2026" 
3. "SWE-bench fault localization robustness 2025 2026"
4. "code LLM robustness surface form variation training" on arXiv
5. "QLoRA Qwen2.5-Coder fault localization fine-tuning"
6. "InfoNCE contrastive code understanding 2025 2026"
7. site:paperswithcode.com fault localization LLM benchmark SOTA
8. "ContraCode follow-up" OR "code contrastive learning robustness 2025"
9. "DebugBench fault localization" current SOTA
10. Any recent (2025-2026) work combining mutation testing with LLM training for code tasks

The goal is to discover if there's any work that independently addresses the same problem: training LLMs to be robust to code surface-form mutations specifically for fault localization. Report full titles and URLs of anything relevant.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "073f59e2-5eca-44b2-8b49-13d14d4d8dca",
  "agentId": "a26c135a0a7f11d02",
  "type": "user",
  "uuid": "27ac6802-ae2b-4127-aec6-75ee83850a2a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "924d92b4-a5d4-492f-8ca6-f254c2b0392e",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 2 · 2026-05-10T05:38:38.016Z_

I'll search for related and competing work on these topics systematically.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "27ac6802-ae2b-4127-aec6-75ee83850a2a",
  "isSidechain": true,
  "agentId": "a26c135a0a7f11d02",
  "requestId": "req_011CatMDugvXTrQRAKGzihyb",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "7c9a1e0b-193d-4c49-95cb-a4f2729cd0fe",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "924d92b4-a5d4-492f-8ca6-f254c2b0392e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_0184dKt1C8ECwsh9nDfLjgr7",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 733,
      "cache_read_input_tokens": 16155,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 733,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 5,
      "service_tier": "standard",
      "inference_geo": "not_available"
    }
  }
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-10T05:38:38.240Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01V5EjSfZ5JMd6GV2LuhhRaD`</summary>

```json
{
  "query": "semantic preserving mutation LLM code robustness training 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7c9a1e0b-193d-4c49-95cb-a4f2729cd0fe",
  "isSidechain": true,
  "agentId": "a26c135a0a7f11d02",
  "requestId": "req_011CatMDugvXTrQRAKGzihyb",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "b65b0314-5458-4018-86c2-b23d18ef9365",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "924d92b4-a5d4-492f-8ca6-f254c2b0392e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_0184dKt1C8ECwsh9nDfLjgr7",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 733,
      "cache_read_input_tokens": 16155,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 733,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 5,
      "service_tier": "standard",
      "inference_geo": "not_available"
    }
  }
}
```

</details>

---

### Tool call

_source line 4 · 2026-05-10T05:38:38.273Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01XgL6PMeNnxS7aUScvJJsaK`</summary>

```json
{
  "query": "contrastive code representation fault localization 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b65b0314-5458-4018-86c2-b23d18ef9365",
  "isSidechain": true,
  "agentId": "a26c135a0a7f11d02",
  "requestId": "req_011CatMDugvXTrQRAKGzihyb",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "d1639066-3e8e-4a4a-8cfa-2fe0b8b0cefe",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "924d92b4-a5d4-492f-8ca6-f254c2b0392e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_0184dKt1C8ECwsh9nDfLjgr7",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 733,
      "cache_read_input_tokens": 16155,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 733,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 5,
      "service_tier": "standard",
      "inference_geo": "not_available"
    }
  }
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-10T05:38:38.450Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01Eo6WJapBAGEb4hdxjVkedj`</summary>

```json
{
  "query": "SWE-bench fault localization robustness 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d1639066-3e8e-4a4a-8cfa-2fe0b8b0cefe",
  "isSidechain": true,
  "agentId": "a26c135a0a7f11d02",
  "requestId": "req_011CatMDugvXTrQRAKGzihyb",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "09a17134-2936-4acc-bef6-e07d9f6ac29d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "924d92b4-a5d4-492f-8ca6-f254c2b0392e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_0184dKt1C8ECwsh9nDfLjgr7",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 733,
      "cache_read_input_tokens": 16155,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 733,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 5,
      "service_tier": "standard",
      "inference_geo": "not_available"
    }
  }
}
```

</details>

---

### Tool call

_source line 6 · 2026-05-10T05:38:38.709Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_0172MEVbN2ZYb1Rx8p9NuoMU`</summary>

```json
{
  "query": "code LLM robustness surface form variation training"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "09a17134-2936-4acc-bef6-e07d9f6ac29d",
  "isSidechain": true,
  "agentId": "a26c135a0a7f11d02",
  "requestId": "req_011CatMDugvXTrQRAKGzihyb",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "7d654440-8727-44d9-91a7-c08e20b806d9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "924d92b4-a5d4-492f-8ca6-f254c2b0392e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_0184dKt1C8ECwsh9nDfLjgr7",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 733,
      "cache_read_input_tokens": 16155,
      "output_tokens": 282,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 733
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 282,
          "cache_read_input_tokens": 16155,
          "cache_creation_input_tokens": 733,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 733,
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

### Tool call

_source line 7 · 2026-05-10T05:38:38.727Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01Fm1ZVSXYhQcmYTdKeaJbqr`</summary>

```json
{
  "query": "QLoRA Qwen2.5-Coder fault localization fine-tuning"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7d654440-8727-44d9-91a7-c08e20b806d9",
  "isSidechain": true,
  "agentId": "a26c135a0a7f11d02",
  "requestId": "req_011CatMDugvXTrQRAKGzihyb",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "6bd7220d-58b2-41ad-b4d3-188df2922aae",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "924d92b4-a5d4-492f-8ca6-f254c2b0392e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_0184dKt1C8ECwsh9nDfLjgr7",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 733,
      "cache_read_input_tokens": 16155,
      "output_tokens": 282,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 733
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 282,
          "cache_read_input_tokens": 16155,
          "cache_creation_input_tokens": 733,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 733,
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

_source line 8 · 2026-05-10T05:38:44.597Z_

<details><summary>↩ Tool result · `toolu_01Fm1ZVSXYhQcmYTdKeaJbqr`</summary>

```text
Web search results for query: "QLoRA Qwen2.5-Coder fault localization fine-tuning"

Links: [{"title":"Qwen2.5 QLoRA, LoRA, and Full Fine-tuning on Your Computer","url":"https://kaitchup.substack.com/p/qwen25-qlora-lora-and-full-fine-tuning"},{"title":"Fine-Tune and Deploy Qwen2.5 - Coder with SFT & DPO on PAI - Alibaba Cloud","url":"https://www.alibabacloud.com/help/en/pai/use-cases/training-evaluation-compression-and-deployment-of-qwen2-5-coder-model"},{"title":"GitHub - risenfromashes/qwen-finetune · GitHub","url":"https://github.com/risenfromashes/qwen-finetune"},{"title":"Complete Guide to Fine-tuning Qwen2.5 VL Model - F22 Labs","url":"https://www.f22labs.com/blogs/complete-guide-to-fine-tuning-qwen2-5-vl-model/"},{"title":"Qwen 2.5 Coder Fine-tuning with Unsloth","url":"https://unsloth.ai/blog/qwen-coder"},{"title":"(Qwen LLM fine-tuning via QLoRA) Chat Assistant","url":"https://www.kaggle.com/code/kongkaifeng/qwen-llm-fine-tuning-via-qlora-chat-assistant"},{"title":"amazon-sagemaker-llm-fine-tuning-remote-decorator/qwen/qwen-2.5-7b-qlora-fsdp-remote-decorator_qa.ipynb at main · aws-samples/amazon-sagemaker-llm-fine-tuning-remote-decorator","url":"https://github.com/aws-samples/amazon-sagemaker-llm-fine-tuning-remote-decorator/blob/main/qwen/qwen-2.5-7b-qlora-fsdp-remote-decorator_qa.ipynb"},{"title":"Qwen2 QLoRA Fine-tuning and Quantization - Colab - Google","url":"https://colab.research.google.com/drive/14rfhWDc-ZqMmVgzPIAywcocceMEWy0as"},{"title":"notebooks/notebooks/how-to-finetune-qwen2-5-vl-for-json-data-extraction.ipynb at main · roboflow/notebooks","url":"https://github.com/roboflow/notebooks/blob/main/notebooks/how-to-finetune-qwen2-5-vl-for-json-data-extraction.ipynb"},{"title":"Fine-Tuning Qwen-2.5-Coder-14B LLM (SFT, PEFT)","url":"https://www.kaggle.com/code/ksmooi/fine-tuning-qwen-2-5-coder-14b-llm-sft-peft/notebook"}]

Based on the search results, I found several resources related to QLoRA and Qwen2.5-Coder fine-tuning, though the specific combination of all three terms (QLoRA, Qwen2.5-Coder, and fault localization) doesn't appear to have dedicated research papers in the top results. Here's what I found:

## QLoRA and Qwen2.5-Coder Fine-tuning

LLaMA Factory supports fine-tuning the Qwen2.5 models, and there is support for FSDP+QLoRA that fine-tunes a 70B model on 2x24GB GPUs.

For the Qwen2.5-Coder specifically, Qwen2.5-Coder models (0.5B to 32B) are optimized for code generation, completion, and repair across 92 programming languages. Model Gallery includes built-in supervised fine-tuning (SFT) and direct preference optimization (DPO) algorithms for Qwen2.5-Coder-32B-Instruct.

QLoRA (Quantized LoRA) further reduces memory usage by quantizing the base model to 4 bits, while preserving performance, making it suitable for fine-tuning these models on resource-constrained hardware.

However, I did not find specific research or documentation on fault localization fine-tuning with QLoRA and Qwen2.5-Coder in these results. If you're looking for more specialized information on fault localization applications, you may want to search for academic papers or technical reports on this topic.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "6bd7220d-58b2-41ad-b4d3-188df2922aae",
  "isSidechain": true,
  "promptId": "073f59e2-5eca-44b2-8b49-13d14d4d8dca",
  "agentId": "a26c135a0a7f11d02",
  "type": "user",
  "uuid": "b8b6f187-a907-4590-9007-68c8ba5ee98b",
  "sourceToolAssistantUUID": "6bd7220d-58b2-41ad-b4d3-188df2922aae",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "924d92b4-a5d4-492f-8ca6-f254c2b0392e",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 9 · 2026-05-10T05:38:44.601Z_

<details><summary>↩ Tool result · `toolu_01XgL6PMeNnxS7aUScvJJsaK`</summary>

```text
Web search results for query: "contrastive code representation fault localization 2025 2026"

Links: [{"title":"Multi-view adaptive contrastive learning for information retrieval based fault localization | Automated Software Engineering | Springer Nature Link","url":"https://link.springer.com/article/10.1007/s10515-025-00573-x"},{"title":"CoverFL: Enhancing Fault Localization via Deep Coverage Relation | ACM Transactions on Software Engineering and Methodology","url":"https://dl.acm.org/doi/10.1145/3787964"},{"title":"SupConFL: Fault Localization with Supervised Contrastive Learning | Request PDF","url":"https://www.researchgate.net/publication/374494097_SupConFL_Fault_Localization_with_Supervised_Contrastive_Learning"},{"title":"GCFR: graph contrastive fault representation for robust diagnosis in power communication networks | Scientific Reports","url":"https://www.nature.com/articles/s41598-025-23457-2"},{"title":"SupConFL: Fault Localization with Supervised Contrastive Learning | Proceedings of the 14th Asia-Pacific Symposium on Internetware","url":"https://dl.acm.org/doi/10.1145/3609437.3609441"},{"title":"GitHub - iSEngLab/AwesomeLLM4SE: [SCIS 2025] A Survey on Large Language Models for Software Engineering · GitHub","url":"https://github.com/iSEngLab/AwesomeLLM4SE"},{"title":"ml4se/README.md at master · saltudelft/ml4se","url":"https://github.com/saltudelft/ml4se/blob/master/README.md"},{"title":"Representation Learning for Fault Diagnosis with Contrastive Predictive Coding | IEEE Conference Publication | IEEE Xplore","url":"https://ieeexplore.ieee.org/document/9693550/"},{"title":"Towards Better Graph Neural Network-Based Fault Localization through Enhanced Code Representation | Proceedings of the ACM on Software Engineering","url":"https://dl.acm.org/doi/abs/10.1145/3660793"},{"title":"Pre-training Code Representation with Semantic Flow Graph for","url":"http://www.lamda.nju.edu.cn/duyl/paper/fse23-duyl.pdf"}]

Based on the search results, I found several relevant papers and developments on contrastive code representation and fault localization from 2025-2026:

## Recent Advances in Contrastive Learning for Fault Localization

**Multi-View Adaptive Contrastive Learning (MACL-IRFL)**
A novel approach named Multi-View Adaptive Contrastive Learning for Information Retrieval Fault Localization (MACL-IRFL) was proposed to learn relationships for software fault localization. This work was published in 2026 in Automated Software Engineering. Results show the model can improve over the best baseline up to 28.93%, 25.57% and 20.35% on Accuracy@1, MAP and MRR, respectively.

**Graph Contrastive Learning for Fault Localization**
A novel graph contrastive learning technique was devised to facilitate the discovery of profound links between faulty code components and failed test cases. This work (CoverFL) was accepted on December 28, 2025, with online publication on March 6, 2026.

**Supervised Contrastive Learning (SupConFL)**
Training through contrastive learning between faulty code and its fixed version allows the model to learn richer features of faulty code elements.

## Related Areas

Additional 2025-2026 research includes work on graph neural networks for fault localization with enhanced code representations and application of contrastive learning to program representation more broadly.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d1639066-3e8e-4a4a-8cfa-2fe0b8b0cefe",
  "isSidechain": true,
  "promptId": "073f59e2-5eca-44b2-8b49-13d14d4d8dca",
  "agentId": "a26c135a0a7f11d02",
  "type": "user",
  "uuid": "18bfab2b-d48a-4778-8042-fa5f65a8a4eb",
  "sourceToolAssistantUUID": "d1639066-3e8e-4a4a-8cfa-2fe0b8b0cefe",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "924d92b4-a5d4-492f-8ca6-f254c2b0392e",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-10T05:38:45.160Z_

<details><summary>↩ Tool result · `toolu_01V5EjSfZ5JMd6GV2LuhhRaD`</summary>

```text
Web search results for query: "semantic preserving mutation LLM code robustness training 2025 2026"

Links: [{"title":"Accepted at the 2026 IEEE International Conference on Software Testing, Verification and Validation (ICST 2026) Assessing the Impact of Code Changes on the Fault Localizability of Large Language Models","url":"https://arxiv.org/html/2504.04372"},{"title":"[2504.04372v3] Assessing the Impact of Code Changes on the Fault Localizability of Large Language Models","url":"https://arxiv.org/abs/2504.04372v3"},{"title":"DeepSeek Robustness Against Semantic-Character Dual-Space Mutated Prompt Injection","url":"https://arxiv.org/html/2604.12548"},{"title":"[2504.04372] Assessing the Impact of Code Changes on the Fault Localizability of Large Language Models","url":"https://arxiv.org/abs/2504.04372"},{"title":"Detecting LLM-generated Code with Subtle Modification by Adversarial Training","url":"https://arxiv.org/pdf/2507.13123"},{"title":"Assessing and improving syntactic adversarial robustness ...","url":"https://chentaolue.github.io/pub-papers/ist25.pdf"},{"title":"GitHub - iSEngLab/AwesomeLLM4SE: [SCIS 2025] A Survey on Large Language Models for Software Engineering · GitHub","url":"https://github.com/iSEngLab/AwesomeLLM4SE"},{"title":"Improving LLM-Generated Code via Genetic Improvement","url":"https://ceur-ws.org/Vol-4121/Ital-IA_2025_paper_111.pdf"},{"title":"How Accurately Do Large Language Models Understand Code?","url":"https://tahakhan.net/files/haroon_arxiv_25.pdf"},{"title":"Are Large Language Models Robust in Understanding Code Against","url":"https://arxiv.org/pdf/2505.10443"}]

I found several highly relevant research papers on semantic-preserving mutations for LLM code robustness. Here's a summary of the key findings:

## Recent Research on Semantic-Preserving Mutations and LLM Code Robustness

### Major Findings (2025-2026)

The first large-scale empirical investigation into LLM fault localization robustness was presented at the 2026 IEEE International Conference on Software Testing, Verification and Validation (ICST 2026), developing an end-to-end evaluation framework addressing data contamination, scalability, automation, and extensibility.

### Impact of Semantic-Preserving Mutations

Semantic-preserving mutations (SPMs) that preserve program behavior include identifier renaming, comment insertion or modification, formatting changes, and dead-code insertion. The research reveals concerning robustness issues:

- Applying SPMs causes LLMs to fail to localize the same fault in 78% of cases
- Misleading comments and dead code account for the majority of robustness loss, with dead code alone reducing average accuracy to 20.38%
- Fault localization accuracy drops by 1.04% per mutation step in Java and 1.93% per step in Python, indicating compounding semantic interference

### Related 2025 Research

Recent work assesses model robustness by applying semantics-preserving code mutations and analyzing output prediction consistency, testing whether LLMs' understanding of code is robust to syntactic changes.

These findings highlight that even simple semantic-preserving mutations are sufficient to throw off LLMs' reasoning capabilities.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "b65b0314-5458-4018-86c2-b23d18ef9365",
  "isSidechain": true,
  "promptId": "073f59e2-5eca-44b2-8b49-13d14d4d8dca",
  "agentId": "a26c135a0a7f11d02",
  "type": "user",
  "uuid": "3f3c889d-9c02-4274-ac3e-77f85d4094d2",
  "sourceToolAssistantUUID": "b65b0314-5458-4018-86c2-b23d18ef9365",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "924d92b4-a5d4-492f-8ca6-f254c2b0392e",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 11 · 2026-05-10T05:38:46.667Z_

<details><summary>↩ Tool result · `toolu_0172MEVbN2ZYb1Rx8p9NuoMU`</summary>

```text
Web search results for query: "code LLM robustness surface form variation training"

Links: [{"title":"[2603.17017] LLM NL2SQL Robustness: Surface Noise vs. Linguistic Variation in Traditional and Agentic Settings","url":"https://arxiv.org/abs/2603.17017"},{"title":"Towards Robust LLM Post-Training: Automatic Failure Management for Reinforcement Fine-Tuning","url":"https://arxiv.org/html/2605.04431"},{"title":"LLM NL2SQL Robustness: Surface Noise vs. Linguistic Variation in Traditional and Agentic Settings","url":"https://arxiv.org/html/2603.17017"},{"title":"Measuring Representation Robustness in Large Language Models for Geometry","url":"https://arxiv.org/html/2604.16421"},{"title":"Memorize or Generalize? Evaluating LLM Code Generation with Code Rewriting","url":"https://arxiv.org/html/2503.02296"},{"title":"Foundations of LLM Knowledge Materialization: Termination, Reproducibility, Robustness","url":"https://arxiv.org/html/2510.06780"},{"title":"Enhancing the Robustness of LLM-Generated Code: Empirical Study and Framework","url":"https://arxiv.org/html/2503.20197v1"},{"title":"GitHub - Hypogenic-AI/robustness-vs-artifacts-21e9-claude: Probing the Robustness Trap: Distinguishing True Model Resilience from Experimental Artifacts in LLM Misalignment Training | Generated by NeuriCo on 2026-04-20 · GitHub","url":"https://github.com/Hypogenic-AI/robustness-vs-artifacts-21e9-claude"},{"title":"Beyond Capable: Accuracy, Calibration, and Robustness in Large Language Models","url":"https://www.sei.cmu.edu/blog/beyond-capable-accuracy-calibration-and-robustness-in-large-language-models/"},{"title":"Prompt Variability Effects On LLM Code Generation","url":"https://arxiv.org/html/2506.10204v1"}]

I found several relevant research papers and resources on LLM robustness and surface form variation. Here's what the search reveals:

## Key Findings:

**NL2SQL Robustness Studies:**
Models exhibit notable performance degradation for surface-level noise (e.g., character-level corruption) and linguistic variation that preserves semantics while altering lexical or syntactic forms. Performance drops the most under ButterFinger (random typos) and back translation, Chinese translation perturbations.

**Code Generation and Memorization:**
Research on code LLMs specifically examines robustness to variations. Mutation induces moderate drops; paraphrase is nearly invariant; rewrites are most disruptive—especially on BigCodeBench—suggesting harmful memorization beyond surface-level robustness.

**Representation Robustness:**
Beyond surface forms, LLMs' robustness to equivalent problem representations remains poorly understood. In geometry, identical problems can be expressed in Euclidean, coordinate, or vector forms, but existing benchmarks report accuracy on fixed formats, implicitly assuming representation invariance.

**Training Robustness:**
RFT-FM better captures structured deviations specific to RFT training, rather than relying only on easily separable surface-level anomalies.

**Prompt Variability:**
Recent research investigated robustness of code LLMs to variations expected in real world application, identifying 18 categories of perturbations such as extra space outside of words.

The research indicates that while LLMs maintain strong performance on standard benchmarks, they show vulnerability to surface form variations and linguistic changes that preserve semantic meaning.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "7d654440-8727-44d9-91a7-c08e20b806d9",
  "isSidechain": true,
  "promptId": "073f59e2-5eca-44b2-8b49-13d14d4d8dca",
  "agentId": "a26c135a0a7f11d02",
  "type": "user",
  "uuid": "4055d210-f12c-4786-821d-f92c16466d07",
  "sourceToolAssistantUUID": "7d654440-8727-44d9-91a7-c08e20b806d9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "924d92b4-a5d4-492f-8ca6-f254c2b0392e",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-10T05:38:49.136Z_

<details><summary>↩ Tool result · `toolu_01Eo6WJapBAGEb4hdxjVkedj`</summary>

```text
Web search results for query: "SWE-bench fault localization robustness 2025 2026"

Links: [{"title":"Introducing SWE-bench Verified | OpenAI","url":"https://openai.com/index/introducing-swe-bench-verified/"},{"title":"Dissecting the SWE-Bench Leaderboards: Profiling Submitters and Architectures of LLM- and Agent-Based Repair Systems","url":"https://arxiv.org/html/2506.17208v2"},{"title":"SWE-bench Verified Issues Benchmark","url":"https://www.emergentmind.com/topics/swe-bench-verified-issues"},{"title":"Dissecting the SWE-Bench Leaderboards: Profiling Submitters and","url":"https://arxiv.org/pdf/2506.17208"},{"title":"SWE-bench Verified","url":"https://www.vals.ai/benchmarks/swebench"},{"title":"Published as a conference paper at ICLR 2024 SWE-BENCH:","url":"https://arxiv.org/pdf/2310.06770"},{"title":"SWE-Bench Leaderboards","url":"https://www.emergentmind.com/topics/swe-bench-leaderboards"},{"title":"GitHub - microsoft/SWE-bench-Live: [NeurIPS 2025 D&B] 🚀 SWE-bench Goes Live!","url":"https://github.com/microsoft/SWE-bench-Live"},{"title":"SWE-Bench Verified Benchmark Leaderboard","url":"https://llm-stats.com/benchmarks/swe-bench-verified"},{"title":"SWE-bench Goes Live!","url":"https://arxiv.org/html/2505.23419v2"}]

I've completed a web search for "SWE-bench fault localization robustness 2025 2026". Here are the key findings:

## Robustness Concerns

OpenAI aimed to improve the robustness and reliability of the SWE-bench benchmark, identifying several critical issues. The unit tests used to evaluate solutions are often overly specific, and in some cases unrelated to the issue, potentially causing correct solutions to be rejected. Additionally, many samples have underspecified issue descriptions, leading to ambiguity on what the problem is and how it should be solved.

## Fault Localization Approaches

Recent 2025 work has focused on improving fault localization. CodeFuse-AAIS proposes adaptive fault localization and expansion of the sampling space by combining multiple LLMs. OrcaLoca + Agentless-1.5 incorporates an approach focused on file and function localization that introduces a dynamic action scheduling system producing actions at varying levels of granularity and prioritizing them based on contextual relevance and urgency.

## Contamination and Data Quality Issues

SWE-Bench-Verified overlaps significantly with LLM pretraining data, with models being 3–6× more accurate in localizing bug locations on this benchmark than on held-out or decontaminated sets, with reported contamination rates reaching 8–10%. Over 15% of instances in SWE-bench Verified require augmentation due to incomplete test patches, and advanced frameworks have revealed that leaderboard success rates may be inflated by 6–7 absolute percentage points due to latent test inadequacies.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "09a17134-2936-4acc-bef6-e07d9f6ac29d",
  "isSidechain": true,
  "promptId": "073f59e2-5eca-44b2-8b49-13d14d4d8dca",
  "agentId": "a26c135a0a7f11d02",
  "type": "user",
  "uuid": "e3e40419-585b-47a9-a50c-865b5c093c48",
  "sourceToolAssistantUUID": "09a17134-2936-4acc-bef6-e07d9f6ac29d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "924d92b4-a5d4-492f-8ca6-f254c2b0392e",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 13 · 2026-05-10T05:38:50.496Z_

Now let me continue with the remaining searches:

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e3e40419-585b-47a9-a50c-865b5c093c48",
  "isSidechain": true,
  "agentId": "a26c135a0a7f11d02",
  "requestId": "req_011CatMEpnX6z3YSjLJXf8gZ",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "74ae67dc-4968-450e-9de3-c1e5a8f20471",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "924d92b4-a5d4-492f-8ca6-f254c2b0392e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_016z9bTS1mi5QEmEu9XYqfVw",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2143,
      "cache_creation_input_tokens": 3803,
      "cache_read_input_tokens": 16888,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3803,
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

_source line 14 · 2026-05-10T05:38:50.700Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_0193Zd5JmxV5c79QU8o8raTe`</summary>

```json
{
  "query": "InfoNCE contrastive code understanding 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "74ae67dc-4968-450e-9de3-c1e5a8f20471",
  "isSidechain": true,
  "agentId": "a26c135a0a7f11d02",
  "requestId": "req_011CatMEpnX6z3YSjLJXf8gZ",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "9bc5d52a-f2f1-4815-976e-20ca36c9a7d7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "924d92b4-a5d4-492f-8ca6-f254c2b0392e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_016z9bTS1mi5QEmEu9XYqfVw",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2143,
      "cache_creation_input_tokens": 3803,
      "cache_read_input_tokens": 16888,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3803,
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

_source line 15 · 2026-05-10T05:38:51.148Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01PnncvV69NNgyhTTg2TfTRu`</summary>

```json
{
  "query": "site:paperswithcode.com fault localization LLM benchmark SOTA"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9bc5d52a-f2f1-4815-976e-20ca36c9a7d7",
  "isSidechain": true,
  "agentId": "a26c135a0a7f11d02",
  "requestId": "req_011CatMEpnX6z3YSjLJXf8gZ",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "7f4f7c89-65fc-426e-9528-67e9d12d73e0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "924d92b4-a5d4-492f-8ca6-f254c2b0392e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_016z9bTS1mi5QEmEu9XYqfVw",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2143,
      "cache_creation_input_tokens": 3803,
      "cache_read_input_tokens": 16888,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3803,
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

_source line 16 · 2026-05-10T05:38:51.580Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01HLdNnzo4c47hWxYEKAUuTB`</summary>

```json
{
  "query": "ContraCode follow-up OR code contrastive learning robustness 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7f4f7c89-65fc-426e-9528-67e9d12d73e0",
  "isSidechain": true,
  "agentId": "a26c135a0a7f11d02",
  "requestId": "req_011CatMEpnX6z3YSjLJXf8gZ",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "4eb54a6e-9b1b-4c8a-b81a-4a24d80761b0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "924d92b4-a5d4-492f-8ca6-f254c2b0392e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_016z9bTS1mi5QEmEu9XYqfVw",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2143,
      "cache_creation_input_tokens": 3803,
      "cache_read_input_tokens": 16888,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3803,
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

_source line 17 · 2026-05-10T05:38:51.813Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_011BAppRfSc7ZUoPpYVmYHBw`</summary>

```json
{
  "query": "DebugBench fault localization current SOTA"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4eb54a6e-9b1b-4c8a-b81a-4a24d80761b0",
  "isSidechain": true,
  "agentId": "a26c135a0a7f11d02",
  "requestId": "req_011CatMEpnX6z3YSjLJXf8gZ",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "2ef4b57b-a7e3-46e1-8765-a5fb51ef13d7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "924d92b4-a5d4-492f-8ca6-f254c2b0392e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_016z9bTS1mi5QEmEu9XYqfVw",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2143,
      "cache_creation_input_tokens": 3803,
      "cache_read_input_tokens": 16888,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3803,
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

_source line 18 · 2026-05-10T05:38:52.039Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01KiznqPgJDCdcBowRaBYhm8`</summary>

```json
{
  "query": "mutation testing LLM training code tasks 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2ef4b57b-a7e3-46e1-8765-a5fb51ef13d7",
  "isSidechain": true,
  "agentId": "a26c135a0a7f11d02",
  "requestId": "req_011CatMEpnX6z3YSjLJXf8gZ",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "2d4bdcb2-1819-4f59-89b4-220c5b677d32",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "924d92b4-a5d4-492f-8ca6-f254c2b0392e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_016z9bTS1mi5QEmEu9XYqfVw",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2143,
      "cache_creation_input_tokens": 3803,
      "cache_read_input_tokens": 16888,
      "output_tokens": 271,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 3803
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2143,
          "output_tokens": 271,
          "cache_read_input_tokens": 16888,
          "cache_creation_input_tokens": 3803,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 3803,
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

_source line 19 · 2026-05-10T05:38:57.476Z_

<details><summary>↩ Tool result · `toolu_01PnncvV69NNgyhTTg2TfTRu`</summary>

```text
Web search results for query: "site:paperswithcode.com fault localization LLM benchmark SOTA"

Links: [{"title":"Fault localization","url":"https://paperswithcode.com/task/fault-localization/codeless"},{"title":"Papers with Code - AgentFL: Scaling LLM-based Fault Localization to Project-Level Context","url":"https://cs.paperswithcode.com/paper/agentfl-scaling-llm-based-fault-localization"},{"title":"MBPP Benchmark (Code Generation)","url":"https://paperswithcode.com/sota/code-generation-on-mbpp"},{"title":"ICAT LLM bias Benchmark (Bias Detection)","url":"https://paperswithcode.com/sota/bias-detection-on-icat-llm-bias"},{"title":"Papers with Code - Fault localization","url":"https://paperswithcode.com/task/fault-localization/latest"},{"title":"TruthfulQA Benchmark (Question Answering)","url":"https://paperswithcode.com/sota/question-answering-on-truthfulqa"},{"title":"AudioCaps Benchmark (Audio Generation)","url":"https://paperswithcode.com/sota/audio-generation-on-audiocaps"},{"title":"VideoInstruct Benchmark (Video-based Generative ...","url":"https://paperswithcode.com/sota/video-based-generative-performance?p=vtimellm-empower-llm-to-grasp-video-moments"},{"title":"AIME24 Benchmark (Mathematical Reasoning)","url":"https://paperswithcode.com/sota/mathematical-reasoning-on-aime24"},{"title":"LRS3-TED Benchmark (Lipreading)","url":"https://paperswithcode.com/sota/lipreading-on-lrs3-ted"}]

Based on the search results, I found relevant information about LLM-based fault localization research on Papers with Code:

## Key Findings

AgentFL is a multi-agent system based on ChatGPT for automated fault localization. AgentFL models the fault localization task as a three-step process, which involves comprehension, navigation, and confirmation.

Existing LLM-based fault localization remains on localizing bugs within a small code scope (i.e., a method or a class), which struggles to diagnose bugs for a large code scope (i.e., an entire software system).

The evaluation on the widely used Defects4J-V1.2.0 benchmark shows that AgentFL can localize 157 out of 395 bugs.

Additionally, LLMAO is the first language model based fault localization approach that locates buggy lines of code without any test coverage information.

The search results also show recent papers on fault localization approaches using LLMs, though specific SOTA (State-of-the-Art) performance metrics across all benchmarks weren't fully detailed in the returned snippets.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "7f4f7c89-65fc-426e-9528-67e9d12d73e0",
  "isSidechain": true,
  "promptId": "073f59e2-5eca-44b2-8b49-13d14d4d8dca",
  "agentId": "a26c135a0a7f11d02",
  "type": "user",
  "uuid": "92368b2e-a0f0-4d54-91ac-ba3c7b49d629",
  "sourceToolAssistantUUID": "7f4f7c89-65fc-426e-9528-67e9d12d73e0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "924d92b4-a5d4-492f-8ca6-f254c2b0392e",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-10T05:38:57.603Z_

<details><summary>↩ Tool result · `toolu_0193Zd5JmxV5c79QU8o8raTe`</summary>

```text
Web search results for query: "InfoNCE contrastive code understanding 2025 2026"

Links: [{"title":"Contrastive Learning for Retrieval: InfoNCE & DPR Guide - Interactive | Michael Brenndoerfer | Michael Brenndoerfer","url":"https://mbrenndoerfer.com/writing/contrastive-learning-retrieval-infonce-dpr"},{"title":"Contrastive Representation Learning | Lil'Log","url":"https://lilianweng.github.io/posts/2021-05-31-contrastive/"},{"title":"InfoNCE: Contrastive Loss for Representation Learning","url":"https://www.emergentmind.com/topics/infonce"},{"title":"Contrastive Learning for Beginners: InfoNCE Loss Explained in Details | by Allen Liang | Medium","url":"https://medium.com/@mlshark/infonce-explained-in-details-and-implementations-902f28199ce6"},{"title":"$f$-MICL: Understanding and Generalizing InfoNCE-based Contrastive Learning | OpenReview","url":"https://openreview.net/forum?id=ZD03VUZmRx"},{"title":"GitHub - RElbers/info-nce-pytorch: PyTorch implementation of the InfoNCE loss for self-supervised learning. · GitHub","url":"https://github.com/RElbers/info-nce-pytorch"},{"title":"Contrastive Learning Loss: NT-Xent & InfoNCE | by Frederik vom Lehn | Self-Supervised Learning | Medium","url":"https://medium.com/self-supervised-learning/nt-xent-loss-normalized-temperature-scaled-cross-entropy-loss-ea5a1ede7c40"},{"title":"[2407.00143] InfoNCE: Identifying the Gap Between Theory and Practice","url":"https://arxiv.org/abs/2407.00143"},{"title":"[2505.06282] InfoNCE is a Free Lunch for Semantically guided Graph Contrastive Learning","url":"https://arxiv.org/abs/2505.06282"},{"title":"Full Guide to Contrastive Learning | Encord","url":"https://encord.com/blog/guide-to-contrastive-learning/"}]

Based on the search results, here's what I found about InfoNCE and contrastive code understanding in recent research (2025-2026):

## Overview of InfoNCE

InfoNCE is a contrastive loss function that frames unsupervised learning as an instance discrimination problem, effectively estimating a lower bound on mutual information. InfoNCE loss maximizes the agreement between positive samples and minimizes the agreement between negative samples in the learned representation space.

## Recent Applications and Developments (2025-2026)

**Code Understanding Challenges**: In code search and large language pre-training corpora, excessive negatives under label noise produce misleading loss signals, especially when semantically similar (but non-augmented) negatives are included.

**Addressing Label Noise**: Weighted variants such as Soft-InfoNCE and InfoNCE+ assign real-valued weights to negatives according to estimated similarity or sampling distribution, thus regularizing representation learning and improving retrieval metrics.

**Theoretical Advances**: Recent 2025 work includes the Symmetric InfoNCE (SymNCE) loss which adds a reverse term to the objective, canceling the dependence and provably ensuring robustness to label noise. Additionally, AnInfoNCE is a generalization of InfoNCE that can provably uncover latent factors in anisotropic settings, broadly generalizing previous identifiability results in contrastive learning.

The search results indicate active research into improving InfoNCE for practical applications, particularly in handling the challenges of code understanding and representation learning in noisy settings.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "9bc5d52a-f2f1-4815-976e-20ca36c9a7d7",
  "isSidechain": true,
  "promptId": "073f59e2-5eca-44b2-8b49-13d14d4d8dca",
  "agentId": "a26c135a0a7f11d02",
  "type": "user",
  "uuid": "7553df41-3b00-4ac8-adf4-3721dfadc4c7",
  "sourceToolAssistantUUID": "9bc5d52a-f2f1-4815-976e-20ca36c9a7d7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "924d92b4-a5d4-492f-8ca6-f254c2b0392e",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 21 · 2026-05-10T05:38:57.961Z_

<details><summary>↩ Tool result · `toolu_011BAppRfSc7ZUoPpYVmYHBw`</summary>

```text
Web search results for query: "DebugBench fault localization current SOTA"

Links: [{"title":"GitHub - CUHK-Shenzhen-SE/D4C: [ICSE'25] Aligning the Objective of LLM-based Program Repair","url":"https://github.com/CUHK-Shenzhen-SE/D4C"},{"title":"Aligning LLMs for FL-free Program Repair","url":"https://arxiv.org/html/2404.08877v1"},{"title":"Aligning the Objective of LLM-based Program Repair","url":"https://arxiv.org/html/2404.08877"},{"title":"Software Fault Localization through Aggregation-Based Neural Ranking for Static and Dynamic Features Selection - PMC","url":"https://pmc.ncbi.nlm.nih.gov/articles/PMC8587821/"},{"title":"Benchmarking and Enhancing LLM Agents in Localizing Linux Kernel Bugs","url":"https://arxiv.org/html/2505.19489"},{"title":"1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29","url":"https://arxiv.org/pdf/2405.20848"},{"title":"Impact of Large Language Models of Code on Fault Localization","url":"https://arxiv.org/html/2408.09657v1"},{"title":"Debugging with Open-Source Large Language Models: An Evaluation","url":"https://arxiv.org/html/2409.03031v1"},{"title":"Interactive Fault Localization Using Test Information | Journal of Computer Science and Technology | Springer Nature Link","url":"https://link.springer.com/article/10.1007/s11390-009-9270-z"},{"title":"Debugging with Open-Source Large Language Models: An Evaluation | Proceedings of the 18th ACM/IEEE International Symposium on Empirical Software Engineering and Measurement","url":"https://dl.acm.org/doi/10.1145/3674805.3690758"}]

Based on the search results, here's what I found about DebugBench fault localization current state-of-the-art:

## Current SOTA on DebugBench

D4C is a straightforward prompting framework for automated program repair that can repair bugs correctly with each patch being sampled only 10 times, surpassing SOTA APR methods with perfect fault localization by 10%. This research was published in early 2024.

The D4C framework's evaluation results on two widely used benchmarks (Defects4J and DebugBench) have demonstrated its effectiveness.

## Open-Source LLM Performance on DebugBench

For open-source models specifically, open-source LLMs achieved scores ranging from 43.9% to 66.6% with DeepSeek-Coder achieving the best score for all three programming languages when evaluated on DebugBench.

## Key Insight About Fault Localization

LLMs can end-to-end locate and repair bugs by using diverse types of artifacts (e.g., failed tests, error messages, and code comments) in a human-like manner can further improve its APR performance, moving away from traditional statement-level fault localization approaches.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "2ef4b57b-a7e3-46e1-8765-a5fb51ef13d7",
  "isSidechain": true,
  "promptId": "073f59e2-5eca-44b2-8b49-13d14d4d8dca",
  "agentId": "a26c135a0a7f11d02",
  "type": "user",
  "uuid": "f91d2176-3c0a-4b98-91de-c17b3ca9d531",
  "sourceToolAssistantUUID": "2ef4b57b-a7e3-46e1-8765-a5fb51ef13d7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "924d92b4-a5d4-492f-8ca6-f254c2b0392e",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 22 · 2026-05-10T05:38:58.121Z_

<details><summary>↩ Tool result · `toolu_01HLdNnzo4c47hWxYEKAUuTB`</summary>

```text
Web search results for query: "ContraCode follow-up OR code contrastive learning robustness 2025"

Links: [{"title":"Contrastive Code Representation Learning","url":"https://arxiv.org/pdf/2007.04973v3"},{"title":"Contrastive Code Representation Learning | OpenReview","url":"https://openreview.net/forum?id=uV7hcsjqM-"},{"title":"ContraBERT: Enhancing Code Pre-trained Models via Contrastive Learning","url":"https://arxiv.org/pdf/2301.09072"},{"title":"[2007.04973] Contrastive Code Representation Learning","url":"https://ar5iv.labs.arxiv.org/html/2007.04973"},{"title":"Contrastive Code Representation Learning","url":"https://parasj.github.io/contracode/"},{"title":"[2007.04973] Contrastive Code Representation Learning","url":"https://arxiv.org/abs/2007.04973"},{"title":"Contrastive Code Representation Learning","url":"https://aclanthology.org/2021.emnlp-main.482.pdf"},{"title":"GitHub - parasj/contracode: Contrastive Code Representation Learning: functionality-based JavaScript embeddings through self-supervised learning","url":"https://github.com/parasj/contracode"},{"title":"CONTRASTIVE CODE REPRESENTATION LEARNING","url":"https://openreview.net/pdf?id=uV7hcsjqM-"},{"title":"ContraBERT: Enhancing Code Pre-Trained Models via Contrastive Learning | Proceedings of the 45th International Conference on Software Engineering","url":"https://dl.acm.org/doi/abs/10.1109/ICSE48619.2023.00207"}]

Based on the search results, I found relevant information about ContraCode and contrastive learning for code robustness. Here's what I found:

## ContraCode: Contrastive Code Representation Learning

ContraCode is a self-supervised algorithm for learning task-agnostic semantic representations of programs via contrastive learning. ContraCode optimizes for a representation that is invariant to semantic-preserving code transformations.

### How It Works

ContraCode develops an automated source-to-source compiler that generates textually divergent variants of source programs, then trains a neural network to identify variants of anchor programs within a large batch of non-equivalent negatives, requiring the network to extract features representing the functionality, not form, of the program.

### Performance and Robustness

Contrastive pre-training with ContraCode learns a more robust representation of functionality that is consistent across code transforms. Contrastive pre-training outperforms RoBERTa on an adversarial code clone detection benchmark by 39% AUROC, and improved adversarial robustness translates to better accuracy over natural code with improvements to summarization and TypeScript type inference accuracy by 2 to 13 percentage points over competitive baselines.

### ContraBERT: A Follow-up Work

ContraBERT aims to improve the robustness of pre-trained models via contrastive learning by designing nine kinds of simple and complex data augmentation operators on programming language and natural language data, and continuing to train existing pre-trained models by masked language modeling and contrastive pre-training task on original samples with their augmented variants.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "4eb54a6e-9b1b-4c8a-b81a-4a24d80761b0",
  "isSidechain": true,
  "promptId": "073f59e2-5eca-44b2-8b49-13d14d4d8dca",
  "agentId": "a26c135a0a7f11d02",
  "type": "user",
  "uuid": "a51053bf-6498-4883-9c13-4453ac0b905f",
  "sourceToolAssistantUUID": "4eb54a6e-9b1b-4c8a-b81a-4a24d80761b0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "924d92b4-a5d4-492f-8ca6-f254c2b0392e",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 23 · 2026-05-10T05:39:00.624Z_

<details><summary>↩ Tool result · `toolu_01KiznqPgJDCdcBowRaBYhm8`</summary>

```text
Web search results for query: "mutation testing LLM training code tasks 2025 2026"

Links: [{"title":"Accepted at the 2026 IEEE International Conference on Software Testing, Verification and Validation (ICST 2026) Assessing the Impact of Code Changes on the Fault Localizability of Large Language Models","url":"https://arxiv.org/html/2504.04372"},{"title":"GitHub - LLM-Testing/LLM4SoftwareTesting · GitHub","url":"https://github.com/LLM-Testing/LLM4SoftwareTesting"},{"title":"GitHub - ExpertiseModel/MuTAP: MutAP: A prompt_based learning technique to automatically generate test cases with Large Language Model · GitHub","url":"https://github.com/ExpertiseModel/MuTAP"},{"title":"GitHub - codeintegrity-ai/mutahunter: Open Source, Language Agnostic Mutation Testing · GitHub","url":"https://github.com/codeintegrity-ai/mutahunter"},{"title":"GitHub - iSEngLab/AwesomeLLM4SE: [SCIS 2025] A Survey on Large Language Models for Software Engineering · GitHub","url":"https://github.com/iSEngLab/AwesomeLLM4SE"},{"title":"[2506.02954] Mutation-Guided Unit Test Generation with a Large Language Model","url":"https://arxiv.org/abs/2506.02954"},{"title":"Meta Applies Mutation Testing with LLM to Improve Compliance Coverage - InfoQ","url":"https://www.infoq.com/news/2026/01/meta-llm-mutation-testing/"},{"title":"LLMs taking shortcuts in test generation: A study with SAP HANA and LevelDB","url":"https://arxiv.org/html/2604.14437v1"},{"title":"GitHub - githubnext/llmorpheus: LLM-based mutation testing","url":"https://github.com/githubnext/llmorpheus"},{"title":"[2503.08182] Mutation Testing via Iterative Large Language Model-Driven Scientific Debugging","url":"https://arxiv.org/abs/2503.08182"}]

Based on the search results, here's what I found about mutation testing, LLM training, and code tasks in 2025-2026:

## Recent Research and Applications

A paper accepted at the 2026 IEEE International Conference on Software Testing, Verification and Validation (ICST 2026) addresses dataset contamination by dynamically injecting faults into real-world seed programs to create unseen fault localization tasks using classical mutation testing, developing an end-to-end evaluation framework that addresses limitations in current LLM evaluation.

Meta has applied large language models to mutation testing to improve compliance coverage across its software systems, integrating LLM-generated mutants and tests into Meta's Automated Compliance Hardening system (ACH), addressing scalability and accuracy limits of traditional mutation testing. Meta's ACH system uses LLMs to generate realistic mutants and targeted tests, focusing on privacy, safety, and regulatory concerns, with an LLM-based equivalence detector filtering redundant mutants and a test generator producing unit tests that engineers can review.

## Mutation-Guided Test Generation

Recent work on mutation-guided unit test generation with large language models notes that while tools like EvoSuite focus on maximizing code coverage, recent advances in LLMs have shifted attention toward LLM-based test generation, though code coverage metrics remain overly emphasized despite being weak indicators of a test suite's fault-detection capability, whereas mutation score offers a more reliable measure.

In an iterative approach, LLMs form hypotheses about how to kill specific mutants, and then iteratively generate and refine tests until they succeed, all with detailed explanations for each step.

## Tools and Frameworks

Mutahunter is an open-source, language agnostic LLM-based mutation testing tool. LLMorpheus is a tool for applying mutation testing to npm packages written in JavaScript/TypeScript using a large language model, which generates mutants by prompting the LLM with background on mutation testing and fragments of source code.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "2d4bdcb2-1819-4f59-89b4-220c5b677d32",
  "isSidechain": true,
  "promptId": "073f59e2-5eca-44b2-8b49-13d14d4d8dca",
  "agentId": "a26c135a0a7f11d02",
  "type": "user",
  "uuid": "3048e359-a551-4db1-81b6-9115d52d6d2f",
  "sourceToolAssistantUUID": "2d4bdcb2-1819-4f59-89b4-220c5b677d32",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "924d92b4-a5d4-492f-8ca6-f254c2b0392e",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 24 · 2026-05-10T05:39:22.010Z_

## Summary of Competing and Related Work

Based on my systematic search, here are the key competing and related works that address similar problems to SeMutFL:

### Most Directly Relevant: LLM Fault Localization Robustness

**1. [ICST 2026] Assessing the Impact of Code Changes on the Fault Localizability of Large Language Models**
- URL: https://arxiv.org/abs/2504.04372
- This is the most directly competing work. It evaluates LLM robustness to semantic-preserving mutations (SPMs) for fault localization, finding that 78% of faults cannot be localized after applying SPMs. It develops an end-to-end evaluation framework addressing data contamination, scalability, and extensibility—the exact problem domain as SeMutFL.

### Contrastive Learning for Fault Localization (2025-2026)

**2. Multi-View Adaptive Contrastive Learning for Information Retrieval Based Fault Localization (MACL-IRFL)**
- URL: https://link.springer.com/article/10.1007/s10515-025-00573-x
- Published 2026 in Automated Software Engineering journal
- Uses contrastive learning to improve fault localization accuracy by up to 28.93%

**3. CoverFL: Enhancing Fault Localization via Deep Coverage Relation**
- URL: https://dl.acm.org/doi/10.1145/3787964
- Accepted December 28, 2025; published March 6, 2026
- Applies graph contrastive learning to discover relationships between faulty code and failed test cases

**4. SupConFL: Fault Localization with Supervised Contrastive Learning**
- URL: https://dl.acm.org/doi/10.1145/3609437.3609441
- Trains models contrastively between faulty and fixed code versions

### Foundational Contrastive Code Learning

**5. ContraCode: Contrastive Code Representation Learning**
- URL: https://arxiv.org/abs/2007.04973
- Seminal 2021 work training models to be invariant to semantic-preserving code transformations
- Shows 39% improvement on adversarial code clone detection
- This is the conceptual foundation for semantic mutation robustness in code

**6. ContraBERT: Enhancing Code Pre-trained Models via Contrastive Learning**
- URL: https://arxiv.org/abs/2301.09072
- Recent follow-up using 9 augmentation operators for contrastive pre-training
- Direct follow-up to ContraCode approach

### LLM Code Robustness to Surface Variations

**7. Memorize or Generalize? Evaluating LLM Code Generation with Code Rewriting**
- URL: https://arxiv.org/abs/2503.02296
- Evaluates code LLM robustness to rewrites and mutations
- Shows varying vulnerability to paraphrase, mutation, and code rewrites

**8. Enhancing the Robustness of LLM-Generated Code: Empirical Study and Framework**
- URL: https://arxiv.org/abs/2503.20197v1
- 2025 work on improving LLM-generated code robustness

**9. Prompt Variability Effects On LLM Code Generation**
- URL: https://arxiv.org/abs/2506.10204v1
- Studies 18 categories of input perturbations to code LLMs

### Program Repair with LLM Fault Localization

**10. D4C: Aligning the Objective of LLM-based Program Repair**
- URL: https://arxiv.org/abs/2404.08877
- ICSE'25 paper on program repair showing that LLMs can end-to-end locate and repair bugs without perfect fault localization

**11. AgentFL: Scaling LLM-based Fault Localization to Project-Level Context**
- URL: https://paperswithcode.com/paper/agentfl-scaling-llm-based-fault-localization
- Multi-agent system for automated fault localization using ChatGPT

**12. Impact of Large Language Models of Code on Fault Localization**
- URL: https://arxiv.org/abs/2408.09657v1
- Evaluates impact of LLMs on fault localization performance

### Mutation Testing and LLM Integration

**13. Mutation Testing via Iterative Large Language Model-Driven Scientific Debugging**
- URL: https://arxiv.org/abs/2503.08182
- Combines mutation testing with iterative LLM-guided test generation

**14. Mutation-Guided Unit Test Generation with a Large Language Model**
- URL: https://arxiv.org/abs/2506.02954
- Recent 2025 work using mutation score to guide LLM test generation

**15. Meta's LLM-based Mutation Testing for Compliance**
- URL: https://www.infoq.com/news/2026/01/meta-llm-mutation-testing/
- Production application of LLMs to mutation testing (2026)

### Supporting Frameworks and Fine-tuning

**16. [SCIS 2025] A Survey on Large Language Models for Software Engineering**
- URL: https://github.com/iSEngLab/AwesomeLLM4SE
- Comprehensive survey covering LLM approaches including robustness

**17. SWE-bench Verified Issues Benchmark**
- URL: https://arxiv.org/pdf/2310.06770
- While primarily a program repair benchmark, SWE-bench includes fault localization evaluation; noted to have 8-10% contamination with pretraining data

**18. Dissecting the SWE-Bench Leaderboards**
- URL: https://arxiv.org/abs/2506.17208
- 2025 analysis of leaderboard reliability, identifying inflation from test inadequacies

### Key Gap Analysis

The search reveals that **the direct combination addressed by SeMutFL—training LLMs on semantic-preserving mutation examples specifically to improve fault localization robustness—appears to be novel**. While ContraCode addresses semantic-preserving mutations and recent work (like the ICST 2026 paper) measures LLM sensitivity to such mutations, I found no prior work that explicitly proposes a training methodology using mutation data to improve fault localization performance.

The closest related approaches are:
- ContraCode's contrastive pre-training on mutations (but for general code understanding, not fault localization)
- Recent contrastive methods for fault localization (but not mutation-robust)
- Meta's LLM-based mutation testing (but for test generation, not localization training)

This suggests SeMutFL fills a genuine gap in the literature.

Sources:
- [Assessing the Impact of Code Changes on the Fault Localizability of Large Language Models](https://arxiv.org/abs/2504.04372)
- [Multi-view adaptive contrastive learning for information retrieval based fault localization](https://link.springer.com/article/10.1007/s10515-025-00573-x)
- [CoverFL: Enhancing Fault Localization via Deep Coverage Relation](https://dl.acm.org/doi/10.1145/3787964)
- [SupConFL: Fault Localization with Supervised Contrastive Learning](https://dl.acm.org/doi/10.1145/3609437.3609441)
- [Contrastive Code Representation Learning (ContraCode)](https://arxiv.org/abs/2007.04973)
- [ContraBERT: Enhancing Code Pre-trained Models via Contrastive Learning](https://arxiv.org/abs/2301.09072)
- [Memorize or Generalize? Evaluating LLM Code Generation with Code Rewriting](https://arxiv.org/abs/2503.02296)
- [Enhancing the Robustness of LLM-Generated Code: Empirical Study and Framework](https://arxiv.org/abs/2503.20197v1)
- [Prompt Variability Effects On LLM Code Generation](https://arxiv.org/abs/2506.10204v1)
- [D4C: Aligning the Objective of LLM-based Program Repair](https://arxiv.org/abs/2404.08877)
- [AgentFL: Scaling LLM-based Fault Localization to Project-Level Context](https://paperswithcode.com/paper/agentfl-scaling-llm-based-fault-localization)
- [Impact of Large Language Models of Code on Fault Localization](https://arxiv.org/abs/2408.09657v1)
- [Mutation Testing via Iterative Large Language Model-Driven Scientific Debugging](https://arxiv.org/abs/2503.08182)
- [Mutation-Guided Unit Test Generation with a Large Language Model](https://arxiv.org/abs/2506.02954)
- [Meta's LLM-based Mutation Testing for Compliance Coverage](https://www.infoq.com/news/2026/01/meta-llm-mutation-testing/)
- [A Survey on Large Language Models for Software Engineering (AwesomeLLM4SE)](https://github.com/iSEngLab/AwesomeLLM4SE)
- [SWE-BENCH: Can Language Models Replace Software Engineers?](https://arxiv.org/pdf/2310.06770)
- [Dissecting the SWE-Bench Leaderboards: Profiling Submitters and Architectures](https://arxiv.org/abs/2506.17208)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3048e359-a551-4db1-81b6-9115d52d6d2f",
  "isSidechain": true,
  "agentId": "a26c135a0a7f11d02",
  "requestId": "req_011CatMFfwywfRuXk18mi34r",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "c4422c40-4e05-49a3-9e4f-a24535c7e150",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "924d92b4-a5d4-492f-8ca6-f254c2b0392e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01YQCeMUkmFqV2NGDpQQvvxY",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 6921,
      "cache_read_input_tokens": 20691,
      "output_tokens": 2342,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 6921
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 7,
          "output_tokens": 2342,
          "cache_read_input_tokens": 20691,
          "cache_creation_input_tokens": 6921,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 6921,
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
