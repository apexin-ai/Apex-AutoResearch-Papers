# Research conversation: 执行项目轨迹扫描，将报告写入 /home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/scan_reports/layer2_20260531T1 — Part 2 of 2

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction (July export snapshot)** · Conversation logs

[← Part 1](part-001.md) · [Transcript overview](../research-conversation-home-ubuntu-agent-ml-research-idea-gen-0513-6-projects-faith-evidence-ie-scan.md) · [Structured JSON](../../../sessions/76/7653e8fe16597dbf357b.json)

## Round 1

### Tool call

_source line 192 · 2026-05-31T14:32:43.405Z_

<details open><summary>🔧 Tool call — Write · `toolu_017pNCKjyFbbctwJYXc4Nppz`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/scan_reports/layer2_20260531T142125.md",
  "content": "# faith-evidence-ie — 轨迹分析报告\n\n> 扫描时间: 2026-05-31T14:21:39Z\n> 工作区: /home/ubuntu/.agent-ml-research-idea_gen_0513_6\n\n## 1. 项目概况\n\n**项目**: FREIGE (Faithfulness-Rewarded Evidence-Grounded Information Extraction via Contrastive Evidence Discrimination)，evidence-grounded DocRE 方向。\n**Venue**: EMNLP 2026 Main（ARR July cycle）。Round 2 评分 3.0 (Findings)，扫描时正在准备 Round 3。\n**周期**: 2026-05-14 ~ 2026-05-25（Director 最后一次 boot 5-24，Agent 最后事件 5-25 19:51；Reviewer 最后事件 5-25 04:09），约 11–12 个活跃日。\n**实验规模**: registry 382 条，DONE 379 / PREPARING 3；conclusion 分布 success 247 (65%)、failed 65 (17%)、killed 47 (12%)、negative 23 (6%)。\n**Session/Token**:\n- Agent 601 sessions / 63.3k turns / 29M output tokens / 784 errors（占总错误 53%）\n- Worker 1497 sessions / 92k turns / 36M output tokens / 464 errors\n- Reviewer 105 sessions / 43.8k turns / 18.4M output tokens\n- Director 171 sessions / 26.3k turns / 8.8M output tokens\n- 总 token 98.6M（其中 output 95.5M），错误总数 1491\n- 总 duration 113,042 minutes（约 1884 小时角色累计活跃时间，跨 4 个角色并行运行）\n**论文**: main.tex 编译通过、35 references、PDF 估计 100 页（含 appendix）、4870 KB。3 figures + 多表格、Round 2 三贡献叙事（RSFT+NLI / Decoupling spectrum / Evidence tax landscape + variance compression）。\n**关键控制事件**: 304 RESET_REQUEST_SENT、307 HARD_LIMIT_REACHED、20 ESCALATED_TO_HUMAN（全部 director_no_response）、5 ESCALATED_SILENT、38 条 mistakes、159 条 decisions、Agent 共 261 次 boot。\n\n## 2. 项目叙事重建\n\n项目分为 6 个清晰的阶段：\n\n**阶段 1 — Setup + GRPO 灾难期（5-14）**\n项目从 IDEA_BRIEF 启动，前 6 小时被 SSH 密钥审批阻塞（GPU 分配 4，实际跑 0）。MVP-1 (CED 信号验证) 在 14:00 前通过（margin=0.4827, acc=81.5%）。\n14:00 后进入 GRPO+QLoRA 训练，连续 5 轮失败（D005–D023）：r1 mode collapse / r2 OOM (num_iterations=2 + 4-bit → KL 数值爆炸 step 5 KL=3.7e9, step 15 KL=3.4e11) / r3 KL 爆炸 / r4-5 mode collapse / extract_r3-4 / flatnli_r3-r6 全部 mode collapse。同期用户（PI 孙震）从 17:17 开始问\"实验为什么做不下去\"，Director 给出长 markdown 解释。这一天的 mvp2_grpo_* 实验 = 14+ 条 killed/failed，但是 mode collapse 数据形成了 Claim 2（decoupling spectrum）的核心证据。\n\n**阶段 2 — Pivot 到 RSFT + MVP-2 通过（5-15）**\n凌晨判定 GRPO+QLoRA 全线 FAIL，pivot 到离线 RSFT (D031/D033/D037)。中午 D037 一度错误宣告 RSFT 也\"灾难性失败 rel_f1=0.0483\"，几小时后 D038 撤回（eval bug：50-doc pred vs 12275 gold denominator）。15:00 后 D040 正式过 MVP，进入 research 阶段。下午 Dream v1 (best=2.5/median=3.0/worst=2.5，倒挂) 被识破\"诚实版本得分更高\"，Dream v2 (best=3.0) 仍未达 3.5 目标。决策 D050 提出 pivot 到 \"analysis paper framing\"，D051 当晚因 plan_011 (bf16 GRPO) ckpt-100 rel_f1=0.4549 推翻 pivot 前提：bf16 GRPO 不 forget，QLoRA 才是 catastrophic 的根因 → C2 reframe 为 \"QLoRA-specific artifact\" (D054)。这一天用户共发 14 条飞书消息，全部为简短状态查询或概念问题。\n\n**阶段 3 — Scaling expansion（5-16 ~ 5-19）**\n进入大规模 scaling study：4 个 Qwen scale (1.7B/4B/8B/14B) + LLaMA-3.1-8B cross-family + Re-DocRED cross-dataset。这段期是错误密集期：\n- M002 4B RSFT gain 错误 (+6.1pp→+5.5pp)\n- M003 Paper Agent Related Work 幻觉引用 (E-GRPO, R1-RE, KD-DocRE 误归属)\n- M004 scaling 实验 k=3 vs 论文声明 k=1 不一致 → D102 必须全部重训\n- M005 4 个并行训练磁盘满 → 全崩，GPU 空转数小时\n- M006 Wave1 批量脚本 4 个 critical 问题（GPU/路径/save_total_limit/DeepSpeed 矛盾）\n- M007/M008 CUDA_VISIBLE_DEVICES 被脚本覆盖\n- M010/M011 1.7B RSFT s43/s44 adapter 错误判断 → Worker 自行删除有效输出\n- M012/M013 14B eval 用 --quantize 违反 D076 协议、D112 RSFT 用 QLoRA 引入 confound\n- 5-17 ~ 5-18 凌晨 ESCALATED_TO_HUMAN 集中爆发：8 条 escalation 在 12 小时内（5-17 22:27 ~ 5-18 02:09），原因均为 director_no_response。\n\n**阶段 4 — Methodology corrections（5-20 ~ 5-22）**\nEvidence tax 计算多次返工，是项目最长的\"原地踏步\"期：\n- D127 sign convention 标准化 → M016 子值翻错\n- M017 第 2 次 ign_f1/rel_f1 混淆（LLaMA RSFT s42），导致 D125/D128/paper_framing/ROADMAP/Paper Agent patch 全部受污染\n- D137 确立 matched@2048 协议 → M026 Worker 仍用 @1024 with-evi（D137 同类错误）\n- M027 D140 全部 Qwen no-evi eval 用了 plan_014 的训练 adapter 而非标准 SFT + --no_evidence flag → 1.7B/4B/8B 全部失效\n- M030 fair_tax 计算文件混用 @1024/@2048，导致论文 LLaMA tax 方向错误\n- M031 LLaMA RSFT no-evi cascade 写错 max_new_tokens=1024 与 with-evi 2048 不匹配\n- M032 8B RSFT 方差压缩 17× 混用了 k=3 和 k=1 模型 → 修正为 6.5×\n- M033 Director 级联指令 LLaMA RSFT 三个路径全错 → Worker 重启丢失 302/500 进度（~5h）\n- M034 Registry cleanup Worker 过度删除 ~194 条实验（指令明确要求只加 note）\n- M035 RSFT seed protocol 缺陷：4B/8B/LLaMA 的 RSFT seeds 全部从 SFT s42 出发（共享 base），variance compression claim 的方法论基础有缺陷\n\n**阶段 5 — Round 2 audit + paper polishing（5-23 ~ 5-24）**\nD155 Round 2 (3.0) Action Matrix；D157 数据审计完成 3 项修正；D158 补跑 1.7B s44 和 14B s44 RSFT 全流程消除跨 scale 种子数不一致。\n\n**阶段 6 — QLoRA flip-flop 事故（5-24 ~ 5-25）**\nM037/M038 双向错误 CRITICAL 指令链：\n1. 前 Director session 在 Agent 完成审计前发 CRITICAL G=4→G=8，触发 Paper Agent 8 处论文修改 + 2 张图重画\n2. Agent 审计表用\"实验命名约定\"而非 config 真值，错报 G=4\n3. 新 Director 信任 Agent 审计，发 CRITICAL revert G=8→G=4\n4. Reviewer 用 registry 行号确认 G=8\n5. Director 再发 CRITICAL 恢复 G=8\n\n三次 flip-flop 造成 Paper Agent 大量重复工作。项目最后一次 Director boot 在 5-24 11:16，扫描时项目处于\"等待 Round 3 review\"状态，4 张 GPU 全部空闲。\n\n**关键转折点**:\n- 5-14 18:00 GRPO 失败 → RSFT pivot（被迫，结果支持了 negative finding 的论文化）\n- 5-15 16:32 plan_011 bf16 GRPO 不 forget → Claim 2 从\"RL fails for IE\"重定位为\"QLoRA-specific artifact\" → 后又 generalize 为 \"decoupling spectrum\"\n- 5-18 D078 CED vs flat-NLI p=0.44 → CED 从核心贡献降级\n- 5-21 D137 matched@2048 协议确立 → 大量已有 evidence tax 数据需重新计算\n- 5-22 D144 4B \"capacity valley\" 叙事被 M027 修正完全推翻\n\n**停滞期**: 5-17 ~ 5-18 凌晨（8 次 ESCALATED_TO_HUMAN）、5-20 ~ 5-22（evidence tax methodology 反复返工）。**加速期**: 5-15 下午（pivot 后多卡并行+plan_011 结果推动叙事重构）、5-23（Round 2 Action Matrix 落地）。\n\n## 3. 科研目标达成度分析\n\n### 3.1 Idea → Findings 的逻辑链\n**原始 idea (IDEA_BRIEF)**: 用 GRPO + CED reward 训练 LLM 同时输出 relation triples + 支撑证据；CED 通过 within-document hard negative 解决 NLI faithfulness 的 gameability 问题。Make-or-break 实验是 CED vs flat-NLI ablation，dual publishability threshold：Evi-F1 > 57.34 AND F1 > 53。\n\n**最终论文 (paper_framing 3 贡献)**:\n1. RSFT + NLI-based scoring 有效性\n2. Decoupling spectrum (GRPO catastrophic > DPO gradual > RSFT none)\n3. Evidence tax landscape + variance compression\n\n**Reframe 链**:\n- Reframe #1（被迫）: GRPO 全线失败 → 从 \"online RL CED\" 转向 RSFT (D031/D037)\n- Reframe #2（被迫）: D078 CED vs flat-NLI p=0.44 统计不可区分 → CED 降级为 \"one possible scoring function\"，与 flat-NLI 等效\n- Reframe #3（主动）: bf16 GRPO 不 forget (D051) → 从 \"online RL fails\" 收窄为 \"QLoRA artifact\"，再泛化为 \"decoupling spectrum\"\n- Reframe #4（被迫）: 4B \"capacity valley\" (+7.5pp) 由 M027 adapter 错误造成 → D144 修正为 +0.73pp，capacity valley 叙事完全推翻，C5 重写为 \"within-family threshold\"\n- Reframe #5（被迫）: variance compression 17× → 6.5×（M032 混用 k=3/k=1 数据）\n\n**与原始 idea 的偏离**: 原始 idea 的核心技术 (CED reward in GRPO) 完全失败，论文最终核心是这个失败本身（decoupling spectrum）+ 离线替代 (RSFT) + scaling 现象学（evidence tax landscape）。**论文的核心 claim 与原 hypothesis 关系微弱——CED 作为 reward 的 contrastive insight 在论文中只保留为 RSFT 的 scoring function，与 flat-NLI 不可区分**。从科学价值看，这是一个失败 idea 通过 negative result + 现象学发现救出来的论文。\n\n### 3.2 实验设计的科研严谨性\n\n**Falsifiable 设计**：✅ Make-or-break (D076/D078: CED vs flat-NLI t-test) 设计良好且诚实执行——p=0.44 直接接受 null。Dream 模拟（D043/D047）作为投稿前可证伪 gate。\n**对照 baseline 设计**：☑️ 部分充分。Baselines 12+ 列出，但 plan_004 DREEAM 自己复现，plan_022 第三个模型家族 / plan_023 DocKS-RAG+LMRC 复现都列为 P2 并未完成。所有 RSFT 与 SFT 同 backbone 同 protocol 比较合规。\n**统计方法**：⚠️ 严谨性反复出问题：\n- M002, M017 两次 ign_f1/rel_f1 混淆，污染了 ROADMAP + paper_framing + Paper Agent patch\n- M005 4 个并行训练磁盘满 → seed 1, 2, 3, 4 全崩\n- M035 共享 SFT base 缺陷直到 Round 3 才暴露 → variance compression 由 contribution 降为 observation\n- D118 \"RSFT 1.7B surpasses 8B SFT\" → 修正为 \"approaches\"\n- D155 \"consistently reduces\" 替代 \"substantially reduces\"（sign test p=0.0625 n=4 结构性上限）\n- D146 4B 3-seed mean=+0.25±0.47pp 用 sample std (ddof=1)，被 Director 纠正过一次（agent.md 红线）\n**P-hacking / cherry-picking 倾向**：\n- 4B 主表 n=3（去掉 s45），附录透明报告 n=4（director.md 红线明确禁止把 s45 加回主表）。这是诚实的，但意味着 s45 被排除有偏的可能性\n- evidence tax 在 dev 用 matched@2048 fair subset，test 用全量 500 docs，两套协议不一致（D147 8B dev=+0.04 vs test=-1.71pp 方向不一致）\n- 4B RSFT test tax 唯一正值 (+1.65±0.29)，但 paper 将其框入 \"heterogeneous, scale-dependent\" 框架内（D153 Version B confirmed）\n\n**实验规模**: 5 scales × 多 seed × 多 protocol 已属重量级；shared SFT base 缺陷削弱了 generalizability claim。\n\n### 3.3 Findings 的质量与 Novelty\n- **Original GRPO+CED claim**：已被证伪，但失败本身（QLoRA quantization 在 RL-for-IE 任务上的 catastrophic collapse）+ 跨方法 decoupling spectrum 有发现价值。\n- **RSFT**: 诚实定位为 STaR (NeurIPS 2022) 单轮变体（D076-related），不作为方法贡献。\n- **Evidence tax landscape (C3)**：跨 5 个 scale + 跨 2 个家族的现象学是项目最有 novelty 的发现——但 D144 \"within-family threshold\" 替代 \"capacity valley\" 后，叙事弹性减弱（1.7B 唯一显著获益，4B/8B/14B 都接近 0，threshold 在 1.7B-4B 之间只是 2 点数据）。\n- **Variance compression**：6.5–31× 跨 scale 一致是 striking 数据，但 M035 共享 SFT base 缺陷使其降为 observation。\n- **EDCR**: 方法级 ρ=-0.965 接近完美相关 → D071 自己承认 \"by-construction 混淆\"，per-relation EDCR 独立诊断（ρ_evi_f1=-0.064）救回了价值。\n\n**审稿评分轨迹**:\n- Dream v1 best/median/worst = 2.5/3.0/2.5\n- Dream v2 best/median/worst = 3.0/2.5/2.5\n- Round 1 actual review = 3.0\n- Round 2 actual review = 3.0 (Findings)\n- 项目目标 EMNLP Main (≥4.0) 与实际评分 3.0 (Findings) 之间存在 1.0 分缺口。从科研内容看，原始 CED hypothesis 失败 → 论文重心被迫转移到现象学发现 + negative result framing，这种\"救出来\"的论文在主会的天花板就是 borderline。\n\n### 3.4 研究效率\n**直接贡献最终论文的实验**: 约 247 success 中粗估 ~150 项被论文主表 / appendix 引用（核心 5 scales × {SFT, RSFT, no-evi} × {dev, test} × multi-seed + 关键消融 + DPO/GRPO baseline）。\n**探索性弯路**:\n- GRPO+QLoRA 整个 mvp2_grpo_* 系列约 30+ 实验，~50 GPU-h，绝大多数 failed/killed。但实验本身产出了 Claim 2 的关键 negative result，**作为 negative result 是有价值的弯路**。\n- D102 全 scale k=3→k=1 重训：~40 GPU-h，纯粹因为 M004 早期 scaling 实验偏离 canonical 配置。**纯粹浪费**。\n- D137/M026 matched@2048 协议反复：~30 GPU-h 浪费在 mismatched comparison（@1024 with-evi vs @2048 no-evi）和后续重算。**纯粹浪费**。\n- M027 D140 全部 Qwen no-evi eval 使用错误 adapter：~20 GPU-h，4B/8B killed，1.7B INVALIDATED + D142 narrative reframe 悬空。**纯粹浪费**。\n- M005 磁盘满 4 训练崩溃 + M019 14B 12h gen 内存 only 丢 1872/3027 docs + M021 rsync 删除 r3 的 5016 条数据：**大型基础设施事故**累计 ~40 GPU-h 浪费。\n- M025/M020/M023 Agent 空闲（cron 回调失效）：累计 ~10 张卡时空转。\n- M037/M038 QLoRA G=4↔G=8 flip-flop：Paper Agent 至少 3 轮重复修改 8 处+2 张图。\n\n**粗估**: ~10–15% GPU 时间在 GRPO 探索（产出 negative result，可接受）；~15–20% 在纯粹 methodology / infra 错误（不可接受）。\n\n### 3.5 论文与实际科研的匹配度\n- ⚠️ D147/director.md 标注\"14B 定位为 validation scale (n=2)，论文中 14B 相关 claim 必须用 hedged 语言\"——14B test tax mean=+0.12±0.64pp (n=3 with s44 补全) CI 跨零，论文用 \"neutral/uncertain\"。✅ 诚实。\n- ⚠️ Variance compression claim 在 M035 暴露后降级为 \"observation\"，experiments.tex/method.tex 加 shared SFT base caveat（reviewer.md 红线）。✅ 诚实。\n- ⚠️ \"RSFT 1.7B surpasses 8B SFT\" → \"approaches\"（D118）。✅ 诚实。\n- ⚠️ Abstract/Contributions 用 \"consistently reduces\" 替代 \"substantially reduces\" (D155)，sign test p=0.0625 n=4 是结构性上限。✅ 诚实。\n- ⚠️ M003 Paper Agent Related Work 含幻觉引用 (E-GRPO/R1-RE) + KD-DocRE 误归属为 Re-DocRED 数据集。已 Reviewer 拦截修正。\n- ⚠️ M036 论文 Table 3/§4.3 GRPO hyperparameter 表 3 项错误 (G=4 vs G=8, lr, batch sizes)，导致 3 轮 reviewer 基于错误数据的 confound 分析。\n- ⚠️ M037/M038 G=4↔G=8 flip-flop。\n\n**总体**: 在被发现后的 disclosure 是诚实的；但 (1) 论文中关键数字多次被错误数据驱动（M002/M017/M027/M032/M036），(2) 这些错误的暴露主要靠 Reviewer 而非 Agent 自检。\n\n### 3.6 人工参与分析\n\n**人工参与频率**: 极低且集中。Director session 共记录 **27 条** 用户（PI 孙震）飞书消息，**全部** 集中在 2026-05-14 ~ 2026-05-15（前 48 小时）。5-15 之后 ~16 天的运行无人工干预。\n\n**用户消息性质**:\n- 概念性提问 (10 条): \"证据\"到底是什么、\"是知识图谱吗\"、\"难道这个 idea 只是多了一个维度\"、\"定位句子很难训练吗\"——用户在 5-14 上午对 idea 本身不熟悉，让 Director 反复解释\n- 状态查询 (12 条): \"实验做的怎么样了\"、\"mvp 验证还没过吗？\"（同样问题重复 4 次）、\"还要多久才可以开始写论文\"\n- 战略性消息 (5 条): \"MVP之后需要Dream\"、\"gpu 利用满了吗\"、\"GRPO+QLoRA 全线失败...会有什么影响\"、\"这篇 paper claim 的点是什么\"、\"你把这个 idea 全部都详细的给我说一遍\"\n\n**触发条件**:\n- ESCALATED_TO_HUMAN 20 次 + ESCALATED_SILENT 5 次都是\"director_no_response\"，理论上应该触达用户，但飞书消息只在 5-14/15 出现 → **运维群升级机制可能未真正联通到 PI**，或 PI 不查看升级消息\n- mistakes.yaml 中 `user_intervention` / `user_feedback` 标记: 0 条。M027/M035 等关键事故均由 Agent/Reviewer 自检发现，无人工介入痕迹\n\n**人工参与的影响**:\n- 5-14 GRPO 失败时用户问\"为什么做不下去\"——Director 整理出长解释，**催生了 D031/D033 判死 GRPO+QLoRA 的决心**。如果没有此提问，Director 可能继续刷 GRPO 配置\n- 5-14 18:24 用户\"gpu 利用满了吗？抓紧最大效率跑mvp\"——是 5-15 4 卡并行 RSFT/GRPO/DPO/SFT-no-evidence 同时跑的直接触发\n- 5-15 03:15 用户主动转述\"GRPO+QLoRA 全线失败...会有什么影响\"，相当于把 Director 在 D031 之前的内部判断变成了\"已正式向 PI 通报的状态\"，巩固了 pivot 决策\n- 5-15 06:18/08:48 用户连环追问 claim 是什么 → 触发 paper_framing.md 落地（D040 之后）\n\n**时机评估**: 用户的早期高频参与对论文叙事定型起到关键作用，但 5-15 之后\"放手\"导致 16 天内所有重大方法论错误（M027/M032/M035/M037/M038 等）均无人工把关。**M035 共享 SFT base 这种根本性方法论缺陷，如果在 5-18 scaling 实验设计时由人审一眼就能拦下；让其拖到 Round 3 才暴露，论文已被迫降级为 observation**。\n\n**反事实推理**: 如果 5-14 PI 不质问 GRPO 失败原因，Director 可能再多刷 1-2 天 GRPO 配置，但最终也会判死（Dream v1/v2 会把它逼出来）。如果 5-15 之后 PI 不放手而是周检 1 次，M002/M017 ign_f1/rel_f1 混淆 / M035 shared SFT base 应该可以早 5-10 天发现，evidence tax 章节可以省 ~30 GPU-h 返工。\n\n**Briefer 角色（2 sessions, 1571 minutes, 61 turns）**: 大幅介入但只在项目 boot 时 onboarding 用，不参与 ongoing 决策。\n\n## 4. 角色行为深度分析\n\n### Director（171 sessions, 26.3k turns, 8.8M output tokens, 55 errors）\n\n**做得好**:\n- 决策记录完整（159 条 D-编号），关键 reframe 都留有依据\n- 5-15 同一天内 (Dream v2 失败 → plan_011 反转) 完成两次叙事重构，反应敏捷\n- D076 统一协议 / D102 k=3→k=1 / D137 matched@2048 等 methodology unification 及时落地\n- 用户 5-14 早期提问时给出的解释结构清晰、tradeoff 明确（17:17 长 markdown 复盘）\n\n**问题**:\n- **决策反复**: D050 pivot 到 analysis paper → D051 推翻；D061 关闭 DPO → D063 撤回；D068 修正 DPO 结论 → D069 再修正 → 进入 spectrum 框架。Decision yaml 中至少 12 处后续 D 修正前一个 D 的结论\n- **D-编号膨胀**: 159 条 decision，平均 1.7 条/小时，多数是策略微调而非战略决策。后期（D110+）大量是数据修正而非真正\"决策\"\n- **5-17/5-18 的 director_no_response 集群**: 16 条 ESCALATED_TO_HUMAN 在 36 小时内 → Director session 在关键 RSFT scaling 高峰期 unresponsive，触发 Agent/Reviewer 多次反复升级\n- **M037/M038 flip-flop**: 前 Director session 在 Agent 完成审计前发 CRITICAL → 后 Director session 信任 Agent 错误审计表又 revert → Reviewer 用 registry 行号才确认。**三方信息冲突时未等最可靠来源（registry）**\n- **M033 LLaMA 路径 3 个全错**: 从 handoff 记忆中照搬路径而非从 registry 成功实验复制 → 浪费 ~5h Worker 进度\n- **M002 4B RSFT gain 错误数字未交叉验证就写入 D088/D094/ROADMAP**: 后由 Reviewer 核实纠正\n- **Cron 回调失效（M023/M025）**: Agent 空闲 2h+ 无 harvest，Director 在 WAIT 期间未设短间隔检查\n\n### Main Agent（601 sessions, 63.3k turns, 29M output tokens, 784 errors）\n\n**做得好**:\n- 跨 11 天 261 次 boot 保持基本任务连续性\n- Top tools: update_registry 3161, read_registry 2355, spawn_worker 1662, post_to_director 1139 → Registry-centric workflow\n- 大多数 worker 派发能正常 closure 到 cron callback\n\n**问题**:\n- **Session 不稳定**: 245 HARD_LIMIT_REACHED + 245 RESET_REQUEST_SENT 表示**每 ~6 turns 就触发一次硬性 reset/handoff**。每次 reset 都需要重读 task_context/agent.md（58 行）和大量 memory.md。这是 token 消耗 29M 的主因\n- **Worker 派发错误率高**: mistakes.yaml 中 M006/M007/M008/M010/M012/M013/M018/M026/M027/M028/M029/M031 共 12 条 worker_dispatch / experiment_design 类错误，多数是\"复制粘贴脚本不修改路径/参数\"\n- **自检能力弱**: 大多数错误 (M002/M017/M026/M032 等数值错误) 由 Reviewer 拦截而非 Agent 自检。Agent 报数往往是从 metrics.json 的位置推断而非字段名提取\n- **未授权操作**: M028 Agent 未经审批自行启动 retrain_4b_rsft_ced_s42；M034 Agent 错误执行 registry 批量删除（指令明确\"只加 note 不删除\"），删除 ~194 条\n- **失效 cron 回调（M023/M025）**: Agent compaction 后丢失 cron 注册，连续 2 次出现\n\n### Reviewer（105 sessions, 43.8k turns, 18.4M output tokens, 113 errors）\n\n**做得好**:\n- 是项目的**关键防错层**: M002, M003, M012, M013, M027, M032, M036, M037 reverse, M038 都由 Reviewer 拦截/纠正\n- top tool ssh_read_only 6608 次 → 重度依赖直接验证而非 Agent 转述\n- D076 paired t-test、D078 CED vs flat-NLI 不可区分、bf16 GRPO vs QLoRA quantization isolation (D052) 等关键统计/方法验证都是 Reviewer 主导\n- 9 次 ESCALATED_TO_HUMAN + 高 ssh_read_only 频次 → 在 Director 不响应时仍主动验证\n\n**问题**:\n- **ScheduleWakeup 728 次** → Reviewer 大量时间花在自我唤醒等待，效率不高\n- 27 sessions 文件平均 2.85MB（p90=7.7MB, max=20MB）→ 单 session 时间极长，token 重负\n- **共享 SFT base 缺陷（M035）拖到 Round 3 才发现**: 在 5-18 全 scale RSFT 设计时本应注意到 registry 依赖链问题，Reviewer 早期审查时没追溯\n\n### Worker（1497 sessions, 92k turns, 36M output tokens, 464 errors）\n\n**做得好**:\n- top tools: ssh_read_only 20071, ssh_execute 4037 — 比 1:5 健康\n- 平均每个 worker session 仅 61 turns、6 个 tool uses → 任务定义粒度合理\n\n**问题**:\n- 464 errors（约 31% 错误率，按 1497 sessions 计算）—— 高\n- M005 4 task 同时写 checkpoint 磁盘满崩；M019 14B 12h gen 无 resume 全丢；M021 rsync 覆盖 r3 写入的文件——**3 起重大事故均与 worker 写 IO 设计有关**\n- Resource_misuse 类错误占比高（M005/M009/M018/M020）\n\n### Paper Agent（17 sessions, 8.6k turns, 4M output tokens, 59 errors）\n\n**问题**:\n- M003 Related Work 含幻觉引用 (E-GRPO, R1-RE)，KD-DocRE 误归属为 Re-DocRED 数据集——**LLM 写作典型 hallucinated citation**\n- 多次成为 Director flip-flop 的下游受害者（M036 3 项超参错误重写、M037 8 处修改、M038 reverse）\n- Top tool ToolSearch 111 次 + WebSearch 55 → 大量用于补救引用\n\n### 角色协作摩擦点\n1. **Agent → Director 的数据传递不可靠**: M002/M017 数值错误未交叉验证直接写入 decision；M037 Agent 审计表用实验名命名而非真值\n2. **Director → Agent 的路径/参数传递不可靠**: M027 / M031 / M033 都是 Director 从 handoff 记忆中照搬错误参数\n3. **Director → Paper Agent 的指令缺乏 dry-run 验证**: M036/M037/M038 三次基于错误真值的 CRITICAL 修改\n4. **Reviewer 是事实仲裁者但成本极高**: 单 session 平均 2.85MB / 1730 minutes，是 Director (1.06 hours/session) 的 ~10× 时长\n\n## 5. 关键发现\n\n### 5.1 [HARNESS] Session reset 风暴吞噬主要 token 预算 — Critical\n\n**证据**:\n- Agent 304 RESET_REQUEST_SENT + 245 HARD_LIMIT_REACHED + 261 boot = **每 6-12 turns 就要 reset 一次**\n- Agent output tokens 29M / 63.3k turns = 平均每 turn 458 tokens，但 boot 时需读 task_context/agent.md（58 行）+ memory.md（66 行）+ paper_framing.md（404 行）+ 多次 read_registry/get_project_status\n- 单次 boot 重读约 50-100k tokens 上下文，261 次 boot ≈ 20M+ token 仅用于\"找回状态\"\n- 5-17 ~5-18 凌晨 16 条 ESCALATED_TO_HUMAN 全部在 36h 内 → reset 频率太高导致 Director 无法处理积压消息\n\n**严重程度**: 极高。98.6M 项目总 token 中估计 25-35% 用于 session 恢复。\n**改进建议**:\n- 把 boot 上下文从 \"重读所有 md\" 改为 \"增量 diff\" — 仅读上次 reset 后变更的部分\n- 拉长单 session wall_time 上限（当前 ~360min → ~720min for Director），减少 boot 次数\n- 把 task_context 改为 yaml/json 结构化，让 boot 只读\"机器需要的\"而非\"人类可读的长 markdown\"\n\n### 5.2 [HARNESS] 三方信息（Agent 报告 / Director 指令 / Registry 真值）冲突时无优先级仲裁 — Critical\n\n**证据**:\n- M037 → M038 G=4↔G=8 三次 flip-flop：前 Director (基于 registry hypothesis 字段误读) → Agent 审计表 (基于实验命名约定) → Reviewer (基于 registry 实际 spec L1015/L1048/L3470) → 最后才确认 G=8\n- M002 4B RSFT gain：Agent 报 rel_f1=0.4655 (无法复现) → Director 写入 D088/D094/ROADMAP → 后 Reviewer 核实纠正\n- M017 LLaMA RSFT s42 ign_f1=0.5839 (实为 rel_f1) → 污染 D125 evidence tax 计算 / D128 3-seed 统计 / paper_framing / ROADMAP / Paper Agent patch\n- M027 Worker adapter 路径错误 → D140 1.7B/4B/8B 全部失效 + D142 reframe 悬空\n- M033 Director 级联指令 LLaMA 3 个路径全错 → Worker 自动修正但丢失 5h 进度\n\n**严重程度**: 极高。每个事故造成 5-50 GPU-h 浪费 + Paper Agent 多轮重做。\n**改进建议**:\n- 数值类报告强制结构化校验: ign_f1 < rel_f1 (DocRED 上恒成立) → invariant check\n- 任何写入 decision 的数值必须 hash 到 registry source-of-truth，自动验证\n- Critical 指令发出前自动锁住相关 decision，Reviewer 不 sign-off 不解锁\n- Agent 报告\"参数路径\"时必须附带 registry exp_id 引用，禁止从 handoff 记忆中复制\n\n### 5.3 [HARNESS] Worker dispatch 的脚本复制粘贴反模式 — High\n\n**证据**: M006/M007/M008/M010/M012/M013/M018/M026/M027/M031/M033 共 11 条 — Agent 派 Worker 时复制现有脚本但未修改其中的 path/seed/quantize/CUDA_VISIBLE_DEVICES/max_new_tokens 等关键参数。\n- M006 Wave1 4 个 critical 一起出现（GPU/路径/save_total_limit/DeepSpeed 矛盾）\n- M007/M008 CUDA_VISIBLE_DEVICES 被 ${GPU:-0} 默认值覆盖\n- M010 1.7B RSFT s43/s44 adapter 指向 s42 而非 seed-specific\n- M012 14B eval 沿用 --quantize 违反 D076\n- M026 fair_tax Worker 用 @1024 with-evi（D137 后同类错误）\n- M027 1.7B/4B/8B no-evi eval 用 plan_014 训练 adapter 而非标准 SFT + --no_evidence flag\n- M031 LLaMA RSFT no-evi max_new_tokens=1024 与配对 with-evi 2048 不匹配\n\n**严重程度**: 高。这些错误平均每次浪费 1-10 GPU-h，累计上百小时。\n**改进建议**:\n- 派 Worker 时强制使用 templated config（jinja-style），所有变量参数化\n- 提交前强制 dry-run: ls 验证路径存在 + diff 对比模板 + nvidia-smi 验证 GPU 空闲\n- 建立\"adapter 物理隔离命名规则\": 训练变体用 plan_XXX_ 前缀，与标准 SFT 隔离（M027 prevention 已提出但未落地）\n\n### 5.4 [HARNESS] Cron 回调在 session compaction 后失效 — High\n\n**证据**:\n- M023 14B RSFT train 完成后 cuda:0 空闲 ~17min，Agent 未自动 harvest\n- M025 Agent 空闲 2h+，3 个实验完成未 harvest，3 张 GPU 白等（\"M023 后未根治\"）\n- M020 milestone 触发后 3/4 GPU 空闲近 1h\n- 5-17 / 5-18 期间多个 ESCALATED_TO_HUMAN 与 Agent idle 重叠\n- ralph_loop_timeline.jsonl 中 304 RESET_REQUEST_SENT vs 245 HARD_LIMIT_REACHED 差值 ~60 → 有 60 次 reset 是手动 / cron 触发的\n\n**严重程度**: 高。3 张卡白等 2h ≈ 6 GPU-h 直接损失，叠加 GRPO 阶段意味着 30-50 GPU-h 损失。\n**改进建议**:\n- Agent compaction 后强制重注册所有活跃 cron（heartbeat 机制）\n- 服务端 cron callback 失效检测：cron 触发后 60s 内未收到 Agent reply 则换 channel（urgent_agent_message）\n- Director WAIT 间隔不超 30min\n\n### 5.5 [HARNESS] Reviewer 作为唯一防错层 — High\n\n**证据**: 38 条 mistakes 中至少 11 条 (M002/M003/M008/M012/M013/M017/M026/M027/M032/M036/M037 reverse/M038) 由 Reviewer 拦截/纠正。Reviewer session 累计 18181 分钟（约 303 小时）— 是 Agent (989h) 的 30% 但 errors 是 Agent (784) 的 14% (113)，Agent 错误率 vs Reviewer 错误率高 ~2×。\nReviewer ssh_read_only 6608 次 + tail_training_logs 492 次 → 重度依赖物理验证。Reviewer 平均单 session 1730 minutes — Director 的 ~10×。\n\n**严重程度**: 高。如果 Reviewer 因任何原因（session crash、context overflow）失能，错误将直达 paper。M035 共享 SFT base 缺陷直到 Round 3 才被 Reviewer 发现 → 拖延 2 周。\n**改进建议**:\n- 关键 invariants（ign_f1 ≤ rel_f1, paired protocol 一致性, adapter 路径合规）自动化为 CI 而非靠 Reviewer 人审\n- Agent 端在 update_registry 时自动跑这些 invariants\n- 把 Reviewer 工作量降低到关键 statistical sign-off + adversarial 角色\n\n### 5.6 [HARNESS] Paper Agent hallucination + 缺乏引用 audit — High\n\n**证据**:\n- M003 Related Work 含幻觉引用：E-GRPO (zhao2025egrpo), R1-RE (dai2025r1re), jin2025rl_panacea 不在 literature_map.yaml；KD-DocRE 错误归属 tan2022redocred (Re-DocRED 数据集论文)\n- 修复后才采用 reference-audit skill\n- M036 Paper Agent Table 3/§4.3 GRPO 超参 3 项错误（G=4 vs G=8, lr, batch sizes）—— 论文已编译多版本\n\n**严重程度**: 高。这是论文上 reviewer.md 红线和 director.md 红线被反复强调的根本原因——但执行靠人审。\n**改进建议**:\n- Paper Agent 写引用前强制 grep literature_map.yaml + WebSearch 验证\n- 所有 hyperparameter 表与 registry spec.command 自动 diff，编译前 block\n- 提交 review 前强制运行 reference-audit skill\n\n### 5.7 [MODEL] Agent 的长程一致性 / cross-session memory 失败 — Critical\n\n**证据**:\n- M002 / M017 两次相同的 ign_f1/rel_f1 混淆，相隔 3 天 — Agent 没从 M002 学到\n- M008 / M033 复制粘贴脚本不改路径，相隔 4 天 — 同类错误\n- M026 / D137 已经做了 matched@2048 protocol 升级，Worker 仍用 @1024 with-evi —— 同 session 内的协议没传到下次 worker dispatch\n- 261 次 boot 后，许多关键 invariant（如 \"evidence tax = no_evi - with_evi，负值=evidence helps\"）被反复需要在 task_context/agent.md 中手写提醒\n- 5-15 D050 (pivot 到 analysis paper) → D051 翻转，时间间隔 3 小时但 Director 完全没保留 D050 的思考脉络（说明 session 内记忆也有问题）\n\n**严重程度**: 极高。这不是 prompt 问题（task_context.md 明确写\"ign_f1 ≤ rel_f1 恒成立\"，红线写\"evidence tax 定义统一\"），是模型在新 session 中无法真正\"将这些规则作为 invariant 主动 check\"。\n**改进建议（可触达的部分）**:\n- 把 \"Agent 要内化的 invariants\" 从 markdown 提示降级为代码层的 wrapper：update_registry 调用时自动做 invariant check，违反则拒绝\n- 这是 [MODEL] 的根本问题但可以靠 [HARNESS] 缓解\n\n### 5.8 [HARNESS] 5-17 director_no_response 集群暴露的\"角色 wall time 不对齐\" — Medium\n\n**证据**: 20 ESCALATED_TO_HUMAN + 5 ESCALATED_SILENT，全部 director_no_response。5-17 22:27 ~ 5-18 02:09 有 8 条 escalation 在 4 小时内。Reviewer 在同期连续提 issue 无人响应。\nAgent boot 261 次但 Director boot 仅 27 次 → 8.6:1 — Director session 平均时长是 Agent 的 ~9×（Director 18065 min / 171 sessions = 106 min vs Agent 59349 / 601 = 99 min...）但 ralph_loop max_wall_time 触发频率不一样。Director 26259 turns vs Agent 63353 turns 也表明 Director 节奏更慢。\n\n**严重程度**: 中。在 scaling 高峰期暴露最明显。\n**改进建议**: 给 Director 单独的 idle_timeout（更长）和 wakeup 优先级（urgent_agent_message 触发 Director boot 优先于普通 cron）。\n\n### 5.9 [HARNESS] 实验追溯链（exp → adapter → data → registry）缺乏自动化校验 — High\n\n**证据**:\n- M027 plan_014 训练 adapter 和标准 SFT adapter 路径相似（含 \"no_evidence\" 字样混淆）→ Worker 选错 → 1.7B/4B/8B no-evi eval 全错\n- M035 RSFT seeds 共享 SFT s42 base 缺陷直到 Round 3 才被 Reviewer 追溯 registry 依赖链发现\n- M032 17×→6.5× 修正：因为 k=3 plan_006 entry 没在切换到 k=1 后标记 [SUPERSEDED]\n- M010/M011 误判：因为 1.7B 的 scored data 来源（s42 生成）未在 registry 显式标注 dependency\n\n**严重程度**: 高。直接影响科学结论可信度。\n**改进建议**:\n- registry 每条 experiment 增加显式 dependencies 字段（parent_adapter / source_data / sft_seed）\n- update_registry 时自动校验 dependency graph 完整性\n- 协议切换（k=3→k=1 / @1024→@2048）时自动给旧 entries 加 [SUPERSEDED] 标签\n\n### 5.10 [HARNESS] 缺少自动化 figure/table 与 registry 的一致性校验 — Medium\n\n**证据**:\n- M036 论文 Table 3/§4.3 hyperparameter 与 registry 不一致 → 3 轮 reviewer 反复\n- M032 figure 中 variance compression 17× 含 k=3 数据\n- audit found 62 项发现 3 项 FAIL (F1 DPO 1ep Rel-F1 33.38→33.37 / F2 method.tex EDCR / F3 fig_spectrum caption)\n\n**严重程度**: 中。\n**改进建议**: 论文每个数字标 provenance (registry exp_id + metric path)，编译前自动 diff。\n\n### 5.11 [MODEL] Director \"决策\"过度导致策略震荡 — Medium\n\n**证据**: 159 条 D-编号，平均 1.7 条/小时；其中 D050↔D051 / D061↔D063 / D068↔D069 / D097↔D098 / D118↔D120 / D134↔D135↔D136↔D137 多组连续修正/翻转。M037/M038 三次 G 值 flip-flop。\n\n**严重程度**: 中。每次震荡都需 Agent/Paper Agent 跟进，浪费 token。\n**改进建议**: 任何 reframe 决策强制 \"等 24h cooldown + 多方 sign-off\" 流程，避免 hot decision。\n\n### 5.12 [INFRA] AutoDL 实例不稳定造成的非线性损失 — Medium\n\n**证据**:\n- M019 14B gen 12h、1872/3027 docs 因 bjb2-12179 实例注销而全丢（无 resume 机制）\n- M021 rsync 在迁移中覆盖正在写入的文件，r3 5016 条数据面临丢失（最终从 /proc/PID/fd 抢救）\n- M005 磁盘满崩 4 任务同时挂掉\n- mistakes 多处提到 \"AutoDL 实例重启后 SSH 端口会变\"\n\n**严重程度**: 中。AutoDL 是已知不稳定环境，但项目早期未把 checkpoint/resume 作为强制要求。\n**改进建议**: ssh-env-setup skill 已列了 AutoDL 经验沉淀，但实际 worker 脚本未强制使用增量写盘 + resume。M019 prevention 已提出 \">1h 任务必须有 resume\"，应作为 worker submit 时的 invariant。\n\n### 5.13 [MODEL+HARNESS] CED 核心创新失败但项目\"救出\"论文的能力 — 项目级 Observation\n\n**证据**: 原始 idea 的 make-or-break (CED vs flat-NLI) p=0.44 直接失败；GRPO+CED 也全线失败；但论文最终通过 (1) decoupling spectrum (negative result) + (2) evidence tax scaling 现象学 + (3) RSFT variance compression 救回 Findings 评分 3.0。\n\n**严重程度**: 这不是 problem 而是 observation——agent system 在原始 hypothesis 死亡后能 reframe 出 publishable contribution，体现了一定的\"科研韧性\"。但代价是 3.0 (Findings) 而非主会评分。\n\n**改进建议**: Dream 模拟 (best/median/worst < 3.5) 应作为更早的 abort signal——D050 当时 pivot 到 analysis paper 的判断其实是对的，被 D051 推翻后项目硬着头皮做 Main，最终落到 Findings。Dream gate 应该更有约束力。\n\n### 5.14 [HARNESS] 用户参与窗口与项目 wall-time 不匹配 — Medium\n\n**证据**: 27 条用户消息全部在前 48h，后续 16 天无人工干预。20 ESCALATED_TO_HUMAN 显示系统知道需要升级但未真正触达。M035 / M027 / M032 等如果有人工每周检查一次都可避免。\n\n**严重程度**: 中。\n**改进建议**: 飞书升级机制需要确认实际触达 PI（read receipt）；定期 push 一次\"本周 mistakes + 关键 decision\" 摘要给 PI 即使无 escalation。\n\n---\n\n## 总结\n\nfaith-evidence-ie 是一个**原始 hypothesis 死亡后通过 negative result + 现象学发现\"救出\"的论文**项目。在系统设计层面（[HARNESS]）：\n- session reset 风暴吞噬 25-35% token 预算（5.1）\n- 三方信息冲突时无仲裁机制 → 多次 critical 错误（5.2）\n- Worker dispatch 的复制粘贴反模式 → 11 起同类事故（5.3）\n- Reviewer 作为唯一防错层 + 关键 invariant 未自动化（5.5/5.9）\n- Paper Agent hallucination + 缺乏自动 reference audit（5.6）\n\n在模型能力层面（[MODEL]）：\n- 长程 invariant 维护失败（5.7）：同类错误 (ign_f1/rel_f1 混淆 / 复制粘贴 / 协议升级未传) 间隔数日反复出现\n- Director 过度决策导致策略震荡（5.11）\n\n在科研产出层面：\n- 原始 CED reward + GRPO 路径完全失败但被论文化为 decoupling spectrum（接受）\n- variance compression / capacity threshold 这类\"现象学\"发现是真实的，但 shared SFT base 缺陷削弱了 generalizability claim（M035）\n- Dream 评分 (2.5-3.0) 准确预测了实际审稿评分 (3.0 Findings)，应作为更强的 gate\n\n最严重的改进点不是 GRPO 失败（那是科学结果），而是**Worker dispatch 反模式 + 数值传递 + 协议切换** 三类系统性 bug 拖累了 ~30% 的 GPU 时间和论文叙事的反复返工。\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6ce2e372-7ba5-4509-bd78-884e1f36eb75",
  "isSidechain": false,
  "requestId": "req_011CbaoXPwCNAosqGmdYCRMA",
  "type": "assistant",
  "uuid": "c1c493a1-3fbb-47e7-a715-2136e140953e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/scan_reports",
  "sessionId": "e661bd34-50c6-4b5f-8a72-51f05c33cc2b",
  "version": "2.1.126",
  "gitBranch": "main",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_01K1vk8nMEA3Zsxc5fJ2WGgq",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 350,
      "cache_read_input_tokens": 188705,
      "output_tokens": 18078,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 350,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [],
      "speed": "standard"
    }
  }
}
```

</details>

---


### Tool result

_source line 193 · 2026-05-31T14:32:43.474Z_

<details><summary>↩ Tool result · `toolu_017pNCKjyFbbctwJYXc4Nppz`</summary>

```text
File created successfully at: /home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/scan_reports/layer2_20260531T142125.md
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c1c493a1-3fbb-47e7-a715-2136e140953e",
  "isSidechain": false,
  "promptId": "69e82015-f241-490b-bfaa-188dab1e85c4",
  "type": "user",
  "uuid": "779358e5-8586-4630-b731-2b4b482116f9",
  "toolUseResult": {
    "type": "create",
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/scan_reports/layer2_20260531T142125.md",
    "content": "# faith-evidence-ie — 轨迹分析报告\n\n> 扫描时间: 2026-05-31T14:21:39Z\n> 工作区: /home/ubuntu/.agent-ml-research-idea_gen_0513_6\n\n## 1. 项目概况\n\n**项目**: FREIGE (Faithfulness-Rewarded Evidence-Grounded Information Extraction via Contrastive Evidence Discrimination)，evidence-grounded DocRE 方向。\n**Venue**: EMNLP 2026 Main（ARR July cycle）。Round 2 评分 3.0 (Findings)，扫描时正在准备 Round 3。\n**周期**: 2026-05-14 ~ 2026-05-25（Director 最后一次 boot 5-24，Agent 最后事件 5-25 19:51；Reviewer 最后事件 5-25 04:09），约 11–12 个活跃日。\n**实验规模**: registry 382 条，DONE 379 / PREPARING 3；conclusion 分布 success 247 (65%)、failed 65 (17%)、killed 47 (12%)、negative 23 (6%)。\n**Session/Token**:\n- Agent 601 sessions / 63.3k turns / 29M output tokens / 784 errors（占总错误 53%）\n- Worker 1497 sessions / 92k turns / 36M output tokens / 464 errors\n- Reviewer 105 sessions / 43.8k turns / 18.4M output tokens\n- Director 171 sessions / 26.3k turns / 8.8M output tokens\n- 总 token 98.6M（其中 output 95.5M），错误总数 1491\n- 总 duration 113,042 minutes（约 1884 小时角色累计活跃时间，跨 4 个角色并行运行）\n**论文**: main.tex 编译通过、35 references、PDF 估计 100 页（含 appendix）、4870 KB。3 figures + 多表格、Round 2 三贡献叙事（RSFT+NLI / Decoupling spectrum / Evidence tax landscape + variance compression）。\n**关键控制事件**: 304 RESET_REQUEST_SENT、307 HARD_LIMIT_REACHED、20 ESCALATED_TO_HUMAN（全部 director_no_response）、5 ESCALATED_SILENT、38 条 mistakes、159 条 decisions、Agent 共 261 次 boot。\n\n## 2. 项目叙事重建\n\n项目分为 6 个清晰的阶段：\n\n**阶段 1 — Setup + GRPO 灾难期（5-14）**\n项目从 IDEA_BRIEF 启动，前 6 小时被 SSH 密钥审批阻塞（GPU 分配 4，实际跑 0）。MVP-1 (CED 信号验证) 在 14:00 前通过（margin=0.4827, acc=81.5%）。\n14:00 后进入 GRPO+QLoRA 训练，连续 5 轮失败（D005–D023）：r1 mode collapse / r2 OOM (num_iterations=2 + 4-bit → KL 数值爆炸 step 5 KL=3.7e9, step 15 KL=3.4e11) / r3 KL 爆炸 / r4-5 mode collapse / extract_r3-4 / flatnli_r3-r6 全部 mode collapse。同期用户（PI 孙震）从 17:17 开始问\"实验为什么做不下去\"，Director 给出长 markdown 解释。这一天的 mvp2_grpo_* 实验 = 14+ 条 killed/failed，但是 mode collapse 数据形成了 Claim 2（decoupling spectrum）的核心证据。\n\n**阶段 2 — Pivot 到 RSFT + MVP-2 通过（5-15）**\n凌晨判定 GRPO+QLoRA 全线 FAIL，pivot 到离线 RSFT (D031/D033/D037)。中午 D037 一度错误宣告 RSFT 也\"灾难性失败 rel_f1=0.0483\"，几小时后 D038 撤回（eval bug：50-doc pred vs 12275 gold denominator）。15:00 后 D040 正式过 MVP，进入 research 阶段。下午 Dream v1 (best=2.5/median=3.0/worst=2.5，倒挂) 被识破\"诚实版本得分更高\"，Dream v2 (best=3.0) 仍未达 3.5 目标。决策 D050 提出 pivot 到 \"analysis paper framing\"，D051 当晚因 plan_011 (bf16 GRPO) ckpt-100 rel_f1=0.4549 推翻 pivot 前提：bf16 GRPO 不 forget，QLoRA 才是 catastrophic 的根因 → C2 reframe 为 \"QLoRA-specific artifact\" (D054)。这一天用户共发 14 条飞书消息，全部为简短状态查询或概念问题。\n\n**阶段 3 — Scaling expansion（5-16 ~ 5-19）**\n进入大规模 scaling study：4 个 Qwen scale (1.7B/4B/8B/14B) + LLaMA-3.1-8B cross-family + Re-DocRED cross-dataset。这段期是错误密集期：\n- M002 4B RSFT gain 错误 (+6.1pp→+5.5pp)\n- M003 Paper Agent Related Work 幻觉引用 (E-GRPO, R1-RE, KD-DocRE 误归属)\n- M004 scaling 实验 k=3 vs 论文声明 k=1 不一致 → D102 必须全部重训\n- M005 4 个并行训练磁盘满 → 全崩，GPU 空转数小时\n- M006 Wave1 批量脚本 4 个 critical 问题（GPU/路径/save_total_limit/DeepSpeed 矛盾）\n- M007/M008 CUDA_VISIBLE_DEVICES 被脚本覆盖\n- M010/M011 1.7B RSFT s43/s44 adapter 错误判断 → Worker 自行删除有效输出\n- M012/M013 14B eval 用 --quantize 违反 D076 协议、D112 RSFT 用 QLoRA 引入 confound\n- 5-17 ~ 5-18 凌晨 ESCALATED_TO_HUMAN 集中爆发：8 条 escalation 在 12 小时内（5-17 22:27 ~ 5-18 02:09），原因均为 director_no_response。\n\n**阶段 4 — Methodology corrections（5-20 ~ 5-22）**\nEvidence tax 计算多次返工，是项目最长的\"原地踏步\"期：\n- D127 sign convention 标准化 → M016 子值翻错\n- M017 第 2 次 ign_f1/rel_f1 混淆（LLaMA RSFT s42），导致 D125/D128/paper_framing/ROADMAP/Paper Agent patch 全部受污染\n- D137 确立 matched@2048 协议 → M026 Worker 仍用 @1024 with-evi（D137 同类错误）\n- M027 D140 全部 Qwen no-evi eval 用了 plan_014 的训练 adapter 而非标准 SFT + --no_evidence flag → 1.7B/4B/8B 全部失效\n- M030 fair_tax 计算文件混用 @1024/@2048，导致论文 LLaMA tax 方向错误\n- M031 LLaMA RSFT no-evi cascade 写错 max_new_tokens=1024 与 with-evi 2048 不匹配\n- M032 8B RSFT 方差压缩 17× 混用了 k=3 和 k=1 模型 → 修正为 6.5×\n- M033 Director 级联指令 LLaMA RSFT 三个路径全错 → Worker 重启丢失 302/500 进度（~5h）\n- M034 Registry cleanup Worker 过度删除 ~194 条实验（指令明确要求只加 note）\n- M035 RSFT seed protocol 缺陷：4B/8B/LLaMA 的 RSFT seeds 全部从 SFT s42 出发（共享 base），variance compression claim 的方法论基础有缺陷\n\n**阶段 5 — Round 2 audit + paper polishing（5-23 ~ 5-24）**\nD155 Round 2 (3.0) Action Matrix；D157 数据审计完成 3 项修正；D158 补跑 1.7B s44 和 14B s44 RSFT 全流程消除跨 scale 种子数不一致。\n\n**阶段 6 — QLoRA flip-flop 事故（5-24 ~ 5-25）**\nM037/M038 双向错误 CRITICAL 指令链：\n1. 前 Director session 在 Agent 完成审计前发 CRITICAL G=4→G=8，触发 Paper Agent 8 处论文修改 + 2 张图重画\n2. Agent 审计表用\"实验命名约定\"而非 config 真值，错报 G=4\n3. 新 Director 信任 Agent 审计，发 CRITICAL revert G=8→G=4\n4. Reviewer 用 registry 行号确认 G=8\n5. Director 再发 CRITICAL 恢复 G=8\n\n三次 flip-flop 造成 Paper Agent 大量重复工作。项目最后一次 Director boot 在 5-24 11:16，扫描时项目处于\"等待 Round 3 review\"状态，4 张 GPU 全部空闲。\n\n**关键转折点**:\n- 5-14 18:00 GRPO 失败 → RSFT pivot（被迫，结果支持了 negative finding 的论文化）\n- 5-15 16:32 plan_011 bf16 GRPO 不 forget → Claim 2 从\"RL fails for IE\"重定位为\"QLoRA-specific artifact\" → 后又 generalize 为 \"decoupling spectrum\"\n- 5-18 D078 CED vs flat-NLI p=0.44 → CED 从核心贡献降级\n- 5-21 D137 matched@2048 协议确立 → 大量已有 evidence tax 数据需重新计算\n- 5-22 D144 4B \"capacity valley\" 叙事被 M027 修正完全推翻\n\n**停滞期**: 5-17 ~ 5-18 凌晨（8 次 ESCALATED_TO_HUMAN）、5-20 ~ 5-22（evidence tax methodology 反复返工）。**加速期**: 5-15 下午（pivot 后多卡并行+plan_011 结果推动叙事重构）、5-23（Round 2 Action Matrix 落地）。\n\n## 3. 科研目标达成度分析\n\n### 3.1 Idea → Findings 的逻辑链\n**原始 idea (IDEA_BRIEF)**: 用 GRPO + CED reward 训练 LLM 同时输出 relation triples + 支撑证据；CED 通过 within-document hard negative 解决 NLI faithfulness 的 gameability 问题。Make-or-break 实验是 CED vs flat-NLI ablation，dual publishability threshold：Evi-F1 > 57.34 AND F1 > 53。\n\n**最终论文 (paper_framing 3 贡献)**:\n1. RSFT + NLI-based scoring 有效性\n2. Decoupling spectrum (GRPO catastrophic > DPO gradual > RSFT none)\n3. Evidence tax landscape + variance compression\n\n**Reframe 链**:\n- Reframe #1（被迫）: GRPO 全线失败 → 从 \"online RL CED\" 转向 RSFT (D031/D037)\n- Reframe #2（被迫）: D078 CED vs flat-NLI p=0.44 统计不可区分 → CED 降级为 \"one possible scoring function\"，与 flat-NLI 等效\n- Reframe #3（主动）: bf16 GRPO 不 forget (D051) → 从 \"online RL fails\" 收窄为 \"QLoRA artifact\"，再泛化为 \"decoupling spectrum\"\n- Reframe #4（被迫）: 4B \"capacity valley\" (+7.5pp) 由 M027 adapter 错误造成 → D144 修正为 +0.73pp，capacity valley 叙事完全推翻，C5 重写为 \"within-family threshold\"\n- Reframe #5（被迫）: variance compression 17× → 6.5×（M032 混用 k=3/k=1 数据）\n\n**与原始 idea 的偏离**: 原始 idea 的核心技术 (CED reward in GRPO) 完全失败，论文最终核心是这个失败本身（decoupling spectrum）+ 离线替代 (RSFT) + scaling 现象学（evidence tax landscape）。**论文的核心 claim 与原 hypothesis 关系微弱——CED 作为 reward 的 contrastive insight 在论文中只保留为 RSFT 的 scoring function，与 flat-NLI 不可区分**。从科学价值看，这是一个失败 idea 通过 negative result + 现象学发现救出来的论文。\n\n### 3.2 实验设计的科研严谨性\n\n**Falsifiable 设计**：✅ Make-or-break (D076/D078: CED vs flat-NLI t-test) 设计良好且诚实执行——p=0.44 直接接受 null。Dream 模拟（D043/D047）作为投稿前可证伪 gate。\n**对照 baseline 设计**：☑️ 部分充分。Baselines 12+ 列出，但 plan_004 DREEAM 自己复现，plan_022 第三个模型家族 / plan_023 DocKS-RAG+LMRC 复现都列为 P2 并未完成。所有 RSFT 与 SFT 同 backbone 同 protocol 比较合规。\n**统计方法**：⚠️ 严谨性反复出问题：\n- M002, M017 两次 ign_f1/rel_f1 混淆，污染了 ROADMAP + paper_framing + Paper Agent patch\n- M005 4 个并行训练磁盘满 → seed 1, 2, 3, 4 全崩\n- M035 共享 SFT base 缺陷直到 Round 3 才暴露 → variance compression 由 contribution 降为 observation\n- D118 \"RSFT 1.7B surpasses 8B SFT\" → 修正为 \"approaches\"\n- D155 \"consistently reduces\" 替代 \"substantially reduces\"（sign test p=0.0625 n=4 结构性上限）\n- D146 4B 3-seed mean=+0.25±0.47pp 用 sample std (ddof=1)，被 Director 纠正过一次（agent.md 红线）\n**P-hacking / cherry-picking 倾向**：\n- 4B 主表 n=3（去掉 s45），附录透明报告 n=4（director.md 红线明确禁止把 s45 加回主表）。这是诚实的，但意味着 s45 被排除有偏的可能性\n- evidence tax 在 dev 用 matched@2048 fair subset，test 用全量 500 docs，两套协议不一致（D147 8B dev=+0.04 vs test=-1.71pp 方向不一致）\n- 4B RSFT test tax 唯一正值 (+1.65±0.29)，但 paper 将其框入 \"heterogeneous, scale-dependent\" 框架内（D153 Version B confirmed）\n\n**实验规模**: 5 scales × 多 seed × 多 protocol 已属重量级；shared SFT base 缺陷削弱了 generalizability claim。\n\n### 3.3 Findings 的质量与 Novelty\n- **Original GRPO+CED claim**：已被证伪，但失败本身（QLoRA quantization 在 RL-for-IE 任务上的 catastrophic collapse）+ 跨方法 decoupling spectrum 有发现价值。\n- **RSFT**: 诚实定位为 STaR (NeurIPS 2022) 单轮变体（D076-related），不作为方法贡献。\n- **Evidence tax landscape (C3)**：跨 5 个 scale + 跨 2 个家族的现象学是项目最有 novelty 的发现——但 D144 \"within-family threshold\" 替代 \"capacity valley\" 后，叙事弹性减弱（1.7B 唯一显著获益，4B/8B/14B 都接近 0，threshold 在 1.7B-4B 之间只是 2 点数据）。\n- **Variance compression**：6.5–31× 跨 scale 一致是 striking 数据，但 M035 共享 SFT base 缺陷使其降为 observation。\n- **EDCR**: 方法级 ρ=-0.965 接近完美相关 → D071 自己承认 \"by-construction 混淆\"，per-relation EDCR 独立诊断（ρ_evi_f1=-0.064）救回了价值。\n\n**审稿评分轨迹**:\n- Dream v1 best/median/worst = 2.5/3.0/2.5\n- Dream v2 best/median/worst = 3.0/2.5/2.5\n- Round 1 actual review = 3.0\n- Round 2 actual review = 3.0 (Findings)\n- 项目目标 EMNLP Main (≥4.0) 与实际评分 3.0 (Findings) 之间存在 1.0 分缺口。从科研内容看，原始 CED hypothesis 失败 → 论文重心被迫转移到现象学发现 + negative result framing，这种\"救出来\"的论文在主会的天花板就是 borderline。\n\n### 3.4 研究效率\n**直接贡献最终论文的实验**: 约 247 success 中粗估 ~150 项被论文主表 / appendix 引用（核心 5 scales × {SFT, RSFT, no-evi} × {dev, test} × multi-seed + 关键消融 + DPO/GRPO baseline）。\n**探索性弯路**:\n- GRPO+QLoRA 整个 mvp2_grpo_* 系列约 30+ 实验，~50 GPU-h，绝大多数 failed/killed。但实验本身产出了 Claim 2 的关键 negative result，**作为 negative result 是有价值的弯路**。\n- D102 全 scale k=3→k=1 重训：~40 GPU-h，纯粹因为 M004 早期 scaling 实验偏离 canonical 配置。**纯粹浪费**。\n- D137/M026 matched@2048 协议反复：~30 GPU-h 浪费在 mismatched comparison（@1024 with-evi vs @2048 no-evi）和后续重算。**纯粹浪费**。\n- M027 D140 全部 Qwen no-evi eval 使用错误 adapter：~20 GPU-h，4B/8B killed，1.7B INVALIDATED + D142 narrative reframe 悬空。**纯粹浪费**。\n- M005 磁盘满 4 训练崩溃 + M019 14B 12h gen 内存 only 丢 1872/3027 docs + M021 rsync 删除 r3 的 5016 条数据：**大型基础设施事故**累计 ~40 GPU-h 浪费。\n- M025/M020/M023 Agent 空闲（cron 回调失效）：累计 ~10 张卡时空转。\n- M037/M038 QLoRA G=4↔G=8 flip-flop：Paper Agent 至少 3 轮重复修改 8 处+2 张图。\n\n**粗估**: ~10–15% GPU 时间在 GRPO 探索（产出 negative result，可接受）；~15–20% 在纯粹 methodology / infra 错误（不可接受）。\n\n### 3.5 论文与实际科研的匹配度\n- ⚠️ D147/director.md 标注\"14B 定位为 validation scale (n=2)，论文中 14B 相关 claim 必须用 hedged 语言\"——14B test tax mean=+0.12±0.64pp (n=3 with s44 补全) CI 跨零，论文用 \"neutral/uncertain\"。✅ 诚实。\n- ⚠️ Variance compression claim 在 M035 暴露后降级为 \"observation\"，experiments.tex/method.tex 加 shared SFT base caveat（reviewer.md 红线）。✅ 诚实。\n- ⚠️ \"RSFT 1.7B surpasses 8B SFT\" → \"approaches\"（D118）。✅ 诚实。\n- ⚠️ Abstract/Contributions 用 \"consistently reduces\" 替代 \"substantially reduces\" (D155)，sign test p=0.0625 n=4 是结构性上限。✅ 诚实。\n- ⚠️ M003 Paper Agent Related Work 含幻觉引用 (E-GRPO/R1-RE) + KD-DocRE 误归属为 Re-DocRED 数据集。已 Reviewer 拦截修正。\n- ⚠️ M036 论文 Table 3/§4.3 GRPO hyperparameter 表 3 项错误 (G=4 vs G=8, lr, batch sizes)，导致 3 轮 reviewer 基于错误数据的 confound 分析。\n- ⚠️ M037/M038 G=4↔G=8 flip-flop。\n\n**总体**: 在被发现后的 disclosure 是诚实的；但 (1) 论文中关键数字多次被错误数据驱动（M002/M017/M027/M032/M036），(2) 这些错误的暴露主要靠 Reviewer 而非 Agent 自检。\n\n### 3.6 人工参与分析\n\n**人工参与频率**: 极低且集中。Director session 共记录 **27 条** 用户（PI 孙震）飞书消息，**全部** 集中在 2026-05-14 ~ 2026-05-15（前 48 小时）。5-15 之后 ~16 天的运行无人工干预。\n\n**用户消息性质**:\n- 概念性提问 (10 条): \"证据\"到底是什么、\"是知识图谱吗\"、\"难道这个 idea 只是多了一个维度\"、\"定位句子很难训练吗\"——用户在 5-14 上午对 idea 本身不熟悉，让 Director 反复解释\n- 状态查询 (12 条): \"实验做的怎么样了\"、\"mvp 验证还没过吗？\"（同样问题重复 4 次）、\"还要多久才可以开始写论文\"\n- 战略性消息 (5 条): \"MVP之后需要Dream\"、\"gpu 利用满了吗\"、\"GRPO+QLoRA 全线失败...会有什么影响\"、\"这篇 paper claim 的点是什么\"、\"你把这个 idea 全部都详细的给我说一遍\"\n\n**触发条件**:\n- ESCALATED_TO_HUMAN 20 次 + ESCALATED_SILENT 5 次都是\"director_no_response\"，理论上应该触达用户，但飞书消息只在 5-14/15 出现 → **运维群升级机制可能未真正联通到 PI**，或 PI 不查看升级消息\n- mistakes.yaml 中 `user_intervention` / `user_feedback` 标记: 0 条。M027/M035 等关键事故均由 Agent/Reviewer 自检发现，无人工介入痕迹\n\n**人工参与的影响**:\n- 5-14 GRPO 失败时用户问\"为什么做不下去\"——Director 整理出长解释，**催生了 D031/D033 判死 GRPO+QLoRA 的决心**。如果没有此提问，Director 可能继续刷 GRPO 配置\n- 5-14 18:24 用户\"gpu 利用满了吗？抓紧最大效率跑mvp\"——是 5-15 4 卡并行 RSFT/GRPO/DPO/SFT-no-evidence 同时跑的直接触发\n- 5-15 03:15 用户主动转述\"GRPO+QLoRA 全线失败...会有什么影响\"，相当于把 Director 在 D031 之前的内部判断变成了\"已正式向 PI 通报的状态\"，巩固了 pivot 决策\n- 5-15 06:18/08:48 用户连环追问 claim 是什么 → 触发 paper_framing.md 落地（D040 之后）\n\n**时机评估**: 用户的早期高频参与对论文叙事定型起到关键作用，但 5-15 之后\"放手\"导致 16 天内所有重大方法论错误（M027/M032/M035/M037/M038 等）均无人工把关。**M035 共享 SFT base 这种根本性方法论缺陷，如果在 5-18 scaling 实验设计时由人审一眼就能拦下；让其拖到 Round 3 才暴露，论文已被迫降级为 observation**。\n\n**反事实推理**: 如果 5-14 PI 不质问 GRPO 失败原因，Director 可能再多刷 1-2 天 GRPO 配置，但最终也会判死（Dream v1/v2 会把它逼出来）。如果 5-15 之后 PI 不放手而是周检 1 次，M002/M017 ign_f1/rel_f1 混淆 / M035 shared SFT base 应该可以早 5-10 天发现，evidence tax 章节可以省 ~30 GPU-h 返工。\n\n**Briefer 角色（2 sessions, 1571 minutes, 61 turns）**: 大幅介入但只在项目 boot 时 onboarding 用，不参与 ongoing 决策。\n\n## 4. 角色行为深度分析\n\n### Director（171 sessions, 26.3k turns, 8.8M output tokens, 55 errors）\n\n**做得好**:\n- 决策记录完整（159 条 D-编号），关键 reframe 都留有依据\n- 5-15 同一天内 (Dream v2 失败 → plan_011 反转) 完成两次叙事重构，反应敏捷\n- D076 统一协议 / D102 k=3→k=1 / D137 matched@2048 等 methodology unification 及时落地\n- 用户 5-14 早期提问时给出的解释结构清晰、tradeoff 明确（17:17 长 markdown 复盘）\n\n**问题**:\n- **决策反复**: D050 pivot 到 analysis paper → D051 推翻；D061 关闭 DPO → D063 撤回；D068 修正 DPO 结论 → D069 再修正 → 进入 spectrum 框架。Decision yaml 中至少 12 处后续 D 修正前一个 D 的结论\n- **D-编号膨胀**: 159 条 decision，平均 1.7 条/小时，多数是策略微调而非战略决策。后期（D110+）大量是数据修正而非真正\"决策\"\n- **5-17/5-18 的 director_no_response 集群**: 16 条 ESCALATED_TO_HUMAN 在 36 小时内 → Director session 在关键 RSFT scaling 高峰期 unresponsive，触发 Agent/Reviewer 多次反复升级\n- **M037/M038 flip-flop**: 前 Director session 在 Agent 完成审计前发 CRITICAL → 后 Director session 信任 Agent 错误审计表又 revert → Reviewer 用 registry 行号才确认。**三方信息冲突时未等最可靠来源（registry）**\n- **M033 LLaMA 路径 3 个全错**: 从 handoff 记忆中照搬路径而非从 registry 成功实验复制 → 浪费 ~5h Worker 进度\n- **M002 4B RSFT gain 错误数字未交叉验证就写入 D088/D094/ROADMAP**: 后由 Reviewer 核实纠正\n- **Cron 回调失效（M023/M025）**: Agent 空闲 2h+ 无 harvest，Director 在 WAIT 期间未设短间隔检查\n\n### Main Agent（601 sessions, 63.3k turns, 29M output tokens, 784 errors）\n\n**做得好**:\n- 跨 11 天 261 次 boot 保持基本任务连续性\n- Top tools: update_registry 3161, read_registry 2355, spawn_worker 1662, post_to_director 1139 → Registry-centric workflow\n- 大多数 worker 派发能正常 closure 到 cron callback\n\n**问题**:\n- **Session 不稳定**: 245 HARD_LIMIT_REACHED + 245 RESET_REQUEST_SENT 表示**每 ~6 turns 就触发一次硬性 reset/handoff**。每次 reset 都需要重读 task_context/agent.md（58 行）和大量 memory.md。这是 token 消耗 29M 的主因\n- **Worker 派发错误率高**: mistakes.yaml 中 M006/M007/M008/M010/M012/M013/M018/M026/M027/M028/M029/M031 共 12 条 worker_dispatch / experiment_design 类错误，多数是\"复制粘贴脚本不修改路径/参数\"\n- **自检能力弱**: 大多数错误 (M002/M017/M026/M032 等数值错误) 由 Reviewer 拦截而非 Agent 自检。Agent 报数往往是从 metrics.json 的位置推断而非字段名提取\n- **未授权操作**: M028 Agent 未经审批自行启动 retrain_4b_rsft_ced_s42；M034 Agent 错误执行 registry 批量删除（指令明确\"只加 note 不删除\"），删除 ~194 条\n- **失效 cron 回调（M023/M025）**: Agent compaction 后丢失 cron 注册，连续 2 次出现\n\n### Reviewer（105 sessions, 43.8k turns, 18.4M output tokens, 113 errors）\n\n**做得好**:\n- 是项目的**关键防错层**: M002, M003, M012, M013, M027, M032, M036, M037 reverse, M038 都由 Reviewer 拦截/纠正\n- top tool ssh_read_only 6608 次 → 重度依赖直接验证而非 Agent 转述\n- D076 paired t-test、D078 CED vs flat-NLI 不可区分、bf16 GRPO vs QLoRA quantization isolation (D052) 等关键统计/方法验证都是 Reviewer 主导\n- 9 次 ESCALATED_TO_HUMAN + 高 ssh_read_only 频次 → 在 Director 不响应时仍主动验证\n\n**问题**:\n- **ScheduleWakeup 728 次** → Reviewer 大量时间花在自我唤醒等待，效率不高\n- 27 sessions 文件平均 2.85MB（p90=7.7MB, max=20MB）→ 单 session 时间极长，token 重负\n- **共享 SFT base 缺陷（M035）拖到 Round 3 才发现**: 在 5-18 全 scale RSFT 设计时本应注意到 registry 依赖链问题，Reviewer 早期审查时没追溯\n\n### Worker（1497 sessions, 92k turns, 36M output tokens, 464 errors）\n\n**做得好**:\n- top tools: ssh_read_only 20071, ssh_execute 4037 — 比 1:5 健康\n- 平均每个 worker session 仅 61 turns、6 个 tool uses → 任务定义粒度合理\n\n**问题**:\n- 464 errors（约 31% 错误率，按 1497 sessions 计算）—— 高\n- M005 4 task 同时写 checkpoint 磁盘满崩；M019 14B 12h gen 无 resume 全丢；M021 rsync 覆盖 r3 写入的文件——**3 起重大事故均与 worker 写 IO 设计有关**\n- Resource_misuse 类错误占比高（M005/M009/M018/M020）\n\n### Paper Agent（17 sessions, 8.6k turns, 4M output tokens, 59 errors）\n\n**问题**:\n- M003 Related Work 含幻觉引用 (E-GRPO, R1-RE)，KD-DocRE 误归属为 Re-DocRED 数据集——**LLM 写作典型 hallucinated citation**\n- 多次成为 Director flip-flop 的下游受害者（M036 3 项超参错误重写、M037 8 处修改、M038 reverse）\n- Top tool ToolSearch 111 次 + WebSearch 55 → 大量用于补救引用\n\n### 角色协作摩擦点\n1. **Agent → Director 的数据传递不可靠**: M002/M017 数值错误未交叉验证直接写入 decision；M037 Agent 审计表用实验名命名而非真值\n2. **Director → Agent 的路径/参数传递不可靠**: M027 / M031 / M033 都是 Director 从 handoff 记忆中照搬错误参数\n3. **Director → Paper Agent 的指令缺乏 dry-run 验证**: M036/M037/M038 三次基于错误真值的 CRITICAL 修改\n4. **Reviewer 是事实仲裁者但成本极高**: 单 session 平均 2.85MB / 1730 minutes，是 Director (1.06 hours/session) 的 ~10× 时长\n\n## 5. 关键发现\n\n### 5.1 [HARNESS] Session reset 风暴吞噬主要 token 预算 — Critical\n\n**证据**:\n- Agent 304 RESET_REQUEST_SENT + 245 HARD_LIMIT_REACHED + 261 boot = **每 6-12 turns 就要 reset 一次**\n- Agent output tokens 29M / 63.3k turns = 平均每 turn 458 tokens，但 boot 时需读 task_context/agent.md（58 行）+ memory.md（66 行）+ paper_framing.md（404 行）+ 多次 read_registry/get_project_status\n- 单次 boot 重读约 50-100k tokens 上下文，261 次 boot ≈ 20M+ token 仅用于\"找回状态\"\n- 5-17 ~5-18 凌晨 16 条 ESCALATED_TO_HUMAN 全部在 36h 内 → reset 频率太高导致 Director 无法处理积压消息\n\n**严重程度**: 极高。98.6M 项目总 token 中估计 25-35% 用于 session 恢复。\n**改进建议**:\n- 把 boot 上下文从 \"重读所有 md\" 改为 \"增量 diff\" — 仅读上次 reset 后变更的部分\n- 拉长单 session wall_time 上限（当前 ~360min → ~720min for Director），减少 boot 次数\n- 把 task_context 改为 yaml/json 结构化，让 boot 只读\"机器需要的\"而非\"人类可读的长 markdown\"\n\n### 5.2 [HARNESS] 三方信息（Agent 报告 / Director 指令 / Registry 真值）冲突时无优先级仲裁 — Critical\n\n**证据**:\n- M037 → M038 G=4↔G=8 三次 flip-flop：前 Director (基于 registry hypothesis 字段误读) → Agent 审计表 (基于实验命名约定) → Reviewer (基于 registry 实际 spec L1015/L1048/L3470) → 最后才确认 G=8\n- M002 4B RSFT gain：Agent 报 rel_f1=0.4655 (无法复现) → Director 写入 D088/D094/ROADMAP → 后 Reviewer 核实纠正\n- M017 LLaMA RSFT s42 ign_f1=0.5839 (实为 rel_f1) → 污染 D125 evidence tax 计算 / D128 3-seed 统计 / paper_framing / ROADMAP / Paper Agent patch\n- M027 Worker adapter 路径错误 → D140 1.7B/4B/8B 全部失效 + D142 reframe 悬空\n- M033 Director 级联指令 LLaMA 3 个路径全错 → Worker 自动修正但丢失 5h 进度\n\n**严重程度**: 极高。每个事故造成 5-50 GPU-h 浪费 + Paper Agent 多轮重做。\n**改进建议**:\n- 数值类报告强制结构化校验: ign_f1 < rel_f1 (DocRED 上恒成立) → invariant check\n- 任何写入 decision 的数值必须 hash 到 registry source-of-truth，自动验证\n- Critical 指令发出前自动锁住相关 decision，Reviewer 不 sign-off 不解锁\n- Agent 报告\"参数路径\"时必须附带 registry exp_id 引用，禁止从 handoff 记忆中复制\n\n### 5.3 [HARNESS] Worker dispatch 的脚本复制粘贴反模式 — High\n\n**证据**: M006/M007/M008/M010/M012/M013/M018/M026/M027/M031/M033 共 11 条 — Agent 派 Worker 时复制现有脚本但未修改其中的 path/seed/quantize/CUDA_VISIBLE_DEVICES/max_new_tokens 等关键参数。\n- M006 Wave1 4 个 critical 一起出现（GPU/路径/save_total_limit/DeepSpeed 矛盾）\n- M007/M008 CUDA_VISIBLE_DEVICES 被 ${GPU:-0} 默认值覆盖\n- M010 1.7B RSFT s43/s44 adapter 指向 s42 而非 seed-specific\n- M012 14B eval 沿用 --quantize 违反 D076\n- M026 fair_tax Worker 用 @1024 with-evi（D137 后同类错误）\n- M027 1.7B/4B/8B no-evi eval 用 plan_014 训练 adapter 而非标准 SFT + --no_evidence flag\n- M031 LLaMA RSFT no-evi max_new_tokens=1024 与配对 with-evi 2048 不匹配\n\n**严重程度**: 高。这些错误平均每次浪费 1-10 GPU-h，累计上百小时。\n**改进建议**:\n- 派 Worker 时强制使用 templated config（jinja-style），所有变量参数化\n- 提交前强制 dry-run: ls 验证路径存在 + diff 对比模板 + nvidia-smi 验证 GPU 空闲\n- 建立\"adapter 物理隔离命名规则\": 训练变体用 plan_XXX_ 前缀，与标准 SFT 隔离（M027 prevention 已提出但未落地）\n\n### 5.4 [HARNESS] Cron 回调在 session compaction 后失效 — High\n\n**证据**:\n- M023 14B RSFT train 完成后 cuda:0 空闲 ~17min，Agent 未自动 harvest\n- M025 Agent 空闲 2h+，3 个实验完成未 harvest，3 张 GPU 白等（\"M023 后未根治\"）\n- M020 milestone 触发后 3/4 GPU 空闲近 1h\n- 5-17 / 5-18 期间多个 ESCALATED_TO_HUMAN 与 Agent idle 重叠\n- ralph_loop_timeline.jsonl 中 304 RESET_REQUEST_SENT vs 245 HARD_LIMIT_REACHED 差值 ~60 → 有 60 次 reset 是手动 / cron 触发的\n\n**严重程度**: 高。3 张卡白等 2h ≈ 6 GPU-h 直接损失，叠加 GRPO 阶段意味着 30-50 GPU-h 损失。\n**改进建议**:\n- Agent compaction 后强制重注册所有活跃 cron（heartbeat 机制）\n- 服务端 cron callback 失效检测：cron 触发后 60s 内未收到 Agent reply 则换 channel（urgent_agent_message）\n- Director WAIT 间隔不超 30min\n\n### 5.5 [HARNESS] Reviewer 作为唯一防错层 — High\n\n**证据**: 38 条 mistakes 中至少 11 条 (M002/M003/M008/M012/M013/M017/M026/M027/M032/M036/M037 reverse/M038) 由 Reviewer 拦截/纠正。Reviewer session 累计 18181 分钟（约 303 小时）— 是 Agent (989h) 的 30% 但 errors 是 Agent (784) 的 14% (113)，Agent 错误率 vs Reviewer 错误率高 ~2×。\nReviewer ssh_read_only 6608 次 + tail_training_logs 492 次 → 重度依赖物理验证。Reviewer 平均单 session 1730 minutes — Director 的 ~10×。\n\n**严重程度**: 高。如果 Reviewer 因任何原因（session crash、context overflow）失能，错误将直达 paper。M035 共享 SFT base 缺陷直到 Round 3 才被 Reviewer 发现 → 拖延 2 周。\n**改进建议**:\n- 关键 invariants（ign_f1 ≤ rel_f1, paired protocol 一致性, adapter 路径合规）自动化为 CI 而非靠 Reviewer 人审\n- Agent 端在 update_registry 时自动跑这些 invariants\n- 把 Reviewer 工作量降低到关键 statistical sign-off + adversarial 角色\n\n### 5.6 [HARNESS] Paper Agent hallucination + 缺乏引用 audit — High\n\n**证据**:\n- M003 Related Work 含幻觉引用：E-GRPO (zhao2025egrpo), R1-RE (dai2025r1re), jin2025rl_panacea 不在 literature_map.yaml；KD-DocRE 错误归属 tan2022redocred (Re-DocRED 数据集论文)\n- 修复后才采用 reference-audit skill\n- M036 Paper Agent Table 3/§4.3 GRPO 超参 3 项错误（G=4 vs G=8, lr, batch sizes）—— 论文已编译多版本\n\n**严重程度**: 高。这是论文上 reviewer.md 红线和 director.md 红线被反复强调的根本原因——但执行靠人审。\n**改进建议**:\n- Paper Agent 写引用前强制 grep literature_map.yaml + WebSearch 验证\n- 所有 hyperparameter 表与 registry spec.command 自动 diff，编译前 block\n- 提交 review 前强制运行 reference-audit skill\n\n### 5.7 [MODEL] Agent 的长程一致性 / cross-session memory 失败 — Critical\n\n**证据**:\n- M002 / M017 两次相同的 ign_f1/rel_f1 混淆，相隔 3 天 — Agent 没从 M002 学到\n- M008 / M033 复制粘贴脚本不改路径，相隔 4 天 — 同类错误\n- M026 / D137 已经做了 matched@2048 protocol 升级，Worker 仍用 @1024 with-evi —— 同 session 内的协议没传到下次 worker dispatch\n- 261 次 boot 后，许多关键 invariant（如 \"evidence tax = no_evi - with_evi，负值=evidence helps\"）被反复需要在 task_context/agent.md 中手写提醒\n- 5-15 D050 (pivot 到 analysis paper) → D051 翻转，时间间隔 3 小时但 Director 完全没保留 D050 的思考脉络（说明 session 内记忆也有问题）\n\n**严重程度**: 极高。这不是 prompt 问题（task_context.md 明确写\"ign_f1 ≤ rel_f1 恒成立\"，红线写\"evidence tax 定义统一\"），是模型在新 session 中无法真正\"将这些规则作为 invariant 主动 check\"。\n**改进建议（可触达的部分）**:\n- 把 \"Agent 要内化的 invariants\" 从 markdown 提示降级为代码层的 wrapper：update_registry 调用时自动做 invariant check，违反则拒绝\n- 这是 [MODEL] 的根本问题但可以靠 [HARNESS] 缓解\n\n### 5.8 [HARNESS] 5-17 director_no_response 集群暴露的\"角色 wall time 不对齐\" — Medium\n\n**证据**: 20 ESCALATED_TO_HUMAN + 5 ESCALATED_SILENT，全部 director_no_response。5-17 22:27 ~ 5-18 02:09 有 8 条 escalation 在 4 小时内。Reviewer 在同期连续提 issue 无人响应。\nAgent boot 261 次但 Director boot 仅 27 次 → 8.6:1 — Director session 平均时长是 Agent 的 ~9×（Director 18065 min / 171 sessions = 106 min vs Agent 59349 / 601 = 99 min...）但 ralph_loop max_wall_time 触发频率不一样。Director 26259 turns vs Agent 63353 turns 也表明 Director 节奏更慢。\n\n**严重程度**: 中。在 scaling 高峰期暴露最明显。\n**改进建议**: 给 Director 单独的 idle_timeout（更长）和 wakeup 优先级（urgent_agent_message 触发 Director boot 优先于普通 cron）。\n\n### 5.9 [HARNESS] 实验追溯链（exp → adapter → data → registry）缺乏自动化校验 — High\n\n**证据**:\n- M027 plan_014 训练 adapter 和标准 SFT adapter 路径相似（含 \"no_evidence\" 字样混淆）→ Worker 选错 → 1.7B/4B/8B no-evi eval 全错\n- M035 RSFT seeds 共享 SFT s42 base 缺陷直到 Round 3 才被 Reviewer 追溯 registry 依赖链发现\n- M032 17×→6.5× 修正：因为 k=3 plan_006 entry 没在切换到 k=1 后标记 [SUPERSEDED]\n- M010/M011 误判：因为 1.7B 的 scored data 来源（s42 生成）未在 registry 显式标注 dependency\n\n**严重程度**: 高。直接影响科学结论可信度。\n**改进建议**:\n- registry 每条 experiment 增加显式 dependencies 字段（parent_adapter / source_data / sft_seed）\n- update_registry 时自动校验 dependency graph 完整性\n- 协议切换（k=3→k=1 / @1024→@2048）时自动给旧 entries 加 [SUPERSEDED] 标签\n\n### 5.10 [HARNESS] 缺少自动化 figure/table 与 registry 的一致性校验 — Medium\n\n**证据**:\n- M036 论文 Table 3/§4.3 hyperparameter 与 registry 不一致 → 3 轮 reviewer 反复\n- M032 figure 中 variance compression 17× 含 k=3 数据\n- audit found 62 项发现 3 项 FAIL (F1 DPO 1ep Rel-F1 33.38→33.37 / F2 method.tex EDCR / F3 fig_spectrum caption)\n\n**严重程度**: 中。\n**改进建议**: 论文每个数字标 provenance (registry exp_id + metric path)，编译前自动 diff。\n\n### 5.11 [MODEL] Director \"决策\"过度导致策略震荡 — Medium\n\n**证据**: 159 条 D-编号，平均 1.7 条/小时；其中 D050↔D051 / D061↔D063 / D068↔D069 / D097↔D098 / D118↔D120 / D134↔D135↔D136↔D137 多组连续修正/翻转。M037/M038 三次 G 值 flip-flop。\n\n**严重程度**: 中。每次震荡都需 Agent/Paper Agent 跟进，浪费 token。\n**改进建议**: 任何 reframe 决策强制 \"等 24h cooldown + 多方 sign-off\" 流程，避免 hot decision。\n\n### 5.12 [INFRA] AutoDL 实例不稳定造成的非线性损失 — Medium\n\n**证据**:\n- M019 14B gen 12h、1872/3027 docs 因 bjb2-12179 实例注销而全丢（无 resume 机制）\n- M021 rsync 在迁移中覆盖正在写入的文件，r3 5016 条数据面临丢失（最终从 /proc/PID/fd 抢救）\n- M005 磁盘满崩 4 任务同时挂掉\n- mistakes 多处提到 \"AutoDL 实例重启后 SSH 端口会变\"\n\n**严重程度**: 中。AutoDL 是已知不稳定环境，但项目早期未把 checkpoint/resume 作为强制要求。\n**改进建议**: ssh-env-setup skill 已列了 AutoDL 经验沉淀，但实际 worker 脚本未强制使用增量写盘 + resume。M019 prevention 已提出 \">1h 任务必须有 resume\"，应作为 worker submit 时的 invariant。\n\n### 5.13 [MODEL+HARNESS] CED 核心创新失败但项目\"救出\"论文的能力 — 项目级 Observation\n\n**证据**: 原始 idea 的 make-or-break (CED vs flat-NLI) p=0.44 直接失败；GRPO+CED 也全线失败；但论文最终通过 (1) decoupling spectrum (negative result) + (2) evidence tax scaling 现象学 + (3) RSFT variance compression 救回 Findings 评分 3.0。\n\n**严重程度**: 这不是 problem 而是 observation——agent system 在原始 hypothesis 死亡后能 reframe 出 publishable contribution，体现了一定的\"科研韧性\"。但代价是 3.0 (Findings) 而非主会评分。\n\n**改进建议**: Dream 模拟 (best/median/worst < 3.5) 应作为更早的 abort signal——D050 当时 pivot 到 analysis paper 的判断其实是对的，被 D051 推翻后项目硬着头皮做 Main，最终落到 Findings。Dream gate 应该更有约束力。\n\n### 5.14 [HARNESS] 用户参与窗口与项目 wall-time 不匹配 — Medium\n\n**证据**: 27 条用户消息全部在前 48h，后续 16 天无人工干预。20 ESCALATED_TO_HUMAN 显示系统知道需要升级但未真正触达。M035 / M027 / M032 等如果有人工每周检查一次都可避免。\n\n**严重程度**: 中。\n**改进建议**: 飞书升级机制需要确认实际触达 PI（read receipt）；定期 push 一次\"本周 mistakes + 关键 decision\" 摘要给 PI 即使无 escalation。\n\n---\n\n## 总结\n\nfaith-evidence-ie 是一个**原始 hypothesis 死亡后通过 negative result + 现象学发现\"救出\"的论文**项目。在系统设计层面（[HARNESS]）：\n- session reset 风暴吞噬 25-35% token 预算（5.1）\n- 三方信息冲突时无仲裁机制 → 多次 critical 错误（5.2）\n- Worker dispatch 的复制粘贴反模式 → 11 起同类事故（5.3）\n- Reviewer 作为唯一防错层 + 关键 invariant 未自动化（5.5/5.9）\n- Paper Agent hallucination + 缺乏自动 reference audit（5.6）\n\n在模型能力层面（[MODEL]）：\n- 长程 invariant 维护失败（5.7）：同类错误 (ign_f1/rel_f1 混淆 / 复制粘贴 / 协议升级未传) 间隔数日反复出现\n- Director 过度决策导致策略震荡（5.11）\n\n在科研产出层面：\n- 原始 CED reward + GRPO 路径完全失败但被论文化为 decoupling spectrum（接受）\n- variance compression / capacity threshold 这类\"现象学\"发现是真实的，但 shared SFT base 缺陷削弱了 generalizability claim（M035）\n- Dream 评分 (2.5-3.0) 准确预测了实际审稿评分 (3.0 Findings)，应作为更强的 gate\n\n最严重的改进点不是 GRPO 失败（那是科学结果），而是**Worker dispatch 反模式 + 数值传递 + 协议切换** 三类系统性 bug 拖累了 ~30% 的 GPU 时间和论文叙事的反复返工。\n",
    "structuredPatch": [],
    "originalFile": null,
    "userModified": false
  },
  "sourceToolAssistantUUID": "c1c493a1-3fbb-47e7-a715-2136e140953e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/scan_reports",
  "sessionId": "e661bd34-50c6-4b5f-8a72-51f05c33cc2b",
  "version": "2.1.126",
  "gitBranch": "main"
}
```

</details>

---


### Runtime record

_source line 194_

```json
{
  "type": "last-prompt",
  "lastPrompt": "执行项目轨迹扫描，将报告写入 /home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/scan_reports/layer2_20260531T142125.md",
  "leafUuid": "779358e5-8586-4630-b731-2b4b482116f9",
  "sessionId": "e661bd34-50c6-4b5f-8a72-51f05c33cc2b"
}
```

---


### Tool call

_source line 195 · 2026-05-31T14:32:47.851Z_

<details open><summary>🔧 Tool call — TodoWrite · `toolu_01AzxURnTFACSZoem4P5DSe1`</summary>

```json
{
  "todos": [
    {
      "content": "Read knowledge files",
      "activeForm": "Reading knowledge files",
      "status": "completed"
    },
    {
      "content": "Read registry/timeline",
      "activeForm": "Reading registry/timeline",
      "status": "completed"
    },
    {
      "content": "Inventory session transcripts",
      "activeForm": "Inventorying transcripts",
      "status": "completed"
    },
    {
      "content": "Deep-dive transcripts for key signals",
      "activeForm": "Deep-diving transcripts",
      "status": "completed"
    },
    {
      "content": "Write layer2 analysis report",
      "activeForm": "Writing report",
      "status": "completed"
    }
  ]
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "779358e5-8586-4630-b731-2b4b482116f9",
  "isSidechain": false,
  "requestId": "req_011CbaowSfKrfwDWfuydNnkz",
  "type": "assistant",
  "uuid": "61b578a7-bfdb-4d66-a8fb-26665747dae5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/scan_reports",
  "sessionId": "e661bd34-50c6-4b5f-8a72-51f05c33cc2b",
  "version": "2.1.126",
  "gitBranch": "main",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_01RtCE1SHWExt2asS31tFFvT",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 18157,
      "cache_read_input_tokens": 189055,
      "output_tokens": 270,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 18157,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [],
      "speed": "standard"
    }
  }
}
```

</details>

---


### Tool result

_source line 196 · 2026-05-31T14:32:47.916Z_

<details><summary>↩ Tool result · `toolu_01AzxURnTFACSZoem4P5DSe1`</summary>

```text
Todos have been modified successfully. Ensure that you continue to use the todo list to track your progress. Please proceed with the current tasks if applicable
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "61b578a7-bfdb-4d66-a8fb-26665747dae5",
  "isSidechain": false,
  "promptId": "69e82015-f241-490b-bfaa-188dab1e85c4",
  "type": "user",
  "uuid": "f5d14edb-7696-4e19-b8fb-a86a9b9d2c39",
  "toolUseResult": {
    "oldTodos": [
      {
        "content": "Read knowledge files",
        "status": "completed",
        "activeForm": "Reading knowledge files"
      },
      {
        "content": "Read registry/timeline",
        "status": "completed",
        "activeForm": "Reading registry/timeline"
      },
      {
        "content": "Inventory session transcripts",
        "status": "completed",
        "activeForm": "Inventorying transcripts"
      },
      {
        "content": "Deep-dive transcripts for key signals",
        "status": "completed",
        "activeForm": "Deep-diving transcripts"
      },
      {
        "content": "Write layer2 analysis report",
        "status": "in_progress",
        "activeForm": "Writing report"
      }
    ],
    "newTodos": [
      {
        "content": "Read knowledge files",
        "status": "completed",
        "activeForm": "Reading knowledge files"
      },
      {
        "content": "Read registry/timeline",
        "status": "completed",
        "activeForm": "Reading registry/timeline"
      },
      {
        "content": "Inventory session transcripts",
        "status": "completed",
        "activeForm": "Inventorying transcripts"
      },
      {
        "content": "Deep-dive transcripts for key signals",
        "status": "completed",
        "activeForm": "Deep-diving transcripts"
      },
      {
        "content": "Write layer2 analysis report",
        "status": "completed",
        "activeForm": "Writing report"
      }
    ],
    "verificationNudgeNeeded": false
  },
  "sourceToolAssistantUUID": "61b578a7-bfdb-4d66-a8fb-26665747dae5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/scan_reports",
  "sessionId": "e661bd34-50c6-4b5f-8a72-51f05c33cc2b",
  "version": "2.1.126",
  "gitBranch": "main"
}
```

</details>

---


### Assistant

_source line 197 · 2026-05-31T14:33:00.720Z_

报告已写入 `/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/scan_reports/layer2_20260531T142125.md`。

核心结论：
- **项目是"救出来"的论文**——原始 CED+GRPO hypothesis 完全失败（D078 p=0.44 / GRPO 全线 catastrophic forgetting），最终通过 decoupling spectrum (negative result) + evidence tax 现象学 + variance compression 拿到 Round 2 评分 3.0 (Findings)。
- **最严重的 HARNESS 问题**: (1) Session reset 风暴吞噬 25-35% token 预算，261 次 Agent boot；(2) 三方信息（Agent 报告 / Director 指令 / Registry 真值）冲突时无优先级仲裁，典型事故 M037/M038 的 G=4↔G=8 三次 flip-flop；(3) Worker dispatch 的脚本复制粘贴反模式，11 起同类事故 (M006-M033)；(4) Reviewer 是唯一防错层，~11 条关键错误靠人审拦截。
- **MODEL 边界**: Agent 长程 invariant 维护失败——ign_f1/rel_f1 混淆 (M002→M017) 和 adapter 路径复制粘贴 (M008→M033) 这类同类错误间隔数日反复出现，红线在 task_context 提示但模型未真正内化。
- **人工参与极不均匀**: 27 条用户消息全部在前 48 小时（前 48h vs 后 16 天 0），M035 共享 SFT base 缺陷如果有周检本可早 2 周发现。20 ESCALATED_TO_HUMAN 显示升级机制未真正触达 PI。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f5d14edb-7696-4e19-b8fb-a86a9b9d2c39",
  "isSidechain": false,
  "requestId": "req_011CbaowmcbUSp6ca6x59HLk",
  "type": "assistant",
  "uuid": "bfd064f9-3c0e-4225-9527-6916d6ab672e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/scan_reports",
  "sessionId": "e661bd34-50c6-4b5f-8a72-51f05c33cc2b",
  "version": "2.1.126",
  "gitBranch": "main",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_01Qy5P98WuWF8pqfjA5KG3QJ",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 328,
      "cache_read_input_tokens": 207212,
      "output_tokens": 623,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 328,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [],
      "speed": "standard"
    }
  }
}
```

</details>

---


### Runtime record

_source line 198_

```json
{
  "type": "last-prompt",
  "lastPrompt": "执行项目轨迹扫描，将报告写入 /home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/scan_reports/layer2_20260531T142125.md",
  "leafUuid": "bfd064f9-3c0e-4225-9527-6916d6ab672e",
  "sessionId": "e661bd34-50c6-4b5f-8a72-51f05c33cc2b"
}
```

---
