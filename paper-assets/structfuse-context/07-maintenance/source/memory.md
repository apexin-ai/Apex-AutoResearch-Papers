# Inference-Time Graph Methods 文献对比

## 对比表

| Method | Paper | Venue | Graph Type | Usage Stage | Inter-proc Data-Flow | Task | Scalability | Key Diff from StructFuse |
|--------|-------|-------|-----------|-------------|---------------------|------|-------------|--------------------------|
| **CodexGraph** | Bridging LLMs and Code Repositories via Code Graph Databases | NAACL 2025 (arXiv:2408.03910) | Code graph DB (MODULE/CLASS/FUNCTION nodes; CONTAINS/INHERITS/USES edges) | Inference-time | No. Static analysis for symbol relations only | General repo-level coding (completion, issue resolution) | CrossCodeEval, SWE-bench, EvoCodeBench | Agent queries graph DB at inference; task-agnostic schema but no data-flow semantics |
| **LocAgent** | Graph-Guided LLM Agents for Code Localization | ACL 2025 (arXiv:2503.09089) | Directed heterogeneous graph (code entities + dependency edges) | Inference-time | No. Dependency edges, not data-flow | Fault localization | 92.7% file-level accuracy; SWE-bench +12% Pass@10 | Agent multi-hop graph reasoning at inference; needs fine-tuned 32B model |
| **RANGER** | RANGER — Repository-Level Agent for Graph-Enhanced Retrieval | arXiv:2509.25257 (Sep 2025) | Knowledge graph + MCTS traversal | Inference-time | No | Code search, QA, cross-file retrieval, completion | CodeSearchNet, RepoQA, RepoBench, CrossCodeEval | MCTS-guided graph exploration; dual-stage (Cypher + MCTS); higher inference cost due to cross-encoder scoring |
| **RepoGraph** | Enhancing AI SE with Repository-level Code Graph | ICLR 2025 (arXiv:2410.14684) | Repo-level code graph (class hierarchy, call graph, file structure) | Inference-time | No. Structural relations only | Software engineering / issue resolution | SWE-bench (+32.8% relative); CrossCodeEval | Plug-in module for existing agents; repo-wide navigation; no semantic analysis |
| **GraphCoder** | Enhancing Repo-Level Code Completion via Code Context Graph | ASE 2024 (arXiv:2406.07003) | Code Context Graph (CFG + CDG + DDG) | Inference-time | Partial. Data dependence graph but **intra-procedural** only | Code completion | Repository-level benchmarks | Coarse-to-fine retrieval with CCG; closest to StructFuse in using data/control flow, but intra-proc and at inference-time |
| **CodeRAG** | Supportive Code Retrieval on Bigraph for Real-World Code Generation | arXiv:2504.10046 (Apr 2025) | Bigraph (requirement graph + DS-code graph) | Inference-time | No. Dependency + semantic edges | Repo-level code generation | DevEval (+40.90 Pass@1 w/ GPT-4o) | Dual-graph (requirements + code); agentic reasoning; high inference overhead |
| **ARISE** | ARISE: A Repository-level Graph Representation and Toolset for Agentic Fault Localization and Program Repair | arXiv:2605.03117 (May 2026), Seddik & Fard | Multi-granularity program graph (statement nodes + def-use edges) | Inference-time | Partial. **Intra-procedural** def-use edges + data-flow slicing tool | Fault localization + repair | SWE-bench Lite (300 issues); +17.0 Function Recall@1 | Closest to StructFuse in data-flow usage; but intra-proc only, agent queries at inference |
| **CodeGRAG** | Bridging NL and PL via Graphical RAG | arXiv:2405.02355 (2024) | Composed syntax graph (AST + DFG + CFG) | Both (GNN training + graph prompt at inference) | Partial. DFG extraction but function-level | Code generation (cross-lingual) | Multiple PLs | Only method with training-time component (GNN soft prompts); but graph also used at inference |
| **StructFuse** (Ours) | Structure-Grounded Hard Negatives via CodeQL Data-Flow | — | Inter-procedural data-flow graph (CodeQL taint tracking) | **Training-time only** | **Yes. Full inter-procedural** (source→sink across call boundaries) | Code retrieval (contrastive training) | Large-scale repos with CodeQL | Zero inference overhead; graph used offline for negative mining; inter-proc data-flow |

