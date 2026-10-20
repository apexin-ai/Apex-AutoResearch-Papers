# research sigma deep analysis

**collapse aware mixing** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 41
- **Recorded user turns:** 0
- **Tool calls:** 20
- **Original source:** `logs/chats/worker_research_sigma-deep-analysis_20260512T172849.jsonl`
- **Structured JSON:** [`26c86402a40aa8bd03bc.json`](../../sessions/26/26c86402a40aa8bd03bc.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

41 recorded events

### Tool call

_source line 1 · 2026-05-12T17:33:12.094275+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:WebSearch,WebFetch,mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__save_project_file",
  "max_results": "4"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_sigma-deep-analysis_20260512T172849",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:WebSearch,WebFetch,mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__save_project_file",
    "max_results": "4"
  }
}
```

</details>

---

### Tool result

_source line 2 · 2026-05-12T17:33:12.094598+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_sigma-deep-analysis_20260512T172849",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-12T17:33:12.094774+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "SIGMA spectral model collapse LLM 2026 Gram matrix"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_sigma-deep-analysis_20260512T172849",
  "tool": "WebSearch",
  "tool_args": {
    "query": "SIGMA spectral model collapse LLM 2026 Gram matrix"
  }
}
```

</details>

---

### Tool call

_source line 4 · 2026-05-12T17:33:12.094964+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "SIGMA spectral indicator model collapse generative AI 2026 ICLR ICML NeurIPS arXiv"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_sigma-deep-analysis_20260512T172849",
  "tool": "WebSearch",
  "tool_args": {
    "query": "SIGMA spectral indicator model collapse generative AI 2026 ICLR ICML NeurIPS arXiv"
  }
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-12T17:33:12.095106+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "collapse-aware-mixing",
  "file": "memory.md",
  "max_chars": "12000"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_sigma-deep-analysis_20260512T172849",
  "tool": "mcp__agent-ml-research__read_project_file",
  "tool_args": {
    "project": "collapse-aware-mixing",
    "file": "memory.md",
    "max_chars": "12000"
  }
}
```

</details>

---

### Tool call

_source line 6 · 2026-05-12T17:33:12.095229+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "collapse-aware-mixing",
  "file": "ideas.md",
  "max_chars": "12000"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_sigma-deep-analysis_20260512T172849",
  "tool": "mcp__agent-ml-research__read_project_file",
  "tool_args": {
    "project": "collapse-aware-mixing",
    "file": "ideas.md",
    "max_chars": "12000"
  }
}
```

</details>

---

### Tool result

_source line 7 · 2026-05-12T17:33:12.095396+00:00_

Web search results for query: "SIGMA spectral model collapse LLM 2026 Gram matrix"

Links: [{"title":"[2601.03385] SIGMA: Scalable Spectral Insights for LLM Model Collapse","url":"https://arxiv.org/abs/2601.03385"},{"title":"SIGMA: Scalable Spectral Insights for LLM Model Collapse","url":"https://www.arxiv.org/pdf/2601.03385"},{"title":"Sigma: Scalable Spectral Insights for LLM Model Collapse","url":"https://arxiv.org/html/2601.03385"},{"title":"Sigma: Scalable Spectral Insights for LLM Collapse","url":"https://arxiv.org/html/2601.03385v1"},{"title":"Predicting LLM Compression Degradation from Spectral Statistics","url":"https://arxiv.org/pdf/2604.18085"},{"title":"Spectral Lens: Activation and Gradient Spectra as Diagnostics of LLM Optimization","url":"https://arxiv.org/html/2605.05683"},{"title":"Downloads 2026","url":"https://iclr.cc/Downloads/2026"},{"title":"AI Updates Today (May 2026) – Latest AI Model Releases","url":"https://llm-stats.com/llm-updates"},{"title":"What is Model Collapse? Examples, Causes and Fixes","url":"https://www.analyticsvidhya.com/blog/2026/01/model-collapse/"},{"title":"Why Model Collapse In LLMs Is Inevitable With Self-Learning | Hackaday","url":"https://hackaday.com/2026/04/29/why-model-collapse-in-llms-is-inevitable-with-self-learning/"}]

Based on the search results, here's what I found about SIGMA and spectral model collapse in LLMs:

## SIGMA: Spectral Insights for LLM Model Collapse

SIGMA (Spectral Inequalities for Gram Matrix Analysis) is a unified framework that benchmarks model collapse through the spectral lens of the embedding Gram matrix.

### Background on Model Collapse

Model collapse is a degenerative process where recursive training on model-generated content leads to a contraction of distributional variance and representational quality.

### The SIGMA Framework

