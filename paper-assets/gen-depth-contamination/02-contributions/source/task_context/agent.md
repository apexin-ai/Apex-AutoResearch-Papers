---
loop: 20
reason: idle_timeout
updated: '2026-05-25T06:26:19+00:00'
---

### 1. 🔴 硬约束 / 红线
- GPU 白名单：cuda:0, cuda:1, cuda:2, cuda:3（cqa1-22115），不可用其他设备
- 论文已提交 EMNLP 2026 ARR（2026-05-25），当前所有实验是 post-submission rebuttal reinforcement，不改论文 framing
- OLMo-1B 是"弱模型例外"narrative 的核心：K*=1 across all domains。不要把 OLMo 结果当 negative——它是 competence-limitation 的正面证据
- LLaMA-8B Wiki 1v2 Bonf CI upper=0.6049 微跨 θ=0.60，点估计 0.5919 < θ。Paper 中 K*=1 by convention，但 CI 需要在 limitations 提及
- cross-scorer 统一用 Qwen2.5-1.5B-Instruct，不可换 scorer（一致性要求）

### 2. 🖥️ 基础设施快照
- 服务器：cqa1-22115，工作目录 `/root/autodl-tmp/gen-depth-contamination/`
- Python：`source /root/miniconda3/etc/profile.d/conda.sh && conda activate base`（aml-train 镜像，不用 venv）
- GPU：4× RTX PRO 6000 Blackwell 98GB，全部空闲
- 模型缓存：`/root/autodl-tmp/.hf_cache/`（Qwen2.5-1.5B-Instruct, OLMo-1B, Gemma-2-27B 等已缓存）
- 关键脚本：`scripts/run_*.py`（各实验入口），`scripts/run_pipeline.py`（通用 OBD pipeline）
- 结果目录：`results/` 和 `data/`
- 活跃进程：无（全部实验已完成，服务器刚重启后无残留进程）
- Cron：无活跃 cron
- W&B：未使用（本项目用 JSON 结果文件 + registry）

### 3. 📊 当前状态
**所有 post-submission 实验已完成。** Registry 无 RUNNING/PREPARING 实验（除历史 killed/failed 的 sweep 系列残留）。

本轮完成的关键实验及结果：
| 实验 | K*/结论 | 关键 AUC |
|------|---------|---------|
| exp_gemma27b_c4 | K*=2(self)/1(cross) | 1v2=0.615(self), 0v1=0.887(cross) |
| 7b-cross-transfer | 82-85% retention | Qwen-7B↔LLaMA-8B |
| gemma27b_cross_transfer | 27B→small 101.3% | 最强 scale-invariance 证据 |
| arxiv_multi_source | K*=3 | 2v3=0.644, CI [0.629,0.659] |
| code_domain_mistral | K*=2 | 1v2=0.615, Bonf CI [0.602,0.628] |
| code_domain_qwen7b | K*=2 | 1v2=0.727 |
| code_domain_olmo | K*=1 | 1v2=0.557 |
| wiki_domain_mistral | K*=1 | 1v2=0.558 |
| wiki_domain_llama | K*=1 | 1v2=0.592 |
| olmo_arxiv_cross_scorer | K*=1 | 1v2=0.500 |
| olmo_c4_cross_scorer | K*=1 | 1v2=0.500 |
| gemma27b_filtering | 无退化 | binary MMLU +0.02pp, HS +0.41pp |

无等待中的 Worker 回调、Cron、或 Director 决策。

### 4. 📋 待办（条件触发式）
- Director 指示继续跑实验 → 4 张 GPU 全部空闲可用，按 rebuttal 价值排序选实验
- Director 要求 bootstrap CI 补充 → code_domain_olmo 和 gemma27b_filtering 尚未跑 bootstrap CI，可 CPU 执行
- Reviewer 质疑 LLaMA Wiki K*=1 → 1v2 Bonf CI upper=0.6049 跨 θ，准备好解释"point estimate below threshold, CI marginally crosses"
- Reviewer 质疑 OLMo 例外 → 3-domain cross-scorer 数据齐全（C4/arXiv/Code 均 K*=1），可引用 competence-limitation 解释
- Paper Agent 需要数据 → 所有结果已在 registry + results/ 目录的 JSON 文件中，bootstrap CI 在 artifacts/ 和 results/arxiv_multi_source_bootstrap/

### 5. 🎯 战略上下文
- **核心论文 claim**：Generation depth K* 由 domain ceiling 决定（Wiki=1, C4=2, Code=2, arXiv=3），跨模型/跨规模一致，OLMo 作为 competence-limited 例外
- **最强新证据**：(1) Gemma-27B cross-transfer retention >100%（depth signal 是 text-intrinsic）；(2) arXiv K*=3 跨 3 个架构 bootstrap 确认；(3) Mistral 4-domain 单模型内 monotonic staircase
- **gemma27b_filtering 结果偏弱**：binary vs no_filter 仅 +0.41pp HellaSwag（seed 42 是 outlier +1.37pp，另两 seed 无差异），MMLU 持平。Paper claim 是"不退化"而非"改善"，这个 framing 是安全的
- **易错点**：(1) 不要混淆 self-scoring 和 cross-scoring 的 K*——同一模型两种 scoring 可能不同（如 Gemma-27B: self K*=2, cross K*=1）；(2) registry 中有大量历史 killed/failed 的 sweep 系列实验，它们是旧方案的残留，与当前 narrative 无关；(3) code_domain_olmo 的分析脚本有 `int(doc_id)` bug（已修复），如果需要重跑类似 pipeline 注意 doc_id 格式