## Discussion 要点

### StructFuse vs Inference-Time Graph Methods: 互补性与差异性

1. **Cost-accuracy tradeoff**: Inference-time methods (CodexGraph, RANGER, RepoGraph) achieve high precision by constructing and querying graphs per request, but incur significant latency (graph construction + traversal + LLM calls). StructFuse amortizes all graph computation to training time—once the encoder is trained with structure-grounded negatives, inference is a single embedding lookup with zero graph overhead. This makes StructFuse suitable for latency-sensitive production retrieval where inference-time graph methods are impractical.

2. **Data-flow depth**: Most inference-time methods use structural graphs (call graphs, class hierarchies, file dependencies). Only GraphCoder and ARISE incorporate data/control flow, but limited to **intra-procedural** scope. StructFuse uniquely leverages **inter-procedural** data-flow via CodeQL's taint tracking, capturing cross-function semantic relationships (e.g., a sanitizer function that transforms data between source and sink across call boundaries). This deeper semantic signal generates harder, more informative negatives.

3. **Complementarity**: StructFuse and inference-time methods are orthogonal and composable. A StructFuse-trained encoder can serve as the embedding backbone for systems like RANGER or CodexGraph, providing better initial retrieval that reduces the graph agent's search space. Conversely, inference-time graph methods can provide reranking on top of StructFuse retrieval for tasks requiring maximum precision.

4. **Scalability model**: Inference-time methods scale linearly with query volume (each query triggers graph operations). StructFuse's cost is front-loaded: CodeQL analysis runs once per repository update, and the resulting negatives improve the encoder permanently. For high-QPS code search services, this one-time investment yields compounding returns.

5. **Task generality vs specialization**: Inference-time graph agents (CodexGraph, RepoGraph) are task-agnostic but require powerful LLMs as backends. StructFuse produces a specialized retrieval encoder that excels at the code search task without LLM inference, making it deployable as a lightweight, efficient first-stage retriever in multi-stage pipelines.

## Related Work 段落草稿 (~200 words)

**Graph-Based Methods for Code Understanding.**
Recent work has explored leveraging code graphs to enhance LLM-based software engineering. Inference-time approaches construct and query graphs during each interaction: CodexGraph (Liu et al., NAACL 2025) builds a code graph database that LLM agents query via structured interfaces; RepoGraph (Ouyang et al., ICLR 2025) provides repository-level navigation as a plug-in module for SE agents; LocAgent (ACL 2025) and RANGER (Shah et al., 2025) employ graph-guided multi-hop reasoning and MCTS-based traversal for code localization and retrieval, respectively. GraphCoder (ASE 2024) incorporates intra-procedural control-flow and data-dependence graphs for code completion retrieval, while ARISE (Seddik & Fard, 2026) extends this with statement-level def-use edges for fault localization. CodeGRAG (2024) bridges training and inference by using GNN-encoded graph prompts.

These methods achieve strong results but impose substantial inference-time costs—graph construction, traversal, and often multiple LLM calls per query. Moreover, their data-flow analysis remains intra-procedural. StructFuse takes a fundamentally different approach: we leverage CodeQL's inter-procedural taint tracking to generate structure-grounded hard negatives at **training time**, producing an encoder that captures cross-function data-flow semantics without any graph overhead at inference. This positions StructFuse as complementary to inference-time graph methods—it can serve as an efficient first-stage retriever whose embeddings already encode deep structural relationships that other methods must compute on-the-fly.

