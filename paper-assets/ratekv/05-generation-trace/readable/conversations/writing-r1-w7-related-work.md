# writing r1 w7 related work

**When Does Non-Uniform KV Cache Quantization Help? Cardinality Constraints and a Heterogeneity Diagnostic** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 54
- **Recorded user turns:** 0
- **Tool calls:** 26
- **Original source:** `logs/chats/worker_writing_r1_w7_related_work_20260515T044227.jsonl`
- **Structured JSON:** [`3640d0dd2fe35b5c2b94.json`](../../sessions/36/3640d0dd2fe35b5c2b94.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

54 recorded events

### Assistant

_source line 1 · 2026-05-15T04:42:36.440063+00:00_

You've hit your limit · resets May 16, 9am (UTC)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_writing_r1_w7_related_work_20260515T044227"
}
```

</details>

---

### Tool call

_source line 2 · 2026-05-15T04:46:25.551311+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/docs/paper/related_work.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_writing_r1_w7_related_work_20260515T044227",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/docs/paper/related_work.tex"
  }
}
```

</details>

---

### Tool result

_source line 3 · 2026-05-15T04:46:25.551610+00:00_

1	\section{Related Work}\label{sec:related_work}
2	
3	\paragraph{KV Cache Quantization.}
4	Uniform-precision methods quantize the KV cache at a single bit-width across all heads, using techniques such as asymmetric per-channel/per-token schemes~\cite{liu2024kivi,hooper2024kvquant}, quantization--serving co-design~\cite{lin2024qserve}, salient-token identification~\cite{he2024zipcache}, low-rank plus sparse correction~\cite{kang2024gear}, and sliding-window adaptation~\cite{duanmu2024skvq}.
5	We extend the design space to per-head non-uniform allocation over hardware-aligned bit-widths $\{2,4,8,16\}$.
6	
7	\paragraph{KV Cache Eviction.}
8	Complementary to quantization, eviction methods reduce cache size by discarding tokens---retaining heavy-hitters~\cite{zhang2023h2o}, per-head important tokens~\cite{li2024snapkv,ge2024fastgen}, persistent-importance tokens~\cite{liu2024scissorhands}, attention sinks~\cite{xiao2024streamingllm}, or progressively fewer tokens in deeper layers~\cite{yang2024pyramidinfer}.
9	Recent per-head eviction methods allocate non-uniform budgets across heads based on retrieval-vs-reasoning importance~\cite{fu2025headkv} or adaptive optimization extending SnapKV/PyramidKV~\cite{feng2025adakv}, confirming that head-level heterogeneity is exploitable for eviction; our work shows it is equally exploitable for quantization.
10	
11	
12	\paragraph{Mixed-Precision Rate-Distortion Allocation.}
13	RateQuant~\cite{zuo2026ratequant} formulates per-head bit-width selection as an MCKP and proves greedy optimality for consecutive bit-widths $\{2,\ldots,6\}$ via the polymatroid structure.
14	On hardware-aligned $\{2,4,8,16\}$, this structure breaks; we show that unconstrained solvers fail catastrophically due to 2-bit distortion compounding, a failure mode absent in RateQuant's setting.
15	Related mixed-precision work operates at coarser granularity---layer-level via gradient-based sensitivity~\cite{li2025kvmix} or Pareto search over hardware-friendly precision
…[truncated 658 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_writing_r1_w7_related_work_20260515T044227",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 4 · 2026-05-15T04:46:25.551834+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/docs/paper/references.bib"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_writing_r1_w7_related_work_20260515T044227",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/docs/paper/references.bib"
  }
}
```

</details>

---

### Tool result

_source line 5 · 2026-05-15T04:46:25.552023+00:00_

1	% Auto-generated from literature_map.yaml (verified=true entries)
2	
3	@inproceedings{liu2024kivi,
4	  title = {{KIVI}: A Tuning-Free Asymmetric 2bit Quantization for {KV} Cache},
5	  author = {Zirui Liu and Jiayi Yuan and Hongye Jin and Shaochen Zhong and Zhaozhuo Xu and Vladimir Braverman and Beidi Chen and Xia Hu},
6	  year = {2024},
7	  booktitle = {ICML 2024},
8	  url = {https://arxiv.org/abs/2402.02750},
9	}
10	
11	@inproceedings{hooper2024kvquant,
12	  title = {{KVQuant}: Towards 10 Million Context Length {LLM} Inference with {KV} Cache Quantization},
13	  author = {Coleman Hooper and Sehoon Kim and Hiva Mohammadzadeh and Michael W. Mahoney and Yakun Sophia Shao and Kurt Keutzer and Amir Gholami},
14	  year = {2024},
15	  booktitle = {NeurIPS 2024},
16	  url = {https://arxiv.org/abs/2401.18079},
17	}
18	
19	@inproceedings{lin2024qserve,
20	  title = {{QServe}: {W4A8KV4} Quantization and System Co-design for Efficient {LLM} Serving},
21	  author = {Yujun Lin and Haotian Tang and Shang Yang and Zhekai Zhang and Guangxuan Xiao and Chuang Gan and Song Han},
22	  year = {2025},
23	  booktitle = {MLSys 2025},
24	  url = {https://arxiv.org/abs/2405.04532},
25	}
26	
27	@inproceedings{he2024zipcache,
28	  title = {{ZipCache}: Accurate and Efficient {KV} Cache Quantization with Salient Token Identification},
29	  author = {Yefei He and Luoming Zhang and Weijia Wu and Jing Liu and Hong Zhou and Bohan Zhuang},
30	  year = {2024},
31	  booktitle = {NeurIPS 2024},
32	  url = {https://arxiv.org/abs/2405.14256},
33	}
34	
35	@misc{kang2024gear,
36	  title = {{GEAR}: An Efficient {KV} Cache Compression Recipe for Near-Lossless Generative Inference of {LLM}},
37	  author = {Hao Kang and Qingru Zhang and Souvik Kundu and Geonhwa Jeong and Zaoxing Liu and Tushar Krishna and Tuo Zhao},
38	  year = {2024},
39	  note = {arXiv preprint},
40	  url = {https://arxiv.org/abs/2403.05527},
41	  eprint = {2403.05527},
42	  archivePrefix = {arXiv},
43	}
44	
45	@misc{duanmu2024skvq,
46	  ti
…[truncated 6252 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_writing_r1_w7_related_work_20260515T044227",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 6 · 2026-05-15T04:46:25.552210+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:WebSearch",
  "max_results": "1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_writing_r1_w7_related_work_20260515T044227",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:WebSearch",
    "max_results": "1"
  }
}
```

</details>

---

### Tool result

