---
loop: 1
reason: max_messages
updated: '2026-05-17T10:15:39+00:00'
---

### 1. 🔴 硬约束 / 红线
- 项目已归档（phase=archived），不得启动任何新实验或恢复 session
- westd-46807 cuda:0 是唯一曾分配的 GPU，westd-34142 从未在本项目白名单内
- 核心假设已被决定性反驳（D002），不可在同一 framing 下继续实验

### 2. 🖥️ 基础设施快照
- 服务器：westd-46807（已归档，可能已被回收）
- 工作目录：/root/verification_triggered_retrieval/
- 数据：/root/autodl-tmp/data/hotpotqa_dev_200.json, musique_dev_200.json
- Wikipedia index：/root/autodl-tmp/ 下 BM25 index (~19GB)
- 模型：Qwen3-8B, BGE-base-en-v1.5, DeBERTa-v3-large（本地缓存）
- 活跃进程：无（archive_project 已清理所有 session/worker/cron）

### 3. 📊 当前状态
项目完全终结。刚执行 archive_project，所有 cleanup 成功。
- mvp_001: DONE (FAIL, distractor corpus)
- mvp_002: DONE (KILL, Wikipedia-scale actively refuted)
- Registry 无 RUNNING/PREPARING 实验
- 无等待中的回调/决策

### 4. 📋 待办
- N/A（项目已归档，无后续动作）
- 如用户想在 retrieval-for-reasoning 方向继续 → 需另开新项目，不可复活本项目

### 5. 🎯 战略上下文
- D001: mvp_001 FAIL 但不 kill（corpus 太小无区分力）→ 追加 Wikipedia pilot
- D002: mvp_002 KILL（Wikipedia 21M passages 上 verification queries 显著更差 -3.28pp p=0.005）
- 根因：multi-hop CoT claims 长而复杂，assertion-form 在 BM25 上引入 noise tokens（日期/地名等），检索偏向表面匹配。FEVER claim-as-query 有效的前提（short claims + targeted corpus）不成立
- 教训（跨项目价值）：领域迁移假设必须先验证前提条件是否匹配；BM25 对 query 长度/表面形式高度敏感
- 易错：不要试图用 dense-only retrieval "救" 这个方向——原 IDEA_BRIEF 明确声称 BM25 应最受益，结果恰恰相反