---

## 参考文献（全部已验证 2026-05-14）

- CodexGraph: arXiv:2408.03910, Liu et al., NAACL 2025
- LocAgent: arXiv:2503.09089, Chen et al., ACL 2025
- RANGER: arXiv:2509.25257, Shah et al., 2025 ✅ verified
- RepoGraph: arXiv:2410.14684, Ouyang et al., ICLR 2025
- GraphCoder: arXiv:2406.07003, Liu et al., ASE 2024
- CodeRAG: arXiv:2504.10046, 2025
- ARISE: arXiv:2605.03117, Seddik & Fard, 2026 ✅ verified (full title: "ARISE: A Repository-level Graph Representation and Toolset for Agentic Fault Localization and Program Repair")
- CodeGRAG: arXiv:2405.02355, 2024

---

## D062 Checkpoint Criterion 效应（pool=50 独立验证, 2026-05-16）

**重大发现**：D062 query split eval 的早期数据（random strategy, selection set 504q, pool=50）显示 checkpoint 选择标准对 R@1 的影响远超预期。

| Seed | best_by_val_loss R@1 | best_by_recall_at_1 R@1 | Δ |
|------|---------------------|------------------------|---|
| s42 | 0.2302 | 0.2302 | 0pp (same ckpt, MD5 identical) |
| s43 | 0.3413 | **0.5040** | **+16.3pp** |
| s44 | 0.3532 | (pending) | — |

**关键洞察**：
1. s43 的 criterion 差异 (+16.3pp) **远大于**任何 strategy 差异（之前最大观测 ~5pp）。Checkpoint 选择标准是 confound 的主要来源，不是 mining strategy。
2. 这直接验证了 D062 query split 方法论的必要性——必须用独立 selection set 选 checkpoint，否则 criterion 偏差会淹没 strategy 效应。
3. 之前 (2026-05-15) 基于 in-training eval (pool=8) 的 criterion 分析显示 mean delta 仅 +0.65pp，严重低估了真实效应。pool=50 独立 eval 揭示的 +16.3pp 说明 pool=8 噪声完全掩盖了 criterion 效应。
4. **论文影响**：D062 结果可能成为方法论贡献的一部分（checkpoint selection methodology），而不仅是消除 confound 的工具。

**待补充**：embedding_distance 和 dataflow_aware 的 criterion 效应数据（D062 eval 6/14 完成中）。

---

## Checkpoint Criterion 与 K 分析 (2026-05-15)

**Checkpoint 选择 criterion 分歧率**：4 个完成的 full M2 runs 中，2/4 (50%) val_loss 与 R@1 选中不同 checkpoint。

**分歧 pattern**：
- Qwen s43: val_loss→step 500, R@1→step 1500, R@1 差 +1.97pp
- StarCoder s42: val_loss→step 1000, R@1→step 2500, R@1 差 +0.64pp
- Mean delta: +0.65pp (R@1 criterion 优于 val_loss criterion)
- StarCoder 步差更大（1500 步 vs 1000 步），与其 pretrained margin 更大的特性一致

**论文写作决策**：主表报 best_by_R@1（target metric aligned），ablation 表展示两种 criterion 对比（D036 已决策 R@1 为 primary）。

**K=7 无 ablation**：所有正式实验固定 K=7。合理性来源：(1) batch_size=8 对齐（1 positive + 7 negatives = 8）(2) DPR 等文献惯例 (3) K=7 negatives are randomly sampled from a pool of 50 strategy-specific candidates per query。K 敏感性列为 limitation/future work。

---

## In-Training Eval 噪声发现 (2026-05-16)

**发现**：in-training eval R@1 有 **±0.5pp 噪声地板**，来源于 val set negative 随机采样。

