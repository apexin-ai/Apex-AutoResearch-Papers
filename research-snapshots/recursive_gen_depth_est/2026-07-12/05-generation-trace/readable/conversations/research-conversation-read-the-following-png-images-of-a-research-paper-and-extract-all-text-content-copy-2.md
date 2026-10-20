# Research conversation: Read the following PNG images of a research paper and extract ALL text content verbatim. Focus on: discussion, limitatio

**How Deep Is Your Data? Estimating Recursive Generation Depth via Statistical Fingerprints (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 11
- **Recorded user turns:** 1
- **Tool calls:** 4
- **Original source:** `logs/chats/exported-trajectories/account-1/agent-acdb831c4aa13a8e1.jsonl`
- **Structured JSON:** [`927cccbffa95be1c71c2.json`](../../sessions/92/927cccbffa95be1c71c2.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

11 recorded events

### User

_source line 1 · 2026-05-16T19:32:26.687Z_

Read the following PNG images of a research paper and extract ALL text content verbatim. Focus on: discussion, limitations, conclusion, and beginning of appendix. Pay special attention to:
- Any discussion of reference model circular dependency / architecturally distinct references
- Discussion of single LoRA instance per depth / 5-Fold CV sample non-independence
- Discussion of deployment requiring pre-known decoding strategy / strategy detection
- Wild data FPR discussion and practical deployment claims
- EDD definition discussion (classifier-dependence vs intrinsic property)
- Any "Limitations" section content

Read these files in order:
1. /home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/_pdf_images/main_p9.png
2. /home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/_pdf_images/main_p10.png
3. /home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/_pdf_images/main_p11.png
4. /home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/_pdf_images/main_p12.png

Return the FULL extracted text, preserving structure. Do not summarize.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "7a8010eb-b6a1-4d1b-aa4e-cd84d2a39d6d",
  "agentId": "acdb831c4aa13a8e1",
  "type": "user",
  "uuid": "a0b2219b-0db6-46dd-a7a9-d566f134e2ae",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/.claude/sessions/review_reviewer_1_37084335",
  "sessionId": "f5009a54-ac13-49a4-83d8-13bbafebaca9",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 2 · 2026-05-16T19:32:26.689Z_

```json
{
  "parentUuid": "a0b2219b-0db6-46dd-a7a9-d566f134e2ae",
  "isSidechain": true,
  "agentId": "acdb831c4aa13a8e1",
  "attachment": {
    "type": "deferred_tools_delta",
    "addedNames": [
      "CronCreate",
      "CronDelete",
      "CronList",
      "EnterWorktree",
      "ExitWorktree",
      "ListMcpResourcesTool",
      "Monitor",
      "NotebookEdit",
      "PushNotification",
      "ReadMcpResourceTool",
      "RemoteTrigger",
      "TaskStop",
      "WebFetch",
      "WebSearch",
      "mcp__agent-ml-research__cleanup_pdf_images",
      "mcp__agent-ml-research__pdf_to_images",
      "mcp__agent-ml-research__review_reviewer_post_to_director",
      "mcp__agent-ml-research__verify_references"
    ],
    "addedLines": [
      "CronCreate",
      "CronDelete",
      "CronList",
      "EnterWorktree",
      "ExitWorktree",
      "ListMcpResourcesTool",
      "Monitor",
      "NotebookEdit",
      "PushNotification",
      "ReadMcpResourceTool",
      "RemoteTrigger",
      "TaskStop",
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
  "uuid": "5044afe3-a0a8-4fff-b5e7-4cddf6a5d168",
  "timestamp": "2026-05-16T19:32:26.689Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/.claude/sessions/review_reviewer_1_37084335",
  "sessionId": "f5009a54-ac13-49a4-83d8-13bbafebaca9",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Tool call

_source line 3 · 2026-05-16T19:32:29.613Z_

<details open><summary>🔧 Tool call — Read · `toolu_016HEYzgihM9N7z4sxr8gYFH`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/_pdf_images/main_p9.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5044afe3-a0a8-4fff-b5e7-4cddf6a5d168",
  "isSidechain": true,
  "agentId": "acdb831c4aa13a8e1",
  "requestId": "req_011Cb6ofKviGngZNCRKBCRYL",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "a4d50bd6-826b-4514-9015-759be68fa940",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/.claude/sessions/review_reviewer_1_37084335",
  "sessionId": "f5009a54-ac13-49a4-83d8-13bbafebaca9",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Hhh8gJYqLaNuE7hzhWUDC8",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 8638,
      "cache_read_input_tokens": 8265,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 8638,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 52,
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

_source line 4 · 2026-05-16T19:32:30.030Z_

<details open><summary>🔧 Tool call — Read · `toolu_018XbqdPYkwQsSECw7LLuRHQ`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/_pdf_images/main_p10.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a4d50bd6-826b-4514-9015-759be68fa940",
  "isSidechain": true,
  "agentId": "acdb831c4aa13a8e1",
  "requestId": "req_011Cb6ofKviGngZNCRKBCRYL",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "9d46da65-9bcf-4cef-8222-f4e178f9a080",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/.claude/sessions/review_reviewer_1_37084335",
  "sessionId": "f5009a54-ac13-49a4-83d8-13bbafebaca9",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Hhh8gJYqLaNuE7hzhWUDC8",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 8638,
      "cache_read_input_tokens": 8265,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 8638,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 52,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool result

_source line 5 · 2026-05-16T19:32:30.252Z_

<details><summary>↩ Tool result · `toolu_016HEYzgihM9N7z4sxr8gYFH`</summary>

````text
```json
{
  "type": "image",
  "source": {
    "type": "base64",
    "data": "[ATTACHMENT_DATA_REDACTED]",
    "media_type": "image/jpeg"
  }
}
```
````

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a4d50bd6-826b-4514-9015-759be68fa940",
  "isSidechain": true,
  "promptId": "7a8010eb-b6a1-4d1b-aa4e-cd84d2a39d6d",
  "agentId": "acdb831c4aa13a8e1",
  "type": "user",
  "uuid": "ec63e6c1-0a09-42c1-9304-e8cc94162f8a",
  "sourceToolAssistantUUID": "a4d50bd6-826b-4514-9015-759be68fa940",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/.claude/sessions/review_reviewer_1_37084335",
  "sessionId": "f5009a54-ac13-49a4-83d8-13bbafebaca9",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-16T19:32:30.799Z_

<details><summary>↩ Tool result · `toolu_018XbqdPYkwQsSECw7LLuRHQ`</summary>

````text
```json
{
  "type": "image",
  "source": {
    "type": "base64",
    "data": "[ATTACHMENT_DATA_REDACTED]",
    "media_type": "image/jpeg"
  }
}
```
````

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "9d46da65-9bcf-4cef-8222-f4e178f9a080",
  "isSidechain": true,
  "promptId": "7a8010eb-b6a1-4d1b-aa4e-cd84d2a39d6d",
  "agentId": "acdb831c4aa13a8e1",
  "type": "user",
  "uuid": "04a3d6e0-62c4-45ca-8ec6-91fccb1da124",
  "sourceToolAssistantUUID": "9d46da65-9bcf-4cef-8222-f4e178f9a080",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/.claude/sessions/review_reviewer_1_37084335",
  "sessionId": "f5009a54-ac13-49a4-83d8-13bbafebaca9",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-16T19:32:31.035Z_

<details open><summary>🔧 Tool call — Read · `toolu_019noYBAwSSFmAB9manGo9zQ`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/_pdf_images/main_p11.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "04a3d6e0-62c4-45ca-8ec6-91fccb1da124",
  "isSidechain": true,
  "agentId": "acdb831c4aa13a8e1",
  "requestId": "req_011Cb6ofKviGngZNCRKBCRYL",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "0fd205f9-196c-4a1e-a7ee-223b245d88b4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/.claude/sessions/review_reviewer_1_37084335",
  "sessionId": "f5009a54-ac13-49a4-83d8-13bbafebaca9",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Hhh8gJYqLaNuE7hzhWUDC8",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 8638,
      "cache_read_input_tokens": 8265,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 8638,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 52,
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

_source line 8 · 2026-05-16T19:32:31.239Z_

<details open><summary>🔧 Tool call — Read · `toolu_01CDVYu7WkMVBAPioroAYafm`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/_pdf_images/main_p12.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0fd205f9-196c-4a1e-a7ee-223b245d88b4",
  "isSidechain": true,
  "agentId": "acdb831c4aa13a8e1",
  "requestId": "req_011Cb6ofKviGngZNCRKBCRYL",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "15f4fe74-d344-48f3-8c37-473e208f66b1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/.claude/sessions/review_reviewer_1_37084335",
  "sessionId": "f5009a54-ac13-49a4-83d8-13bbafebaca9",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Hhh8gJYqLaNuE7hzhWUDC8",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 8638,
      "cache_read_input_tokens": 8265,
      "output_tokens": 334,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 8638
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 334,
          "cache_read_input_tokens": 8265,
          "cache_creation_input_tokens": 8638,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 8638,
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

_source line 9 · 2026-05-16T19:32:31.945Z_

<details><summary>↩ Tool result · `toolu_019noYBAwSSFmAB9manGo9zQ`</summary>

````text
```json
{
  "type": "image",
  "source": {
    "type": "base64",
    "data": "[ATTACHMENT_DATA_REDACTED]",
    "media_type": "image/jpeg"
  }
}
```
````

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "0fd205f9-196c-4a1e-a7ee-223b245d88b4",
  "isSidechain": true,
  "promptId": "7a8010eb-b6a1-4d1b-aa4e-cd84d2a39d6d",
  "agentId": "acdb831c4aa13a8e1",
  "type": "user",
  "uuid": "6c42209e-c3a4-4048-ab93-846fb36974ba",
  "sourceToolAssistantUUID": "0fd205f9-196c-4a1e-a7ee-223b245d88b4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/.claude/sessions/review_reviewer_1_37084335",
  "sessionId": "f5009a54-ac13-49a4-83d8-13bbafebaca9",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-16T19:32:32.135Z_

<details><summary>↩ Tool result · `toolu_01CDVYu7WkMVBAPioroAYafm`</summary>

````text
```json
{
  "type": "image",
  "source": {
    "type": "base64",
    "data": "[ATTACHMENT_DATA_REDACTED]",
    "media_type": "image/jpeg"
  }
}
```
````

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "15f4fe74-d344-48f3-8c37-473e208f66b1",
  "isSidechain": true,
  "promptId": "7a8010eb-b6a1-4d1b-aa4e-cd84d2a39d6d",
  "agentId": "acdb831c4aa13a8e1",
  "type": "user",
  "uuid": "04c155c6-21f6-45ff-8424-386488d43ae3",
  "sourceToolAssistantUUID": "15f4fe74-d344-48f3-8c37-473e208f66b1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/.claude/sessions/review_reviewer_1_37084335",
  "sessionId": "f5009a54-ac13-49a4-83d8-13bbafebaca9",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 11 · 2026-05-16T19:35:21.868Z_



Here is the full extracted text from the four pages:

---

## Page 9 (References page, continued)

Neural Networks with Application to Age Estimation. *Pattern Recognition Letters*, 140:325–331. arXiv:1901.07884.

Elvis Dohmatob, Yunzhen Feng, and Julia Kempe. 2024a. Model Collapse Demystified: The Case of Regression. In *Proceedings of NeurIPS*. arXiv:2402.07712.

Elvis Dohmatob, Yunzhen Feng, Arjan Suhbatmaniam, and Julia Kempe. 2025. Strong Model Collapse. In *Proceedings of ICLR*. arXiv:2410.04840.

Elvis Dohmatob, Yunzhen Feng, Pu Yang, Francois Charton, and Julia Kempe. 2024b. A Tale of Tails: Model Collapse as a Change of Scaling Laws. In *Proceedings of ICML*. arXiv:2402.07043(78).

George Drayson, Emile Thinane, and Vasileios Lampos. 2025. Machine-generated text detection prevents language model collapse. In *Findings of EMNLP*. arXiv:2502.15654.

Ali Falahati, Mohammad Mohammad Amiri, Kate Larson, and Lukasz Golab. 2026. Curated Synthetic Data Doesn't Have to Destroy a Language Model: A Closer Study of Generative Retraining with Pluralistic Preferences. arXiv:2605.07724.

Matthew Finlayson, John Hewitt, Alexander Koller, Swabha Swayamdipta, and Ashish Sabharwal. 2024. Closing the Curious Case of Neural Text Degeneration. In *Proceedings of ICLR*. arXiv:2310.01693v2.

Esteban Garces Arias, Meimingwei Li, Christian Heumann, and Matthias Assenmacher. 2025. Decoding Decoded: Understanding Hyperparameter Effects in Open-Ended Text Generation. In *Proceedings of COLING*. arXiv:2410.06097.

Sebastian Gehrmann, Hendrik Strobelt, and Alexander M. Rush. 2019. GLTR: Statistical Detection and Visualization of Generated Text. In *Proceedings of ACL: System Demonstrations*. 199:606610.

Matthias Gerstgrasser, Rylan Schaeffer, Apratim Dey, Rafael Rafailov, Henry Sleight, John Hughes, Tomasz Korbak, Rajashree Agrawal, Dhruv Pai, Andrey Gromov, Daniel A. Roberts, Diyi Yang, David L. Donoho, and Sanmi Koyejo. 2024. Is Model Collapse Inevitable? Breaking the Curse of Recursion by Accumulating Real and Synthetic Data. arXiv:2404.01413.

Aamir Guitian Qubbanwa, Yashraj Jaiswal, Abhishek Pandey, Abhishek Kadian, Ahmad Al-Dahle, Areeba Lottam, Akhil Mathur, Alan Schelten, and 1 others. 2024. The Llama 3 Herd of Models. arXiv:2407.21783.

Yi Gu, Lingyue Pang, Xiangmin Yu, Tianyu Wang, Jianjie Liu, Cory E. Parker, and Alexander Ash. 2026. SIGMA: Scalable Spectral Insights for LLM Model Collapse. arXiv:2601.03385.

Abhinamya Hans, Avi Schwarzschild, Valeria Cherepanova, Hamid Kazemi, Aniruddha Saha, Micah Goldblum, Jonas Geiping, and Tom Goldstein. 2024. Spotting LLMs With Binoculars: Zero-Shot Detection of Machine-Generated Text. In *Proceedings of ICML*. arXiv:2401.12070.

Pengcheng He, Jianfeng Gao, and Weizhu Chen. 2023. DeBERTaV3: Improving DeBERTa using ELECTRA-Style Pre-Training with Gradient-Disentangled Embedding Sharing. In *Proceedings of ICLR*. arXiv:2111.09543.

Ari Holtzman, Jan Buys, Li Du, Maxwell Forbes, and Yejin Choi. 2020. The Curious Case of Neural Text Degeneration. In *Proceedings of ICLR*. arXiv:1904.09751.

Edward J. Hu, Yelong Shen, Phillip Wallis, Zeyuan Allen-Zhu, Yuanzhi Li, Shean Wang, Lu Wang, and Weizhu Chen. 2022. LoRA: Low-Rank Adaptation of Large Language Models. In *Proceedings of ICLR*. arXiv:2106.09685.

Figani Keisha, Zekun Wu, Ze Wang, Adriano Koshiyama, and Philip Treleaven. 2025. Knowledge Collapse in LLMs: When Fluency Surfaces but Facts Fail under Recursive Synthetic Training. arXiv:2509.04796.

John Kirchenbauer, Jonas Geiping, Yuxin Wen, Jonathan Katz, Ian Miers, and Tom Goldstein. 2023. A Watermark for Large Language Models. In *Proceedings of ICML*. arXiv:2301.10226v4.

Yinhao Liu, Mylo Ori, Naman Goyal, Jingfei Du, Manidar Joshi, Danqi Chen, Omer Levy, Mike Lewis, Luke Zettlemoyer, and Veselin Stoyanov. 2019. RoBERTa: A Robustly Optimized BERT Pretraining Approach. arXiv preprint arXiv:1907.11692.

Marian Marcis, Stefano Soatto, Pratik Chaudhari, and Paolo Tabuada. 2024. Heat Death of Generative Models in Closed-Loop Learning. In *Proceedings of ICASSP*. 199:806610.

Eric Mitchell, Yoonho Lee, Alexander Khazatsky, Christopher D. Manning, and Chelsea Finn. 2023. DetectGPT: Zero-Shot Machine-Generated Text Detection using Probability Curvature. In *Proceedings of ICML*. arXiv:2301.11305.

Amr Moharram, Aliraghem George, Michalis Vazirgiannis, and Gaohan Shang. 2025. LLM as a Broken Telephone: Iterative Generation Distorts Information. In *Proceedings of ACL*. arXiv:2502.20258.

Dileep Pitawela, Gustavo Carneiro, and Hsiang-Ting Chen. 2025. CLOC: Contrastive Learning for Odds and Classification with Multi-Margin N-pair Loss. In *Proceedings of CVPR*. arXiv:2504.17813.

Xiao Pu, Zepeng Cheng, Lin Yuan, Yu Wu, and Xiouli Bi. 2026. Breaking the Generator Barrier: Disentangled Representation for Generalizable AI-Text Detection. arXiv:2604.13692.

---

## Page 10 (References continued + Appendix begins)

Shushanta Pudasaini, Luis Miralles-Pechuan, David Lillis, and Marina Llorens Salvador. 2026. Why AI-Generated Text Detection Fails: Evidence from Explanation At Beyond Benchmark Accuracy. arXiv:2603.23146.

Vinu Sankar Sadasivan, Aounon Kumar, Sriram Balasubramanian, Wenxiao Wang, and Soheil Feizi. 2023. Can AI-Generated Text be Reliably Detected? arXiv:2303.11156.

Max Stahlhauer and Albert Gatt. 2026. Synthetic Eggs in Many Baskets: The Impact of Synthetic Data Diversity on LLM Fine-Tuning. In *Findings of ACL*.

Lianghe Shi, Meng Wu, Haijie Zhang, Zekui Zhang, Moht Tao, and Qing Gu. 2025. A Closer Look at Model Collapse: From a Generalization-to-Memorization. In *Proceedings of NeurIPS, Spotlight*.

Ilia Shumailov, Zakhar Shumaylov, Yiren Zhao, Nicolas Papernot, Ross Anderson, and Yarin Gal. 2024. AI models collapse when trained on recursively generated data. *Nature*, 631:755–759.

Masashi Sugiyama, Makoto Yamada, and Klaus-Robert Müller. 2007. Covariate Shift Adaptation by Importance Weighted Cross Validation. *Journal of Machine Learning Research*, 8:985–1005.

Qwen Team. 2025. Qwen2.5: A Party of Foundation Models. arXiv:2412.15115.

Katherine Thai, Bradley Emi, Elyas Masrour, and Mo-hit Tyagi. 2026. Fullcount: Quantifying the Extent of AI Editing in Text. In *Proceedings of ICLR*. arXiv:2510.01539.

Adaku Uchendu, Thai Le, Kai Shu, and Dongwon Lee. 2020. Authorship Attribution for Neural Text Generation. In *Proceedings of EMNLP*.

Vivek Verma, Eve Fleisig, Nicholas Tomlin, and Dan Klein. 2024. Ghostbusters: Detecting Text Ghostwritten by Large Language Models. In *Proceedings of NAACL*. arXiv:2305.15047.

Kevin Wang, Hongsun Nil, and Dinking Li. 2026. Can Generative Artificial Intelligence Survey Data Contain Contamination? Theoretical Guarantees under Contaminated Recursive Training. arXiv:2602.16665.

Yuxia Wang, Jonibek Mansurov, Petar Ivanov, Jinjin Sa, Artem Shelmanov, Akim Tsvigun, Osama Mohammed Afzal, Tarek Mahmoud, Giovanni Puccetti, Thomas Arnold, Chenxi Whitehouse, Alham Fikri Aji, Nizar Habash, Iryna Gurevych, and Preslav Nakov. 2024. SemEval-2024 Task 8: Multidomain, Multimodel and Multilingual Machine-Generated Text Detection. In *Proceedings of the 18th International Workshop on Semantic Evaluation (SemEval-2024)*. arXiv:2404.14183.

Alexander Wetzig, Aatmik Gupta, Saumya Malik, and Danuji Chen. 2024. QaRating: Selecting High-Quality Data for Training Language Models. In *Proceedings of EMC*. arXiv:2402.09719.

Gian Wiher, Clara Meister, and Ryan Cotterell. 2022. On Decoding Strategies for Neural Text Generation. *Transactions of the Association for Computational Linguistics*, 10:997–1012.

Junchen Wu, Shu Yang, Ruotshe Zhao, Yifm Yuan, Lisha Sam Chen, and Lipeck Fai Wang. 2025. A Survey on LLM-Generated Text Detection: Necessity, Methods, and Future Directions. *Computational Linguistics*, 51(1):275–354.

Sang Michael Xie, Shibani Santureui, Tengyu Ma, and Percy Liang. 2023. Data Selection for Language Models via Importance Resampling. In *Proceedings of NeurIPS*. arXiv:2302.03169.

Xuanmng Yang, Wei Cheng, Yue Wu, Linda Petzold, William Yang Wang, and Haifeng Chen. 2024. DNA-GPT: Divergent N-Gram Analysis for Training-Free Detection of GPT-Generated Text. In *Proceedings of ICLR*. arXiv:2305.17359.

Junyan Ye, Baichhuan Zhao, Zifeng Huang, Junao Zhang, Tuotu Wu, He Mengqi, Pin Li, Hongjin Li, Zihao Wang, Tong Wu, Zhifeieng Wu, Yiping Chen, Dalton Lian, Conghui He, and Weijia Li. 2025. LOKI: A Comprehensive Synthetic Data Detection Benchmark using Large Multimodal Models. In *Proceedings of ICLR (Spotlight)*. arXiv:2410.09732.

## A Additional Results

### A.1 Top-k Feature Trajectories

Figure 3 shows feature trajectories for nucleus (p=0.95) and temperature (τ=0.9) sampling. Top-k (k=50) trajectories follow the same monotonically decreasing trend for all features but with compressed inter-depth spacing, consistent with the signal attenuation effect discussed in §4.4. Concretely, the d0→d1 drop is 99.1%, and under top-k is 78% (vs. 87% for nucleus), and the d2→d3 relative is 31% (vs. 39% for nucleus). Despite the magnitude reduction, feature rank ordering across depths is preserved, which explains why ordinal classifiers maintain directionality even under top-k conditions.

### A.2 Permutation Importance

To verify that the Gini-based importance rankings in §4.2 are not an artifact of the impurity measure, we compute permutation importance (5-fold CV, 10 repeats) for all 9 atlas cells. The top-2 features are stable across measures: ρ90_r₁ ranks in the top 2 in 9/9 cells under both Gini and permutation importance, and VAR_SURPRISAL in 8/9 (vs. 7/9 for Gini,

---

## Page 11 (Appendix continued)

[Figure 3 is shown: Feature trajectories across depths d0–d3 for top-k (k=50), stratified by model (columns) and strategy (line styles). Top row: p90_r₁ (monotonically decreasing). Middle: var_surprisal (decreasing). Bottom: ent_trigram (decreasing). Shaded bands = interquartile range. The d0 → d1 gap exceeds all subsequent inter-depth gaps.]

with the additional cell being OLMo top-k; the single SHAP exception is GPT-2 XL top-k, where P75_PPL displaces VAR_SURPRISAL to rank 3). Kendall's W=0.90 across all three methods (Gini, permutation, SHAP) indicates strong concordance (p<0.005). Pairwise Spearman correlations are: SHAP–Gini ρ=0.93, SHAP–permutation ρ=0.84, Gini–permutation ρ=0.71. Per-cell top-5 overlap between SHAP and permutation importance is 3–4 out of 5 features; the aggregated (mean-across-cells) top-5 sets are identical, confirming that the top features are robust to the choice of importance measure at the aggregate level while per-cell rankings exhibit model-dependent variation.

### A.3 Per-Class Recall

Table 7 reports per-class recall across all 9 atlas cells (4-class in-distribution, 5-fold CV). Depth d2 recall exceeds 96% uniformly. Among generated depths, d2 is the hardest class in every cell; the deficit is most pronounced under top-k sampling (d6–53%), where vocabulary truncation removes the tail tokens that carry depth-discriminative signal.

### A.4 DCOL Iteration Details

Table 8 summarizes all six DCOL iterations. DeBERTa-v3-large exhibited systematic numerical instability across five configurations; RoBERTa-large resolved stability but could not close the accuracy gap with feature-based methods.

Table 7. Per-class recall (%) for all 9 atlas cells. d2 is the lowest-recall class in every cell. Boldface marks the highest d2 recall.

| Cell | d0 | d1 | d2 | d3 |
|------|-----|-----|-----|-----|
| Pythia, nuc. | 99.7 | 81.9 | 56.5 | 72.3 |
| Pythia, τ | 99.5 | 81.1 | 53.0 | 72.1 |
| PyMo, top-k | 99.5 | 72.3 | 45.6 | 57.5 |
| OLMo, nuc. | 99.8 | 80.3 | 63.5 | 76.5 |
| OLMo, τ | 99.5 | 47.7 | 64.1 | 72.2 |
| OLMo, top-k | 99.5 | 70.5 | 53.1 | 60.6 |
| GPT-2 XL, nuc. | 99.5 | 85.9 | 73.3 | 79.5 |
| GPT-2 XL, τ | 99.5 | 80.0 | 69.0 | 81.9 |
| GPT-2 XL, top-k | 98.5 | 79.5 | 52.5 | 71.1 |

Table 8: DCOL iteration summary. All classifiers use Pythia-1.4B nucleus data. RF baseline: 78.2%.

| Iter | Backbone | Config | Outcome |
|------|----------|--------|---------|
| v1 | DeBERTa | FT, m_lr 1e⁻⁵ | Embed. collapse |
| v2 | DeBERTa | FT, m_lr 1e⁻⁵ | OOM |
| v3 | DeBERTa | FT, m_lr 1e⁻⁵ | Forgetting + OOM |
| v4 | DeBERTa | LoRA, m_lr | Embed. collapse |
| v5 | DeBERTa | LoRA, m_lr 1e⁻⁴ | NaN gradients |
| v6 | RoBERTa | FT, grad clip 1.0 | Stable, 4-class acc 55.9% |

### A.5 Zero-Shot LLM Prompt Template

Both DeepSeek V1.2 and Qwen2.5-7B-Instruct use identical prompting. The system message defines recursive generation depth with per-depth descriptions (depth-0: human-written, depth 1-3: successive LLM generation cycles) and lists expected textual patterns at each depth (vocabulary richness, repetition, coherence). The user message presents the passage (truncated to ≤384 words) and requests a JSON response containing an integer depth prediction (0–3), a confidence score, and chain-of-thought reasoning. No in-context examples are provided.

System: "You are an expert at detecting AI-generated text and estimating its generation depth. Recursive generation depth refers to how many times a text has been through an LLM generation cycle. Depth 0: Original human-written [...] Depth 3: Text generated by an LLM given depth-2 text as input. Key patterns by depth: Depth 0 (human): Rich vocabulary [...], Depth 3 (third-gen): Noticeable repetition, formulaic structure [...]"

User: "Analyze the following text and estimate its recursive generation depth (0, 1, 2, or 3). TEXT: [text]. Respond with ONLY a JSON object: {"depth": <0-3>, "confidence": &lt;float 0-1>, "reasoning": [str]}"

---

## Page 12 (Appendix continued)

### A.6 Temperature Robustness

The cross-strategy results in §5.3 use a single temperature (τ=0.9). To test whether depth signal generalizes across temperatures, we repeat the classification pipeline at τ ∈ {0.5, 0.7, 0.9, 1.1} on Pythia-1.4B.

**Within-τ robustness.** For τ ∈ {0.5, 0.9}, d1-vs-d2 AUC exceeds 0.80 (peak 0.851 at τ=0.7, comparable to nucleus p=0.95's 0.861) and 4-class accuracy ranges from 75.4% to 77.3% (Table 9), confirming the depth signal is not an artifact of a single temperature. The same top-5 features (var_surprisal, p75_ppl, mean_ppl, mean_surprisal, p75_rp1) dominate across all τ values with only minor rank-order variation.

**Collapse at τ=1.1:** memorization as prerequisite. At τ=1.1, 4-class accuracy drops to 57.2% and d1v2 AUC falls to 0.528. Training loss reveals the mechanism: at low temperature (τ=0.5), fine-tuning loss decreases steeply across recursive depths (2.27 → 0.42 → 0.16), indicating rapid memorization of the model's own output. At τ=1.1, loss remains nearly flat (2.27 → 1.91 → 1.85)—high-entropy output resists memorization, so depth-dependent distributional shifts do not accumulate. This establishes memorization as a *prerequisite* for detectable depth signal: recursive depth is discriminable only when successive fine-tuning iterations progressively reshape the output distribution.

**Cross-τ non-transferability.** Leave-one-out transfer yields mean accuracy of 46.7% with mean d1v2 AUC of 0.319 (Table 10)—worse than cross-strategy transfer (59.1%; §5.3). Holdout τ=0.5 produces inverted d1/d2 AUC (0.176), confirming that different temperatures produce *surprisal distributions with incompatible shapes*. This extends the strategy-specificity finding: even within a single decoding family, the feature space is temperature-specific, reinforcing the need for strategy-conditioned classifiers.

**Ecological validity.** On WikiText-103 (546 editorial passages), all three model-specific RF classifiers achieve ≥98.5% d0 accuracy despite ≤621% domain shift in mean ρ—partly an easy case, as WikiText's higher perplexity places it farther from d1–d3 in feature space. On noisier web-crawl data (5,000 C4 passages), FPR ranges from

4.7% (OLMo) to 22.4% (GPT-2 XL), concentrated in template/SEO content with high n-gram repetition (Table 12); deployment on heterogeneous web data requires model-specific calibration.

Table 9: Within-τ 4-class classification (Pythia 1.4B, 5-fold CV, d1v2 = pairwise AUC for depth 1 vs. depth 2).

| τ | 4-class acc(%) | d1v2 AUC | d0v1 | d1v3 AUC |
|---|----------------|----------|------|----------|
| 0.5 | 77.3 | 0.842 | 0.990 | 0.796 |
| 0.7 | 75.4 | 0.853 | 0.997 | 0.720 |
| 0.9 | 75.9 | 0.898 | 0.991 | 0.781 |
| 1.1 | 57.2 | 0.528 | 0.988 | 0.599 |

Table 10: Cross-τ leave-one-out transfer (Pythia-1.4B). Train on three temperatures, test on the hold-out one.

| Holdout | Acc (%) | d1v2 AUC |
|---------|---------|----------|
| τ=0.2 | 41.0 | 0.299 |
| τ=0.5 | 46.4 | 0.271 |
| τ=0.9 | 49.3 | 0.527 |
| τ=1.1 | 46.7 | 0.319 |
| Mean | 46.7 | 0.319 |

### A.7 Feature Overlap Analysis

We probe whether end-to-end PLM representations capture the same depth signals as our statistical features via linear probing of [CLS] representations from DeBERTa-v3-base and RoBERTa-base. PLM representations encode *surface* lexical features (TF/RF: R²=0.85, repeated bigrams) but fail to capture perplexity distribution statistics (VAR_SURPRISAL and P90_PPL yrd suggest R² under linear probing), confirming these features are not linearly accessible in the pretrained representation space. This confirms that the PPp accuracy gap between feature-based and end-to-end methods (§4.8) stems from complementarity—not redundation—*representation*. PLMs capture lexical patterns while the targeted statistical features capture distributional tail properties that constitute the dominant depth markers.

### A.8 End-to-End Learning

DeBERTa-v3-base (He et al., 2023) and RoBERTa-base (Liu et al., 2019) finetuned end-to-end achieve 58.3% (±4.7%) and 59.5% (±3.2%) respectively— lagging the RF baseline (78.2%) by 19.9pp and 18.7pp. The 1.2pp inter-backbone gap rules out architecture bias. Table 11 shows both backbones share the same failure mode—high d0 F1 (>0.94) but collapsed d1/d2 performance (F1 ≤ 0.42)—

---

**Regarding the specific topics requested:**

1. **Reference model circular dependency / architecturally distinct references**: No discussion found in these pages.

2. **Single LoRA instance per depth / 5-Fold CV sample non-independence**: No discussion found in these pages.

3. **Deployment requiring pre-known decoding strategy / strategy detection**: Mentioned indirectly in A.6 — "cross-strategy transfer (59.1%; §5.3)" and "This extends the strategy-specificity finding: even within a single decoding family, the feature space is temperature-specific, reinforcing the need for strategy-conditioned classifiers." No discussion of a strategy detection mechanism.

4. **Wild data FPR discussion and practical deployment claims**: In A.6 — "On noisier web-crawl data (5,000 C4 passages), FPR ranges from 4.7% (OLMo) to 22.4% (GPT-2 XL), concentrated in template/SEO content with high n-gram repetition (Table 12); deployment on heterogeneous web data requires model-specific calibration."

5. **EDD definition discussion (classifier-dependence vs intrinsic property)**: No discussion found in these pages.

6. **"Limitations" section**: No Limitations section appears in these four pages. The content goes from the end of references directly into "A Additional Results" appendix sections (A.1 through A.8).

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "04c155c6-21f6-45ff-8424-386488d43ae3",
  "isSidechain": true,
  "agentId": "acdb831c4aa13a8e1",
  "requestId": "req_011Cb6ofjCw9LTFjqXxxD83k",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "b18d7a0d-191b-4954-89f6-9fbbf085f474",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/.claude/sessions/review_reviewer_1_37084335",
  "sessionId": "f5009a54-ac13-49a4-83d8-13bbafebaca9",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011d5KFKSQ5Ge61vhew19tiu",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 2711,
      "cache_read_input_tokens": 16903,
      "output_tokens": 6940,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2711
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 6940,
          "cache_read_input_tokens": 16903,
          "cache_creation_input_tokens": 2711,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2711,
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