_source line 7 · 2026-05-15T04:46:25.552342+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_writing_r1_w7_related_work_20260515T044227",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 8 · 2026-05-15T04:46:25.552462+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "HAWQ Hessian aware quantization ICCV 2019 mixed precision"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_writing_r1_w7_related_work_20260515T044227",
  "tool": "WebSearch",
  "tool_args": {
    "query": "HAWQ Hessian aware quantization ICCV 2019 mixed precision"
  }
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-15T04:46:25.552582+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "HAWQ-V2 Hessian aware quantization NeurIPS 2020 block wise mixed precision"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_writing_r1_w7_related_work_20260515T044227",
  "tool": "WebSearch",
  "tool_args": {
    "query": "HAWQ-V2 Hessian aware quantization NeurIPS 2020 block wise mixed precision"
  }
}
```

</details>

---

### Tool call

_source line 10 · 2026-05-15T04:46:25.552729+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "HAQ hardware aware automated quantization CVPR 2019 Han"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_writing_r1_w7_related_work_20260515T044227",
  "tool": "WebSearch",
  "tool_args": {
    "query": "HAQ hardware aware automated quantization CVPR 2019 Han"
  }
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-15T04:46:25.552848+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "RotateKV rotation KV cache quantization IJCAI 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_writing_r1_w7_related_work_20260515T044227",
  "tool": "WebSearch",
  "tool_args": {
    "query": "RotateKV rotation KV cache quantization IJCAI 2025"
  }
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-15T04:46:25.552997+00:00_

Web search results for query: "HAWQ-V2 Hessian aware quantization NeurIPS 2020 block wise mixed precision"

Links: [{"title":"HAWQ-V2: Hessian Aware trace-Weighted Quantization of Neural Networks","url":"https://www.stat.berkeley.edu/~mmahoney/pubs/NeurIPS-2020-hawq-v2.pdf"},{"title":"HAWQ-V2: Hessian Aware trace-Weighted Quantization of Neural Networks","url":"https://proceedings.neurips.cc/paper_files/paper/2020/hash/d77c703536718b95308130ff2e5cf9ee-Abstract.html"},{"title":"[1905.03696] HAWQ: Hessian AWare Quantization of Neural Networks with Mixed-Precision","url":"https://arxiv.org/abs/1905.03696"},{"title":"Review for NeurIPS paper: HAWQ-V2: Hessian Aware trace-Weighted Quantization of Neural Networks","url":"https://papers.nips.cc/paper_files/paper/2020/file/d77c703536718b95308130ff2e5cf9ee-Review.html"},{"title":"[1911.03852] HAWQ-V2: Hessian Aware trace-Weighted Quantization of Neural Networks","url":"https://arxiv.org/abs/1911.03852"},{"title":"GitHub - Zhen-Dong/HAWQ: Quantization library for PyTorch. Support low-precision and mixed-precision quantization, with hardware implementation through TVM. · GitHub","url":"https://github.com/zhen-dong/hawq"},{"title":"HAWQ: Hessian AWare Quantization of Neural Networks with Mixed-Precision","url":"https://www.stat.berkeley.edu/~mmahoney/pubs/HAWQ_ICCV_2019_paper.pdf"},{"title":"[PDF] HAWQ: Hessian AWare Quantization of Neural Networks With Mixed-Precision | Semantic Scholar","url":"https://www.semanticscholar.org/paper/HAWQ:-Hessian-AWare-Quantization-of-Neural-Networks-Dong-Yao/1a858b96d2fdfeadf8c0f7126cbd55825223fb9d"},{"title":"(PDF) HAWQ: Hessian AWare Quantization of Neural Networks With Mixed-Precision","url":"https://www.researchgate.net/publication/339558933_HAWQ_Hessian_AWare_Quantization_of_Neural_Networks_With_Mixed-Precision"},{"title":"HAWQ-V2: Hessian Aware trace-Weighted Quantization of Neural Networks","url":"https://papers.nips.cc/paper/2020/hash/d77c703536718b95308130ff2e5cf9ee-Abstract.html"}]


…[truncated 1746 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_writing_r1_w7_related_work_20260515T044227",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 13 · 2026-05-15T04:46:25.553178+00:00_

Web search results for query: "HAQ hardware aware automated quantization CVPR 2019 Han"

Links: [{"title":"GitHub - mit-han-lab/haq: [CVPR 2019, Oral] HAQ: Hardware-Aware Automated Quantization with Mixed Precision · GitHub","url":"https://github.com/mit-han-lab/haq"},{"title":"HAQ: Hardware-Aware Automated Quantization with Mixed Precision","url":"https://openaccess.thecvf.com/content_CVPR_2019/papers/Wang_HAQ_Hardware-Aware_Automated_Quantization_With_Mixed_Precision_CVPR_2019_paper.pdf"},{"title":"[1811.08886] HAQ: Hardware-Aware Automated Quantization with Mixed Precision","url":"https://arxiv.org/abs/1811.08886"},{"title":"GitHub - zhyj3038/haq-release: [CVPR 2019, Oral] HAQ: Hardware-Aware Automated Quantization with Mixed Precision","url":"https://github.com/zhyj3038/haq-release"},{"title":"haq/README.md at master · mit-han-lab/haq","url":"https://github.com/mit-han-lab/haq/blob/master/README.md"},{"title":"GitHub - phrb/haq-release: [CVPR 2019, Oral] HAQ: Hardware-Aware Automated Quantization with Mixed Precision · GitHub","url":"https://github.com/phrb/haq-release"},{"title":"HAQ: Hardware-Aware Automated Quantization","url":"https://hanlab.mit.edu/projects/haq"},{"title":"haq/rl_quantize.py at master · mit-han-lab/haq","url":"https://github.com/mit-han-lab/haq/blob/master/rl_quantize.py"},{"title":"HAQ: Hardware-Aware Automated Quantization With Mixed Precision - MIT-IBM Watson AI Lab","url":"https://mitibmwatsonailab.mit.edu/research/blog/haq-hardware-aware-automated-quantization-with-mixed-precision/"},{"title":"Actions · mit-han-lab/haq","url":"https://github.com/mit-han-lab/haq/actions"}]

I found comprehensive results for your search on HAQ (Hardware-Aware Automated Quantization). Here's what I found:

## Overview

HAQ is a CVPR 2019 oral paper on Hardware-Aware Automated Quantization with Mixed Precision, authored by Kuan Wang, Zhijian Liu, Yujun Lin, Ji Lin, and Song Han from MIT.

## Key Concept

The framework addresses the challenge of finding opt
…[truncated 1217 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_writing_r1_w7_related_work_20260515T044227",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-15T04:46:25.553355+00:00_

Web search results for query: "HAWQ Hessian aware quantization ICCV 2019 mixed precision"

Links: [{"title":"HAWQ: Hessian AWare Quantization of Neural Networks with Mixed-Precision","url":"https://www.stat.berkeley.edu/~mmahoney/pubs/HAWQ_ICCV_2019_paper.pdf"},{"title":"[1905.03696] HAWQ: Hessian AWare Quantization of Neural Networks with Mixed-Precision","url":"https://arxiv.org/abs/1905.03696"},{"title":"[PDF] HAWQ: Hessian AWare Quantization of Neural Networks With Mixed-Precision | Semantic Scholar","url":"https://www.semanticscholar.org/paper/HAWQ:-Hessian-AWare-Quantization-of-Neural-Networks-Dong-Yao/1a858b96d2fdfeadf8c0f7126cbd55825223fb9d"},{"title":"ICCV 2019 Open Access Repository","url":"https://openaccess.thecvf.com/content_ICCV_2019/html/Dong_HAWQ_Hessian_AWare_Quantization_of_Neural_Networks_With_Mixed-Precision_ICCV_2019_paper.html"},{"title":"GitHub - Zhen-Dong/HAWQ: Quantization library for PyTorch. Support low-precision and mixed-precision quantization, with hardware implementation through TVM. · GitHub","url":"https://github.com/zhen-dong/hawq"},{"title":"(PDF) HAWQ: Hessian AWare Quantization of Neural Networks With Mixed-Precision","url":"https://www.researchgate.net/publication/339558933_HAWQ_Hessian_AWare_Quantization_of_Neural_Networks_With_Mixed-Precision"},{"title":"HAWQ: Hessian AWare Quantization of Neural Networks With Mixed-Precision [Quick Review]","url":"https://liner.com/review/hawq-hessian-aware-quantization-neural-networks-with-mixedprecision"},{"title":"HAWQ: Hessian AWare Quantization of Neural Networks ...","url":"https://www.computer.org/csdl/proceedings-article/iccv/2019/480300a293/1hVlrFy597i"},{"title":"HAWQ: Hessian AWare Quantization of Neural Networks with Mixed-Precision","url":"http://amirgholami.org/assets/papers/2019_hawq.pdf"},{"title":"[1911.03852] HAWQ-V2: Hessian Aware trace-Weighted Quantization of Neural Networks","url":"https://arxiv.org/abs/1911.03852"}]

Based on the search results, here's what I found abou
…[truncated 1614 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_writing_r1_w7_related_work_20260515T044227",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 15 · 2026-05-15T04:46:25.553531+00:00_

Web search results for query: "RotateKV rotation KV cache quantization IJCAI 2025"

Links: [{"title":"RotateKV: Accurate and Robust 2-Bit KV Cache Quantization","url":"https://www.ijcai.org/proceedings/2025/0690.pdf"},{"title":"RotateKV: Accurate and Robust 2-Bit KV Cache Quantization for LLMs via Outlier-Aware Adaptive Rotations | IJCAI","url":"https://www.ijcai.org/proceedings/2025/690"},{"title":"[2501.16383] RotateKV: Accurate and Robust 2-Bit KV Cache Quantization for LLMs via Outlier-Aware Adaptive Rotations","url":"https://arxiv.org/abs/2501.16383"},{"title":"RotateKV: Accurate and Robust 2-Bit KV Cache Quantization for LLMs via Outlier-Aware Adaptive Rotations","url":"https://www.researchgate.net/publication/388460119_RotateKV_Accurate_and_Robust_2-Bit_KV_Cache_Quantization_for_LLMs_via_Outlier-Aware_Adaptive_Rotations"},{"title":"FibQuant: Universal Vector Quantization for Random-Access KV-Cache Compression","url":"https://arxiv.org/html/2605.11478"},{"title":"RotateKV: Accurate and Robust 2-Bit KV Cache Quantization for LLMs via Outlier-Aware Adaptive Rotations","url":"https://paperreading.club/page?id=280530"},{"title":"[2605.11478] FibQuant: Universal Vector Quantization for Random-Access KV-Cache Compression","url":"https://arxiv.org/abs/2605.11478"},{"title":"[Literature Review] RotateKV: Accurate and Robust 2-Bit KV Cache Quantization for LLMs via Outlier-Aware Adaptive Rotations","url":"https://www.themoonlight.io/en/review/rotatekv-accurate-and-robust-2-bit-kv-cache-quantization-for-llms-via-outlier-aware-adaptive-rotations"},{"title":"MixKVQ: Query-Aware Mixed-Precision KV Cache Quantization for Long-Context Reasoning","url":"https://arxiv.org/html/2512.19206v1"},{"title":"PapersAnon on X: \"RotateKV: Accurate and Robust 2-Bit KV Cache Quantization for LLMs via Outlier-Aware Adaptive Rotations KV quant method that utilizes outlier aware rotation, pre-RoPE grouped-head rotation, and attention-sink-aware quantization to achieve a 3.97× reduction in p
…[truncated 1741 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_writing_r1_w7_related_work_20260515T044227",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 16 · 2026-05-15T04:46:25.553698+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "MiniKV ACL Findings 2025 minimal KV cache LLM"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_writing_r1_w7_related_work_20260515T044227",
  "tool": "WebSearch",
  "tool_args": {
    "query": "MiniKV ACL Findings 2025 minimal KV cache LLM"
  }
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-15T04:46:25.553825+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "AQUA-KV ICML 2025 adaptive quantization KV cache"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_writing_r1_w7_related_work_20260515T044227",
  "tool": "WebSearch",
  "tool_args": {
    "query": "AQUA-KV ICML 2025 adaptive quantization KV cache"
  }
}
```

</details>

---

### Tool call