**根因**（代码审计确认）：
- `val_ds.__getitem__` 中 `random.shuffle(fallback)` 动态采样 negatives（train.py:109-110）
- `val_ds._negatives` 从未被填充（`refresh_negatives` 仅对 train_ds 调用）
- 全局 `random` 状态在训练中持续变化，每次 eval pass 的 negative 组合不同
- dataloader `shuffle=False`，问题不在 batch 顺序，在 negative 采样

**证据**：embed_s43 同一模型权重（step 1500）两次 eval：R@1=0.5606 (periodic) vs 0.5655 (final) = 0.49pp 差异。val_loss 同理：0.4926 vs 0.4876。

**影响**：
1. Claim 1 的 strategy delta（2-seed mean ≈ 0, 单 seed -0.67 ~ +0.52pp）与噪声**同量级**
2. in-training eval 不能可靠区分 strategies
3. **pool=50 post-hoc eval（negatives 预定义、确定性）是唯一可靠对比基础**
4. 论文不应基于 in-training eval 数值做 strategy ranking claim

**修复建议**：eval 时固定 seed 或预写死 val negatives。当前已跑实验不需重跑（pool=50 re-eval 会修复）。

---

## UniXcoder Null Result (2026-05-16)

**发现**：UniXcoder-base (125M, encoder-only RoBERTa) 3 strategies × seed 42，strategy differentiation 完全消失。

| Strategy | R@1 (pool=8) | val_loss |
|----------|-------------|----------|
| random | 0.5534 | 0.4513 |
| embedding | 0.5497 | 0.4466 |
| dataflow | 0.5510 | 0.4628 |

R@1 span 仅 0.37pp，三策略在噪声范围内无差异。

**解释假设**：
1. **Model capacity**: 125M 参数可能不足以利用 hard negative 的细粒度结构信息。大模型 (3B Qwen/StarCoder) 有更多参数来编码 structural 差异。
2. **Representation space**: UniXcoder 的 pretrained representation 可能已经更 uniform（RoBERTa-based encoder vs decoder-only），hard negative 的 "hardness" 在其表征空间中差异更小。
3. **Training dynamics**: batch_size=16 + max_seq_length=1024（vs Qwen/StarCoder 的 batch=8 + seq=2048），可能改变了 InfoNCE loss 的梯度结构。

**论文定位**：3 encoder × 3 seed 实验中，null only on encoder-only/small-scale → "strategy differentiation is model-capacity dependent"，支撑 Track A (stratified heterogeneity)。s43/s44 已启动，用于 3-seed 统计确认。

**Regime 差异**：s42 patience=3, s43/s44 patience=2。Paper 中需标注。

---

## BM25 Negative Mining 策略洞察 (2026-05-14, updated)

**两层重叠率数据（注意区分）**：
- **k=50 全候选重叠**（mining worker 报告）：BM25 vs embedding 87.1%, vs random 76.2%, vs dataflow 71.8%
- **top-7 Jaccard**（训练实际用的 num_negatives=7，分层分析）：差异远大于全候选

**分层 top-7 Jaccard 重叠率**（seed 42, 2920 matched queries / 12290 total）：
| 层级 | BM25 vs Embedding | BM25 vs Random | BM25 vs Dataflow |
|------|-------------------|----------------|------------------|
| Small (<50 files, 39 repos) | 0.668 | 0.411 | 0.667 |
| Medium (50-200, 29 repos) | 0.380 | 0.067 | 0.363 |
| Large (200+, 15 repos) | 0.297 | 0.007 | 0.405 |

**核心修正**：之前基于 87% 预测"Phase 2 中 BM25 R@1 很可能接近 embedding"——这个预测可能不成立。在中大 repo（训练数据主体）上 top-7 Jaccard 仅 30-38%，BM25 和 embedding 选出的训练 negatives 大部分不同。Phase 2 训练结果将真正区分两种策略。

**意外发现**：BM25 vs dataflow 在大 repo 上重叠率（0.405）高于 vs embedding（0.297）。词汇相似性信号与数据流依赖有部分对齐，而纯 embedding 距离选择了不同维度的 hard negatives。

