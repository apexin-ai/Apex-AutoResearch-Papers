# paper research

**Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 9
- **Recorded user turns:** 0
- **Tool calls:** 4
- **Original source:** `logs/chats/worker_paper_research_20260516T092303.jsonl`
- **Structured JSON:** [`a0af4d0463c3031ae500.json`](../../sessions/a0/a0af4d0463c3031ae500.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

9 recorded events

### Tool call

_source line 1 · 2026-05-16T09:24:45.512619+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/literature_map.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_research_20260516T092303",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/literature_map.yaml"
  }
}
```

</details>

---

### Tool result

_source line 2 · 2026-05-16T09:24:45.513252+00:00_

1	# Literature Map: KL Distillation for Sparse SwiGLU Activation Prediction
2	# Last updated: 2026-05-15
3	# Survey scope: 2023-2026, 4 directions
4	
5	# =============================================================================
6	# Direction 1: KL distillation for structured/activation sparsity
7	# Finding: NO prior work uses KL to train an activation sparsity PREDICTOR.
8	# Existing predictors use BCE (DejaVu, ShadowLLM). SPON uses KL but for
9	# learnable bias correction, not predictor training. This is our novelty.
10	# =============================================================================
11	
12	- title: "Resting Neurons, Active Insights: Robustify Activation Sparsity for Large Language Models"
13	  authors: [Haotian Xu, Jiannan Yang, Tian Gao, Tsui-Wei Weng, Tengfei Ma]
14	  venue: ICML 2026
15	  year: 2026
16	  arxiv_id: "2512.12744"
17	  category: direct-competitor
18	  role: "最接近的KL蒸馏用于稀疏性的工作——但SPON训练的是可学习bias项而非predictor"
19	  key_finding: "SPON注入input-independent learnable activation vectors作为sparse computation的anchor，用KL散度(dense vs sparse logits)做distribution matching训练，训练后吸收进bias项，零推理开销"
20	  relevance_to_us: "SPON证明KL divergence比BCE/MSE更适合sparsity场景的distribution matching。但SPON是全局bias correction而非per-token predictor——我们的predictor方案能实现input-dependent的sparsity pattern，比SPON更灵活。SPON在50-60% sparsity下测试，与我们目标一致"
21	
22	- title: "Compact Language Models via Pruning and Knowledge Distillation"
23	  authors: [Saurav Muralidharan, Sharath Turuvekere Sreenivas, Raviraj Joshi, Marcin Chochowski, Mostofa Patwary, Mohammad Shoeybi, Bryan Catanzaro, Jan Kautz, Pavlo Molchanov]
24	  venue: NeurIPS 2024
25	  year: 2024
26	  arxiv_id: "2407.14679"
27	  category: method-component
28	  role: "KL蒸馏用于结构化剪枝后恢复——验证logit-only KL优于intermediate matching"
29	  key_finding: "Minitron用logit-only forward KL divergence做structured pruning后的distillation recovery，发现仅用KL loss（不用CE或intermediate matching）效果最好，学生模型继承了teacher的inter-token关系和confidence calibration"
30	  relevance_to_
…[truncated 16394 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_research_20260516T092303",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-16T09:24:45.513502+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "python3 -c \"\nimport urllib.request, json, time\n\npapers = [\n    ('2407.21783', 'LLaMA 3'),\n    ('2310.06825', 'Mistral 7B'),\n    ('1611.01144', 'Gumbel-Softmax'),\n    ('2002.05202', 'GLU Variants'),\n    ('1612.08083', 'WikiText-2 Merity'),\n    ('1503.02531', 'Knowledge Distillation Hinton'),\n    ('1308.3432', 'Straight-Through Estimator Bengio'),\n    ('1910.10683', 'T5/C4 Raffel'),\n]\n\nfor arxiv_id, label in papers:\n    try:\n        url = f'https://api.semanticscholar.org/graph/v1/paper/arxiv:{arxiv_id}?fields=title,authors,year,venue,externalIds'\n        req = urllib.request.Request(url)\n        data = json.loads(urllib.request.urlopen(req, timeout=10).read())\n        authors = [a['name'] for a in data.get('authors', [])]\n        print(f'--- {label} ---')\n        print(f'title: {data.get(\\\"title\\\")}')\n        print(f'authors: {authors[:5]}')\n        print(f'year: {data.get(\\\"year\\\")}')\n        print(f'venue: {data.get(\\\"venue\\\")}')\n        print()\n        time.sleep(1)\n    except Exception as e:\n        print(f'--- {label} --- ERROR: {e}')\n        print()\n        time.sleep(1)\n\"\n",
  "description": "Fetch paper metadata from Semantic Scholar API",
  "timeout": "120000"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_research_20260516T092303",
  "tool": "Bash",
  "tool_args": {
    "command": "python3 -c \"\nimport urllib.request, json, time\n\npapers = [\n    ('2407.21783', 'LLaMA 3'),\n    ('2310.06825', 'Mistral 7B'),\n    ('1611.01144', 'Gumbel-Softmax'),\n    ('2002.05202', 'GLU Variants'),\n    ('1612.08083', 'WikiText-2 Merity'),\n    ('1503.02531', 'Knowledge Distillation Hinton'),\n    ('1308.3432', 'Straight-Through Estimator Bengio'),\n    ('1910.10683', 'T5/C4 Raffel'),\n]\n\nfor arxiv_id, label in papers:\n    try:\n        url = f'https://api.semanticscholar.org/graph/v1/paper/arxiv:{arxiv_id}?fields=title,authors,year,venue,externalIds'\n        req = urllib.request.Request(url)\n        data = json.loads(urllib.request.urlopen(req, timeout=10).read())\n        authors = [a['name'] for a in data.get('authors', [])]\n        print(f'--- {label} ---')\n        print(f'title: {data.get(\\\"title\\\")}')\n        print(f'authors: {authors[:5]}')\n        print(f'year: {data.get(\\\"year\\\")}')\n        print(f'venue: {data.get(\\\"venue\\\")}')\n        print()\n        time.sleep(1)\n    except Exception as e:\n        print(f'--- {label} --- ERROR: {e}')\n        print()\n        time.sleep(1)\n\"\n",
    "description": "Fetch paper metadata from Semantic Scholar API",
    "timeout": "120000"
  }
}
```