_source line 18 · 2026-05-15T04:46:25.553948+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "PM-KVQ KV cache quantization paper"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_writing_r1_w7_related_work_20260515T044227",
  "tool": "WebSearch",
  "tool_args": {
    "query": "PM-KVQ KV cache quantization paper"
  }
}
```

</details>

---

### Tool call

_source line 19 · 2026-05-15T04:46:25.554063+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Kitty KV cache quantization LLM paper"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_writing_r1_w7_related_work_20260515T044227",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Kitty KV cache quantization LLM paper"
  }
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-15T04:46:25.554207+00:00_

Web search results for query: "MiniKV ACL Findings 2025 minimal KV cache LLM"

Links: [{"title":"MiniKV: Pushing the Limits of 2-Bit KV Cache via Compression and System Co-Design for Efficient Long Context Inference - ACL Anthology","url":"https://aclanthology.org/2025.findings-acl.952/"},{"title":"MiniKV: Pushing the Limits of 2-Bit KV Cache via ...","url":"https://aclanthology.org/2025.findings-acl.952.pdf"},{"title":"MiniKV: Pushing the Limits of 2-Bit KV Cache via Compression and System Co-Design for Efficient Long Context Inferences","url":"https://supercomputing-system-ai-lab.github.io/projects/minikv/"},{"title":"MiniKV: Pushing the Limits of 2-Bit KV Cache via Compression and System Co-Design for Efficient Long Context Inference","url":"https://arxiv.org/html/2411.18077v3"},{"title":"Introducing MiniKV: Efficient KV Cache for LLM Inference","url":"https://www.linkedin.com/posts/minjia-zhang-05857226_llm-inferenceoptimization-kvcache-activity-7355610760175120385-AP-o"},{"title":"GitHub - TreeAI-Lab/Awesome-KV-Cache-Management: This repository serves as a comprehensive survey of LLM development, featuring numerous research papers along with their corresponding code links. · GitHub","url":"https://github.com/TreeAI-Lab/Awesome-KV-Cache-Management"},{"title":"KVPR: Efficient LLM Inference with I/O-Aware KV Cache ...","url":"https://aclanthology.org/2025.findings-acl.997.pdf"},{"title":"MiniKV: Pushing the Limits of 2-Bit KV Cache via Compression and System Co-Design for Efficient Long Context Inference | Request PDF","url":"https://www.researchgate.net/publication/394273621_MiniKV_Pushing_the_Limits_of_2-Bit_KV_Cache_via_Compression_and_System_Co-Design_for_Efficient_Long_Context_Inference"},{"title":"MiniKV: 2-Bit KV Cache for LLMs | PDF | Computing","url":"https://www.scribd.com/document/814284617/2411-18077v2"},{"title":"Findings of the Association for Computational Linguistics:","url":"https://aclanthology.org/2025.findings-naacl.84.pdf"}]

Based on the sear
…[truncated 1433 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_writing_r1_w7_related_work_20260515T044227",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 21 · 2026-05-15T04:46:25.554373+00:00_

Web search results for query: "Kitty KV cache quantization LLM paper"

Links: [{"title":"[2511.18643] Kitty: Accurate and Efficient 2-bit KV Cache Quantization with Dynamic Channel-wise Precision Boost","url":"https://arxiv.org/abs/2511.18643"},{"title":"KITTY: ACCURATE AND EFFICIENT 2-BIT KV CACHE QUANTIZATION WITH","url":"https://www.arxiv.org/pdf/2511.18643"},{"title":"GitHub - Summer-Summer/Kitty: Algorithm-System Co-design: accurate and efficient 2-bit KV cache quantization for LLM Inference..","url":"https://github.com/Summer-Summer/Kitty"},{"title":"1 Introduction","url":"https://arxiv.org/html/2511.18643"},{"title":"KV Cache Optimization Strategies for Scalable and Efficient LLM Inference","url":"https://arxiv.org/html/2603.20397v1"},{"title":"GitHub - SqueezeAILab/KVQuant: [NeurIPS 2024] KVQuant: Towards 10 Million Context Length LLM Inference with KV Cache Quantization · GitHub","url":"https://github.com/SqueezeAILab/KVQuant"},{"title":"NeurIPS Poster KVQuant: Towards 10 Million Context Length LLM Inference with KV Cache Quantization","url":"https://neurips.cc/virtual/2024/poster/96936"},{"title":"[2402.02750] KIVI: A Tuning-Free Asymmetric 2bit Quantization for KV Cache","url":"https://arxiv.org/abs/2402.02750"},{"title":"[2401.18079] KVQuant: Towards 10 Million Context Length LLM Inference with KV Cache Quantization","url":"https://arxiv.org/abs/2401.18079"},{"title":"Top 10 KV Cache Compression Techniques for LLM Inference: Reducing Memory Overhead Across Eviction, Quantization, and Low-Rank Methods - MarkTechPost","url":"https://www.marktechpost.com/2026/04/29/top-10-kv-cache-compression-techniques-for-llm-inference-reducing-memory-overhead-across-eviction-quantization-and-low-rank-methods/"}]

Based on the search results, I found information about the Kitty paper on KV cache quantization:

## Kitty: KV Cache Quantization Paper

Kitty is titled "Accurate and Efficient 2-bit KV Cache Quantization with Dynamic Channel-wise Precision Boost" by Haojun Xia 
…[truncated 1200 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_writing_r1_w7_related_work_20260515T044227",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 22 · 2026-05-15T04:46:25.554562+00:00_

Web search results for query: "AQUA-KV ICML 2025 adaptive quantization KV cache"

Links: [{"title":"ICML Poster Cache Me If You Must: Adaptive Key-Value Quantization for Large Language Models","url":"https://icml.cc/virtual/2025/poster/46067"},{"title":"[2501.19392] Cache Me If You Must: Adaptive Key-Value Quantization for Large Language Models","url":"https://arxiv.org/abs/2501.19392"},{"title":"Cache Me If You Must: Adaptive Key-Value Quantization for Large Language Models","url":"https://arxiv.org/html/2501.19392v1"},{"title":"Cache Me If You Must: Adaptive Key-Value Quantization for Large Language Models | OpenReview","url":"https://openreview.net/forum?id=COowwJOAZi&noteId=eSHMRqb2AD"},{"title":"Cache Me If You Must: Adaptive Key-Value Quantization for Large Language Models","url":"https://proceedings.mlr.press/v267/shutova25a.html"},{"title":"ICML Poster KVTuner: Sensitivity-Aware Layer-Wise Mixed-Precision KV Cache Quantization for Efficient and Nearly Lossless LLM Inference","url":"https://icml.cc/virtual/2025/poster/43487"},{"title":"QAQ: Quality Adaptive Quantization for LLM KV Cache Wen Cheng*","url":"https://openaccess.thecvf.com/content/ICCV2025W/U&ME/papers/Cheng_QAQ_Quality_Adaptive_Quantization_for_LLM_KV_Cache_ICCVW_2025_paper.pdf"},{"title":"Don’t Waste Bits! Adaptive KV-Cache Quantization for Lightweight On-Device LLMs","url":"https://arxiv.org/html/2604.04722v1"},{"title":"Hardware-Efficient Key-Value Caching in LLMs | by DrKilngon | Medium","url":"https://medium.com/@DrKilngon/hardware-efficient-key-value-caching-in-llms-3f9966c012cf"},{"title":"AsymKV: Enabling 1-Bit Quantization of KV Cache with ...","url":"https://aclanthology.org/2025.coling-main.158.pdf"}]

I found comprehensive information about AQUA-KV from ICML 2025. Here's a summary of the research:

## AQUA-KV Overview

AQUA-KV is an adaptive quantization for Key-Value caches that relies on compact adapters to exploit existing dependencies between Keys and Values, and aims to "optimall
…[truncated 1670 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_writing_r1_w7_related_work_20260515T044227",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 23 · 2026-05-15T04:46:25.554780+00:00_

Web search results for query: "PM-KVQ KV cache quantization paper"

Links: [{"title":"GitHub - thu-nics/PM-KVQ: The official code implementation for paper \"PM-KVQ: Progressive Mixed-precision KV Cache Quantization for Long-CoT LLMs\"","url":"https://github.com/thu-nics/PM-KVQ"},{"title":"PM-KVQ: Progressive Mixed-precision KV Cache Quantization for Long-CoT LLMs | OpenReview","url":"https://openreview.net/forum?id=Vem6FQvRvq"},{"title":"PM-KVQ: Progressive Mixed-precision KV Cache Quantization for Long-CoT LLMs","url":"https://arxiv.org/html/2505.18610"},{"title":"[2505.18610] PM-KVQ: Progressive Mixed-precision KV Cache Quantization for Long-CoT LLMs","url":"https://arxiv.org/abs/2505.18610"},{"title":"Quantized KV Cache - vLLM","url":"https://docs.vllm.ai/en/latest/features/quantization/quantized_kvcache/"},{"title":"PM-KVQ: PROGRESSIVE MIXED-PRECISION KV CACHE ...","url":"https://openreview.net/pdf/aa856ae96a62b942c63e9f66b198e0a68f9601e8.pdf"},{"title":"Is KV Cache Quantization Sabotaging Your Context? — We test the impact of quantizing caches on long-horizon agentic coding workloads.","url":"https://dasroot.net/posts/2026/05/kv-cache-quantization-agentic-coding-long-horizon/"},{"title":"PM-KVQ: Progressive Mixed-precision KV Cache Quantization for Long-CoT LLMs | Request PDF","url":"https://www.researchgate.net/publication/392105885_PM-KVQ_Progressive_Mixed-precision_KV_Cache_Quantization_for_Long-CoT_LLMs"},{"title":"GitHub - SqueezeAILab/KVQuant: [NeurIPS 2024] KVQuant: Towards 10 Million Context Length LLM Inference with KV Cache Quantization · GitHub","url":"https://github.com/SqueezeAILab/KVQuant"},{"title":"Towards 10 Million Context Length LLM Inference with KV ...","url":"https://www.stat.berkeley.edu/~mmahoney/pubs/neurips-2024-kvquant.pdf"}]

Based on the search results, I found information about the PM-KVQ paper on KV cache quantization:

## PM-KVQ: Progressive Mixed-Precision KV Cache Quantization for Long-CoT LLMs

The paper addresses KV cache mem
…[truncated 1463 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_writing_r1_w7_related_work_20260515T044227",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 24 · 2026-05-15T04:46:25.554970+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "RotateKV authors arxiv 2501.16383 Su"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_writing_r1_w7_related_work_20260515T044227",
  "tool": "WebSearch",
  "tool_args": {
    "query": "RotateKV authors arxiv 2501.16383 Su"
  }
}
```

</details>

---

### Tool call

_source line 25 · 2026-05-15T04:46:25.555097+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "MiniKV 2-bit KV cache arxiv 2411.18077 authors Akshat Sharma"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_writing_r1_w7_related_work_20260515T044227",
  "tool": "WebSearch",
  "tool_args": {
    "query": "MiniKV 2-bit KV cache arxiv 2411.18077 authors Akshat Sharma"
  }
}
```

</details>

---

### Tool call

_source line 26 · 2026-05-15T04:46:25.555216+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"Cache Me If You Must\" 2501.19392 authors Shutova adaptive KV quantization"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_writing_r1_w7_related_work_20260515T044227",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"Cache Me If You Must\" 2501.19392 authors Shutova adaptive KV quantization"
  }
}
```

</details>

---

### Tool call