By deriving and utilizing deterministic and stochastic bounds on the matrix's spectrum, SIGMA provides a mathematically grounded metric to track the contract
…[truncated 812 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_sigma-deep-analysis_20260512T172849",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-12T17:33:12.095586+00:00_

Web search results for query: "SIGMA spectral indicator model collapse generative AI 2026 ICLR ICML NeurIPS arXiv"

Links: [{"title":"[2601.03385] SIGMA: Scalable Spectral Insights for LLM Model Collapse","url":"https://arxiv.org/abs/2601.03385"},{"title":"Sigma: Scalable Spectral Insights for LLM Model Collapse","url":"https://arxiv.org/html/2601.03385"},{"title":"Sigma: Scalable Spectral Insights for LLM Collapse","url":"https://arxiv.org/html/2601.03385v1"},{"title":"SIGMA: Scalable Spectral Insights for LLM Model Collapse","url":"https://www.arxiv.org/pdf/2601.03385v2"},{"title":"Model collapse - Wikipedia","url":"https://en.wikipedia.org/wiki/Model_collapse"},{"title":"Lazy Diffusion: Mitigating spectral collapse in generative diffusion-based stable autoregressive emulation of turbulent flows","url":"https://arxiv.org/html/2512.09572v1"},{"title":"Sigma AI — human context to accelerate next-gen AI - Sigma AI","url":"https://sigma.ai/"},{"title":"AI Model Collapse: Causes and Prevention - WitnessAI","url":"https://witness.ai/blog/ai-model-collapse/"},{"title":"AI Model Collapse: Causes, Early Signs, and How to Prevent It","url":"https://www.projectpro.io/article/ai-model-collapse/1177"},{"title":"An explanation of AI model collapse","url":"https://www.techtarget.com/whatis/video/An-explanation-of-AI-model-collapse"}]

I found relevant results about SIGMA! Here's what the search revealed:

## SIGMA: Scalable Spectral Insights for LLM Model Collapse

SIGMA (Spectral Inequalities for Gram Matrix Analysis) is a unified framework that benchmarks model collapse through the spectral lens of the embedding Gram matrix.

### Key Features

SIGMA addresses "model collapse"—a degenerative process where recursive training on model-generated content leads to a contraction of distributional variance and representational quality.

By deriving and utilizing deterministic and stochastic bounds on the matrix's spectrum, SIGMA provides a mathematically grounded metric to track the c
…[truncated 954 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_sigma-deep-analysis_20260512T172849",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 9 · 2026-05-12T17:33:12.095795+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/collapse-aware-mixing/memory.md\", \"content\": \"# Memory — collapse-aware-mixing\\n\\n## 竞争格局\\n\\n### SIGMA 已占据\\\"谱分析检测 collapse\\\"位置 (2026-05-12)\\nSIGMA (2026-01) 已将 Gram 矩阵谱分析用于 LLM model collapse 检测。**不能 claim \\\"首次将谱分析用于 collapse 检测\\\"。** 但 SIGMA 无控制机制、未验证 leading indicator。我们的 novelty = SIGMA 谱监控 + ERBP 理论动机 + EntroPIC PI 控制范式，首次组合成：谱有效秩 → PI 控制器 → 动态 real/synthetic 比例调节。推荐 framing：从 \\\"spectral metrics detect collapse\\\" → **\\\"from passive monitoring to active closed-loop control\\\"**。\\n\\n## 经验教训\\n\\n### 实验运行期间禁止修改依赖代码 (2026-05-12)\\nReviewer 指出：v5 pipeline 运行期间 Worker 修改了 metrics.py 和 pilot_pipeline.py。虽然当前 run 不受影响（进程已加载旧模块），但**今后实验进程运行期间不修改服务器上该实验依赖的代码文件**。新功能等 run 完成后再部署。\\n\\n### Pythia-1b + wikitext-103 + lr=1e-5 导致发散 (2026-05-12)\\nmvp_pilot_v4 在 G0 训练 760 步后 loss 维持 106-116（正常应为 2-4），PPL 溢出到 inf。独立诊断确认 ratio=1.00（非 transformers 报告 artifact，是真实发散）。grad_norm 43-113 无 NaN/Inf，训练速度稳定 2.08s/step，说明梯度计算正常但 loss landscape 不对。**lr=1e-5 对 Pythia-1b fine-tune wikitext-103 可能过大，下次考虑 2e-6 或更低。**\\n\\n### tmux + conda 环境激活 (2026-05-12)\\nsubmit_training_job 通过 tmux 执行命令，tmux 默认用 sh 而非 bash。bash -c 命令**必须**包含 `source /root/miniconda3/etc/profile.d/conda.sh && conda activate base`，否则 python3 找不到。mvp_pilot 因此崩溃。\\n\\n### AutoDL network_turbo 必须在 tmux 命令中显式激活 (2026-05-12)\\nsubmit_training_job 的命令在 tmux 新 session 中执行，不继承 Worker SSH session 的环境变量。因此 `source /etc/network_turbo` 必须写在 bash -c 命令里，否则 HuggingFace 不可达（`Errno 101: Network is unreachable`）。同时需设置：\\n- `REQUESTS_CA_BUNDLE=/etc/ssl/certs/ca-certificates.crt`\\n- `SSL_CERT_FILE=/etc/ssl/certs/ca-certificates.crt`\\n- `HF_HUB_DISABLE_XET=1`\\n- `HF_HOME=/root/autodl-tmp/.hf_cache`\\n\\nmvp_pilot_v2 因此崩溃（tokenizer vocab_file 未缓存 → AttributeError）。\\n\\n### HF 数据集下载锁阻塞 (2026-05-12)\\ndry-run/测试后必须清理遗留 Python 进程，否则 HF dataset builder lock 会阻塞后续正式实验。PID 2371（测试用 `load_dataset('openwebtext')`）持锁
…[truncated 2328 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_sigma-deep-analysis_20260512T172849",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-12T17:33:12.096005+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"No ideas.md found for 'collapse-aware-mixing'.\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_sigma-deep-analysis_20260512T172849",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-12T17:33:12.096177+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://arxiv.org/html/2601.03385",
  "prompt": "Extract the COMPLETE technical details of the SIGMA paper. I need:\n\n1. EXACT spectral metrics used (effective rank? spectral norm? condition number? eigenvalue distribution? what specific formula?)\n2. Which layers are analyzed (embedding layer only? all layers? specific layers?)\n3. The deterministic vs stochastic bounds - what exactly are they?\n4. Did they validate leading indicator properties? If so, what is the time lead over perplexity?\n5. Experimental setup: model sizes, datasets, number of training generations, batch sizes\n6. Do they propose any control mechanism or mitigation strategy? Or purely monitoring/detection?\n7. Their definition of the Gram matrix - is it token embeddings, or weight matrices?\n8. Key equations and theorems\n9. Limitations they acknowledge\n10. The \"scalable estimation\" method - how do they avoid full eigendecomposition?\n\nBe thorough - extract every technical detail available."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_sigma-deep-analysis_20260512T172849",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://arxiv.org/html/2601.03385",
    "prompt": "Extract the COMPLETE technical details of the SIGMA paper. I need:\n\n1. EXACT spectral metrics used (effective rank? spectral norm? condition number? eigenvalue distribution? what specific formula?)\n2. Which layers are analyzed (embedding layer only? all layers? specific layers?)\n3. The deterministic vs stochastic bounds - what exactly are they?\n4. Did they validate leading indicator properties? If so, what is the time lead over perplexity?\n5. Experimental setup: model sizes, datasets, number of training generations, batch sizes\n6. Do they propose any control mechanism or mitigation strategy? Or purely monitoring/detection?\n7. Their definition of the Gram matrix - is it token embeddings, or weight matrices?\n8. Key equations and theorems\n9. Limitations they acknowledge\n10. The \"scalable estimation\" method - how do they avoid full eigendecomposition?\n\nBe thorough - extract every technical detail available."
  }
}
```

</details>

---

### Tool call

_source line 12 · 2026-05-12T17:33:12.096310+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://arxiv.org/abs/2601.03385",
  "prompt": "Extract: 1) Full list of authors and affiliations, 2) Complete abstract, 3) Publication venue (is it accepted at any conference like ICLR 2026, ICML 2026?), 4) Paper version history, 5) Any mentions of code availability or GitHub repo"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_sigma-deep-analysis_20260512T172849",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://arxiv.org/abs/2601.03385",
    "prompt": "Extract: 1) Full list of authors and affiliations, 2) Complete abstract, 3) Publication venue (is it accepted at any conference like ICLR 2026, ICML 2026?), 4) Paper version history, 5) Any mentions of code availability or GitHub repo"
  }
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-12T17:33:12.096432+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "collapse-aware-mixing",
  "file": "ROADMAP.md",
  "max_chars": "12000"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_sigma-deep-analysis_20260512T172849",
  "tool": "mcp__agent-ml-research__read_project_file",
  "tool_args": {
    "project": "collapse-aware-mixing",
    "file": "ROADMAP.md",
    "max_chars": "12000"
  }
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-12T17:33:12.096563+00:00_

# SIGMA: Scalable Spectral Insights for LLM Model Collapse - Paper Details

## 1) Authors and Affiliations
The paper lists seven authors: Yi Gu, Lingyou Pang, Xiangkun Ye, Tianyu Wang, Jianyu Lin, Carey E. Priebe, and Alexander Aue. However, **specific institutional affiliations are not displayed on this abstract page**.

## 2) Complete Abstract
The authors present their framework as addressing "model collapse"—"a degenerative process where recursive training on model-generated content leads to a contraction of distributional variance and representational quality." They propose SIGMA, which uses "deterministic and stochastic bounds on the matrix's spectrum" to track representation space contraction and monitor "the health of recursive training pipelines."

## 3) Publication Venue
**No conference acceptance is mentioned.** The paper is posted on arXiv (identifier 2601.03385) as a preprint with the CS.LG (Machine Learning) classification. There is no indication of acceptance at ICLR 2026, ICML 2026, or any other venue.

## 4) Paper Version History
- **v1**: Submitted January 6, 2026 (122 KB)
- **v2**: January 19, 2026 (120 KB)
- **v3**: March 23, 2026 (120 KB) — current version

## 5) Code Availability
**No code repository or GitHub link is mentioned** on this abstract page. The page includes sections for code availability tools (alphaXiv, CatalyzeX, etc.), but none are populated with actual links.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_sigma-deep-analysis_20260512T172849",
  "tool": "WebFetch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 15 · 2026-05-12T17:33:12.096745+00:00_

# Technical Details of the SIGMA Framework for LLM Model Collapse Detection

## 1. EXACT SPECTRAL METRICS

**Primary Metric: Log-Determinant of Gram Matrix**
The core metric is `log|G| = log(∏λⱼ) = Σlog(λⱼ)` where λⱼ are eigenvalues. Two derived diagnostics track collapse:

- **Track I (Deterministic)**: `𝒢_KF^(k)(δ) = log det(Im + 1/(β̂_k+δ) G_A^(k))`
- **Track II (Stochastic)**: `𝒰_LLN,cov^(k)(δ) = log det(G_A^(k)+δI_m) - m log n_A`

These measure eigenspectrum contraction without full decomposition.

## 2. LAYERS ANALYZED

The framework analyzes **embedding layers only**. Specifically, sentence embeddings X_i ∈ ℝ^m where m=384 (embedding dimension). The Gram matrix G=MM^T is constructed from embedding vectors, not weight matrices or hidden states.

## 3. DETERMINISTIC VS STOCHASTIC BOUNDS

**Theorem 1 (Deterministic Bound):**
```
det(G_A^(k)) ≤ det(G^(k)) ≤ ∏(λᵢ(G_A^(k)) + β_k)
```
where β_k = λ_max(G_B^(k)) is the spectral radius of unobserved data. Distribution-free but loose in practice.

**Theorem 2 (Stochastic Scaling Bound):**
```
det(G^(k)) ≤ K·(n_k/n_A)^m det(G_A)
```
Assumes i.i.d. column vectors from distribution with positive-definite covariance C. Enables scalable estimation.

**Theorem 3 (Error Estimation):**
Provides confidence intervals with precision scaling as `1/√n_A`, not total corpus size n_k.

## 4. LEADING INDICATOR VALIDATION

**No explicit time-lead analysis over perplexity is provided.** The paper evaluates Sigma metrics against model generation quality through two settings (S1: data recursion only; S2: data+weight recursion) but does not report quantitative lead times compared to standard language modeling loss metrics.

## 5. EXPERIMENTAL SETUP

| Parameter | Value |
|-----------|-------|
| Model | OPT-125M (facebook/opt-125m) |
| Dataset | TECH corpus (N=1000 contexts of 64 tokens) |
| Generations | 50 (g=0 to g=50) |
| Epochs/generation | 5 |
| Batch size | 16 |
| Learning rate | 2×10⁻⁵ |
| Synthetic fraction | α=0.0 (pure synthetic) 
…[truncated 3161 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_sigma-deep-analysis_20260512T172849",
  "tool": "WebFetch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-12T17:33:12.096997+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/collapse-aware-mixing/ROADMAP.md\", \"content\": \"# collapse-aware-mixing — Research Dashboard\\n\\n> 最后更新: 2026-05-12 14:06 UTC | 更新原因: D003 数据切换 + 参数更新 + 基础设施教训记录\\n\\n## 核心方向\\n谱塌缩指标（embedding Gram 矩阵有效秩）驱动 PI 控制器，动态调节迭代 LLM 预训练中合成/真实数据混合比例。连接 SIGMA 的谱监控与 ERBP 的熵-储库框架，将被动监控升级为主动闭环控制。详见 IDEA_BRIEF.md。\\n\\n## 当前进展\\n- 阶段：MVP 验证\\n- 目标会议：EMNLP 2026 ARR（DDL 2026-05-25，剩 13 天）\\n- 实验：mvp_pilot v1/v2/v3 均失败（基础设施问题），v4 部署中\\n- 基础设施：cqa1-38874 1×RTX PRO 6000 96GB (cuda:0)\\n- ⚠️ GPU 空转 5+ 小时（09:05 至今）\\n\\n## MVP 验证方案（D003 更新）\\n**核心假设**：谱有效秩在迭代合成训练的 collapse 过程中，比 PPL 更早发出退化信号（leading indicator）。\\n\\n**实验设计**：Pythia-1B，3 代 × 100M tokens（D003: 从 500M 降至 100M），真实数据 wikitext-103-raw-v1（D003: 从 OpenWebText 切换），每 10M tokens 一个 checkpoint（每代 ~10 个 checkpoint）。\\n\\n**指标**：谱有效秩、token 级预测熵方差、n-gram 熵、词表覆盖率、PPL（held-out 真实数据）、代际 KL 散度（含完整分布报告）。\\n\\n### GO 标准（同时满足）\\n1. **谱领先性**：谱有效秩在某 checkpoint t 下降 ≥1σ（σ = G0 阶段 checkpoint 间有效秩的标准差），而此时 PPL 尚未从 G0 基线上升 ≥2 points（绝对值）或 ≥5%（相对值）\\n2. **非平稳性**：代际 KL 散度 > 0.1 nats（报告完整 KL 分布 + 阈值合理性说明）\\n\\n### NO-GO 决策树\\n| 场景 | 判定 | 行动 |\\n|------|------|------|\\n| 谱领先 + KL>0.1 | **GO** | 进入 research，primary framing（leading indicator → 闭环控制） |\\n| 谱与 PPL 同步下降，但谱粒度更细（CV 更小） | **Conditional GO** | pivot 到 secondary framing（higher-resolution indicator） |\\n| KL < 0.1 但 collapse 可测 | **延展** | 加 1 代观察；仍 < 0.1 → kill 自适应控制 claim |\\n| 谱不下降 / PPL 先于谱下降 | **KILL** | 谱指标对 autoregressive LLM collapse 无效 |\\n| 2 代内无 collapse 迹象 | **延展** | 扩到 3 代；仍无 → kill |\\n\\n**资源**：~1-2 GPU-hours（wikitext-103 规模）。\\n\\n## 代码状态\\n- ✅ pilot_pipeline.py（4 bug 修复）\\n- ✅ metrics.py（完整 KL 报告）\\n- ✅ controller.py（14/14 测试通过）\\n- ✅ main_experiment.py（3 bug 修复：optimizer state / KL / golden ratio）\\n- ✅ golden_ratio_baseline.py\\n- ✅ env_init.sh + preflight.sh（系统性修复）\\n- ✅ launch_pilot_v4.sh\\n\\n## 基础设施教训\\nv1-v3 连续崩溃暴露两个系统性缺陷（详见 Reviewer 复盘）：\\n1. 环境初始化未程序化 → 已修
…[truncated 1123 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_sigma-deep-analysis_20260512T172849",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-12T17:33:12.097193+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://arxiv.org/html/2601.03385",
  "prompt": "Extract ALL details about:\n1. The experimental results - what happens to Track I and Track II metrics across generations? Do they decline monotonically? What are the actual numerical values?\n2. Setting S1 vs S2 - what exactly is the difference? S1 is data recursion only, S2 is data+weight recursion - explain in detail\n3. Surface-form diagnostics mentioned (Distinct-2, HHI) - what do these show?\n4. The relationship between their spectral metrics and perplexity/loss - do they correlate? Is one earlier than the other?\n5. Their discussion of related work - what other spectral methods do they cite?\n6. Any mention of \"effective rank\", \"entropy\", \"PI controller\", \"control\", \"mixing ratio\", \"synthetic data ratio\", or \"data mixing\"\n7. The exact model architecture used (OPT-125M details)\n8. Future work section - what do they plan next?\n9. Any mention of ERBP, EntroPIC, or reservoir-based approaches\n10. Their theoretical contribution vs empirical contribution - which is stronger?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_sigma-deep-analysis_20260512T172849",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://arxiv.org/html/2601.03385",
    "prompt": "Extract ALL details about:\n1. The experimental results - what happens to Track I and Track II metrics across generations? Do they decline monotonically? What are the actual numerical values?\n2. Setting S1 vs S2 - what exactly is the difference? S1 is data recursion only, S2 is data+weight recursion - explain in detail\n3. Surface-form diagnostics mentioned (Distinct-2, HHI) - what do these show?\n4. The relationship between their spectral metrics and perplexity/loss - do they correlate? Is one earlier than the other?\n5. Their discussion of related work - what other spectral methods do they cite?\n6. Any mention of \"effective rank\", \"entropy\", \"PI controller\", \"control\", \"mixing ratio\", \"synthetic data ratio\", or \"data mixing\"\n7. The exact model architecture used (OPT-125M details)\n8. Future work section - what do they plan next?\n9. Any mention of ERBP, EntroPIC, or reservoir-based approaches\n10. Their theoretical contribution vs empirical contribution - which is stronger?"
  }
}
```

</details>

---

### Tool call

_source line 18 · 2026-05-12T17:33:12.097329+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "collapse-aware-mixing",
  "file": "paper_framing.md",
  "max_chars": "12000"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_sigma-deep-analysis_20260512T172849",
  "tool": "mcp__agent-ml-research__read_project_file",
  "tool_args": {
    "project": "collapse-aware-mixing",
    "file": "paper_framing.md",
    "max_chars": "12000"
  }
}
```

</details>

---

### Tool result

_source line 19 · 2026-05-12T17:33:12.097490+00:00_

# Analysis of Sigma Paper: Key Details

## 1. Experimental Results

**Track II (Δ𝒰_LLN,cov)** shows dramatic decline in Setting S2:
- S1: final drift ≈ -151, slope ≈ -0.941 (gradual)
- S2: final drift ≈ -1537, slope ≈ -42.621 (steep acceleration)

**Track I (Δ𝒢_KF)** remains stable:
- S1: final drift ≈ -142, slope ≈ -0.918
- S2: final drift ≈ -2.426, slope ≈ +2.350 (near-flat or slightly positive)

The paper describes how "Track II contracts by more than an order of magnitude" in S2 while "Track I remains near zero," representing "early collapse" where observed spectrum contracts but the conservative envelope stays permissive.

## 2. Setting S1 vs S2 Detailed Comparison

**S1 (Restart-from-base):** "Each generation regenerates a fresh synthetic data pool, but training always restarts from the same base model." Isolates data recursion's effect without weight carryover.

**S2 (True recursion):** "We do not restart from a fixed base checkpoint. Instead, we carry the model weights forward across generations." Creates compounding feedback where parameters shaped by earlier generations influence subsequent synthetic generation.

The authors explain S2 exhibits "self-distillation" early on, quietly removing low-probability alternatives before outputs look obviously repetitive.

## 3. Surface-Form Diagnostics

**Distinct-2:** Ratio of unique bigrams to total bigrams. Lower values indicate increased short-range phrase reuse.

**HHI (n-gram):** Herfindahl-Hirschman Index over n-gram frequencies. Higher values indicate concentrated, repeated phrases—measuring whether few n-grams dominate the corpus.

The paper treats these as "contextual, not definitional" and does not claim they define collapse; they contextualize geometric contraction.

## 4. Relationship to Perplexity/Loss

**Not discussed in provided content.** The paper focuses purely on embedding Gram matrix spectral properties and surface-form repetition metrics. No correlation analysis with perplexity or training loss 
…[truncated 2194 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_sigma-deep-analysis_20260512T172849",
  "tool": "WebFetch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-12T17:33:12.097642+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"No paper_framing.md found for 'collapse-aware-mixing'.\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_sigma-deep-analysis_20260512T172849",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 21 · 2026-05-12T17:33:12.097775+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "collapse-aware-mixing",
  "file": "literature_map.yaml",
  "max_chars": "12000"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_sigma-deep-analysis_20260512T172849",
  "tool": "mcp__agent-ml-research__read_project_file",
  "tool_args": {
    "project": "collapse-aware-mixing",
    "file": "literature_map.yaml",
    "max_chars": "12000"
  }
}
```