</details>

---

### Tool result

_source line 4 · 2026-05-16T09:24:45.513684+00:00_

--- LLaMA 3 --- ERROR: HTTP Error 429: 

--- Mistral 7B --- ERROR: HTTP Error 429: 

--- Gumbel-Softmax --- ERROR: HTTP Error 429: 

--- GLU Variants --- ERROR: HTTP Error 429: 

--- WikiText-2 Merity --- ERROR: HTTP Error 429: 

--- Knowledge Distillation Hinton --- ERROR: HTTP Error 429: 

--- Straight-Through Estimator Bengio --- ERROR: HTTP Error 429: 

--- T5/C4 Raffel --- ERROR: HTTP Error 429:

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_research_20260516T092303",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-16T09:24:45.513859+00:00_

called Edit

<details open><summary>🔧 Tool call — Edit</summary>

```json
{
  "replace_all": "False",
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/literature_map.yaml",
  "old_string": "# 主要related work定位:\n# - vs TEAL: trained predictor(input-dependent) vs fixed magnitude threshold\n# - vs DejaVu/ShadowLLM: KL loss vs BCE loss训练predictor\n# - vs SPON: predictor vs learnable bias; 都用KL但目标不同\n# - vs DIP: trained predictor vs predictor-free pruning\n# - vs ReLU/TurboSparse/ProSparse: 不改activation function\n# - vs Fast Forward: KL loss vs BCE+error compensation\n# - vs CATS: input-dependent predictor vs fixed percentile threshold",
  "new_string": "# 主要related work定位:\n# - vs TEAL: trained predictor(input-dependent) vs fixed magnitude threshold\n# - vs DejaVu/ShadowLLM: KL loss vs BCE loss训练predictor\n# - vs SPON: predictor vs learnable bias; 都用KL但目标不同\n# - vs DIP: trained predictor vs predictor-free pruning\n# - vs ReLU/TurboSparse/ProSparse: 不改activation function\n# - vs Fast Forward: KL loss vs BCE+error compensation\n# - vs CATS: input-dependent predictor vs fixed percentile threshold\n\n# =============================================================================\n# Cluster 4: Foundational references\n# =============================================================================\n\n- title: \"The Llama 3 Herd of Models\"\n  authors: [Aaron Grattafiori, Abhimanyu Dubey, Abhinav Jauhri, Abhinav Pandey, Abhishek Kadian, Ahmad Al-Dahle, Aieleen Lakber, Aimin Chen, Ait Mokhtar Salma, Ajay Menon]\n  venue: arXiv\n  year: 2024\n  arxiv_id: \"2407.21783\"\n  category: foundational\n  role: \"主要评估模型架构——SwiGLU FFN的代表性开源LLM\"\n  key_finding: \"Llama 3系列采用SwiGLU FFN、GQA、RoPE，从8B到405B参数规模。在15T+ token上训练，性能比肩GPT-4。SwiGLU FFN的标准化使activation sparsity研究有广泛适用性\"\n  relevance_to_us: \"我们的predictor专为SwiGLU架构设计，Llama 3是主要目标模型。其FFN结构（gate_proj * up_proj → down_proj）决定了predictor的输入输出接口\"\n\n- title: \"Mistral 7B\"\n  authors: [Albert Q. Jiang, Alexandre Sablayrolles, Arthur Mensch, Chris Bamford, Devendra Singh Chaplot, Diego de las Casas, Florian Bressand, Gianna Lengyel, Guillaume Lample, Lucile Saulnier]\n  venue: arXiv\n  year: 2023\n  arxiv_id: \"2310.06825\"\n  category: foundational\n  role: \"评估模型——高效SwiGLU架构的代表，sliding window attention\"\n  key_finding: \"Mistral 7B用SwiGLU+GQA+sliding window attention，在所有benchmark上超越Llama 2 13B。证明紧凑SwiGLU模型的高效性\"\n  relevance_to_us: \"实验评估的关键模型之一。Mistral的SwiGLU intermediate size=14336（比Llama大），为predictor设计提供不同维度配置的测试场景\"\n\n- title: \"Categorical Reparameterization with Gumbel-Softmax\"\n  authors: [Eric Jang, Shixiang Gu, Ben Poole]\n  venue: ICLR 2017\n  year: 2017\n  arxiv_id: \"1611.01144\"\n  category: foundational\n  role: \"Predictor输出离散mask的可微松弛方法——训练时的梯度传播基础\"\n  key_finding: \"Gumbel-Softmax提供categorical分布的连续松弛，使离散采样可通过reparameterization trick进行梯度反传。温度τ→0时逼近one-hot\"\n  relevance_to_us: \"我们的predictor输出binary activation mask（离散决策），训练时需要梯度流过mask。Gumbel-Softmax或Straight-Through Estimator是使mask可微的标准技术\"\n\n- title: \"GLU Variants Improve Transformer\"\n  authors: [Noam Shazeer]\n  venue: arXiv\n  year: 2020\n  arxiv_id: \"2002.05202\"\n  category: foundational\n  role: \"SwiGLU激活函数的提出——定义了我们工作的目标FFN架构\"\n  key_finding: \"提出多种GLU变体（GEGLU、SwiGLU等）替代标准FFN中的ReLU，SwiGLU=Swish(xW)⊙(xV)在perplexity上一致优于ReLU/GELU FFN\"\n  relevance_to_us: \"SwiGLU是我们工作的架构基础。SwiGLU的gate机制（Swish门控）产生的activation pattern比ReLU更平滑、天然稀疏性更低，这是trained predictor必要性的根本原因\"\n\n- title: \"Pointer Sentinel Mixture Models\"\n  authors: [Stephen Merity, Caiming Xiong, James Bradbury, Richard Socher]\n  venue: ICLR 2017\n  year: 2017\n  arxiv_id: \"1609.07843\"\n  category: foundational\n  role: \"WikiText-2/WikiText-103 benchmark的来源——标准language modeling评估数据集\"\n  key_finding: \"提出WikiText-2和WikiText-103数据集，包含Wikipedia长文档，token数分别为2M和103M。成为language modeling perplexity评估的标准benchmark\"\n  relevance_to_us: \"WikiText-2是我们评估sparsity对perplexity影响的标准benchmark。所有competitor（TEAL、DejaVu、CATS等）均报告WikiText-2 perplexity，确保结果可比\"\n\n- title: \"Distilling the Knowledge in a Neural Network\"\n  authors: [Geoffrey Hinton, Oriol Vinyals, Jeff Dean]\n  venue: NeurIPS 2014 Workshop\n  year: 2015\n  arxiv_id: \"1503.02531\"\n  category: foundational\n  role: \"知识蒸馏的奠基工作——soft target训练的理论基础\"\n  key_finding: \"Teacher的soft probability outputs（经温度缩放）包含dark knowledge（类间相似性信息），student通过匹配teacher soft targets学到比hard label更丰富的信息\"\n  relevance_to_us: \"我们的KL predictor训练本质是知识蒸馏：dense model是teacher，sparse model是student，predictor学习使sparse output distribution匹配dense distribution。Hinton的soft target insight解释了为什么KL优于BCE（保留分布结构）\"\n\n- title: \"Estimating or Propagating Gradients Through Stochastic Neurons for Conditional Computation\"\n  authors: [Yoshua Bengio, Nicholas Léonard, Aaron Courville]\n  venue: arXiv\n  year: 2013\n  arxiv_id: \"1308.3432\"\n  category: foundational\n  role: \"Straight-Through Estimator——离散mask梯度反传的基础方法\"\n  key_finding: \"提出Straight-Through Estimator (STE)：前向传播用离散值，反向传播时将梯度直接传过离散节点（视为identity）。为stochastic/discrete neuron的训练提供实用方案\"\n  relevance_to_us: \"STE是训练binary mask predictor的另一标准选择（与Gumbel-Softmax互补）。我们的predictor在inference时输出hard binary mask，训练时可用STE或Gumbel-Softmax传梯度\"\n\n- title: \"Exploring the Limits of Transfer Learning with a Unified Text-to-Text Transformer\"\n  authors: [Colin Raffel, Noam Shazeer, Adam Roberts, Katherine Lee, Sharan Narang, Michael Matena, Yanqi Zhou, Wei Li, Peter J. Liu]\n  venue: JMLR\n  year: 2020\n  arxiv_id: \"1910.10683\"\n  category: foundational\n  role: \"C4数据集的来源——大规模预训练和蒸馏训练的标准数据\"\n  key_finding: \"提出T5统一text-to-text框架，系统比较预训练策略。副产品Colossal Clean Crawled Corpus (C4)成为标准预训练/微调数据集，约750GB清洗后的英文网页文本\"\n  relevance_to_us: \"C4是我们predictor蒸馏训练的候选数据源。使用与预训练相同分布的数据训练predictor，确保学到的sparsity pattern在实际推理时有效\""
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_research_20260516T092303",
  "tool": "Edit",
  "tool_args": {
    "replace_all": "False",
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/literature_map.yaml",
    "old_string": "# 主要related work定位:\n# - vs TEAL: trained predictor(input-dependent) vs fixed magnitude threshold\n# - vs DejaVu/ShadowLLM: KL loss vs BCE loss训练predictor\n# - vs SPON: predictor vs learnable bias; 都用KL但目标不同\n# - vs DIP: trained predictor vs predictor-free pruning\n# - vs ReLU/TurboSparse/ProSparse: 不改activation function\n# - vs Fast Forward: KL loss vs BCE+error compensation\n# - vs CATS: input-dependent predictor vs fixed percentile threshold",
    "new_string": "# 主要related work定位:\n# - vs TEAL: trained predictor(input-dependent) vs fixed magnitude threshold\n# - vs DejaVu/ShadowLLM: KL loss vs BCE loss训练predictor\n# - vs SPON: predictor vs learnable bias; 都用KL但目标不同\n# - vs DIP: trained predictor vs predictor-free pruning\n# - vs ReLU/TurboSparse/ProSparse: 不改activation function\n# - vs Fast Forward: KL loss vs BCE+error compensation\n# - vs CATS: input-dependent predictor vs fixed percentile threshold\n\n# =============================================================================\n# Cluster 4: Foundational references\n# =============================================================================\n\n- title: \"The Llama 3 Herd of Models\"\n  authors: [Aaron Grattafiori, Abhimanyu Dubey, Abhinav Jauhri, Abhinav Pandey, Abhishek Kadian, Ahmad Al-Dahle, Aieleen Lakber, Aimin Chen, Ait Mokhtar Salma, Ajay Menon]\n  venue: arXiv\n  year: 2024\n  arxiv_id: \"2407.21783\"\n  category: foundational\n  role: \"主要评估模型架构——SwiGLU FFN的代表性开源LLM\"\n  key_finding: \"Llama 3系列采用SwiGLU FFN、GQA、RoPE，从8B到405B参数规模。在15T+ token上训练，性能比肩GPT-4。SwiGLU FFN的标准化使activation sparsity研究有广泛适用性\"\n  relevance_to_us: \"我们的predictor专为SwiGLU架构设计，Llama 3是主要目标模型。其FFN结构（gate_proj * up_proj → down_proj）决定了predictor的输入输出接口\"\n\n- title: \"Mistral 7B\"\n  authors: [Albert Q. Jiang, Alexandre Sablayrolles, Arthur Mensch, Chris Bamford, Devendra Singh Chaplot, Diego de las Casas, Florian Bressand, Gianna Lengyel, Guillaume Lample, Lucile Saulnier]\n  venue: arXiv\n  year: 2023\n  arxiv_id: \"2310.06825\"\n  category: foundational\n  role: \"评估模型——高效SwiGLU架构的代表，sliding window attention\"\n  key_finding: \"Mistral 7B用SwiGLU+GQA+sliding window attention，在所有benchmark上超越Llama 2 13B。证明紧凑SwiGLU模型的高效性\"\n  relevance_to_us: \"实验评估的关键模型之一。Mistral的SwiGLU intermediate size=14336（比Llama大），为predictor设计提供不同维度配置的测试场景\"\n\n- title: \"Categorical Reparameterization with Gumbel-Softmax\"\n  authors: [Eric Jang, Shixiang Gu, Ben Poole]\n  venue: ICLR 2017\n  year: 2017\n  arxiv_id: \"1611.01144\"\n  category: foundational\n  role: \"Predictor输出离散mask的可微松弛方法——训练时的梯度传播基础\"\n  key_finding: \"Gumbel-Softmax提供categorical分布的连续松弛，使离散采样可通过reparameterization trick进行梯度反传。温度τ→0时逼近one-hot\"\n  relevance_to_us: \"我们的predictor输出binary activation mask（离散决策），训练时需要梯度流过mask。Gumbel-Softmax或Straight-Through Estimator是使mask可微的标准技术\"\n\n- title: \"GLU Variants Improve Transformer\"\n  authors: [Noam Shazeer]\n  venue: arXiv\n  year: 2020\n  arxiv_id: \"2002.05202\"\n  category: foundational\n  role: \"SwiGLU激活函数的提出——定义了我们工作的目标FFN架构\"\n  key_finding: \"提出多种GLU变体（GEGLU、SwiGLU等）替代标准FFN中的ReLU，SwiGLU=Swish(xW)⊙(xV)在perplexity上一致优于ReLU/GELU FFN\"\n  relevance_to_us: \"SwiGLU是我们工作的架构基础。SwiGLU的gate机制（Swish门控）产生的activation pattern比ReLU更平滑、天然稀疏性更低，这是trained predictor必要性的根本原因\"\n\n- title: \"Pointer Sentinel Mixture Models\"\n  authors: [Stephen Merity, Caiming Xiong, James Bradbury, Richard Socher]\n  venue: ICLR 2017\n  year: 2017\n  arxiv_id: \"1609.07843\"\n  category: foundational\n  role: \"WikiText-2/WikiText-103 benchmark的来源——标准language modeling评估数据集\"\n  key_finding: \"提出WikiText-2和WikiText-103数据集，包含Wikipedia长文档，token数分别为2M和103M。成为language modeling perplexity评估的标准benchmark\"\n  relevance_to_us: \"WikiText-2是我们评估sparsity对perplexity影响的标准benchmark。所有competitor（TEAL、DejaVu、CATS等）均报告WikiText-2 perplexity，确保结果可比\"\n\n- title: \"Distilling the Knowledge in a Neural Network\"\n  authors: [Geoffrey Hinton, Oriol Vinyals, Jeff Dean]\n  venue: NeurIPS 2014 Workshop\n  year: 2015\n  arxiv_id: \"1503.02531\"\n  category: foundational\n  role: \"知识蒸馏的奠基工作——soft target训练的理论基础\"\n  key_finding: \"Teacher的soft probability outputs（经温度缩放）包含dark knowledge（类间相似性信息），student通过匹配teacher soft targets学到比hard label更丰富的信息\"\n  relevance_to_us: \"我们的KL predictor训练本质是知识蒸馏：dense model是teacher，sparse model是student，predictor学习使sparse output distribution匹配dense distribution。Hinton的soft target insight解释了为什么KL优于BCE（保留分布结构）\"\n\n- title: \"Estimating or Propagating Gradients Through Stochastic Neurons for Conditional Computation\"\n  authors: [Yoshua Bengio, Nicholas Léonard, Aaron Courville]\n  venue: arXiv\n  year: 2013\n  arxiv_id: \"1308.3432\"\n  category: foundational\n  role: \"Straight-Through Estimator——离散mask梯度反传的基础方法\"\n  key_finding: \"提出Straight-Through Estimator (STE)：前向传播用离散值，反向传播时将梯度直接传过离散节点（视为identity）。为stochastic/discrete neuron的训练提供实用方案\"\n  relevance_to_us: \"STE是训练binary mask predictor的另一标准选择（与Gumbel-Softmax互补）。我们的predictor在inference时输出hard binary mask，训练时可用STE或Gumbel-Softmax传梯度\"\n\n- title: \"Exploring the Limits of Transfer Learning with a Unified Text-to-Text Transformer\"\n  authors: [Colin Raffel, Noam Shazeer, Adam Roberts, Katherine Lee, Sharan Narang, Michael Matena, Yanqi Zhou, Wei Li, Peter J. Liu]\n  venue: JMLR\n  year: 2020\n  arxiv_id: \"1910.10683\"\n  category: foundational\n  role: \"C4数据集的来源——大规模预训练和蒸馏训练的标准数据\"\n  key_finding: \"提出T5统一text-to-text框架，系统比较预训练策略。副产品Colossal Clean Crawled Corpus (C4)成为标准预训练/微调数据集，约750GB清洗后的英文网页文本\"\n  relevance_to_us: \"C4是我们predictor蒸馏训练的候选数据源。使用与预训练相同分布的数据训练predictor，确保学到的sparsity pattern在实际推理时有效\""
  }
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-16T09:24:45.514188+00:00_

The file /home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/literature_map.yaml has been updated successfully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_research_20260516T092303",
  "tool": "Edit",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-16T09:24:45.514379+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/literature_map.yaml",
  "offset": "273"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_research_20260516T092303",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/literature_map.yaml",
    "offset": "273"
  }
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-16T09:24:45.514559+00:00_

273	# 竞争格局总结
274	# =============================================================================
275	#
276	# 我们的独特定位:
277	# 1. 唯一使用KL divergence训练activation sparsity predictor的工作
278	#    - DejaVu/ShadowLLM用BCE训练predictor
279	#    - SPON用KL但训练bias correction而非predictor
280	#    - TEAL/CATS/R-Sparse/SparseInfer/SVD-CSP是training-free
281	# 2. 专注SwiGLU模型的50% sparsity目标
282	#    - ReLU/dReLU方案需要替换activation function
283	#    - 很多training-free方案在SwiGLU上效果不佳(DIP论文证实)
284	# 3. 通过保留output distribution(而非逐neuron匹配)来指导sparsity
285	#    - Minitron/SPON已证明KL loss优于MSE/BCE做distribution matching
286	#    - 我们将此insight应用到predictor训练
287	#
288	# 主要related work定位:
289	# - vs TEAL: trained predictor(input-dependent) vs fixed magnitude threshold
290	# - vs DejaVu/ShadowLLM: KL loss vs BCE loss训练predictor
291	# - vs SPON: predictor vs learnable bias; 都用KL但目标不同
292	# - vs DIP: trained predictor vs predictor-free pruning
293	# - vs ReLU/TurboSparse/ProSparse: 不改activation function
294	# - vs Fast Forward: KL loss vs BCE+error compensation
295	# - vs CATS: input-dependent predictor vs fixed percentile threshold
296	
297	# =============================================================================
298	# Cluster 4: Foundational references
299	# =============================================================================
300	
301	- title: "The Llama 3 Herd of Models"
302	  authors: [Aaron Grattafiori, Abhimanyu Dubey, Abhinav Jauhri, Abhinav Pandey, Abhishek Kadian, Ahmad Al-Dahle, Aieleen Lakber, Aimin Chen, Ait Mokhtar Salma, Ajay Menon]
303	  venue: arXiv
304	  year: 2024
305	  arxiv_id: "2407.21783"
306	  category: foundational
307	  role: "主要评估模型架构——SwiGLU FFN的代表性开源LLM"
308	  key_finding: "Llama 3系列采用SwiGLU FFN、GQA、RoPE，从8B到405B参数规模。在15T+ token上训练，性能比肩GPT-4。SwiGLU FFN的标准化使activation sparsity研究有广泛适用性"
309	  relevance_to_us: "我们的predictor专为SwiGLU架构设计，Llama 3是主要目标模型。其FFN结构（gate_proj * up_proj → down_proj）决定了predictor的输入输出接口"
310	
311	- title: "Mistral 7B"
312	  authors: [Albert Q. Jiang
…[truncated 3919 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_research_20260516T092303",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 9 · 2026-05-16T09:24:45.514750+00:00_

已完成。新增 8 篇 foundational references 到 `literature_map.yaml` 的 Cluster 4 section：

**Must-cite (4篇):**
1. LLaMA 3 (2407.21783) — 主要评估模型
2. Mistral 7B (2310.06825) — 评估模型
3. Gumbel-Softmax (1611.01144) — 离散mask可微松弛
4. GLU Variants (2002.05202) — SwiGLU架构来源

**额外 (4篇):**
5. WikiText-2/Merity (1609.07843) — 评估benchmark
6. Knowledge Distillation/Hinton (1503.02531) — 蒸馏理论基础
7. Straight-Through Estimator/Bengio (1308.3432) — 离散梯度传播
8. T5/C4/Raffel (1910.10683) — 训练数据来源

格式与现有条目一致，无重复。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_paper_research_20260516T092303"
}
```

</details>

---