_source line 27 · 2026-05-15T04:46:25.555332+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "PM-KVQ Progressive Mixed-precision arxiv 2505.18610 authors"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_writing_r1_w7_related_work_20260515T044227",
  "tool": "WebSearch",
  "tool_args": {
    "query": "PM-KVQ Progressive Mixed-precision arxiv 2505.18610 authors"
  }
}
```

</details>

---

### Tool result

_source line 28 · 2026-05-15T04:46:25.555486+00:00_

Web search results for query: "PM-KVQ Progressive Mixed-precision arxiv 2505.18610 authors"

Links: [{"title":"[2505.18610] PM-KVQ: Progressive Mixed-precision KV Cache Quantization for Long-CoT LLMs","url":"https://arxiv.org/abs/2505.18610"},{"title":"PM-KVQ: Progressive Mixed-precision KV Cache Quantization for Long-CoT LLMs | Request PDF","url":"https://www.researchgate.net/publication/392105885_PM-KVQ_Progressive_Mixed-precision_KV_Cache_Quantization_for_Long-CoT_LLMs"},{"title":"PM-KVQ: Progressive Mixed-precision KV Cache Quantization for Long-CoT LLMs","url":"https://arxiv.org/html/2505.18610"},{"title":"RateQuant: Optimal Mixed-Precision KV Cache Quantization via Rate-Distortion Theory","url":"https://arxiv.org/html/2605.06675"},{"title":"PM-KVQ: Progressive Mixed-precision KV Cache Quantization for Long-CoT LLMs | OpenReview","url":"https://openreview.net/forum?id=Vem6FQvRvq"},{"title":"Progressive Mixed-precision KV Cache Quantization for ...","url":"https://nicsefc.ee.tsinghua.edu.cn/nics_file/pdf/716c42fa-d7f1-4fd9-b74d-ab279456d2d8.pdf"},{"title":"PM-KVQ: PROGRESSIVE MIXED-PRECISION KV CACHE ...","url":"https://openreview.net/pdf/aa856ae96a62b942c63e9f66b198e0a68f9601e8.pdf"},{"title":"Progressive Mixed-precision KV Cache Quantization for ...","url":"https://arxiv.org/pdf/2505.18610"},{"title":"MixKVQ: Query-Aware Mixed-Precision KV Cache Quantization for Long-Context Reasoning","url":"https://arxiv.org/html/2512.19206v1"},{"title":"Progressive Mixed-Precision Decoding for Efficient LLM Inference","url":"https://arxiv.org/html/2410.13461v1"}]

Based on the search results, the authors of the PM-KVQ paper (arxiv 2505.18610) are: Tengxuan Liu, Shiyao Li, Jiayi Yang, Tianchen Zhao, Feng Zhou, Xiaohui Song, Guohao Dai, Shengen Yan, Huazhong Yang, and Yu Wang.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_writing_r1_w7_related_work_20260515T044227",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 29 · 2026-05-15T04:46:25.555663+00:00_

Web search results for query: "MiniKV 2-bit KV cache arxiv 2411.18077 authors Akshat Sharma"

Links: [{"title":"[2411.18077] MiniKV: Pushing the Limits of LLM Inference via 2-Bit Layer-Discriminative KV Cache","url":"https://arxiv.org/abs/2411.18077"},{"title":"[2411.18077v2] MiniKV: Pushing the Limits of LLM Inference via 2-Bit Layer-Discriminative KV Cache","url":"https://arxiv.org/abs/2411.18077v2"},{"title":"MiniKV: Pushing the Limits of 2-Bit KV Cache via Compression and System Co-Design for Efficient Long Context Inference","url":"https://arxiv.org/html/2411.18077"},{"title":"MiniKV: Pushing the Limits of 2-Bit KV Cache via Compression and System Co-Design for Efficient Long Context Inferences","url":"https://supercomputing-system-ai-lab.github.io/projects/minikv/"},{"title":"Pushing the Limits of LLM Inference via 2-Bit Layer-Discriminative KV Cache | Request PDF","url":"https://www.researchgate.net/publication/386211053_Pushing_the_Limits_of_LLM_Inference_via_2-Bit_Layer-Discriminative_KV_Cache"},{"title":"1 Introduction","url":"https://arxiv.org/html/2411.18077v1"},{"title":"KITTY: ACCURATE AND EFFICIENT 2-BIT KV CACHE QUANTIZATION WITH","url":"https://www.arxiv.org/pdf/2511.18643"},{"title":"MiniKV: Pushing the Limits of 2-Bit KV Cache via Compression and System Co-Design for Efficient Long Context Inference - ACL Anthology","url":"https://aclanthology.org/2025.findings-acl.952/"},{"title":"MiniKV: Pushing the Limits of LLM Inference via 2-Bit Layer-Discriminative KV Cache | PromptLayer","url":"https://www.promptlayer.com/research-papers/minikv-shrinking-llm-memory-for-longer-conversations"},{"title":"Computation and Language Nov 2024","url":"https://www.arxiv.org/list/cs.CL/2024-11?skip=825&show=25"}]

Based on the search results, I found detailed information about the MiniKV paper (arxiv 2411.18077):

## MiniKV: 2-Bit KV Cache Paper

**Title:** MiniKV: Pushing the Limits of LLM Inference via 2-Bit Layer-Discriminative KV Cache

**Authors:** Akshat Sharma
…[truncated 1255 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_writing_r1_w7_related_work_20260515T044227",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 30 · 2026-05-15T04:46:25.555830+00:00_

Web search results for query: "RotateKV authors arxiv 2501.16383 Su"

Links: [{"title":"[2501.16383] RotateKV: Accurate and Robust 2-Bit KV Cache Quantization for LLMs via Outlier-Aware Adaptive Rotations","url":"https://arxiv.org/abs/2501.16383"},{"title":"RotateKV: Accurate and Robust 2-Bit KV Cache Quantization for LLMs via Outlier-Aware Adaptive Rotations","url":"https://www.researchgate.net/publication/388460119_RotateKV_Accurate_and_Robust_2-Bit_KV_Cache_Quantization_for_LLMs_via_Outlier-Aware_Adaptive_Rotations"},{"title":"arXiv.org e-Print archive","url":"https://arxiv.org/"},{"title":"Computer Vision and Pattern Recognition","url":"https://arxiv.org/list/cs.CV/pastweek?skip=7&show=1000"},{"title":"Untitled Document","url":"https://arxiv.org/html/2501.16383"},{"title":"arXiv.org | 232753 Publications | 16958 Citations | Top authors | Related journals","url":"https://scispace.com/journals/arxiv-org-bl5k1ptr"},{"title":"[2503.16383] Quantum Characterization, Verification, and Validation","url":"https://arxiv.org/abs/2503.16383"},{"title":"DeepSeek-R1: Incentivizing Reasoning Capability in LLMs via Reinforcement Learning","url":"https://arxiv.org/html/2501.12948v1"},{"title":"Computer Science authors/titles recent submissions (821 skipped)","url":"https://export.arxiv.org/list/cs/pastweek?skip=821&show=250"},{"title":"[2601.16383] On The Robustness of Foundational 3D Medical Image Segmentation Models Against Imprecise Visual Prompts","url":"https://arxiv.org/abs/2601.16383"}]

Based on the search results, I found the paper you're looking for:

The authors of arxiv paper 2501.16383 "RotateKV: Accurate and Robust 2-Bit KV Cache Quantization for LLMs via Outlier-Aware Adaptive Rotations" are Zunhai Su, Zhe Chen, Wang Shen, Hanyu Wei, Linge Li, Huangqi Yu, and Kehong Yuan. The paper was submitted on January 25, 2025 and last revised on February 2, 2025.

The paper proposes RotateKV, which achieves accurate and robust performance through innovations including Outlie
…[truncated 191 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_writing_r1_w7_related_work_20260515T044227",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 31 · 2026-05-15T04:46:25.555997+00:00_

Web search results for query: ""Cache Me If You Must" 2501.19392 authors Shutova adaptive KV quantization"

Links: [{"title":"[2501.19392] Cache Me If You Must: Adaptive Key-Value Quantization for Large Language Models","url":"https://arxiv.org/abs/2501.19392"},{"title":"Cache Me If You Must: Adaptive Key-Value Quantization for Large Language Models","url":"https://arxiv.org/html/2501.19392"},{"title":"Cache Me If You Must: Adaptive Key-Value Quantization ...","url":"https://arxiv.org/pdf/2501.19392"},{"title":"(PDF) Cache Me If You Must: Adaptive Key-Value Quantization for Large Language Models","url":"https://www.researchgate.net/publication/388633908_Cache_Me_If_You_Must_Adaptive_Key-Value_Quantization_for_Large_Language_Models"},{"title":"ICML Poster Cache Me If You Must: Adaptive Key-Value Quantization for Large Language Models","url":"https://icml.cc/virtual/2025/poster/46067"},{"title":"Cache Me If You Must: Adaptive Key-Value Quantization for Large Language Models | OpenReview","url":"https://openreview.net/forum?id=COowwJOAZi&noteId=eSHMRqb2AD"},{"title":"Cache Me If You Must: Adaptive Key-Value Quantization for Large Language Models","url":"https://proceedings.mlr.press/v267/shutova25a.html"},{"title":"Cache Me If You Must: Adaptive Key-Value Quantization for Large Language Models","url":"https://openreview.net/pdf?id=COowwJOAZi"},{"title":"[Literature Review] Cache Me If You Must: Adaptive Key-Value Quantization for Large Language Models","url":"https://www.themoonlight.io/en/review/cache-me-if-you-must-adaptive-key-value-quantization-for-large-language-models"},{"title":"KV Cache Quantization","url":"https://www.aussieai.com/research/kv-cache-quantization"}]

I found detailed information about this paper. Here's what I found:

## Paper Overview

"Cache Me If You Must: Adaptive Key-Value Quantization for Large Language Models" is arXiv paper 2501.19392, authored by Alina Shutova, Vladimir Malinovskii, Vage Egiazarian, Denis Kuznedelev, Denis Mazur, Nikita
…[truncated 1375 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_writing_r1_w7_related_work_20260515T044227",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 32 · 2026-05-15T04:46:25.556153+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "HAWQ arxiv 1905.03696 authors Dong Yao Gholami Mahoney Keutzer"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_writing_r1_w7_related_work_20260515T044227",
  "tool": "WebSearch",
  "tool_args": {
    "query": "HAWQ arxiv 1905.03696 authors Dong Yao Gholami Mahoney Keutzer"
  }
}
```

</details>

---

### Tool call

_source line 33 · 2026-05-15T04:46:25.556274+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "HAWQ-V2 arxiv 1911.03852 authors Dong Yao Arfeen Gholami Mahoney Keutzer"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_writing_r1_w7_related_work_20260515T044227",
  "tool": "WebSearch",
  "tool_args": {
    "query": "HAWQ-V2 arxiv 1911.03852 authors Dong Yao Arfeen Gholami Mahoney Keutzer"
  }
}
```

</details>

---

### Tool call

_source line 34 · 2026-05-15T04:46:25.556388+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Kitty 2-bit KV cache quantization arxiv 2511.18643 authors Haojun Xia"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_writing_r1_w7_related_work_20260515T044227",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Kitty 2-bit KV cache quantization arxiv 2511.18643 authors Haojun Xia"
  }
}
```