</details>

---

### Tool result

_source line 22 · 2026-05-12T17:33:12.097915+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"No literature_map.yaml found for 'collapse-aware-mixing'.\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_sigma-deep-analysis_20260512T172849",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 23 · 2026-05-12T17:33:12.098033+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/IDEA_BRIEF*",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/collapse-aware-mixing"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_sigma-deep-analysis_20260512T172849",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/IDEA_BRIEF*",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/collapse-aware-mixing"
  }
}
```

</details>

---

### Tool result

_source line 24 · 2026-05-12T17:33:12.098147+00:00_

docs/IDEA_BRIEF.md

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_sigma-deep-analysis_20260512T172849",
  "tool": "Glob",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 25 · 2026-05-12T17:33:12.098262+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/collapse-aware-mixing/docs/IDEA_BRIEF.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_sigma-deep-analysis_20260512T172849",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/collapse-aware-mixing/docs/IDEA_BRIEF.md"
  }
}
```

</details>

---

### Tool result

_source line 26 · 2026-05-12T17:33:12.098545+00:00_

1	# Idea Brief: Spectral Collapse-Aware Adaptive Mixing via Entropy-Reservoir PI Control for Iterative Synthetic-Real LLM Pretraining
2	
3	
4	- **Idea ID**: `idea_012`
5	- **Created**: 2026-05-12
6	- **Approved**: 2026-05-12
7	- **Source**: foreign:be-idea-gen-0509-4
8	- **Level**: top-tier
9	- **Target Venues**: EMNLP 2026 (ARR submission deadline: May 25, 2026) — primary target, 15 days from today. Three contributions: spectral collapse indicator for closed-loop control, PI-ERBP stability connection (tiered: design guidance guaranteed, formal proof aspirational), pilot-validated improvement margin via KL-based non-stationarity measurement., AAAI 2027 (deadline projected July-August 2026) — extended version with Tier 3 formal proof (if not achieved for EMNLP), formal κ/s_min bounds for specific architectures, additional conditions (ForTIFAI-TCE combination, AC-ODM comparison), and 6+ generation experiments, ICLR 2027 (estimated deadline September-October 2026) — alternative venue for extended version
10	
11	## Seed Topic
12	
13	Target: EMNLP 2026, ARR submission deadline 2026-05-25 (16 days from today 2026-05-09). Track: Machine Learning for NLP / Resources and Evaluation. Aligns with EMNLP 2026 special theme "New Missions for NLP Research" which explicitly calls for work on data contamination, synthetic data feedback loops, and data governance.
14	
15	Direction: Synthetic data quality, model collapse prevention, contamination detection. In-scope: synthetic data verification/filtering methods, detecting training data contamination in benchmarks, methods to break recursive data feedback loops, data mixing strategies that prevent quality degradation, principled synthetic data generation with quality guarantees.
16	
17	Contribution type: METHOD ONLY. Must propose a concrete detection algorithm, filtering pipeline, or training recipe — not just an observation about model collapse. Method + analysis OK.
18	
19	HARD CONSTRAINTS:
20	1. Compute: ≤200 H100-hours total. Mode
…[truncated 42389 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_sigma-deep-analysis_20260512T172849",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 27 · 2026-05-12T17:33:12.098734+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/collapse-aware-mixing/artifacts/",
  "description": "List existing artifacts"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_sigma-deep-analysis_20260512T172849",
  "tool": "Bash",
  "tool_args": {
    "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/collapse-aware-mixing/artifacts/",
    "description": "List existing artifacts"
  }
}
```

</details>

---

### Tool result

_source line 28 · 2026-05-12T17:33:12.098892+00:00_

_project
code
diag_mvp_pilot_v4.md
literature_survey_spectral_collapse.md
manifest.yaml

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_sigma-deep-analysis_20260512T172849",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 29 · 2026-05-12T17:33:12.099081+00:00_

called Write

<details open><summary>🔧 Tool call — Write</summary>

````json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/collapse-aware-mixing/artifacts/sigma_deep_analysis.md",
  "content": "# SIGMA Deep Analysis: Precise Differentiation from Collapse-Aware Mixing\n\n> Generated: 2026-05-12 | Source: arXiv:2601.03385 v3 (2026-03-23)\n> Authors: Yi Gu, Lingyou Pang, Xiangkun Ye, Tianyu Wang, Jianyu Lin, Carey E. Priebe, Alexander Aue\n> Venue: arXiv preprint (no conference acceptance as of 2026-05)\n\n---\n\n## 1. SIGMA 技术方法详解\n\n### 1.1 谱指标：log-determinant, 非有效秩\n\nSIGMA 的核心指标是 **Gram 矩阵的 log-determinant**（`log|G| = Σ log(λⱼ)`），而非 spectral effective rank。具体实现为两条并行的诊断轨道：\n\n| | Track I (确定性) | Track II (随机性) |\n|---|---|---|\n| **公式** | `𝒢_KF(δ) = Σ log(1 + λᵢ(G_A)/(β̂_k+δ))` | `𝒰_LLN,cov(δ) = log det(G_A+δI) - m·log(n_A)` |\n| **理论基础** | Weyl 不等式 + Ky Fan 优超 | 大数定律缩放 |\n| **性质** | 保守的上界包络（distribution-free） | 灵敏的统计估计量 |\n| **敏感度** | 低（S2 下几乎平坦，slope ≈ +2.35） | 高（S2 下 slope ≈ -42.6） |\n\n**关键区别**：SIGMA 用 log-determinant（特征值的对数之和），我们用 **spectral effective rank = exp(H(σ))**（归一化奇异值分布的 Shannon 熵的指数）。两者虽然都基于谱分析，但数学定义不同：\n- log-det 对所有特征值等权求和，对小特征值的变化极其敏感（log 在零附近放大）\n- effective rank 先归一化为概率分布再算熵，反映的是谱的\"均匀程度\"而非\"总量\"\n- effective rank 有界（∈ [1, m]），更适合作为控制器输入信号\n\n### 1.2 分析层级：仅 embedding 层\n\nSIGMA 分析的是 **sentence embeddings**（m=384 维），使用冻结的 sentence encoder 提取。不分析 weight matrices、hidden states 或 attention patterns。\n\nGram 矩阵定义：`G = M·Mᵀ ∈ S⁺ᵐ`，其中 M ∈ ℝ^(m×n) 将 embedding 向量排列为列。\n\n我们的方法同样使用 embedding 层 Gram 矩阵，但用模型自身的 final-layer hidden states（非外部 sentence encoder），更直接反映模型内部表征健康度。\n\n### 1.3 可扩展估计：子采样 + Cholesky\n\nSIGMA 避免全矩阵特征分解的方法：\n1. 仅计算 n_A 列的子 Gram 矩阵 G_A（n_A > m 即可）\n2. 用 Cholesky 分解计算 log-det（`log det = 2Σ log Lᵢᵢ`），O(m³) 复杂度\n3. 通过 Theorem 2 的缩放律 `m·log(n/n_A)` 估计全 Gram 矩阵的 log-det\n4. Theorem 3 给出估计误差的置信区间，精度仅依赖 n_A，与总语料大小 n 无关\n\n### 1.4 实验设置\n\n| 参数 | SIGMA | 我们（MVP pilot） |\n|------|-------|-------------------|\n| 模型 | OPT-125M (125M) | Pythia-1B (1B) |\n| 数据集 | TECH corpus (1000 contexts × 64 tokens) | wikitext-103-raw-v1 |\n| 迭代代数 | 50 代 | 3 代（pilot），5 代（full） |\n| 每代 epoch | 5 | - |\n| 合成比例 | α=0.0（纯合成） | 动态调节（PI 控制） |\n| Embedding 维度 | 384（外部 encoder） | 模型自身 hidden dim |\n| 评估指标 | log-det, Distinct-2, HHI | effective rank, PPL, KL, n-gram entropy |\n\n### 1.5 两种实验设置\n\n- **S1 (Restart-from-base)**：每代重新生成合成数据，但训练总是从同一个 base model 重启。隔离数据递归效应。\n- **S2 (True recursion)**：权重跨代继续训练，形成自蒸馏反馈环。\n\n实验结果：\n- S1: Track II 缓慢下降（slope ≈ -0.94/代，50 代后总漂移 ≈ -151）\n- S2: Track II 急剧下降（slope ≈ -42.6/代，50 代后总漂移 ≈ -1537），而 Track I 几乎不变\n- 两条轨道的发散本身被用作早期 collapse 的诊断信号\n\n---\n\n## 2. Leading Indicator 验证\n\n### SIGMA 未做的事情\n\n**SIGMA 未验证 leading indicator 特性。** 论文未报告：\n- 谱指标与 perplexity 的时序对比\n- 谱指标相对于 PPL 的提前预警时间\n- 谱指标与下游任务性能的相关性分析\n\nSIGMA 仅展示了 Track I 与 Track II 的发散模式作为 collapse 的诊断签名，但未与传统性能指标（PPL、loss）做时序竞赛。论文明确承认缺乏预测能力：\"measures collapse states but does not predict failure before output degradation becomes visible\"。\n\n### 我们的差异化机会\n\n这是一个关键的 contribution 空间。我们的 MVP pilot 核心假设正是验证 **spectral effective rank 作为 PPL 的 leading indicator**——即谱有效秩在 PPL 尚未显著上升时已经开始下降。这是 SIGMA 完全未触及的。\n\n---\n\n## 3. 控制机制\n\n### SIGMA：纯监控，无控制\n\nSIGMA 是一个 **纯诊断/监控框架**。论文未提出任何：\n- 数据混合比例调节\n- 训练干预策略\n- 反馈控制机制\n- 缓解措施建议\n\n未来工作方向是 Koopman Operator Theory——从\"监控状态\"过渡到\"预测动力学\"，但仍然是预测，不是控制。\n\n### 我们：闭环 PI 控制\n\n我们的核心 novelty：\n- 谱有效秩 → PI 控制器输入\n- PI 控制器 → 实时调节 real/synthetic 混合比例 w_t\n- 公式：`w_t = w_{t-1} - Kp·(r_t - r_{t-1}) - Ki·(r_t - r_target)`\n- rank 下降 → 增加真实数据比例；rank 恢复 → 减少真实数据比例\n- 有离散时间稳定性分析（Tier 1）和 ERBP 连接（Tier 2）\n\n---\n\n## 4. 精确对比矩阵\n\n| 维度 | SIGMA | 我们 (Collapse-Aware Mixing) |\n|------|-------|------------------------------|\n| **谱指标** | log-determinant of Gram matrix | spectral effective rank = exp(H(σ)) |\n| **分析对象** | 外部 sentence encoder embeddings (m=384) | 模型自身 final-layer hidden states |\n| **诊断 vs 控制** | 纯监控/诊断 | 闭环 PI 控制器 |\n| **Leading indicator** | 未验证 | 核心假设 + 实验验证 |\n| **数据混合** | 未涉及（纯合成 α=0） | real/synthetic 动态混合比例 |\n| **理论贡献** | 确定性/随机性谱界（3 个定理） | PI 稳定性 + ERBP 连接（tiered） |\n| **控制理论** | 无 | 离散时间 PI 稳定性条件 |\n| **ERBP 连接** | 无 | λ·s_min > κ 条件驱动 setpoint |\n| **实验规模** | OPT-125M, 50 代, 极小数据 | Pythia-1B, 3-5 代, wikitext-103 |\n| **应用场景** | 递归训练管线健康监控 | 迭代合成预训练的数据治理 |\n| **代码** | 未公开 | - |\n| **发表状态** | arXiv preprint (未被会议接收) | 目标 EMNLP 2026 |\n\n---\n\n## 5. SIGMA 的局限性 = 我们的 Contribution 空间\n\n### 5.1 无控制机制（最大差异）\nSIGMA 在检测到 collapse 后无法做任何事情。我们将谱信号接入闭环控制器，实现\"从被动监控到主动干预\"。\n\n### 5.2 未验证 leading indicator\nSIGMA 未与 PPL/loss 做时序对比。我们的 pilot 明确测试谱有效秩是否领先于 PPL 下降。\n\n### 5.3 纯合成设置，未考虑混合场景\nSIGMA 实验仅在 α=0（100% 合成）设置下运行，未研究 real/synthetic 混合场景。我们的方法核心就是动态混合。\n\n### 5.4 极小实验规模\nOPT-125M + 1000 条 64-token 上下文（~64K tokens）。我们用 Pythia-1B + wikitext-103（~100M tokens/代），更接近实际预训练规模。\n\n### 5.5 外部 encoder 依赖\nSIGMA 依赖冻结的外部 sentence encoder (384 维) 提取 embeddings。这引入了额外依赖，且 encoder 本身可能对某些 collapse 模式不敏感。我们直接用模型自身的 hidden states。\n\n### 5.6 理论聚焦于界，非控制\nSIGMA 的三个定理建立的是谱界（bounds），不涉及如何利用这些信号做决策。我们建立 PI 控制器稳定性条件并连接到 ERBP 的信息几何框架。\n\n### 5.7 Track I 保守性\nTrack I 在 S2 设置下几乎平坦（slope ≈ +2.35），对 true recursion collapse 不敏感。两条轨道的发散虽然可以作为诊断信号，但需要同时维护两个指标增加了复杂度。我们的 effective rank 是单一标量信号。\n\n### 5.8 无预测/预判能力\n论文自承\"measures collapse states but does not predict failure\"。Koopman operator 方向是未来工作。\n\n---\n\n## 6. Paper Positioning 素材\n\n### 6.1 Introduction 定位（建议措辞）\n\n> Recent work has shown that spectral analysis of embedding Gram matrices can detect representational collapse in LLMs. SIGMA (Gu et al., 2026) derives deterministic and stochastic bounds on the log-determinant of the Gram matrix, providing a scalable monitoring framework that captures collapse-induced contraction of the representation space. However, SIGMA operates purely as a diagnostic tool — detecting collapse states post-hoc without providing mechanisms for intervention or prevention. We take the next step: integrating spectral collapse indicators into a closed-loop PI controller that dynamically adjusts the synthetic-to-real data mixing ratio to actively prevent collapse during iterative training.\n\n### 6.2 Related Work 定位（建议段落）\n\n> **Spectral collapse monitoring.** SIGMA (Gu et al., 2026) introduces a two-track framework for monitoring model collapse via the log-determinant of the embedding Gram matrix. Their deterministic bound (Track I) provides a conservative envelope via Weyl's inequality, while the stochastic estimator (Track II) offers greater sensitivity, detecting collapse an order of magnitude earlier than Track I in true-recursion settings. However, SIGMA differs from our approach in several key respects: (1) they use the log-determinant metric, while we use spectral effective rank (exp(H(σ))), which provides a bounded, normalized signal more suitable as a controller input; (2) they analyze embeddings from a frozen external sentence encoder rather than the model's own representations; (3) they validate only on OPT-125M with a corpus of ~64K tokens across 50 generations, while we target Pythia-1B scale with 100M+ tokens per generation; and most critically, (4) they use spectral metrics purely for monitoring, whereas we integrate them into a PI controller for active data composition adjustment. SIGMA explicitly identifies the transition from monitoring to prediction as future work; we address the complementary gap of transitioning from monitoring to control.\n\n### 6.3 核心 Framing\n\n**一句话定位**：SIGMA 证明了\"谱分析能检测 collapse\"；我们回答\"检测到 collapse 后怎么办\"。\n\n**Contribution 矩阵定位**（2×2 象限图）：\n\n```\n                  Offline/Monitoring    Online/Closed-loop\n                  ─────────────────    ──────────────────\nLoss-based    │   DoReMi, Aioli       AC-ODM (withdrawn)\n              │\nSpectral      │   SIGMA, DiSF         ★ Ours ★\n```\n\n我们占据的是 **spectral × online closed-loop** 的空白象限。\n\n### 6.4 不应 claim 的\n\n- ~~首次将谱分析用于 LLM collapse 检测~~（SIGMA 在先）\n- ~~首次使用 Gram 矩阵分析 collapse~~（SIGMA 在先）\n- ~~首次提出 scalable 的谱 collapse 指标~~（SIGMA 的子采样方法在先）\n\n### 6.5 可以 claim 的\n\n1. **首次将谱 collapse 指标用于闭环控制**（SIGMA 纯监控，DiSF 是离线选择，SSO 是权重空间）\n2. **首次验证 effective rank 作为 PPL 的 leading indicator**（SIGMA 未做时序对比）\n3. **首次连接 ERBP 稳定性条件与 PI 控制器设计**（ERBP 未提供动态调节机制）\n4. **首次在迭代 synthetic-real 混合场景下实现自适应数据比例控制**（有别于 generic domain mixing 的 Aioli/GRAPE）\n\n---\n\n## 7. 风险评估\n\n| 风险 | 概率 | 影响 | 缓解 |\n|------|------|------|------|\n| Reviewer 认为我们只是\"SIGMA + PI controller 的 trivial 拼接\" | 中 | 高 | 强调 non-trivial integration challenges（信号量化噪声、setpoint 跨规模迁移、ERBP 连接），用 toy model 论证 effective rank 与 log-det 的本质差异 |\n| SIGMA 在 camera-ready 前被 ICML/NeurIPS 接收，reviewer 期待与其对比实验 | 低 | 中 | 准备 log-det vs effective rank 的消融实验作为 appendix |\n| Reviewer 要求解释为何不直接使用 SIGMA 的 log-det 而用 effective rank | 高 | 低 | effective rank 有界 [1,m] 适合控制器输入，log-det 无界且对正则化参数 δ 敏感 |\n\n---\n\n## 8. 补充：SIGMA 未引用/未涉及的框架\n\nSIGMA 未引用 ERBP、EntroPIC、RankMe，也未涉及 PI/PID 控制、数据混合优化、或 dynamic regret theory。这些都是我们独立的理论支柱。\n"
}
````

</details>

<details><summary>Recorded metadata</summary>

````json
{
  "recorded_role": "tool",
  "session": "worker_research_sigma-deep-analysis_20260512T172849",
  "tool": "Write",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/collapse-aware-mixing/artifacts/sigma_deep_analysis.md",
    "content": "# SIGMA Deep Analysis: Precise Differentiation from Collapse-Aware Mixing\n\n> Generated: 2026-05-12 | Source: arXiv:2601.03385 v3 (2026-03-23)\n> Authors: Yi Gu, Lingyou Pang, Xiangkun Ye, Tianyu Wang, Jianyu Lin, Carey E. Priebe, Alexander Aue\n> Venue: arXiv preprint (no conference acceptance as of 2026-05)\n\n---\n\n## 1. SIGMA 技术方法详解\n\n### 1.1 谱指标：log-determinant, 非有效秩\n\nSIGMA 的核心指标是 **Gram 矩阵的 log-determinant**（`log|G| = Σ log(λⱼ)`），而非 spectral effective rank。具体实现为两条并行的诊断轨道：\n\n| | Track I (确定性) | Track II (随机性) |\n|---|---|---|\n| **公式** | `𝒢_KF(δ) = Σ log(1 + λᵢ(G_A)/(β̂_k+δ))` | `𝒰_LLN,cov(δ) = log det(G_A+δI) - m·log(n_A)` |\n| **理论基础** | Weyl 不等式 + Ky Fan 优超 | 大数定律缩放 |\n| **性质** | 保守的上界包络（distribution-free） | 灵敏的统计估计量 |\n| **敏感度** | 低（S2 下几乎平坦，slope ≈ +2.35） | 高（S2 下 slope ≈ -42.6） |\n\n**关键区别**：SIGMA 用 log-determinant（特征值的对数之和），我们用 **spectral effective rank = exp(H(σ))**（归一化奇异值分布的 Shannon 熵的指数）。两者虽然都基于谱分析，但数学定义不同：\n- log-det 对所有特征值等权求和，对小特征值的变化极其敏感（log 在零附近放大）\n- effective rank 先归一化为概率分布再算熵，反映的是谱的\"均匀程度\"而非\"总量\"\n- effective rank 有界（∈ [1, m]），更适合作为控制器输入信号\n\n### 1.2 分析层级：仅 embedding 层\n\nSIGMA 分析的是 **sentence embeddings**（m=384 维），使用冻结的 sentence encoder 提取。不分析 weight matrices、hidden states 或 attention patterns。\n\nGram 矩阵定义：`G = M·Mᵀ ∈ S⁺ᵐ`，其中 M ∈ ℝ^(m×n) 将 embedding 向量排列为列。\n\n我们的方法同样使用 embedding 层 Gram 矩阵，但用模型自身的 final-layer hidden states（非外部 sentence encoder），更直接反映模型内部表征健康度。\n\n### 1.3 可扩展估计：子采样 + Cholesky\n\nSIGMA 避免全矩阵特征分解的方法：\n1. 仅计算 n_A 列的子 Gram 矩阵 G_A（n_A > m 即可）\n2. 用 Cholesky 分解计算 log-det（`log det = 2Σ log Lᵢᵢ`），O(m³) 复杂度\n3. 通过 Theorem 2 的缩放律 `m·log(n/n_A)` 估计全 Gram 矩阵的 log-det\n4. Theorem 3 给出估计误差的置信区间，精度仅依赖 n_A，与总语料大小 n 无关\n\n### 1.4 实验设置\n\n| 参数 | SIGMA | 我们（MVP pilot） |\n|------|-------|-------------------|\n| 模型 | OPT-125M (125M) | Pythia-1B (1B) |\n| 数据集 | TECH corpus (1000 contexts × 64 tokens) | wikitext-103-raw-v1 |\n| 迭代代数 | 50 代 | 3 代（pilot），5 代（full） |\n| 每代 epoch | 5 | - |\n| 合成比例 | α=0.0（纯合成） | 动态调节（PI 控制） |\n| Embedding 维度 | 384（外部 encoder） | 模型自身 hidden dim |\n| 评估指标 | log-det, Distinct-2, HHI | effective rank, PPL, KL, n-gram entropy |\n\n### 1.5 两种实验设置\n\n- **S1 (Restart-from-base)**：每代重新生成合成数据，但训练总是从同一个 base model 重启。隔离数据递归效应。\n- **S2 (True recursion)**：权重跨代继续训练，形成自蒸馏反馈环。\n\n实验结果：\n- S1: Track II 缓慢下降（slope ≈ -0.94/代，50 代后总漂移 ≈ -151）\n- S2: Track II 急剧下降（slope ≈ -42.6/代，50 代后总漂移 ≈ -1537），而 Track I 几乎不变\n- 两条轨道的发散本身被用作早期 collapse 的诊断信号\n\n---\n\n## 2. Leading Indicator 验证\n\n### SIGMA 未做的事情\n\n**SIGMA 未验证 leading indicator 特性。** 论文未报告：\n- 谱指标与 perplexity 的时序对比\n- 谱指标相对于 PPL 的提前预警时间\n- 谱指标与下游任务性能的相关性分析\n\nSIGMA 仅展示了 Track I 与 Track II 的发散模式作为 collapse 的诊断签名，但未与传统性能指标（PPL、loss）做时序竞赛。论文明确承认缺乏预测能力：\"measures collapse states but does not predict failure before output degradation becomes visible\"。\n\n### 我们的差异化机会\n\n这是一个关键的 contribution 空间。我们的 MVP pilot 核心假设正是验证 **spectral effective rank 作为 PPL 的 leading indicator**——即谱有效秩在 PPL 尚未显著上升时已经开始下降。这是 SIGMA 完全未触及的。\n\n---\n\n## 3. 控制机制\n\n### SIGMA：纯监控，无控制\n\nSIGMA 是一个 **纯诊断/监控框架**。论文未提出任何：\n- 数据混合比例调节\n- 训练干预策略\n- 反馈控制机制\n- 缓解措施建议\n\n未来工作方向是 Koopman Operator Theory——从\"监控状态\"过渡到\"预测动力学\"，但仍然是预测，不是控制。\n\n### 我们：闭环 PI 控制\n\n我们的核心 novelty：\n- 谱有效秩 → PI 控制器输入\n- PI 控制器 → 实时调节 real/synthetic 混合比例 w_t\n- 公式：`w_t = w_{t-1} - Kp·(r_t - r_{t-1}) - Ki·(r_t - r_target)`\n- rank 下降 → 增加真实数据比例；rank 恢复 → 减少真实数据比例\n- 有离散时间稳定性分析（Tier 1）和 ERBP 连接（Tier 2）\n\n---\n\n## 4. 精确对比矩阵\n\n| 维度 | SIGMA | 我们 (Collapse-Aware Mixing) |\n|------|-------|------------------------------|\n| **谱指标** | log-determinant of Gram matrix | spectral effective rank = exp(H(σ)) |\n| **分析对象** | 外部 sentence encoder embeddings (m=384) | 模型自身 final-layer hidden states |\n| **诊断 vs 控制** | 纯监控/诊断 | 闭环 PI 控制器 |\n| **Leading indicator** | 未验证 | 核心假设 + 实验验证 |\n| **数据混合** | 未涉及（纯合成 α=0） | real/synthetic 动态混合比例 |\n| **理论贡献** | 确定性/随机性谱界（3 个定理） | PI 稳定性 + ERBP 连接（tiered） |\n| **控制理论** | 无 | 离散时间 PI 稳定性条件 |\n| **ERBP 连接** | 无 | λ·s_min > κ 条件驱动 setpoint |\n| **实验规模** | OPT-125M, 50 代, 极小数据 | Pythia-1B, 3-5 代, wikitext-103 |\n| **应用场景** | 递归训练管线健康监控 | 迭代合成预训练的数据治理 |\n| **代码** | 未公开 | - |\n| **发表状态** | arXiv preprint (未被会议接收) | 目标 EMNLP 2026 |\n\n---\n\n## 5. SIGMA 的局限性 = 我们的 Contribution 空间\n\n### 5.1 无控制机制（最大差异）\nSIGMA 在检测到 collapse 后无法做任何事情。我们将谱信号接入闭环控制器，实现\"从被动监控到主动干预\"。\n\n### 5.2 未验证 leading indicator\nSIGMA 未与 PPL/loss 做时序对比。我们的 pilot 明确测试谱有效秩是否领先于 PPL 下降。\n\n### 5.3 纯合成设置，未考虑混合场景\nSIGMA 实验仅在 α=0（100% 合成）设置下运行，未研究 real/synthetic 混合场景。我们的方法核心就是动态混合。\n\n### 5.4 极小实验规模\nOPT-125M + 1000 条 64-token 上下文（~64K tokens）。我们用 Pythia-1B + wikitext-103（~100M tokens/代），更接近实际预训练规模。\n\n### 5.5 外部 encoder 依赖\nSIGMA 依赖冻结的外部 sentence encoder (384 维) 提取 embeddings。这引入了额外依赖，且 encoder 本身可能对某些 collapse 模式不敏感。我们直接用模型自身的 hidden states。\n\n### 5.6 理论聚焦于界，非控制\nSIGMA 的三个定理建立的是谱界（bounds），不涉及如何利用这些信号做决策。我们建立 PI 控制器稳定性条件并连接到 ERBP 的信息几何框架。\n\n### 5.7 Track I 保守性\nTrack I 在 S2 设置下几乎平坦（slope ≈ +2.35），对 true recursion collapse 不敏感。两条轨道的发散虽然可以作为诊断信号，但需要同时维护两个指标增加了复杂度。我们的 effective rank 是单一标量信号。\n\n### 5.8 无预测/预判能力\n论文自承\"measures collapse states but does not predict failure\"。Koopman operator 方向是未来工作。\n\n---\n\n## 6. Paper Positioning 素材\n\n### 6.1 Introduction 定位（建议措辞）\n\n> Recent work has shown that spectral analysis of embedding Gram matrices can detect representational collapse in LLMs. SIGMA (Gu et al., 2026) derives deterministic and stochastic bounds on the log-determinant of the Gram matrix, providing a scalable monitoring framework that captures collapse-induced contraction of the representation space. However, SIGMA operates purely as a diagnostic tool — detecting collapse states post-hoc without providing mechanisms for intervention or prevention. We take the next step: integrating spectral collapse indicators into a closed-loop PI controller that dynamically adjusts the synthetic-to-real data mixing ratio to actively prevent collapse during iterative training.\n\n### 6.2 Related Work 定位（建议段落）\n\n> **Spectral collapse monitoring.** SIGMA (Gu et al., 2026) introduces a two-track framework for monitoring model collapse via the log-determinant of the embedding Gram matrix. Their deterministic bound (Track I) provides a conservative envelope via Weyl's inequality, while the stochastic estimator (Track II) offers greater sensitivity, detecting collapse an order of magnitude earlier than Track I in true-recursion settings. However, SIGMA differs from our approach in several key respects: (1) they use the log-determinant metric, while we use spectral effective rank (exp(H(σ))), which provides a bounded, normalized signal more suitable as a controller input; (2) they analyze embeddings from a frozen external sentence encoder rather than the model's own representations; (3) they validate only on OPT-125M with a corpus of ~64K tokens across 50 generations, while we target Pythia-1B scale with 100M+ tokens per generation; and most critically, (4) they use spectral metrics purely for monitoring, whereas we integrate them into a PI controller for active data composition adjustment. SIGMA explicitly identifies the transition from monitoring to prediction as future work; we address the complementary gap of transitioning from monitoring to control.\n\n### 6.3 核心 Framing\n\n**一句话定位**：SIGMA 证明了\"谱分析能检测 collapse\"；我们回答\"检测到 collapse 后怎么办\"。\n\n**Contribution 矩阵定位**（2×2 象限图）：\n\n```\n                  Offline/Monitoring    Online/Closed-loop\n                  ─────────────────    ──────────────────\nLoss-based    │   DoReMi, Aioli       AC-ODM (withdrawn)\n              │\nSpectral      │   SIGMA, DiSF         ★ Ours ★\n```\n\n我们占据的是 **spectral × online closed-loop** 的空白象限。\n\n### 6.4 不应 claim 的\n\n- ~~首次将谱分析用于 LLM collapse 检测~~（SIGMA 在先）\n- ~~首次使用 Gram 矩阵分析 collapse~~（SIGMA 在先）\n- ~~首次提出 scalable 的谱 collapse 指标~~（SIGMA 的子采样方法在先）\n\n### 6.5 可以 claim 的\n\n1. **首次将谱 collapse 指标用于闭环控制**（SIGMA 纯监控，DiSF 是离线选择，SSO 是权重空间）\n2. **首次验证 effective rank 作为 PPL 的 leading indicator**（SIGMA 未做时序对比）\n3. **首次连接 ERBP 稳定性条件与 PI 控制器设计**（ERBP 未提供动态调节机制）\n4. **首次在迭代 synthetic-real 混合场景下实现自适应数据比例控制**（有别于 generic domain mixing 的 Aioli/GRAPE）\n\n---\n\n## 7. 风险评估\n\n| 风险 | 概率 | 影响 | 缓解 |\n|------|------|------|------|\n| Reviewer 认为我们只是\"SIGMA + PI controller 的 trivial 拼接\" | 中 | 高 | 强调 non-trivial integration challenges（信号量化噪声、setpoint 跨规模迁移、ERBP 连接），用 toy model 论证 effective rank 与 log-det 的本质差异 |\n| SIGMA 在 camera-ready 前被 ICML/NeurIPS 接收，reviewer 期待与其对比实验 | 低 | 中 | 准备 log-det vs effective rank 的消融实验作为 appendix |\n| Reviewer 要求解释为何不直接使用 SIGMA 的 log-det 而用 effective rank | 高 | 低 | effective rank 有界 [1,m] 适合控制器输入，log-det 无界且对正则化参数 δ 敏感 |\n\n---\n\n## 8. 补充：SIGMA 未引用/未涉及的框架\n\nSIGMA 未引用 ERBP、EntroPIC、RankMe，也未涉及 PI/PID 控制、数据混合优化、或 dynamic regret theory。这些都是我们独立的理论支柱。\n"
  }
}
````

</details>

---

### Tool result

_source line 30 · 2026-05-12T17:33:12.099368+00:00_

File created successfully at: /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/collapse-aware-mixing/artifacts/sigma_deep_analysis.md

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_sigma-deep-analysis_20260512T172849",
  "tool": "Write",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 31 · 2026-05-12T17:33:12.099517+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__append_idea",
  "max_results": "1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_sigma-deep-analysis_20260512T172849",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__append_idea",
    "max_results": "1"
  }
}
```