---

## hard_negative_mining.py vs build_m1_training_data.py 实现差异 [2026-05-15]

**发现者**：Reviewer
**影响**：当前 M2 不受影响（用 pre-mined 数据），plan_015（dynamic negative mining）实施前必须对齐

**差异**：

### hard_negative_mining.py `DataFlowAwareMiner`（training/hard_negative_mining.py）
三步法：
1. **Embedding top-K**：调用 `EmbeddingDistanceMiner.mine()` 获取 top-50 cosine similarity 最高的 candidates（从所有 non-positive candidates 中）
2. **Dataflow filter**：过滤掉 `_is_reachable(query, fid)` 为 True 的文件——仅检查 `dataflow_graph[src]` 中的直接条目（1-hop 可达性）
3. **BM25 re-rank**：如果 `bm25_index` 可用，对剩余 disconnected candidates 按 BM25 分数降序重排
4. **Fallback**：如果 disconnected 不足 `num_negatives`，用 random padding 补足

### build_m1_training_data.py `build_candidate_pools()`（scripts/build_m1_training_data.py）
两步法：
1. **Dataflow filter**：从 `non_pos_files` 中排除 `full_connected_set`（= `positive_files ∪ cg_connected`，即 dataflow 直连 + call graph 邻居——比 `DataFlowAwareMiner` 排除范围更广）
2. **BM25 sort**：对 disconnected 文件按 BM25 分数降序排序，取 top-K（pool_size=50）
3. **无 embedding 步骤**：dataflow pool 完全不使用 embedding 信号

额外注意：当 `--model-path` 未提供时，`emb_scores = bm25`（line 317-318），此时 embedding pool 也退化为 BM25 排序，仅在是否排除 `full_connected` 上与 dataflow pool 不同。

### 差异总结

| 维度 | hard_negative_mining.py | build_m1_training_data.py |
|------|------------------------|--------------------------|
| Candidate 初筛 | Embedding cosine top-50 | 全部 non-positive（无初筛） |
| Dataflow 排除范围 | `dataflow_graph[src]` 直接条目 | `positive_files ∪ cg_connected`（更广） |
| 排序信号 | Embedding 为主 → BM25 re-rank | 纯 BM25 排序 |
| Embedding 角色 | 主选择器（决定候选池） | 不参与 dataflow pool |
| BM25 角色 | 可选的 re-ranker | 唯一排序信号 |

### 对齐建议
plan_015 实施 dynamic negative mining 时需统一为一种逻辑。建议：
1. **排除范围统一**：采用 `build_m1_training_data.py` 的 `full_connected`（dataflow + call graph），因为 call graph 邻居也不应作为 hard negatives
2. **选择信号**：dynamic mining 应使用当前 epoch 的 encoder embedding（不是 pretrained），这是 dynamic mining 的核心价值——所以 `DataFlowAwareMiner` 的 embedding→filter→BM25 三步法更合理，但需将排除范围从 1-hop dataflow 扩展到 full_connected
3. **具体改动**：修改 `DataFlowAwareMiner._is_reachable()` 使其也排除 call graph 连接，或在 `mine()` 中接受 `full_connected_set` 参数

---

## SWE-bench eval 脚本路径 [2026-05-15, Reviewer 纠正]

eval_swebench 脚本已存在（之前 Worker 搜索了错误目录 /root/structfuse）：
- `/root/structfuse-context/evaluation/eval_swebench.py`（含 .bak 和 .pyc）
- `/root/structfuse-context/scripts/eval_swebench_e2e.py`

Agent 通过 OpenAI-compatible API 调用（非本地推理），配置项：STRUCTFUSE_LLM_BACKEND=api, STRUCTFUSE_LLM_API_BASE, STRUCTFUSE_LLM_API_KEY, STRUCTFUSE_LLM_MODEL。Retriever 和 agent 分离，单卡 VRAM 无压力。plan_003 基于现有脚本执行，不需要从头创建。