</details>

---

### Tool result

_source line 35 · 2026-05-15T04:46:25.556533+00:00_

Web search results for query: "HAWQ arxiv 1905.03696 authors Dong Yao Gholami Mahoney Keutzer"

Links: [{"title":"[1905.03696] HAWQ: Hessian AWare Quantization of Neural Networks with Mixed-Precision","url":"https://arxiv.org/abs/1905.03696"},{"title":"[1905.03696v1] HAWQ: Hessian AWare Quantization of Neural Networks with Mixed-Precision","url":"https://arxiv.org/abs/1905.03696v1"},{"title":"HAWQ: Hessian AWare Quantization of Neural Networks with Mixed-Precision","url":"https://arxiv.org/pdf/1905.03696"},{"title":"[PDF] HAWQ: Hessian AWare Quantization of Neural Networks With Mixed-Precision | Semantic Scholar","url":"https://www.semanticscholar.org/paper/HAWQ:-Hessian-AWare-Quantization-of-Neural-Networks-Dong-Yao/1a858b96d2fdfeadf8c0f7126cbd55825223fb9d"},{"title":"[PDF] HAWQ-V2: Hessian Aware trace-Weighted Quantization of Neural Networks | Semantic Scholar","url":"https://www.semanticscholar.org/paper/HAWQ-V2:-Hessian-Aware-trace-Weighted-Quantization-Dong-Yao/0a5d987ddb5463062babceca90ba974db0cf96e7"},{"title":"Arxiv","url":"https://arxiv.org/pdf/1905.03696v1"},{"title":"HAWQ-V3: Dyadic neural network quantization - Amazon Science","url":"https://www.amazon.science/publications/hawq-v3-dyadic-neural-network-quantization"},{"title":"[2101.08940] Hessian-Aware Pruning and Optimal Neural Implant","url":"https://arxiv.org/abs/2101.08940"},{"title":"[PDF] A Survey of Quantization Methods for Efficient Neural Network Inference | Semantic Scholar","url":"https://www.semanticscholar.org/paper/A-Survey-of-Quantization-Methods-for-Efficient-Gholami-Kim/04e283adccf66742130bde4a4dedcda8f549dd7e"},{"title":"Zhen Dong, Zhewei Yao, Daiyaan Arfeen, Amir Gholami, Michael W. Mahoney, Kurt Keutzer · HAWQ-V2: Hessian Aware trace-Weighted Quantization of Neural Networks","url":"https://slideslive.com/38937182/hawqv2-hessian-aware-traceweighted-quantization-of-neural-networks"}]

Based on the search results, I found the paper you're looking for:

