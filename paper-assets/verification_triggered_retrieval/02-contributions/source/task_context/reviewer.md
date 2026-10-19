---
loop: 1
reason: max_wall_time
updated: '2026-05-17T10:15:37+00:00'
---

### 1. 🔴 硬约束 / 红线
- 项目已 KILLED (D002)，不得启动新实验或占用 GPU
- westd-46807 cuda:0 待释放，确认无残留进程后通知 Director 释放资源
- 如果 Director 要求 pivot 到新方向，需重新立项，不能在本项目 registry 下继续注册实验

### 2. 🖥️ 基础设施快照
- 服务器：westd-46807 (RTX PRO 6000 95GB)，工作目录 `/root/verification_triggered_retrieval/`
- 数据：`/root/autodl-tmp/data/` (hotpotqa_dev_200.json, musique_dev_200.json)
- 模型：`/root/autodl-tmp/models/` (Qwen3-8B, bge-base-en-v1.5, nli-deberta-v3-large)
- Wikipedia index：`/root/autodl-tmp/wiki_corpus/lucene_index` (19GB, ~21M passages BM25)
- HF cache：`/root/autodl-tmp/huggingface/`
- 活跃进程：无（实验已全部完成，GPU 空闲）
- 实验输出：mvp_001 → `mvp_experiment/outputs/`，mvp_002 → `mvp_experiment_v2/outputs/`

### 3. 📊 当前状态
项目终结。两轮 MVP 均完成，ROADMAP 已更新为 KILLED 状态。
- mvp_001: DONE (negative, distractor corpus 无区分力)
- mvp_002: DONE (KILL, Wikipedia-scale 反向显著 p=0.005)
- 无 RUNNING/PREPARING 实验，无等待中的 Worker/Cron/Director 决策

### 4. 📋 待办
- Director 确认释放 GPU → 通知 Manager 回收 westd-46807 cuda:0
- Director 要求写跨项目教训 → 检查 `ml-experiment-guide.skill.md` 是否已有类似条目，补充"领域迁移假设需先验证前提条件匹配"教训
- Director 要求 pivot → 需全新立项，不在本项目下续做

### 5. 🎯 战略上下文
- D001: mvp_001 FAIL 但未 kill（我指出 ~2000 passage corpus 中 entity matching 主导，两种 query 返回相同文档，实验缺 discriminative power）
- D002: mvp_002 Wikipedia-scale 确认 kill（overlap 降到 53%证明有区分力，但 verification 显著更差 -3.28pp p=0.005）
- 根因：assertion-form queries 在 BM25 上引入 noise tokens（日期/地名），multi-hop CoT 产生的复杂 claims ≠ FEVER 短 claims
- 易错点：如果有人想 salvage "换 dense retrieval 再试"——注意 IDEA_BRIEF 的核心 claim 是"query formulation matters at verification moments"，BM25 是对 surface form 最敏感的 retriever，连 BM25 都反向显著，dense retrieval 上 formulation 的影响只会更小而非更大