---

## Qwen 链日志缓冲问题 [2026-05-15, Reviewer 发现]

Qwen 链脚本用 `python`（有 stdout 缓冲），导致日志延迟输出，监控出现盲区。StarCoder 链用了 `python -u` 没此问题。**后续 Qwen subrun 启动时须加 `PYTHONUNBUFFERED=1` 环境变量或 `python -u`**，保证日志实时输出。当前 run 不需要重启。

---

## 运维经验 (2026-05-14)

**Registry 状态机 workaround**：当长链训练（多 run 串行）中途因 cron timeout 或子进程退出导致 registry 状态误标（DONE/failed 或 ANALYZING），而实际训练仍在跑时，不可回退状态。解决方案：创建 `{exp_id}_resumed` / `{exp_id}_continued` 新 entry，步进 PREPARING→QUEUED→ALLOCATED→RUNNING，注册 cron 监控实际 PID。原 entry 保留历史 metrics。

**Bash 预读陷阱**：运行中的 bash 脚本已将循环体/数组预读到内存，磁盘上修改脚本文件不影响执行。需要在链外设置独立 tmux watcher 监控链 PID 退出后手动触发后续任务。

**BM25 Phase 2 触发机制**：两个 tmux watcher（`bm25_starcoder_watcher`, `bm25_qwen_watcher`）每 5 分钟检查链 PID 存活，退出后自动启动 BM25 脚本。watcher 启动的训练不经过 submit_training_job，需在链完成回调中补注册 cron。

---

## 关键决策记录

**m1_reextract_v2 数据使用决策 (2026-05-14, Director Session 8)**：即使 reextract 将数据从 ~16K 增至 ~44K，不重跑 M2。原因：ARR May 25 DDL 不允许再加 4-5 天重训。处理方式：(1) post-M2 完成后若有 GPU 空档，跑 1-seed pilot (Qwen, embedding, 新数据) 对比当前 M2 baseline；(2) 论文中作为 scalability/data efficiency 讨论点；(3) 全量重训留 camera-ready。

---

## Related Work Gap 分析 [2026-05-15]

当前 literature_map.yaml 39 篇，已超 25+ 目标，但覆盖不均。最薄弱：contrastive learning for code（仅 3 篇）、通用 hard negative mining 方法论。推荐添加 7 篇（全部 WebSearch 验证）：
- **必须加**：RocketQA (NAACL 2021)、ContraBERT (ICSE 2023)、ProGraML (ICML 2021)、CrossCodeEval (NeurIPS 2023)
- **强烈建议**：SynCoBERT (arXiv 2021)、CAPSTONE (EMNLP 2023)
- **可选**：CoSQA (ACL 2021)

---

## Qwen random_s42 训练 Regime 异常 [2026-05-16]

**根因确认**：s42 使用 3 epoch / patience=0（D026 设计，提供 overfitting curve），而 s43/s44 使用 2 epoch / patience=2（D050 统一 regime）。这导致：
- warmup 424 步 vs 283 步，step 500 时 s42 val_loss 已比 s43/s44 差 (0.4869 vs 0.4476/0.4252)
- s42 两个 checkpoint (best_by_val_loss + best_by_recall_at_1) MD5 完全相同（均 step 1000），pool=50 R@1 两种选法结果一致是预期行为
- pool=50 R@1: s42=0.2730 vs s43=0.3138 / s44=0.3181，差距 4pp+ 主要由 regime 差异解释

**决策影响**：当前 random_s42 不应纳入 cross-seed 统计。需用统一 2-epoch/patience=2 regime 重训才能获得可比结果。Supplement chain (embed_s42/dataflow_s42/bm25_s42) 已用 D050 统一 regime，不受影响。