The paper "HAWQ: Hessian AWare Qua
…[truncated 434 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_writing_r1_w7_related_work_20260515T044227",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 36 · 2026-05-15T04:46:25.556716+00:00_

Web search results for query: "HAWQ-V2 arxiv 1911.03852 authors Dong Yao Arfeen Gholami Mahoney Keutzer"

Links: [{"title":"[1911.03852] HAWQ-V2: Hessian Aware trace-Weighted Quantization of Neural Networks","url":"https://arxiv.org/abs/1911.03852"},{"title":"[1911.03852v1] HAWQ-V2: Hessian Aware trace-Weighted Quantization of Neural Networks","url":"https://arxiv.org/abs/1911.03852v1"},{"title":"[PDF] HAWQ-V2: Hessian Aware trace-Weighted Quantization of Neural Networks | Semantic Scholar","url":"https://www.semanticscholar.org/paper/HAWQ-V2:-Hessian-Aware-trace-Weighted-Quantization-Dong-Yao/0a5d987ddb5463062babceca90ba974db0cf96e7"},{"title":"[PDF] HAWQ-V2: Hessian Aware trace-Weighted Quantization of Neural Networks | Researchain","url":"https://researchain.net/archives/pdf/Hawq-V2-Hessian-Aware-Trace-Weighted-Quantization-Of-Neural-Networks-2142199"},{"title":"Zhen Dong, Zhewei Yao, Daiyaan Arfeen, Amir Gholami, Michael W. Mahoney, Kurt Keutzer · HAWQ-V2: Hessian Aware trace-Weighted Quantization of Neural Networks","url":"https://slideslive.com/38937182/hawqv2-hessian-aware-traceweighted-quantization-of-neural-networks"},{"title":"[1905.03696v1] HAWQ: Hessian AWare Quantization of Neural Networks with Mixed-Precision","url":"https://arxiv.org/abs/1905.03696v1"},{"title":"[1905.03696] HAWQ: Hessian AWare Quantization of Neural Networks with Mixed-Precision","url":"https://arxiv.org/abs/1905.03696"},{"title":"InfoQ: Mixed-Precision Quantization via Global Information Flow","url":"https://arxiv.org/pdf/2508.04753"},{"title":"[PDF] HAWQ: Hessian AWare Quantization of Neural Networks With Mixed-Precision | Semantic Scholar","url":"https://www.semanticscholar.org/paper/HAWQ:-Hessian-AWare-Quantization-of-Neural-Networks-Dong-Yao/1a858b96d2fdfeadf8c0f7126cbd55825223fb9d"},{"title":"HAWQ-V2: Hessian Aware trace-Weighted Quantization of Neural Networks - ADS","url":"https://ui.adsabs.harvard.edu/abs/2019arXiv191103852D/abstract"}]

Based on the search results, I found 
…[truncated 581 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_writing_r1_w7_related_work_20260515T044227",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 37 · 2026-05-15T04:46:25.556898+00:00_

Web search results for query: "Kitty 2-bit KV cache quantization arxiv 2511.18643 authors Haojun Xia"

Links: [{"title":"[2511.18643] Kitty: Accurate and Efficient 2-bit KV Cache Quantization with Dynamic Channel-wise Precision Boost","url":"https://arxiv.org/abs/2511.18643"},{"title":"KITTY: ACCURATE AND EFFICIENT 2-BIT KV CACHE QUANTIZATION WITH","url":"https://www.arxiv.org/pdf/2511.18643"},{"title":"1 Introduction","url":"https://arxiv.org/html/2511.18643"},{"title":"GitHub - Summer-Summer/Kitty: Algorithm-System Co-design: accurate and efficient 2-bit KV cache quantization for LLM Inference..","url":"https://github.com/Summer-Summer/Kitty"},{"title":"(PDF) Kitty: Accurate and Efficient 2-bit KV Cache Quantization with Dynamic Channel-wise Precision Boost","url":"https://www.researchgate.net/publication/397934403_Kitty_Accurate_and_Efficient_2-bit_KV_Cache_Quantization_with_Dynamic_Channel-wise_Precision_Boost"},{"title":"RateQuant: Optimal Mixed-Precision KV Cache Quantization via Rate-Distortion Theory","url":"https://arxiv.org/html/2605.06675"},{"title":"[2402.02750] KIVI: A Tuning-Free Asymmetric 2bit Quantization for KV Cache","url":"https://arxiv.org/abs/2402.02750"},{"title":"FibQuant: Universal Vector Quantization for Random-Access KV-Cache Compression","url":"https://arxiv.org/html/2605.11478"},{"title":"[PDF] KIVI: A Tuning-Free Asymmetric 2bit Quantization for KV Cache | Semantic Scholar","url":"https://www.semanticscholar.org/paper/KIVI:-A-Tuning-Free-Asymmetric-2bit-Quantization-KV-Liu-Yuan/a3e000e0d7f64c1d094c2a8bf6f43992cbabe91b"},{"title":"KIVI-Plug-and-play-2bit-KV-Cache-Quantization-with- ...","url":"https://www.researchgate.net/profile/Zirui-Liu-29/publication/376831635_KIVI_Plug-and-play_2bit_KV_Cache_Quantization_with_Streaming_Asymmetric_Quantization/links/658b5d282468df72d3db3280/KIVI-Plug-and-play-2bit-KV-Cache-Quantization-with-Streaming-Asymmetric-Quantization.pdf"}]

I found the paper you're looking for! Here's what I can tell you abou
…[truncated 1494 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_writing_r1_w7_related_work_20260515T044227",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 38 · 2026-05-15T04:46:25.557086+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "32\\.45|11\\.23|RateQuant|greedy",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/docs/paper",
  "output_mode": "content",
  "-n": "True",
  "head_limit": "80"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_writing_r1_w7_related_work_20260515T044227",
  "tool": "Grep",
  "tool_args": {
    "pattern": "32\\.45|11\\.23|RateQuant|greedy",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/docs/paper",
    "output_mode": "content",
    "-n": "True",
    "head_limit": "80"
  }
}
```

</details>

---

### Tool result

_source line 39 · 2026-05-15T04:46:25.557258+00:00_

docs/paper/related_work.tex:13:RateQuant~\cite{zuo2026ratequant} formulates per-head bit-width selection as an MCKP and proves greedy optimality for consecutive bit-widths $\{2,\ldots,6\}$ via the polymatroid structure.
docs/paper/related_work.tex:14:On hardware-aligned $\{2,4,8,16\}$, this structure breaks; we show that unconstrained solvers fail catastrophically due to 2-bit distortion compounding, a failure mode absent in RateQuant's setting.
docs/paper/experiments.tex:32:(2)~unconstrained greedy allocation (RateQuant-style~\cite{zuo2026ratequant});
docs/paper/experiments.tex:50:Qwen2.5-7B      & 9.81  & 15.45 & 32.45 & 36.92 & \textbf{11.23}$\pm$0.06 \\
docs/paper/experiments.tex:60:On Qwen2.5-7B, constrained MCKP achieves 11.23 PPL, a 27.3\% reduction over uniform 4-bit (15.45).
docs/paper/experiments.tex:62:Without the cardinality constraint, both greedy (32.45) and MCKP (36.92) perform \emph{worse} than uniform---a catastrophic failure caused by excessive 2-bit assignments that compound across layers.
docs/paper/experiments.tex:102:4$\times$ & 15.45 & 11.23 & $+$4.22 \\
docs/paper/experiments.tex:113:At 4$\times$, the gap is substantial: constrained MCKP reduces PPL from 15.45 to 11.23, a 27.3\% improvement.
docs/paper/experiments.tex:133:Qwen2.5-7B      & 11.23 & 11.52 & 11.69$\pm$0.47 & 12.23 \\
docs/paper/experiments.tex:142:On Qwen, MCKP (11.23) beats the L0-random median (11.52) by 0.29 PPL and the naive positional heuristic (12.23) by 1.00 PPL, confirming that profiling-guided selection outperforms both random and depth-based assignment.
docs/paper/experiments.tex:185:On Qwen2.5-7B, C4-calibrated MCKP achieves 11.29 PPL on WikiText-2 (vs.\ 15.45 uniform, a 27\% reduction), only 0.06 PPL above the WikiText-2-calibrated result (11.23).
docs/paper/main.bbl:147:\newblock \href {https://arxiv.org/abs/2605.06675} {{RateQuant}: Optimal
docs/paper/conclusion.tex:4:A single constraint---limiting simultaneously active 2-bit heads to $k \leq 8$ (7\% of heads)---re
…[truncated 8070 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_writing_r1_w7_related_work_20260515T044227",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 40 · 2026-05-15T04:46:25.557441+00:00_

called Edit

<details open><summary>🔧 Tool call — Edit</summary>

```json
{
  "replace_all": "False",
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/docs/paper/references.bib",
  "old_string": "@inproceedings{michel2019sixteen,\n  title = {Are Sixteen Heads Really Better than One?},\n  author = {Paul Michel and Omer Levy and Graham Neubig},\n  year = {2019},\n  booktitle = {NeurIPS 2019},\n  url = {https://arxiv.org/abs/1905.10650},\n}",
  "new_string": "@inproceedings{michel2019sixteen,\n  title = {Are Sixteen Heads Really Better than One?},\n  author = {Paul Michel and Omer Levy and Graham Neubig},\n  year = {2019},\n  booktitle = {NeurIPS 2019},\n  url = {https://arxiv.org/abs/1905.10650},\n}\n\n@inproceedings{dong2019hawq,\n  title = {{HAWQ}: {Hessian} AWare Quantization of Neural Networks with Mixed-Precision},\n  author = {Zhen Dong and Zhewei Yao and Amir Gholami and Michael W. Mahoney and Kurt Keutzer},\n  year = {2019},\n  booktitle = {ICCV 2019},\n  url = {https://arxiv.org/abs/1905.03696},\n}\n\n@inproceedings{dong2020hawqv2,\n  title = {{HAWQ-V2}: {Hessian} Aware trace-Weighted Quantization of Neural Networks},\n  author = {Zhen Dong and Zhewei Yao and Yaohui Cai and Daiyaan Arfeen and Amir Gholami and Michael W. Mahoney and Kurt Keutzer},\n  year = {2020},\n  booktitle = {NeurIPS 2020},\n  url = {https://arxiv.org/abs/1911.03852},\n}\n\n@inproceedings{wang2019haq,\n  title = {{HAQ}: Hardware-Aware Automated Quantization with Mixed Precision},\n  author = {Kuan Wang and Zhijian Liu and Yujun Lin and Ji Lin and Song Han},\n  year = {2019},\n  booktitle = {CVPR 2019},\n  url = {https://arxiv.org/abs/1811.08886},\n}\n\n@inproceedings{su2025rotatekv,\n  title = {{RotateKV}: Accurate and Robust 2-Bit {KV} Cache Quantization for {LLMs} via Outlier-Aware Adaptive Rotations},\n  author = {Zunhai Su and Zhe Chen and Wang Shen and Hanyu Wei and Linge Li and Huangqi Yu and Kehong Yuan},\n  year = {2025},\n  booktitle = {IJCAI 2025},\n  url = {https://arxiv.org/abs/2501.16383},\n}\n\n@inproceedings{sharma2025minikv,\n  title = {{MiniKV}: Pushing the Limits of 2-Bit {KV} Cache via Compression and System Co-Design for Efficient Long Context Inference},\n  author = {Akshat Sharma and Hangliang Ding and Jianping Li and Neel Dani and Minjia Zhang},\n  year = {2025},\n  booktitle = {Findings of ACL 2025},\n  url = {https://arxiv.org/abs/2411.18077},\n}\n\n@inproceedings{shutova2025aquakv,\n  title = {Cache Me If You Must: Adaptive Key-Value Quantization for Large Language Models},\n  author = {Alina Shutova and Vladimir Malinovskii and Vage Egiazarian and Denis Kuznedelev and Denis Mazur and Nikita Surkov and Ivan Ermakov and Dan Alistarh},\n  year = {2025},\n  booktitle = {ICML 2025},\n  url = {https://arxiv.org/abs/2501.19392},\n}\n\n@misc{liu2025pmkvq,\n  title = {{PM-KVQ}: Progressive Mixed-precision {KV} Cache Quantization for Long-CoT {LLMs}},\n  author = {Tengxuan Liu and Shiyao Li and Jiayi Yang and Tianchen Zhao and Feng Zhou and Xiaohui Song and Guohao Dai and Shengen Yan and Huazhong Yang and Yu Wang},\n  year = {2025},\n  note = {arXiv preprint},\n  url = {https://arxiv.org/abs/2505.18610},\n  eprint = {2505.18610},\n  archivePrefix = {arXiv},\n}\n\n@misc{xia2025kitty,\n  title = {{Kitty}: Accurate and Efficient 2-bit {KV} Cache Quantization with Dynamic Channel-wise Precision Boost},\n  author = {Haojun Xia and Xiaoxia Wu and Jisen Li and Robert Wu and Junxiong Wang and Jue Wang and Chenxi Li and Aman Singhal and Alay Dilipbhai Shah and Alpay Ariyak and Donglin Zhuang and Zhongzhu Zhou and Ben Athiwaratkun and Zhen Zheng and Shuaiwen Leon Song},\n  year = {2025},\n  note = {arXiv preprint},\n  url = {https://arxiv.org/abs/2511.18643},\n  eprint = {2511.18643},\n  archivePrefix = {arXiv},\n}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_writing_r1_w7_related_work_20260515T044227",
  "tool": "Edit",
  "tool_args": {
    "replace_all": "False",
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/docs/paper/references.bib",
    "old_string": "@inproceedings{michel2019sixteen,\n  title = {Are Sixteen Heads Really Better than One?},\n  author = {Paul Michel and Omer Levy and Graham Neubig},\n  year = {2019},\n  booktitle = {NeurIPS 2019},\n  url = {https://arxiv.org/abs/1905.10650},\n}",
    "new_string": "@inproceedings{michel2019sixteen,\n  title = {Are Sixteen Heads Really Better than One?},\n  author = {Paul Michel and Omer Levy and Graham Neubig},\n  year = {2019},\n  booktitle = {NeurIPS 2019},\n  url = {https://arxiv.org/abs/1905.10650},\n}\n\n@inproceedings{dong2019hawq,\n  title = {{HAWQ}: {Hessian} AWare Quantization of Neural Networks with Mixed-Precision},\n  author = {Zhen Dong and Zhewei Yao and Amir Gholami and Michael W. Mahoney and Kurt Keutzer},\n  year = {2019},\n  booktitle = {ICCV 2019},\n  url = {https://arxiv.org/abs/1905.03696},\n}\n\n@inproceedings{dong2020hawqv2,\n  title = {{HAWQ-V2}: {Hessian} Aware trace-Weighted Quantization of Neural Networks},\n  author = {Zhen Dong and Zhewei Yao and Yaohui Cai and Daiyaan Arfeen and Amir Gholami and Michael W. Mahoney and Kurt Keutzer},\n  year = {2020},\n  booktitle = {NeurIPS 2020},\n  url = {https://arxiv.org/abs/1911.03852},\n}\n\n@inproceedings{wang2019haq,\n  title = {{HAQ}: Hardware-Aware Automated Quantization with Mixed Precision},\n  author = {Kuan Wang and Zhijian Liu and Yujun Lin and Ji Lin and Song Han},\n  year = {2019},\n  booktitle = {CVPR 2019},\n  url = {https://arxiv.org/abs/1811.08886},\n}\n\n@inproceedings{su2025rotatekv,\n  title = {{RotateKV}: Accurate and Robust 2-Bit {KV} Cache Quantization for {LLMs} via Outlier-Aware Adaptive Rotations},\n  author = {Zunhai Su and Zhe Chen and Wang Shen and Hanyu Wei and Linge Li and Huangqi Yu and Kehong Yuan},\n  year = {2025},\n  booktitle = {IJCAI 2025},\n  url = {https://arxiv.org/abs/2501.16383},\n}\n\n@inproceedings{sharma2025minikv,\n  title = {{MiniKV}: Pushing the Limits of 2-Bit {KV} Cache via Compression and System Co-Design for Efficient Long Context Inference},\n  author = {Akshat Sharma and Hangliang Ding and Jianping Li and Neel Dani and Minjia Zhang},\n  year = {2025},\n  booktitle = {Findings of ACL 2025},\n  url = {https://arxiv.org/abs/2411.18077},\n}\n\n@inproceedings{shutova2025aquakv,\n  title = {Cache Me If You Must: Adaptive Key-Value Quantization for Large Language Models},\n  author = {Alina Shutova and Vladimir Malinovskii and Vage Egiazarian and Denis Kuznedelev and Denis Mazur and Nikita Surkov and Ivan Ermakov and Dan Alistarh},\n  year = {2025},\n  booktitle = {ICML 2025},\n  url = {https://arxiv.org/abs/2501.19392},\n}\n\n@misc{liu2025pmkvq,\n  title = {{PM-KVQ}: Progressive Mixed-precision {KV} Cache Quantization for Long-CoT {LLMs}},\n  author = {Tengxuan Liu and Shiyao Li and Jiayi Yang and Tianchen Zhao and Feng Zhou and Xiaohui Song and Guohao Dai and Shengen Yan and Huazhong Yang and Yu Wang},\n  year = {2025},\n  note = {arXiv preprint},\n  url = {https://arxiv.org/abs/2505.18610},\n  eprint = {2505.18610},\n  archivePrefix = {arXiv},\n}\n\n@misc{xia2025kitty,\n  title = {{Kitty}: Accurate and Efficient 2-bit {KV} Cache Quantization with Dynamic Channel-wise Precision Boost},\n  author = {Haojun Xia and Xiaoxia Wu and Jisen Li and Robert Wu and Junxiong Wang and Jue Wang and Chenxi Li and Aman Singhal and Alay Dilipbhai Shah and Alpay Ariyak and Donglin Zhuang and Zhongzhu Zhou and Ben Athiwaratkun and Zhen Zheng and Shuaiwen Leon Song},\n  year = {2025},\n  note = {arXiv preprint},\n  url = {https://arxiv.org/abs/2511.18643},\n  eprint = {2511.18643},\n  archivePrefix = {arXiv},\n}"
  }
}
```

</details>

---

### Tool result

_source line 41 · 2026-05-15T04:46:25.557660+00:00_

The file /home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/docs/paper/references.bib has been updated successfully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_writing_r1_w7_related_work_20260515T044227",
  "tool": "Edit",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 42 · 2026-05-15T04:46:25.557816+00:00_

called Edit

<details open><summary>🔧 Tool call — Edit</summary>

```json
{
  "replace_all": "False",
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/docs/paper/related_work.tex",
  "old_string": "\\paragraph{KV Cache Quantization.}\nUniform-precision methods quantize the KV cache at a single bit-width across all heads, using techniques such as asymmetric per-channel/per-token schemes~\\cite{liu2024kivi,hooper2024kvquant}, quantization--serving co-design~\\cite{lin2024qserve}, salient-token identification~\\cite{he2024zipcache}, low-rank plus sparse correction~\\cite{kang2024gear}, and sliding-window adaptation~\\cite{duanmu2024skvq}.\nWe extend the design space to per-head non-uniform allocation over hardware-aligned bit-widths $\\{2,4,8,16\\}$.",
  "new_string": "\\paragraph{KV Cache Quantization.}\nUniform-precision methods quantize the KV cache at a single bit-width across all heads, using techniques such as asymmetric per-channel/per-token schemes~\\cite{liu2024kivi,hooper2024kvquant}, quantization--serving co-design~\\cite{lin2024qserve}, salient-token identification~\\cite{he2024zipcache}, low-rank plus sparse correction~\\cite{kang2024gear}, sliding-window adaptation~\\cite{duanmu2024skvq}, rotation-based outlier smoothing for robust 2-bit~\\cite{su2025rotatekv}, 2-bit with adaptive token retention~\\cite{sharma2025minikv}, and adapter-based inter-layer prediction at 2--2.5 bits~\\cite{shutova2025aquakv}.\nWe extend the design space to per-head non-uniform allocation over hardware-aligned bit-widths $\\{2,4,8,16\\}$."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_writing_r1_w7_related_work_20260515T044227",
  "tool": "Edit",
  "tool_args": {
    "replace_all": "False",
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/docs/paper/related_work.tex",
    "old_string": "\\paragraph{KV Cache Quantization.}\nUniform-precision methods quantize the KV cache at a single bit-width across all heads, using techniques such as asymmetric per-channel/per-token schemes~\\cite{liu2024kivi,hooper2024kvquant}, quantization--serving co-design~\\cite{lin2024qserve}, salient-token identification~\\cite{he2024zipcache}, low-rank plus sparse correction~\\cite{kang2024gear}, and sliding-window adaptation~\\cite{duanmu2024skvq}.\nWe extend the design space to per-head non-uniform allocation over hardware-aligned bit-widths $\\{2,4,8,16\\}$.",
    "new_string": "\\paragraph{KV Cache Quantization.}\nUniform-precision methods quantize the KV cache at a single bit-width across all heads, using techniques such as asymmetric per-channel/per-token schemes~\\cite{liu2024kivi,hooper2024kvquant}, quantization--serving co-design~\\cite{lin2024qserve}, salient-token identification~\\cite{he2024zipcache}, low-rank plus sparse correction~\\cite{kang2024gear}, sliding-window adaptation~\\cite{duanmu2024skvq}, rotation-based outlier smoothing for robust 2-bit~\\cite{su2025rotatekv}, 2-bit with adaptive token retention~\\cite{sharma2025minikv}, and adapter-based inter-layer prediction at 2--2.5 bits~\\cite{shutova2025aquakv}.\nWe extend the design space to per-head non-uniform allocation over hardware-aligned bit-widths $\\{2,4,8,16\\}$."
  }
}
```

</details>

---

### Tool result

_source line 43 · 2026-05-15T04:46:25.557969+00:00_

The file /home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/docs/paper/related_work.tex has been updated successfully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_writing_r1_w7_related_work_20260515T044227",
  "tool": "Edit",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 44 · 2026-05-15T04:46:25.558098+00:00_

called Edit

<details open><summary>🔧 Tool call — Edit</summary>

```json
{
  "replace_all": "False",
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/docs/paper/related_work.tex",
  "old_string": "\\paragraph{Mixed-Precision Rate-Distortion Allocation.}\nRateQuant~\\cite{zuo2026ratequant} formulates per-head bit-width selection as an MCKP and proves greedy optimality for consecutive bit-widths $\\{2,\\ldots,6\\}$ via the polymatroid structure.\nOn hardware-aligned $\\{2,4,8,16\\}$, this structure breaks; we show that unconstrained solvers fail catastrophically due to 2-bit distortion compounding, a failure mode absent in RateQuant's setting.\nRelated mixed-precision work operates at coarser granularity---layer-level via gradient-based sensitivity~\\cite{li2025kvmix} or Pareto search over hardware-friendly precision pairs~\\cite{li2025kvtuner}, memory-budget-level~\\cite{lei2026arkv}---at the weight level~\\cite{kim2024squeezellm}, or dynamically at inference time~\\cite{zhang2025mixkvq}; our allocation is static and per-head.",
  "new_string": "\\paragraph{Mixed-Precision Quantization (Weights).}\nMixed-precision allocation has a long history at the weight level.\nHAWQ~\\cite{dong2019hawq} and HAWQ-V2~\\cite{dong2020hawqv2} use second-order (Hessian-based) sensitivity to assign per-layer bit-widths, with V2 introducing block-wise trace-weighted scoring and Pareto-frontier selection; HAQ~\\cite{wang2019haq} learns an allocation by reinforcement learning under hardware-aware latency/energy constraints.\nThese methods establish that non-uniform bit-width allocation is effective when per-component sensitivity is heterogeneous; we transfer this insight from weights to the KV cache at per-head granularity, where heterogeneity is empirically much larger (\\S\\ref{sec:heterogeneity}).\n\n\\paragraph{Mixed-Precision Rate-Distortion Allocation.}\nRateQuant~\\cite{zuo2026ratequant} formulates per-head bit-width selection as an MCKP and proves greedy optimality for consecutive bit-widths $\\{2,\\ldots,6\\}$ via the polymatroid structure, which relies on the assumption that per-head distortions decompose additively into the global objective---valid when adjacent bit-widths differ by a single bit so that quantization noise stays in the small-perturbation regime.\nOn hardware-aligned $\\{2,4,8,16\\}$, the 4$\\times$ gap between 2-bit and 4-bit drives 2-bit distortion to compound super-additively, breaking the polymatroid structure and the additivity assumption with it.\nConcretely, running RateQuant's greedy algorithm (Algorithm~1) directly on $\\{2,4,8,16\\}$ yields 32.45 PPL on Qwen2.5-7B at $4\\times$ compression---catastrophically worse than uniform 4-bit (15.45)---whereas our cardinality constraint on simultaneously active 2-bit heads recovers 11.23 PPL at the same average bit-width (Table~\\ref{tab:solver_equiv}).\nThe constraint is the minimal fix that restores the additive regime in which RateQuant's polymatroid argument applies.\nRelated mixed-precision KV-cache work operates at coarser granularity---layer-level via gradient-based sensitivity~\\cite{li2025kvmix} or Pareto search over hardware-friendly precision pairs~\\cite{li2025kvtuner}, block-level via progressive decoding-step quantization for long-CoT reasoning~\\cite{liu2025pmkvq}, channel-level via dynamic precision boost on sensitive Key channels~\\cite{xia2025kitty}, memory-budget-level~\\cite{lei2026arkv}---at the weight level~\\cite{kim2024squeezellm}, or dynamically at inference time~\\cite{zhang2025mixkvq}; our allocation is static and per-head."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_writing_r1_w7_related_work_20260515T044227",
  "tool": "Edit",
  "tool_args": {
    "replace_all": "False",
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/docs/paper/related_work.tex",
    "old_string": "\\paragraph{Mixed-Precision Rate-Distortion Allocation.}\nRateQuant~\\cite{zuo2026ratequant} formulates per-head bit-width selection as an MCKP and proves greedy optimality for consecutive bit-widths $\\{2,\\ldots,6\\}$ via the polymatroid structure.\nOn hardware-aligned $\\{2,4,8,16\\}$, this structure breaks; we show that unconstrained solvers fail catastrophically due to 2-bit distortion compounding, a failure mode absent in RateQuant's setting.\nRelated mixed-precision work operates at coarser granularity---layer-level via gradient-based sensitivity~\\cite{li2025kvmix} or Pareto search over hardware-friendly precision pairs~\\cite{li2025kvtuner}, memory-budget-level~\\cite{lei2026arkv}---at the weight level~\\cite{kim2024squeezellm}, or dynamically at inference time~\\cite{zhang2025mixkvq}; our allocation is static and per-head.",
    "new_string": "\\paragraph{Mixed-Precision Quantization (Weights).}\nMixed-precision allocation has a long history at the weight level.\nHAWQ~\\cite{dong2019hawq} and HAWQ-V2~\\cite{dong2020hawqv2} use second-order (Hessian-based) sensitivity to assign per-layer bit-widths, with V2 introducing block-wise trace-weighted scoring and Pareto-frontier selection; HAQ~\\cite{wang2019haq} learns an allocation by reinforcement learning under hardware-aware latency/energy constraints.\nThese methods establish that non-uniform bit-width allocation is effective when per-component sensitivity is heterogeneous; we transfer this insight from weights to the KV cache at per-head granularity, where heterogeneity is empirically much larger (\\S\\ref{sec:heterogeneity}).\n\n\\paragraph{Mixed-Precision Rate-Distortion Allocation.}\nRateQuant~\\cite{zuo2026ratequant} formulates per-head bit-width selection as an MCKP and proves greedy optimality for consecutive bit-widths $\\{2,\\ldots,6\\}$ via the polymatroid structure, which relies on the assumption that per-head distortions decompose additively into the global objective---valid when adjacent bit-widths differ by a single bit so that quantization noise stays in the small-perturbation regime.\nOn hardware-aligned $\\{2,4,8,16\\}$, the 4$\\times$ gap between 2-bit and 4-bit drives 2-bit distortion to compound super-additively, breaking the polymatroid structure and the additivity assumption with it.\nConcretely, running RateQuant's greedy algorithm (Algorithm~1) directly on $\\{2,4,8,16\\}$ yields 32.45 PPL on Qwen2.5-7B at $4\\times$ compression---catastrophically worse than uniform 4-bit (15.45)---whereas our cardinality constraint on simultaneously active 2-bit heads recovers 11.23 PPL at the same average bit-width (Table~\\ref{tab:solver_equiv}).\nThe constraint is the minimal fix that restores the additive regime in which RateQuant's polymatroid argument applies.\nRelated mixed-precision KV-cache work operates at coarser granularity---layer-level via gradient-based sensitivity~\\cite{li2025kvmix} or Pareto search over hardware-friendly precision pairs~\\cite{li2025kvtuner}, block-level via progressive decoding-step quantization for long-CoT reasoning~\\cite{liu2025pmkvq}, channel-level via dynamic precision boost on sensitive Key channels~\\cite{xia2025kitty}, memory-budget-level~\\cite{lei2026arkv}---at the weight level~\\cite{kim2024squeezellm}, or dynamically at inference time~\\cite{zhang2025mixkvq}; our allocation is static and per-head."
  }
}
```

</details>

---

### Tool result

_source line 45 · 2026-05-15T04:46:25.558278+00:00_

The file /home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/docs/paper/related_work.tex has been updated successfully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_writing_r1_w7_related_work_20260515T044227",
  "tool": "Edit",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 46 · 2026-05-15T04:46:25.558412+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/docs/paper/related_work.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_writing_r1_w7_related_work_20260515T044227",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/docs/paper/related_work.tex"
  }
}
```

</details>

---

### Tool result

_source line 47 · 2026-05-15T04:46:25.558558+00:00_

1	\section{Related Work}\label{sec:related_work}
2	
3	\paragraph{KV Cache Quantization.}
4	Uniform-precision methods quantize the KV cache at a single bit-width across all heads, using techniques such as asymmetric per-channel/per-token schemes~\cite{liu2024kivi,hooper2024kvquant}, quantization--serving co-design~\cite{lin2024qserve}, salient-token identification~\cite{he2024zipcache}, low-rank plus sparse correction~\cite{kang2024gear}, sliding-window adaptation~\cite{duanmu2024skvq}, rotation-based outlier smoothing for robust 2-bit~\cite{su2025rotatekv}, 2-bit with adaptive token retention~\cite{sharma2025minikv}, and adapter-based inter-layer prediction at 2--2.5 bits~\cite{shutova2025aquakv}.
5	We extend the design space to per-head non-uniform allocation over hardware-aligned bit-widths $\{2,4,8,16\}$.
6	
7	\paragraph{KV Cache Eviction.}
8	Complementary to quantization, eviction methods reduce cache size by discarding tokens---retaining heavy-hitters~\cite{zhang2023h2o}, per-head important tokens~\cite{li2024snapkv,ge2024fastgen}, persistent-importance tokens~\cite{liu2024scissorhands}, attention sinks~\cite{xiao2024streamingllm}, or progressively fewer tokens in deeper layers~\cite{yang2024pyramidinfer}.
9	Recent per-head eviction methods allocate non-uniform budgets across heads based on retrieval-vs-reasoning importance~\cite{fu2025headkv} or adaptive optimization extending SnapKV/PyramidKV~\cite{feng2025adakv}, confirming that head-level heterogeneity is exploitable for eviction; our work shows it is equally exploitable for quantization.
10	
11	
12	\paragraph{Mixed-Precision Quantization (Weights).}
13	Mixed-precision allocation has a long history at the weight level.
14	HAWQ~\cite{dong2019hawq} and HAWQ-V2~\cite{dong2020hawqv2} use second-order (Hessian-based) sensitivity to assign per-layer bit-widths, with V2 introducing block-wise trace-weighted scoring and Pareto-frontier selection; HAQ~\cite{wang2019haq} learns an allocation by reinforcement learning
…[truncated 2533 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_writing_r1_w7_related_work_20260515T044227",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 48 · 2026-05-15T04:46:25.558734+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/docs/paper && latexmk -pdf -interaction=nonstopmode -halt-on-error main.tex 2>&1 | tail -40",
  "description": "Compile paper to check for errors"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_writing_r1_w7_related_work_20260515T044227",
  "tool": "Bash",
  "tool_args": {
    "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/docs/paper && latexmk -pdf -interaction=nonstopmode -halt-on-error main.tex 2>&1 | tail -40",
    "description": "Compile paper to check for errors"
  }
}
```

</details>

---

### Tool result

_source line 49 · 2026-05-15T04:46:25.558885+00:00_

 [][] 
)
Underfull \hbox (badness 1286) in paragraph at lines 78--32
\OT1/ptm/m/it/10.95 not \OT1/ptm/m/n/10.95 rep-re-sent op-ti-mized CUDA ker-nel
 per-for-
[13] [14] (./main.aux) )
(see the transcript file for additional information)&lt;/usr/share/texlive/texmf-d
ist/fonts/type1/public/amsfonts/cm/cmex10.pfb>&lt;/usr/share/texlive/texmf-dist/fo
nts/type1/public/amsfonts/cm/cmmi10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/ty
pe1/public/amsfonts/cm/cmmi6.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/pub
lic/amsfonts/cm/cmmi8.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/ams
fonts/cm/cmmi9.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/c
m/cmr10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr6.
pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr7.pfb>&lt;/us
r/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr8.pfb>&lt;/usr/share/
texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr9.pfb>&lt;/usr/share/texlive/
texmf-dist/fonts/type1/public/amsfonts/cm/cmsy10.pfb>&lt;/usr/share/texlive/texmf-
dist/fonts/type1/public/amsfonts/cm/cmsy6.pfb>&lt;/usr/share/texlive/texmf-dist/fo
nts/type1/public/amsfonts/cm/cmsy7.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/typ
e1/public/amsfonts/cm/cmsy8.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/publ
ic/amsfonts/cm/cmsy9.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsf
onts/symbols/msam10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfo
nts/symbols/msbm10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/urw/courier/u
crr8a.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/urw/helvetic/uhvb8a.pfb>&lt;/
usr/share/texlive/texmf-dist/fonts/type1/urw/times/utmb8a.pfb>&lt;/usr/share/texli
ve/texmf-dist/fonts/type1/urw/times/utmr8a.pfb>&lt;/usr/share/texlive/texmf-dist/f
onts/type1/urw/times/utmri8a.pfb>
Output written on main.pdf (14 pages, 385111 bytes).
Transcript written on main.log.
Latexmk: Getting log file 'main.log'
Latexmk: Examining 'main.fls'
Latexmk: Examining 'main.log'

…[truncated 282 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_writing_r1_w7_related_work_20260515T044227",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 50 · 2026-05-15T04:46:25.559029+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "grep -i \"warning\\|error\\|undefined\" main.log | grep -iE \"citation|undefined|reference\" | head -20",
  "description": "Check log for undefined citation warnings"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_writing_r1_w7_related_work_20260515T044227",
  "tool": "Bash",
  "tool_args": {
    "command": "grep -i \"warning\\|error\\|undefined\" main.log | grep -iE \"citation|undefined|reference\" | head -20",
    "description": "Check log for undefined citation warnings"
  }
}
```

</details>

---

### Tool result

_source line 51 · 2026-05-15T04:46:25.559149+00:00_

(Bash completed with no output)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_writing_r1_w7_related_work_20260515T044227",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 52 · 2026-05-15T04:46:25.559276+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "Warning|undefined|citation",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/docs/paper/main.log",
  "output_mode": "content",
  "-i": "True",
  "head_limit": "30"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_writing_r1_w7_related_work_20260515T044227",
  "tool": "Grep",
  "tool_args": {
    "pattern": "Warning|undefined|citation",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/docs/paper/main.log",
    "output_mode": "content",
    "-i": "True",
    "head_limit": "30"
  }
}
```

</details>

---

### Tool result

_source line 53 · 2026-05-15T04:46:25.559435+00:00_

150:Package: infwarerr 2019/12/03 v1.5 Providing info/warning/error messages (HO)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_writing_r1_w7_related_work_20260515T044227",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 54 · 2026-05-15T04:46:25.559600+00:00_

Compilation clean: 14-page PDF built, no undefined-citation warnings. Summary of changes:

**`references.bib`** — added 8 verified entries:
- `dong2019hawq` (ICCV 2019), `dong2020hawqv2` (NeurIPS 2020), `wang2019haq` (CVPR 2019)
- `su2025rotatekv` (IJCAI 2025), `sharma2025minikv` (Findings of ACL 2025), `shutova2025aquakv` (ICML 2025, "Cache Me If You Must")
- `liu2025pmkvq` (arXiv preprint), `xia2025kitty` (arXiv preprint)
- Skipped "Don't Waste Bits!" — not verified.

**`related_work.tex`** —
- KV Cache Quantization paragraph: added RotateKV / MiniKV / AQUA-KV at the end of the uniform-precision enumeration.
- New **Mixed-Precision Quantization (Weights)** paragraph: HAWQ / HAWQ-V2 / HAQ, framed as the foundational weight-level mixed-precision lineage, with one transfer sentence to our per-head KV setting.
- Mixed-Precision Rate-Distortion Allocation paragraph: expanded RateQuant differentiation with the concrete additivity argument (single-bit gap → small-perturbation regime → polymatroid), the catastrophic-failure numbers (32.45 vs uniform 15.45 vs constrained 11.23 on Qwen2.5-7B at 4×, referencing `tab:solver_equiv`), and the framing that the cardinality constraint "restores the additive regime in which RateQuant's polymatroid argument applies." Also folded PM-KVQ (block-level) and Kitty (channel-level) into the granularity enumeration.

Sources:
- [HAWQ (ICCV 2019)](https://arxiv.org/abs/1905.03696)
- [HAWQ-V2 (NeurIPS 2020)](https://arxiv.org/abs/1911.03852)
- [HAQ (CVPR 2019)](https://arxiv.org/abs/1811.08886)
- [RotateKV (IJCAI 2025)](https://www.ijcai.org/proceedings/2025/690)
- [MiniKV (Findings of ACL 2025)](https://aclanthology.org/2025.findings-acl.952/)
- [AQUA-KV / Cache Me If You Must (ICML 2025)](https://proceedings.mlr.press/v267/shutova25a.html)
- [PM-KVQ](https://arxiv.org/abs/2505.18610)
- [Kitty](https://arxiv.org/abs/2511.18643)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_writing_r1_w7_related_work_20260515T044227"
}
```

</details>

---