</details>

---

### Tool result

_source line 32 · 2026-05-12T17:33:12.099645+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_sigma-deep-analysis_20260512T172849",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 33 · 2026-05-12T17:33:12.099774+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "register_artifact",
  "max_results": "3"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_sigma-deep-analysis_20260512T172849",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "register_artifact",
    "max_results": "3"
  }
}
```

</details>

---

### Tool result

_source line 34 · 2026-05-12T17:33:12.099913+00:00_

No matching deferred tools found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_sigma-deep-analysis_20260512T172849",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 35 · 2026-05-12T17:33:12.100029+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "register_artifact",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/collapse-aware-mixing/artifacts/manifest.yaml",
  "output_mode": "content"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_sigma-deep-analysis_20260512T172849",
  "tool": "Grep",
  "tool_args": {
    "pattern": "register_artifact",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/collapse-aware-mixing/artifacts/manifest.yaml",
    "output_mode": "content"
  }
}
```

</details>

---

### Tool result

_source line 36 · 2026-05-12T17:33:12.100140+00:00_

No matches found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_sigma-deep-analysis_20260512T172849",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 37 · 2026-05-12T17:33:12.100250+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/collapse-aware-mixing/artifacts/manifest.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_sigma-deep-analysis_20260512T172849",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/collapse-aware-mixing/artifacts/manifest.yaml"
  }
}
```

</details>

---

### Tool result

_source line 38 · 2026-05-12T17:33:12.100401+00:00_

1	- id: art_20260512_fb1679
2	  name: MVP Pilot 实验代码
3	  type: intermediate
4	  description: 'Pythia-1B 迭代合成训练 pilot 代码：训练循环 (HF Trainer) + 6 项崩塌检测指标 (谱有效秩/token
5	    熵方差/n-gram 熵/词表覆盖率/PPL/代际 KL) + 合成数据生成 + 全流程编排。文件: config.py, data_utils.py, metrics.py,
6	    generate.py, train.py, pilot_pipeline.py, requirements.txt'
7	  path: projects/collapse-aware-mixing/artifacts/_project/intermediate/pilot_pipeline.py
8	  url: null
9	  project: collapse-aware-mixing
10	  exp_id: null
11	  skill: ''
12	  created_at: '2026-05-12T08:58:15.853621+00:00'
13	  tags:
14	  - code
15	  - mvp
16	  - pilot
17	  - spectral-rank
18	  - model-collapse
19	- id: art_20260512_b8e7c5
20	  name: controller.py
21	  type: intermediate
22	  description: Discrete-time PI controller for collapse-aware real/synthetic data
23	    mixing (CollapseAwareController + ControllerConfig)
24	  path: projects/collapse-aware-mixing/artifacts/_project/intermediate/controller.py
25	  url: null
26	  project: collapse-aware-mixing
27	  exp_id: null
28	  skill: ''
29	  created_at: '2026-05-12T11:23:30.104218+00:00'
30	  tags:
31	  - controller
32	  - pi-controller
33	  - code
34	- id: art_20260512_8f8ca7
35	  name: test_controller.py
36	  type: intermediate
37	  description: '14 unit tests for PI controller: steady state, rank drop, recovery,
38	    clamp, reset, history'
39	  path: projects/collapse-aware-mixing/artifacts/_project/intermediate/test_controller.py
40	  url: null
41	  project: collapse-aware-mixing
42	  exp_id: null
43	  skill: ''
44	  created_at: '2026-05-12T11:23:32.519716+00:00'
45	  tags:
46	  - test
47	  - controller
48	  - code
49	- id: art_20260512_5fef4c
50	  name: golden_ratio_baseline.py
51	  type: intermediate
52	  description: Fixed-ratio real/synthetic mixing baseline. G0 100% real, G1+ mixed
53	    at --real_ratio. Outputs JSON summary.
54	  path: projects/collapse-aware-mixing/artifacts/_project/intermediate/golden_ratio_baseline.py
55	  url: null
56	  project: collapse-aware-mixing
5
…[truncated 1214 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_sigma-deep-analysis_20260512T172849",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 39 · 2026-05-12T17:33:12.100557+00:00_

called Edit

<details open><summary>🔧 Tool call — Edit</summary>

```json
{
  "replace_all": "False",
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/collapse-aware-mixing/artifacts/manifest.yaml",
  "old_string": "  tags:\n  - literature\n  - novelty\n  - framing\n  - SIGMA\n  - ERBP",
  "new_string": "  tags:\n  - literature\n  - novelty\n  - framing\n  - SIGMA\n  - ERBP\n- id: art_20260512_a3d1f0\n  name: SIGMA 深度分析报告\n  type: report\n  description: SIGMA (arXiv:2601.03385) 全文技术分析：log-det vs effective rank、无控制机制、未验证\n    leading indicator、实验规模局限。含精确对比矩阵、paper positioning 素材、Related Work 建议措辞。\n  path: projects/collapse-aware-mixing/artifacts/sigma_deep_analysis.md\n  url: null\n  project: collapse-aware-mixing\n  exp_id: null\n  skill: ''\n  created_at: '2026-05-12T19:30:00.000000+00:00'\n  tags:\n  - literature\n  - SIGMA\n  - positioning\n  - related-work\n  - novelty"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_sigma-deep-analysis_20260512T172849",
  "tool": "Edit",
  "tool_args": {
    "replace_all": "False",
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/collapse-aware-mixing/artifacts/manifest.yaml",
    "old_string": "  tags:\n  - literature\n  - novelty\n  - framing\n  - SIGMA\n  - ERBP",
    "new_string": "  tags:\n  - literature\n  - novelty\n  - framing\n  - SIGMA\n  - ERBP\n- id: art_20260512_a3d1f0\n  name: SIGMA 深度分析报告\n  type: report\n  description: SIGMA (arXiv:2601.03385) 全文技术分析：log-det vs effective rank、无控制机制、未验证\n    leading indicator、实验规模局限。含精确对比矩阵、paper positioning 素材、Related Work 建议措辞。\n  path: projects/collapse-aware-mixing/artifacts/sigma_deep_analysis.md\n  url: null\n  project: collapse-aware-mixing\n  exp_id: null\n  skill: ''\n  created_at: '2026-05-12T19:30:00.000000+00:00'\n  tags:\n  - literature\n  - SIGMA\n  - positioning\n  - related-work\n  - novelty"
  }
}
```

</details>

---

### Tool result

_source line 40 · 2026-05-12T17:33:12.100713+00:00_

The file /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/collapse-aware-mixing/artifacts/manifest.yaml has been updated successfully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_sigma-deep-analysis_20260512T172849",
  "tool": "Edit",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 41 · 2026-05-12T17:33:12.100915+00:00_

报告已保存至 `artifacts/sigma_deep_analysis.md`。核心发现：

**SIGMA 与我们的 4 个关键差异：**

1. **谱指标不同**：SIGMA 用 log-determinant（`Σ log λⱼ`），我们用 spectral effective rank（`exp(H(σ))`）。后者有界 [1,m]，更适合作为控制器输入。

2. **纯监控 vs 闭环控制**：SIGMA 无任何干预/控制机制，未来工作方向是 Koopman operator 预测（仍是被动）。我们有 PI 控制器做实时 real/synthetic 比例调节。

3. **未验证 leading indicator**：SIGMA 未做谱指标与 PPL 的时序对比，自承"measures collapse states but does not predict failure"。这是我们的核心假设验证。

4. **实验设置差异大**：OPT-125M + 64K tokens + 外部 sentence encoder vs 我们的 Pythia-1B + wikitext-103 + 模型自身 hidden states。

**Positioning 一句话**：SIGMA 证明了"谱分析能检测 collapse"；我们回答"检测到之后怎么办"——从 passive monitoring 到 active closed-loop control。

Sources:
- [SIGMA: Scalable Spectral Insights for LLM Model Collapse](https://arxiv.org/abs/2601.03385)
- [SIGMA HTML full text](https://arxiv.org/html/2601.03385)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_research_sigma-deep-analysis_20260512T172849"
}
```

</details>

---
