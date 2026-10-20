# research related work supplement

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Worker execution logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 81
- **Recorded user turns:** 0
- **Tool calls:** 28
- **Original source:** `logs/workers/worker_research_related_work_supplement_20260514T123126.log`
- **Structured JSON:** [`4af38a20776d7a2cb1bc.json`](../../sessions/4a/4af38a20776d7a2cb1bc.json)

## Before a recorded user message

81 recorded events

### Log line

_source line 1_

Warning: no stdin data received in 3s, proceeding without it. If piping from a slow command, redirect stdin explicitly: < /dev/null to skip, or wait longer.

---

### System

_source line 2_

```json
{
  "type": "system",
  "subtype": "init",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training",
  "session_id": "0a05528b-d05d-4fb3-947f-20e0adce1e25",
  "tools": [
    "Task",
    "AskUserQuestion",
    "Bash",
    "CronCreate",
    "CronDelete",
    "CronList",
    "Edit",
    "EnterPlanMode",
    "EnterWorktree",
    "ExitPlanMode",
    "ExitWorktree",
    "Glob",
    "Grep",
    "ListMcpResourcesTool",
    "Monitor",
    "NotebookEdit",
    "PushNotification",
    "Read",
    "ReadMcpResourceTool",
    "RemoteTrigger",
    "ScheduleWakeup",
    "Skill",
    "TaskOutput",
    "TaskStop",
    "TodoWrite",
    "ToolSearch",
    "WebFetch",
    "WebSearch",
    "Write",
    "mcp__agent-ml-research__append_idea",
    "mcp__agent-ml-research__read_project_file",
    "mcp__agent-ml-research__save_project_file"
  ],
  "mcp_servers": [
    {
      "name": "agent-ml-research",
      "status": "connected"
    }
  ],
  "model": "claude-opus-4-6",
  "permissionMode": "bypassPermissions",
  "slash_commands": [
    "update-config",
    "debug",
    "simplify",
    "batch",
    "fewer-permission-prompts",
    "loop",
    "schedule",
    "claude-api",
    "clear",
    "compact",
    "context",
    "heapdump",
    "init",
    "review",
    "security-review",
    "extra-usage",
    "usage",
    "insights",
    "team-onboarding"
  ],
  "apiKeySource": "none",
  "claude_code_version": "2.1.126",
  "output_style": "default",
  "agents": [
    "claude",
    "Explore",
    "general-purpose",
    "Plan",
    "statusline-setup"
  ],
  "skills": [
    "update-config",
    "debug",
    "simplify",
    "batch",
    "fewer-permission-prompts",
    "loop",
    "schedule",
    "claude-api"
  ],
  "plugins": [],
  "analytics_disabled": false,
  "uuid": "b848962f-c89a-4d34-9993-d26c213c67cb",
  "memory_paths": {
    "auto": "/home/ubuntu/.claude-account-4/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-10-projects-provenance-weight-training/memory/"
  },
  "fast_mode_state": "off"
}
```

---

### Runtime record

_source line 3_

```json
{
  "type": "rate_limit_event",
  "rate_limit_info": {
    "status": "allowed",
    "resetsAt": 1778779200,
    "rateLimitType": "five_hour",
    "overageStatus": "rejected",
    "overageDisabledReason": "org_level_disabled",
    "isUsingOverage": false
  },
  "uuid": "69661440-6df7-42fc-9871-cd8593bf0a5d",
  "session_id": "0a05528b-d05d-4fb3-947f-20e0adce1e25"
}
```

---

### Assistant

_source line 4_

Let me start by reading the current survey file and searching for the two papers.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "0a05528b-d05d-4fb3-947f-20e0adce1e25",
  "uuid": "f655494f-3013-499f-9c08-d09468e0f5c1",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Mb7WnajvbE6ejeq1WVc3WW",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 11842,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 11842
      },
      "output_tokens": 2,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool call

_source line 5_

<details open><summary>🔧 Tool call — Read · `toolu_01NhSFdzfrwsN7RLhBL5bqqk`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/related_work_notes.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "0a05528b-d05d-4fb3-947f-20e0adce1e25",
  "uuid": "de43227c-e712-4db2-a484-03232ebcc38a",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Mb7WnajvbE6ejeq1WVc3WW",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 11842,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 11842
      },
      "output_tokens": 2,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-14T12:31:38.416Z_

<details><summary>↩ Tool result · `toolu_01NhSFdzfrwsN7RLhBL5bqqk`</summary>

```text
1	# Related Work Survey — Provenance Weight Training
2	
3	## 1. Data Quality / Data Selection for LLM Pretraining
4	
5	| # | 论文 | 年份 | 场所 | 一句话 Contribution | 与我们的关系 |
6	|---|------|------|------|-------------------|------------|
7	| 1 | **DSIR: Data Selection for Language Models via Importance Resampling** (Xie, Santurkar, Ma, Liang) | 2023 | NeurIPS | 用 hashed n-gram 特征估计 importance weight，对大规模语料做 importance resampling 来匹配目标分布 | DSIR 按目标分布做 selection，我们按 provenance 做 weighting——都用 lightweight feature 做数据筛选，但动机不同：DSIR 优化 domain match，我们降低 synthetic contamination |
8	| 2 | **QuRating: Selecting High-Quality Data for Training Language Models** (Wettig, Gupta, Malik, Chen) | 2024 | ICML | 用 LLM pairwise judgment 对数据做 4 维质量评分（writing style / expertise / facts / educational value），训练 QuRater 模型标注 260B 语料 | QuRating 用 LLM 判断 "质量"，我们用检测器判断 "来源"——都是 model-based annotation + downstream reweighting，但 quality 和 provenance 是正交维度 |
9	| 3 | **The FineWeb Datasets: Decanting the Web for the Finest Text Data at Scale** (Penedo et al., HuggingFace) | 2024 | arXiv | 用 Llama-3-70B 合成标注训练 educational quality classifier，过滤出 1.3T token 的 FineWeb-Edu，在 MMLU/ARC 上大幅领先 | FineWeb-Edu 用 LLM-based classifier 做 hard filtering（保留/丢弃），我们用 detector 做 soft weighting（降权不丢弃），保留更多数据多样性 |
10	| 4 | **D4: Improving LLM Pretraining via Document De-Duplication and Diversification** (Tirumala, Simig et al.) | 2023 | NeurIPS D&B | 用 pretrained embedding + K-Means 做去重和多样性平衡，6.7B 模型上提升 2% 下游准确率和 20% 训练效率 | D4 关注重复和多样性，我们关注 synthetic contamination——互补方法，可以先 D4 去重再用我们的 provenance weighting |
11	| 5 | **DoReMi: Optimizing Data Mixtures Speeds Up Language Model Pretraining** (Xie, Pham et al.) | 2023 | NeurIPS | 用 Group DRO 在 proxy model 上优化 domain mixture weights，无需下游任务信息，8B 模型提升 6.5% few-shot 准确率 | DoReMi 做 domain-level reweighting（按 domain 调权），我们做 instance-level reweighting（按 q-score 调权）——粒度不同，理论上可以组合使用 |
12	| 6 | **DataComp-LM (DCLM): In Search of the Next Generation of Training Sets for Language Models** (Li et al.) | 2024 | NeurIPS D&B | 提供 240T token 标准化语料 + 评估套件，系统性对比 data curation 策略，证明 model-based filtering 是关键 | DCLM 是 benchmark 框架，我们的 provenance-based weighting 可以作为一种新的 curation strategy 在 DCLM 上评估 |
13	| 7 | **Scaling Data-Constrained Language Models** (Muennighoff, Rush et al.) | 2023 | NeurIPS | 系统研究数据受限时的 scaling law，发现 ≤4 epochs 重复数据对 loss 影响可忽略，提出考虑重复衰减的 compute-optimal law | 当 unique data 不足时更可能混入 synthetic data 来补量——我们的方法提供了一种替代方案：不用丢弃 synthetic data，而是降权使用 |
14	
15	## 2. Synthetic Data Contamination Detection
16	
17	| # | 论文 | 年份 | 场所 | 一句话 Contribution | 与我们的关系 |
18	|---|------|------|------|-------------------|------------|
19	| 1 | **DetectGPT: Zero-Shot Machine-Generated Text Detection using Probability Curvature** (Mitchell et al.) | 2023 | ICML | 零样本检测：用 log probability curvature（在 perturbation 前后的 log-prob 变化）区分 human vs machine text，无需训练分类器 | DetectGPT 做 binary detection（是否机器生成），我们需要 calibrated probability（q-score）——我们选择 TF-IDF + LogReg 正是因为需要 well-calibrated 的连续 score 而非仅 binary 判断 |
20	| 2 | **Fast-DetectGPT: Efficient Zero-Shot Detection via Conditional Probability Curvature** (Bao et al.) | 2024 | ICLR | 将 DetectGPT 的 perturbation 步骤替换为 sampling，加速 340 倍且 AUROC 提升约 75% | 同上——更高效但仍是 binary detection，calibration 质量（ECE）未被重点评估，而这正是我们工作的核心关注点 |
21	| 3 | **Binoculars: Zero-Shot Detection of LLM-Generated Text** (Hans et al.) | 2024 | ICML | 用两个 LLM 的 perplexity / cross-perplexity 比值做检测，ChatGPT 文本在 0.01% FPR 下召回 >90% | Binoculars 需要两个 LLM 推理，计算成本高；我们的 TF-IDF + LogReg 检测器极轻量，适合标注数十亿 token 级别的 pretraining corpus |
22	| 4 | **GLTR: Statistical Detection and Visualization of Generated Text** (Gehrmann, Strobelt, Rush) | 2019 | ACL | 用 LM 的 top-k token 排名做统计检测和可视化，帮助人类识别机器文本（人类检测率从 54% 提升到 72%） | 早期 statistical detection 工作，启发了后续基于 model statistics 的方法；我们的方法同样基于统计特征但目标不同（scoring for weighting 而非 human-in-the-loop detection） |
23	| 5 | **A Watermark for Large Language Models** (Kirchenbauer et al.) | 2023 | ICML | 在生成时嵌入 statistical watermark（green/red token list），可用 p-value 统计检验来检测 | Watermarking 需要控制生成过程，无法检测已有的、未 watermarked 的 synthetic data——我们的场景是 post-hoc detection on existing corpus |
24	| 6 | **A Survey on LLM-Generated Text Detection: Necessity, Methods, and Future Directions** (Wu et al.) | 2024 | Computational Linguistics (MIT Press) | 系统综述 statistical / neural / watermarking 三类检测方法，讨论 robustness 和 generalization | 综述文献，帮助定位我们的检测器在整个 detection 方法谱系中的位置——我们是 training-based statistical classifier，但用于 weighting 而非 filtering |
25	
26	## 3. Sample Reweighting in Training
27	
28	| # | 论文 | 年份 | 场所 | 一句话 Contribution | 与我们的关系 |
29	|---|------|------|------|-------------------|------------|
30	| 1 | **Improving the Accuracy of Likelihood-based Inference under Covariate Shift** (Shimodaira) | 2000 | JASA | 奠基性工作：提出 importance weighted ERM（IWERM），通过 density ratio 修正 covariate shift 下的 loss | 理论基础直接相关——我们的 weight = 1 - q^b 可以看作一种 bounded importance weight，Shimodaira 的 IWERM 理论为我们的方法提供了正当性 |
31	| 2 | **Learning to Reweight Examples for Robust Deep Learning** (Ren, Zeng, Yang, Urtasun) | 2018 | ICML | 用 meta-learning 在训练中动态学习 sample weights（基于 gradient direction 在 clean validation set 上的表现） | L2RW 需要 clean validation set 做 meta-optimization，我们的方法不需要——weight 由 provenance detector 预先确定，无需在训练中迭代调整 |
32	| 3 | **Meta-Weight-Net: Learning an Explicit Mapping For Sample Weighting** (Shu et al.) | 2019 | NeurIPS | 用 MLP 学习 loss → weight 的显式映射函数，在 noisy label 和 class imbalance 场景下优于手工设计的 weighting | 与 L2RW 类似用 meta-learning；我们的 weight function 是 analytic form（1 - q^b），不需要 meta-learning，更透明可解释 |
33	| 4 | **Curriculum Learning** (Bengio, Louradour, Collobert, Weston) | 2009 | ICML | 奠基性工作：证明按从易到难的顺序训练（curriculum）可以加速收敛并改善 non-convex optimization 的局部极小值 | Curriculum learning 按难度排序，我们按 provenance 加权——虽然形式不同（排序 vs 加权），但都是 non-uniform training 的思想 |
34	| 5 | **Dynamic Loss-Based Sample Reweighting for Improved LLM Pretraining** (Wang et al.) | 2025 | ICLR | 在 LLM pretraining 中做 instance-level dynamic reweighting（基于 loss 值在线调整权重），提出 LinUpper / Quadratic 等策略 | 最直接的对比工作之一——他们基于 loss 做 weighting，我们基于 provenance 做 weighting。两者可组合：先用 provenance weight 再用 loss-based dynamic adjustment |
35	| 6 | **DoReMi** (Xie et al., 2023, 见第 1 节) | 2023 | NeurIPS | Domain-level reweighting via Group DRO | 我们做 instance-level provenance weighting，DoReMi 做 domain-level mixture optimization——粒度和信号来源不同 |
36	
37	## 4. Theoretical Analysis of Data Mixing / Contamination
38	
39	| # | 论文 | 年份 | 场所 | 一句话 Contribution | 与我们的关系 |
40	|---|------|------|------|-------------------|------------|
41	| 1 | **AI Models Collapse When Trained on Recursively Generated Data** (Shumailov, Shumaylov, Zhao, Papernot, Anderson, Gal) | 2024 | Nature | 提出 model collapse 概念：在 synthetic data 上迭代训练导致分布尾部丢失和性能退化，在 VAE / GMM / LLM 上验证 | 我们工作的核心 motivation——Shumailov 证明了 synthetic contamination 的危害，我们提出用 provenance weighting 来缓解而非完全过滤 |
42	| 2 | **Strong Model Collapse** (Dohmatob, Feng, Subramonian, Kempe) | 2025 | ICLR | 证明即使极小比例的 synthetic data（1/1000）也会导致 model collapse；用 operator-valued free probability theory 给出 bias-variance 分解 | 强化了 motivation——即使少量 synthetic data 也有害，说明我们的 provenance weighting 方法的必要性：不能靠 "少量就没事" 来忽视 |
43	| 3 | **Is Model Collapse Inevitable? Breaking the Curse of Recursion by Accumulating Real and Synthetic Data** (Gerstgrasser, Schaeffer et al.) | 2024 | COLM | 证明如果 accumulate（而非 replace）数据，model collapse 可以避免；在 linear model 下证明 test error 有有限上界 | 与我们的方法互补——他们说 "保留 real data 可以救"，我们说 "对 synthetic data 降权也可以救"，都是 mitigate 而非 discard 的思路 |
44	| 4 | **How Bad is Training on Synthetic Data? A Statistical Analysis of Language Model Collapse** (Seddik, Chen, Hayou, Youssef, Debbah) | 2024 | COLM | 给出 recursive training 的统计模型，证明纯 synthetic 训练不可避免 collapse，但 real + synthetic 混合训练在 synthetic 比例低于阈值时可避免 | 直接相关——他们给出了 synthetic data 比例的阈值分析，我们的 α_eff 理论可以看作这类阈值分析的推广（从 hard threshold 到 soft weighting） |
45	| 5 | **Data Mixing Laws: Optimizing Data Mixtures by Predicting Language Modeling Performance** (Ye, Liu, Sun, Zhan, Zhou, Qiu) | 2025 | ICLR | 发现 domain mixture proportion 和 model performance 之间存在可预测的函数关系（data mixing laws），可以用小规模实验预测大模型表现 | Data mixing laws 可用于预测不同 provenance weight 设置下的 model performance——我们的 Grid-b 搜索可以理论上用 mixing laws 来加速 |
46	| 6 | **Scaling Data-Constrained Language Models** (Muennighoff et al., 2023, 见第 1 节) | 2023 | NeurIPS | 数据受限下的 scaling law，重复 ≤4 epochs 影响可忽略 | 提供了数据受限场景的理论框架，我们的 α_eff 分析在此基础上进一步考虑了 contamination 的影响 |
47	
48	## Key Observations
49	
50	### 与现有工作的主要区别
51	
52	1. **Data selection vs. data weighting**: 多数现有方法（DSIR, FineWeb-Edu, D4）做 hard selection（保留或丢弃），我们做 soft weighting（降权但不丢弃），保留了更多数据多样性和信息。
53	2. **Quality-based vs. provenance-based**: QuRating / FineWeb-Edu 基于 "质量" 评分，我们基于 "来源"（是否 synthetic）评分——这是正交的信号维度，可以组合使用。
54	3. **Detection for filtering vs. detection for weighting**: 现有 synthetic text detection 工作（DetectGPT, Binoculars）几乎全部用于 binary filtering 或人工审核，我们首次将 calibrated detection score 用于 continuous training weight，对检测器的 calibration（ECE）提出了新要求。
55	4. **Analytic weight function vs. learned weights**: 与 meta-learning reweighting（L2RW, Meta-Weight-Net）相比，我们的 weight = 1 - q^b 是 closed-form，无需 clean validation set 或 meta-optimization，更高效透明。
56	
57	### 最直接的竞争对手 / 对比工作
58	
59	- **Dynamic Loss-Based Sample Reweighting (Wang et al., ICLR 2025)**: 同为 instance-level reweighting for LLM pretraining，但信号来源不同（loss vs. provenance）。
60	- **DoReMi (Xie et al., NeurIPS 2023)**: Domain-level reweighting，粒度不同但目标相似。
61	- **FineWeb-Edu filtering**: 最接近的 "data quality" 竞品，但是 hard filtering 不是 soft weighting。
62	
63	### 潜在的引用遗漏风险
64	
65	- **Ghostbuster** (Verma et al., 2024): 另一个 feature-based synthetic text detector，可能需要作为 detection baseline 引用 [需确认场所]
66	- **GPTZero**: 商业工具，学术论文 (2025 arXiv) 可作为检测方法的 context 引用 [需确认]
67	- **Self-play fine-tuning / synthetic data augmentation 文献**: 我们的工作假设 synthetic data 有害，但有大量文献证明 synthetic data 在 fine-tuning 中有益——需要在 related work 中 acknowledge 并区分 pretraining contamination vs. fine-tuning augmentation 的不同场景
68	- **Distributionally robust optimization (DRO) 基础文献**: Sagawa et al. (2020) Group DRO 等，作为 DoReMi 的理论基础可能需要提及
69	- **Data influence / data attribution 文献**: TracIn, influence functions 等，虽然不是直接竞品但在 "understanding data's effect on training" 的大框架下相关
70	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "0a05528b-d05d-4fb3-947f-20e0adce1e25",
  "uuid": "4675be58-41b0-4187-bb3a-dedaabe3c46d",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/related_work_notes.md",
      "content": "# Related Work Survey — Provenance Weight Training\n\n## 1. Data Quality / Data Selection for LLM Pretraining\n\n| # | 论文 | 年份 | 场所 | 一句话 Contribution | 与我们的关系 |\n|---|------|------|------|-------------------|------------|\n| 1 | **DSIR: Data Selection for Language Models via Importance Resampling** (Xie, Santurkar, Ma, Liang) | 2023 | NeurIPS | 用 hashed n-gram 特征估计 importance weight，对大规模语料做 importance resampling 来匹配目标分布 | DSIR 按目标分布做 selection，我们按 provenance 做 weighting——都用 lightweight feature 做数据筛选，但动机不同：DSIR 优化 domain match，我们降低 synthetic contamination |\n| 2 | **QuRating: Selecting High-Quality Data for Training Language Models** (Wettig, Gupta, Malik, Chen) | 2024 | ICML | 用 LLM pairwise judgment 对数据做 4 维质量评分（writing style / expertise / facts / educational value），训练 QuRater 模型标注 260B 语料 | QuRating 用 LLM 判断 \"质量\"，我们用检测器判断 \"来源\"——都是 model-based annotation + downstream reweighting，但 quality 和 provenance 是正交维度 |\n| 3 | **The FineWeb Datasets: Decanting the Web for the Finest Text Data at Scale** (Penedo et al., HuggingFace) | 2024 | arXiv | 用 Llama-3-70B 合成标注训练 educational quality classifier，过滤出 1.3T token 的 FineWeb-Edu，在 MMLU/ARC 上大幅领先 | FineWeb-Edu 用 LLM-based classifier 做 hard filtering（保留/丢弃），我们用 detector 做 soft weighting（降权不丢弃），保留更多数据多样性 |\n| 4 | **D4: Improving LLM Pretraining via Document De-Duplication and Diversification** (Tirumala, Simig et al.) | 2023 | NeurIPS D&B | 用 pretrained embedding + K-Means 做去重和多样性平衡，6.7B 模型上提升 2% 下游准确率和 20% 训练效率 | D4 关注重复和多样性，我们关注 synthetic contamination——互补方法，可以先 D4 去重再用我们的 provenance weighting |\n| 5 | **DoReMi: Optimizing Data Mixtures Speeds Up Language Model Pretraining** (Xie, Pham et al.) | 2023 | NeurIPS | 用 Group DRO 在 proxy model 上优化 domain mixture weights，无需下游任务信息，8B 模型提升 6.5% few-shot 准确率 | DoReMi 做 domain-level reweighting（按 domain 调权），我们做 instance-level reweighting（按 q-score 调权）——粒度不同，理论上可以组合使用 |\n| 6 | **DataComp-LM (DCLM): In Search of the Next Generation of Training Sets for Language Models** (Li et al.) | 2024 | NeurIPS D&B | 提供 240T token 标准化语料 + 评估套件，系统性对比 data curation 策略，证明 model-based filtering 是关键 | DCLM 是 benchmark 框架，我们的 provenance-based weighting 可以作为一种新的 curation strategy 在 DCLM 上评估 |\n| 7 | **Scaling Data-Constrained Language Models** (Muennighoff, Rush et al.) | 2023 | NeurIPS | 系统研究数据受限时的 scaling law，发现 ≤4 epochs 重复数据对 loss 影响可忽略，提出考虑重复衰减的 compute-optimal law | 当 unique data 不足时更可能混入 synthetic data 来补量——我们的方法提供了一种替代方案：不用丢弃 synthetic data，而是降权使用 |\n\n## 2. Synthetic Data Contamination Detection\n\n| # | 论文 | 年份 | 场所 | 一句话 Contribution | 与我们的关系 |\n|---|------|------|------|-------------------|------------|\n| 1 | **DetectGPT: Zero-Shot Machine-Generated Text Detection using Probability Curvature** (Mitchell et al.) | 2023 | ICML | 零样本检测：用 log probability curvature（在 perturbation 前后的 log-prob 变化）区分 human vs machine text，无需训练分类器 | DetectGPT 做 binary detection（是否机器生成），我们需要 calibrated probability（q-score）——我们选择 TF-IDF + LogReg 正是因为需要 well-calibrated 的连续 score 而非仅 binary 判断 |\n| 2 | **Fast-DetectGPT: Efficient Zero-Shot Detection via Conditional Probability Curvature** (Bao et al.) | 2024 | ICLR | 将 DetectGPT 的 perturbation 步骤替换为 sampling，加速 340 倍且 AUROC 提升约 75% | 同上——更高效但仍是 binary detection，calibration 质量（ECE）未被重点评估，而这正是我们工作的核心关注点 |\n| 3 | **Binoculars: Zero-Shot Detection of LLM-Generated Text** (Hans et al.) | 2024 | ICML | 用两个 LLM 的 perplexity / cross-perplexity 比值做检测，ChatGPT 文本在 0.01% FPR 下召回 >90% | Binoculars 需要两个 LLM 推理，计算成本高；我们的 TF-IDF + LogReg 检测器极轻量，适合标注数十亿 token 级别的 pretraining corpus |\n| 4 | **GLTR: Statistical Detection and Visualization of Generated Text** (Gehrmann, Strobelt, Rush) | 2019 | ACL | 用 LM 的 top-k token 排名做统计检测和可视化，帮助人类识别机器文本（人类检测率从 54% 提升到 72%） | 早期 statistical detection 工作，启发了后续基于 model statistics 的方法；我们的方法同样基于统计特征但目标不同（scoring for weighting 而非 human-in-the-loop detection） |\n| 5 | **A Watermark for Large Language Models** (Kirchenbauer et al.) | 2023 | ICML | 在生成时嵌入 statistical watermark（green/red token list），可用 p-value 统计检验来检测 | Watermarking 需要控制生成过程，无法检测已有的、未 watermarked 的 synthetic data——我们的场景是 post-hoc detection on existing corpus |\n| 6 | **A Survey on LLM-Generated Text Detection: Necessity, Methods, and Future Directions** (Wu et al.) | 2024 | Computational Linguistics (MIT Press) | 系统综述 statistical / neural / watermarking 三类检测方法，讨论 robustness 和 generalization | 综述文献，帮助定位我们的检测器在整个 detection 方法谱系中的位置——我们是 training-based statistical classifier，但用于 weighting 而非 filtering |\n\n## 3. Sample Reweighting in Training\n\n| # | 论文 | 年份 | 场所 | 一句话 Contribution | 与我们的关系 |\n|---|------|------|------|-------------------|------------|\n| 1 | **Improving the Accuracy of Likelihood-based Inference under Covariate Shift** (Shimodaira) | 2000 | JASA | 奠基性工作：提出 importance weighted ERM（IWERM），通过 density ratio 修正 covariate shift 下的 loss | 理论基础直接相关——我们的 weight = 1 - q^b 可以看作一种 bounded importance weight，Shimodaira 的 IWERM 理论为我们的方法提供了正当性 |\n| 2 | **Learning to Reweight Examples for Robust Deep Learning** (Ren, Zeng, Yang, Urtasun) | 2018 | ICML | 用 meta-learning 在训练中动态学习 sample weights（基于 gradient direction 在 clean validation set 上的表现） | L2RW 需要 clean validation set 做 meta-optimization，我们的方法不需要——weight 由 provenance detector 预先确定，无需在训练中迭代调整 |\n| 3 | **Meta-Weight-Net: Learning an Explicit Mapping For Sample Weighting** (Shu et al.) | 2019 | NeurIPS | 用 MLP 学习 loss → weight 的显式映射函数，在 noisy label 和 class imbalance 场景下优于手工设计的 weighting | 与 L2RW 类似用 meta-learning；我们的 weight function 是 analytic form（1 - q^b），不需要 meta-learning，更透明可解释 |\n| 4 | **Curriculum Learning** (Bengio, Louradour, Collobert, Weston) | 2009 | ICML | 奠基性工作：证明按从易到难的顺序训练（curriculum）可以加速收敛并改善 non-convex optimization 的局部极小值 | Curriculum learning 按难度排序，我们按 provenance 加权——虽然形式不同（排序 vs 加权），但都是 non-uniform training 的思想 |\n| 5 | **Dynamic Loss-Based Sample Reweighting for Improved LLM Pretraining** (Wang et al.) | 2025 | ICLR | 在 LLM pretraining 中做 instance-level dynamic reweighting（基于 loss 值在线调整权重），提出 LinUpper / Quadratic 等策略 | 最直接的对比工作之一——他们基于 loss 做 weighting，我们基于 provenance 做 weighting。两者可组合：先用 provenance weight 再用 loss-based dynamic adjustment |\n| 6 | **DoReMi** (Xie et al., 2023, 见第 1 节) | 2023 | NeurIPS | Domain-level reweighting via Group DRO | 我们做 instance-level provenance weighting，DoReMi 做 domain-level mixture optimization——粒度和信号来源不同 |\n\n## 4. Theoretical Analysis of Data Mixing / Contamination\n\n| # | 论文 | 年份 | 场所 | 一句话 Contribution | 与我们的关系 |\n|---|------|------|------|-------------------|------------|\n| 1 | **AI Models Collapse When Trained on Recursively Generated Data** (Shumailov, Shumaylov, Zhao, Papernot, Anderson, Gal) | 2024 | Nature | 提出 model collapse 概念：在 synthetic data 上迭代训练导致分布尾部丢失和性能退化，在 VAE / GMM / LLM 上验证 | 我们工作的核心 motivation——Shumailov 证明了 synthetic contamination 的危害，我们提出用 provenance weighting 来缓解而非完全过滤 |\n| 2 | **Strong Model Collapse** (Dohmatob, Feng, Subramonian, Kempe) | 2025 | ICLR | 证明即使极小比例的 synthetic data（1/1000）也会导致 model collapse；用 operator-valued free probability theory 给出 bias-variance 分解 | 强化了 motivation——即使少量 synthetic data 也有害，说明我们的 provenance weighting 方法的必要性：不能靠 \"少量就没事\" 来忽视 |\n| 3 | **Is Model Collapse Inevitable? Breaking the Curse of Recursion by Accumulating Real and Synthetic Data** (Gerstgrasser, Schaeffer et al.) | 2024 | COLM | 证明如果 accumulate（而非 replace）数据，model collapse 可以避免；在 linear model 下证明 test error 有有限上界 | 与我们的方法互补——他们说 \"保留 real data 可以救\"，我们说 \"对 synthetic data 降权也可以救\"，都是 mitigate 而非 discard 的思路 |\n| 4 | **How Bad is Training on Synthetic Data? A Statistical Analysis of Language Model Collapse** (Seddik, Chen, Hayou, Youssef, Debbah) | 2024 | COLM | 给出 recursive training 的统计模型，证明纯 synthetic 训练不可避免 collapse，但 real + synthetic 混合训练在 synthetic 比例低于阈值时可避免 | 直接相关——他们给出了 synthetic data 比例的阈值分析，我们的 α_eff 理论可以看作这类阈值分析的推广（从 hard threshold 到 soft weighting） |\n| 5 | **Data Mixing Laws: Optimizing Data Mixtures by Predicting Language Modeling Performance** (Ye, Liu, Sun, Zhan, Zhou, Qiu) | 2025 | ICLR | 发现 domain mixture proportion 和 model performance 之间存在可预测的函数关系（data mixing laws），可以用小规模实验预测大模型表现 | Data mixing laws 可用于预测不同 provenance weight 设置下的 model performance——我们的 Grid-b 搜索可以理论上用 mixing laws 来加速 |\n| 6 | **Scaling Data-Constrained Language Models** (Muennighoff et al., 2023, 见第 1 节) | 2023 | NeurIPS | 数据受限下的 scaling law，重复 ≤4 epochs 影响可忽略 | 提供了数据受限场景的理论框架，我们的 α_eff 分析在此基础上进一步考虑了 contamination 的影响 |\n\n## Key Observations\n\n### 与现有工作的主要区别\n\n1. **Data selection vs. data weighting**: 多数现有方法（DSIR, FineWeb-Edu, D4）做 hard selection（保留或丢弃），我们做 soft weighting（降权但不丢弃），保留了更多数据多样性和信息。\n2. **Quality-based vs. provenance-based**: QuRating / FineWeb-Edu 基于 \"质量\" 评分，我们基于 \"来源\"（是否 synthetic）评分——这是正交的信号维度，可以组合使用。\n3. **Detection for filtering vs. detection for weighting**: 现有 synthetic text detection 工作（DetectGPT, Binoculars）几乎全部用于 binary filtering 或人工审核，我们首次将 calibrated detection score 用于 continuous training weight，对检测器的 calibration（ECE）提出了新要求。\n4. **Analytic weight function vs. learned weights**: 与 meta-learning reweighting（L2RW, Meta-Weight-Net）相比，我们的 weight = 1 - q^b 是 closed-form，无需 clean validation set 或 meta-optimization，更高效透明。\n\n### 最直接的竞争对手 / 对比工作\n\n- **Dynamic Loss-Based Sample Reweighting (Wang et al., ICLR 2025)**: 同为 instance-level reweighting for LLM pretraining，但信号来源不同（loss vs. provenance）。\n- **DoReMi (Xie et al., NeurIPS 2023)**: Domain-level reweighting，粒度不同但目标相似。\n- **FineWeb-Edu filtering**: 最接近的 \"data quality\" 竞品，但是 hard filtering 不是 soft weighting。\n\n### 潜在的引用遗漏风险\n\n- **Ghostbuster** (Verma et al., 2024): 另一个 feature-based synthetic text detector，可能需要作为 detection baseline 引用 [需确认场所]\n- **GPTZero**: 商业工具，学术论文 (2025 arXiv) 可作为检测方法的 context 引用 [需确认]\n- **Self-play fine-tuning / synthetic data augmentation 文献**: 我们的工作假设 synthetic data 有害，但有大量文献证明 synthetic data 在 fine-tuning 中有益——需要在 related work 中 acknowledge 并区分 pretraining contamination vs. fine-tuning augmentation 的不同场景\n- **Distributionally robust optimization (DRO) 基础文献**: Sagawa et al. (2020) Group DRO 等，作为 DoReMi 的理论基础可能需要提及\n- **Data influence / data attribution 文献**: TracIn, influence functions 等，虽然不是直接竞品但在 \"understanding data's effect on training\" 的大框架下相关\n",
      "numLines": 70,
      "startLine": 1,
      "totalLines": 70
    }
  }
}
```

</details>

---

### Tool call

_source line 7_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01UU37PEmHC1kwWERFw4Q1mB`</summary>

```json
{
  "query": "select:WebSearch",
  "max_results": 1
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "0a05528b-d05d-4fb3-947f-20e0adce1e25",
  "uuid": "78d51a34-4e6c-45df-89dc-bf51bb6fcdf0",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Mb7WnajvbE6ejeq1WVc3WW",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 11842,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 11842
      },
      "output_tokens": 2,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-14T12:31:38.524Z_

<details><summary>↩ Tool result · `toolu_01UU37PEmHC1kwWERFw4Q1mB`</summary>

````text
```json
{
  "type": "tool_reference",
  "tool_name": "WebSearch"
}
```
````

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "0a05528b-d05d-4fb3-947f-20e0adce1e25",
  "uuid": "6d8818ff-3c7f-4909-bd3b-609c9ee886ef",
  "tool_use_result": {
    "matches": [
      "WebSearch"
    ],
    "query": "select:WebSearch",
    "total_deferred_tools": 22
  }
}
```

</details>

---

### Assistant

_source line 9_

<details><summary>Logged reasoning block</summary>

```text
Now I have the current survey file and the WebSearch tool. Let me search for the two papers and the five pending items in parallel.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "0a05528b-d05d-4fb3-947f-20e0adce1e25",
  "uuid": "3a7c4f11-d583-44ac-b450-1a09846e21b6",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01H3TdrebvrPk9fFdEmkGz5X",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 5673,
      "cache_read_input_tokens": 23683,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 5673
      },
      "output_tokens": 24,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Assistant

_source line 10_

Now let me search for all the papers in parallel.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "0a05528b-d05d-4fb3-947f-20e0adce1e25",
  "uuid": "1d775573-d41e-4692-8c87-b125629e7889",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01H3TdrebvrPk9fFdEmkGz5X",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 5673,
      "cache_read_input_tokens": 23683,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 5673
      },
      "output_tokens": 24,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool call

_source line 11_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01BCUdo7qeNAWDrpab89jT2G`</summary>

```json
{
  "query": "Drayson EMNLP 2025 detect reweight synthetic data"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "0a05528b-d05d-4fb3-947f-20e0adce1e25",
  "uuid": "2d3b9637-e3ba-4877-9028-206b0a49b23a",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01H3TdrebvrPk9fFdEmkGz5X",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 5673,
      "cache_read_input_tokens": 23683,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 5673
      },
      "output_tokens": 24,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool call

_source line 12_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01R5NH6oGjEfEfvsW2tsp6XN`</summary>

```json
{
  "query": "arxiv 2602.16065"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "0a05528b-d05d-4fb3-947f-20e0adce1e25",
  "uuid": "6dfb92ea-e2e4-45f8-951d-f053fecb779d",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01H3TdrebvrPk9fFdEmkGz5X",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 5673,
      "cache_read_input_tokens": 23683,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 5673
      },
      "output_tokens": 24,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool call

_source line 13_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01ErVKf4sR1Nmuhkg3rptwC5`</summary>

```json
{
  "query": "Ghostbuster Verma 2024 synthetic text detection"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "0a05528b-d05d-4fb3-947f-20e0adce1e25",
  "uuid": "2928c39a-d6cd-44d9-8324-323d14fda3f7",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01H3TdrebvrPk9fFdEmkGz5X",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 5673,
      "cache_read_input_tokens": 23683,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 5673
      },
      "output_tokens": 24,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool call

_source line 14_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01Js6zE1muSbqrZTfoTKkJE4`</summary>

```json
{
  "query": "GPTZero academic paper 2024 2025 machine text detection"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "0a05528b-d05d-4fb3-947f-20e0adce1e25",
  "uuid": "b7359037-e4c3-4f39-bc77-78d37c1666aa",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01H3TdrebvrPk9fFdEmkGz5X",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 5673,
      "cache_read_input_tokens": 23683,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 5673
      },
      "output_tokens": 24,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool call

_source line 15_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01FnN1hVDnTnU7xZPYdrr2RX`</summary>

```json
{
  "query": "Group DRO Sagawa 2020 distributionally robust optimization"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "0a05528b-d05d-4fb3-947f-20e0adce1e25",
  "uuid": "4461b4fe-6719-4e9c-b28b-5c403409b73b",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01H3TdrebvrPk9fFdEmkGz5X",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 5673,
      "cache_read_input_tokens": 23683,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 5673
      },
      "output_tokens": 24,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-14T12:31:48.963Z_

<details><summary>↩ Tool result · `toolu_01R5NH6oGjEfEfvsW2tsp6XN`</summary>

```text
Web search results for query: "arxiv 2602.16065"

Links: [{"title":"[2602.16065] Can Generative Artificial Intelligence Survive Data Contamination? Theoretical Guarantees under Contaminated Recursive Training","url":"https://arxiv.org/abs/2602.16065"},{"title":"Can Generative Artificial Intelligence Survive Data Contamination? Theoretical Guarantees under Contaminated Recursive Training","url":"https://arxiv.org/html/2602.16065"},{"title":"[2604.16065] Phase transitions in microbial lineage trees","url":"https://arxiv.org/abs/2604.16065"},{"title":"Large Reward Models: Generalizable Online Robot Reward Generation with Vision-Language Models","url":"https://arxiv.org/html/2603.16065"},{"title":"[2504.16065] A Mysterious Connection Between Tolerant Junta Testing and Agnostically Learning Conjunctions","url":"https://arxiv.org/abs/2504.16065"},{"title":"[2509.16065] Complexity of the Freezing Majority Rule with L-shaped Neighborhoods","url":"https://arxiv.org/abs/2509.16065"},{"title":"[2502.16065] A Survey of Model Extraction Attacks and Defenses in Distributed Computing Environments","url":"https://arxiv.org/abs/2502.16065"},{"title":"Simple, highly-stable transfer cavity for laser stabilization based on a carbon-fiber reinforced polymer spacer","url":"https://arxiv.org/html/2409.16065"},{"title":"Complexity of the Freezing Majority Rule with L-shaped Neighborhoods","url":"https://arxiv.org/pdf/2509.16065"},{"title":"arXiv:2502.16065v1 [cs.CR] 22 Feb 2025","url":"https://arxiv.org/pdf/2502.16065"}]

Based on the search results, arXiv paper 2602.16065 is titled "Can Generative Artificial Intelligence Survive Data Contamination? Theoretical Guarantees under Contaminated Recursive Training".

The paper examines how generative AI systems like large language models are increasingly trained on mixtures of human-generated data and AI-generated data from earlier versions through recursive training processes with data contamination. Existing theoretical work has examined only simplified settings with discrete or Gaussian data, which has shown that such recursive training leads to model collapse. However, the paper notes that real data distributions are far more complex, and modern generative models are far more flexible than Gaussian and linear mechanisms.

The paper was published on February 17, 2026.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "0a05528b-d05d-4fb3-947f-20e0adce1e25",
  "uuid": "d5c6dd4f-a191-4481-abfd-79e6bd6cd23c",
  "tool_use_result": {
    "query": "arxiv 2602.16065",
    "results": [
      {
        "tool_use_id": "srvtoolu_01Xeg2rnaJghSnV9127UZrM5",
        "content": [
          {
            "title": "[2602.16065] Can Generative Artificial Intelligence Survive Data Contamination? Theoretical Guarantees under Contaminated Recursive Training",
            "url": "https://arxiv.org/abs/2602.16065"
          },
          {
            "title": "Can Generative Artificial Intelligence Survive Data Contamination? Theoretical Guarantees under Contaminated Recursive Training",
            "url": "https://arxiv.org/html/2602.16065"
          },
          {
            "title": "[2604.16065] Phase transitions in microbial lineage trees",
            "url": "https://arxiv.org/abs/2604.16065"
          },
          {
            "title": "Large Reward Models: Generalizable Online Robot Reward Generation with Vision-Language Models",
            "url": "https://arxiv.org/html/2603.16065"
          },
          {
            "title": "[2504.16065] A Mysterious Connection Between Tolerant Junta Testing and Agnostically Learning Conjunctions",
            "url": "https://arxiv.org/abs/2504.16065"
          },
          {
            "title": "[2509.16065] Complexity of the Freezing Majority Rule with L-shaped Neighborhoods",
            "url": "https://arxiv.org/abs/2509.16065"
          },
          {
            "title": "[2502.16065] A Survey of Model Extraction Attacks and Defenses in Distributed Computing Environments",
            "url": "https://arxiv.org/abs/2502.16065"
          },
          {
            "title": "Simple, highly-stable transfer cavity for laser stabilization based on a carbon-fiber reinforced polymer spacer",
            "url": "https://arxiv.org/html/2409.16065"
          },
          {
            "title": "Complexity of the Freezing Majority Rule with L-shaped Neighborhoods",
            "url": "https://arxiv.org/pdf/2509.16065"
          },
          {
            "title": "arXiv:2502.16065v1 [cs.CR] 22 Feb 2025",
            "url": "https://arxiv.org/pdf/2502.16065"
          }
        ]
      },
      "Based on the search results, arXiv paper 2602.16065 is titled \"Can Generative Artificial Intelligence Survive Data Contamination? Theoretical Guarantees under Contaminated Recursive Training\".\n\nThe paper examines how generative AI systems like large language models are increasingly trained on mixtures of human-generated data and AI-generated data from earlier versions through recursive training processes with data contamination. Existing theoretical work has examined only simplified settings with discrete or Gaussian data, which has shown that such recursive training leads to model collapse. However, the paper notes that real data distributions are far more complex, and modern generative models are far more flexible than Gaussian and linear mechanisms.\n\nThe paper was published on February 17, 2026."
    ],
    "durationSeconds": 4.47821363
  }
}
```

</details>

---

### Tool result

_source line 17 · 2026-05-14T12:31:49.875Z_

<details><summary>↩ Tool result · `toolu_01BCUdo7qeNAWDrpab89jT2G`</summary>

```text
Web search results for query: "Drayson EMNLP 2025 detect reweight synthetic data"

Links: [{"title":"Demystifying Synthetic Data in LLM Pre-training","url":"https://aclanthology.org/2025.emnlp-main.544.pdf"},{"title":"Accepted System Demonstrations Papers - EMNLP 2025","url":"https://2025.emnlp.org/program/demo_papers/"},{"title":"Scaling Low-Resource MT via Synthetic Data Generation ...","url":"https://aclanthology.org/2025.emnlp-main.1408.pdf"},{"title":"Demystifying Synthetic Data in LLM Pre-training: A Systematic Study of Scaling Laws, Benefits, and Pitfalls - ACL Anthology","url":"https://aclanthology.org/2025.emnlp-main.544/"},{"title":"Synthetic Text Data Generation and Evaluation for High- ...","url":"https://aclanthology.org/2025.emnlp-demos.35.pdf"},{"title":"GitHub - pengr/LLM-Synthetic-Data: A live reading list for LLM data synthesis (Updated to July, 2025). · GitHub","url":"https://github.com/pengr/LLM-Synthetic-Data"},{"title":"Demystifying Synthetic Data in LLM Pre-training: A Systematic Study of Scaling Laws, Benefits, and Pitfalls | Cool Papers - Immersive Paper Discovery","url":"https://papers.cool/venue/2025.emnlp-main.544@ACL"},{"title":"Exploring Quality and Diversity in Synthetic Data ...","url":"https://aclanthology.org/2025.emnlp-main.1351.pdf"},{"title":"Synthetic Data for Evaluation: Supporting LLM-as-a-Judge Workflows with EvalAssist for EMNLP 2025 - IBM Research","url":"https://research.ibm.com/publications/synthetic-data-for-evaluation-supporting-llm-as-a-judge-workflows-with-evalassist"},{"title":"Synthetic Data in LLM Pre-Training","url":"https://www.emergentmind.com/papers/2510.01631"}]

I searched for the query "Drayson EMNLP 2025 detect reweight synthetic data" but the search results don't appear to contain a paper specifically by "Drayson" at EMNLP 2025 about detecting and reweighting synthetic data. 

The search results show several papers about synthetic data from EMNLP 2025, including:
- "Demystifying Synthetic Data in LLM Pre-training" by Kang et al.
- "SynthTextEval: Synthetic Text Data Generation and Evaluation" 
- Papers on synthetic data quality and diversity

However, none of these appear to match the specific "Drayson" paper you're looking for. It's possible that:
1. The author's name might be spelled differently
2. The paper might use different keywords in its title
3. The paper might not have been published at EMNLP 2025

Could you provide additional details about this paper, such as:
- The full author name(s)?
- Alternative keywords or phrases from the title?
- Whether it was a main conference paper or a different venue?

This would help me locate the specific research you're interested in.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "0a05528b-d05d-4fb3-947f-20e0adce1e25",
  "uuid": "19d18c21-2dfd-4ed9-80e5-6c0dc6da630c",
  "tool_use_result": {
    "query": "Drayson EMNLP 2025 detect reweight synthetic data",
    "results": [
      {
        "tool_use_id": "srvtoolu_01JUzWwzpPFcUQv7uTqbvABg",
        "content": [
          {
            "title": "Demystifying Synthetic Data in LLM Pre-training",
            "url": "https://aclanthology.org/2025.emnlp-main.544.pdf"
          },
          {
            "title": "Accepted System Demonstrations Papers - EMNLP 2025",
            "url": "https://2025.emnlp.org/program/demo_papers/"
          },
          {
            "title": "Scaling Low-Resource MT via Synthetic Data Generation ...",
            "url": "https://aclanthology.org/2025.emnlp-main.1408.pdf"
          },
          {
            "title": "Demystifying Synthetic Data in LLM Pre-training: A Systematic Study of Scaling Laws, Benefits, and Pitfalls - ACL Anthology",
            "url": "https://aclanthology.org/2025.emnlp-main.544/"
          },
          {
            "title": "Synthetic Text Data Generation and Evaluation for High- ...",
            "url": "https://aclanthology.org/2025.emnlp-demos.35.pdf"
          },
          {
            "title": "GitHub - pengr/LLM-Synthetic-Data: A live reading list for LLM data synthesis (Updated to July, 2025). · GitHub",
            "url": "https://github.com/pengr/LLM-Synthetic-Data"
          },
          {
            "title": "Demystifying Synthetic Data in LLM Pre-training: A Systematic Study of Scaling Laws, Benefits, and Pitfalls | Cool Papers - Immersive Paper Discovery",
            "url": "https://papers.cool/venue/2025.emnlp-main.544@ACL"
          },
          {
            "title": "Exploring Quality and Diversity in Synthetic Data ...",
            "url": "https://aclanthology.org/2025.emnlp-main.1351.pdf"
          },
          {
            "title": "Synthetic Data for Evaluation: Supporting LLM-as-a-Judge Workflows with EvalAssist for EMNLP 2025 - IBM Research",
            "url": "https://research.ibm.com/publications/synthetic-data-for-evaluation-supporting-llm-as-a-judge-workflows-with-evalassist"
          },
          {
            "title": "Synthetic Data in LLM Pre-Training",
            "url": "https://www.emergentmind.com/papers/2510.01631"
          }
        ]
      },
      "I searched for the query \"Drayson EMNLP 2025 detect reweight synthetic data\" but the search results don't appear to contain a paper specifically by \"Drayson\" at EMNLP 2025 about detecting and reweighting synthetic data. \n\nThe search results show several papers about synthetic data from EMNLP 2025, including:\n- \"Demystifying Synthetic Data in LLM Pre-training\" by Kang et al.\n- \"SynthTextEval: Synthetic Text Data Generation and Evaluation\" \n- Papers on synthetic data quality and diversity\n\nHowever, none of these appear to match the specific \"Drayson\" paper you're looking for. It's possible that:\n1. The author's name might be spelled differently\n2. The paper might use different keywords in its title\n3. The paper might not have been published at EMNLP 2025\n\nCould you provide additional details about this paper, such as:\n- The full author name(s)?\n- Alternative keywords or phrases from the title?\n- Whether it was a main conference paper or a different venue?\n\nThis would help me locate the specific research you're interested in."
    ],
    "durationSeconds": 5.8626152220000005
  }
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-14T12:31:51.302Z_

<details><summary>↩ Tool result · `toolu_01ErVKf4sR1Nmuhkg3rptwC5`</summary>

```text
Web search results for query: "Ghostbuster Verma 2024 synthetic text detection"

Links: [{"title":"Ghostbuster: Detecting Text Ghostwritten by Large Language Models - ACL Anthology","url":"https://aclanthology.org/2024.naacl-long.95/"},{"title":"Ghostbuster: Detecting Text Ghostwritten by Large Language Models Vivek Verma","url":"https://nlp.cs.berkeley.edu/pubs/Verma-Fleisig-Tomlin-Klein_2024_Ghostbuster_paper.pdf"},{"title":"[2305.15047] Ghostbuster: Detecting Text Ghostwritten by Large Language Models","url":"https://arxiv.org/abs/2305.15047"},{"title":"Ghostbuster: Detecting Text Ghostwritten by Large Language Models","url":"https://arxiv.org/html/2305.15047v3"},{"title":"Detecting Text Ghostwritten by Large Language Models","url":"https://aclanthology.org/2024.naacl-long.95.pdf"},{"title":"Ghostbuster: Detecting Text Ghostwritten by Large Language Models – The Berkeley Artificial Intelligence Research Blog","url":"https://bair.berkeley.edu/blog/2023/11/14/ghostbuster/"},{"title":"GitHub - vivek3141/ghostbuster: Ghostbuster: Detecting Text Ghostwritten by Large Language Models (NAACL 2024) · GitHub","url":"https://github.com/vivek3141/ghostbuster"},{"title":"Ghostbuster: Detecting Text Ghostwritten by Large Language Models | AI Research Paper Details","url":"https://www.aimodels.fyi/papers/arxiv/ghostbuster-detecting-text-ghostwritten-by-large-language"},{"title":"[2305.15047v1] Ghostbuster: Detecting Text Ghostwritten by Large Language Models","url":"https://arxiv.org/abs/2305.15047v1"},{"title":"Ghostbuster: Detecting Text Ghostwritten by Large Language Models | OpenReview","url":"https://openreview.net/forum?id=XnyZfCerSX"}]

Based on the search results, here's what I found about Ghostbuster and the Verma 2024 research on synthetic text detection:

## Overview

Ghostbuster is a state-of-the-art system for detecting AI-generated text. The paper was authored by Vivek Verma, Eve Fleisig, Nicholas Tomlin, and Dan Klein and was published in the Proceedings of the 2024 Conference of the North American Chapter of the Association for Computational Linguistics: Human Language Technologies.

## Methodology

The method works by passing documents through a series of weaker language models, running a structured search over possible combinations of their features, and then training a classifier on the selected features to predict whether documents are AI-generated. Crucially, Ghostbuster does not require access to token probabilities from the target model, making it useful for detecting text generated by black-box models or unknown model versions.

## Performance Results

Ghostbuster achieves 99.0 F1 when evaluated across domains, which is 5.9 F1 higher than the best preexisting model. It also outperforms all previous approaches in generalization across writing domains (+7.5 F1), prompting strategies (+2.1 F1), and language models (+4.4 F1).

## Datasets

In conjunction with their model, the researchers released three new datasets of human- and AI-generated text as detection benchmarks in the domains of student essays, creative writing, and news articles.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "0a05528b-d05d-4fb3-947f-20e0adce1e25",
  "uuid": "16a5b834-2f5a-49c2-b9f0-90f2bd289450",
  "tool_use_result": {
    "query": "Ghostbuster Verma 2024 synthetic text detection",
    "results": [
      {
        "tool_use_id": "srvtoolu_01Wt2KKGiSkKJsNNEszNHhs9",
        "content": [
          {
            "title": "Ghostbuster: Detecting Text Ghostwritten by Large Language Models - ACL Anthology",
            "url": "https://aclanthology.org/2024.naacl-long.95/"
          },
          {
            "title": "Ghostbuster: Detecting Text Ghostwritten by Large Language Models Vivek Verma",
            "url": "https://nlp.cs.berkeley.edu/pubs/Verma-Fleisig-Tomlin-Klein_2024_Ghostbuster_paper.pdf"
          },
          {
            "title": "[2305.15047] Ghostbuster: Detecting Text Ghostwritten by Large Language Models",
            "url": "https://arxiv.org/abs/2305.15047"
          },
          {
            "title": "Ghostbuster: Detecting Text Ghostwritten by Large Language Models",
            "url": "https://arxiv.org/html/2305.15047v3"
          },
          {
            "title": "Detecting Text Ghostwritten by Large Language Models",
            "url": "https://aclanthology.org/2024.naacl-long.95.pdf"
          },
          {
            "title": "Ghostbuster: Detecting Text Ghostwritten by Large Language Models – The Berkeley Artificial Intelligence Research Blog",
            "url": "https://bair.berkeley.edu/blog/2023/11/14/ghostbuster/"
          },
          {
            "title": "GitHub - vivek3141/ghostbuster: Ghostbuster: Detecting Text Ghostwritten by Large Language Models (NAACL 2024) · GitHub",
            "url": "https://github.com/vivek3141/ghostbuster"
          },
          {
            "title": "Ghostbuster: Detecting Text Ghostwritten by Large Language Models | AI Research Paper Details",
            "url": "https://www.aimodels.fyi/papers/arxiv/ghostbuster-detecting-text-ghostwritten-by-large-language"
          },
          {
            "title": "[2305.15047v1] Ghostbuster: Detecting Text Ghostwritten by Large Language Models",
            "url": "https://arxiv.org/abs/2305.15047v1"
          },
          {
            "title": "Ghostbuster: Detecting Text Ghostwritten by Large Language Models | OpenReview",
            "url": "https://openreview.net/forum?id=XnyZfCerSX"
          }
        ]
      },
      "Based on the search results, here's what I found about Ghostbuster and the Verma 2024 research on synthetic text detection:\n\n## Overview\n\nGhostbuster is a state-of-the-art system for detecting AI-generated text. The paper was authored by Vivek Verma, Eve Fleisig, Nicholas Tomlin, and Dan Klein and was published in the Proceedings of the 2024 Conference of the North American Chapter of the Association for Computational Linguistics: Human Language Technologies.\n\n## Methodology\n\nThe method works by passing documents through a series of weaker language models, running a structured search over possible combinations of their features, and then training a classifier on the selected features to predict whether documents are AI-generated. Crucially, Ghostbuster does not require access to token probabilities from the target model, making it useful for detecting text generated by black-box models or unknown model versions.\n\n## Performance Results\n\nGhostbuster achieves 99.0 F1 when evaluated across domains, which is 5.9 F1 higher than the best preexisting model. It also outperforms all previous approaches in generalization across writing domains (+7.5 F1), prompting strategies (+2.1 F1), and language models (+4.4 F1).\n\n## Datasets\n\nIn conjunction with their model, the researchers released three new datasets of human- and AI-generated text as detection benchmarks in the domains of student essays, creative writing, and news articles."
    ],
    "durationSeconds": 6.342830267000001
  }
}
```

</details>

---

### Tool result

_source line 19 · 2026-05-14T12:31:53.120Z_

<details><summary>↩ Tool result · `toolu_01Js6zE1muSbqrZTfoTKkJE4`</summary>

```text
Web search results for query: "GPTZero academic paper 2024 2025 machine text detection"

Links: [{"title":"Utilizing GPTZero to Detect AI-Generated Writing","url":"https://files.eric.ed.gov/fulltext/EJ1482073.pdf"},{"title":"GPTZero Review 2025: Accuracy, False Positives & Top Alternatives","url":"https://skywork.ai/blog/gptzero-review-2025/"},{"title":"GPTZero","url":"https://gptzero.me/"},{"title":"Issues in Information Systems Volume 25, Issue 3 pp. 165-174, 2024 165","url":"https://www.iacis.org/iis/2024/3_iis_2024_165-174.pdf"},{"title":"GPTZero Performance in Identifying Artificial Intelligence-Generated Medical Texts: A Preliminary Study - PMC","url":"https://pmc.ncbi.nlm.nih.gov/articles/PMC10519776/"},{"title":"GPTZero Technology - AI Detection","url":"https://gptzero.me/technology"},{"title":"GPTZero's Research Contributions","url":"https://gptzero.me/resources/researchers"},{"title":"Assessing the Effectiveness of AI Detection Tools for Varying Levels of AI-Generated Text | Springer Nature Link","url":"https://link.springer.com/chapter/10.1007/978-3-032-14197-2_27"},{"title":"(PDF) Assessing GPTZero's Accuracy in Identifying AI vs. Human-Written Essays","url":"https://www.researchgate.net/publication/393183923_Assessing_GPTZero's_Accuracy_in_Identifying_AI_vs_Human-Written_Essays"},{"title":"GPTZero - Wikipedia","url":"https://en.wikipedia.org/wiki/GPTZero"}]

Based on the web search results, here are relevant academic papers and findings about GPTZero's machine-generated text detection from 2024-2025:

## Academic Papers

A 2025 paper by Paullet, Pinchot, Kinney, and Stewart titled "Detecting AI-Generated Writing Using GPTZero" was published in the Information Systems Education Journal, volume 23, issue 6, pages 44-52.

Another study tested GPTZero's capabilities for detecting if assignments were written by humans or AI, using a set of 100 samples.

## Recent Technical Research

GPTZero's latest paper, "GPTZero: Robust Detection of LLM-Generated Texts," provides a walkthrough of their detection pipeline including data gathering and QA, hierarchical modeling, robustness evaluation, and explainability methods. The paper frames detection as Human, AI, and Mixed categories with a hierarchical multi-task architecture, and reports state-of-the-art results across domains, languages, and multilabel settings.

## Key Findings on Accuracy

A study found that GPTZero can identify AI-generated texts at around 90-99% accuracy rates. However, academic work in 2025 shows that paraphrasing strategies can drastically reduce detector recall, with a training-free attack presented in June 2025 demonstrating how adversarial paraphrasing can evade detectors widely.

## Limitations and Cautions

One study found that GPTZero has a low false-positive rate (classifying human-written text as machine-generated) but a high false-negative rate (classifying machine-generated text as human-written).


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "0a05528b-d05d-4fb3-947f-20e0adce1e25",
  "uuid": "211a627c-d6b9-4c67-964d-dacb49e6d4cf",
  "tool_use_result": {
    "query": "GPTZero academic paper 2024 2025 machine text detection",
    "results": [
      {
        "tool_use_id": "srvtoolu_013rSidYLUBGeaSQvASm9v7B",
        "content": [
          {
            "title": "Utilizing GPTZero to Detect AI-Generated Writing",
            "url": "https://files.eric.ed.gov/fulltext/EJ1482073.pdf"
          },
          {
            "title": "GPTZero Review 2025: Accuracy, False Positives & Top Alternatives",
            "url": "https://skywork.ai/blog/gptzero-review-2025/"
          },
          {
            "title": "GPTZero",
            "url": "https://gptzero.me/"
          },
          {
            "title": "Issues in Information Systems Volume 25, Issue 3 pp. 165-174, 2024 165",
            "url": "https://www.iacis.org/iis/2024/3_iis_2024_165-174.pdf"
          },
          {
            "title": "GPTZero Performance in Identifying Artificial Intelligence-Generated Medical Texts: A Preliminary Study - PMC",
            "url": "https://pmc.ncbi.nlm.nih.gov/articles/PMC10519776/"
          },
          {
            "title": "GPTZero Technology - AI Detection",
            "url": "https://gptzero.me/technology"
          },
          {
            "title": "GPTZero's Research Contributions",
            "url": "https://gptzero.me/resources/researchers"
          },
          {
            "title": "Assessing the Effectiveness of AI Detection Tools for Varying Levels of AI-Generated Text | Springer Nature Link",
            "url": "https://link.springer.com/chapter/10.1007/978-3-032-14197-2_27"
          },
          {
            "title": "(PDF) Assessing GPTZero's Accuracy in Identifying AI vs. Human-Written Essays",
            "url": "https://www.researchgate.net/publication/393183923_Assessing_GPTZero's_Accuracy_in_Identifying_AI_vs_Human-Written_Essays"
          },
          {
            "title": "GPTZero - Wikipedia",
            "url": "https://en.wikipedia.org/wiki/GPTZero"
          }
        ]
      },
      "Based on the web search results, here are relevant academic papers and findings about GPTZero's machine-generated text detection from 2024-2025:\n\n## Academic Papers\n\nA 2025 paper by Paullet, Pinchot, Kinney, and Stewart titled \"Detecting AI-Generated Writing Using GPTZero\" was published in the Information Systems Education Journal, volume 23, issue 6, pages 44-52.\n\nAnother study tested GPTZero's capabilities for detecting if assignments were written by humans or AI, using a set of 100 samples.\n\n## Recent Technical Research\n\nGPTZero's latest paper, \"GPTZero: Robust Detection of LLM-Generated Texts,\" provides a walkthrough of their detection pipeline including data gathering and QA, hierarchical modeling, robustness evaluation, and explainability methods. The paper frames detection as Human, AI, and Mixed categories with a hierarchical multi-task architecture, and reports state-of-the-art results across domains, languages, and multilabel settings.\n\n## Key Findings on Accuracy\n\nA study found that GPTZero can identify AI-generated texts at around 90-99% accuracy rates. However, academic work in 2025 shows that paraphrasing strategies can drastically reduce detector recall, with a training-free attack presented in June 2025 demonstrating how adversarial paraphrasing can evade detectors widely.\n\n## Limitations and Cautions\n\nOne study found that GPTZero has a low false-positive rate (classifying human-written text as machine-generated) but a high false-negative rate (classifying machine-generated text as human-written)."
    ],
    "durationSeconds": 7.690098508000001
  }
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-14T12:31:54.213Z_

<details><summary>↩ Tool result · `toolu_01FnN1hVDnTnU7xZPYdrr2RX`</summary>

```text
Web search results for query: "Group DRO Sagawa 2020 distributionally robust optimization"

Links: [{"title":"[1911.08731] Distributionally Robust Neural Networks for Group Shifts: On the Importance of Regularization for Worst-Case Generalization","url":"https://arxiv.org/abs/1911.08731"},{"title":"GitHub - kohpangwei/group_DRO: Distributionally robust neural networks for group shifts · GitHub","url":"https://github.com/kohpangwei/group_DRO"},{"title":"Distributionally Robust Neural Networks for Group Shifts:","url":"https://cs.stanford.edu/~ssagawa/assets/slides/groupDRO_ICLR2020.pdf"},{"title":"Distributionally Robust Neural Networks | OpenReview","url":"https://openreview.net/forum?id=ryxGuJrFvS"},{"title":"FOCUS ON THE COMMON GOOD: GROUP DISTRIBU","url":"https://openreview.net/pdf?id=irARV_2VFs4"},{"title":"Distributionally Robust Optimization with Probabilistic Group","url":"https://ojs.aaai.org/index.php/AAAI/article/view/26394/26166"},{"title":"[PDF] Distributionally Robust Neural Networks for Group Shifts: On the Importance of Regularization for Worst-Case Generalization | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Distributionally-Robust-Neural-Networks-for-Group-Sagawa-Koh/193092aef465bec868d1089ccfcac0279b914bda"},{"title":"Per-Group Distributionally Robust Optimization (Per-GDRO ...","url":"https://opt-ml.org/papers/2025/paper163.pdf"},{"title":"distributionally robust neural networks","url":"https://openreview.net/pdf?id=ryxGuJrFvS"},{"title":"Group Distributionally Robust Optimization with Flexible Sample Queries","url":"https://arxiv.org/html/2505.15212v1"}]

Based on the search results, I found comprehensive information about Group DRO and Sagawa's 2020 work on distributionally robust optimization.

## Summary of Group DRO (Sagawa et al., 2020)

Distributionally robust optimization (DRO) allows us to learn models that instead minimize the worst-case training loss over a set of pre-defined groups. Overparameterized neural networks can be highly accurate on average on an i.i.d. test set yet consistently fail on atypical groups of the data (e.g., by learning spurious correlations that hold on average but not in such groups).

### Key Challenge with Naive Application

Naively applying group DRO to overparameterized neural networks fails: these models can perfectly fit the training data, and any model with vanishing average training loss also already has vanishing worst-case training loss. Instead, the poor worst-case performance arises from poor generalization on some groups.

### Solution: Regularization

By coupling group DRO models with increased regularization---a stronger-than-typical L2 penalty or early stopping---substantial improvements in worst-group accuracies are achieved, with 10-40 percentage point improvements on a natural language inference task and two image tasks, while maintaining high average accuracies.

### Algorithmic Contribution

A stochastic optimization algorithm, with convergence guarantees, was introduced to efficiently train group DRO models.

This 2020 paper by Shiori Sagawa, Pang Wei Koh, Tatsunori Hashimoto, and Percy Liang was published at ICLR 2020 and has become influential in the field of distributionally robust optimization for addressing group-based fairness and robustness in machine learning.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "0a05528b-d05d-4fb3-947f-20e0adce1e25",
  "uuid": "a8c02947-be74-42ba-8285-06e54cc418b3",
  "tool_use_result": {
    "query": "Group DRO Sagawa 2020 distributionally robust optimization",
    "results": [
      {
        "tool_use_id": "srvtoolu_01G16GCErgK6yF2eKaFESMe9",
        "content": [
          {
            "title": "[1911.08731] Distributionally Robust Neural Networks for Group Shifts: On the Importance of Regularization for Worst-Case Generalization",
            "url": "https://arxiv.org/abs/1911.08731"
          },
          {
            "title": "GitHub - kohpangwei/group_DRO: Distributionally robust neural networks for group shifts · GitHub",
            "url": "https://github.com/kohpangwei/group_DRO"
          },
          {
            "title": "Distributionally Robust Neural Networks for Group Shifts:",
            "url": "https://cs.stanford.edu/~ssagawa/assets/slides/groupDRO_ICLR2020.pdf"
          },
          {
            "title": "Distributionally Robust Neural Networks | OpenReview",
            "url": "https://openreview.net/forum?id=ryxGuJrFvS"
          },
          {
            "title": "FOCUS ON THE COMMON GOOD: GROUP DISTRIBU",
            "url": "https://openreview.net/pdf?id=irARV_2VFs4"
          },
          {
            "title": "Distributionally Robust Optimization with Probabilistic Group",
            "url": "https://ojs.aaai.org/index.php/AAAI/article/view/26394/26166"
          },
          {
            "title": "[PDF] Distributionally Robust Neural Networks for Group Shifts: On the Importance of Regularization for Worst-Case Generalization | Semantic Scholar",
            "url": "https://www.semanticscholar.org/paper/Distributionally-Robust-Neural-Networks-for-Group-Sagawa-Koh/193092aef465bec868d1089ccfcac0279b914bda"
          },
          {
            "title": "Per-Group Distributionally Robust Optimization (Per-GDRO ...",
            "url": "https://opt-ml.org/papers/2025/paper163.pdf"
          },
          {
            "title": "distributionally robust neural networks",
            "url": "https://openreview.net/pdf?id=ryxGuJrFvS"
          },
          {
            "title": "Group Distributionally Robust Optimization with Flexible Sample Queries",
            "url": "https://arxiv.org/html/2505.15212v1"
          }
        ]
      },
      "Based on the search results, I found comprehensive information about Group DRO and Sagawa's 2020 work on distributionally robust optimization.\n\n## Summary of Group DRO (Sagawa et al., 2020)\n\nDistributionally robust optimization (DRO) allows us to learn models that instead minimize the worst-case training loss over a set of pre-defined groups. Overparameterized neural networks can be highly accurate on average on an i.i.d. test set yet consistently fail on atypical groups of the data (e.g., by learning spurious correlations that hold on average but not in such groups).\n\n### Key Challenge with Naive Application\n\nNaively applying group DRO to overparameterized neural networks fails: these models can perfectly fit the training data, and any model with vanishing average training loss also already has vanishing worst-case training loss. Instead, the poor worst-case performance arises from poor generalization on some groups.\n\n### Solution: Regularization\n\nBy coupling group DRO models with increased regularization---a stronger-than-typical L2 penalty or early stopping---substantial improvements in worst-group accuracies are achieved, with 10-40 percentage point improvements on a natural language inference task and two image tasks, while maintaining high average accuracies.\n\n### Algorithmic Contribution\n\nA stochastic optimization algorithm, with convergence guarantees, was introduced to efficiently train group DRO models.\n\nThis 2020 paper by Shiori Sagawa, Pang Wei Koh, Tatsunori Hashimoto, and Percy Liang was published at ICLR 2020 and has become influential in the field of distributionally robust optimization for addressing group-based fairness and robustness in machine learning."
    ],
    "durationSeconds": 8.434454394000001
  }
}
```

</details>

---

### Assistant

_source line 21_

<details><summary>Logged reasoning block</summary>

```text
Let me search more specifically for the Drayson paper and also for the remaining pending items (self-play fine-tuning, data influence/attribution).

The first search for Drayson didn't find a match. Let me try different search terms. Also, the arxiv 2602.16065 paper is found - "Can Generative Artificial Intelligence Survive Data Contamination? Theoretical Guarantees under Contaminated Recursive Training". I need to get the authors.

Let me also search for:


- Drayson using alternative keywords
- The authors of that arxiv paper on data contamination
- Papers on self-play fine-tuning and synthetic data augmentation
- TracIn and data influence attribution methods
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "0a05528b-d05d-4fb3-947f-20e0adce1e25",
  "uuid": "d8bb7ccc-32c1-40c7-9d37-0fdb1ce2d30c",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LJYErPAA9vHeYr3isFyJhs",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4590,
      "cache_read_input_tokens": 29356,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4590
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Assistant

_source line 22_

Drayson paper not found with initial search. Let me try alternative queries and get the remaining information.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "0a05528b-d05d-4fb3-947f-20e0adce1e25",
  "uuid": "0073234b-a523-4b93-be24-f6734b4379eb",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LJYErPAA9vHeYr3isFyJhs",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4590,
      "cache_read_input_tokens": 29356,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4590
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool call

_source line 23_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01YJ778eU145WqVRf1vc1VRb`</summary>

```json
{
  "query": "Drayson 2025 \"detect and reweight\" synthetic data pretraining language model"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "0a05528b-d05d-4fb3-947f-20e0adce1e25",
  "uuid": "9b6e2e69-6b77-4685-abad-6b70d5605a66",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LJYErPAA9vHeYr3isFyJhs",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4590,
      "cache_read_input_tokens": 29356,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4590
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool call

_source line 24_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01NYRBnj8GoHabz1AptvJUnq`</summary>

```json
{
  "query": "arxiv 2602.16065 authors \"contaminated recursive training\""
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "0a05528b-d05d-4fb3-947f-20e0adce1e25",
  "uuid": "97c712d2-9e1a-498d-b4af-ac39754a11c3",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LJYErPAA9vHeYr3isFyJhs",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4590,
      "cache_read_input_tokens": 29356,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4590
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool call

_source line 25_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01QcU7vquDUQdm7X3xPjh65x`</summary>

```json
{
  "query": "self-play fine-tuning synthetic data augmentation beneficial LLM representative paper 2024"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "0a05528b-d05d-4fb3-947f-20e0adce1e25",
  "uuid": "7f1bf9b9-9e0a-42bb-943e-8cad129b157c",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LJYErPAA9vHeYr3isFyJhs",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4590,
      "cache_read_input_tokens": 29356,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4590
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool call

_source line 26_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01EddMzyDfGDXqybX2SE7DF9`</summary>

```json
{
  "query": "TracIn data influence functions data attribution training survey"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "0a05528b-d05d-4fb3-947f-20e0adce1e25",
  "uuid": "6b659666-6880-45d3-b413-6bfae90a3c5a",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LJYErPAA9vHeYr3isFyJhs",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4590,
      "cache_read_input_tokens": 29356,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4590
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool result

_source line 27 · 2026-05-14T12:32:08.093Z_

<details><summary>↩ Tool result · `toolu_01NYRBnj8GoHabz1AptvJUnq`</summary>

```text
Web search results for query: "arxiv 2602.16065 authors "contaminated recursive training""

Links: [{"title":"[2602.16065] Can Generative Artificial Intelligence Survive Data Contamination? Theoretical Guarantees under Contaminated Recursive Training","url":"https://arxiv.org/abs/2602.16065"},{"title":"Can Generative Artificial Intelligence Survive Data Contamination? Theoretical Guarantees under Contaminated Recursive Training","url":"https://arxiv.org/html/2602.16065"},{"title":"Machine Learning","url":"https://arxiv.org/list/cs.LG/recent?skip=789&show=250"},{"title":"[2602.15659] Can Recommender Systems Teach Themselves? A Recursive Self-Improving Framework with Fidelity Control","url":"https://arxiv.org/abs/2602.15659"},{"title":"From Collapse to Improvement: Statistical Perspectives on the Evolutionary Dynamics of Iterative Training on Contaminated Sources","url":"https://arxiv.org/html/2602.10531v1"},{"title":"[2602.10531v1] From Collapse to Improvement: Statistical Perspectives on the Evolutionary Dynamics of Iterative Training on Contaminated Sources","url":"https://arxiv.org/abs/2602.10531v1"},{"title":"[2602.10531] From Collapse to Improvement: Statistical Perspectives on the Evolutionary Dynamics of Iterative Training on Contaminated Sources","url":"https://arxiv.org/abs/2602.10531"},{"title":"The Curse of Recursion: Training on Generated Data Makes Models Forget","url":"https://arxiv.org/html/2305.17493v3"},{"title":"Recursive Language Models Alex L. Zhang 1 Tim Kraska 1 Omar Khattab 1 Abstract","url":"https://arxiv.org/pdf/2512.24601"},{"title":"[2602.19126] Robust Predictive Uncertainty and Double Descent in Contaminated Bayesian Random Features","url":"https://arxiv.org/abs/2602.19126"}]

Based on the search results, here's what I found about arxiv 2602.16065:

**Paper Title:** Can Generative Artificial Intelligence Survive Data Contamination? Theoretical Guarantees under Contaminated Recursive Training

**Authors:** Kevin Wang, Hongqian Niu, Didong Li

**Submission Date:** February 17, 2026

**Overview:** The paper examines recursive training processes where generative models are trained on mixtures of human-generated data and AI-generated data from earlier versions, creating a recursive training process with data contamination. Existing theoretical work has examined only highly simplified settings, where both the real data and the generative model are discrete or Gaussian, where it has been shown that such recursive training leads to model collapse.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "0a05528b-d05d-4fb3-947f-20e0adce1e25",
  "uuid": "4d65d73b-5803-4725-8e6f-4e57075ad4f2",
  "tool_use_result": {
    "query": "arxiv 2602.16065 authors \"contaminated recursive training\"",
    "results": [
      {
        "tool_use_id": "srvtoolu_019Szd6PC4tpK8yfhrjcTBqh",
        "content": [
          {
            "title": "[2602.16065] Can Generative Artificial Intelligence Survive Data Contamination? Theoretical Guarantees under Contaminated Recursive Training",
            "url": "https://arxiv.org/abs/2602.16065"
          },
          {
            "title": "Can Generative Artificial Intelligence Survive Data Contamination? Theoretical Guarantees under Contaminated Recursive Training",
            "url": "https://arxiv.org/html/2602.16065"
          },
          {
            "title": "Machine Learning",
            "url": "https://arxiv.org/list/cs.LG/recent?skip=789&show=250"
          },
          {
            "title": "[2602.15659] Can Recommender Systems Teach Themselves? A Recursive Self-Improving Framework with Fidelity Control",
            "url": "https://arxiv.org/abs/2602.15659"
          },
          {
            "title": "From Collapse to Improvement: Statistical Perspectives on the Evolutionary Dynamics of Iterative Training on Contaminated Sources",
            "url": "https://arxiv.org/html/2602.10531v1"
          },
          {
            "title": "[2602.10531v1] From Collapse to Improvement: Statistical Perspectives on the Evolutionary Dynamics of Iterative Training on Contaminated Sources",
            "url": "https://arxiv.org/abs/2602.10531v1"
          },
          {
            "title": "[2602.10531] From Collapse to Improvement: Statistical Perspectives on the Evolutionary Dynamics of Iterative Training on Contaminated Sources",
            "url": "https://arxiv.org/abs/2602.10531"
          },
          {
            "title": "The Curse of Recursion: Training on Generated Data Makes Models Forget",
            "url": "https://arxiv.org/html/2305.17493v3"
          },
          {
            "title": "Recursive Language Models Alex L. Zhang 1 Tim Kraska 1 Omar Khattab 1 Abstract",
            "url": "https://arxiv.org/pdf/2512.24601"
          },
          {
            "title": "[2602.19126] Robust Predictive Uncertainty and Double Descent in Contaminated Bayesian Random Features",
            "url": "https://arxiv.org/abs/2602.19126"
          }
        ]
      },
      "Based on the search results, here's what I found about arxiv 2602.16065:\n\n**Paper Title:** Can Generative Artificial Intelligence Survive Data Contamination? Theoretical Guarantees under Contaminated Recursive Training\n\n**Authors:** Kevin Wang, Hongqian Niu, Didong Li\n\n**Submission Date:** February 17, 2026\n\n**Overview:** The paper examines recursive training processes where generative models are trained on mixtures of human-generated data and AI-generated data from earlier versions, creating a recursive training process with data contamination. Existing theoretical work has examined only highly simplified settings, where both the real data and the generative model are discrete or Gaussian, where it has been shown that such recursive training leads to model collapse."
    ],
    "durationSeconds": 4.623550486
  }
}
```

</details>

---

### Tool result

_source line 28 · 2026-05-14T12:32:09.192Z_

<details><summary>↩ Tool result · `toolu_01YJ778eU145WqVRf1vc1VRb`</summary>

```text
Web search results for query: "Drayson 2025 "detect and reweight" synthetic data pretraining language model"

Links: [{"title":"Demystifying Synthetic Data in LLM Pre-training: A Systematic Study of Scaling Laws, Benefits, and Pitfalls","url":"https://arxiv.org/html/2510.01631v1"},{"title":"Demystifying Synthetic Data in LLM Pre-training","url":"https://aclanthology.org/2025.emnlp-main.544.pdf"},{"title":"[2409.14781] Pretraining Data Detection for Large Language Models: A Divergence-based Calibration Method","url":"https://arxiv.org/abs/2409.14781"},{"title":"Synthetic bootstrapped pretraining","url":"https://arxiv.org/html/2509.15248v1"},{"title":"GitHub - pengr/LLM-Synthetic-Data: A live reading list for LLM data synthesis (Updated to July, 2025). · GitHub","url":"https://github.com/pengr/LLM-Synthetic-Data"},{"title":"Detecting Pretraining Data from Large Language Models","url":"https://swj0419.github.io/detect-pretrain.github.io/"},{"title":"Published as a conference paper at ICLR 2025 SYNTHETIC CONTINUED PRETRAINING","url":"https://proceedings.iclr.cc/paper_files/paper/2025/file/6dcf277ea32ce3288914faf369fe6de0-Paper-Conference.pdf"},{"title":"Detecting Pretraining Data from Large Language Models | OpenReview","url":"https://openreview.net/forum?id=zWqr3MQuNs"},{"title":"Will Synthetic Data Finally Solve the Data Access Problem?","url":"https://iclr.cc/virtual/2025/workshop/24001"},{"title":"Demystifying Synthetic Data in LLM Pre-training: A Systematic Study of Scaling Laws, Benefits, and Pitfalls - ACL Anthology","url":"https://aclanthology.org/2025.emnlp-main.544/"}]

Based on the search results, I couldn't find a specific 2025 paper by "Drayson" that uses the phrase "detect and reweight" for synthetic data pretraining. 

However, the search returned several relevant 2025 papers on synthetic data in language model pretraining:

1. **"Demystifying Synthetic Data in LLM Pre-training: A Systematic Study of Scaling Laws, Benefits, and Pitfalls"** (Kang et al., EMNLP 2025) - This paper investigates training data's crucial role in LLM scaling and conducts a large-scale empirical investigation using a unified protocol and scaling laws.

2. **"Synthetic Bootstrapped Pretraining"** - This introduces a language model pretraining procedure that first learns a model of relations between documents from the pretraining dataset and then leverages it to synthesize a vast new corpus for joint training.

3. Papers on **pretraining data detection** - such as one on "Pretraining Data Detection for Large Language Models: A Divergence-based Calibration Method" (2025) that addresses detection methods for identifying whether text was part of an LLM's training data.

It's possible that the author's name or paper title is slightly different from what was searched. If you have additional details about the Drayson paper (such as the correct year, alternate author names, or a more complete title), I can search again to locate the specific work.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "0a05528b-d05d-4fb3-947f-20e0adce1e25",
  "uuid": "97864322-c34f-4ffb-831a-b01d08e35c13",
  "tool_use_result": {
    "query": "Drayson 2025 \"detect and reweight\" synthetic data pretraining language model",
    "results": [
      {
        "tool_use_id": "srvtoolu_017be5KoefQjoLFahZpekXy6",
        "content": [
          {
            "title": "Demystifying Synthetic Data in LLM Pre-training: A Systematic Study of Scaling Laws, Benefits, and Pitfalls",
            "url": "https://arxiv.org/html/2510.01631v1"
          },
          {
            "title": "Demystifying Synthetic Data in LLM Pre-training",
            "url": "https://aclanthology.org/2025.emnlp-main.544.pdf"
          },
          {
            "title": "[2409.14781] Pretraining Data Detection for Large Language Models: A Divergence-based Calibration Method",
            "url": "https://arxiv.org/abs/2409.14781"
          },
          {
            "title": "Synthetic bootstrapped pretraining",
            "url": "https://arxiv.org/html/2509.15248v1"
          },
          {
            "title": "GitHub - pengr/LLM-Synthetic-Data: A live reading list for LLM data synthesis (Updated to July, 2025). · GitHub",
            "url": "https://github.com/pengr/LLM-Synthetic-Data"
          },
          {
            "title": "Detecting Pretraining Data from Large Language Models",
            "url": "https://swj0419.github.io/detect-pretrain.github.io/"
          },
          {
            "title": "Published as a conference paper at ICLR 2025 SYNTHETIC CONTINUED PRETRAINING",
            "url": "https://proceedings.iclr.cc/paper_files/paper/2025/file/6dcf277ea32ce3288914faf369fe6de0-Paper-Conference.pdf"
          },
          {
            "title": "Detecting Pretraining Data from Large Language Models | OpenReview",
            "url": "https://openreview.net/forum?id=zWqr3MQuNs"
          },
          {
            "title": "Will Synthetic Data Finally Solve the Data Access Problem?",
            "url": "https://iclr.cc/virtual/2025/workshop/24001"
          },
          {
            "title": "Demystifying Synthetic Data in LLM Pre-training: A Systematic Study of Scaling Laws, Benefits, and Pitfalls - ACL Anthology",
            "url": "https://aclanthology.org/2025.emnlp-main.544/"
          }
        ]
      },
      "Based on the search results, I couldn't find a specific 2025 paper by \"Drayson\" that uses the phrase \"detect and reweight\" for synthetic data pretraining. \n\nHowever, the search returned several relevant 2025 papers on synthetic data in language model pretraining:\n\n1. **\"Demystifying Synthetic Data in LLM Pre-training: A Systematic Study of Scaling Laws, Benefits, and Pitfalls\"** (Kang et al., EMNLP 2025) - This paper investigates training data's crucial role in LLM scaling and conducts a large-scale empirical investigation using a unified protocol and scaling laws.\n\n2. **\"Synthetic Bootstrapped Pretraining\"** - This introduces a language model pretraining procedure that first learns a model of relations between documents from the pretraining dataset and then leverages it to synthesize a vast new corpus for joint training.\n\n3. Papers on **pretraining data detection** - such as one on \"Pretraining Data Detection for Large Language Models: A Divergence-based Calibration Method\" (2025) that addresses detection methods for identifying whether text was part of an LLM's training data.\n\nIt's possible that the author's name or paper title is slightly different from what was searched. If you have additional details about the Drayson paper (such as the correct year, alternate author names, or a more complete title), I can search again to locate the specific work."
    ],
    "durationSeconds": 6.269426064999999
  }
}
```

</details>

---

### Tool result

_source line 29 · 2026-05-14T12:32:11.463Z_

<details><summary>↩ Tool result · `toolu_01EddMzyDfGDXqybX2SE7DF9`</summary>

```text
Web search results for query: "TracIn data influence functions data attribution training survey"

Links: [{"title":"Training Data Influence Analysis and Estimation: A Survey Zayd Hammoudeh∗1,2","url":"https://arxiv.org/pdf/2212.04612"},{"title":"TracIn — A Simple Method to Estimate Training Data Influence","url":"https://research.google/blog/tracin-a-simple-method-to-estimate-training-data-influence/"},{"title":"Training data influence analysis and estimation: a survey | Machine Learning | Springer Nature Link","url":"https://link.springer.com/article/10.1007/s10994-023-06495-7"},{"title":"(PDF) Training data influence analysis and estimation: a survey","url":"https://www.researchgate.net/publication/379410061_Training_data_influence_analysis_and_estimation_a_survey"},{"title":"Estimating Training Data Influence by Tracing Gradient ...","url":"https://proceedings.neurips.cc/paper/2020/file/e6385d39ec9394f2f3a354d9d2b88eec-Paper.pdf"},{"title":"TRAK: Attributing Model Behavior at Scale","url":"https://proceedings.mlr.press/v202/park23c/park23c.pdf"},{"title":"Training Data Attribution via Approximate Unrolling","url":"https://proceedings.neurips.cc/paper_files/paper/2024/file/7af60ccb99c7a434a0d9d9c1fb00ca94-Paper-Conference.pdf"},{"title":"Integrated Influence: Data Attribution with Baseline","url":"https://arxiv.org/html/2508.05089"},{"title":"A Survey of Data Attribution: Methods, Applications, and ...","url":"https://hal.science/hal-05230469v1/document"},{"title":"[2002.08484] Estimating Training Data Influence by Tracing Gradient Descent","url":"https://arxiv.org/abs/2002.08484"}]

Based on the search results, here's what I found about TracIn, data influence functions, data attribution, and training surveys:

## Overview

The first comprehensive survey of training data influence analysis and estimation has recently been published, covering key methods including TracIn, influence functions, and other approaches.

## TracIn Method

TracIn is a method that computes the influence of a training example on a prediction made by the model by tracing how the loss on the test point changes during the training process whenever the training example of interest was utilized.

The TracIn method can be reduced to the simple form of the dot product of loss gradients of the test and training examples, weighted by the learning rate, and summed across checkpoints. Notably, TracIn is simple to implement; all it needs is the ability to work with gradients, checkpoints, and loss functions.

## Training Data Influence Analysis

Influence analysis partially demystifies training's underlying interactions by quantifying the amount each training instance alters the final model. Measuring the training data's influence exactly can be provably hard in the worst case; this has led to the development and use of influence estimators, which only approximate the true influence.

## Related Methods

The survey details gradient-based static estimators including influence functions and representer points, as well as dynamic estimators TracIn and HyDRA.

The search results show these are active areas of machine learning research with multiple papers and surveys addressing data attribution and influence estimation methods.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "0a05528b-d05d-4fb3-947f-20e0adce1e25",
  "uuid": "e0daa4d1-289f-4cff-b487-7e9db9922f9f",
  "tool_use_result": {
    "query": "TracIn data influence functions data attribution training survey",
    "results": [
      {
        "tool_use_id": "srvtoolu_016yGNfvmi1Kwc3vq8ZwuS4i",
        "content": [
          {
            "title": "Training Data Influence Analysis and Estimation: A Survey Zayd Hammoudeh∗1,2",
            "url": "https://arxiv.org/pdf/2212.04612"
          },
          {
            "title": "TracIn — A Simple Method to Estimate Training Data Influence",
            "url": "https://research.google/blog/tracin-a-simple-method-to-estimate-training-data-influence/"
          },
          {
            "title": "Training data influence analysis and estimation: a survey | Machine Learning | Springer Nature Link",
            "url": "https://link.springer.com/article/10.1007/s10994-023-06495-7"
          },
          {
            "title": "(PDF) Training data influence analysis and estimation: a survey",
            "url": "https://www.researchgate.net/publication/379410061_Training_data_influence_analysis_and_estimation_a_survey"
          },
          {
            "title": "Estimating Training Data Influence by Tracing Gradient ...",
            "url": "https://proceedings.neurips.cc/paper/2020/file/e6385d39ec9394f2f3a354d9d2b88eec-Paper.pdf"
          },
          {
            "title": "TRAK: Attributing Model Behavior at Scale",
            "url": "https://proceedings.mlr.press/v202/park23c/park23c.pdf"
          },
          {
            "title": "Training Data Attribution via Approximate Unrolling",
            "url": "https://proceedings.neurips.cc/paper_files/paper/2024/file/7af60ccb99c7a434a0d9d9c1fb00ca94-Paper-Conference.pdf"
          },
          {
            "title": "Integrated Influence: Data Attribution with Baseline",
            "url": "https://arxiv.org/html/2508.05089"
          },
          {
            "title": "A Survey of Data Attribution: Methods, Applications, and ...",
            "url": "https://hal.science/hal-05230469v1/document"
          },
          {
            "title": "[2002.08484] Estimating Training Data Influence by Tracing Gradient Descent",
            "url": "https://arxiv.org/abs/2002.08484"
          }
        ]
      },
      "Based on the search results, here's what I found about TracIn, data influence functions, data attribution, and training surveys:\n\n## Overview\n\nThe first comprehensive survey of training data influence analysis and estimation has recently been published, covering key methods including TracIn, influence functions, and other approaches.\n\n## TracIn Method\n\nTracIn is a method that computes the influence of a training example on a prediction made by the model by tracing how the loss on the test point changes during the training process whenever the training example of interest was utilized.\n\nThe TracIn method can be reduced to the simple form of the dot product of loss gradients of the test and training examples, weighted by the learning rate, and summed across checkpoints. Notably, TracIn is simple to implement; all it needs is the ability to work with gradients, checkpoints, and loss functions.\n\n## Training Data Influence Analysis\n\nInfluence analysis partially demystifies training's underlying interactions by quantifying the amount each training instance alters the final model. Measuring the training data's influence exactly can be provably hard in the worst case; this has led to the development and use of influence estimators, which only approximate the true influence.\n\n## Related Methods\n\nThe survey details gradient-based static estimators including influence functions and representer points, as well as dynamic estimators TracIn and HyDRA.\n\nThe search results show these are active areas of machine learning research with multiple papers and surveys addressing data attribution and influence estimation methods."
    ],
    "durationSeconds": 6.929377274999999
  }
}
```

</details>

---

### Tool result

_source line 30 · 2026-05-14T12:32:12.548Z_

<details><summary>↩ Tool result · `toolu_01QcU7vquDUQdm7X3xPjh65x`</summary>

```text
Web search results for query: "self-play fine-tuning synthetic data augmentation beneficial LLM representative paper 2024"

Links: [{"title":"Self-Play Fine-Tuning Converts Weak Language Models to Strong Language Models","url":"https://uclaml.github.io/SPIN/"},{"title":"Self-Play Fine-Tuning Converts Weak Language Models to Strong Language Models","url":"https://arxiv.org/pdf/2401.01335"},{"title":"GitHub - uclaml/SPIN: The official implementation of Self-Play Fine-Tuning (SPIN) · GitHub","url":"https://github.com/uclaml/SPIN"},{"title":"[2401.01335] Self-Play Fine-Tuning Converts Weak Language Models to Strong Language Models","url":"https://arxiv.org/abs/2401.01335"},{"title":"Synthetic Data Generation Strategies for Fine-Tuning LLMs","url":"https://scale.com/blog/synthetic-data-fine-tuning-llms"},{"title":"Triplets Better Than Pairs: Towards Stable and Effective Self-Play Fine-Tuning for LLMs","url":"https://arxiv.org/html/2601.08198"},{"title":"Self-Play Fine-Tuning Converts Weak Language Models ...","url":"https://www.emergentmind.com/papers/2401.01335"},{"title":"How to Generate and Use Synthetic Data for Finetuning","url":"https://eugeneyan.com/writing/synthetic/"},{"title":"GitHub - pengr/LLM-Synthetic-Data: A live reading list for LLM data synthesis (Updated to July, 2025). · GitHub","url":"https://github.com/pengr/LLM-Synthetic-Data"},{"title":"GitHub - thomasgauthier/LLM-self-play: Minimal implementation of the Self-Play Fine-Tuning Converts Weak Language Models to Strong Language Models paper (ArXiv 20232401.01335)","url":"https://github.com/thomasgauthier/LLM-self-play"}]

Based on the search results, here's a comprehensive overview of a representative 2024 paper on self-play fine-tuning with synthetic data augmentation for LLMs:

## Self-Play Fine-Tuning (SPIN) - Key Paper from 2024

The most prominent 2024 paper in this area is "Self-Play Fine-Tuning Converts Weak Language Models to Strong Language Models" by Chen, Deng, Yuan, Ji, and Gu, published on arXiv as paper 2401.01335.

### Core Approach

The method uses a self-play mechanism where the LLM refines its capability by playing against instances of itself, with the LLM generating its own training data from previous iterations and refining its policy by discerning these self-generated responses from those obtained from human-annotated data.

### Benefits of Synthetic Data

Analysis demonstrates the effectiveness of the synthetic data used by SPIN compared to the SFT (Supervised Fine-Tuning) data, as well as the necessity of iterative training in SPIN. This approach eliminates the need for additional binary feedback from humans or an extra reward model thanks to the self-play mechanism.

### Empirical Results

SPIN can significantly improve the LLM's performance across a variety of benchmarks and even outperform models trained through direct preference optimization (DPO) supplemented with extra GPT-4 preference data.

### Theoretical Grounding

The authors prove that the global optimum to the training objective function is achieved only when the LLM policy aligns with the target data distribution.

This paper represents a significant advancement in showing how synthetic data augmentation through self-play mechanisms can be beneficial for improving LLMs without requiring additional human annotation beyond the initial SFT dataset.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "0a05528b-d05d-4fb3-947f-20e0adce1e25",
  "uuid": "2d26dc23-1858-4aab-a159-155385b9b11d",
  "tool_use_result": {
    "query": "self-play fine-tuning synthetic data augmentation beneficial LLM representative paper 2024",
    "results": [
      {
        "tool_use_id": "srvtoolu_01X29MSVH9XrF7MwEuifCcag",
        "content": [
          {
            "title": "Self-Play Fine-Tuning Converts Weak Language Models to Strong Language Models",
            "url": "https://uclaml.github.io/SPIN/"
          },
          {
            "title": "Self-Play Fine-Tuning Converts Weak Language Models to Strong Language Models",
            "url": "https://arxiv.org/pdf/2401.01335"
          },
          {
            "title": "GitHub - uclaml/SPIN: The official implementation of Self-Play Fine-Tuning (SPIN) · GitHub",
            "url": "https://github.com/uclaml/SPIN"
          },
          {
            "title": "[2401.01335] Self-Play Fine-Tuning Converts Weak Language Models to Strong Language Models",
            "url": "https://arxiv.org/abs/2401.01335"
          },
          {
            "title": "Synthetic Data Generation Strategies for Fine-Tuning LLMs",
            "url": "https://scale.com/blog/synthetic-data-fine-tuning-llms"
          },
          {
            "title": "Triplets Better Than Pairs: Towards Stable and Effective Self-Play Fine-Tuning for LLMs",
            "url": "https://arxiv.org/html/2601.08198"
          },
          {
            "title": "Self-Play Fine-Tuning Converts Weak Language Models ...",
            "url": "https://www.emergentmind.com/papers/2401.01335"
          },
          {
            "title": "How to Generate and Use Synthetic Data for Finetuning",
            "url": "https://eugeneyan.com/writing/synthetic/"
          },
          {
            "title": "GitHub - pengr/LLM-Synthetic-Data: A live reading list for LLM data synthesis (Updated to July, 2025). · GitHub",
            "url": "https://github.com/pengr/LLM-Synthetic-Data"
          },
          {
            "title": "GitHub - thomasgauthier/LLM-self-play: Minimal implementation of the Self-Play Fine-Tuning Converts Weak Language Models to Strong Language Models paper (ArXiv 20232401.01335)",
            "url": "https://github.com/thomasgauthier/LLM-self-play"
          }
        ]
      },
      "Based on the search results, here's a comprehensive overview of a representative 2024 paper on self-play fine-tuning with synthetic data augmentation for LLMs:\n\n## Self-Play Fine-Tuning (SPIN) - Key Paper from 2024\n\nThe most prominent 2024 paper in this area is \"Self-Play Fine-Tuning Converts Weak Language Models to Strong Language Models\" by Chen, Deng, Yuan, Ji, and Gu, published on arXiv as paper 2401.01335.\n\n### Core Approach\n\nThe method uses a self-play mechanism where the LLM refines its capability by playing against instances of itself, with the LLM generating its own training data from previous iterations and refining its policy by discerning these self-generated responses from those obtained from human-annotated data.\n\n### Benefits of Synthetic Data\n\nAnalysis demonstrates the effectiveness of the synthetic data used by SPIN compared to the SFT (Supervised Fine-Tuning) data, as well as the necessity of iterative training in SPIN. This approach eliminates the need for additional binary feedback from humans or an extra reward model thanks to the self-play mechanism.\n\n### Empirical Results\n\nSPIN can significantly improve the LLM's performance across a variety of benchmarks and even outperform models trained through direct preference optimization (DPO) supplemented with extra GPT-4 preference data.\n\n### Theoretical Grounding\n\nThe authors prove that the global optimum to the training objective function is achieved only when the LLM policy aligns with the target data distribution.\n\nThis paper represents a significant advancement in showing how synthetic data augmentation through self-play mechanisms can be beneficial for improving LLMs without requiring additional human annotation beyond the initial SFT dataset."
    ],
    "durationSeconds": 8.130561173000002
  }
}
```

</details>

---

### Assistant

_source line 31_

<details><summary>Logged reasoning block</summary>

```text
I still couldn't find the Drayson paper. Let me try more specific searches. The user describes it as the most direct predecessor work, with detect-and-reweight approach where b is a heuristic hyperparameter. Let me try different search angles.

Also, I got the arxiv 2602.16065 info - "Can Generative Artificial Intelligence Survive Data Contamination? Theoretical Guarantees under Contaminated Recursive Training" by Kevin Wang, Hongqian Niu, Didong Li. February 2026.


Let me refine my search strategy for the Drayson paper with some different keyword combinations.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "0a05528b-d05d-4fb3-947f-20e0adce1e25",
  "uuid": "9aa0e557-e221-4df0-bea6-d5cb76facba3",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BF2jNWa8Avx1r9PA2GAp7p",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 854,
      "cache_creation_input_tokens": 3092,
      "cache_read_input_tokens": 33946,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3092
      },
      "output_tokens": 9,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Assistant

_source line 32_

Still can't find Drayson. Let me try more specific searches.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "0a05528b-d05d-4fb3-947f-20e0adce1e25",
  "uuid": "4c40a1bf-f89f-46f2-a22c-8c6f4570204c",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BF2jNWa8Avx1r9PA2GAp7p",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 854,
      "cache_creation_input_tokens": 3092,
      "cache_read_input_tokens": 33946,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3092
      },
      "output_tokens": 9,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool call

_source line 33_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01DWQ9vHVaN6T7FSACY58HTi`</summary>

```json
{
  "query": "\"detect-and-reweight\" synthetic data contamination pretraining 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "0a05528b-d05d-4fb3-947f-20e0adce1e25",
  "uuid": "71c60c62-4387-4c07-a835-0ff85287b86d",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BF2jNWa8Avx1r9PA2GAp7p",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 854,
      "cache_creation_input_tokens": 3092,
      "cache_read_input_tokens": 33946,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3092
      },
      "output_tokens": 9,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool call

_source line 34_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01EPweqFSpRU25aMo9VVCHp3`</summary>

```json
{
  "query": "Drayson synthetic contamination weighting pretraining heuristic hyperparameter"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "0a05528b-d05d-4fb3-947f-20e0adce1e25",
  "uuid": "1605292c-a0bf-4b4f-8251-22a9711760e1",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BF2jNWa8Avx1r9PA2GAp7p",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 854,
      "cache_creation_input_tokens": 3092,
      "cache_read_input_tokens": 33946,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3092
      },
      "output_tokens": 9,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool result

_source line 35 · 2026-05-14T12:32:25.072Z_

<details><summary>↩ Tool result · `toolu_01EPweqFSpRU25aMo9VVCHp3`</summary>

```text
Web search results for query: "Drayson synthetic contamination weighting pretraining heuristic hyperparameter"

Links: [{"title":"Chemprop: A Machine Learning Package for Chemical Property Prediction | Journal of Chemical Information and Modeling","url":"https://pubs.acs.org/doi/10.1021/acs.jcim.3c01250"},{"title":"Choosing Covariate Balancing Methods for Causal Inference: Practical Insights from a Simulation Study","url":"https://arxiv.org/html/2412.00280v2"},{"title":"Hyperparameter Optimization in Machine Learning","url":"https://arxiv.org/html/2410.22854v3"},{"title":"Synthetic Pretraining | Vintage Data - Pierre-Carl Langlais","url":"https://vintagedata.org/blog/posts/synthetic-pretraining"},{"title":"A primer on using balancing weights to estimate inverse ...","url":"https://pmc.ncbi.nlm.nih.gov/articles/PMC12527280/"},{"title":"Energy-Based Constraint Networks:","url":"https://arxiv.org/pdf/2605.00960"},{"title":"Core","url":"https://fileserver-az.core.ac.uk/download/pdf/237011209.pdf"},{"title":"A Physically Constrained Deep-Learning Fusion Method for Estimating Surface NO2 Concentration from Satellite and Ground Monitors | Environmental Science & Technology","url":"https://pubs.acs.org/doi/10.1021/acs.est.4c07341"},{"title":"[2405.17535] Calibrated Dataset Condensation for Faster Hyperparameter Search","url":"https://arxiv.org/abs/2405.17535"},{"title":"Hyperparameter Optimization with Neural Network Pruning","url":"https://arxiv.org/pdf/2205.08695"}]

The search results don't appear to contain specific information about "Drayson synthetic contamination weighting pretraining heuristic hyperparameter." The results returned contain general information about hyperparameter optimization, synthetic pretraining, and related machine learning concepts, but nothing specifically matching that query phrase.

It's possible that:

1. This might be a very specific research concept or paper that isn't widely indexed
2. The exact phrase combination may not appear in available sources
3. It could be a technical term from a specific research domain that hasn't been published online yet

Could you provide more context about what you're looking for? For example:
- Is this from a specific research paper or researcher?
- What field or domain is this related to (machine learning, chemistry, biology, etc.)?
- Do you have any additional details about where you encountered this term?

This would help me conduct a more targeted search for the information you need.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "0a05528b-d05d-4fb3-947f-20e0adce1e25",
  "uuid": "2c00e9e3-0740-45e9-b329-2be5ca71ddf3",
  "tool_use_result": {
    "query": "Drayson synthetic contamination weighting pretraining heuristic hyperparameter",
    "results": [
      {
        "tool_use_id": "srvtoolu_01538iKfPxzNWTpFBWE7kSfd",
        "content": [
          {
            "title": "Chemprop: A Machine Learning Package for Chemical Property Prediction | Journal of Chemical Information and Modeling",
            "url": "https://pubs.acs.org/doi/10.1021/acs.jcim.3c01250"
          },
          {
            "title": "Choosing Covariate Balancing Methods for Causal Inference: Practical Insights from a Simulation Study",
            "url": "https://arxiv.org/html/2412.00280v2"
          },
          {
            "title": "Hyperparameter Optimization in Machine Learning",
            "url": "https://arxiv.org/html/2410.22854v3"
          },
          {
            "title": "Synthetic Pretraining | Vintage Data - Pierre-Carl Langlais",
            "url": "https://vintagedata.org/blog/posts/synthetic-pretraining"
          },
          {
            "title": "A primer on using balancing weights to estimate inverse ...",
            "url": "https://pmc.ncbi.nlm.nih.gov/articles/PMC12527280/"
          },
          {
            "title": "Energy-Based Constraint Networks:",
            "url": "https://arxiv.org/pdf/2605.00960"
          },
          {
            "title": "Core",
            "url": "https://fileserver-az.core.ac.uk/download/pdf/237011209.pdf"
          },
          {
            "title": "A Physically Constrained Deep-Learning Fusion Method for Estimating Surface NO2 Concentration from Satellite and Ground Monitors | Environmental Science & Technology",
            "url": "https://pubs.acs.org/doi/10.1021/acs.est.4c07341"
          },
          {
            "title": "[2405.17535] Calibrated Dataset Condensation for Faster Hyperparameter Search",
            "url": "https://arxiv.org/abs/2405.17535"
          },
          {
            "title": "Hyperparameter Optimization with Neural Network Pruning",
            "url": "https://arxiv.org/pdf/2205.08695"
          }
        ]
      },
      "The search results don't appear to contain specific information about \"Drayson synthetic contamination weighting pretraining heuristic hyperparameter.\" The results returned contain general information about hyperparameter optimization, synthetic pretraining, and related machine learning concepts, but nothing specifically matching that query phrase.\n\nIt's possible that:\n\n1. This might be a very specific research concept or paper that isn't widely indexed\n2. The exact phrase combination may not appear in available sources\n3. It could be a technical term from a specific research domain that hasn't been published online yet\n\nCould you provide more context about what you're looking for? For example:\n- Is this from a specific research paper or researcher?\n- What field or domain is this related to (machine learning, chemistry, biology, etc.)?\n- Do you have any additional details about where you encountered this term?\n\nThis would help me conduct a more targeted search for the information you need."
    ],
    "durationSeconds": 4.437149884999999
  }
}
```

</details>

---

### Tool result

_source line 36 · 2026-05-14T12:32:30.508Z_

<details><summary>↩ Tool result · `toolu_01DWQ9vHVaN6T7FSACY58HTi`</summary>

```text
Web search results for query: ""detect-and-reweight" synthetic data contamination pretraining 2025"

Links: [{"title":"GitHub - lyy1994/awesome-data-contamination: The Paper List on Data Contamination for Large Language Models Evaluation. · GitHub","url":"https://github.com/lyy1994/awesome-data-contamination"},{"title":"A Survey on Data Contamination for Large Language Models","url":"https://arxiv.org/html/2502.14425v2"},{"title":"Detecting Data Contamination in LLMs via In-Context Learning","url":"https://arxiv.org/html/2510.27055v1"},{"title":"Synthetic Pretraining | Vintage Data - Pierre-Carl Langlais","url":"https://vintagedata.org/blog/posts/synthetic-pretraining"},{"title":"[2401.06059] Investigating Data Contamination for Pre-training Language Models","url":"https://arxiv.org/abs/2401.06059"},{"title":"Towards Data Contamination Detection for Modern Large ...","url":"https://aclanthology.org/2025.coling-main.338.pdf"},{"title":"Hierarchical Contamination Detection for Synthetic ...","url":"https://www.arxiv.org/pdf/2511.17602"},{"title":"A Comprehensive Survey of Contamination Detection Methods in Large Language Models","url":"https://arxiv.org/html/2404.00699v4"},{"title":"[2311.09783] Investigating Data Contamination in Modern Benchmarks for Large Language Models","url":"https://arxiv.org/abs/2311.09783"},{"title":"detecting data contamination from reinforcement learning ...","url":"https://arxiv.org/pdf/2510.09259"}]

Based on the search results, I found relevant information about data contamination detection research in 2025, though I didn't find a specific paper with the exact phrase "detect-and-reweight" in the title. However, the search returned several highly relevant papers on synthetic data contamination and detection methods from 2025:

## Key Findings:

**Data Contamination from Synthetic Data:**
Methods that produce high-quality training data introduce contamination risks as generators may inadvertently encode benchmark knowledge through web-scraped pretraining or intentional benchmark inclusion.

**Hierarchical Contamination Detection:**
Rapid scaling of synthetic data generation means that subtle contamination can propagate across training pipelines, systematically inflating evaluation metrics while masking true generalization failures.

**Contamination Detection Methods:**
As of early 2025, there are more than 50 detection techniques and more than 100 relevant papers on contamination detection in LLMs. Contamination detection is categorized into two broad types: open-data and closed-data contamination detection.

**Survey Coverage:**
A comprehensive 2025 survey indicates extensive research on contamination detection methodologies, covering various approaches including membership inference attacks, token probability-based methods, and prompt-based detection techniques.

If you're looking for a specific paper on "detect-and-reweight" methodology, you may want to search on arXiv directly or check recent conference proceedings (ICLR 2025, ACL 2025, COLING 2025) as these results reference multiple 2025 papers on this topic.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "0a05528b-d05d-4fb3-947f-20e0adce1e25",
  "uuid": "bc02e6f2-a7e0-4f94-9576-9899181b8107",
  "tool_use_result": {
    "query": "\"detect-and-reweight\" synthetic data contamination pretraining 2025",
    "results": [
      {
        "tool_use_id": "srvtoolu_01TNWdnHJNDtATaUFYJe2mU3",
        "content": [
          {
            "title": "GitHub - lyy1994/awesome-data-contamination: The Paper List on Data Contamination for Large Language Models Evaluation. · GitHub",
            "url": "https://github.com/lyy1994/awesome-data-contamination"
          },
          {
            "title": "A Survey on Data Contamination for Large Language Models",
            "url": "https://arxiv.org/html/2502.14425v2"
          },
          {
            "title": "Detecting Data Contamination in LLMs via In-Context Learning",
            "url": "https://arxiv.org/html/2510.27055v1"
          },
          {
            "title": "Synthetic Pretraining | Vintage Data - Pierre-Carl Langlais",
            "url": "https://vintagedata.org/blog/posts/synthetic-pretraining"
          },
          {
            "title": "[2401.06059] Investigating Data Contamination for Pre-training Language Models",
            "url": "https://arxiv.org/abs/2401.06059"
          },
          {
            "title": "Towards Data Contamination Detection for Modern Large ...",
            "url": "https://aclanthology.org/2025.coling-main.338.pdf"
          },
          {
            "title": "Hierarchical Contamination Detection for Synthetic ...",
            "url": "https://www.arxiv.org/pdf/2511.17602"
          },
          {
            "title": "A Comprehensive Survey of Contamination Detection Methods in Large Language Models",
            "url": "https://arxiv.org/html/2404.00699v4"
          },
          {
            "title": "[2311.09783] Investigating Data Contamination in Modern Benchmarks for Large Language Models",
            "url": "https://arxiv.org/abs/2311.09783"
          },
          {
            "title": "detecting data contamination from reinforcement learning ...",
            "url": "https://arxiv.org/pdf/2510.09259"
          }
        ]
      },
      "Based on the search results, I found relevant information about data contamination detection research in 2025, though I didn't find a specific paper with the exact phrase \"detect-and-reweight\" in the title. However, the search returned several highly relevant papers on synthetic data contamination and detection methods from 2025:\n\n## Key Findings:\n\n**Data Contamination from Synthetic Data:**\nMethods that produce high-quality training data introduce contamination risks as generators may inadvertently encode benchmark knowledge through web-scraped pretraining or intentional benchmark inclusion.\n\n**Hierarchical Contamination Detection:**\nRapid scaling of synthetic data generation means that subtle contamination can propagate across training pipelines, systematically inflating evaluation metrics while masking true generalization failures.\n\n**Contamination Detection Methods:**\nAs of early 2025, there are more than 50 detection techniques and more than 100 relevant papers on contamination detection in LLMs. Contamination detection is categorized into two broad types: open-data and closed-data contamination detection.\n\n**Survey Coverage:**\nA comprehensive 2025 survey indicates extensive research on contamination detection methodologies, covering various approaches including membership inference attacks, token probability-based methods, and prompt-based detection techniques.\n\nIf you're looking for a specific paper on \"detect-and-reweight\" methodology, you may want to search on arXiv directly or check recent conference proceedings (ICLR 2025, ACL 2025, COLING 2025) as these results reference multiple 2025 papers on this topic."
    ],
    "durationSeconds": 9.992338879000002
  }
}
```

</details>

---

### Assistant

_source line 37_

<details><summary>Logged reasoning block</summary>

```text
Let me also check the project's knowledge files - paper_framing or similar - to see if there's more context on who "Drayson et al." is.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "0a05528b-d05d-4fb3-947f-20e0adce1e25",
  "uuid": "3c1576a6-8749-4983-aa5d-a79efa2c6407",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013a7Q5oZJdusCWCr1jRJw6U",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 707,
      "cache_creation_input_tokens": 1962,
      "cache_read_input_tokens": 37038,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1962
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Assistant

_source line 38_

Let me check the project's knowledge files for more context on "Drayson et al."

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "0a05528b-d05d-4fb3-947f-20e0adce1e25",
  "uuid": "bdf7290f-a1be-4cdc-8039-62a9f74e0756",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013a7Q5oZJdusCWCr1jRJw6U",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 707,
      "cache_creation_input_tokens": 1962,
      "cache_read_input_tokens": 37038,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1962
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool call

_source line 39_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01Bp6yziFHkh3HGcrVfHRGgW`</summary>

```json
{
  "query": "select:mcp__agent-ml-research__read_project_file",
  "max_results": 1
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "0a05528b-d05d-4fb3-947f-20e0adce1e25",
  "uuid": "11279868-1c40-4b44-a6ae-ce57ee57ab2f",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013a7Q5oZJdusCWCr1jRJw6U",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 707,
      "cache_creation_input_tokens": 1962,
      "cache_read_input_tokens": 37038,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1962
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool result

_source line 40 · 2026-05-14T12:32:35.918Z_

<details><summary>↩ Tool result · `toolu_01Bp6yziFHkh3HGcrVfHRGgW`</summary>

````text
```json
{
  "type": "tool_reference",
  "tool_name": "mcp__agent-ml-research__read_project_file"
}
```
````

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "0a05528b-d05d-4fb3-947f-20e0adce1e25",
  "uuid": "92cf6f05-e557-441f-8759-56ccd9d45144",
  "tool_use_result": {
    "matches": [
      "mcp__agent-ml-research__read_project_file"
    ],
    "query": "select:mcp__agent-ml-research__read_project_file",
    "total_deferred_tools": 22
  }
}
```

</details>

---

### Tool call

_source line 41_

<details open><summary>🔧 Tool call — Glob · `toolu_01JDT1cjKb91pkuyrGY63EG7`</summary>

```json
{
  "pattern": "**/*framing*",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "0a05528b-d05d-4fb3-947f-20e0adce1e25",
  "uuid": "ecd177b1-282e-4f79-a246-d231301836e5",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013a7Q5oZJdusCWCr1jRJw6U",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 707,
      "cache_creation_input_tokens": 1962,
      "cache_read_input_tokens": 37038,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1962
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool result

_source line 42 · 2026-05-14T12:32:37.906Z_

<details><summary>↩ Tool result · `toolu_01JDT1cjKb91pkuyrGY63EG7`</summary>

```text
paper_framing.md
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "0a05528b-d05d-4fb3-947f-20e0adce1e25",
  "uuid": "2cc5a650-0a70-4ddc-ba36-832dd20ab937",
  "tool_use_result": {
    "filenames": [
      "paper_framing.md"
    ],
    "durationMs": 9,
    "numFiles": 1,
    "truncated": false
  }
}
```

</details>

---

### Tool call

_source line 43_

<details open><summary>🔧 Tool call — Grep · `toolu_01PSHkavdkbuSQCYv7CFkvuL`</summary>

```json
{
  "pattern": "Drayson",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training",
  "output_mode": "files_with_matches"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "0a05528b-d05d-4fb3-947f-20e0adce1e25",
  "uuid": "41b28cbf-6672-4233-89f5-962487c38fd9",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013a7Q5oZJdusCWCr1jRJw6U",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 707,
      "cache_creation_input_tokens": 1962,
      "cache_read_input_tokens": 37038,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1962
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool result

_source line 44 · 2026-05-14T12:32:38.569Z_

<details><summary>↩ Tool result · `toolu_01PSHkavdkbuSQCYv7CFkvuL`</summary>

```text
Found 30 files
logs/workers/worker_research_related_work_supplement_20260514T123126.log
logs/chats/feishu_group_oc_2b6c9bea33a70c93bf4bf04ac36b8df9_director.jsonl
logs/chats/feishu_group_oc_39371eead41d9df941b3542b7f23b377.jsonl
logs/chats/feishu_group_oc_39371eead41d9df941b3542b7f23b377_reviewer.jsonl
logs/chats/archive/feishu_group_oc_2b6c9bea33a70c93bf4bf04ac36b8df9_director_20260514T104857_654704.jsonl
logs/workers/worker_ops_verify-contamination-ratio_20260514T093910.log
logs/workers/worker_ops_diagnostic-status-and-eval_20260514T084518.log
logs/workers/worker_eval_contamination-sensitivity-v2_20260514T081710.log
logs/chats/worker_eval_contamination-sensitivity-diagnostic_20260514T080933.jsonl
logs/workers/worker_eval_contamination-sensitivity-diagnostic_20260514T080933.log
paper_framing.md
logs/workers/worker_eval_mvp-held-out-perplexity_20260514T070406.log
logs/chats/archive/feishu_group_oc_39371eead41d9df941b3542b7f23b377_reviewer_20260514T065255_458039.jsonl
logs/workers/worker_code_check-grid-b-split_20260514T024458.log
logs/chats/archive/feishu_group_oc_39371eead41d9df941b3542b7f23b377_reviewer_20260514T021956_383198.jsonl
logs/workers/worker_code_adaptive-b-readiness_20260513T235900.log
logs/workers/worker_code_eval_pipeline_check_20260513T235536.log
logs/chats/archive/feishu_group_oc_39371eead41d9df941b3542b7f23b377_20260513T235325_711314.jsonl
logs/workers/worker_code_verify-adaptive-code_20260513T234937.log
logs/workers/worker_infra_fix-uniform-resubmit_20260513T232214.log
logs/workers/worker_infra_server-check-restart-uniform_20260513T231603.log
artifacts/training/pretrain_weighted.py
logs/chats/archive/feishu_group_oc_39371eead41d9df941b3542b7f23b377_reviewer_20260513T220201_359096.jsonl
logs/chats/archive/feishu_group_oc_2b6c9bea33a70c93bf4bf04ac36b8df9_director_20260513T215534_580228.jsonl
logs/workers/worker_code_sync-fixes_20260513T182522.log
logs/workers/worker_infra_env-setup-sync_20260513T174954.log
logs/workers/worker_code_eval_and_runner_20260513T174428.log
logs/workers/worker_code_alpha_eff_and_training_20260513T174320.log
artifacts/weighting/alpha_eff.py
docs/IDEA_BRIEF.md
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "0a05528b-d05d-4fb3-947f-20e0adce1e25",
  "uuid": "dfd5ddd3-3fdc-4fb1-996f-3e0e45af50e6",
  "tool_use_result": {
    "mode": "files_with_matches",
    "filenames": [
      "logs/workers/worker_research_related_work_supplement_20260514T123126.log",
      "logs/chats/feishu_group_oc_2b6c9bea33a70c93bf4bf04ac36b8df9_director.jsonl",
      "logs/chats/feishu_group_oc_39371eead41d9df941b3542b7f23b377.jsonl",
      "logs/chats/feishu_group_oc_39371eead41d9df941b3542b7f23b377_reviewer.jsonl",
      "logs/chats/archive/feishu_group_oc_2b6c9bea33a70c93bf4bf04ac36b8df9_director_20260514T104857_654704.jsonl",
      "logs/workers/worker_ops_verify-contamination-ratio_20260514T093910.log",
      "logs/workers/worker_ops_diagnostic-status-and-eval_20260514T084518.log",
      "logs/workers/worker_eval_contamination-sensitivity-v2_20260514T081710.log",
      "logs/chats/worker_eval_contamination-sensitivity-diagnostic_20260514T080933.jsonl",
      "logs/workers/worker_eval_contamination-sensitivity-diagnostic_20260514T080933.log",
      "paper_framing.md",
      "logs/workers/worker_eval_mvp-held-out-perplexity_20260514T070406.log",
      "logs/chats/archive/feishu_group_oc_39371eead41d9df941b3542b7f23b377_reviewer_20260514T065255_458039.jsonl",
      "logs/workers/worker_code_check-grid-b-split_20260514T024458.log",
      "logs/chats/archive/feishu_group_oc_39371eead41d9df941b3542b7f23b377_reviewer_20260514T021956_383198.jsonl",
      "logs/workers/worker_code_adaptive-b-readiness_20260513T235900.log",
      "logs/workers/worker_code_eval_pipeline_check_20260513T235536.log",
      "logs/chats/archive/feishu_group_oc_39371eead41d9df941b3542b7f23b377_20260513T235325_711314.jsonl",
      "logs/workers/worker_code_verify-adaptive-code_20260513T234937.log",
      "logs/workers/worker_infra_fix-uniform-resubmit_20260513T232214.log",
      "logs/workers/worker_infra_server-check-restart-uniform_20260513T231603.log",
      "artifacts/training/pretrain_weighted.py",
      "logs/chats/archive/feishu_group_oc_39371eead41d9df941b3542b7f23b377_reviewer_20260513T220201_359096.jsonl",
      "logs/chats/archive/feishu_group_oc_2b6c9bea33a70c93bf4bf04ac36b8df9_director_20260513T215534_580228.jsonl",
      "logs/workers/worker_code_sync-fixes_20260513T182522.log",
      "logs/workers/worker_infra_env-setup-sync_20260513T174954.log",
      "logs/workers/worker_code_eval_and_runner_20260513T174428.log",
      "logs/workers/worker_code_alpha_eff_and_training_20260513T174320.log",
      "artifacts/weighting/alpha_eff.py",
      "docs/IDEA_BRIEF.md"
    ],
    "numFiles": 30
  }
}
```

</details>

---

### Tool call

_source line 45_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01Cf6kazsHKo1tthyQ2JiVWe`</summary>

```json
{
  "project": "provenance_weight_training",
  "file": "paper_framing.md",
  "max_chars": 12000
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "0a05528b-d05d-4fb3-947f-20e0adce1e25",
  "uuid": "2d6212f2-a37d-4f60-9d89-fee9ffef5c2f",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017HEtvAaqgqqcpmAZW5fR6Q",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 2356,
      "cache_read_input_tokens": 39000,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2356
      },
      "output_tokens": 46,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool result

_source line 46 · 2026-05-14T12:32:42.714Z_

<details><summary>↩ Tool result · `toolu_01Cf6kazsHKo1tthyQ2JiVWe`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/paper_framing.md\", \"content\": \"# Paper Framing — provenance_weight_training\\n\\n> 状态: DRAFT (MVP 进行中，eval 数据部分就绪)\\n> 最后更新: 2026-05-14 08:00 UTC\\n> 投稿目标: EMNLP 2026 ARR May 25\\n\\n## Core Insight\\n\\n在 web 语料合成文本占比 20-60% 的现实场景下，基于检测器置信度估计有效真实数据比例 α_eff(b)，推导理论启发的最优权重指数 b*，无需网格搜索即可自适应调节训练权重——将 detect-and-reweight 从 heuristic 提升为有原则的方法。\\n\\n收敛理论（arXiv 2602.16065）作为 **motivation**（非 contribution）：bound d(ℙ̂_t, ℙ_0) ≲ t^{−min{p,α}} 启发了 α_eff 的定义和 b* 的推导，但我们不 claim 理论桥接。\\n\\n## Core Claims\\n\\n### Claim 1 (Primary): Adaptive b* 替代 Grid Search\\n从 α_eff(b) 推导的 adaptive b* 在多种污染程度下无需网格搜索即可匹配/超越 grid-searched best-b。\\n\\n- **MVP 证据**: adaptive ×3 seeds vs grid-b ×3 seeds（40% 污染, Qwen3-0.6B, 200M tokens）\\n- **Pass criteria**: adaptive 均值 ≥ 90% grid-search 最优 perplexity 改善量\\n- **状态**: 🔄 Eval 数据部分就绪，等 grid-b 全部 b 值出齐\\n\\n**Eval Perplexity 数据（held-out 纯人类 FineWeb, 4.08M tokens, unweighted）：**\\n\\n| Method | b | Mean PPL | Std | vs Uniform |\\n|--------|---|----------|-----|------------|\\n| Uniform | — | 17.694 | 0.008 | baseline |\\n| **Adaptive** | **b*(batch)** | **17.639** | **0.006** | **-0.055 (-0.31%)** |\\n| Grid_b | 0.5 | 17.651 | — | -0.043 (-0.24%) |\\n| Grid_b | 1.0 | ⏳ | | |\\n| Grid_b | 1.5-5.0 | ⏳ | | |\\n\\n初步排序: adaptive (17.639) > grid_b b=0.5 (17.651) > uniform (17.694)。\\n若 b=0.5 是 grid-best → ratio = 0.055/0.043 = 128% → 远超 90% → **PASS**。\\n\\n**两条 Narrative 路径（待 grid-b 全部出齐后选定）：**\\n- **Path A (adaptive > grid-best)**: \\\"理论启发的 adaptive b* 不仅免去 grid search，还超越 grid-best\\\"——最强 claim\\n- **Path B (adaptive ≈ grid-best, < 0.5% gap)**: \\\"adaptive b* 无需 grid search 即可匹配 grid-best，节省 6× 计算量\\\"——稳健 claim，强调实用价值\\n\\n### Claim 2 (Secondary): Lightweight Detector 足以支撑 Adaptive Reweighting\\n即使用 TF-IDF + logistic regression 级别的简单检测器（AUC≈0.94），adaptive reweighting 仍然有效。q-score 的连续分布（而非二值极化）是方法奏效的关键。\\n\\n- **已有证据**: ModernBERT AUC=0.9998 → q-score 极化 → 不同 b 值无区分度；TF-IDF AUC=0.939 → q-score std=0.374, mid_range_ratio=0.463 → 有意义的权重区分\\n- **Full paper 扩展**: detector quality ablation（多个 AUC 水平下 adaptive vs grid-b 对比）→ 若数据支持，可升级为\\\"检测不确定性越大，adaptive 价值越高\\\"\\n\\n### Claim 3 (Framework): Soft-to-Hard 连续谱统一框架\\n权重函数 w=(1-q)^b 在 b 的取值上形成连续谱：b=0 为均匀加权（无干预），b→∞ 为硬删除（detect-and-remove），b* 为检测器质量驱动的最优操作点。这将 \\\"reweight vs remove\\\" 的二选一问题统一为同一框架下的参数选择。\\n\\n- **呈现方式**: Method section 的核心框架（Algorithm 1 伪代码）\\n- **论证**: \\\"Why reweight, not remove\\\" — 高污染下硬删除的信息损失 + 中间概率样本的过激处理\\n\\n## Narrative Structure\\n\\n**起点**: 实际问题（web 语料 20-60% 为合成文本，不同 LLM 生成，比例未知）\\n**现有方法的不足**: Drayson et al. (EMNLP 2025) 的 detect-and-reweight 有效但 b 是 heuristic hyperparameter；golden-ratio weighting 假设已知比例；Strong Model Collapse 证明 known-proportion mixing 不够\\n**我们的方案**: 从 batch 统计量自适应估计 α_eff(b) 并推导 b*，无需预知比例、无需网格搜索\\n**理论连接**: 收敛 bound 作为 Background/Motivation，α_eff 定义受其启发，但不 claim 理论贡献\\n**Method 呈现**: Algorithm 1 (adaptive b*) + soft-to-hard 连续谱 + ESS 约束\\n\\n## Contribution Structure (2 Core + 1 Supporting)\\n\\n1. **Core 1 — Algorithm**: Adaptive reweighting with convergence-inspired b* (Algorithm 1, soft-to-hard continuum)\\n2. **Core 2 — Pipeline**: First end-to-end pipeline for unlabeled multi-generator web contamination with estimated (not assumed-known) fractions\\n3. **Supporting — Empirical characterization**: Theory-practice gap tightness analysis via dual-metric validation (Wasserstein/MMD vs cross-entropy)\\n\\n## Anticipated Reviewer Concerns\\n\\n| Concern | Response Strategy | 实验支撑 |\\n|---------|------------------|----------|\\n| \\\"Incremental over Drayson et al.\\\" | soft-to-hard 框架提升概念层次 + adaptive 消除 grid search + multi-generator | Claim 1 + Claim 3 |\\n| \\\"Theory not rigorous / overclaimed\\\" | 明确 scope disclaimer: motivation not contribution; \\\"Testable Sufficient Condition\\\" not theorem | Background section |\\n| \\\"Only 0.6B model, would it scale?\\\" | Full paper: Llama-3.2-3B 验证 | 扩展实验 |\\n| \\\"Detector quality sensitivity\\\" | Claim 2 + calibration analysis + robustness ablation | detector quality ablation |\\n| \\\"Controlled injection ≠ real web\\\" | Full paper: domain-skewed injection + semi-realistic profile (Binoculars on Common Crawl) | 扩展实验 |\\n| \\\"Why reweight, not just remove?\\\" | Claim 3: 信息损失论证 + hard removal 作为 b→∞ 极端 | soft-to-hard ablation |\\n\\n## Key Risks\\n\\n1. **Novelty ceiling**: 底层仍是 importance weighting，审稿人可能认为 incremental。应对：soft-to-hard 框架 + surprising empirical findings\\n2. **Venue fit**: 核心逻辑偏 ML，EMNLP reviewer 可能低估。应对：加 NLP-specific analysis (linguistic diversity, cross-generator transfer)\\n3. **Single contamination level in MVP**: 40% 一个点不够 generalize。应对：full matrix 覆盖 20%/40%/60%\\n4. **效应量小 (0.3% relative PPL)**: 如果 grid-b 效应也在同量级，说明 40% 污染对 0.6B/200M 本身影响有限。应对策略：(a) 核心 claim 转向\\\"方法正确性 + grid search 替代\\\"而非\\\"大幅性能提升\\\"；(b) full paper 加更高污染比例(60%)和更大模型(3B)展示效应放大；(c) 强调 adaptive 的 zero-cost advantage（同等性能但不需要 6× grid search）\\n\\n## MVP → Full Paper 扩展路径\\n\\n| 维度 | MVP | Full Paper |\\n|------|-----|-----------|\\n| 污染比例 | 40% | 20%, 40%, 60% |\\n| 模型 | Qwen3-0.6B | + Llama-3.2-3B |\\n| 生成器 | Qwen3-0.6B (self) | + Llama-3.2-1B, Mistral, Gemma |\\n| 检测器 | TF-IDF + LR | + ModernBERT variants (quality ablation) |\\n| Baseline | uniform, grid-b, adaptive | + detect-and-remove, random reweighting, perplexity filter, DSIR, loss-based DRO, oracle |\\n| 评估 | train_loss (perplexity) | + MMLU, HellaSwag, Self-BLEU, distinct-n, Wasserstein, MMD |\\n| 注入方式 | uniform random | + domain-skewed, semi-realistic |\\n\", \"total_chars\": 5174, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "0a05528b-d05d-4fb3-947f-20e0adce1e25",
  "uuid": "d4044c8b-f7ed-4dc6-afe2-8191f61d52fc",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"path\\\": \\\"/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/paper_framing.md\\\", \\\"content\\\": \\\"# Paper Framing — provenance_weight_training\\\\n\\\\n> 状态: DRAFT (MVP 进行中，eval 数据部分就绪)\\\\n> 最后更新: 2026-05-14 08:00 UTC\\\\n> 投稿目标: EMNLP 2026 ARR May 25\\\\n\\\\n## Core Insight\\\\n\\\\n在 web 语料合成文本占比 20-60% 的现实场景下，基于检测器置信度估计有效真实数据比例 α_eff(b)，推导理论启发的最优权重指数 b*，无需网格搜索即可自适应调节训练权重——将 detect-and-reweight 从 heuristic 提升为有原则的方法。\\\\n\\\\n收敛理论（arXiv 2602.16065）作为 **motivation**（非 contribution）：bound d(ℙ̂_t, ℙ_0) ≲ t^{−min{p,α}} 启发了 α_eff 的定义和 b* 的推导，但我们不 claim 理论桥接。\\\\n\\\\n## Core Claims\\\\n\\\\n### Claim 1 (Primary): Adaptive b* 替代 Grid Search\\\\n从 α_eff(b) 推导的 adaptive b* 在多种污染程度下无需网格搜索即可匹配/超越 grid-searched best-b。\\\\n\\\\n- **MVP 证据**: adaptive ×3 seeds vs grid-b ×3 seeds（40% 污染, Qwen3-0.6B, 200M tokens）\\\\n- **Pass criteria**: adaptive 均值 ≥ 90% grid-search 最优 perplexity 改善量\\\\n- **状态**: 🔄 Eval 数据部分就绪，等 grid-b 全部 b 值出齐\\\\n\\\\n**Eval Perplexity 数据（held-out 纯人类 FineWeb, 4.08M tokens, unweighted）：**\\\\n\\\\n| Method | b | Mean PPL | Std | vs Uniform |\\\\n|--------|---|----------|-----|------------|\\\\n| Uniform | — | 17.694 | 0.008 | baseline |\\\\n| **Adaptive** | **b*(batch)** | **17.639** | **0.006** | **-0.055 (-0.31%)** |\\\\n| Grid_b | 0.5 | 17.651 | — | -0.043 (-0.24%) |\\\\n| Grid_b | 1.0 | ⏳ | | |\\\\n| Grid_b | 1.5-5.0 | ⏳ | | |\\\\n\\\\n初步排序: adaptive (17.639) > grid_b b=0.5 (17.651) > uniform (17.694)。\\\\n若 b=0.5 是 grid-best → ratio = 0.055/0.043 = 128% → 远超 90% → **PASS**。\\\\n\\\\n**两条 Narrative 路径（待 grid-b 全部出齐后选定）：**\\\\n- **Path A (adaptive > grid-best)**: \\\\\\\"理论启发的 adaptive b* 不仅免去 grid search，还超越 grid-best\\\\\\\"——最强 claim\\\\n- **Path B (adaptive ≈ grid-best, < 0.5% gap)**: \\\\\\\"adaptive b* 无需 grid search 即可匹配 grid-best，节省 6× 计算量\\\\\\\"——稳健 claim，强调实用价值\\\\n\\\\n### Claim 2 (Secondary): Lightweight Detector 足以支撑 Adaptive Reweighting\\\\n即使用 TF-IDF + logistic regression 级别的简单检测器（AUC≈0.94），adaptive reweighting 仍然有效。q-score 的连续分布（而非二值极化）是方法奏效的关键。\\\\n\\\\n- **已有证据**: ModernBERT AUC=0.9998 → q-score 极化 → 不同 b 值无区分度；TF-IDF AUC=0.939 → q-score std=0.374, mid_range_ratio=0.463 → 有意义的权重区分\\\\n- **Full paper 扩展**: detector quality ablation（多个 AUC 水平下 adaptive vs grid-b 对比）→ 若数据支持，可升级为\\\\\\\"检测不确定性越大，adaptive 价值越高\\\\\\\"\\\\n\\\\n### Claim 3 (Framework): Soft-to-Hard 连续谱统一框架\\\\n权重函数 w=(1-q)^b 在 b 的取值上形成连续谱：b=0 为均匀加权（无干预），b→∞ 为硬删除（detect-and-remove），b* 为检测器质量驱动的最优操作点。这将 \\\\\\\"reweight vs remove\\\\\\\" 的二选一问题统一为同一框架下的参数选择。\\\\n\\\\n- **呈现方式**: Method section 的核心框架（Algorithm 1 伪代码）\\\\n- **论证**: \\\\\\\"Why reweight, not remove\\\\\\\" — 高污染下硬删除的信息损失 + 中间概率样本的过激处理\\\\n\\\\n## Narrative Structure\\\\n\\\\n**起点**: 实际问题（web 语料 20-60% 为合成文本，不同 LLM 生成，比例未知）\\\\n**现有方法的不足**: Drayson et al. (EMNLP 2025) 的 detect-and-reweight 有效但 b 是 heuristic hyperparameter；golden-ratio weighting 假设已知比例；Strong Model Collapse 证明 known-proportion mixing 不够\\\\n**我们的方案**: 从 batch 统计量自适应估计 α_eff(b) 并推导 b*，无需预知比例、无需网格搜索\\\\n**理论连接**: 收敛 bound 作为 Background/Motivation，α_eff 定义受其启发，但不 claim 理论贡献\\\\n**Method 呈现**: Algorithm 1 (adaptive b*) + soft-to-hard 连续谱 + ESS 约束\\\\n\\\\n## Contribution Structure (2 Core + 1 Supporting)\\\\n\\\\n1. **Core 1 — Algorithm**: Adaptive reweighting with convergence-inspired b* (Algorithm 1, soft-to-hard continuum)\\\\n2. **Core 2 — Pipeline**: First end-to-end pipeline for unlabeled multi-generator web contamination with estimated (not assumed-known) fractions\\\\n3. **Supporting — Empirical characterization**: Theory-practice gap tightness analysis via dual-metric validation (Wasserstein/MMD vs cross-entropy)\\\\n\\\\n## Anticipated Reviewer Concerns\\\\n\\\\n| Concern | Response Strategy | 实验支撑 |\\\\n|---------|------------------|----------|\\\\n| \\\\\\\"Incremental over Drayson et al.\\\\\\\" | soft-to-hard 框架提升概念层次 + adaptive 消除 grid search + multi-generator | Claim 1 + Claim 3 |\\\\n| \\\\\\\"Theory not rigorous / overclaimed\\\\\\\" | 明确 scope disclaimer: motivation not contribution; \\\\\\\"Testable Sufficient Condition\\\\\\\" not theorem | Background section |\\\\n| \\\\\\\"Only 0.6B model, would it scale?\\\\\\\" | Full paper: Llama-3.2-3B 验证 | 扩展实验 |\\\\n| \\\\\\\"Detector quality sensitivity\\\\\\\" | Claim 2 + calibration analysis + robustness ablation | detector quality ablation |\\\\n| \\\\\\\"Controlled injection ≠ real web\\\\\\\" | Full paper: domain-skewed injection + semi-realistic profile (Binoculars on Common Crawl) | 扩展实验 |\\\\n| \\\\\\\"Why reweight, not just remove?\\\\\\\" | Claim 3: 信息损失论证 + hard removal 作为 b→∞ 极端 | soft-to-hard ablation |\\\\n\\\\n## Key Risks\\\\n\\\\n1. **Novelty ceiling**: 底层仍是 importance weighting，审稿人可能认为 incremental。应对：soft-to-hard 框架 + surprising empirical findings\\\\n2. **Venue fit**: 核心逻辑偏 ML，EMNLP reviewer 可能低估。应对：加 NLP-specific analysis (linguistic diversity, cross-generator transfer)\\\\n3. **Single contamination level in MVP**: 40% 一个点不够 generalize。应对：full matrix 覆盖 20%/40%/60%\\\\n4. **效应量小 (0.3% relative PPL)**: 如果 grid-b 效应也在同量级，说明 40% 污染对 0.6B/200M 本身影响有限。应对策略：(a) 核心 claim 转向\\\\\\\"方法正确性 + grid search 替代\\\\\\\"而非\\\\\\\"大幅性能提升\\\\\\\"；(b) full paper 加更高污染比例(60%)和更大模型(3B)展示效应放大；(c) 强调 adaptive 的 zero-cost advantage（同等性能但不需要 6× grid search）\\\\n\\\\n## MVP → Full Paper 扩展路径\\\\n\\\\n| 维度 | MVP | Full Paper |\\\\n|------|-----|-----------|\\\\n| 污染比例 | 40% | 20%, 40%, 60% |\\\\n| 模型 | Qwen3-0.6B | + Llama-3.2-3B |\\\\n| 生成器 | Qwen3-0.6B (self) | + Llama-3.2-1B, Mistral, Gemma |\\\\n| 检测器 | TF-IDF + LR | + ModernBERT variants (quality ablation) |\\\\n| Baseline | uniform, grid-b, adaptive | + detect-and-remove, random reweighting, perplexity filter, DSIR, loss-based DRO, oracle |\\\\n| 评估 | train_loss (perplexity) | + MMLU, HellaSwag, Self-BLEU, distinct-n, Wasserstein, MMD |\\\\n| 注入方式 | uniform random | + domain-skewed, semi-realistic |\\\\n\\\", \\\"total_chars\\\": 5174, \\\"truncated\\\": false}, \\\"error\\\": null, \\\"metadata\\\": {}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/paper_framing.md\", \"content\": \"# Paper Framing — provenance_weight_training\\n\\n> 状态: DRAFT (MVP 进行中，eval 数据部分就绪)\\n> 最后更新: 2026-05-14 08:00 UTC\\n> 投稿目标: EMNLP 2026 ARR May 25\\n\\n## Core Insight\\n\\n在 web 语料合成文本占比 20-60% 的现实场景下，基于检测器置信度估计有效真实数据比例 α_eff(b)，推导理论启发的最优权重指数 b*，无需网格搜索即可自适应调节训练权重——将 detect-and-reweight 从 heuristic 提升为有原则的方法。\\n\\n收敛理论（arXiv 2602.16065）作为 **motivation**（非 contribution）：bound d(ℙ̂_t, ℙ_0) ≲ t^{−min{p,α}} 启发了 α_eff 的定义和 b* 的推导，但我们不 claim 理论桥接。\\n\\n## Core Claims\\n\\n### Claim 1 (Primary): Adaptive b* 替代 Grid Search\\n从 α_eff(b) 推导的 adaptive b* 在多种污染程度下无需网格搜索即可匹配/超越 grid-searched best-b。\\n\\n- **MVP 证据**: adaptive ×3 seeds vs grid-b ×3 seeds（40% 污染, Qwen3-0.6B, 200M tokens）\\n- **Pass criteria**: adaptive 均值 ≥ 90% grid-search 最优 perplexity 改善量\\n- **状态**: 🔄 Eval 数据部分就绪，等 grid-b 全部 b 值出齐\\n\\n**Eval Perplexity 数据（held-out 纯人类 FineWeb, 4.08M tokens, unweighted）：**\\n\\n| Method | b | Mean PPL | Std | vs Uniform |\\n|--------|---|----------|-----|------------|\\n| Uniform | — | 17.694 | 0.008 | baseline |\\n| **Adaptive** | **b*(batch)** | **17.639** | **0.006** | **-0.055 (-0.31%)** |\\n| Grid_b | 0.5 | 17.651 | — | -0.043 (-0.24%) |\\n| Grid_b | 1.0 | ⏳ | | |\\n| Grid_b | 1.5-5.0 | ⏳ | | |\\n\\n初步排序: adaptive (17.639) > grid_b b=0.5 (17.651) > uniform (17.694)。\\n若 b=0.5 是 grid-best → ratio = 0.055/0.043 = 128% → 远超 90% → **PASS**。\\n\\n**两条 Narrative 路径（待 grid-b 全部出齐后选定）：**\\n- **Path A (adaptive > grid-best)**: \\\"理论启发的 adaptive b* 不仅免去 grid search，还超越 grid-best\\\"——最强 claim\\n- **Path B (adaptive ≈ grid-best, < 0.5% gap)**: \\\"adaptive b* 无需 grid search 即可匹配 grid-best，节省 6× 计算量\\\"——稳健 claim，强调实用价值\\n\\n### Claim 2 (Secondary): Lightweight Detector 足以支撑 Adaptive Reweighting\\n即使用 TF-IDF + logistic regression 级别的简单检测器（AUC≈0.94），adaptive reweighting 仍然有效。q-score 的连续分布（而非二值极化）是方法奏效的关键。\\n\\n- **已有证据**: ModernBERT AUC=0.9998 → q-score 极化 → 不同 b 值无区分度；TF-IDF AUC=0.939 → q-score std=0.374, mid_range_ratio=0.463 → 有意义的权重区分\\n- **Full paper 扩展**: detector quality ablation（多个 AUC 水平下 adaptive vs grid-b 对比）→ 若数据支持，可升级为\\\"检测不确定性越大，adaptive 价值越高\\\"\\n\\n### Claim 3 (Framework): Soft-to-Hard 连续谱统一框架\\n权重函数 w=(1-q)^b 在 b 的取值上形成连续谱：b=0 为均匀加权（无干预），b→∞ 为硬删除（detect-and-remove），b* 为检测器质量驱动的最优操作点。这将 \\\"reweight vs remove\\\" 的二选一问题统一为同一框架下的参数选择。\\n\\n- **呈现方式**: Method section 的核心框架（Algorithm 1 伪代码）\\n- **论证**: \\\"Why reweight, not remove\\\" — 高污染下硬删除的信息损失 + 中间概率样本的过激处理\\n\\n## Narrative Structure\\n\\n**起点**: 实际问题（web 语料 20-60% 为合成文本，不同 LLM 生成，比例未知）\\n**现有方法的不足**: Drayson et al. (EMNLP 2025) 的 detect-and-reweight 有效但 b 是 heuristic hyperparameter；golden-ratio weighting 假设已知比例；Strong Model Collapse 证明 known-proportion mixing 不够\\n**我们的方案**: 从 batch 统计量自适应估计 α_eff(b) 并推导 b*，无需预知比例、无需网格搜索\\n**理论连接**: 收敛 bound 作为 Background/Motivation，α_eff 定义受其启发，但不 claim 理论贡献\\n**Method 呈现**: Algorithm 1 (adaptive b*) + soft-to-hard 连续谱 + ESS 约束\\n\\n## Contribution Structure (2 Core + 1 Supporting)\\n\\n1. **Core 1 — Algorithm**: Adaptive reweighting with convergence-inspired b* (Algorithm 1, soft-to-hard continuum)\\n2. **Core 2 — Pipeline**: First end-to-end pipeline for unlabeled multi-generator web contamination with estimated (not assumed-known) fractions\\n3. **Supporting — Empirical characterization**: Theory-practice gap tightness analysis via dual-metric validation (Wasserstein/MMD vs cross-entropy)\\n\\n## Anticipated Reviewer Concerns\\n\\n| Concern | Response Strategy | 实验支撑 |\\n|---------|------------------|----------|\\n| \\\"Incremental over Drayson et al.\\\" | soft-to-hard 框架提升概念层次 + adaptive 消除 grid search + multi-generator | Claim 1 + Claim 3 |\\n| \\\"Theory not rigorous / overclaimed\\\" | 明确 scope disclaimer: motivation not contribution; \\\"Testable Sufficient Condition\\\" not theorem | Background section |\\n| \\\"Only 0.6B model, would it scale?\\\" | Full paper: Llama-3.2-3B 验证 | 扩展实验 |\\n| \\\"Detector quality sensitivity\\\" | Claim 2 + calibration analysis + robustness ablation | detector quality ablation |\\n| \\\"Controlled injection ≠ real web\\\" | Full paper: domain-skewed injection + semi-realistic profile (Binoculars on Common Crawl) | 扩展实验 |\\n| \\\"Why reweight, not just remove?\\\" | Claim 3: 信息损失论证 + hard removal 作为 b→∞ 极端 | soft-to-hard ablation |\\n\\n## Key Risks\\n\\n1. **Novelty ceiling**: 底层仍是 importance weighting，审稿人可能认为 incremental。应对：soft-to-hard 框架 + surprising empirical findings\\n2. **Venue fit**: 核心逻辑偏 ML，EMNLP reviewer 可能低估。应对：加 NLP-specific analysis (linguistic diversity, cross-generator transfer)\\n3. **Single contamination level in MVP**: 40% 一个点不够 generalize。应对：full matrix 覆盖 20%/40%/60%\\n4. **效应量小 (0.3% relative PPL)**: 如果 grid-b 效应也在同量级，说明 40% 污染对 0.6B/200M 本身影响有限。应对策略：(a) 核心 claim 转向\\\"方法正确性 + grid search 替代\\\"而非\\\"大幅性能提升\\\"；(b) full paper 加更高污染比例(60%)和更大模型(3B)展示效应放大；(c) 强调 adaptive 的 zero-cost advantage（同等性能但不需要 6× grid search）\\n\\n## MVP → Full Paper 扩展路径\\n\\n| 维度 | MVP | Full Paper |\\n|------|-----|-----------|\\n| 污染比例 | 40% | 20%, 40%, 60% |\\n| 模型 | Qwen3-0.6B | + Llama-3.2-3B |\\n| 生成器 | Qwen3-0.6B (self) | + Llama-3.2-1B, Mistral, Gemma |\\n| 检测器 | TF-IDF + LR | + ModernBERT variants (quality ablation) |\\n| Baseline | uniform, grid-b, adaptive | + detect-and-remove, random reweighting, perplexity filter, DSIR, loss-based DRO, oracle |\\n| 评估 | train_loss (perplexity) | + MMLU, HellaSwag, Self-BLEU, distinct-n, Wasserstein, MMD |\\n| 注入方式 | uniform random | + domain-skewed, semi-realistic |\\n\", \"total_chars\": 5174, \"truncated\": false}, \"error\": null, \"metadata\": {}}"
    }
  }
}
```

</details>

---

### Assistant

_source line 47_

<details><summary>Logged reasoning block</summary>

```text
Now I have the paper_framing context. It references "Drayson et al. (EMNLP 2025)" as a direct predecessor. Let me try one more search to find this paper specifically. The framing mentions "detect-and-reweight" and "Drayson et al." Let me search with different terms.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "0a05528b-d05d-4fb3-947f-20e0adce1e25",
  "uuid": "94c47a71-75e8-45d0-ae90-cfbc7025b7ef",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LwesawUpWf6dW5BUqLc1KJ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3002,
      "cache_read_input_tokens": 41356,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3002
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Assistant

_source line 48_

Let me try more targeted searches for the Drayson paper.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "0a05528b-d05d-4fb3-947f-20e0adce1e25",
  "uuid": "907c7457-f16a-4130-83ec-f3967ef6654e",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LwesawUpWf6dW5BUqLc1KJ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3002,
      "cache_read_input_tokens": 41356,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3002
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool call

_source line 49_

<details open><summary>🔧 Tool call — WebSearch · `toolu_015F15F7xZ5CVmZAey3EYkB6`</summary>

```json
{
  "query": "Drayson EMNLP 2025 reweighting LLM training synthetic"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "0a05528b-d05d-4fb3-947f-20e0adce1e25",
  "uuid": "6867364c-a0d4-4c3d-9bbf-8dd730c61460",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LwesawUpWf6dW5BUqLc1KJ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3002,
      "cache_read_input_tokens": 41356,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3002
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool call

_source line 50_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01CvDJbx2n6xrbZ5ff3QYgiU`</summary>

```json
{
  "query": "\"Drayson\" machine learning 2025 weighting synthetic data detection"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "0a05528b-d05d-4fb3-947f-20e0adce1e25",
  "uuid": "a07bc6ef-79e9-4f8c-8704-4a5653085ed0",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LwesawUpWf6dW5BUqLc1KJ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3002,
      "cache_read_input_tokens": 41356,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3002
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool result

_source line 51 · 2026-05-14T12:32:53.944Z_

<details><summary>↩ Tool result · `toolu_015F15F7xZ5CVmZAey3EYkB6`</summary>

```text
Web search results for query: "Drayson EMNLP 2025 reweighting LLM training synthetic"

Links: [{"title":"Demystifying Synthetic Data in LLM Pre-training","url":"https://aclanthology.org/2025.emnlp-main.544.pdf"},{"title":"Demystifying Synthetic Data in LLM Pre-training: A Systematic Study of Scaling Laws, Benefits, and Pitfalls | Cool Papers - Immersive Paper Discovery","url":"https://papers.cool/venue/2025.emnlp-main.544@ACL"},{"title":"DORM: Preference Data Weights Optimization for Reward ...","url":"https://aclanthology.org/2025.findings-emnlp.1237.pdf"},{"title":"Demystifying Synthetic Data in LLM Pre-training: A Systematic Study of Scaling Laws, Benefits, and Pitfalls - ACL Anthology","url":"https://aclanthology.org/2025.emnlp-main.544/"},{"title":"Scaling Low-Resource MT via Synthetic Data Generation ...","url":"https://aclanthology.org/2025.emnlp-main.1408.pdf"},{"title":"Accepted Findings Papers - EMNLP 2025","url":"https://2025.emnlp.org/program/find_papers/"},{"title":"Synthetic Data in LLM Pre-Training","url":"https://www.emergentmind.com/papers/2510.01631"},{"title":"Reinforcement Learning for LLM Agent Planning","url":"https://aclanthology.org/2025.emnlp-industry.116.pdf"},{"title":"iTool: Reinforced Fine-Tuning with Dynamic Deficiency ...","url":"https://aclanthology.org/2025.emnlp-main.701.pdf"},{"title":"[2510.01631] Demystifying Synthetic Data in LLM Pre-training: A Systematic Study of Scaling Laws, Benefits, and Pitfalls","url":"https://arxiv.org/abs/2510.01631"}]

Based on the search results, the query appears to refer to "Demystifying Synthetic Data in LLM Pre-training: A Systematic Study of Scaling Laws, Benefits, and Pitfalls" presented at the 2025 Conference on Empirical Methods in Natural Language Processing. 

However, I should note that the first author of this paper is Feiyang Kang, along with co-authors Newsha Ardalani, Michael Kuchnik, Youssef Emad, Mostafa Elhoushi, Shubhabrata Sengupta, Shang-Wen Li, Ramya Raghavendra, Ruoxi Jia, and Carole-Jean Wu - not someone named Drayson. The search results don't show a paper matching all the terms in your query (specifically with "Drayson" as an author and "reweighting" as a focus).

If you're looking for information about data reweighting techniques for LLM training with synthetic data at EMNLP 2025, there may be a different paper, or the author name might be spelled differently. Would you like me to search with different terms?


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "0a05528b-d05d-4fb3-947f-20e0adce1e25",
  "uuid": "3aef0b18-c8e3-4241-b555-f30bbf0c1f76",
  "tool_use_result": {
    "query": "Drayson EMNLP 2025 reweighting LLM training synthetic",
    "results": [
      {
        "tool_use_id": "srvtoolu_01MBCSb7EHjTcepRW1T6nc7t",
        "content": [
          {
            "title": "Demystifying Synthetic Data in LLM Pre-training",
            "url": "https://aclanthology.org/2025.emnlp-main.544.pdf"
          },
          {
            "title": "Demystifying Synthetic Data in LLM Pre-training: A Systematic Study of Scaling Laws, Benefits, and Pitfalls | Cool Papers - Immersive Paper Discovery",
            "url": "https://papers.cool/venue/2025.emnlp-main.544@ACL"
          },
          {
            "title": "DORM: Preference Data Weights Optimization for Reward ...",
            "url": "https://aclanthology.org/2025.findings-emnlp.1237.pdf"
          },
          {
            "title": "Demystifying Synthetic Data in LLM Pre-training: A Systematic Study of Scaling Laws, Benefits, and Pitfalls - ACL Anthology",
            "url": "https://aclanthology.org/2025.emnlp-main.544/"
          },
          {
            "title": "Scaling Low-Resource MT via Synthetic Data Generation ...",
            "url": "https://aclanthology.org/2025.emnlp-main.1408.pdf"
          },
          {
            "title": "Accepted Findings Papers - EMNLP 2025",
            "url": "https://2025.emnlp.org/program/find_papers/"
          },
          {
            "title": "Synthetic Data in LLM Pre-Training",
            "url": "https://www.emergentmind.com/papers/2510.01631"
          },
          {
            "title": "Reinforcement Learning for LLM Agent Planning",
            "url": "https://aclanthology.org/2025.emnlp-industry.116.pdf"
          },
          {
            "title": "iTool: Reinforced Fine-Tuning with Dynamic Deficiency ...",
            "url": "https://aclanthology.org/2025.emnlp-main.701.pdf"
          },
          {
            "title": "[2510.01631] Demystifying Synthetic Data in LLM Pre-training: A Systematic Study of Scaling Laws, Benefits, and Pitfalls",
            "url": "https://arxiv.org/abs/2510.01631"
          }
        ]
      },
      "Based on the search results, the query appears to refer to \"Demystifying Synthetic Data in LLM Pre-training: A Systematic Study of Scaling Laws, Benefits, and Pitfalls\" presented at the 2025 Conference on Empirical Methods in Natural Language Processing. \n\nHowever, I should note that the first author of this paper is Feiyang Kang, along with co-authors Newsha Ardalani, Michael Kuchnik, Youssef Emad, Mostafa Elhoushi, Shubhabrata Sengupta, Shang-Wen Li, Ramya Raghavendra, Ruoxi Jia, and Carole-Jean Wu - not someone named Drayson. The search results don't show a paper matching all the terms in your query (specifically with \"Drayson\" as an author and \"reweighting\" as a focus).\n\nIf you're looking for information about data reweighting techniques for LLM training with synthetic data at EMNLP 2025, there may be a different paper, or the author name might be spelled differently. Would you like me to search with different terms?"
    ],
    "durationSeconds": 5.595908351000006
  }
}
```

</details>

---

### Tool result

_source line 52 · 2026-05-14T12:32:56.152Z_

<details><summary>↩ Tool result · `toolu_01CvDJbx2n6xrbZ5ff3QYgiU`</summary>

```text
Web search results for query: ""Drayson" machine learning 2025 weighting synthetic data detection"

Links: [{"title":"Advancing APT detection through transformer-driven feature learning and synthetic data generation | Scientific Reports","url":"https://www.nature.com/articles/s41598-026-41317-5"},{"title":"Machine Learning for Synthetic Data Generation: A Review","url":"https://arxiv.org/html/2302.04062v6"},{"title":"In machine learning, synthetic data can offer real performance improvements | MIT News | Massachusetts Institute of Technology","url":"https://news.mit.edu/2022/synthetic-data-ai-improvements-1103"},{"title":"Synthetic data as an enabler for machine learning applications in medicine - PMC","url":"https://pmc.ncbi.nlm.nih.gov/articles/PMC9619172/"},{"title":"The Impact of Synthetic Data on Object Detection Model Performance: A Comparative Analysis with Real-World Data","url":"https://arxiv.org/html/2510.12208v1"},{"title":"Synthetic Data for Deep Learning | Springer Nature Link","url":"https://link.springer.com/book/10.1007/978-3-030-75178-4"},{"title":"Synthetic Data for Deep Learning in Computer Vision & Medical Imaging: A Means to Reduce Data Bias | ACM Computing Surveys","url":"https://dl.acm.org/doi/10.1145/3663759"},{"title":"Evaluating the Impact of Synthetic Data on Object Detection Tasks in Autonomous Driving","url":"https://arxiv.org/html/2503.09803v1"},{"title":"does training with synthetic data truly pro","url":"https://arxiv.org/pdf/2502.12976"},{"title":"[2302.04062] Machine Learning for Synthetic Data Generation: A Review","url":"https://arxiv.org/abs/2302.04062"}]

The search results don't contain specific information about "Drayson" in relation to machine learning, weighting synthetic data detection, or 2025 research. The results show various general studies on synthetic data generation and detection in machine learning, but none appear to reference a researcher or work by "Drayson."

Would you like me to:
1. Search with different terms to find information about Drayson's work?
2. Search for more specific aspects like "Drayson synthetic data weighting" or "Drayson detection method"?
3. Explore related topics on synthetic data detection techniques that might be relevant?

Please let me know how you'd like me to proceed with finding the information you're looking for.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "0a05528b-d05d-4fb3-947f-20e0adce1e25",
  "uuid": "42ae6ba5-a2a6-43cc-b1b9-9789c7d04b74",
  "tool_use_result": {
    "query": "\"Drayson\" machine learning 2025 weighting synthetic data detection",
    "results": [
      {
        "tool_use_id": "srvtoolu_01D4rAkCHA2HzVtTqMKYEScr",
        "content": [
          {
            "title": "Advancing APT detection through transformer-driven feature learning and synthetic data generation | Scientific Reports",
            "url": "https://www.nature.com/articles/s41598-026-41317-5"
          },
          {
            "title": "Machine Learning for Synthetic Data Generation: A Review",
            "url": "https://arxiv.org/html/2302.04062v6"
          },
          {
            "title": "In machine learning, synthetic data can offer real performance improvements | MIT News | Massachusetts Institute of Technology",
            "url": "https://news.mit.edu/2022/synthetic-data-ai-improvements-1103"
          },
          {
            "title": "Synthetic data as an enabler for machine learning applications in medicine - PMC",
            "url": "https://pmc.ncbi.nlm.nih.gov/articles/PMC9619172/"
          },
          {
            "title": "The Impact of Synthetic Data on Object Detection Model Performance: A Comparative Analysis with Real-World Data",
            "url": "https://arxiv.org/html/2510.12208v1"
          },
          {
            "title": "Synthetic Data for Deep Learning | Springer Nature Link",
            "url": "https://link.springer.com/book/10.1007/978-3-030-75178-4"
          },
          {
            "title": "Synthetic Data for Deep Learning in Computer Vision & Medical Imaging: A Means to Reduce Data Bias | ACM Computing Surveys",
            "url": "https://dl.acm.org/doi/10.1145/3663759"
          },
          {
            "title": "Evaluating the Impact of Synthetic Data on Object Detection Tasks in Autonomous Driving",
            "url": "https://arxiv.org/html/2503.09803v1"
          },
          {
            "title": "does training with synthetic data truly pro",
            "url": "https://arxiv.org/pdf/2502.12976"
          },
          {
            "title": "[2302.04062] Machine Learning for Synthetic Data Generation: A Review",
            "url": "https://arxiv.org/abs/2302.04062"
          }
        ]
      },
      "The search results don't contain specific information about \"Drayson\" in relation to machine learning, weighting synthetic data detection, or 2025 research. The results show various general studies on synthetic data generation and detection in machine learning, but none appear to reference a researcher or work by \"Drayson.\"\n\nWould you like me to:\n1. Search with different terms to find information about Drayson's work?\n2. Search for more specific aspects like \"Drayson synthetic data weighting\" or \"Drayson detection method\"?\n3. Explore related topics on synthetic data detection techniques that might be relevant?\n\nPlease let me know how you'd like me to proceed with finding the information you're looking for."
    ],
    "durationSeconds": 7.6225915529999915
  }
}
```

</details>

---

### Assistant

_source line 53_

<details><summary>Logged reasoning block</summary>

```text
I can't find any paper by "Drayson" related to detect-and-reweight for synthetic data. Let me check the project's ideas.md or other files that might reference this paper with more details. Let me also check the IDEA_BRIEF.md or look at chat logs that mention "Drayson".
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "0a05528b-d05d-4fb3-947f-20e0adce1e25",
  "uuid": "ebda3b72-fd34-4338-b1c7-0a3f4206bc34",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UKptDtnewseoPBVaU9uMvj",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1828,
      "cache_read_input_tokens": 44358,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1828
      },
      "output_tokens": 9,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Assistant

_source line 54_

Let me check project files for more details on the Drayson reference.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "0a05528b-d05d-4fb3-947f-20e0adce1e25",
  "uuid": "32c75b3e-3a1e-4353-8acb-65e435cd7854",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UKptDtnewseoPBVaU9uMvj",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1828,
      "cache_read_input_tokens": 44358,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1828
      },
      "output_tokens": 9,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool call

_source line 55_

<details open><summary>🔧 Tool call — Grep · `toolu_017SD4MAK1nq7fVxRU7pqAyb`</summary>

```json
{
  "pattern": "Drayson",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/IDEA_BRIEF.md",
  "output_mode": "content",
  "-C": 3
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "0a05528b-d05d-4fb3-947f-20e0adce1e25",
  "uuid": "60616647-17d1-4a13-8fd5-ee0383635e9e",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UKptDtnewseoPBVaU9uMvj",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1828,
      "cache_read_input_tokens": 44358,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1828
      },
      "output_tokens": 9,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool result

_source line 56 · 2026-05-14T12:33:06.214Z_

<details><summary>↩ Tool result · `toolu_017SD4MAK1nq7fVxRU7pqAyb`</summary>

```text
40-
41-## Core Problem
42-
43:[Omitted long matching line]
44-
45-## Opportunity / Why Now
46-
47:[Omitted long matching line]
48-
49-## Landscape (SOTA & Limitations)
50-
51:[Omitted long matching line]
52-
53-## Proposed Approach
54-
--
56-
57-[Omitted long context line]
58-
59:[Omitted long matching line]
60-
61-[Omitted long context line]
62-
--
76-
77-  b* = inf{b ≥ 0 : α_eff(b) ≥ τ}  subject to  ESS(b*) ≥ n_min
78-
79:where τ = min(p, target_rate) is the rate exponent threshold and n_min is the minimum effective sample size for stable gradient estimates. When the constraints conflict, we solve b* = argmax_b α_eff(b) s.t. ESS(b) ≥ n_min. When batch contamination is low (ρ̂ < 1−τ), we use uniform weights (b=0). This replaces the heuristic grid search over b in Drayson et al. (EMNLP 2025) with an adaptive, batch-dependent schedule.
80-
81-*Step 4 — Concentration argument and calibration correction.* For finite batches, α̂_eff(b) concentrates around its expectation at a rate governed by ESS: |α̂_eff − α_eff| ≤ O(√(w_max / (ESS · Σw_i)) · log(1/δ)) with probability 1−δ. With imperfect detector calibration (expected calibration error ε), we apply a safety margin: τ_adj = τ + c·ε·(b+1) where c is estimated from the calibration curve.
82-
83-If Phase 1 succeeds, we extend: w_i = (1−q(x_i))^b · α^{d̂_i}, incorporating estimated depth d̂_i as a multiplicative adjustment.
84-
85:**Phase 4 — End-to-End Validation with Dual-Metric Evaluation (~145 H100-hours, with data generation explicitly budgeted).** We pretrain Qwen3-0.6B on FineWeb subsets (~2B tokens each) with controlled multi-generator contamination at 20%, 40%, and 60% synthetic fraction, comparing: (a) uniform weighting (no mitigation), (b) heuristic b via grid search à la Drayson et al. (EMNLP 2025), (c) our convergence-informed adaptive b.
86-
87-[Omitted long context line]
88-
--
108-
109-## Key References
110-
111:- Machine-generated text detection prevents language model collapse (Drayson et al., EMNLP 2025 Main Conference) — binary detection + importance resampling baseline using GPT-2 and SmolLM2 (4 LLMs, 2 families, 6 decoding strategies) with single-generator-per-experiment evaluation on WikiText-2; our work extends with convergence-informed calibration, multi-generator cross-contamination evaluation, and web-scale corpora
112-- Can Generative AI Survive Data Contamination? Theoretical Guarantees under Contaminated Recursive Training (arXiv 2602.16065, Feb 2026) — convergence bound d(ℙ̂_t,ℙ_0) ≲ t^{−min{p,α}} we operationalize via the α_eff(b) bridge; Assumption A2 restricts d to convex metrics, explicitly excluding cross-entropy/KL — motivating our dual-metric validation approach
113-- Strong Model Collapse (arXiv 2410.04840, Dohmatob et al., ICLR 2025 Spotlight) — proves even 0.1% synthetic contamination causes collapse under static mixing with known proportions; escape requires p₂→0; our detection-based adaptive reweighting functionally achieves this for detected synthetic samples, differentiating from their known-proportion weighted mixing analysis
114-[Omitted long context line]
--
130-## Reviewer Evaluation
131-
132-**Scores**:
133:  - clarity: **{'rationale': 'Exceptionally well-organized with explicit acknowledgment of all theoretical limitations (A2 metric exclusion, informal theory-practice bridge, Pinsker direction). The framing of α_eff(b) as a hypothesis rather than a theorem is intellectually honest. Differentiation from 6+ related approaches (Drayson et al., Amin et al., Strong Model Collapse, golden-ratio, Schaeffer critique, Fu et al.) is thorough and fair.', 'score': 4}**/5
134-  - feasibility: **{'rationale': '163 H100-hours is well within the 200-hour budget with 37h margin. Both Qwen3-0.6B (Apache 2.0, ungated) and Llama-3.2-1B (gated but accessible) are verified as publicly available. The Phase 3 math is explicit and tractable; pre-registered success criteria with fallback framing make the paper robust to the core hypothesis being weak.', 'score': 4}**/5
135-  - impact: **{'rationale': "Directly addresses the EMNLP 2026 special theme's explicit call for work on 'contamination' and 'synthetic data feedback loops.' The dual-metric validation methodology and depth classifiability investigation are independently valuable contributions regardless of whether convergence-informed b outperforms heuristic b. Provides a principled framework where only heuristics previously existed.", 'score': 4}**/5
136-  - novelty: **{'rationale': 'The integration gap is verified as genuine — no prior work connects the convergence bound of arXiv 2602.16065 to practical weight calibration with estimated (not assumed-known) contamination fractions. The α_eff(b) formulation, ESS-constrained importance weighting for LM training, dual-metric validation methodology, and depth classifiability investigation are all confirmed novel through independent search.', 'score': 4}**/5
--
173-
174-10. [模型规模验证] — 原始仅用 Qwen3-0.6B。增加 Llama-3.2-3B 在 3 个关键 contamination level 的 end-to-end 验证 — 命中 Significance（部分回应 "would findings hold at larger scale" 质疑）。
175-
176:[Omitted long matching line]
177-
178-12. [生态效度补充] — 原始仅有均匀随机注入。增加：(a) domain-skewed injection（domain 间 synthetic 比例 10–80%）；(b) semi-realistic profile（用 Binoculars 对 recent Common Crawl dump 标注子集作为接近真实分布的 contamination profile）— 命中 Significance / Practical Impact（回应 controlled injection ≠ real web 的质疑）。
179-
--
189-
190-【主要风险】:
191-
192:[Omitted long matching line]
193-
194-[Omitted long context line]
195-
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "0a05528b-d05d-4fb3-947f-20e0adce1e25",
  "uuid": "40468ac1-4945-461c-8cf4-7ae771405983",
  "tool_use_result": {
    "mode": "content",
    "numFiles": 0,
    "filenames": [],
    "content": "40-\n41-## Core Problem\n42-\n43:[Omitted long matching line]\n44-\n45-## Opportunity / Why Now\n46-\n47:[Omitted long matching line]\n48-\n49-## Landscape (SOTA & Limitations)\n50-\n51:[Omitted long matching line]\n52-\n53-## Proposed Approach\n54-\n--\n56-\n57-[Omitted long context line]\n58-\n59:[Omitted long matching line]\n60-\n61-[Omitted long context line]\n62-\n--\n76-\n77-  b* = inf{b ≥ 0 : α_eff(b) ≥ τ}  subject to  ESS(b*) ≥ n_min\n78-\n79:where τ = min(p, target_rate) is the rate exponent threshold and n_min is the minimum effective sample size for stable gradient estimates. When the constraints conflict, we solve b* = argmax_b α_eff(b) s.t. ESS(b) ≥ n_min. When batch contamination is low (ρ̂ < 1−τ), we use uniform weights (b=0). This replaces the heuristic grid search over b in Drayson et al. (EMNLP 2025) with an adaptive, batch-dependent schedule.\n80-\n81-*Step 4 — Concentration argument and calibration correction.* For finite batches, α̂_eff(b) concentrates around its expectation at a rate governed by ESS: |α̂_eff − α_eff| ≤ O(√(w_max / (ESS · Σw_i)) · log(1/δ)) with probability 1−δ. With imperfect detector calibration (expected calibration error ε), we apply a safety margin: τ_adj = τ + c·ε·(b+1) where c is estimated from the calibration curve.\n82-\n83-If Phase 1 succeeds, we extend: w_i = (1−q(x_i))^b · α^{d̂_i}, incorporating estimated depth d̂_i as a multiplicative adjustment.\n84-\n85:**Phase 4 — End-to-End Validation with Dual-Metric Evaluation (~145 H100-hours, with data generation explicitly budgeted).** We pretrain Qwen3-0.6B on FineWeb subsets (~2B tokens each) with controlled multi-generator contamination at 20%, 40%, and 60% synthetic fraction, comparing: (a) uniform weighting (no mitigation), (b) heuristic b via grid search à la Drayson et al. (EMNLP 2025), (c) our convergence-informed adaptive b.\n86-\n87-[Omitted long context line]\n88-\n--\n108-\n109-## Key References\n110-\n111:- Machine-generated text detection prevents language model collapse (Drayson et al., EMNLP 2025 Main Conference) — binary detection + importance resampling baseline using GPT-2 and SmolLM2 (4 LLMs, 2 families, 6 decoding strategies) with single-generator-per-experiment evaluation on WikiText-2; our work extends with convergence-informed calibration, multi-generator cross-contamination evaluation, and web-scale corpora\n112-- Can Generative AI Survive Data Contamination? Theoretical Guarantees under Contaminated Recursive Training (arXiv 2602.16065, Feb 2026) — convergence bound d(ℙ̂_t,ℙ_0) ≲ t^{−min{p,α}} we operationalize via the α_eff(b) bridge; Assumption A2 restricts d to convex metrics, explicitly excluding cross-entropy/KL — motivating our dual-metric validation approach\n113-- Strong Model Collapse (arXiv 2410.04840, Dohmatob et al., ICLR 2025 Spotlight) — proves even 0.1% synthetic contamination causes collapse under static mixing with known proportions; escape requires p₂→0; our detection-based adaptive reweighting functionally achieves this for detected synthetic samples, differentiating from their known-proportion weighted mixing analysis\n114-[Omitted long context line]\n--\n130-## Reviewer Evaluation\n131-\n132-**Scores**:\n133:  - clarity: **{'rationale': 'Exceptionally well-organized with explicit acknowledgment of all theoretical limitations (A2 metric exclusion, informal theory-practice bridge, Pinsker direction). The framing of α_eff(b) as a hypothesis rather than a theorem is intellectually honest. Differentiation from 6+ related approaches (Drayson et al., Amin et al., Strong Model Collapse, golden-ratio, Schaeffer critique, Fu et al.) is thorough and fair.', 'score': 4}**/5\n134-  - feasibility: **{'rationale': '163 H100-hours is well within the 200-hour budget with 37h margin. Both Qwen3-0.6B (Apache 2.0, ungated) and Llama-3.2-1B (gated but accessible) are verified as publicly available. The Phase 3 math is explicit and tractable; pre-registered success criteria with fallback framing make the paper robust to the core hypothesis being weak.', 'score': 4}**/5\n135-  - impact: **{'rationale': \"Directly addresses the EMNLP 2026 special theme's explicit call for work on 'contamination' and 'synthetic data feedback loops.' The dual-metric validation methodology and depth classifiability investigation are independently valuable contributions regardless of whether convergence-informed b outperforms heuristic b. Provides a principled framework where only heuristics previously existed.\", 'score': 4}**/5\n136-  - novelty: **{'rationale': 'The integration gap is verified as genuine — no prior work connects the convergence bound of arXiv 2602.16065 to practical weight calibration with estimated (not assumed-known) contamination fractions. The α_eff(b) formulation, ESS-constrained importance weighting for LM training, dual-metric validation methodology, and depth classifiability investigation are all confirmed novel through independent search.', 'score': 4}**/5\n--\n173-\n174-10. [模型规模验证] — 原始仅用 Qwen3-0.6B。增加 Llama-3.2-3B 在 3 个关键 contamination level 的 end-to-end 验证 — 命中 Significance（部分回应 \"would findings hold at larger scale\" 质疑）。\n175-\n176:[Omitted long matching line]\n177-\n178-12. [生态效度补充] — 原始仅有均匀随机注入。增加：(a) domain-skewed injection（domain 间 synthetic 比例 10–80%）；(b) semi-realistic profile（用 Binoculars 对 recent Common Crawl dump 标注子集作为接近真实分布的 contamination profile）— 命中 Significance / Practical Impact（回应 controlled injection ≠ real web 的质疑）。\n179-\n--\n189-\n190-【主要风险】:\n191-\n192:[Omitted long matching line]\n193-\n194-[Omitted long context line]\n195-",
    "numLines": 69
  }
}
```

</details>

---

### Tool call

_source line 57_

<details open><summary>🔧 Tool call — Grep · `toolu_012eGdvAa4QdqoUqyRUeMwjo`</summary>

```json
{
  "pattern": "Drayson",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts",
  "output_mode": "content",
  "-C": 3
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "0a05528b-d05d-4fb3-947f-20e0adce1e25",
  "uuid": "adbe5db7-0082-43f4-a91d-c7f1f19b719d",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UKptDtnewseoPBVaU9uMvj",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1828,
      "cache_read_input_tokens": 44358,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1828
      },
      "output_tokens": 9,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool result

_source line 58 · 2026-05-14T12:33:07.246Z_

<details><summary>↩ Tool result · `toolu_012eGdvAa4QdqoUqyRUeMwjo`</summary>

```text
/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/training/pretrain_weighted.py-2-
artifacts/training/pretrain_weighted.py-3-Supports three weighting methods:
artifacts/training/pretrain_weighted.py-4-  - uniform:  all samples equally weighted (baseline)
artifacts/training/pretrain_weighted.py:5:  - grid:     fixed b value per run (Drayson et al. EMNLP 2025). Grid search = run
/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/training/pretrain_weighted.py-6-               once per b ∈ {0.5, 1.0, 1.5, 2.0, 3.0, 5.0}, pick best val ppl.
artifacts/training/pretrain_weighted.py-7-  - adaptive: batch-adaptive b* via α_eff convergence theory (ours)
/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/training/pretrain_weighted.py-8-
--
/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/weighting/alpha_eff.py-15-
artifacts/weighting/alpha_eff.py-16-References:
/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/weighting/alpha_eff.py-17-  - arXiv 2602.16065 (convergence bounds for weighted pretraining)
artifacts/weighting/alpha_eff.py:18:  - Drayson et al., EMNLP 2025 (grid-search weighting baseline)
/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/weighting/alpha_eff.py-19-
artifacts/weighting/alpha_eff.py-20-Inputs:  q_scores ∈ [0,1]^N (synthetic probabilities from detector)
artifacts/weighting/alpha_eff.py-21-Outputs: weights w ∈ R_+^N (normalized to sum to N)
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "0a05528b-d05d-4fb3-947f-20e0adce1e25",
  "uuid": "e5549ad2-5dd5-4533-a6ed-f4889ca84559",
  "tool_use_result": {
    "mode": "content",
    "numFiles": 0,
    "filenames": [],
    "content": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/training/pretrain_weighted.py-2-\nartifacts/training/pretrain_weighted.py-3-Supports three weighting methods:\nartifacts/training/pretrain_weighted.py-4-  - uniform:  all samples equally weighted (baseline)\nartifacts/training/pretrain_weighted.py:5:  - grid:     fixed b value per run (Drayson et al. EMNLP 2025). Grid search = run\n/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/training/pretrain_weighted.py-6-               once per b ∈ {0.5, 1.0, 1.5, 2.0, 3.0, 5.0}, pick best val ppl.\nartifacts/training/pretrain_weighted.py-7-  - adaptive: batch-adaptive b* via α_eff convergence theory (ours)\n/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/training/pretrain_weighted.py-8-\n--\n/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/weighting/alpha_eff.py-15-\nartifacts/weighting/alpha_eff.py-16-References:\n/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/weighting/alpha_eff.py-17-  - arXiv 2602.16065 (convergence bounds for weighted pretraining)\nartifacts/weighting/alpha_eff.py:18:  - Drayson et al., EMNLP 2025 (grid-search weighting baseline)\n/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/weighting/alpha_eff.py-19-\nartifacts/weighting/alpha_eff.py-20-Inputs:  q_scores ∈ [0,1]^N (synthetic probabilities from detector)\nartifacts/weighting/alpha_eff.py-21-Outputs: weights w ∈ R_+^N (normalized to sum to N)",
    "numLines": 15
  }
}
```

</details>

---

### Assistant

_source line 59_

<details><summary>Logged reasoning block</summary>

```text
Now I found the key reference from IDEA_BRIEF.md:

"Machine-generated text detection prevents language model collapse (Drayson et al., EMNLP 2025 Main Conference) — binary detection + importance resampling baseline using GPT-2 and SmolLM2 (4 LLMs, 2 families, 6 decoding strategies) with single-generator-per-experiment evaluation on WikiText-2"

Let me search for this exact paper title.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "0a05528b-d05d-4fb3-947f-20e0adce1e25",
  "uuid": "23d5e07b-f0bc-4fbc-a764-d7a4448659fc",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013tFAJJkQ2W85BZ4CAaP6f3",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2856,
      "cache_read_input_tokens": 46186,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2856
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Assistant

_source line 60_

Found the full title. Let me search for it specifically.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "0a05528b-d05d-4fb3-947f-20e0adce1e25",
  "uuid": "bcfc80b5-8d31-49ae-9c79-874295a8cfdf",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013tFAJJkQ2W85BZ4CAaP6f3",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2856,
      "cache_read_input_tokens": 46186,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2856
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool call

_source line 61_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01NwtRzKjhHgGnZ6Ys19vhJa`</summary>

```json
{
  "query": "\"Machine-generated text detection prevents language model collapse\" Drayson 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "0a05528b-d05d-4fb3-947f-20e0adce1e25",
  "uuid": "9156f7bf-50a8-43b4-83e7-3b86f28dccad",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013tFAJJkQ2W85BZ4CAaP6f3",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2856,
      "cache_read_input_tokens": 46186,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2856
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool result

_source line 62 · 2026-05-14T12:33:20.926Z_

<details><summary>↩ Tool result · `toolu_01NwtRzKjhHgGnZ6Ys19vhJa`</summary>

```text
Web search results for query: ""Machine-generated text detection prevents language model collapse" Drayson 2025"

Links: [{"title":"[2502.15654] Machine-generated text detection prevents language model collapse","url":"https://arxiv.org/abs/2502.15654"},{"title":"Machine-generated text detection prevents language ...","url":"https://omega.cs.ucl.ac.uk/assets/pdf/papers/drayson2025-model-collapse.pdf"},{"title":"Machine-generated text detection prevents language model collapse","url":"https://arxiv.org/html/2502.15654"},{"title":"GitHub - GeorgeDrayson/model_collapse","url":"https://github.com/GeorgeDrayson/model_collapse"},{"title":"Machine-generated text detection prevents language model collapse - UCL Discovery","url":"https://discovery.ucl.ac.uk/id/eprint/10217226/"},{"title":"(PDF) Machine-generated text detection prevents language model collapse","url":"https://www.researchgate.net/publication/397412242_Machine-generated_text_detection_prevents_language_model_collapse"},{"title":"Computation and Language Feb 2025","url":"https://www.arxiv.org/list/cs.CL/2025-02?skip=1325&show=250"},{"title":"Learning by Surprise: Surplexity for Mitigating Model Collapse in Generative AI","url":"https://arxiv.org/html/2410.12341v3"},{"title":"Machine-generated text detection prevents language model ...","url":"https://discovery.ucl.ac.uk/id/eprint/10217226/1/2025.emnlp-main.1506.pdf"},{"title":"Machine Learning Feb 2025","url":"https://arxiv.org/list/cs.LG/2025-02?skip=3800&show=2000"}]

I found the research paper you were looking for. Here's what the search reveals:

## Overview

The paper "Machine-generated text detection prevents language model collapse" is by George Drayson, Emine Yilmaz, and Vasileios Lampos (2025). It was published in the Proceedings of the 2025 Conference on Empirical Methods in Natural Language Processing.

## Main Problem and Approach

The research addresses how as LLMs become increasingly prevalent, their generated outputs are proliferating across the web, risking a future where machine-generated content dilutes human-authored text. Since online data is the primary resource for LLM pre-training, subsequent models could be trained on an unknown portion of synthetic samples, which could lead to model collapse—a degenerative process whereby LLMs reinforce their own errors, reduce output diversity, and ultimately yield declining performance.

## Research Focus

The study investigates the impact of decoding strategy on model collapse, analysing the text characteristics at each model generation, the similarity to human references, and the resulting model performance. The project proposes an importance sampling approach to alleviate model collapse.

The paper has been made available on arXiv and includes official implementation code in a GitHub repository.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "0a05528b-d05d-4fb3-947f-20e0adce1e25",
  "uuid": "34bbb247-430c-4e19-bc63-7a92b4d98cb4",
  "tool_use_result": {
    "query": "\"Machine-generated text detection prevents language model collapse\" Drayson 2025",
    "results": [
      {
        "tool_use_id": "srvtoolu_015pnytLh1UsRbpU8FDLe5ng",
        "content": [
          {
            "title": "[2502.15654] Machine-generated text detection prevents language model collapse",
            "url": "https://arxiv.org/abs/2502.15654"
          },
          {
            "title": "Machine-generated text detection prevents language ...",
            "url": "https://omega.cs.ucl.ac.uk/assets/pdf/papers/drayson2025-model-collapse.pdf"
          },
          {
            "title": "Machine-generated text detection prevents language model collapse",
            "url": "https://arxiv.org/html/2502.15654"
          },
          {
            "title": "GitHub - GeorgeDrayson/model_collapse",
            "url": "https://github.com/GeorgeDrayson/model_collapse"
          },
          {
            "title": "Machine-generated text detection prevents language model collapse - UCL Discovery",
            "url": "https://discovery.ucl.ac.uk/id/eprint/10217226/"
          },
          {
            "title": "(PDF) Machine-generated text detection prevents language model collapse",
            "url": "https://www.researchgate.net/publication/397412242_Machine-generated_text_detection_prevents_language_model_collapse"
          },
          {
            "title": "Computation and Language Feb 2025",
            "url": "https://www.arxiv.org/list/cs.CL/2025-02?skip=1325&show=250"
          },
          {
            "title": "Learning by Surprise: Surplexity for Mitigating Model Collapse in Generative AI",
            "url": "https://arxiv.org/html/2410.12341v3"
          },
          {
            "title": "Machine-generated text detection prevents language model ...",
            "url": "https://discovery.ucl.ac.uk/id/eprint/10217226/1/2025.emnlp-main.1506.pdf"
          },
          {
            "title": "Machine Learning Feb 2025",
            "url": "https://arxiv.org/list/cs.LG/2025-02?skip=3800&show=2000"
          }
        ]
      },
      "I found the research paper you were looking for. Here's what the search reveals:\n\n## Overview\n\nThe paper \"Machine-generated text detection prevents language model collapse\" is by George Drayson, Emine Yilmaz, and Vasileios Lampos (2025). It was published in the Proceedings of the 2025 Conference on Empirical Methods in Natural Language Processing.\n\n## Main Problem and Approach\n\nThe research addresses how as LLMs become increasingly prevalent, their generated outputs are proliferating across the web, risking a future where machine-generated content dilutes human-authored text. Since online data is the primary resource for LLM pre-training, subsequent models could be trained on an unknown portion of synthetic samples, which could lead to model collapse—a degenerative process whereby LLMs reinforce their own errors, reduce output diversity, and ultimately yield declining performance.\n\n## Research Focus\n\nThe study investigates the impact of decoding strategy on model collapse, analysing the text characteristics at each model generation, the similarity to human references, and the resulting model performance. The project proposes an importance sampling approach to alleviate model collapse.\n\nThe paper has been made available on arXiv and includes official implementation code in a GitHub repository."
    ],
    "durationSeconds": 6.373293453999999
  }
}
```

</details>

---

### Assistant

_source line 63_

<details><summary>Logged reasoning block</summary>

```text
Now I have all the information I need:

**Drayson et al. (EMNLP 2025)**:
- Title: "Machine-generated text detection prevents language model collapse"
- Authors: George Drayson, Emine Yilmaz, Vasileios Lampos
- Venue: EMNLP 2025 Main Conference
- arXiv: 2502.15654

**arXiv 2602.16065**:
- Title: "Can Generative Artificial Intelligence Survive Data Contamination? Theoretical Guarantees under Contaminated Recursive Training"


- Authors: Kevin Wang, Hongqian Niu, Didong Li
- Date: February 2026

I'm also pulling in a couple other relevant papers on detection methods—Ghostbuster from NAACL 2024 on identifying LLM-generated text, and Group DRO from Sagawa et al. on handling distribution shifts in neural networks.

There's also the Self-Play Fine-Tuning approach from Chen et al. that strengthens weaker language models through self-play iterations.

Now I'm evaluating how these papers relate to our work. Ghostbuster is a feature-based detector using structured search over LM features with a classifier, which differs from our TF-IDF and logistic regression approach, though both are detection methods in the same space.

For GPTZero, it's a commercial product without a peer-reviewed methodological paper—the academic papers about it are third-party evaluations rather than foundational contributions. Including it would be like citing Turnitin, which isn't standard practice in academic related work sections.

On synthetic data augmentation, I need to distinguish between pretraining contamination (uncontrolled, unknown provenance) and fine-tuning augmentation (controlled, intentional). There's substantial literature showing synthetic data helps fine-tuning, but our paper focuses on the pretraining contamination problem. Rather than adding separate entries for papers like SPIN or Self-Instruct, I'll just clarify this distinction briefly in the framing—a sentence or two in the intro or related work should suffice to establish that we're addressing a different setting.

For Group DRO, since DoReMi is our direct comparison point and our method operates at the instance level rather than the group level, citing DoReMi is sufficient. Group DRO's foundational work doesn't need a separate entry because the lineage is covered through DoReMi, and a reviewer won't expect us to cite Group DRO when our approach diverges from its group-level optimization strategy.

Now I'm looking at data influence and attribution methods like TracIn and influence functions...

these measure how individual training samples affect predictions, but that's fundamentally different from what we're doing. We're weighting samples based on provenance upfront, not computing influence post-hoc to understand their effects. The goals, methods, and settings are all distinct, so including these would muddy the narrative without adding real relevance.

Now I'm organizing the related work sections. For Section 3, I'll add Drayson et al. as the first entry and shift the rest down. In Section 4, I need to figure out where the convergence theory paper fits among the model collapse entries—it seems like it belongs after Seddik et al.'s statistical analysis, since it provides the convergence bounds that directly motivate our α_eff formulation. I'll insert it as new #5 and shift the remaining entries down. Now I'm working through the citation decision log for each item: Ghostbuster gets added to Section 2, GPTZero is excluded since it's a commercial tool without peer-reviewed methodology, and for self-play fine-tuning I'll acknowledge the distinction between pretraining contamination and fine-tuning augmentation in the main text with references to SPIN and Self-Instruct as representative works.

Group DRO doesn't need inclusion since DoReMi already covers the theoretical foundation, and our instance-level weighting isn't directly comparable to their group-level approach. Data influence methods like TracIn are also unnecessary—we're doing pre-hoc weighting based on provenance rather than post-hoc influence estimation, and citing them would dilute the core narrative.

Actually, let me reconsider Ghostbuster against my actual standard: does it directly relate to our core claims, and would reviewers likely ask why we didn't cite it? That's what should drive the decision.

Ghostbuster uses feature-based detection similar to our TF-IDF approach, but our paper isn't primarily about detection—it's a component we use. We already have six detection methods cited in related work, and adding Ghostbuster wouldn't strengthen our narrative. Still, as a NAACL 2024 paper using a comparable feature-based approach without target model access, a reviewer might reasonably question its absence. I think we should include it. I'm leaning toward including Ghostbuster since it's a well-known feature-based detector from a top venue with an architecture similar to our approach, making its omission a notable gap. I'll add it as the seventh entry in Section 2. Now I need to verify the SPIN paper's publication venue — I believe it was accepted at ICML 2024 — and then work through all the edits systematically, starting with the Drayson entry in Section 3.

For Drayson's work on machine-generated text detection and model collapse, they introduced the detect-and-reweight framework to mitigate collapse by using a binary detector for synthetic text and importance resampling to downweight detected samples, validated on GPT-2 and SmolLM2. This is our most direct predecessor — they established the detect-and-reweight paradigm, but their approach relies on a grid-searched hyperparameter and only evaluates single-generator scenarios on WikiText-2, whereas we provide a theoretically-motivated adaptive alternative and extend to multi-generator settings.

For Wang et al.'s work on generative AI under data contamination, they provide convergence guarantees for contaminated recursive training with a bound that decays as t^{−min{p,α}}, where α represents the proportion of effective real data, and they generalize beyond Gaussian assumptions. Their convergence analysis directly inspired how we define α_eff and derive b*.

The key insight is that their theoretical framework treats α as a known parameter, but we transform it into something a detector can estimate—this shift from fixed to estimated quantity provides the theoretical foundation for our approach.

Now I'm mapping out the specific edits needed across multiple tables. For Section 3, I need to insert Drayson at the top and renumber the existing six entries down by one. Section 4 requires inserting the arXiv paper after Seddik and shifting subsequent entries. Section 2 gets Ghostbuster added as entry 7. I'm also planning to revise the section about potential citation gaps. Now I'm identifying the exact line numbers and content for each section. For Section 3, I need to insert the Drayson entry right after the header separator and then renumber all subsequent entries. In Section 4, I'll insert the new entry after the fourth item, which means shifting entries 5 and 6 down to positions 6 and 7.

For Section 2, I'm adding Ghostbuster as the seventh entry after the existing six items. Then I need to update the "潜在的引用遗漏风险" section at the end of the file to reflect these changes—removing Ghostbuster from that list since it's now a main entry, and adjusting the remaining items accordingly.

Rather than doing individual line edits, I'll make a few larger replacements to ensure the old strings are unique and exact. For Section 3, I'll replace the entire table including the header separator and all data rows with the updated version that has Drayson as the first entry and everything else renumbered. I'll do the same for Section 4, then add the Ghostbuster row to Section 2, and finally replace the entire "潜在的引用遗漏风险" section with the corrected list. 作：提出 importance weighted ERM（IWERM），通过 density ratio 修正 covariate shift 下的 loss | 理论基础直接相关——我们的 weight = 1 - q^b 可以看作一种 bounded importance weight，Shimodaira 的 IWERM 理论为我们的方法提供了正当性 |

L2RW 需要 clean validation set 做 meta-optimization，而我们的方法中 weight 由 provenance detector 预先确定，训练过程中无需调整。Meta-Weight-Net 用 MLP 学习 loss 到 weight 的映射，在噪声标签和类别不平衡问题上表现更好，但与 L2RW 类似依赖 meta-learning；相比之下，我们采用解析形式的 weight function（1 - q^b），更加透明可解释且无需 meta-learning。Curriculum Learning 是这个领域的奠基性工作，证明了按特定顺序学习的有效性。

虽然 curriculum learning 按难度排序而我们按 provenance 加权，形式不同，但都遵循非均匀训练的核心思想。最近的 Dynamic Loss-Based Sample Reweighting 工作在 LLM 预训练中基于 loss 值在线调整权重，这是最直接的对比工作之一——他们基于 loss 做 weighting，我们基于 provenance 做 weighting，两种方法可以组合使用。

DoReMi 则在 domain 级别做混合优化，而我们的方法在 instance 级别基于 provenance 来重加权，粒度和信号来源都不同。

新加入的 Drayson 等人的工作首次提出 detect-and-reweight 框架来缓解模型坍塌，用二分类检测器识别合成文本。

通过重要性重采样降低合成样本的权重，在多个 LLM 和解码策略上验证了有效性。这是我们最直接的前驱工作——他们开创了这个范式，但权重指数需要网格搜索来调整，且只在单生成器场景下评估。我们的改进在于提供理论启发的自适应权重替代网格搜索，并扩展到多生成器的网络规模场景。

现在我在处理表格的编辑，需要在不同部分插入新的条目并重新编号。

第3部分要在表头后插入Drayson并重新编号所有条目，第4部分要在第4条目后插入arXiv论文并调整编号，第2部分要添加Ghostbuster作为第7条目。同时还需要完全替换"潜在的引用遗漏风险"部分。对于自我对弈和合成数据增强的部分，虽然决定是不收录，但我应该考虑是否需要说明这个区分。

现在开始执行这些编辑。
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "0a05528b-d05d-4fb3-947f-20e0adce1e25",
  "uuid": "fb2b2506-5c42-4053-80f4-98a9041b9e57",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018PAjRcLWvsuWe8tsDEkBeJ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 962,
      "cache_read_input_tokens": 49042,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 962
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Assistant

_source line 64_

Now I have all the information. Let me construct the edits.

**Summary of findings:**
- **Drayson et al.**: "Machine-generated text detection prevents language model collapse" (Drayson, Yilmaz, Lampos), EMNLP 2025, arXiv 2502.15654
- **arXiv 2602.16065**: "Can Generative Artificial Intelligence Survive Data Contamination? Theoretical Guarantees under Contaminated Recursive Training" (Wang, Niu, Li), Feb 2026
- **Ghostbuster**: NAACL 2024, Verma, Fleisig, Tomlin, Klein — 收录
- **GPTZero**: 无同行评审方法学论文 — 不收录
- **Self-play/synthetic augmentation**: 不收录，建议正文一句话 acknowledge
- **Group DRO**: DoReMi 引用已覆盖 — 不收录
- **Data influence/TracIn**: 关系太远 — 不收录

Now editing the survey file.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "0a05528b-d05d-4fb3-947f-20e0adce1e25",
  "uuid": "ad60a204-2ebb-4665-be13-323ade4956d2",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018PAjRcLWvsuWe8tsDEkBeJ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 962,
      "cache_read_input_tokens": 49042,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 962
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool call

_source line 65_

<details open><summary>🔧 Tool call — Edit · `toolu_01XmCSYa4dwEjo3qRZ9gN659`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/related_work_notes.md",
  "old_string": "## 3. Sample Reweighting in Training\n\n| # | 论文 | 年份 | 场所 | 一句话 Contribution | 与我们的关系 |\n|---|------|------|------|-------------------|------------|\n| 1 | **Improving the Accuracy of Likelihood-based Inference under Covariate Shift** (Shimodaira) | 2000 | JASA | 奠基性工作：提出 importance weighted ERM（IWERM），通过 density ratio 修正 covariate shift 下的 loss | 理论基础直接相关——我们的 weight = 1 - q^b 可以看作一种 bounded importance weight，Shimodaira 的 IWERM 理论为我们的方法提供了正当性 |\n| 2 | **Learning to Reweight Examples for Robust Deep Learning** (Ren, Zeng, Yang, Urtasun) | 2018 | ICML | 用 meta-learning 在训练中动态学习 sample weights（基于 gradient direction 在 clean validation set 上的表现） | L2RW 需要 clean validation set 做 meta-optimization，我们的方法不需要——weight 由 provenance detector 预先确定，无需在训练中迭代调整 |\n| 3 | **Meta-Weight-Net: Learning an Explicit Mapping For Sample Weighting** (Shu et al.) | 2019 | NeurIPS | 用 MLP 学习 loss → weight 的显式映射函数，在 noisy label 和 class imbalance 场景下优于手工设计的 weighting | 与 L2RW 类似用 meta-learning；我们的 weight function 是 analytic form（1 - q^b），不需要 meta-learning，更透明可解释 |\n| 4 | **Curriculum Learning** (Bengio, Louradour, Collobert, Weston) | 2009 | ICML | 奠基性工作：证明按从易到难的顺序训练（curriculum）可以加速收敛并改善 non-convex optimization 的局部极小值 | Curriculum learning 按难度排序，我们按 provenance 加权——虽然形式不同（排序 vs 加权），但都是 non-uniform training 的思想 |\n| 5 | **Dynamic Loss-Based Sample Reweighting for Improved LLM Pretraining** (Wang et al.) | 2025 | ICLR | 在 LLM pretraining 中做 instance-level dynamic reweighting（基于 loss 值在线调整权重），提出 LinUpper / Quadratic 等策略 | 最直接的对比工作之一——他们基于 loss 做 weighting，我们基于 provenance 做 weighting。两者可组合：先用 provenance weight 再用 loss-based dynamic adjustment |\n| 6 | **DoReMi** (Xie et al., 2023, 见第 1 节) | 2023 | NeurIPS | Domain-level reweighting via Group DRO | 我们做 instance-level provenance weighting，DoReMi 做 domain-level mixture optimization——粒度和信号来源不同 |",
  "new_string": "## 3. Sample Reweighting in Training\n\n| # | 论文 | 年份 | 场所 | 一句话 Contribution | 与我们的关系 |\n|---|------|------|------|-------------------|------------|\n| 1 | **Machine-Generated Text Detection Prevents Language Model Collapse** (Drayson, Yilmaz, Lampos) | 2025 | EMNLP | 首次提出 detect-and-reweight 框架缓解 model collapse：用 binary detector 检测 synthetic text，通过 importance resampling 降权 synthetic samples，在 GPT-2 / SmolLM2（4 LLM, 2 families, 6 decoding strategies）上验证有效性 | 我们最直接的前驱工作——他们开创了 detect-and-reweight 范式，但权重指数 b 是需要 grid search 的 heuristic hyperparameter，且仅评估 single-generator 场景（WikiText-2）；我们提供理论启发的 adaptive b* 替代 grid search，并扩展到 multi-generator web-scale 场景 |\n| 2 | **Improving the Accuracy of Likelihood-based Inference under Covariate Shift** (Shimodaira) | 2000 | JASA | 奠基性工作：提出 importance weighted ERM（IWERM），通过 density ratio 修正 covariate shift 下的 loss | 理论基础直接相关——我们的 weight = 1 - q^b 可以看作一种 bounded importance weight，Shimodaira 的 IWERM 理论为我们的方法提供了正当性 |\n| 3 | **Learning to Reweight Examples for Robust Deep Learning** (Ren, Zeng, Yang, Urtasun) | 2018 | ICML | 用 meta-learning 在训练中动态学习 sample weights（基于 gradient direction 在 clean validation set 上的表现） | L2RW 需要 clean validation set 做 meta-optimization，我们的方法不需要——weight 由 provenance detector 预先确定，无需在训练中迭代调整 |\n| 4 | **Meta-Weight-Net: Learning an Explicit Mapping For Sample Weighting** (Shu et al.) | 2019 | NeurIPS | 用 MLP 学习 loss → weight 的显式映射函数，在 noisy label 和 class imbalance 场景下优于手工设计的 weighting | 与 L2RW 类似用 meta-learning；我们的 weight function 是 analytic form（1 - q^b），不需要 meta-learning，更透明可解释 |\n| 5 | **Curriculum Learning** (Bengio, Louradour, Collobert, Weston) | 2009 | ICML | 奠基性工作：证明按从易到难的顺序训练（curriculum）可以加速收敛并改善 non-convex optimization 的局部极小值 | Curriculum learning 按难度排序，我们按 provenance 加权——虽然形式不同（排序 vs 加权），但都是 non-uniform training 的思想 |\n| 6 | **Dynamic Loss-Based Sample Reweighting for Improved LLM Pretraining** (Wang et al.) | 2025 | ICLR | 在 LLM pretraining 中做 instance-level dynamic reweighting（基于 loss 值在线调整权重），提出 LinUpper / Quadratic 等策略 | 最直接的对比工作之一——他们基于 loss 做 weighting，我们基于 provenance 做 weighting。两者可组合：先用 provenance weight 再用 loss-based dynamic adjustment |\n| 7 | **DoReMi** (Xie et al., 2023, 见第 1 节) | 2023 | NeurIPS | Domain-level reweighting via Group DRO | 我们做 instance-level provenance weighting，DoReMi 做 domain-level mixture optimization——粒度和信号来源不同 |"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "0a05528b-d05d-4fb3-947f-20e0adce1e25",
  "uuid": "1caf477b-8f66-45e0-838b-5bb38cc8225d",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018PAjRcLWvsuWe8tsDEkBeJ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 962,
      "cache_read_input_tokens": 49042,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 962
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool result

_source line 66 · 2026-05-14T12:35:53.841Z_

<details><summary>↩ Tool result · `toolu_01XmCSYa4dwEjo3qRZ9gN659`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/related_work_notes.md has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "0a05528b-d05d-4fb3-947f-20e0adce1e25",
  "uuid": "072352a5-b275-4d97-b685-8109d869a02e",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/related_work_notes.md",
    "oldString": "## 3. Sample Reweighting in Training\n\n| # | 论文 | 年份 | 场所 | 一句话 Contribution | 与我们的关系 |\n|---|------|------|------|-------------------|------------|\n| 1 | **Improving the Accuracy of Likelihood-based Inference under Covariate Shift** (Shimodaira) | 2000 | JASA | 奠基性工作：提出 importance weighted ERM（IWERM），通过 density ratio 修正 covariate shift 下的 loss | 理论基础直接相关——我们的 weight = 1 - q^b 可以看作一种 bounded importance weight，Shimodaira 的 IWERM 理论为我们的方法提供了正当性 |\n| 2 | **Learning to Reweight Examples for Robust Deep Learning** (Ren, Zeng, Yang, Urtasun) | 2018 | ICML | 用 meta-learning 在训练中动态学习 sample weights（基于 gradient direction 在 clean validation set 上的表现） | L2RW 需要 clean validation set 做 meta-optimization，我们的方法不需要——weight 由 provenance detector 预先确定，无需在训练中迭代调整 |\n| 3 | **Meta-Weight-Net: Learning an Explicit Mapping For Sample Weighting** (Shu et al.) | 2019 | NeurIPS | 用 MLP 学习 loss → weight 的显式映射函数，在 noisy label 和 class imbalance 场景下优于手工设计的 weighting | 与 L2RW 类似用 meta-learning；我们的 weight function 是 analytic form（1 - q^b），不需要 meta-learning，更透明可解释 |\n| 4 | **Curriculum Learning** (Bengio, Louradour, Collobert, Weston) | 2009 | ICML | 奠基性工作：证明按从易到难的顺序训练（curriculum）可以加速收敛并改善 non-convex optimization 的局部极小值 | Curriculum learning 按难度排序，我们按 provenance 加权——虽然形式不同（排序 vs 加权），但都是 non-uniform training 的思想 |\n| 5 | **Dynamic Loss-Based Sample Reweighting for Improved LLM Pretraining** (Wang et al.) | 2025 | ICLR | 在 LLM pretraining 中做 instance-level dynamic reweighting（基于 loss 值在线调整权重），提出 LinUpper / Quadratic 等策略 | 最直接的对比工作之一——他们基于 loss 做 weighting，我们基于 provenance 做 weighting。两者可组合：先用 provenance weight 再用 loss-based dynamic adjustment |\n| 6 | **DoReMi** (Xie et al., 2023, 见第 1 节) | 2023 | NeurIPS | Domain-level reweighting via Group DRO | 我们做 instance-level provenance weighting，DoReMi 做 domain-level mixture optimization——粒度和信号来源不同 |",
    "newString": "## 3. Sample Reweighting in Training\n\n| # | 论文 | 年份 | 场所 | 一句话 Contribution | 与我们的关系 |\n|---|------|------|------|-------------------|------------|\n| 1 | **Machine-Generated Text Detection Prevents Language Model Collapse** (Drayson, Yilmaz, Lampos) | 2025 | EMNLP | 首次提出 detect-and-reweight 框架缓解 model collapse：用 binary detector 检测 synthetic text，通过 importance resampling 降权 synthetic samples，在 GPT-2 / SmolLM2（4 LLM, 2 families, 6 decoding strategies）上验证有效性 | 我们最直接的前驱工作——他们开创了 detect-and-reweight 范式，但权重指数 b 是需要 grid search 的 heuristic hyperparameter，且仅评估 single-generator 场景（WikiText-2）；我们提供理论启发的 adaptive b* 替代 grid search，并扩展到 multi-generator web-scale 场景 |\n| 2 | **Improving the Accuracy of Likelihood-based Inference under Covariate Shift** (Shimodaira) | 2000 | JASA | 奠基性工作：提出 importance weighted ERM（IWERM），通过 density ratio 修正 covariate shift 下的 loss | 理论基础直接相关——我们的 weight = 1 - q^b 可以看作一种 bounded importance weight，Shimodaira 的 IWERM 理论为我们的方法提供了正当性 |\n| 3 | **Learning to Reweight Examples for Robust Deep Learning** (Ren, Zeng, Yang, Urtasun) | 2018 | ICML | 用 meta-learning 在训练中动态学习 sample weights（基于 gradient direction 在 clean validation set 上的表现） | L2RW 需要 clean validation set 做 meta-optimization，我们的方法不需要——weight 由 provenance detector 预先确定，无需在训练中迭代调整 |\n| 4 | **Meta-Weight-Net: Learning an Explicit Mapping For Sample Weighting** (Shu et al.) | 2019 | NeurIPS | 用 MLP 学习 loss → weight 的显式映射函数，在 noisy label 和 class imbalance 场景下优于手工设计的 weighting | 与 L2RW 类似用 meta-learning；我们的 weight function 是 analytic form（1 - q^b），不需要 meta-learning，更透明可解释 |\n| 5 | **Curriculum Learning** (Bengio, Louradour, Collobert, Weston) | 2009 | ICML | 奠基性工作：证明按从易到难的顺序训练（curriculum）可以加速收敛并改善 non-convex optimization 的局部极小值 | Curriculum learning 按难度排序，我们按 provenance 加权——虽然形式不同（排序 vs 加权），但都是 non-uniform training 的思想 |\n| 6 | **Dynamic Loss-Based Sample Reweighting for Improved LLM Pretraining** (Wang et al.) | 2025 | ICLR | 在 LLM pretraining 中做 instance-level dynamic reweighting（基于 loss 值在线调整权重），提出 LinUpper / Quadratic 等策略 | 最直接的对比工作之一——他们基于 loss 做 weighting，我们基于 provenance 做 weighting。两者可组合：先用 provenance weight 再用 loss-based dynamic adjustment |\n| 7 | **DoReMi** (Xie et al., 2023, 见第 1 节) | 2023 | NeurIPS | Domain-level reweighting via Group DRO | 我们做 instance-level provenance weighting，DoReMi 做 domain-level mixture optimization——粒度和信号来源不同 |",
    "originalFile": "# Related Work Survey — Provenance Weight Training\n\n## 1. Data Quality / Data Selection for LLM Pretraining\n\n| # | 论文 | 年份 | 场所 | 一句话 Contribution | 与我们的关系 |\n|---|------|------|------|-------------------|------------|\n| 1 | **DSIR: Data Selection for Language Models via Importance Resampling** (Xie, Santurkar, Ma, Liang) | 2023 | NeurIPS | 用 hashed n-gram 特征估计 importance weight，对大规模语料做 importance resampling 来匹配目标分布 | DSIR 按目标分布做 selection，我们按 provenance 做 weighting——都用 lightweight feature 做数据筛选，但动机不同：DSIR 优化 domain match，我们降低 synthetic contamination |\n| 2 | **QuRating: Selecting High-Quality Data for Training Language Models** (Wettig, Gupta, Malik, Chen) | 2024 | ICML | 用 LLM pairwise judgment 对数据做 4 维质量评分（writing style / expertise / facts / educational value），训练 QuRater 模型标注 260B 语料 | QuRating 用 LLM 判断 \"质量\"，我们用检测器判断 \"来源\"——都是 model-based annotation + downstream reweighting，但 quality 和 provenance 是正交维度 |\n| 3 | **The FineWeb Datasets: Decanting the Web for the Finest Text Data at Scale** (Penedo et al., HuggingFace) | 2024 | arXiv | 用 Llama-3-70B 合成标注训练 educational quality classifier，过滤出 1.3T token 的 FineWeb-Edu，在 MMLU/ARC 上大幅领先 | FineWeb-Edu 用 LLM-based classifier 做 hard filtering（保留/丢弃），我们用 detector 做 soft weighting（降权不丢弃），保留更多数据多样性 |\n| 4 | **D4: Improving LLM Pretraining via Document De-Duplication and Diversification** (Tirumala, Simig et al.) | 2023 | NeurIPS D&B | 用 pretrained embedding + K-Means 做去重和多样性平衡，6.7B 模型上提升 2% 下游准确率和 20% 训练效率 | D4 关注重复和多样性，我们关注 synthetic contamination——互补方法，可以先 D4 去重再用我们的 provenance weighting |\n| 5 | **DoReMi: Optimizing Data Mixtures Speeds Up Language Model Pretraining** (Xie, Pham et al.) | 2023 | NeurIPS | 用 Group DRO 在 proxy model 上优化 domain mixture weights，无需下游任务信息，8B 模型提升 6.5% few-shot 准确率 | DoReMi 做 domain-level reweighting（按 domain 调权），我们做 instance-level reweighting（按 q-score 调权）——粒度不同，理论上可以组合使用 |\n| 6 | **DataComp-LM (DCLM): In Search of the Next Generation of Training Sets for Language Models** (Li et al.) | 2024 | NeurIPS D&B | 提供 240T token 标准化语料 + 评估套件，系统性对比 data curation 策略，证明 model-based filtering 是关键 | DCLM 是 benchmark 框架，我们的 provenance-based weighting 可以作为一种新的 curation strategy 在 DCLM 上评估 |\n| 7 | **Scaling Data-Constrained Language Models** (Muennighoff, Rush et al.) | 2023 | NeurIPS | 系统研究数据受限时的 scaling law，发现 ≤4 epochs 重复数据对 loss 影响可忽略，提出考虑重复衰减的 compute-optimal law | 当 unique data 不足时更可能混入 synthetic data 来补量——我们的方法提供了一种替代方案：不用丢弃 synthetic data，而是降权使用 |\n\n## 2. Synthetic Data Contamination Detection\n\n| # | 论文 | 年份 | 场所 | 一句话 Contribution | 与我们的关系 |\n|---|------|------|------|-------------------|------------|\n| 1 | **DetectGPT: Zero-Shot Machine-Generated Text Detection using Probability Curvature** (Mitchell et al.) | 2023 | ICML | 零样本检测：用 log probability curvature（在 perturbation 前后的 log-prob 变化）区分 human vs machine text，无需训练分类器 | DetectGPT 做 binary detection（是否机器生成），我们需要 calibrated probability（q-score）——我们选择 TF-IDF + LogReg 正是因为需要 well-calibrated 的连续 score 而非仅 binary 判断 |\n| 2 | **Fast-DetectGPT: Efficient Zero-Shot Detection via Conditional Probability Curvature** (Bao et al.) | 2024 | ICLR | 将 DetectGPT 的 perturbation 步骤替换为 sampling，加速 340 倍且 AUROC 提升约 75% | 同上——更高效但仍是 binary detection，calibration 质量（ECE）未被重点评估，而这正是我们工作的核心关注点 |\n| 3 | **Binoculars: Zero-Shot Detection of LLM-Generated Text** (Hans et al.) | 2024 | ICML | 用两个 LLM 的 perplexity / cross-perplexity 比值做检测，ChatGPT 文本在 0.01% FPR 下召回 >90% | Binoculars 需要两个 LLM 推理，计算成本高；我们的 TF-IDF + LogReg 检测器极轻量，适合标注数十亿 token 级别的 pretraining corpus |\n| 4 | **GLTR: Statistical Detection and Visualization of Generated Text** (Gehrmann, Strobelt, Rush) | 2019 | ACL | 用 LM 的 top-k token 排名做统计检测和可视化，帮助人类识别机器文本（人类检测率从 54% 提升到 72%） | 早期 statistical detection 工作，启发了后续基于 model statistics 的方法；我们的方法同样基于统计特征但目标不同（scoring for weighting 而非 human-in-the-loop detection） |\n| 5 | **A Watermark for Large Language Models** (Kirchenbauer et al.) | 2023 | ICML | 在生成时嵌入 statistical watermark（green/red token list），可用 p-value 统计检验来检测 | Watermarking 需要控制生成过程，无法检测已有的、未 watermarked 的 synthetic data——我们的场景是 post-hoc detection on existing corpus |\n| 6 | **A Survey on LLM-Generated Text Detection: Necessity, Methods, and Future Directions** (Wu et al.) | 2024 | Computational Linguistics (MIT Press) | 系统综述 statistical / neural / watermarking 三类检测方法，讨论 robustness 和 generalization | 综述文献，帮助定位我们的检测器在整个 detection 方法谱系中的位置——我们是 training-based statistical classifier，但用于 weighting 而非 filtering |\n\n## 3. Sample Reweighting in Training\n\n| # | 论文 | 年份 | 场所 | 一句话 Contribution | 与我们的关系 |\n|---|------|------|------|-------------------|------------|\n| 1 | **Improving the Accuracy of Likelihood-based Inference under Covariate Shift** (Shimodaira) | 2000 | JASA | 奠基性工作：提出 importance weighted ERM（IWERM），通过 density ratio 修正 covariate shift 下的 loss | 理论基础直接相关——我们的 weight = 1 - q^b 可以看作一种 bounded importance weight，Shimodaira 的 IWERM 理论为我们的方法提供了正当性 |\n| 2 | **Learning to Reweight Examples for Robust Deep Learning** (Ren, Zeng, Yang, Urtasun) | 2018 | ICML | 用 meta-learning 在训练中动态学习 sample weights（基于 gradient direction 在 clean validation set 上的表现） | L2RW 需要 clean validation set 做 meta-optimization，我们的方法不需要——weight 由 provenance detector 预先确定，无需在训练中迭代调整 |\n| 3 | **Meta-Weight-Net: Learning an Explicit Mapping For Sample Weighting** (Shu et al.) | 2019 | NeurIPS | 用 MLP 学习 loss → weight 的显式映射函数，在 noisy label 和 class imbalance 场景下优于手工设计的 weighting | 与 L2RW 类似用 meta-learning；我们的 weight function 是 analytic form（1 - q^b），不需要 meta-learning，更透明可解释 |\n| 4 | **Curriculum Learning** (Bengio, Louradour, Collobert, Weston) | 2009 | ICML | 奠基性工作：证明按从易到难的顺序训练（curriculum）可以加速收敛并改善 non-convex optimization 的局部极小值 | Curriculum learning 按难度排序，我们按 provenance 加权——虽然形式不同（排序 vs 加权），但都是 non-uniform training 的思想 |\n| 5 | **Dynamic Loss-Based Sample Reweighting for Improved LLM Pretraining** (Wang et al.) | 2025 | ICLR | 在 LLM pretraining 中做 instance-level dynamic reweighting（基于 loss 值在线调整权重），提出 LinUpper / Quadratic 等策略 | 最直接的对比工作之一——他们基于 loss 做 weighting，我们基于 provenance 做 weighting。两者可组合：先用 provenance weight 再用 loss-based dynamic adjustment |\n| 6 | **DoReMi** (Xie et al., 2023, 见第 1 节) | 2023 | NeurIPS | Domain-level reweighting via Group DRO | 我们做 instance-level provenance weighting，DoReMi 做 domain-level mixture optimization——粒度和信号来源不同 |\n\n## 4. Theoretical Analysis of Data Mixing / Contamination\n\n| # | 论文 | 年份 | 场所 | 一句话 Contribution | 与我们的关系 |\n|---|------|------|------|-------------------|------------|\n| 1 | **AI Models Collapse When Trained on Recursively Generated Data** (Shumailov, Shumaylov, Zhao, Papernot, Anderson, Gal) | 2024 | Nature | 提出 model collapse 概念：在 synthetic data 上迭代训练导致分布尾部丢失和性能退化，在 VAE / GMM / LLM 上验证 | 我们工作的核心 motivation——Shumailov 证明了 synthetic contamination 的危害，我们提出用 provenance weighting 来缓解而非完全过滤 |\n| 2 | **Strong Model Collapse** (Dohmatob, Feng, Subramonian, Kempe) | 2025 | ICLR | 证明即使极小比例的 synthetic data（1/1000）也会导致 model collapse；用 operator-valued free probability theory 给出 bias-variance 分解 | 强化了 motivation——即使少量 synthetic data 也有害，说明我们的 provenance weighting 方法的必要性：不能靠 \"少量就没事\" 来忽视 |\n| 3 | **Is Model Collapse Inevitable? Breaking the Curse of Recursion by Accumulating Real and Synthetic Data** (Gerstgrasser, Schaeffer et al.) | 2024 | COLM | 证明如果 accumulate（而非 replace）数据，model collapse 可以避免；在 linear model 下证明 test error 有有限上界 | 与我们的方法互补——他们说 \"保留 real data 可以救\"，我们说 \"对 synthetic data 降权也可以救\"，都是 mitigate 而非 discard 的思路 |\n| 4 | **How Bad is Training on Synthetic Data? A Statistical Analysis of Language Model Collapse** (Seddik, Chen, Hayou, Youssef, Debbah) | 2024 | COLM | 给出 recursive training 的统计模型，证明纯 synthetic 训练不可避免 collapse，但 real + synthetic 混合训练在 synthetic 比例低于阈值时可避免 | 直接相关——他们给出了 synthetic data 比例的阈值分析，我们的 α_eff 理论可以看作这类阈值分析的推广（从 hard threshold 到 soft weighting） |\n| 5 | **Data Mixing Laws: Optimizing Data Mixtures by Predicting Language Modeling Performance** (Ye, Liu, Sun, Zhan, Zhou, Qiu) | 2025 | ICLR | 发现 domain mixture proportion 和 model performance 之间存在可预测的函数关系（data mixing laws），可以用小规模实验预测大模型表现 | Data mixing laws 可用于预测不同 provenance weight 设置下的 model performance——我们的 Grid-b 搜索可以理论上用 mixing laws 来加速 |\n| 6 | **Scaling Data-Constrained Language Models** (Muennighoff et al., 2023, 见第 1 节) | 2023 | NeurIPS | 数据受限下的 scaling law，重复 ≤4 epochs 影响可忽略 | 提供了数据受限场景的理论框架，我们的 α_eff 分析在此基础上进一步考虑了 contamination 的影响 |\n\n## Key Observations\n\n### 与现有工作的主要区别\n\n1. **Data selection vs. data weighting**: 多数现有方法（DSIR, FineWeb-Edu, D4）做 hard selection（保留或丢弃），我们做 soft weighting（降权但不丢弃），保留了更多数据多样性和信息。\n2. **Quality-based vs. provenance-based**: QuRating / FineWeb-Edu 基于 \"质量\" 评分，我们基于 \"来源\"（是否 synthetic）评分——这是正交的信号维度，可以组合使用。\n3. **Detection for filtering vs. detection for weighting**: 现有 synthetic text detection 工作（DetectGPT, Binoculars）几乎全部用于 binary filtering 或人工审核，我们首次将 calibrated detection score 用于 continuous training weight，对检测器的 calibration（ECE）提出了新要求。\n4. **Analytic weight function vs. learned weights**: 与 meta-learning reweighting（L2RW, Meta-Weight-Net）相比，我们的 weight = 1 - q^b 是 closed-form，无需 clean validation set 或 meta-optimization，更高效透明。\n\n### 最直接的竞争对手 / 对比工作\n\n- **Dynamic Loss-Based Sample Reweighting (Wang et al., ICLR 2025)**: 同为 instance-level reweighting for LLM pretraining，但信号来源不同（loss vs. provenance）。\n- **DoReMi (Xie et al., NeurIPS 2023)**: Domain-level reweighting，粒度不同但目标相似。\n- **FineWeb-Edu filtering**: 最接近的 \"data quality\" 竞品，但是 hard filtering 不是 soft weighting。\n\n### 潜在的引用遗漏风险\n\n- **Ghostbuster** (Verma et al., 2024): 另一个 feature-based synthetic text detector，可能需要作为 detection baseline 引用 [需确认场所]\n- **GPTZero**: 商业工具，学术论文 (2025 arXiv) 可作为检测方法的 context 引用 [需确认]\n- **Self-play fine-tuning / synthetic data augmentation 文献**: 我们的工作假设 synthetic data 有害，但有大量文献证明 synthetic data 在 fine-tuning 中有益——需要在 related work 中 acknowledge 并区分 pretraining contamination vs. fine-tuning augmentation 的不同场景\n- **Distributionally robust optimization (DRO) 基础文献**: Sagawa et al. (2020) Group DRO 等，作为 DoReMi 的理论基础可能需要提及\n- **Data influence / data attribution 文献**: TracIn, influence functions 等，虽然不是直接竞品但在 \"understanding data's effect on training\" 的大框架下相关\n",
    "structuredPatch": [
      {
        "oldStart": 27,
        "oldLines": 12,
        "newStart": 27,
        "newLines": 13,
        "lines": [
          " ",
          " | # | 论文 | 年份 | 场所 | 一句话 Contribution | 与我们的关系 |",
          " |---|------|------|------|-------------------|------------|",
          "-| 1 | **Improving the Accuracy of Likelihood-based Inference under Covariate Shift** (Shimodaira) | 2000 | JASA | 奠基性工作：提出 importance weighted ERM（IWERM），通过 density ratio 修正 covariate shift 下的 loss | 理论基础直接相关——我们的 weight = 1 - q^b 可以看作一种 bounded importance weight，Shimodaira 的 IWERM 理论为我们的方法提供了正当性 |",
          "-| 2 | **Learning to Reweight Examples for Robust Deep Learning** (Ren, Zeng, Yang, Urtasun) | 2018 | ICML | 用 meta-learning 在训练中动态学习 sample weights（基于 gradient direction 在 clean validation set 上的表现） | L2RW 需要 clean validation set 做 meta-optimization，我们的方法不需要——weight 由 provenance detector 预先确定，无需在训练中迭代调整 |",
          "-| 3 | **Meta-Weight-Net: Learning an Explicit Mapping For Sample Weighting** (Shu et al.) | 2019 | NeurIPS | 用 MLP 学习 loss → weight 的显式映射函数，在 noisy label 和 class imbalance 场景下优于手工设计的 weighting | 与 L2RW 类似用 meta-learning；我们的 weight function 是 analytic form（1 - q^b），不需要 meta-learning，更透明可解释 |",
          "-| 4 | **Curriculum Learning** (Bengio, Louradour, Collobert, Weston) | 2009 | ICML | 奠基性工作：证明按从易到难的顺序训练（curriculum）可以加速收敛并改善 non-convex optimization 的局部极小值 | Curriculum learning 按难度排序，我们按 provenance 加权——虽然形式不同（排序 vs 加权），但都是 non-uniform training 的思想 |",
          "-| 5 | **Dynamic Loss-Based Sample Reweighting for Improved LLM Pretraining** (Wang et al.) | 2025 | ICLR | 在 LLM pretraining 中做 instance-level dynamic reweighting（基于 loss 值在线调整权重），提出 LinUpper / Quadratic 等策略 | 最直接的对比工作之一——他们基于 loss 做 weighting，我们基于 provenance 做 weighting。两者可组合：先用 provenance weight 再用 loss-based dynamic adjustment |",
          "-| 6 | **DoReMi** (Xie et al., 2023, 见第 1 节) | 2023 | NeurIPS | Domain-level reweighting via Group DRO | 我们做 instance-level provenance weighting，DoReMi 做 domain-level mixture optimization——粒度和信号来源不同 |",
          "+| 1 | **Machine-Generated Text Detection Prevents Language Model Collapse** (Drayson, Yilmaz, Lampos) | 2025 | EMNLP | 首次提出 detect-and-reweight 框架缓解 model collapse：用 binary detector 检测 synthetic text，通过 importance resampling 降权 synthetic samples，在 GPT-2 / SmolLM2（4 LLM, 2 families, 6 decoding strategies）上验证有效性 | 我们最直接的前驱工作——他们开创了 detect-and-reweight 范式，但权重指数 b 是需要 grid search 的 heuristic hyperparameter，且仅评估 single-generator 场景（WikiText-2）；我们提供理论启发的 adaptive b* 替代 grid search，并扩展到 multi-generator web-scale 场景 |",
          "+| 2 | **Improving the Accuracy of Likelihood-based Inference under Covariate Shift** (Shimodaira) | 2000 | JASA | 奠基性工作：提出 importance weighted ERM（IWERM），通过 density ratio 修正 covariate shift 下的 loss | 理论基础直接相关——我们的 weight = 1 - q^b 可以看作一种 bounded importance weight，Shimodaira 的 IWERM 理论为我们的方法提供了正当性 |",
          "+| 3 | **Learning to Reweight Examples for Robust Deep Learning** (Ren, Zeng, Yang, Urtasun) | 2018 | ICML | 用 meta-learning 在训练中动态学习 sample weights（基于 gradient direction 在 clean validation set 上的表现） | L2RW 需要 clean validation set 做 meta-optimization，我们的方法不需要——weight 由 provenance detector 预先确定，无需在训练中迭代调整 |",
          "+| 4 | **Meta-Weight-Net: Learning an Explicit Mapping For Sample Weighting** (Shu et al.) | 2019 | NeurIPS | 用 MLP 学习 loss → weight 的显式映射函数，在 noisy label 和 class imbalance 场景下优于手工设计的 weighting | 与 L2RW 类似用 meta-learning；我们的 weight function 是 analytic form（1 - q^b），不需要 meta-learning，更透明可解释 |",
          "+| 5 | **Curriculum Learning** (Bengio, Louradour, Collobert, Weston) | 2009 | ICML | 奠基性工作：证明按从易到难的顺序训练（curriculum）可以加速收敛并改善 non-convex optimization 的局部极小值 | Curriculum learning 按难度排序，我们按 provenance 加权——虽然形式不同（排序 vs 加权），但都是 non-uniform training 的思想 |",
          "+| 6 | **Dynamic Loss-Based Sample Reweighting for Improved LLM Pretraining** (Wang et al.) | 2025 | ICLR | 在 LLM pretraining 中做 instance-level dynamic reweighting（基于 loss 值在线调整权重），提出 LinUpper / Quadratic 等策略 | 最直接的对比工作之一——他们基于 loss 做 weighting，我们基于 provenance 做 weighting。两者可组合：先用 provenance weight 再用 loss-based dynamic adjustment |",
          "+| 7 | **DoReMi** (Xie et al., 2023, 见第 1 节) | 2023 | NeurIPS | Domain-level reweighting via Group DRO | 我们做 instance-level provenance weighting，DoReMi 做 domain-level mixture optimization——粒度和信号来源不同 |",
          " ",
          " ## 4. Theoretical Analysis of Data Mixing / Contamination",
          " "
        ]
      }
    ],
    "userModified": false,
    "replaceAll": false
  }
}
```

</details>

---

### Tool call

_source line 67_

<details open><summary>🔧 Tool call — Edit · `toolu_01Wp1aLktyNkTvQ9TNWdpyRw`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/related_work_notes.md",
  "old_string": "| 4 | **How Bad is Training on Synthetic Data? A Statistical Analysis of Language Model Collapse** (Seddik, Chen, Hayou, Youssef, Debbah) | 2024 | COLM | 给出 recursive training 的统计模型，证明纯 synthetic 训练不可避免 collapse，但 real + synthetic 混合训练在 synthetic 比例低于阈值时可避免 | 直接相关——他们给出了 synthetic data 比例的阈值分析，我们的 α_eff 理论可以看作这类阈值分析的推广（从 hard threshold 到 soft weighting） |\n| 5 | **Data Mixing Laws: Optimizing Data Mixtures by Predicting Language Modeling Performance** (Ye, Liu, Sun, Zhan, Zhou, Qiu) | 2025 | ICLR | 发现 domain mixture proportion 和 model performance 之间存在可预测的函数关系（data mixing laws），可以用小规模实验预测大模型表现 | Data mixing laws 可用于预测不同 provenance weight 设置下的 model performance——我们的 Grid-b 搜索可以理论上用 mixing laws 来加速 |\n| 6 | **Scaling Data-Constrained Language Models** (Muennighoff et al., 2023, 见第 1 节) | 2023 | NeurIPS | 数据受限下的 scaling law，重复 ≤4 epochs 影响可忽略 | 提供了数据受限场景的理论框架，我们的 α_eff 分析在此基础上进一步考虑了 contamination 的影响 |",
  "new_string": "| 4 | **How Bad is Training on Synthetic Data? A Statistical Analysis of Language Model Collapse** (Seddik, Chen, Hayou, Youssef, Debbah) | 2024 | COLM | 给出 recursive training 的统计模型，证明纯 synthetic 训练不可避免 collapse，但 real + synthetic 混合训练在 synthetic 比例低于阈值时可避免 | 直接相关——他们给出了 synthetic data 比例的阈值分析，我们的 α_eff 理论可以看作这类阈值分析的推广（从 hard threshold 到 soft weighting） |\n| 5 | **Can Generative Artificial Intelligence Survive Data Contamination? Theoretical Guarantees under Contaminated Recursive Training** (Wang, Niu, Li) | 2026 | arXiv 2602.16065 | 为 contaminated recursive training 提供收敛保证：bound d(ℙ̂_t, ℙ_0) ≲ t^{−min{p,α}}，推广至 non-Gaussian 设置；Assumption A2 限制 d 为凸度量，显式排除 cross-entropy/KL | 该论文的收敛 bound 直接启发了我们的 α_eff 定义和 b* 推导——α_eff(b) 将其理论中的 α 从 known parameter 变为 detector-estimated quantity，是我们方法的理论 motivation（非 contribution） |\n| 6 | **Data Mixing Laws: Optimizing Data Mixtures by Predicting Language Modeling Performance** (Ye, Liu, Sun, Zhan, Zhou, Qiu) | 2025 | ICLR | 发现 domain mixture proportion 和 model performance 之间存在可预测的函数关系（data mixing laws），可以用小规模实验预测大模型表现 | Data mixing laws 可用于预测不同 provenance weight 设置下的 model performance——我们的 Grid-b 搜索可以理论上用 mixing laws 来加速 |\n| 7 | **Scaling Data-Constrained Language Models** (Muennighoff et al., 2023, 见第 1 节) | 2023 | NeurIPS | 数据受限下的 scaling law，重复 ≤4 epochs 影响可忽略 | 提供了数据受限场景的理论框架，我们的 α_eff 分析在此基础上进一步考虑了 contamination 的影响 |"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "0a05528b-d05d-4fb3-947f-20e0adce1e25",
  "uuid": "d4a87179-6079-43db-9eb4-d5dbb11ac461",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0112ShQSojNiVSUtVnJNX9as",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 8514,
      "cache_read_input_tokens": 50004,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 8514
      },
      "output_tokens": 46,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool result

_source line 68 · 2026-05-14T12:36:23.887Z_

<details><summary>↩ Tool result · `toolu_01Wp1aLktyNkTvQ9TNWdpyRw`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/related_work_notes.md has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "0a05528b-d05d-4fb3-947f-20e0adce1e25",
  "uuid": "c5376dd0-c193-48a4-bab5-31892dbe37dc",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/related_work_notes.md",
    "oldString": "| 4 | **How Bad is Training on Synthetic Data? A Statistical Analysis of Language Model Collapse** (Seddik, Chen, Hayou, Youssef, Debbah) | 2024 | COLM | 给出 recursive training 的统计模型，证明纯 synthetic 训练不可避免 collapse，但 real + synthetic 混合训练在 synthetic 比例低于阈值时可避免 | 直接相关——他们给出了 synthetic data 比例的阈值分析，我们的 α_eff 理论可以看作这类阈值分析的推广（从 hard threshold 到 soft weighting） |\n| 5 | **Data Mixing Laws: Optimizing Data Mixtures by Predicting Language Modeling Performance** (Ye, Liu, Sun, Zhan, Zhou, Qiu) | 2025 | ICLR | 发现 domain mixture proportion 和 model performance 之间存在可预测的函数关系（data mixing laws），可以用小规模实验预测大模型表现 | Data mixing laws 可用于预测不同 provenance weight 设置下的 model performance——我们的 Grid-b 搜索可以理论上用 mixing laws 来加速 |\n| 6 | **Scaling Data-Constrained Language Models** (Muennighoff et al., 2023, 见第 1 节) | 2023 | NeurIPS | 数据受限下的 scaling law，重复 ≤4 epochs 影响可忽略 | 提供了数据受限场景的理论框架，我们的 α_eff 分析在此基础上进一步考虑了 contamination 的影响 |",
    "newString": "| 4 | **How Bad is Training on Synthetic Data? A Statistical Analysis of Language Model Collapse** (Seddik, Chen, Hayou, Youssef, Debbah) | 2024 | COLM | 给出 recursive training 的统计模型，证明纯 synthetic 训练不可避免 collapse，但 real + synthetic 混合训练在 synthetic 比例低于阈值时可避免 | 直接相关——他们给出了 synthetic data 比例的阈值分析，我们的 α_eff 理论可以看作这类阈值分析的推广（从 hard threshold 到 soft weighting） |\n| 5 | **Can Generative Artificial Intelligence Survive Data Contamination? Theoretical Guarantees under Contaminated Recursive Training** (Wang, Niu, Li) | 2026 | arXiv 2602.16065 | 为 contaminated recursive training 提供收敛保证：bound d(ℙ̂_t, ℙ_0) ≲ t^{−min{p,α}}，推广至 non-Gaussian 设置；Assumption A2 限制 d 为凸度量，显式排除 cross-entropy/KL | 该论文的收敛 bound 直接启发了我们的 α_eff 定义和 b* 推导——α_eff(b) 将其理论中的 α 从 known parameter 变为 detector-estimated quantity，是我们方法的理论 motivation（非 contribution） |\n| 6 | **Data Mixing Laws: Optimizing Data Mixtures by Predicting Language Modeling Performance** (Ye, Liu, Sun, Zhan, Zhou, Qiu) | 2025 | ICLR | 发现 domain mixture proportion 和 model performance 之间存在可预测的函数关系（data mixing laws），可以用小规模实验预测大模型表现 | Data mixing laws 可用于预测不同 provenance weight 设置下的 model performance——我们的 Grid-b 搜索可以理论上用 mixing laws 来加速 |\n| 7 | **Scaling Data-Constrained Language Models** (Muennighoff et al., 2023, 见第 1 节) | 2023 | NeurIPS | 数据受限下的 scaling law，重复 ≤4 epochs 影响可忽略 | 提供了数据受限场景的理论框架，我们的 α_eff 分析在此基础上进一步考虑了 contamination 的影响 |",
    "originalFile": "# Related Work Survey — Provenance Weight Training\n\n## 1. Data Quality / Data Selection for LLM Pretraining\n\n| # | 论文 | 年份 | 场所 | 一句话 Contribution | 与我们的关系 |\n|---|------|------|------|-------------------|------------|\n| 1 | **DSIR: Data Selection for Language Models via Importance Resampling** (Xie, Santurkar, Ma, Liang) | 2023 | NeurIPS | 用 hashed n-gram 特征估计 importance weight，对大规模语料做 importance resampling 来匹配目标分布 | DSIR 按目标分布做 selection，我们按 provenance 做 weighting——都用 lightweight feature 做数据筛选，但动机不同：DSIR 优化 domain match，我们降低 synthetic contamination |\n| 2 | **QuRating: Selecting High-Quality Data for Training Language Models** (Wettig, Gupta, Malik, Chen) | 2024 | ICML | 用 LLM pairwise judgment 对数据做 4 维质量评分（writing style / expertise / facts / educational value），训练 QuRater 模型标注 260B 语料 | QuRating 用 LLM 判断 \"质量\"，我们用检测器判断 \"来源\"——都是 model-based annotation + downstream reweighting，但 quality 和 provenance 是正交维度 |\n| 3 | **The FineWeb Datasets: Decanting the Web for the Finest Text Data at Scale** (Penedo et al., HuggingFace) | 2024 | arXiv | 用 Llama-3-70B 合成标注训练 educational quality classifier，过滤出 1.3T token 的 FineWeb-Edu，在 MMLU/ARC 上大幅领先 | FineWeb-Edu 用 LLM-based classifier 做 hard filtering（保留/丢弃），我们用 detector 做 soft weighting（降权不丢弃），保留更多数据多样性 |\n| 4 | **D4: Improving LLM Pretraining via Document De-Duplication and Diversification** (Tirumala, Simig et al.) | 2023 | NeurIPS D&B | 用 pretrained embedding + K-Means 做去重和多样性平衡，6.7B 模型上提升 2% 下游准确率和 20% 训练效率 | D4 关注重复和多样性，我们关注 synthetic contamination——互补方法，可以先 D4 去重再用我们的 provenance weighting |\n| 5 | **DoReMi: Optimizing Data Mixtures Speeds Up Language Model Pretraining** (Xie, Pham et al.) | 2023 | NeurIPS | 用 Group DRO 在 proxy model 上优化 domain mixture weights，无需下游任务信息，8B 模型提升 6.5% few-shot 准确率 | DoReMi 做 domain-level reweighting（按 domain 调权），我们做 instance-level reweighting（按 q-score 调权）——粒度不同，理论上可以组合使用 |\n| 6 | **DataComp-LM (DCLM): In Search of the Next Generation of Training Sets for Language Models** (Li et al.) | 2024 | NeurIPS D&B | 提供 240T token 标准化语料 + 评估套件，系统性对比 data curation 策略，证明 model-based filtering 是关键 | DCLM 是 benchmark 框架，我们的 provenance-based weighting 可以作为一种新的 curation strategy 在 DCLM 上评估 |\n| 7 | **Scaling Data-Constrained Language Models** (Muennighoff, Rush et al.) | 2023 | NeurIPS | 系统研究数据受限时的 scaling law，发现 ≤4 epochs 重复数据对 loss 影响可忽略，提出考虑重复衰减的 compute-optimal law | 当 unique data 不足时更可能混入 synthetic data 来补量——我们的方法提供了一种替代方案：不用丢弃 synthetic data，而是降权使用 |\n\n## 2. Synthetic Data Contamination Detection\n\n| # | 论文 | 年份 | 场所 | 一句话 Contribution | 与我们的关系 |\n|---|------|------|------|-------------------|------------|\n| 1 | **DetectGPT: Zero-Shot Machine-Generated Text Detection using Probability Curvature** (Mitchell et al.) | 2023 | ICML | 零样本检测：用 log probability curvature（在 perturbation 前后的 log-prob 变化）区分 human vs machine text，无需训练分类器 | DetectGPT 做 binary detection（是否机器生成），我们需要 calibrated probability（q-score）——我们选择 TF-IDF + LogReg 正是因为需要 well-calibrated 的连续 score 而非仅 binary 判断 |\n| 2 | **Fast-DetectGPT: Efficient Zero-Shot Detection via Conditional Probability Curvature** (Bao et al.) | 2024 | ICLR | 将 DetectGPT 的 perturbation 步骤替换为 sampling，加速 340 倍且 AUROC 提升约 75% | 同上——更高效但仍是 binary detection，calibration 质量（ECE）未被重点评估，而这正是我们工作的核心关注点 |\n| 3 | **Binoculars: Zero-Shot Detection of LLM-Generated Text** (Hans et al.) | 2024 | ICML | 用两个 LLM 的 perplexity / cross-perplexity 比值做检测，ChatGPT 文本在 0.01% FPR 下召回 >90% | Binoculars 需要两个 LLM 推理，计算成本高；我们的 TF-IDF + LogReg 检测器极轻量，适合标注数十亿 token 级别的 pretraining corpus |\n| 4 | **GLTR: Statistical Detection and Visualization of Generated Text** (Gehrmann, Strobelt, Rush) | 2019 | ACL | 用 LM 的 top-k token 排名做统计检测和可视化，帮助人类识别机器文本（人类检测率从 54% 提升到 72%） | 早期 statistical detection 工作，启发了后续基于 model statistics 的方法；我们的方法同样基于统计特征但目标不同（scoring for weighting 而非 human-in-the-loop detection） |\n| 5 | **A Watermark for Large Language Models** (Kirchenbauer et al.) | 2023 | ICML | 在生成时嵌入 statistical watermark（green/red token list），可用 p-value 统计检验来检测 | Watermarking 需要控制生成过程，无法检测已有的、未 watermarked 的 synthetic data——我们的场景是 post-hoc detection on existing corpus |\n| 6 | **A Survey on LLM-Generated Text Detection: Necessity, Methods, and Future Directions** (Wu et al.) | 2024 | Computational Linguistics (MIT Press) | 系统综述 statistical / neural / watermarking 三类检测方法，讨论 robustness 和 generalization | 综述文献，帮助定位我们的检测器在整个 detection 方法谱系中的位置——我们是 training-based statistical classifier，但用于 weighting 而非 filtering |\n\n## 3. Sample Reweighting in Training\n\n| # | 论文 | 年份 | 场所 | 一句话 Contribution | 与我们的关系 |\n|---|------|------|------|-------------------|------------|\n| 1 | **Machine-Generated Text Detection Prevents Language Model Collapse** (Drayson, Yilmaz, Lampos) | 2025 | EMNLP | 首次提出 detect-and-reweight 框架缓解 model collapse：用 binary detector 检测 synthetic text，通过 importance resampling 降权 synthetic samples，在 GPT-2 / SmolLM2（4 LLM, 2 families, 6 decoding strategies）上验证有效性 | 我们最直接的前驱工作——他们开创了 detect-and-reweight 范式，但权重指数 b 是需要 grid search 的 heuristic hyperparameter，且仅评估 single-generator 场景（WikiText-2）；我们提供理论启发的 adaptive b* 替代 grid search，并扩展到 multi-generator web-scale 场景 |\n| 2 | **Improving the Accuracy of Likelihood-based Inference under Covariate Shift** (Shimodaira) | 2000 | JASA | 奠基性工作：提出 importance weighted ERM（IWERM），通过 density ratio 修正 covariate shift 下的 loss | 理论基础直接相关——我们的 weight = 1 - q^b 可以看作一种 bounded importance weight，Shimodaira 的 IWERM 理论为我们的方法提供了正当性 |\n| 3 | **Learning to Reweight Examples for Robust Deep Learning** (Ren, Zeng, Yang, Urtasun) | 2018 | ICML | 用 meta-learning 在训练中动态学习 sample weights（基于 gradient direction 在 clean validation set 上的表现） | L2RW 需要 clean validation set 做 meta-optimization，我们的方法不需要——weight 由 provenance detector 预先确定，无需在训练中迭代调整 |\n| 4 | **Meta-Weight-Net: Learning an Explicit Mapping For Sample Weighting** (Shu et al.) | 2019 | NeurIPS | 用 MLP 学习 loss → weight 的显式映射函数，在 noisy label 和 class imbalance 场景下优于手工设计的 weighting | 与 L2RW 类似用 meta-learning；我们的 weight function 是 analytic form（1 - q^b），不需要 meta-learning，更透明可解释 |\n| 5 | **Curriculum Learning** (Bengio, Louradour, Collobert, Weston) | 2009 | ICML | 奠基性工作：证明按从易到难的顺序训练（curriculum）可以加速收敛并改善 non-convex optimization 的局部极小值 | Curriculum learning 按难度排序，我们按 provenance 加权——虽然形式不同（排序 vs 加权），但都是 non-uniform training 的思想 |\n| 6 | **Dynamic Loss-Based Sample Reweighting for Improved LLM Pretraining** (Wang et al.) | 2025 | ICLR | 在 LLM pretraining 中做 instance-level dynamic reweighting（基于 loss 值在线调整权重），提出 LinUpper / Quadratic 等策略 | 最直接的对比工作之一——他们基于 loss 做 weighting，我们基于 provenance 做 weighting。两者可组合：先用 provenance weight 再用 loss-based dynamic adjustment |\n| 7 | **DoReMi** (Xie et al., 2023, 见第 1 节) | 2023 | NeurIPS | Domain-level reweighting via Group DRO | 我们做 instance-level provenance weighting，DoReMi 做 domain-level mixture optimization——粒度和信号来源不同 |\n\n## 4. Theoretical Analysis of Data Mixing / Contamination\n\n| # | 论文 | 年份 | 场所 | 一句话 Contribution | 与我们的关系 |\n|---|------|------|------|-------------------|------------|\n| 1 | **AI Models Collapse When Trained on Recursively Generated Data** (Shumailov, Shumaylov, Zhao, Papernot, Anderson, Gal) | 2024 | Nature | 提出 model collapse 概念：在 synthetic data 上迭代训练导致分布尾部丢失和性能退化，在 VAE / GMM / LLM 上验证 | 我们工作的核心 motivation——Shumailov 证明了 synthetic contamination 的危害，我们提出用 provenance weighting 来缓解而非完全过滤 |\n| 2 | **Strong Model Collapse** (Dohmatob, Feng, Subramonian, Kempe) | 2025 | ICLR | 证明即使极小比例的 synthetic data（1/1000）也会导致 model collapse；用 operator-valued free probability theory 给出 bias-variance 分解 | 强化了 motivation——即使少量 synthetic data 也有害，说明我们的 provenance weighting 方法的必要性：不能靠 \"少量就没事\" 来忽视 |\n| 3 | **Is Model Collapse Inevitable? Breaking the Curse of Recursion by Accumulating Real and Synthetic Data** (Gerstgrasser, Schaeffer et al.) | 2024 | COLM | 证明如果 accumulate（而非 replace）数据，model collapse 可以避免；在 linear model 下证明 test error 有有限上界 | 与我们的方法互补——他们说 \"保留 real data 可以救\"，我们说 \"对 synthetic data 降权也可以救\"，都是 mitigate 而非 discard 的思路 |\n| 4 | **How Bad is Training on Synthetic Data? A Statistical Analysis of Language Model Collapse** (Seddik, Chen, Hayou, Youssef, Debbah) | 2024 | COLM | 给出 recursive training 的统计模型，证明纯 synthetic 训练不可避免 collapse，但 real + synthetic 混合训练在 synthetic 比例低于阈值时可避免 | 直接相关——他们给出了 synthetic data 比例的阈值分析，我们的 α_eff 理论可以看作这类阈值分析的推广（从 hard threshold 到 soft weighting） |\n| 5 | **Data Mixing Laws: Optimizing Data Mixtures by Predicting Language Modeling Performance** (Ye, Liu, Sun, Zhan, Zhou, Qiu) | 2025 | ICLR | 发现 domain mixture proportion 和 model performance 之间存在可预测的函数关系（data mixing laws），可以用小规模实验预测大模型表现 | Data mixing laws 可用于预测不同 provenance weight 设置下的 model performance——我们的 Grid-b 搜索可以理论上用 mixing laws 来加速 |\n| 6 | **Scaling Data-Constrained Language Models** (Muennighoff et al., 2023, 见第 1 节) | 2023 | NeurIPS | 数据受限下的 scaling law，重复 ≤4 epochs 影响可忽略 | 提供了数据受限场景的理论框架，我们的 α_eff 分析在此基础上进一步考虑了 contamination 的影响 |\n\n## Key Observations\n\n### 与现有工作的主要区别\n\n1. **Data selection vs. data weighting**: 多数现有方法（DSIR, FineWeb-Edu, D4）做 hard selection（保留或丢弃），我们做 soft weighting（降权但不丢弃），保留了更多数据多样性和信息。\n2. **Quality-based vs. provenance-based**: QuRating / FineWeb-Edu 基于 \"质量\" 评分，我们基于 \"来源\"（是否 synthetic）评分——这是正交的信号维度，可以组合使用。\n3. **Detection for filtering vs. detection for weighting**: 现有 synthetic text detection 工作（DetectGPT, Binoculars）几乎全部用于 binary filtering 或人工审核，我们首次将 calibrated detection score 用于 continuous training weight，对检测器的 calibration（ECE）提出了新要求。\n4. **Analytic weight function vs. learned weights**: 与 meta-learning reweighting（L2RW, Meta-Weight-Net）相比，我们的 weight = 1 - q^b 是 closed-form，无需 clean validation set 或 meta-optimization，更高效透明。\n\n### 最直接的竞争对手 / 对比工作\n\n- **Dynamic Loss-Based Sample Reweighting (Wang et al., ICLR 2025)**: 同为 instance-level reweighting for LLM pretraining，但信号来源不同（loss vs. provenance）。\n- **DoReMi (Xie et al., NeurIPS 2023)**: Domain-level reweighting，粒度不同但目标相似。\n- **FineWeb-Edu filtering**: 最接近的 \"data quality\" 竞品，但是 hard filtering 不是 soft weighting。\n\n### 潜在的引用遗漏风险\n\n- **Ghostbuster** (Verma et al., 2024): 另一个 feature-based synthetic text detector，可能需要作为 detection baseline 引用 [需确认场所]\n- **GPTZero**: 商业工具，学术论文 (2025 arXiv) 可作为检测方法的 context 引用 [需确认]\n- **Self-play fine-tuning / synthetic data augmentation 文献**: 我们的工作假设 synthetic data 有害，但有大量文献证明 synthetic data 在 fine-tuning 中有益——需要在 related work 中 acknowledge 并区分 pretraining contamination vs. fine-tuning augmentation 的不同场景\n- **Distributionally robust optimization (DRO) 基础文献**: Sagawa et al. (2020) Group DRO 等，作为 DoReMi 的理论基础可能需要提及\n- **Data influence / data attribution 文献**: TracIn, influence functions 等，虽然不是直接竞品但在 \"understanding data's effect on training\" 的大框架下相关\n",
    "structuredPatch": [
      {
        "oldStart": 43,
        "oldLines": 8,
        "newStart": 43,
        "newLines": 9,
        "lines": [
          " | 2 | **Strong Model Collapse** (Dohmatob, Feng, Subramonian, Kempe) | 2025 | ICLR | 证明即使极小比例的 synthetic data（1/1000）也会导致 model collapse；用 operator-valued free probability theory 给出 bias-variance 分解 | 强化了 motivation——即使少量 synthetic data 也有害，说明我们的 provenance weighting 方法的必要性：不能靠 \"少量就没事\" 来忽视 |",
          " | 3 | **Is Model Collapse Inevitable? Breaking the Curse of Recursion by Accumulating Real and Synthetic Data** (Gerstgrasser, Schaeffer et al.) | 2024 | COLM | 证明如果 accumulate（而非 replace）数据，model collapse 可以避免；在 linear model 下证明 test error 有有限上界 | 与我们的方法互补——他们说 \"保留 real data 可以救\"，我们说 \"对 synthetic data 降权也可以救\"，都是 mitigate 而非 discard 的思路 |",
          " | 4 | **How Bad is Training on Synthetic Data? A Statistical Analysis of Language Model Collapse** (Seddik, Chen, Hayou, Youssef, Debbah) | 2024 | COLM | 给出 recursive training 的统计模型，证明纯 synthetic 训练不可避免 collapse，但 real + synthetic 混合训练在 synthetic 比例低于阈值时可避免 | 直接相关——他们给出了 synthetic data 比例的阈值分析，我们的 α_eff 理论可以看作这类阈值分析的推广（从 hard threshold 到 soft weighting） |",
          "-| 5 | **Data Mixing Laws: Optimizing Data Mixtures by Predicting Language Modeling Performance** (Ye, Liu, Sun, Zhan, Zhou, Qiu) | 2025 | ICLR | 发现 domain mixture proportion 和 model performance 之间存在可预测的函数关系（data mixing laws），可以用小规模实验预测大模型表现 | Data mixing laws 可用于预测不同 provenance weight 设置下的 model performance——我们的 Grid-b 搜索可以理论上用 mixing laws 来加速 |",
          "-| 6 | **Scaling Data-Constrained Language Models** (Muennighoff et al., 2023, 见第 1 节) | 2023 | NeurIPS | 数据受限下的 scaling law，重复 ≤4 epochs 影响可忽略 | 提供了数据受限场景的理论框架，我们的 α_eff 分析在此基础上进一步考虑了 contamination 的影响 |",
          "+| 5 | **Can Generative Artificial Intelligence Survive Data Contamination? Theoretical Guarantees under Contaminated Recursive Training** (Wang, Niu, Li) | 2026 | arXiv 2602.16065 | 为 contaminated recursive training 提供收敛保证：bound d(ℙ̂_t, ℙ_0) ≲ t^{−min{p,α}}，推广至 non-Gaussian 设置；Assumption A2 限制 d 为凸度量，显式排除 cross-entropy/KL | 该论文的收敛 bound 直接启发了我们的 α_eff 定义和 b* 推导——α_eff(b) 将其理论中的 α 从 known parameter 变为 detector-estimated quantity，是我们方法的理论 motivation（非 contribution） |",
          "+| 6 | **Data Mixing Laws: Optimizing Data Mixtures by Predicting Language Modeling Performance** (Ye, Liu, Sun, Zhan, Zhou, Qiu) | 2025 | ICLR | 发现 domain mixture proportion 和 model performance 之间存在可预测的函数关系（data mixing laws），可以用小规模实验预测大模型表现 | Data mixing laws 可用于预测不同 provenance weight 设置下的 model performance——我们的 Grid-b 搜索可以理论上用 mixing laws 来加速 |",
          "+| 7 | **Scaling Data-Constrained Language Models** (Muennighoff et al., 2023, 见第 1 节) | 2023 | NeurIPS | 数据受限下的 scaling law，重复 ≤4 epochs 影响可忽略 | 提供了数据受限场景的理论框架，我们的 α_eff 分析在此基础上进一步考虑了 contamination 的影响 |",
          " ",
          " ## Key Observations",
          " "
        ]
      }
    ],
    "userModified": false,
    "replaceAll": false
  }
}
```

</details>

---

### Tool call

_source line 69_

<details open><summary>🔧 Tool call — Edit · `toolu_016LTxsERzaXRYD28dmkkePh`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/related_work_notes.md",
  "old_string": "| 6 | **A Survey on LLM-Generated Text Detection: Necessity, Methods, and Future Directions** (Wu et al.) | 2024 | Computational Linguistics (MIT Press) | 系统综述 statistical / neural / watermarking 三类检测方法，讨论 robustness 和 generalization | 综述文献，帮助定位我们的检测器在整个 detection 方法谱系中的位置——我们是 training-based statistical classifier，但用于 weighting 而非 filtering |",
  "new_string": "| 6 | **A Survey on LLM-Generated Text Detection: Necessity, Methods, and Future Directions** (Wu et al.) | 2024 | Computational Linguistics (MIT Press) | 系统综述 statistical / neural / watermarking 三类检测方法，讨论 robustness 和 generalization | 综述文献，帮助定位我们的检测器在整个 detection 方法谱系中的位置——我们是 training-based statistical classifier，但用于 weighting 而非 filtering |\n| 7 | **Ghostbuster: Detecting Text Ghostwritten by Large Language Models** (Verma, Fleisig, Tomlin, Klein) | 2024 | NAACL | 用 structured search 在多个弱 LM 的特征空间中组合 features，训练分类器检测 AI 生成文本；无需 target model 的 token probabilities，跨域 F1 达 99.0 | 架构上与我们的 TF-IDF + LogReg 检测器最接近——都用 lightweight features + 训练分类器，不依赖 target model access；区别在于我们需要 calibrated q-score 而非 binary detection |"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "0a05528b-d05d-4fb3-947f-20e0adce1e25",
  "uuid": "8b6880a1-f68b-416c-b1ed-92ae447861a8",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TQgZyeeTg6kc9Y153raUc6",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1340,
      "cache_read_input_tokens": 58518,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1340
      },
      "output_tokens": 39,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool result

_source line 70 · 2026-05-14T12:36:37.132Z_

<details><summary>↩ Tool result · `toolu_016LTxsERzaXRYD28dmkkePh`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/related_work_notes.md has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "0a05528b-d05d-4fb3-947f-20e0adce1e25",
  "uuid": "17e12048-e1bd-401a-89d6-3130da9ef1ee",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/related_work_notes.md",
    "oldString": "| 6 | **A Survey on LLM-Generated Text Detection: Necessity, Methods, and Future Directions** (Wu et al.) | 2024 | Computational Linguistics (MIT Press) | 系统综述 statistical / neural / watermarking 三类检测方法，讨论 robustness 和 generalization | 综述文献，帮助定位我们的检测器在整个 detection 方法谱系中的位置——我们是 training-based statistical classifier，但用于 weighting 而非 filtering |",
    "newString": "| 6 | **A Survey on LLM-Generated Text Detection: Necessity, Methods, and Future Directions** (Wu et al.) | 2024 | Computational Linguistics (MIT Press) | 系统综述 statistical / neural / watermarking 三类检测方法，讨论 robustness 和 generalization | 综述文献，帮助定位我们的检测器在整个 detection 方法谱系中的位置——我们是 training-based statistical classifier，但用于 weighting 而非 filtering |\n| 7 | **Ghostbuster: Detecting Text Ghostwritten by Large Language Models** (Verma, Fleisig, Tomlin, Klein) | 2024 | NAACL | 用 structured search 在多个弱 LM 的特征空间中组合 features，训练分类器检测 AI 生成文本；无需 target model 的 token probabilities，跨域 F1 达 99.0 | 架构上与我们的 TF-IDF + LogReg 检测器最接近——都用 lightweight features + 训练分类器，不依赖 target model access；区别在于我们需要 calibrated q-score 而非 binary detection |",
    "originalFile": "# Related Work Survey — Provenance Weight Training\n\n## 1. Data Quality / Data Selection for LLM Pretraining\n\n| # | 论文 | 年份 | 场所 | 一句话 Contribution | 与我们的关系 |\n|---|------|------|------|-------------------|------------|\n| 1 | **DSIR: Data Selection for Language Models via Importance Resampling** (Xie, Santurkar, Ma, Liang) | 2023 | NeurIPS | 用 hashed n-gram 特征估计 importance weight，对大规模语料做 importance resampling 来匹配目标分布 | DSIR 按目标分布做 selection，我们按 provenance 做 weighting——都用 lightweight feature 做数据筛选，但动机不同：DSIR 优化 domain match，我们降低 synthetic contamination |\n| 2 | **QuRating: Selecting High-Quality Data for Training Language Models** (Wettig, Gupta, Malik, Chen) | 2024 | ICML | 用 LLM pairwise judgment 对数据做 4 维质量评分（writing style / expertise / facts / educational value），训练 QuRater 模型标注 260B 语料 | QuRating 用 LLM 判断 \"质量\"，我们用检测器判断 \"来源\"——都是 model-based annotation + downstream reweighting，但 quality 和 provenance 是正交维度 |\n| 3 | **The FineWeb Datasets: Decanting the Web for the Finest Text Data at Scale** (Penedo et al., HuggingFace) | 2024 | arXiv | 用 Llama-3-70B 合成标注训练 educational quality classifier，过滤出 1.3T token 的 FineWeb-Edu，在 MMLU/ARC 上大幅领先 | FineWeb-Edu 用 LLM-based classifier 做 hard filtering（保留/丢弃），我们用 detector 做 soft weighting（降权不丢弃），保留更多数据多样性 |\n| 4 | **D4: Improving LLM Pretraining via Document De-Duplication and Diversification** (Tirumala, Simig et al.) | 2023 | NeurIPS D&B | 用 pretrained embedding + K-Means 做去重和多样性平衡，6.7B 模型上提升 2% 下游准确率和 20% 训练效率 | D4 关注重复和多样性，我们关注 synthetic contamination——互补方法，可以先 D4 去重再用我们的 provenance weighting |\n| 5 | **DoReMi: Optimizing Data Mixtures Speeds Up Language Model Pretraining** (Xie, Pham et al.) | 2023 | NeurIPS | 用 Group DRO 在 proxy model 上优化 domain mixture weights，无需下游任务信息，8B 模型提升 6.5% few-shot 准确率 | DoReMi 做 domain-level reweighting（按 domain 调权），我们做 instance-level reweighting（按 q-score 调权）——粒度不同，理论上可以组合使用 |\n| 6 | **DataComp-LM (DCLM): In Search of the Next Generation of Training Sets for Language Models** (Li et al.) | 2024 | NeurIPS D&B | 提供 240T token 标准化语料 + 评估套件，系统性对比 data curation 策略，证明 model-based filtering 是关键 | DCLM 是 benchmark 框架，我们的 provenance-based weighting 可以作为一种新的 curation strategy 在 DCLM 上评估 |\n| 7 | **Scaling Data-Constrained Language Models** (Muennighoff, Rush et al.) | 2023 | NeurIPS | 系统研究数据受限时的 scaling law，发现 ≤4 epochs 重复数据对 loss 影响可忽略，提出考虑重复衰减的 compute-optimal law | 当 unique data 不足时更可能混入 synthetic data 来补量——我们的方法提供了一种替代方案：不用丢弃 synthetic data，而是降权使用 |\n\n## 2. Synthetic Data Contamination Detection\n\n| # | 论文 | 年份 | 场所 | 一句话 Contribution | 与我们的关系 |\n|---|------|------|------|-------------------|------------|\n| 1 | **DetectGPT: Zero-Shot Machine-Generated Text Detection using Probability Curvature** (Mitchell et al.) | 2023 | ICML | 零样本检测：用 log probability curvature（在 perturbation 前后的 log-prob 变化）区分 human vs machine text，无需训练分类器 | DetectGPT 做 binary detection（是否机器生成），我们需要 calibrated probability（q-score）——我们选择 TF-IDF + LogReg 正是因为需要 well-calibrated 的连续 score 而非仅 binary 判断 |\n| 2 | **Fast-DetectGPT: Efficient Zero-Shot Detection via Conditional Probability Curvature** (Bao et al.) | 2024 | ICLR | 将 DetectGPT 的 perturbation 步骤替换为 sampling，加速 340 倍且 AUROC 提升约 75% | 同上——更高效但仍是 binary detection，calibration 质量（ECE）未被重点评估，而这正是我们工作的核心关注点 |\n| 3 | **Binoculars: Zero-Shot Detection of LLM-Generated Text** (Hans et al.) | 2024 | ICML | 用两个 LLM 的 perplexity / cross-perplexity 比值做检测，ChatGPT 文本在 0.01% FPR 下召回 >90% | Binoculars 需要两个 LLM 推理，计算成本高；我们的 TF-IDF + LogReg 检测器极轻量，适合标注数十亿 token 级别的 pretraining corpus |\n| 4 | **GLTR: Statistical Detection and Visualization of Generated Text** (Gehrmann, Strobelt, Rush) | 2019 | ACL | 用 LM 的 top-k token 排名做统计检测和可视化，帮助人类识别机器文本（人类检测率从 54% 提升到 72%） | 早期 statistical detection 工作，启发了后续基于 model statistics 的方法；我们的方法同样基于统计特征但目标不同（scoring for weighting 而非 human-in-the-loop detection） |\n| 5 | **A Watermark for Large Language Models** (Kirchenbauer et al.) | 2023 | ICML | 在生成时嵌入 statistical watermark（green/red token list），可用 p-value 统计检验来检测 | Watermarking 需要控制生成过程，无法检测已有的、未 watermarked 的 synthetic data——我们的场景是 post-hoc detection on existing corpus |\n| 6 | **A Survey on LLM-Generated Text Detection: Necessity, Methods, and Future Directions** (Wu et al.) | 2024 | Computational Linguistics (MIT Press) | 系统综述 statistical / neural / watermarking 三类检测方法，讨论 robustness 和 generalization | 综述文献，帮助定位我们的检测器在整个 detection 方法谱系中的位置——我们是 training-based statistical classifier，但用于 weighting 而非 filtering |\n\n## 3. Sample Reweighting in Training\n\n| # | 论文 | 年份 | 场所 | 一句话 Contribution | 与我们的关系 |\n|---|------|------|------|-------------------|------------|\n| 1 | **Machine-Generated Text Detection Prevents Language Model Collapse** (Drayson, Yilmaz, Lampos) | 2025 | EMNLP | 首次提出 detect-and-reweight 框架缓解 model collapse：用 binary detector 检测 synthetic text，通过 importance resampling 降权 synthetic samples，在 GPT-2 / SmolLM2（4 LLM, 2 families, 6 decoding strategies）上验证有效性 | 我们最直接的前驱工作——他们开创了 detect-and-reweight 范式，但权重指数 b 是需要 grid search 的 heuristic hyperparameter，且仅评估 single-generator 场景（WikiText-2）；我们提供理论启发的 adaptive b* 替代 grid search，并扩展到 multi-generator web-scale 场景 |\n| 2 | **Improving the Accuracy of Likelihood-based Inference under Covariate Shift** (Shimodaira) | 2000 | JASA | 奠基性工作：提出 importance weighted ERM（IWERM），通过 density ratio 修正 covariate shift 下的 loss | 理论基础直接相关——我们的 weight = 1 - q^b 可以看作一种 bounded importance weight，Shimodaira 的 IWERM 理论为我们的方法提供了正当性 |\n| 3 | **Learning to Reweight Examples for Robust Deep Learning** (Ren, Zeng, Yang, Urtasun) | 2018 | ICML | 用 meta-learning 在训练中动态学习 sample weights（基于 gradient direction 在 clean validation set 上的表现） | L2RW 需要 clean validation set 做 meta-optimization，我们的方法不需要——weight 由 provenance detector 预先确定，无需在训练中迭代调整 |\n| 4 | **Meta-Weight-Net: Learning an Explicit Mapping For Sample Weighting** (Shu et al.) | 2019 | NeurIPS | 用 MLP 学习 loss → weight 的显式映射函数，在 noisy label 和 class imbalance 场景下优于手工设计的 weighting | 与 L2RW 类似用 meta-learning；我们的 weight function 是 analytic form（1 - q^b），不需要 meta-learning，更透明可解释 |\n| 5 | **Curriculum Learning** (Bengio, Louradour, Collobert, Weston) | 2009 | ICML | 奠基性工作：证明按从易到难的顺序训练（curriculum）可以加速收敛并改善 non-convex optimization 的局部极小值 | Curriculum learning 按难度排序，我们按 provenance 加权——虽然形式不同（排序 vs 加权），但都是 non-uniform training 的思想 |\n| 6 | **Dynamic Loss-Based Sample Reweighting for Improved LLM Pretraining** (Wang et al.) | 2025 | ICLR | 在 LLM pretraining 中做 instance-level dynamic reweighting（基于 loss 值在线调整权重），提出 LinUpper / Quadratic 等策略 | 最直接的对比工作之一——他们基于 loss 做 weighting，我们基于 provenance 做 weighting。两者可组合：先用 provenance weight 再用 loss-based dynamic adjustment |\n| 7 | **DoReMi** (Xie et al., 2023, 见第 1 节) | 2023 | NeurIPS | Domain-level reweighting via Group DRO | 我们做 instance-level provenance weighting，DoReMi 做 domain-level mixture optimization——粒度和信号来源不同 |\n\n## 4. Theoretical Analysis of Data Mixing / Contamination\n\n| # | 论文 | 年份 | 场所 | 一句话 Contribution | 与我们的关系 |\n|---|------|------|------|-------------------|------------|\n| 1 | **AI Models Collapse When Trained on Recursively Generated Data** (Shumailov, Shumaylov, Zhao, Papernot, Anderson, Gal) | 2024 | Nature | 提出 model collapse 概念：在 synthetic data 上迭代训练导致分布尾部丢失和性能退化，在 VAE / GMM / LLM 上验证 | 我们工作的核心 motivation——Shumailov 证明了 synthetic contamination 的危害，我们提出用 provenance weighting 来缓解而非完全过滤 |\n| 2 | **Strong Model Collapse** (Dohmatob, Feng, Subramonian, Kempe) | 2025 | ICLR | 证明即使极小比例的 synthetic data（1/1000）也会导致 model collapse；用 operator-valued free probability theory 给出 bias-variance 分解 | 强化了 motivation——即使少量 synthetic data 也有害，说明我们的 provenance weighting 方法的必要性：不能靠 \"少量就没事\" 来忽视 |\n| 3 | **Is Model Collapse Inevitable? Breaking the Curse of Recursion by Accumulating Real and Synthetic Data** (Gerstgrasser, Schaeffer et al.) | 2024 | COLM | 证明如果 accumulate（而非 replace）数据，model collapse 可以避免；在 linear model 下证明 test error 有有限上界 | 与我们的方法互补——他们说 \"保留 real data 可以救\"，我们说 \"对 synthetic data 降权也可以救\"，都是 mitigate 而非 discard 的思路 |\n| 4 | **How Bad is Training on Synthetic Data? A Statistical Analysis of Language Model Collapse** (Seddik, Chen, Hayou, Youssef, Debbah) | 2024 | COLM | 给出 recursive training 的统计模型，证明纯 synthetic 训练不可避免 collapse，但 real + synthetic 混合训练在 synthetic 比例低于阈值时可避免 | 直接相关——他们给出了 synthetic data 比例的阈值分析，我们的 α_eff 理论可以看作这类阈值分析的推广（从 hard threshold 到 soft weighting） |\n| 5 | **Can Generative Artificial Intelligence Survive Data Contamination? Theoretical Guarantees under Contaminated Recursive Training** (Wang, Niu, Li) | 2026 | arXiv 2602.16065 | 为 contaminated recursive training 提供收敛保证：bound d(ℙ̂_t, ℙ_0) ≲ t^{−min{p,α}}，推广至 non-Gaussian 设置；Assumption A2 限制 d 为凸度量，显式排除 cross-entropy/KL | 该论文的收敛 bound 直接启发了我们的 α_eff 定义和 b* 推导——α_eff(b) 将其理论中的 α 从 known parameter 变为 detector-estimated quantity，是我们方法的理论 motivation（非 contribution） |\n| 6 | **Data Mixing Laws: Optimizing Data Mixtures by Predicting Language Modeling Performance** (Ye, Liu, Sun, Zhan, Zhou, Qiu) | 2025 | ICLR | 发现 domain mixture proportion 和 model performance 之间存在可预测的函数关系（data mixing laws），可以用小规模实验预测大模型表现 | Data mixing laws 可用于预测不同 provenance weight 设置下的 model performance——我们的 Grid-b 搜索可以理论上用 mixing laws 来加速 |\n| 7 | **Scaling Data-Constrained Language Models** (Muennighoff et al., 2023, 见第 1 节) | 2023 | NeurIPS | 数据受限下的 scaling law，重复 ≤4 epochs 影响可忽略 | 提供了数据受限场景的理论框架，我们的 α_eff 分析在此基础上进一步考虑了 contamination 的影响 |\n\n## Key Observations\n\n### 与现有工作的主要区别\n\n1. **Data selection vs. data weighting**: 多数现有方法（DSIR, FineWeb-Edu, D4）做 hard selection（保留或丢弃），我们做 soft weighting（降权但不丢弃），保留了更多数据多样性和信息。\n2. **Quality-based vs. provenance-based**: QuRating / FineWeb-Edu 基于 \"质量\" 评分，我们基于 \"来源\"（是否 synthetic）评分——这是正交的信号维度，可以组合使用。\n3. **Detection for filtering vs. detection for weighting**: 现有 synthetic text detection 工作（DetectGPT, Binoculars）几乎全部用于 binary filtering 或人工审核，我们首次将 calibrated detection score 用于 continuous training weight，对检测器的 calibration（ECE）提出了新要求。\n4. **Analytic weight function vs. learned weights**: 与 meta-learning reweighting（L2RW, Meta-Weight-Net）相比，我们的 weight = 1 - q^b 是 closed-form，无需 clean validation set 或 meta-optimization，更高效透明。\n\n### 最直接的竞争对手 / 对比工作\n\n- **Dynamic Loss-Based Sample Reweighting (Wang et al., ICLR 2025)**: 同为 instance-level reweighting for LLM pretraining，但信号来源不同（loss vs. provenance）。\n- **DoReMi (Xie et al., NeurIPS 2023)**: Domain-level reweighting，粒度不同但目标相似。\n- **FineWeb-Edu filtering**: 最接近的 \"data quality\" 竞品，但是 hard filtering 不是 soft weighting。\n\n### 潜在的引用遗漏风险\n\n- **Ghostbuster** (Verma et al., 2024): 另一个 feature-based synthetic text detector，可能需要作为 detection baseline 引用 [需确认场所]\n- **GPTZero**: 商业工具，学术论文 (2025 arXiv) 可作为检测方法的 context 引用 [需确认]\n- **Self-play fine-tuning / synthetic data augmentation 文献**: 我们的工作假设 synthetic data 有害，但有大量文献证明 synthetic data 在 fine-tuning 中有益——需要在 related work 中 acknowledge 并区分 pretraining contamination vs. fine-tuning augmentation 的不同场景\n- **Distributionally robust optimization (DRO) 基础文献**: Sagawa et al. (2020) Group DRO 等，作为 DoReMi 的理论基础可能需要提及\n- **Data influence / data attribution 文献**: TracIn, influence functions 等，虽然不是直接竞品但在 \"understanding data's effect on training\" 的大框架下相关\n",
    "structuredPatch": [
      {
        "oldStart": 22,
        "oldLines": 6,
        "newStart": 22,
        "newLines": 7,
        "lines": [
          " | 4 | **GLTR: Statistical Detection and Visualization of Generated Text** (Gehrmann, Strobelt, Rush) | 2019 | ACL | 用 LM 的 top-k token 排名做统计检测和可视化，帮助人类识别机器文本（人类检测率从 54% 提升到 72%） | 早期 statistical detection 工作，启发了后续基于 model statistics 的方法；我们的方法同样基于统计特征但目标不同（scoring for weighting 而非 human-in-the-loop detection） |",
          " | 5 | **A Watermark for Large Language Models** (Kirchenbauer et al.) | 2023 | ICML | 在生成时嵌入 statistical watermark（green/red token list），可用 p-value 统计检验来检测 | Watermarking 需要控制生成过程，无法检测已有的、未 watermarked 的 synthetic data——我们的场景是 post-hoc detection on existing corpus |",
          " | 6 | **A Survey on LLM-Generated Text Detection: Necessity, Methods, and Future Directions** (Wu et al.) | 2024 | Computational Linguistics (MIT Press) | 系统综述 statistical / neural / watermarking 三类检测方法，讨论 robustness 和 generalization | 综述文献，帮助定位我们的检测器在整个 detection 方法谱系中的位置——我们是 training-based statistical classifier，但用于 weighting 而非 filtering |",
          "+| 7 | **Ghostbuster: Detecting Text Ghostwritten by Large Language Models** (Verma, Fleisig, Tomlin, Klein) | 2024 | NAACL | 用 structured search 在多个弱 LM 的特征空间中组合 features，训练分类器检测 AI 生成文本；无需 target model 的 token probabilities，跨域 F1 达 99.0 | 架构上与我们的 TF-IDF + LogReg 检测器最接近——都用 lightweight features + 训练分类器，不依赖 target model access；区别在于我们需要 calibrated q-score 而非 binary detection |",
          " ",
          " ## 3. Sample Reweighting in Training",
          " "
        ]
      }
    ],
    "userModified": false,
    "replaceAll": false
  }
}
```

</details>

---

### Assistant

_source line 71_

Now replace the "潜在的引用遗漏风险" section with the decision record.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "0a05528b-d05d-4fb3-947f-20e0adce1e25",
  "uuid": "805adde3-d709-4922-9855-511a51ac1e35",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Da66aiDJXQJnrSHyHTzsZo",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 659,
      "cache_read_input_tokens": 59858,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 659
      },
      "output_tokens": 1,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool call

_source line 72_

<details open><summary>🔧 Tool call — Edit · `toolu_018GNK4yUc6xtq3Hrenwpy2x`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/related_work_notes.md",
  "old_string": "### 潜在的引用遗漏风险\n\n- **Ghostbuster** (Verma et al., 2024): 另一个 feature-based synthetic text detector，可能需要作为 detection baseline 引用 [需确认场所]\n- **GPTZero**: 商业工具，学术论文 (2025 arXiv) 可作为检测方法的 context 引用 [需确认]\n- **Self-play fine-tuning / synthetic data augmentation 文献**: 我们的工作假设 synthetic data 有害，但有大量文献证明 synthetic data 在 fine-tuning 中有益——需要在 related work 中 acknowledge 并区分 pretraining contamination vs. fine-tuning augmentation 的不同场景\n- **Distributionally robust optimization (DRO) 基础文献**: Sagawa et al. (2020) Group DRO 等，作为 DoReMi 的理论基础可能需要提及\n- **Data influence / data attribution 文献**: TracIn, influence functions 等，虽然不是直接竞品但在 \"understanding data's effect on training\" 的大框架下相关",
  "new_string": "### 引用决策记录\n\n| # | 候选论文 | 决策 | 理由 |\n|---|---------|------|------|\n| 1 | **Ghostbuster** (Verma, Fleisig, Tomlin, Klein, NAACL 2024) | ✅ 收录 → Section 2 #7 | Feature-based detector，架构与我们的 TF-IDF + LogReg 最接近（lightweight features + classifier, 无需 target model access），审稿人可能质疑遗漏 |\n| 2 | **GPTZero** | ❌ 不收录 | 商业工具，无同行评审的方法学论文。现有学术文献均为第三方评估（准确率测试），非方法贡献。学术 related work 中引用商业产品无先例价值 |\n| 3 | **Self-play fine-tuning / synthetic data augmentation** (代表性工作：SPIN, Chen et al., ICML 2024; Self-Instruct, Wang et al., ACL 2023) | ❌ 不收录为单独条目 | 我们关注的是 pretraining 阶段不可控的 synthetic contamination（来源未知、比例未知），与 fine-tuning 阶段有意使用 synthetic data augmentation 是不同场景。建议在 Related Work 正文中用一句话 acknowledge 此区别（\"We focus on uncontrolled synthetic contamination in pretraining, distinct from intentional synthetic augmentation in fine-tuning (Chen et al., 2024)\"），但无需展开讨论 |\n| 4 | **Group DRO** (Sagawa, Koh, Hashimoto, Liang, ICLR 2020) | ❌ 不收录 | DoReMi 引用已覆盖 Group DRO 理论基础。我们是 instance-level provenance weighting，与 Group DRO 的 group-level worst-case optimization 无直接可比性。审稿人不太可能因缺 Group DRO 引用而提问 |\n| 5 | **Data influence / data attribution** (TracIn, Pruthi et al., NeurIPS 2020; Influence Functions, Koh & Liang, ICML 2017) | ❌ 不收录 | 我们不做 post-hoc influence estimation，而是基于 provenance 做 pre-hoc weighting。目标不同（归因 vs 降权）、方法不同（梯度追踪 vs 检测器评分）、场景不同（诊断 vs 训练干预）。引了反而分散 detect-and-reweight 的主线叙事 |"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "0a05528b-d05d-4fb3-947f-20e0adce1e25",
  "uuid": "c2dae7f2-0392-4d8e-a833-1982128c9a90",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Da66aiDJXQJnrSHyHTzsZo",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 659,
      "cache_read_input_tokens": 59858,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 659
      },
      "output_tokens": 1,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool result

_source line 73 · 2026-05-14T12:37:04.244Z_

<details><summary>↩ Tool result · `toolu_018GNK4yUc6xtq3Hrenwpy2x`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/related_work_notes.md has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "0a05528b-d05d-4fb3-947f-20e0adce1e25",
  "uuid": "e4755185-4d23-4e42-87ee-dc754d2fdc3c",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/related_work_notes.md",
    "oldString": "### 潜在的引用遗漏风险\n\n- **Ghostbuster** (Verma et al., 2024): 另一个 feature-based synthetic text detector，可能需要作为 detection baseline 引用 [需确认场所]\n- **GPTZero**: 商业工具，学术论文 (2025 arXiv) 可作为检测方法的 context 引用 [需确认]\n- **Self-play fine-tuning / synthetic data augmentation 文献**: 我们的工作假设 synthetic data 有害，但有大量文献证明 synthetic data 在 fine-tuning 中有益——需要在 related work 中 acknowledge 并区分 pretraining contamination vs. fine-tuning augmentation 的不同场景\n- **Distributionally robust optimization (DRO) 基础文献**: Sagawa et al. (2020) Group DRO 等，作为 DoReMi 的理论基础可能需要提及\n- **Data influence / data attribution 文献**: TracIn, influence functions 等，虽然不是直接竞品但在 \"understanding data's effect on training\" 的大框架下相关",
    "newString": "### 引用决策记录\n\n| # | 候选论文 | 决策 | 理由 |\n|---|---------|------|------|\n| 1 | **Ghostbuster** (Verma, Fleisig, Tomlin, Klein, NAACL 2024) | ✅ 收录 → Section 2 #7 | Feature-based detector，架构与我们的 TF-IDF + LogReg 最接近（lightweight features + classifier, 无需 target model access），审稿人可能质疑遗漏 |\n| 2 | **GPTZero** | ❌ 不收录 | 商业工具，无同行评审的方法学论文。现有学术文献均为第三方评估（准确率测试），非方法贡献。学术 related work 中引用商业产品无先例价值 |\n| 3 | **Self-play fine-tuning / synthetic data augmentation** (代表性工作：SPIN, Chen et al., ICML 2024; Self-Instruct, Wang et al., ACL 2023) | ❌ 不收录为单独条目 | 我们关注的是 pretraining 阶段不可控的 synthetic contamination（来源未知、比例未知），与 fine-tuning 阶段有意使用 synthetic data augmentation 是不同场景。建议在 Related Work 正文中用一句话 acknowledge 此区别（\"We focus on uncontrolled synthetic contamination in pretraining, distinct from intentional synthetic augmentation in fine-tuning (Chen et al., 2024)\"），但无需展开讨论 |\n| 4 | **Group DRO** (Sagawa, Koh, Hashimoto, Liang, ICLR 2020) | ❌ 不收录 | DoReMi 引用已覆盖 Group DRO 理论基础。我们是 instance-level provenance weighting，与 Group DRO 的 group-level worst-case optimization 无直接可比性。审稿人不太可能因缺 Group DRO 引用而提问 |\n| 5 | **Data influence / data attribution** (TracIn, Pruthi et al., NeurIPS 2020; Influence Functions, Koh & Liang, ICML 2017) | ❌ 不收录 | 我们不做 post-hoc influence estimation，而是基于 provenance 做 pre-hoc weighting。目标不同（归因 vs 降权）、方法不同（梯度追踪 vs 检测器评分）、场景不同（诊断 vs 训练干预）。引了反而分散 detect-and-reweight 的主线叙事 |",
    "originalFile": "# Related Work Survey — Provenance Weight Training\n\n## 1. Data Quality / Data Selection for LLM Pretraining\n\n| # | 论文 | 年份 | 场所 | 一句话 Contribution | 与我们的关系 |\n|---|------|------|------|-------------------|------------|\n| 1 | **DSIR: Data Selection for Language Models via Importance Resampling** (Xie, Santurkar, Ma, Liang) | 2023 | NeurIPS | 用 hashed n-gram 特征估计 importance weight，对大规模语料做 importance resampling 来匹配目标分布 | DSIR 按目标分布做 selection，我们按 provenance 做 weighting——都用 lightweight feature 做数据筛选，但动机不同：DSIR 优化 domain match，我们降低 synthetic contamination |\n| 2 | **QuRating: Selecting High-Quality Data for Training Language Models** (Wettig, Gupta, Malik, Chen) | 2024 | ICML | 用 LLM pairwise judgment 对数据做 4 维质量评分（writing style / expertise / facts / educational value），训练 QuRater 模型标注 260B 语料 | QuRating 用 LLM 判断 \"质量\"，我们用检测器判断 \"来源\"——都是 model-based annotation + downstream reweighting，但 quality 和 provenance 是正交维度 |\n| 3 | **The FineWeb Datasets: Decanting the Web for the Finest Text Data at Scale** (Penedo et al., HuggingFace) | 2024 | arXiv | 用 Llama-3-70B 合成标注训练 educational quality classifier，过滤出 1.3T token 的 FineWeb-Edu，在 MMLU/ARC 上大幅领先 | FineWeb-Edu 用 LLM-based classifier 做 hard filtering（保留/丢弃），我们用 detector 做 soft weighting（降权不丢弃），保留更多数据多样性 |\n| 4 | **D4: Improving LLM Pretraining via Document De-Duplication and Diversification** (Tirumala, Simig et al.) | 2023 | NeurIPS D&B | 用 pretrained embedding + K-Means 做去重和多样性平衡，6.7B 模型上提升 2% 下游准确率和 20% 训练效率 | D4 关注重复和多样性，我们关注 synthetic contamination——互补方法，可以先 D4 去重再用我们的 provenance weighting |\n| 5 | **DoReMi: Optimizing Data Mixtures Speeds Up Language Model Pretraining** (Xie, Pham et al.) | 2023 | NeurIPS | 用 Group DRO 在 proxy model 上优化 domain mixture weights，无需下游任务信息，8B 模型提升 6.5% few-shot 准确率 | DoReMi 做 domain-level reweighting（按 domain 调权），我们做 instance-level reweighting（按 q-score 调权）——粒度不同，理论上可以组合使用 |\n| 6 | **DataComp-LM (DCLM): In Search of the Next Generation of Training Sets for Language Models** (Li et al.) | 2024 | NeurIPS D&B | 提供 240T token 标准化语料 + 评估套件，系统性对比 data curation 策略，证明 model-based filtering 是关键 | DCLM 是 benchmark 框架，我们的 provenance-based weighting 可以作为一种新的 curation strategy 在 DCLM 上评估 |\n| 7 | **Scaling Data-Constrained Language Models** (Muennighoff, Rush et al.) | 2023 | NeurIPS | 系统研究数据受限时的 scaling law，发现 ≤4 epochs 重复数据对 loss 影响可忽略，提出考虑重复衰减的 compute-optimal law | 当 unique data 不足时更可能混入 synthetic data 来补量——我们的方法提供了一种替代方案：不用丢弃 synthetic data，而是降权使用 |\n\n## 2. Synthetic Data Contamination Detection\n\n| # | 论文 | 年份 | 场所 | 一句话 Contribution | 与我们的关系 |\n|---|------|------|------|-------------------|------------|\n| 1 | **DetectGPT: Zero-Shot Machine-Generated Text Detection using Probability Curvature** (Mitchell et al.) | 2023 | ICML | 零样本检测：用 log probability curvature（在 perturbation 前后的 log-prob 变化）区分 human vs machine text，无需训练分类器 | DetectGPT 做 binary detection（是否机器生成），我们需要 calibrated probability（q-score）——我们选择 TF-IDF + LogReg 正是因为需要 well-calibrated 的连续 score 而非仅 binary 判断 |\n| 2 | **Fast-DetectGPT: Efficient Zero-Shot Detection via Conditional Probability Curvature** (Bao et al.) | 2024 | ICLR | 将 DetectGPT 的 perturbation 步骤替换为 sampling，加速 340 倍且 AUROC 提升约 75% | 同上——更高效但仍是 binary detection，calibration 质量（ECE）未被重点评估，而这正是我们工作的核心关注点 |\n| 3 | **Binoculars: Zero-Shot Detection of LLM-Generated Text** (Hans et al.) | 2024 | ICML | 用两个 LLM 的 perplexity / cross-perplexity 比值做检测，ChatGPT 文本在 0.01% FPR 下召回 >90% | Binoculars 需要两个 LLM 推理，计算成本高；我们的 TF-IDF + LogReg 检测器极轻量，适合标注数十亿 token 级别的 pretraining corpus |\n| 4 | **GLTR: Statistical Detection and Visualization of Generated Text** (Gehrmann, Strobelt, Rush) | 2019 | ACL | 用 LM 的 top-k token 排名做统计检测和可视化，帮助人类识别机器文本（人类检测率从 54% 提升到 72%） | 早期 statistical detection 工作，启发了后续基于 model statistics 的方法；我们的方法同样基于统计特征但目标不同（scoring for weighting 而非 human-in-the-loop detection） |\n| 5 | **A Watermark for Large Language Models** (Kirchenbauer et al.) | 2023 | ICML | 在生成时嵌入 statistical watermark（green/red token list），可用 p-value 统计检验来检测 | Watermarking 需要控制生成过程，无法检测已有的、未 watermarked 的 synthetic data——我们的场景是 post-hoc detection on existing corpus |\n| 6 | **A Survey on LLM-Generated Text Detection: Necessity, Methods, and Future Directions** (Wu et al.) | 2024 | Computational Linguistics (MIT Press) | 系统综述 statistical / neural / watermarking 三类检测方法，讨论 robustness 和 generalization | 综述文献，帮助定位我们的检测器在整个 detection 方法谱系中的位置——我们是 training-based statistical classifier，但用于 weighting 而非 filtering |\n| 7 | **Ghostbuster: Detecting Text Ghostwritten by Large Language Models** (Verma, Fleisig, Tomlin, Klein) | 2024 | NAACL | 用 structured search 在多个弱 LM 的特征空间中组合 features，训练分类器检测 AI 生成文本；无需 target model 的 token probabilities，跨域 F1 达 99.0 | 架构上与我们的 TF-IDF + LogReg 检测器最接近——都用 lightweight features + 训练分类器，不依赖 target model access；区别在于我们需要 calibrated q-score 而非 binary detection |\n\n## 3. Sample Reweighting in Training\n\n| # | 论文 | 年份 | 场所 | 一句话 Contribution | 与我们的关系 |\n|---|------|------|------|-------------------|------------|\n| 1 | **Machine-Generated Text Detection Prevents Language Model Collapse** (Drayson, Yilmaz, Lampos) | 2025 | EMNLP | 首次提出 detect-and-reweight 框架缓解 model collapse：用 binary detector 检测 synthetic text，通过 importance resampling 降权 synthetic samples，在 GPT-2 / SmolLM2（4 LLM, 2 families, 6 decoding strategies）上验证有效性 | 我们最直接的前驱工作——他们开创了 detect-and-reweight 范式，但权重指数 b 是需要 grid search 的 heuristic hyperparameter，且仅评估 single-generator 场景（WikiText-2）；我们提供理论启发的 adaptive b* 替代 grid search，并扩展到 multi-generator web-scale 场景 |\n| 2 | **Improving the Accuracy of Likelihood-based Inference under Covariate Shift** (Shimodaira) | 2000 | JASA | 奠基性工作：提出 importance weighted ERM（IWERM），通过 density ratio 修正 covariate shift 下的 loss | 理论基础直接相关——我们的 weight = 1 - q^b 可以看作一种 bounded importance weight，Shimodaira 的 IWERM 理论为我们的方法提供了正当性 |\n| 3 | **Learning to Reweight Examples for Robust Deep Learning** (Ren, Zeng, Yang, Urtasun) | 2018 | ICML | 用 meta-learning 在训练中动态学习 sample weights（基于 gradient direction 在 clean validation set 上的表现） | L2RW 需要 clean validation set 做 meta-optimization，我们的方法不需要——weight 由 provenance detector 预先确定，无需在训练中迭代调整 |\n| 4 | **Meta-Weight-Net: Learning an Explicit Mapping For Sample Weighting** (Shu et al.) | 2019 | NeurIPS | 用 MLP 学习 loss → weight 的显式映射函数，在 noisy label 和 class imbalance 场景下优于手工设计的 weighting | 与 L2RW 类似用 meta-learning；我们的 weight function 是 analytic form（1 - q^b），不需要 meta-learning，更透明可解释 |\n| 5 | **Curriculum Learning** (Bengio, Louradour, Collobert, Weston) | 2009 | ICML | 奠基性工作：证明按从易到难的顺序训练（curriculum）可以加速收敛并改善 non-convex optimization 的局部极小值 | Curriculum learning 按难度排序，我们按 provenance 加权——虽然形式不同（排序 vs 加权），但都是 non-uniform training 的思想 |\n| 6 | **Dynamic Loss-Based Sample Reweighting for Improved LLM Pretraining** (Wang et al.) | 2025 | ICLR | 在 LLM pretraining 中做 instance-level dynamic reweighting（基于 loss 值在线调整权重），提出 LinUpper / Quadratic 等策略 | 最直接的对比工作之一——他们基于 loss 做 weighting，我们基于 provenance 做 weighting。两者可组合：先用 provenance weight 再用 loss-based dynamic adjustment |\n| 7 | **DoReMi** (Xie et al., 2023, 见第 1 节) | 2023 | NeurIPS | Domain-level reweighting via Group DRO | 我们做 instance-level provenance weighting，DoReMi 做 domain-level mixture optimization——粒度和信号来源不同 |\n\n## 4. Theoretical Analysis of Data Mixing / Contamination\n\n| # | 论文 | 年份 | 场所 | 一句话 Contribution | 与我们的关系 |\n|---|------|------|------|-------------------|------------|\n| 1 | **AI Models Collapse When Trained on Recursively Generated Data** (Shumailov, Shumaylov, Zhao, Papernot, Anderson, Gal) | 2024 | Nature | 提出 model collapse 概念：在 synthetic data 上迭代训练导致分布尾部丢失和性能退化，在 VAE / GMM / LLM 上验证 | 我们工作的核心 motivation——Shumailov 证明了 synthetic contamination 的危害，我们提出用 provenance weighting 来缓解而非完全过滤 |\n| 2 | **Strong Model Collapse** (Dohmatob, Feng, Subramonian, Kempe) | 2025 | ICLR | 证明即使极小比例的 synthetic data（1/1000）也会导致 model collapse；用 operator-valued free probability theory 给出 bias-variance 分解 | 强化了 motivation——即使少量 synthetic data 也有害，说明我们的 provenance weighting 方法的必要性：不能靠 \"少量就没事\" 来忽视 |\n| 3 | **Is Model Collapse Inevitable? Breaking the Curse of Recursion by Accumulating Real and Synthetic Data** (Gerstgrasser, Schaeffer et al.) | 2024 | COLM | 证明如果 accumulate（而非 replace）数据，model collapse 可以避免；在 linear model 下证明 test error 有有限上界 | 与我们的方法互补——他们说 \"保留 real data 可以救\"，我们说 \"对 synthetic data 降权也可以救\"，都是 mitigate 而非 discard 的思路 |\n| 4 | **How Bad is Training on Synthetic Data? A Statistical Analysis of Language Model Collapse** (Seddik, Chen, Hayou, Youssef, Debbah) | 2024 | COLM | 给出 recursive training 的统计模型，证明纯 synthetic 训练不可避免 collapse，但 real + synthetic 混合训练在 synthetic 比例低于阈值时可避免 | 直接相关——他们给出了 synthetic data 比例的阈值分析，我们的 α_eff 理论可以看作这类阈值分析的推广（从 hard threshold 到 soft weighting） |\n| 5 | **Can Generative Artificial Intelligence Survive Data Contamination? Theoretical Guarantees under Contaminated Recursive Training** (Wang, Niu, Li) | 2026 | arXiv 2602.16065 | 为 contaminated recursive training 提供收敛保证：bound d(ℙ̂_t, ℙ_0) ≲ t^{−min{p,α}}，推广至 non-Gaussian 设置；Assumption A2 限制 d 为凸度量，显式排除 cross-entropy/KL | 该论文的收敛 bound 直接启发了我们的 α_eff 定义和 b* 推导——α_eff(b) 将其理论中的 α 从 known parameter 变为 detector-estimated quantity，是我们方法的理论 motivation（非 contribution） |\n| 6 | **Data Mixing Laws: Optimizing Data Mixtures by Predicting Language Modeling Performance** (Ye, Liu, Sun, Zhan, Zhou, Qiu) | 2025 | ICLR | 发现 domain mixture proportion 和 model performance 之间存在可预测的函数关系（data mixing laws），可以用小规模实验预测大模型表现 | Data mixing laws 可用于预测不同 provenance weight 设置下的 model performance——我们的 Grid-b 搜索可以理论上用 mixing laws 来加速 |\n| 7 | **Scaling Data-Constrained Language Models** (Muennighoff et al., 2023, 见第 1 节) | 2023 | NeurIPS | 数据受限下的 scaling law，重复 ≤4 epochs 影响可忽略 | 提供了数据受限场景的理论框架，我们的 α_eff 分析在此基础上进一步考虑了 contamination 的影响 |\n\n## Key Observations\n\n### 与现有工作的主要区别\n\n1. **Data selection vs. data weighting**: 多数现有方法（DSIR, FineWeb-Edu, D4）做 hard selection（保留或丢弃），我们做 soft weighting（降权但不丢弃），保留了更多数据多样性和信息。\n2. **Quality-based vs. provenance-based**: QuRating / FineWeb-Edu 基于 \"质量\" 评分，我们基于 \"来源\"（是否 synthetic）评分——这是正交的信号维度，可以组合使用。\n3. **Detection for filtering vs. detection for weighting**: 现有 synthetic text detection 工作（DetectGPT, Binoculars）几乎全部用于 binary filtering 或人工审核，我们首次将 calibrated detection score 用于 continuous training weight，对检测器的 calibration（ECE）提出了新要求。\n4. **Analytic weight function vs. learned weights**: 与 meta-learning reweighting（L2RW, Meta-Weight-Net）相比，我们的 weight = 1 - q^b 是 closed-form，无需 clean validation set 或 meta-optimization，更高效透明。\n\n### 最直接的竞争对手 / 对比工作\n\n- **Dynamic Loss-Based Sample Reweighting (Wang et al., ICLR 2025)**: 同为 instance-level reweighting for LLM pretraining，但信号来源不同（loss vs. provenance）。\n- **DoReMi (Xie et al., NeurIPS 2023)**: Domain-level reweighting，粒度不同但目标相似。\n- **FineWeb-Edu filtering**: 最接近的 \"data quality\" 竞品，但是 hard filtering 不是 soft weighting。\n\n### 潜在的引用遗漏风险\n\n- **Ghostbuster** (Verma et al., 2024): 另一个 feature-based synthetic text detector，可能需要作为 detection baseline 引用 [需确认场所]\n- **GPTZero**: 商业工具，学术论文 (2025 arXiv) 可作为检测方法的 context 引用 [需确认]\n- **Self-play fine-tuning / synthetic data augmentation 文献**: 我们的工作假设 synthetic data 有害，但有大量文献证明 synthetic data 在 fine-tuning 中有益——需要在 related work 中 acknowledge 并区分 pretraining contamination vs. fine-tuning augmentation 的不同场景\n- **Distributionally robust optimization (DRO) 基础文献**: Sagawa et al. (2020) Group DRO 等，作为 DoReMi 的理论基础可能需要提及\n- **Data influence / data attribution 文献**: TracIn, influence functions 等，虽然不是直接竞品但在 \"understanding data's effect on training\" 的大框架下相关\n",
    "structuredPatch": [
      {
        "oldStart": 63,
        "oldLines": 10,
        "newStart": 63,
        "newLines": 12,
        "lines": [
          " - **DoReMi (Xie et al., NeurIPS 2023)**: Domain-level reweighting，粒度不同但目标相似。",
          " - **FineWeb-Edu filtering**: 最接近的 \"data quality\" 竞品，但是 hard filtering 不是 soft weighting。",
          " ",
          "-### 潜在的引用遗漏风险",
          "+### 引用决策记录",
          " ",
          "-- **Ghostbuster** (Verma et al., 2024): 另一个 feature-based synthetic text detector，可能需要作为 detection baseline 引用 [需确认场所]",
          "-- **GPTZero**: 商业工具，学术论文 (2025 arXiv) 可作为检测方法的 context 引用 [需确认]",
          "-- **Self-play fine-tuning / synthetic data augmentation 文献**: 我们的工作假设 synthetic data 有害，但有大量文献证明 synthetic data 在 fine-tuning 中有益——需要在 related work 中 acknowledge 并区分 pretraining contamination vs. fine-tuning augmentation 的不同场景",
          "-- **Distributionally robust optimization (DRO) 基础文献**: Sagawa et al. (2020) Group DRO 等，作为 DoReMi 的理论基础可能需要提及",
          "-- **Data influence / data attribution 文献**: TracIn, influence functions 等，虽然不是直接竞品但在 \"understanding data's effect on training\" 的大框架下相关",
          "+| # | 候选论文 | 决策 | 理由 |",
          "+|---|---------|------|------|",
          "+| 1 | **Ghostbuster** (Verma, Fleisig, Tomlin, Klein, NAACL 2024) | ✅ 收录 → Section 2 #7 | Feature-based detector，架构与我们的 TF-IDF + LogReg 最接近（lightweight features + classifier, 无需 target model access），审稿人可能质疑遗漏 |",
          "+| 2 | **GPTZero** | ❌ 不收录 | 商业工具，无同行评审的方法学论文。现有学术文献均为第三方评估（准确率测试），非方法贡献。学术 related work 中引用商业产品无先例价值 |",
          "+| 3 | **Self-play fine-tuning / synthetic data augmentation** (代表性工作：SPIN, Chen et al., ICML 2024; Self-Instruct, Wang et al., ACL 2023) | ❌ 不收录为单独条目 | 我们关注的是 pretraining 阶段不可控的 synthetic contamination（来源未知、比例未知），与 fine-tuning 阶段有意使用 synthetic data augmentation 是不同场景。建议在 Related Work 正文中用一句话 acknowledge 此区别（\"We focus on uncontrolled synthetic contamination in pretraining, distinct from intentional synthetic augmentation in fine-tuning (Chen et al., 2024)\"），但无需展开讨论 |",
          "+| 4 | **Group DRO** (Sagawa, Koh, Hashimoto, Liang, ICLR 2020) | ❌ 不收录 | DoReMi 引用已覆盖 Group DRO 理论基础。我们是 instance-level provenance weighting，与 Group DRO 的 group-level worst-case optimization 无直接可比性。审稿人不太可能因缺 Group DRO 引用而提问 |",
          "+| 5 | **Data influence / data attribution** (TracIn, Pruthi et al., NeurIPS 2020; Influence Functions, Koh & Liang, ICML 2017) | ❌ 不收录 | 我们不做 post-hoc influence estimation，而是基于 provenance 做 pre-hoc weighting。目标不同（归因 vs 降权）、方法不同（梯度追踪 vs 检测器评分）、场景不同（诊断 vs 训练干预）。引了反而分散 detect-and-reweight 的主线叙事 |"
        ]
      }
    ],
    "userModified": false,
    "replaceAll": false
  }
}
```

</details>

---

### Assistant

_source line 74_

Now let me also update the "最直接的竞争对手" section to include Drayson.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "0a05528b-d05d-4fb3-947f-20e0adce1e25",
  "uuid": "b6c1c2f2-6cd6-4038-b8af-123a41398484",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SxgCfefGe4kDa33NC8Ah3Y",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1370,
      "cache_read_input_tokens": 60517,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1370
      },
      "output_tokens": 1,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool call

_source line 75_

<details open><summary>🔧 Tool call — Edit · `toolu_0145JrAysy87t8jwcHZkqv8H`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/related_work_notes.md",
  "old_string": "### 最直接的竞争对手 / 对比工作\n\n- **Dynamic Loss-Based Sample Reweighting (Wang et al., ICLR 2025)**: 同为 instance-level reweighting for LLM pretraining，但信号来源不同（loss vs. provenance）。\n- **DoReMi (Xie et al., NeurIPS 2023)**: Domain-level reweighting，粒度不同但目标相似。\n- **FineWeb-Edu filtering**: 最接近的 \"data quality\" 竞品，但是 hard filtering 不是 soft weighting。",
  "new_string": "### 最直接的竞争对手 / 对比工作\n\n- **Drayson et al. (EMNLP 2025)**: 最直接的前驱——同为 detect-and-reweight，但 b 是 heuristic，我们提供 adaptive b*。\n- **Dynamic Loss-Based Sample Reweighting (Wang et al., ICLR 2025)**: 同为 instance-level reweighting for LLM pretraining，但信号来源不同（loss vs. provenance）。\n- **DoReMi (Xie et al., NeurIPS 2023)**: Domain-level reweighting，粒度不同但目标相似。\n- **FineWeb-Edu filtering**: 最接近的 \"data quality\" 竞品，但是 hard filtering 不是 soft weighting。"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "0a05528b-d05d-4fb3-947f-20e0adce1e25",
  "uuid": "d1c951e6-a737-459b-ab23-235ea5860bb4",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SxgCfefGe4kDa33NC8Ah3Y",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1370,
      "cache_read_input_tokens": 60517,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1370
      },
      "output_tokens": 1,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool result

_source line 76 · 2026-05-14T12:37:16.158Z_

<details><summary>↩ Tool result · `toolu_0145JrAysy87t8jwcHZkqv8H`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/related_work_notes.md has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "0a05528b-d05d-4fb3-947f-20e0adce1e25",
  "uuid": "4afe2e03-0372-466f-a404-e6f1735151ba",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/related_work_notes.md",
    "oldString": "### 最直接的竞争对手 / 对比工作\n\n- **Dynamic Loss-Based Sample Reweighting (Wang et al., ICLR 2025)**: 同为 instance-level reweighting for LLM pretraining，但信号来源不同（loss vs. provenance）。\n- **DoReMi (Xie et al., NeurIPS 2023)**: Domain-level reweighting，粒度不同但目标相似。\n- **FineWeb-Edu filtering**: 最接近的 \"data quality\" 竞品，但是 hard filtering 不是 soft weighting。",
    "newString": "### 最直接的竞争对手 / 对比工作\n\n- **Drayson et al. (EMNLP 2025)**: 最直接的前驱——同为 detect-and-reweight，但 b 是 heuristic，我们提供 adaptive b*。\n- **Dynamic Loss-Based Sample Reweighting (Wang et al., ICLR 2025)**: 同为 instance-level reweighting for LLM pretraining，但信号来源不同（loss vs. provenance）。\n- **DoReMi (Xie et al., NeurIPS 2023)**: Domain-level reweighting，粒度不同但目标相似。\n- **FineWeb-Edu filtering**: 最接近的 \"data quality\" 竞品，但是 hard filtering 不是 soft weighting。",
    "originalFile": "# Related Work Survey — Provenance Weight Training\n\n## 1. Data Quality / Data Selection for LLM Pretraining\n\n| # | 论文 | 年份 | 场所 | 一句话 Contribution | 与我们的关系 |\n|---|------|------|------|-------------------|------------|\n| 1 | **DSIR: Data Selection for Language Models via Importance Resampling** (Xie, Santurkar, Ma, Liang) | 2023 | NeurIPS | 用 hashed n-gram 特征估计 importance weight，对大规模语料做 importance resampling 来匹配目标分布 | DSIR 按目标分布做 selection，我们按 provenance 做 weighting——都用 lightweight feature 做数据筛选，但动机不同：DSIR 优化 domain match，我们降低 synthetic contamination |\n| 2 | **QuRating: Selecting High-Quality Data for Training Language Models** (Wettig, Gupta, Malik, Chen) | 2024 | ICML | 用 LLM pairwise judgment 对数据做 4 维质量评分（writing style / expertise / facts / educational value），训练 QuRater 模型标注 260B 语料 | QuRating 用 LLM 判断 \"质量\"，我们用检测器判断 \"来源\"——都是 model-based annotation + downstream reweighting，但 quality 和 provenance 是正交维度 |\n| 3 | **The FineWeb Datasets: Decanting the Web for the Finest Text Data at Scale** (Penedo et al., HuggingFace) | 2024 | arXiv | 用 Llama-3-70B 合成标注训练 educational quality classifier，过滤出 1.3T token 的 FineWeb-Edu，在 MMLU/ARC 上大幅领先 | FineWeb-Edu 用 LLM-based classifier 做 hard filtering（保留/丢弃），我们用 detector 做 soft weighting（降权不丢弃），保留更多数据多样性 |\n| 4 | **D4: Improving LLM Pretraining via Document De-Duplication and Diversification** (Tirumala, Simig et al.) | 2023 | NeurIPS D&B | 用 pretrained embedding + K-Means 做去重和多样性平衡，6.7B 模型上提升 2% 下游准确率和 20% 训练效率 | D4 关注重复和多样性，我们关注 synthetic contamination——互补方法，可以先 D4 去重再用我们的 provenance weighting |\n| 5 | **DoReMi: Optimizing Data Mixtures Speeds Up Language Model Pretraining** (Xie, Pham et al.) | 2023 | NeurIPS | 用 Group DRO 在 proxy model 上优化 domain mixture weights，无需下游任务信息，8B 模型提升 6.5% few-shot 准确率 | DoReMi 做 domain-level reweighting（按 domain 调权），我们做 instance-level reweighting（按 q-score 调权）——粒度不同，理论上可以组合使用 |\n| 6 | **DataComp-LM (DCLM): In Search of the Next Generation of Training Sets for Language Models** (Li et al.) | 2024 | NeurIPS D&B | 提供 240T token 标准化语料 + 评估套件，系统性对比 data curation 策略，证明 model-based filtering 是关键 | DCLM 是 benchmark 框架，我们的 provenance-based weighting 可以作为一种新的 curation strategy 在 DCLM 上评估 |\n| 7 | **Scaling Data-Constrained Language Models** (Muennighoff, Rush et al.) | 2023 | NeurIPS | 系统研究数据受限时的 scaling law，发现 ≤4 epochs 重复数据对 loss 影响可忽略，提出考虑重复衰减的 compute-optimal law | 当 unique data 不足时更可能混入 synthetic data 来补量——我们的方法提供了一种替代方案：不用丢弃 synthetic data，而是降权使用 |\n\n## 2. Synthetic Data Contamination Detection\n\n| # | 论文 | 年份 | 场所 | 一句话 Contribution | 与我们的关系 |\n|---|------|------|------|-------------------|------------|\n| 1 | **DetectGPT: Zero-Shot Machine-Generated Text Detection using Probability Curvature** (Mitchell et al.) | 2023 | ICML | 零样本检测：用 log probability curvature（在 perturbation 前后的 log-prob 变化）区分 human vs machine text，无需训练分类器 | DetectGPT 做 binary detection（是否机器生成），我们需要 calibrated probability（q-score）——我们选择 TF-IDF + LogReg 正是因为需要 well-calibrated 的连续 score 而非仅 binary 判断 |\n| 2 | **Fast-DetectGPT: Efficient Zero-Shot Detection via Conditional Probability Curvature** (Bao et al.) | 2024 | ICLR | 将 DetectGPT 的 perturbation 步骤替换为 sampling，加速 340 倍且 AUROC 提升约 75% | 同上——更高效但仍是 binary detection，calibration 质量（ECE）未被重点评估，而这正是我们工作的核心关注点 |\n| 3 | **Binoculars: Zero-Shot Detection of LLM-Generated Text** (Hans et al.) | 2024 | ICML | 用两个 LLM 的 perplexity / cross-perplexity 比值做检测，ChatGPT 文本在 0.01% FPR 下召回 >90% | Binoculars 需要两个 LLM 推理，计算成本高；我们的 TF-IDF + LogReg 检测器极轻量，适合标注数十亿 token 级别的 pretraining corpus |\n| 4 | **GLTR: Statistical Detection and Visualization of Generated Text** (Gehrmann, Strobelt, Rush) | 2019 | ACL | 用 LM 的 top-k token 排名做统计检测和可视化，帮助人类识别机器文本（人类检测率从 54% 提升到 72%） | 早期 statistical detection 工作，启发了后续基于 model statistics 的方法；我们的方法同样基于统计特征但目标不同（scoring for weighting 而非 human-in-the-loop detection） |\n| 5 | **A Watermark for Large Language Models** (Kirchenbauer et al.) | 2023 | ICML | 在生成时嵌入 statistical watermark（green/red token list），可用 p-value 统计检验来检测 | Watermarking 需要控制生成过程，无法检测已有的、未 watermarked 的 synthetic data——我们的场景是 post-hoc detection on existing corpus |\n| 6 | **A Survey on LLM-Generated Text Detection: Necessity, Methods, and Future Directions** (Wu et al.) | 2024 | Computational Linguistics (MIT Press) | 系统综述 statistical / neural / watermarking 三类检测方法，讨论 robustness 和 generalization | 综述文献，帮助定位我们的检测器在整个 detection 方法谱系中的位置——我们是 training-based statistical classifier，但用于 weighting 而非 filtering |\n| 7 | **Ghostbuster: Detecting Text Ghostwritten by Large Language Models** (Verma, Fleisig, Tomlin, Klein) | 2024 | NAACL | 用 structured search 在多个弱 LM 的特征空间中组合 features，训练分类器检测 AI 生成文本；无需 target model 的 token probabilities，跨域 F1 达 99.0 | 架构上与我们的 TF-IDF + LogReg 检测器最接近——都用 lightweight features + 训练分类器，不依赖 target model access；区别在于我们需要 calibrated q-score 而非 binary detection |\n\n## 3. Sample Reweighting in Training\n\n| # | 论文 | 年份 | 场所 | 一句话 Contribution | 与我们的关系 |\n|---|------|------|------|-------------------|------------|\n| 1 | **Machine-Generated Text Detection Prevents Language Model Collapse** (Drayson, Yilmaz, Lampos) | 2025 | EMNLP | 首次提出 detect-and-reweight 框架缓解 model collapse：用 binary detector 检测 synthetic text，通过 importance resampling 降权 synthetic samples，在 GPT-2 / SmolLM2（4 LLM, 2 families, 6 decoding strategies）上验证有效性 | 我们最直接的前驱工作——他们开创了 detect-and-reweight 范式，但权重指数 b 是需要 grid search 的 heuristic hyperparameter，且仅评估 single-generator 场景（WikiText-2）；我们提供理论启发的 adaptive b* 替代 grid search，并扩展到 multi-generator web-scale 场景 |\n| 2 | **Improving the Accuracy of Likelihood-based Inference under Covariate Shift** (Shimodaira) | 2000 | JASA | 奠基性工作：提出 importance weighted ERM（IWERM），通过 density ratio 修正 covariate shift 下的 loss | 理论基础直接相关——我们的 weight = 1 - q^b 可以看作一种 bounded importance weight，Shimodaira 的 IWERM 理论为我们的方法提供了正当性 |\n| 3 | **Learning to Reweight Examples for Robust Deep Learning** (Ren, Zeng, Yang, Urtasun) | 2018 | ICML | 用 meta-learning 在训练中动态学习 sample weights（基于 gradient direction 在 clean validation set 上的表现） | L2RW 需要 clean validation set 做 meta-optimization，我们的方法不需要——weight 由 provenance detector 预先确定，无需在训练中迭代调整 |\n| 4 | **Meta-Weight-Net: Learning an Explicit Mapping For Sample Weighting** (Shu et al.) | 2019 | NeurIPS | 用 MLP 学习 loss → weight 的显式映射函数，在 noisy label 和 class imbalance 场景下优于手工设计的 weighting | 与 L2RW 类似用 meta-learning；我们的 weight function 是 analytic form（1 - q^b），不需要 meta-learning，更透明可解释 |\n| 5 | **Curriculum Learning** (Bengio, Louradour, Collobert, Weston) | 2009 | ICML | 奠基性工作：证明按从易到难的顺序训练（curriculum）可以加速收敛并改善 non-convex optimization 的局部极小值 | Curriculum learning 按难度排序，我们按 provenance 加权——虽然形式不同（排序 vs 加权），但都是 non-uniform training 的思想 |\n| 6 | **Dynamic Loss-Based Sample Reweighting for Improved LLM Pretraining** (Wang et al.) | 2025 | ICLR | 在 LLM pretraining 中做 instance-level dynamic reweighting（基于 loss 值在线调整权重），提出 LinUpper / Quadratic 等策略 | 最直接的对比工作之一——他们基于 loss 做 weighting，我们基于 provenance 做 weighting。两者可组合：先用 provenance weight 再用 loss-based dynamic adjustment |\n| 7 | **DoReMi** (Xie et al., 2023, 见第 1 节) | 2023 | NeurIPS | Domain-level reweighting via Group DRO | 我们做 instance-level provenance weighting，DoReMi 做 domain-level mixture optimization——粒度和信号来源不同 |\n\n## 4. Theoretical Analysis of Data Mixing / Contamination\n\n| # | 论文 | 年份 | 场所 | 一句话 Contribution | 与我们的关系 |\n|---|------|------|------|-------------------|------------|\n| 1 | **AI Models Collapse When Trained on Recursively Generated Data** (Shumailov, Shumaylov, Zhao, Papernot, Anderson, Gal) | 2024 | Nature | 提出 model collapse 概念：在 synthetic data 上迭代训练导致分布尾部丢失和性能退化，在 VAE / GMM / LLM 上验证 | 我们工作的核心 motivation——Shumailov 证明了 synthetic contamination 的危害，我们提出用 provenance weighting 来缓解而非完全过滤 |\n| 2 | **Strong Model Collapse** (Dohmatob, Feng, Subramonian, Kempe) | 2025 | ICLR | 证明即使极小比例的 synthetic data（1/1000）也会导致 model collapse；用 operator-valued free probability theory 给出 bias-variance 分解 | 强化了 motivation——即使少量 synthetic data 也有害，说明我们的 provenance weighting 方法的必要性：不能靠 \"少量就没事\" 来忽视 |\n| 3 | **Is Model Collapse Inevitable? Breaking the Curse of Recursion by Accumulating Real and Synthetic Data** (Gerstgrasser, Schaeffer et al.) | 2024 | COLM | 证明如果 accumulate（而非 replace）数据，model collapse 可以避免；在 linear model 下证明 test error 有有限上界 | 与我们的方法互补——他们说 \"保留 real data 可以救\"，我们说 \"对 synthetic data 降权也可以救\"，都是 mitigate 而非 discard 的思路 |\n| 4 | **How Bad is Training on Synthetic Data? A Statistical Analysis of Language Model Collapse** (Seddik, Chen, Hayou, Youssef, Debbah) | 2024 | COLM | 给出 recursive training 的统计模型，证明纯 synthetic 训练不可避免 collapse，但 real + synthetic 混合训练在 synthetic 比例低于阈值时可避免 | 直接相关——他们给出了 synthetic data 比例的阈值分析，我们的 α_eff 理论可以看作这类阈值分析的推广（从 hard threshold 到 soft weighting） |\n| 5 | **Can Generative Artificial Intelligence Survive Data Contamination? Theoretical Guarantees under Contaminated Recursive Training** (Wang, Niu, Li) | 2026 | arXiv 2602.16065 | 为 contaminated recursive training 提供收敛保证：bound d(ℙ̂_t, ℙ_0) ≲ t^{−min{p,α}}，推广至 non-Gaussian 设置；Assumption A2 限制 d 为凸度量，显式排除 cross-entropy/KL | 该论文的收敛 bound 直接启发了我们的 α_eff 定义和 b* 推导——α_eff(b) 将其理论中的 α 从 known parameter 变为 detector-estimated quantity，是我们方法的理论 motivation（非 contribution） |\n| 6 | **Data Mixing Laws: Optimizing Data Mixtures by Predicting Language Modeling Performance** (Ye, Liu, Sun, Zhan, Zhou, Qiu) | 2025 | ICLR | 发现 domain mixture proportion 和 model performance 之间存在可预测的函数关系（data mixing laws），可以用小规模实验预测大模型表现 | Data mixing laws 可用于预测不同 provenance weight 设置下的 model performance——我们的 Grid-b 搜索可以理论上用 mixing laws 来加速 |\n| 7 | **Scaling Data-Constrained Language Models** (Muennighoff et al., 2023, 见第 1 节) | 2023 | NeurIPS | 数据受限下的 scaling law，重复 ≤4 epochs 影响可忽略 | 提供了数据受限场景的理论框架，我们的 α_eff 分析在此基础上进一步考虑了 contamination 的影响 |\n\n## Key Observations\n\n### 与现有工作的主要区别\n\n1. **Data selection vs. data weighting**: 多数现有方法（DSIR, FineWeb-Edu, D4）做 hard selection（保留或丢弃），我们做 soft weighting（降权但不丢弃），保留了更多数据多样性和信息。\n2. **Quality-based vs. provenance-based**: QuRating / FineWeb-Edu 基于 \"质量\" 评分，我们基于 \"来源\"（是否 synthetic）评分——这是正交的信号维度，可以组合使用。\n3. **Detection for filtering vs. detection for weighting**: 现有 synthetic text detection 工作（DetectGPT, Binoculars）几乎全部用于 binary filtering 或人工审核，我们首次将 calibrated detection score 用于 continuous training weight，对检测器的 calibration（ECE）提出了新要求。\n4. **Analytic weight function vs. learned weights**: 与 meta-learning reweighting（L2RW, Meta-Weight-Net）相比，我们的 weight = 1 - q^b 是 closed-form，无需 clean validation set 或 meta-optimization，更高效透明。\n\n### 最直接的竞争对手 / 对比工作\n\n- **Dynamic Loss-Based Sample Reweighting (Wang et al., ICLR 2025)**: 同为 instance-level reweighting for LLM pretraining，但信号来源不同（loss vs. provenance）。\n- **DoReMi (Xie et al., NeurIPS 2023)**: Domain-level reweighting，粒度不同但目标相似。\n- **FineWeb-Edu filtering**: 最接近的 \"data quality\" 竞品，但是 hard filtering 不是 soft weighting。\n\n### 引用决策记录\n\n| # | 候选论文 | 决策 | 理由 |\n|---|---------|------|------|\n| 1 | **Ghostbuster** (Verma, Fleisig, Tomlin, Klein, NAACL 2024) | ✅ 收录 → Section 2 #7 | Feature-based detector，架构与我们的 TF-IDF + LogReg 最接近（lightweight features + classifier, 无需 target model access），审稿人可能质疑遗漏 |\n| 2 | **GPTZero** | ❌ 不收录 | 商业工具，无同行评审的方法学论文。现有学术文献均为第三方评估（准确率测试），非方法贡献。学术 related work 中引用商业产品无先例价值 |\n| 3 | **Self-play fine-tuning / synthetic data augmentation** (代表性工作：SPIN, Chen et al., ICML 2024; Self-Instruct, Wang et al., ACL 2023) | ❌ 不收录为单独条目 | 我们关注的是 pretraining 阶段不可控的 synthetic contamination（来源未知、比例未知），与 fine-tuning 阶段有意使用 synthetic data augmentation 是不同场景。建议在 Related Work 正文中用一句话 acknowledge 此区别（\"We focus on uncontrolled synthetic contamination in pretraining, distinct from intentional synthetic augmentation in fine-tuning (Chen et al., 2024)\"），但无需展开讨论 |\n| 4 | **Group DRO** (Sagawa, Koh, Hashimoto, Liang, ICLR 2020) | ❌ 不收录 | DoReMi 引用已覆盖 Group DRO 理论基础。我们是 instance-level provenance weighting，与 Group DRO 的 group-level worst-case optimization 无直接可比性。审稿人不太可能因缺 Group DRO 引用而提问 |\n| 5 | **Data influence / data attribution** (TracIn, Pruthi et al., NeurIPS 2020; Influence Functions, Koh & Liang, ICML 2017) | ❌ 不收录 | 我们不做 post-hoc influence estimation，而是基于 provenance 做 pre-hoc weighting。目标不同（归因 vs 降权）、方法不同（梯度追踪 vs 检测器评分）、场景不同（诊断 vs 训练干预）。引了反而分散 detect-and-reweight 的主线叙事 |\n",
    "structuredPatch": [
      {
        "oldStart": 59,
        "oldLines": 6,
        "newStart": 59,
        "newLines": 7,
        "lines": [
          " ",
          " ### 最直接的竞争对手 / 对比工作",
          " ",
          "+- **Drayson et al. (EMNLP 2025)**: 最直接的前驱——同为 detect-and-reweight，但 b 是 heuristic，我们提供 adaptive b*。",
          " - **Dynamic Loss-Based Sample Reweighting (Wang et al., ICLR 2025)**: 同为 instance-level reweighting for LLM pretraining，但信号来源不同（loss vs. provenance）。",
          " - **DoReMi (Xie et al., NeurIPS 2023)**: Domain-level reweighting，粒度不同但目标相似。",
          " - **FineWeb-Edu filtering**: 最接近的 \"data quality\" 竞品，但是 hard filtering 不是 soft weighting。"
        ]
      }
    ],
    "userModified": false,
    "replaceAll": false
  }
}
```

</details>

---

### Assistant

_source line 77_

Let me verify the final file.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "0a05528b-d05d-4fb3-947f-20e0adce1e25",
  "uuid": "fed358f4-53e7-4054-81b7-38a1b157527d",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BSKXx7gD2uPdrg4HnLvJr6",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 600,
      "cache_read_input_tokens": 61887,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 600
      },
      "output_tokens": 1,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool call

_source line 78_

<details open><summary>🔧 Tool call — Read · `toolu_01NCLGECY2RRMVUZjmtJx7Wi`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/related_work_notes.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "0a05528b-d05d-4fb3-947f-20e0adce1e25",
  "uuid": "622e9011-ff80-4b29-b143-99ab6ea232c6",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BSKXx7gD2uPdrg4HnLvJr6",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 600,
      "cache_read_input_tokens": 61887,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 600
      },
      "output_tokens": 1,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool result

_source line 79 · 2026-05-14T12:37:19.902Z_

<details><summary>↩ Tool result · `toolu_01NCLGECY2RRMVUZjmtJx7Wi`</summary>

```text
1	# Related Work Survey — Provenance Weight Training
2	
3	## 1. Data Quality / Data Selection for LLM Pretraining
4	
5	| # | 论文 | 年份 | 场所 | 一句话 Contribution | 与我们的关系 |
6	|---|------|------|------|-------------------|------------|
7	| 1 | **DSIR: Data Selection for Language Models via Importance Resampling** (Xie, Santurkar, Ma, Liang) | 2023 | NeurIPS | 用 hashed n-gram 特征估计 importance weight，对大规模语料做 importance resampling 来匹配目标分布 | DSIR 按目标分布做 selection，我们按 provenance 做 weighting——都用 lightweight feature 做数据筛选，但动机不同：DSIR 优化 domain match，我们降低 synthetic contamination |
8	| 2 | **QuRating: Selecting High-Quality Data for Training Language Models** (Wettig, Gupta, Malik, Chen) | 2024 | ICML | 用 LLM pairwise judgment 对数据做 4 维质量评分（writing style / expertise / facts / educational value），训练 QuRater 模型标注 260B 语料 | QuRating 用 LLM 判断 "质量"，我们用检测器判断 "来源"——都是 model-based annotation + downstream reweighting，但 quality 和 provenance 是正交维度 |
9	| 3 | **The FineWeb Datasets: Decanting the Web for the Finest Text Data at Scale** (Penedo et al., HuggingFace) | 2024 | arXiv | 用 Llama-3-70B 合成标注训练 educational quality classifier，过滤出 1.3T token 的 FineWeb-Edu，在 MMLU/ARC 上大幅领先 | FineWeb-Edu 用 LLM-based classifier 做 hard filtering（保留/丢弃），我们用 detector 做 soft weighting（降权不丢弃），保留更多数据多样性 |
10	| 4 | **D4: Improving LLM Pretraining via Document De-Duplication and Diversification** (Tirumala, Simig et al.) | 2023 | NeurIPS D&B | 用 pretrained embedding + K-Means 做去重和多样性平衡，6.7B 模型上提升 2% 下游准确率和 20% 训练效率 | D4 关注重复和多样性，我们关注 synthetic contamination——互补方法，可以先 D4 去重再用我们的 provenance weighting |
11	| 5 | **DoReMi: Optimizing Data Mixtures Speeds Up Language Model Pretraining** (Xie, Pham et al.) | 2023 | NeurIPS | 用 Group DRO 在 proxy model 上优化 domain mixture weights，无需下游任务信息，8B 模型提升 6.5% few-shot 准确率 | DoReMi 做 domain-level reweighting（按 domain 调权），我们做 instance-level reweighting（按 q-score 调权）——粒度不同，理论上可以组合使用 |
12	| 6 | **DataComp-LM (DCLM): In Search of the Next Generation of Training Sets for Language Models** (Li et al.) | 2024 | NeurIPS D&B | 提供 240T token 标准化语料 + 评估套件，系统性对比 data curation 策略，证明 model-based filtering 是关键 | DCLM 是 benchmark 框架，我们的 provenance-based weighting 可以作为一种新的 curation strategy 在 DCLM 上评估 |
13	| 7 | **Scaling Data-Constrained Language Models** (Muennighoff, Rush et al.) | 2023 | NeurIPS | 系统研究数据受限时的 scaling law，发现 ≤4 epochs 重复数据对 loss 影响可忽略，提出考虑重复衰减的 compute-optimal law | 当 unique data 不足时更可能混入 synthetic data 来补量——我们的方法提供了一种替代方案：不用丢弃 synthetic data，而是降权使用 |
14	
15	## 2. Synthetic Data Contamination Detection
16	
17	| # | 论文 | 年份 | 场所 | 一句话 Contribution | 与我们的关系 |
18	|---|------|------|------|-------------------|------------|
19	| 1 | **DetectGPT: Zero-Shot Machine-Generated Text Detection using Probability Curvature** (Mitchell et al.) | 2023 | ICML | 零样本检测：用 log probability curvature（在 perturbation 前后的 log-prob 变化）区分 human vs machine text，无需训练分类器 | DetectGPT 做 binary detection（是否机器生成），我们需要 calibrated probability（q-score）——我们选择 TF-IDF + LogReg 正是因为需要 well-calibrated 的连续 score 而非仅 binary 判断 |
20	| 2 | **Fast-DetectGPT: Efficient Zero-Shot Detection via Conditional Probability Curvature** (Bao et al.) | 2024 | ICLR | 将 DetectGPT 的 perturbation 步骤替换为 sampling，加速 340 倍且 AUROC 提升约 75% | 同上——更高效但仍是 binary detection，calibration 质量（ECE）未被重点评估，而这正是我们工作的核心关注点 |
21	| 3 | **Binoculars: Zero-Shot Detection of LLM-Generated Text** (Hans et al.) | 2024 | ICML | 用两个 LLM 的 perplexity / cross-perplexity 比值做检测，ChatGPT 文本在 0.01% FPR 下召回 >90% | Binoculars 需要两个 LLM 推理，计算成本高；我们的 TF-IDF + LogReg 检测器极轻量，适合标注数十亿 token 级别的 pretraining corpus |
22	| 4 | **GLTR: Statistical Detection and Visualization of Generated Text** (Gehrmann, Strobelt, Rush) | 2019 | ACL | 用 LM 的 top-k token 排名做统计检测和可视化，帮助人类识别机器文本（人类检测率从 54% 提升到 72%） | 早期 statistical detection 工作，启发了后续基于 model statistics 的方法；我们的方法同样基于统计特征但目标不同（scoring for weighting 而非 human-in-the-loop detection） |
23	| 5 | **A Watermark for Large Language Models** (Kirchenbauer et al.) | 2023 | ICML | 在生成时嵌入 statistical watermark（green/red token list），可用 p-value 统计检验来检测 | Watermarking 需要控制生成过程，无法检测已有的、未 watermarked 的 synthetic data——我们的场景是 post-hoc detection on existing corpus |
24	| 6 | **A Survey on LLM-Generated Text Detection: Necessity, Methods, and Future Directions** (Wu et al.) | 2024 | Computational Linguistics (MIT Press) | 系统综述 statistical / neural / watermarking 三类检测方法，讨论 robustness 和 generalization | 综述文献，帮助定位我们的检测器在整个 detection 方法谱系中的位置——我们是 training-based statistical classifier，但用于 weighting 而非 filtering |
25	| 7 | **Ghostbuster: Detecting Text Ghostwritten by Large Language Models** (Verma, Fleisig, Tomlin, Klein) | 2024 | NAACL | 用 structured search 在多个弱 LM 的特征空间中组合 features，训练分类器检测 AI 生成文本；无需 target model 的 token probabilities，跨域 F1 达 99.0 | 架构上与我们的 TF-IDF + LogReg 检测器最接近——都用 lightweight features + 训练分类器，不依赖 target model access；区别在于我们需要 calibrated q-score 而非 binary detection |
26	
27	## 3. Sample Reweighting in Training
28	
29	| # | 论文 | 年份 | 场所 | 一句话 Contribution | 与我们的关系 |
30	|---|------|------|------|-------------------|------------|
31	| 1 | **Machine-Generated Text Detection Prevents Language Model Collapse** (Drayson, Yilmaz, Lampos) | 2025 | EMNLP | 首次提出 detect-and-reweight 框架缓解 model collapse：用 binary detector 检测 synthetic text，通过 importance resampling 降权 synthetic samples，在 GPT-2 / SmolLM2（4 LLM, 2 families, 6 decoding strategies）上验证有效性 | 我们最直接的前驱工作——他们开创了 detect-and-reweight 范式，但权重指数 b 是需要 grid search 的 heuristic hyperparameter，且仅评估 single-generator 场景（WikiText-2）；我们提供理论启发的 adaptive b* 替代 grid search，并扩展到 multi-generator web-scale 场景 |
32	| 2 | **Improving the Accuracy of Likelihood-based Inference under Covariate Shift** (Shimodaira) | 2000 | JASA | 奠基性工作：提出 importance weighted ERM（IWERM），通过 density ratio 修正 covariate shift 下的 loss | 理论基础直接相关——我们的 weight = 1 - q^b 可以看作一种 bounded importance weight，Shimodaira 的 IWERM 理论为我们的方法提供了正当性 |
33	| 3 | **Learning to Reweight Examples for Robust Deep Learning** (Ren, Zeng, Yang, Urtasun) | 2018 | ICML | 用 meta-learning 在训练中动态学习 sample weights（基于 gradient direction 在 clean validation set 上的表现） | L2RW 需要 clean validation set 做 meta-optimization，我们的方法不需要——weight 由 provenance detector 预先确定，无需在训练中迭代调整 |
34	| 4 | **Meta-Weight-Net: Learning an Explicit Mapping For Sample Weighting** (Shu et al.) | 2019 | NeurIPS | 用 MLP 学习 loss → weight 的显式映射函数，在 noisy label 和 class imbalance 场景下优于手工设计的 weighting | 与 L2RW 类似用 meta-learning；我们的 weight function 是 analytic form（1 - q^b），不需要 meta-learning，更透明可解释 |
35	| 5 | **Curriculum Learning** (Bengio, Louradour, Collobert, Weston) | 2009 | ICML | 奠基性工作：证明按从易到难的顺序训练（curriculum）可以加速收敛并改善 non-convex optimization 的局部极小值 | Curriculum learning 按难度排序，我们按 provenance 加权——虽然形式不同（排序 vs 加权），但都是 non-uniform training 的思想 |
36	| 6 | **Dynamic Loss-Based Sample Reweighting for Improved LLM Pretraining** (Wang et al.) | 2025 | ICLR | 在 LLM pretraining 中做 instance-level dynamic reweighting（基于 loss 值在线调整权重），提出 LinUpper / Quadratic 等策略 | 最直接的对比工作之一——他们基于 loss 做 weighting，我们基于 provenance 做 weighting。两者可组合：先用 provenance weight 再用 loss-based dynamic adjustment |
37	| 7 | **DoReMi** (Xie et al., 2023, 见第 1 节) | 2023 | NeurIPS | Domain-level reweighting via Group DRO | 我们做 instance-level provenance weighting，DoReMi 做 domain-level mixture optimization——粒度和信号来源不同 |
38	
39	## 4. Theoretical Analysis of Data Mixing / Contamination
40	
41	| # | 论文 | 年份 | 场所 | 一句话 Contribution | 与我们的关系 |
42	|---|------|------|------|-------------------|------------|
43	| 1 | **AI Models Collapse When Trained on Recursively Generated Data** (Shumailov, Shumaylov, Zhao, Papernot, Anderson, Gal) | 2024 | Nature | 提出 model collapse 概念：在 synthetic data 上迭代训练导致分布尾部丢失和性能退化，在 VAE / GMM / LLM 上验证 | 我们工作的核心 motivation——Shumailov 证明了 synthetic contamination 的危害，我们提出用 provenance weighting 来缓解而非完全过滤 |
44	| 2 | **Strong Model Collapse** (Dohmatob, Feng, Subramonian, Kempe) | 2025 | ICLR | 证明即使极小比例的 synthetic data（1/1000）也会导致 model collapse；用 operator-valued free probability theory 给出 bias-variance 分解 | 强化了 motivation——即使少量 synthetic data 也有害，说明我们的 provenance weighting 方法的必要性：不能靠 "少量就没事" 来忽视 |
45	| 3 | **Is Model Collapse Inevitable? Breaking the Curse of Recursion by Accumulating Real and Synthetic Data** (Gerstgrasser, Schaeffer et al.) | 2024 | COLM | 证明如果 accumulate（而非 replace）数据，model collapse 可以避免；在 linear model 下证明 test error 有有限上界 | 与我们的方法互补——他们说 "保留 real data 可以救"，我们说 "对 synthetic data 降权也可以救"，都是 mitigate 而非 discard 的思路 |
46	| 4 | **How Bad is Training on Synthetic Data? A Statistical Analysis of Language Model Collapse** (Seddik, Chen, Hayou, Youssef, Debbah) | 2024 | COLM | 给出 recursive training 的统计模型，证明纯 synthetic 训练不可避免 collapse，但 real + synthetic 混合训练在 synthetic 比例低于阈值时可避免 | 直接相关——他们给出了 synthetic data 比例的阈值分析，我们的 α_eff 理论可以看作这类阈值分析的推广（从 hard threshold 到 soft weighting） |
47	| 5 | **Can Generative Artificial Intelligence Survive Data Contamination? Theoretical Guarantees under Contaminated Recursive Training** (Wang, Niu, Li) | 2026 | arXiv 2602.16065 | 为 contaminated recursive training 提供收敛保证：bound d(ℙ̂_t, ℙ_0) ≲ t^{−min{p,α}}，推广至 non-Gaussian 设置；Assumption A2 限制 d 为凸度量，显式排除 cross-entropy/KL | 该论文的收敛 bound 直接启发了我们的 α_eff 定义和 b* 推导——α_eff(b) 将其理论中的 α 从 known parameter 变为 detector-estimated quantity，是我们方法的理论 motivation（非 contribution） |
48	| 6 | **Data Mixing Laws: Optimizing Data Mixtures by Predicting Language Modeling Performance** (Ye, Liu, Sun, Zhan, Zhou, Qiu) | 2025 | ICLR | 发现 domain mixture proportion 和 model performance 之间存在可预测的函数关系（data mixing laws），可以用小规模实验预测大模型表现 | Data mixing laws 可用于预测不同 provenance weight 设置下的 model performance——我们的 Grid-b 搜索可以理论上用 mixing laws 来加速 |
49	| 7 | **Scaling Data-Constrained Language Models** (Muennighoff et al., 2023, 见第 1 节) | 2023 | NeurIPS | 数据受限下的 scaling law，重复 ≤4 epochs 影响可忽略 | 提供了数据受限场景的理论框架，我们的 α_eff 分析在此基础上进一步考虑了 contamination 的影响 |
50	
51	## Key Observations
52	
53	### 与现有工作的主要区别
54	
55	1. **Data selection vs. data weighting**: 多数现有方法（DSIR, FineWeb-Edu, D4）做 hard selection（保留或丢弃），我们做 soft weighting（降权但不丢弃），保留了更多数据多样性和信息。
56	2. **Quality-based vs. provenance-based**: QuRating / FineWeb-Edu 基于 "质量" 评分，我们基于 "来源"（是否 synthetic）评分——这是正交的信号维度，可以组合使用。
57	3. **Detection for filtering vs. detection for weighting**: 现有 synthetic text detection 工作（DetectGPT, Binoculars）几乎全部用于 binary filtering 或人工审核，我们首次将 calibrated detection score 用于 continuous training weight，对检测器的 calibration（ECE）提出了新要求。
58	4. **Analytic weight function vs. learned weights**: 与 meta-learning reweighting（L2RW, Meta-Weight-Net）相比，我们的 weight = 1 - q^b 是 closed-form，无需 clean validation set 或 meta-optimization，更高效透明。
59	
60	### 最直接的竞争对手 / 对比工作
61	
62	- **Drayson et al. (EMNLP 2025)**: 最直接的前驱——同为 detect-and-reweight，但 b 是 heuristic，我们提供 adaptive b*。
63	- **Dynamic Loss-Based Sample Reweighting (Wang et al., ICLR 2025)**: 同为 instance-level reweighting for LLM pretraining，但信号来源不同（loss vs. provenance）。
64	- **DoReMi (Xie et al., NeurIPS 2023)**: Domain-level reweighting，粒度不同但目标相似。
65	- **FineWeb-Edu filtering**: 最接近的 "data quality" 竞品，但是 hard filtering 不是 soft weighting。
66	
67	### 引用决策记录
68	
69	| # | 候选论文 | 决策 | 理由 |
70	|---|---------|------|------|
71	| 1 | **Ghostbuster** (Verma, Fleisig, Tomlin, Klein, NAACL 2024) | ✅ 收录 → Section 2 #7 | Feature-based detector，架构与我们的 TF-IDF + LogReg 最接近（lightweight features + classifier, 无需 target model access），审稿人可能质疑遗漏 |
72	| 2 | **GPTZero** | ❌ 不收录 | 商业工具，无同行评审的方法学论文。现有学术文献均为第三方评估（准确率测试），非方法贡献。学术 related work 中引用商业产品无先例价值 |
73	| 3 | **Self-play fine-tuning / synthetic data augmentation** (代表性工作：SPIN, Chen et al., ICML 2024; Self-Instruct, Wang et al., ACL 2023) | ❌ 不收录为单独条目 | 我们关注的是 pretraining 阶段不可控的 synthetic contamination（来源未知、比例未知），与 fine-tuning 阶段有意使用 synthetic data augmentation 是不同场景。建议在 Related Work 正文中用一句话 acknowledge 此区别（"We focus on uncontrolled synthetic contamination in pretraining, distinct from intentional synthetic augmentation in fine-tuning (Chen et al., 2024)"），但无需展开讨论 |
74	| 4 | **Group DRO** (Sagawa, Koh, Hashimoto, Liang, ICLR 2020) | ❌ 不收录 | DoReMi 引用已覆盖 Group DRO 理论基础。我们是 instance-level provenance weighting，与 Group DRO 的 group-level worst-case optimization 无直接可比性。审稿人不太可能因缺 Group DRO 引用而提问 |
75	| 5 | **Data influence / data attribution** (TracIn, Pruthi et al., NeurIPS 2020; Influence Functions, Koh & Liang, ICML 2017) | ❌ 不收录 | 我们不做 post-hoc influence estimation，而是基于 provenance 做 pre-hoc weighting。目标不同（归因 vs 降权）、方法不同（梯度追踪 vs 检测器评分）、场景不同（诊断 vs 训练干预）。引了反而分散 detect-and-reweight 的主线叙事 |
76	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "0a05528b-d05d-4fb3-947f-20e0adce1e25",
  "uuid": "dc998dc2-bba6-41da-9800-f86707da34b1",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/related_work_notes.md",
      "content": "# Related Work Survey — Provenance Weight Training\n\n## 1. Data Quality / Data Selection for LLM Pretraining\n\n| # | 论文 | 年份 | 场所 | 一句话 Contribution | 与我们的关系 |\n|---|------|------|------|-------------------|------------|\n| 1 | **DSIR: Data Selection for Language Models via Importance Resampling** (Xie, Santurkar, Ma, Liang) | 2023 | NeurIPS | 用 hashed n-gram 特征估计 importance weight，对大规模语料做 importance resampling 来匹配目标分布 | DSIR 按目标分布做 selection，我们按 provenance 做 weighting——都用 lightweight feature 做数据筛选，但动机不同：DSIR 优化 domain match，我们降低 synthetic contamination |\n| 2 | **QuRating: Selecting High-Quality Data for Training Language Models** (Wettig, Gupta, Malik, Chen) | 2024 | ICML | 用 LLM pairwise judgment 对数据做 4 维质量评分（writing style / expertise / facts / educational value），训练 QuRater 模型标注 260B 语料 | QuRating 用 LLM 判断 \"质量\"，我们用检测器判断 \"来源\"——都是 model-based annotation + downstream reweighting，但 quality 和 provenance 是正交维度 |\n| 3 | **The FineWeb Datasets: Decanting the Web for the Finest Text Data at Scale** (Penedo et al., HuggingFace) | 2024 | arXiv | 用 Llama-3-70B 合成标注训练 educational quality classifier，过滤出 1.3T token 的 FineWeb-Edu，在 MMLU/ARC 上大幅领先 | FineWeb-Edu 用 LLM-based classifier 做 hard filtering（保留/丢弃），我们用 detector 做 soft weighting（降权不丢弃），保留更多数据多样性 |\n| 4 | **D4: Improving LLM Pretraining via Document De-Duplication and Diversification** (Tirumala, Simig et al.) | 2023 | NeurIPS D&B | 用 pretrained embedding + K-Means 做去重和多样性平衡，6.7B 模型上提升 2% 下游准确率和 20% 训练效率 | D4 关注重复和多样性，我们关注 synthetic contamination——互补方法，可以先 D4 去重再用我们的 provenance weighting |\n| 5 | **DoReMi: Optimizing Data Mixtures Speeds Up Language Model Pretraining** (Xie, Pham et al.) | 2023 | NeurIPS | 用 Group DRO 在 proxy model 上优化 domain mixture weights，无需下游任务信息，8B 模型提升 6.5% few-shot 准确率 | DoReMi 做 domain-level reweighting（按 domain 调权），我们做 instance-level reweighting（按 q-score 调权）——粒度不同，理论上可以组合使用 |\n| 6 | **DataComp-LM (DCLM): In Search of the Next Generation of Training Sets for Language Models** (Li et al.) | 2024 | NeurIPS D&B | 提供 240T token 标准化语料 + 评估套件，系统性对比 data curation 策略，证明 model-based filtering 是关键 | DCLM 是 benchmark 框架，我们的 provenance-based weighting 可以作为一种新的 curation strategy 在 DCLM 上评估 |\n| 7 | **Scaling Data-Constrained Language Models** (Muennighoff, Rush et al.) | 2023 | NeurIPS | 系统研究数据受限时的 scaling law，发现 ≤4 epochs 重复数据对 loss 影响可忽略，提出考虑重复衰减的 compute-optimal law | 当 unique data 不足时更可能混入 synthetic data 来补量——我们的方法提供了一种替代方案：不用丢弃 synthetic data，而是降权使用 |\n\n## 2. Synthetic Data Contamination Detection\n\n| # | 论文 | 年份 | 场所 | 一句话 Contribution | 与我们的关系 |\n|---|------|------|------|-------------------|------------|\n| 1 | **DetectGPT: Zero-Shot Machine-Generated Text Detection using Probability Curvature** (Mitchell et al.) | 2023 | ICML | 零样本检测：用 log probability curvature（在 perturbation 前后的 log-prob 变化）区分 human vs machine text，无需训练分类器 | DetectGPT 做 binary detection（是否机器生成），我们需要 calibrated probability（q-score）——我们选择 TF-IDF + LogReg 正是因为需要 well-calibrated 的连续 score 而非仅 binary 判断 |\n| 2 | **Fast-DetectGPT: Efficient Zero-Shot Detection via Conditional Probability Curvature** (Bao et al.) | 2024 | ICLR | 将 DetectGPT 的 perturbation 步骤替换为 sampling，加速 340 倍且 AUROC 提升约 75% | 同上——更高效但仍是 binary detection，calibration 质量（ECE）未被重点评估，而这正是我们工作的核心关注点 |\n| 3 | **Binoculars: Zero-Shot Detection of LLM-Generated Text** (Hans et al.) | 2024 | ICML | 用两个 LLM 的 perplexity / cross-perplexity 比值做检测，ChatGPT 文本在 0.01% FPR 下召回 >90% | Binoculars 需要两个 LLM 推理，计算成本高；我们的 TF-IDF + LogReg 检测器极轻量，适合标注数十亿 token 级别的 pretraining corpus |\n| 4 | **GLTR: Statistical Detection and Visualization of Generated Text** (Gehrmann, Strobelt, Rush) | 2019 | ACL | 用 LM 的 top-k token 排名做统计检测和可视化，帮助人类识别机器文本（人类检测率从 54% 提升到 72%） | 早期 statistical detection 工作，启发了后续基于 model statistics 的方法；我们的方法同样基于统计特征但目标不同（scoring for weighting 而非 human-in-the-loop detection） |\n| 5 | **A Watermark for Large Language Models** (Kirchenbauer et al.) | 2023 | ICML | 在生成时嵌入 statistical watermark（green/red token list），可用 p-value 统计检验来检测 | Watermarking 需要控制生成过程，无法检测已有的、未 watermarked 的 synthetic data——我们的场景是 post-hoc detection on existing corpus |\n| 6 | **A Survey on LLM-Generated Text Detection: Necessity, Methods, and Future Directions** (Wu et al.) | 2024 | Computational Linguistics (MIT Press) | 系统综述 statistical / neural / watermarking 三类检测方法，讨论 robustness 和 generalization | 综述文献，帮助定位我们的检测器在整个 detection 方法谱系中的位置——我们是 training-based statistical classifier，但用于 weighting 而非 filtering |\n| 7 | **Ghostbuster: Detecting Text Ghostwritten by Large Language Models** (Verma, Fleisig, Tomlin, Klein) | 2024 | NAACL | 用 structured search 在多个弱 LM 的特征空间中组合 features，训练分类器检测 AI 生成文本；无需 target model 的 token probabilities，跨域 F1 达 99.0 | 架构上与我们的 TF-IDF + LogReg 检测器最接近——都用 lightweight features + 训练分类器，不依赖 target model access；区别在于我们需要 calibrated q-score 而非 binary detection |\n\n## 3. Sample Reweighting in Training\n\n| # | 论文 | 年份 | 场所 | 一句话 Contribution | 与我们的关系 |\n|---|------|------|------|-------------------|------------|\n| 1 | **Machine-Generated Text Detection Prevents Language Model Collapse** (Drayson, Yilmaz, Lampos) | 2025 | EMNLP | 首次提出 detect-and-reweight 框架缓解 model collapse：用 binary detector 检测 synthetic text，通过 importance resampling 降权 synthetic samples，在 GPT-2 / SmolLM2（4 LLM, 2 families, 6 decoding strategies）上验证有效性 | 我们最直接的前驱工作——他们开创了 detect-and-reweight 范式，但权重指数 b 是需要 grid search 的 heuristic hyperparameter，且仅评估 single-generator 场景（WikiText-2）；我们提供理论启发的 adaptive b* 替代 grid search，并扩展到 multi-generator web-scale 场景 |\n| 2 | **Improving the Accuracy of Likelihood-based Inference under Covariate Shift** (Shimodaira) | 2000 | JASA | 奠基性工作：提出 importance weighted ERM（IWERM），通过 density ratio 修正 covariate shift 下的 loss | 理论基础直接相关——我们的 weight = 1 - q^b 可以看作一种 bounded importance weight，Shimodaira 的 IWERM 理论为我们的方法提供了正当性 |\n| 3 | **Learning to Reweight Examples for Robust Deep Learning** (Ren, Zeng, Yang, Urtasun) | 2018 | ICML | 用 meta-learning 在训练中动态学习 sample weights（基于 gradient direction 在 clean validation set 上的表现） | L2RW 需要 clean validation set 做 meta-optimization，我们的方法不需要——weight 由 provenance detector 预先确定，无需在训练中迭代调整 |\n| 4 | **Meta-Weight-Net: Learning an Explicit Mapping For Sample Weighting** (Shu et al.) | 2019 | NeurIPS | 用 MLP 学习 loss → weight 的显式映射函数，在 noisy label 和 class imbalance 场景下优于手工设计的 weighting | 与 L2RW 类似用 meta-learning；我们的 weight function 是 analytic form（1 - q^b），不需要 meta-learning，更透明可解释 |\n| 5 | **Curriculum Learning** (Bengio, Louradour, Collobert, Weston) | 2009 | ICML | 奠基性工作：证明按从易到难的顺序训练（curriculum）可以加速收敛并改善 non-convex optimization 的局部极小值 | Curriculum learning 按难度排序，我们按 provenance 加权——虽然形式不同（排序 vs 加权），但都是 non-uniform training 的思想 |\n| 6 | **Dynamic Loss-Based Sample Reweighting for Improved LLM Pretraining** (Wang et al.) | 2025 | ICLR | 在 LLM pretraining 中做 instance-level dynamic reweighting（基于 loss 值在线调整权重），提出 LinUpper / Quadratic 等策略 | 最直接的对比工作之一——他们基于 loss 做 weighting，我们基于 provenance 做 weighting。两者可组合：先用 provenance weight 再用 loss-based dynamic adjustment |\n| 7 | **DoReMi** (Xie et al., 2023, 见第 1 节) | 2023 | NeurIPS | Domain-level reweighting via Group DRO | 我们做 instance-level provenance weighting，DoReMi 做 domain-level mixture optimization——粒度和信号来源不同 |\n\n## 4. Theoretical Analysis of Data Mixing / Contamination\n\n| # | 论文 | 年份 | 场所 | 一句话 Contribution | 与我们的关系 |\n|---|------|------|------|-------------------|------------|\n| 1 | **AI Models Collapse When Trained on Recursively Generated Data** (Shumailov, Shumaylov, Zhao, Papernot, Anderson, Gal) | 2024 | Nature | 提出 model collapse 概念：在 synthetic data 上迭代训练导致分布尾部丢失和性能退化，在 VAE / GMM / LLM 上验证 | 我们工作的核心 motivation——Shumailov 证明了 synthetic contamination 的危害，我们提出用 provenance weighting 来缓解而非完全过滤 |\n| 2 | **Strong Model Collapse** (Dohmatob, Feng, Subramonian, Kempe) | 2025 | ICLR | 证明即使极小比例的 synthetic data（1/1000）也会导致 model collapse；用 operator-valued free probability theory 给出 bias-variance 分解 | 强化了 motivation——即使少量 synthetic data 也有害，说明我们的 provenance weighting 方法的必要性：不能靠 \"少量就没事\" 来忽视 |\n| 3 | **Is Model Collapse Inevitable? Breaking the Curse of Recursion by Accumulating Real and Synthetic Data** (Gerstgrasser, Schaeffer et al.) | 2024 | COLM | 证明如果 accumulate（而非 replace）数据，model collapse 可以避免；在 linear model 下证明 test error 有有限上界 | 与我们的方法互补——他们说 \"保留 real data 可以救\"，我们说 \"对 synthetic data 降权也可以救\"，都是 mitigate 而非 discard 的思路 |\n| 4 | **How Bad is Training on Synthetic Data? A Statistical Analysis of Language Model Collapse** (Seddik, Chen, Hayou, Youssef, Debbah) | 2024 | COLM | 给出 recursive training 的统计模型，证明纯 synthetic 训练不可避免 collapse，但 real + synthetic 混合训练在 synthetic 比例低于阈值时可避免 | 直接相关——他们给出了 synthetic data 比例的阈值分析，我们的 α_eff 理论可以看作这类阈值分析的推广（从 hard threshold 到 soft weighting） |\n| 5 | **Can Generative Artificial Intelligence Survive Data Contamination? Theoretical Guarantees under Contaminated Recursive Training** (Wang, Niu, Li) | 2026 | arXiv 2602.16065 | 为 contaminated recursive training 提供收敛保证：bound d(ℙ̂_t, ℙ_0) ≲ t^{−min{p,α}}，推广至 non-Gaussian 设置；Assumption A2 限制 d 为凸度量，显式排除 cross-entropy/KL | 该论文的收敛 bound 直接启发了我们的 α_eff 定义和 b* 推导——α_eff(b) 将其理论中的 α 从 known parameter 变为 detector-estimated quantity，是我们方法的理论 motivation（非 contribution） |\n| 6 | **Data Mixing Laws: Optimizing Data Mixtures by Predicting Language Modeling Performance** (Ye, Liu, Sun, Zhan, Zhou, Qiu) | 2025 | ICLR | 发现 domain mixture proportion 和 model performance 之间存在可预测的函数关系（data mixing laws），可以用小规模实验预测大模型表现 | Data mixing laws 可用于预测不同 provenance weight 设置下的 model performance——我们的 Grid-b 搜索可以理论上用 mixing laws 来加速 |\n| 7 | **Scaling Data-Constrained Language Models** (Muennighoff et al., 2023, 见第 1 节) | 2023 | NeurIPS | 数据受限下的 scaling law，重复 ≤4 epochs 影响可忽略 | 提供了数据受限场景的理论框架，我们的 α_eff 分析在此基础上进一步考虑了 contamination 的影响 |\n\n## Key Observations\n\n### 与现有工作的主要区别\n\n1. **Data selection vs. data weighting**: 多数现有方法（DSIR, FineWeb-Edu, D4）做 hard selection（保留或丢弃），我们做 soft weighting（降权但不丢弃），保留了更多数据多样性和信息。\n2. **Quality-based vs. provenance-based**: QuRating / FineWeb-Edu 基于 \"质量\" 评分，我们基于 \"来源\"（是否 synthetic）评分——这是正交的信号维度，可以组合使用。\n3. **Detection for filtering vs. detection for weighting**: 现有 synthetic text detection 工作（DetectGPT, Binoculars）几乎全部用于 binary filtering 或人工审核，我们首次将 calibrated detection score 用于 continuous training weight，对检测器的 calibration（ECE）提出了新要求。\n4. **Analytic weight function vs. learned weights**: 与 meta-learning reweighting（L2RW, Meta-Weight-Net）相比，我们的 weight = 1 - q^b 是 closed-form，无需 clean validation set 或 meta-optimization，更高效透明。\n\n### 最直接的竞争对手 / 对比工作\n\n- **Drayson et al. (EMNLP 2025)**: 最直接的前驱——同为 detect-and-reweight，但 b 是 heuristic，我们提供 adaptive b*。\n- **Dynamic Loss-Based Sample Reweighting (Wang et al., ICLR 2025)**: 同为 instance-level reweighting for LLM pretraining，但信号来源不同（loss vs. provenance）。\n- **DoReMi (Xie et al., NeurIPS 2023)**: Domain-level reweighting，粒度不同但目标相似。\n- **FineWeb-Edu filtering**: 最接近的 \"data quality\" 竞品，但是 hard filtering 不是 soft weighting。\n\n### 引用决策记录\n\n| # | 候选论文 | 决策 | 理由 |\n|---|---------|------|------|\n| 1 | **Ghostbuster** (Verma, Fleisig, Tomlin, Klein, NAACL 2024) | ✅ 收录 → Section 2 #7 | Feature-based detector，架构与我们的 TF-IDF + LogReg 最接近（lightweight features + classifier, 无需 target model access），审稿人可能质疑遗漏 |\n| 2 | **GPTZero** | ❌ 不收录 | 商业工具，无同行评审的方法学论文。现有学术文献均为第三方评估（准确率测试），非方法贡献。学术 related work 中引用商业产品无先例价值 |\n| 3 | **Self-play fine-tuning / synthetic data augmentation** (代表性工作：SPIN, Chen et al., ICML 2024; Self-Instruct, Wang et al., ACL 2023) | ❌ 不收录为单独条目 | 我们关注的是 pretraining 阶段不可控的 synthetic contamination（来源未知、比例未知），与 fine-tuning 阶段有意使用 synthetic data augmentation 是不同场景。建议在 Related Work 正文中用一句话 acknowledge 此区别（\"We focus on uncontrolled synthetic contamination in pretraining, distinct from intentional synthetic augmentation in fine-tuning (Chen et al., 2024)\"），但无需展开讨论 |\n| 4 | **Group DRO** (Sagawa, Koh, Hashimoto, Liang, ICLR 2020) | ❌ 不收录 | DoReMi 引用已覆盖 Group DRO 理论基础。我们是 instance-level provenance weighting，与 Group DRO 的 group-level worst-case optimization 无直接可比性。审稿人不太可能因缺 Group DRO 引用而提问 |\n| 5 | **Data influence / data attribution** (TracIn, Pruthi et al., NeurIPS 2020; Influence Functions, Koh & Liang, ICML 2017) | ❌ 不收录 | 我们不做 post-hoc influence estimation，而是基于 provenance 做 pre-hoc weighting。目标不同（归因 vs 降权）、方法不同（梯度追踪 vs 检测器评分）、场景不同（诊断 vs 训练干预）。引了反而分散 detect-and-reweight 的主线叙事 |\n",
      "numLines": 76,
      "startLine": 1,
      "totalLines": 76
    }
  }
}
```

</details>

---

### Assistant

_source line 80_

文件结构正确，所有编辑已就位。

**完成的修改：**

1. **Section 3 #1** — 插入 Drayson, Yilmaz & Lampos (EMNLP 2025) "Machine-Generated Text Detection Prevents Language Model Collapse"，原有条目重编号为 #2-#7
2. **Section 4 #5** — 插入 Wang, Niu & Li (arXiv 2602.16065, 2026) "Can Generative AI Survive Data Contamination?"，原 #5-#6 重编号为 #6-#7
3. **Section 2 #7** — 新增 Ghostbuster (Verma et al., NAACL 2024)
4. **"潜在的引用遗漏风险"** → **"引用决策记录"**，5 项全部处理：Ghostbuster 收录，GPTZero / Self-play / Group DRO / Data influence 不收录（附理由）
5. **竞争对手列表** — 首位增加 Drayson et al.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "0a05528b-d05d-4fb3-947f-20e0adce1e25",
  "uuid": "df07aef2-6e65-424e-ab0e-5aa4b221ef13",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KvMTRUvUZS6DXzdDWq9chf",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6206,
      "cache_read_input_tokens": 62487,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 6206
      },
      "output_tokens": 1,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Task result

_source line 81_

文件结构正确，所有编辑已就位。

**完成的修改：**

1. **Section 3 #1** — 插入 Drayson, Yilmaz & Lampos (EMNLP 2025) "Machine-Generated Text Detection Prevents Language Model Collapse"，原有条目重编号为 #2-#7
2. **Section 4 #5** — 插入 Wang, Niu & Li (arXiv 2602.16065, 2026) "Can Generative AI Survive Data Contamination?"，原 #5-#6 重编号为 #6-#7
3. **Section 2 #7** — 新增 Ghostbuster (Verma et al., NAACL 2024)
4. **"潜在的引用遗漏风险"** → **"引用决策记录"**，5 项全部处理：Ghostbuster 收录，GPTZero / Self-play / Group DRO / Data influence 不收录（附理由）
5. **竞争对手列表** — 首位增加 Drayson et al.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "type": "result",
  "subtype": "success",
  "is_error": false,
  "api_error_status": null,
  "duration_ms": 360309,
  "duration_api_ms": 414001,
  "num_turns": 29,
  "stop_reason": "end_turn",
  "session_id": "0a05528b-d05d-4fb3-947f-20e0adce1e25",
  "total_cost_usd": 1.5026464999999996,
  "usage": {
    "input_tokens": 1581,
    "cache_creation_input_tokens": 56852,
    "cache_read_input_tokens": 709077,
    "output_tokens": 14939,
    "server_tool_use": {
      "web_search_requests": 0,
      "web_fetch_requests": 0
    },
    "service_tier": "standard",
    "cache_creation": {
      "ephemeral_1h_input_tokens": 56852,
      "ephemeral_5m_input_tokens": 0
    },
    "inference_geo": "",
    "iterations": [
      {
        "input_tokens": 1,
        "output_tokens": 299,
        "cache_read_input_tokens": 62487,
        "cache_creation_input_tokens": 6206,
        "cache_creation": {
          "ephemeral_5m_input_tokens": 0,
          "ephemeral_1h_input_tokens": 6206
        },
        "type": "message"
      }
    ],
    "speed": "standard"
  },
  "modelUsage": {
    "claude-haiku-4-5-20251001": {
      "inputTokens": 243028,
      "outputTokens": 5675,
      "cacheReadInputTokens": 0,
      "cacheCreationInputTokens": 0,
      "webSearchRequests": 14,
      "costUSD": 0.411403,
      "contextWindow": 200000,
      "maxOutputTokens": 32000
    },
    "claude-opus-4-6": {
      "inputTokens": 1581,
      "outputTokens": 14939,
      "cacheReadInputTokens": 709077,
      "cacheCreationInputTokens": 56852,
      "webSearchRequests": 0,
      "costUSD": 1.0912435,
      "contextWindow": 200000,
      "maxOutputTokens": 64000
    }
  },
  "permission_denials": [],
  "terminal_reason": "completed",
  "fast_mode_state": "off",
  "uuid": "b2295b74-6ad8-43b4-89f0-20223c6ee197"
}
```

</details>

---
