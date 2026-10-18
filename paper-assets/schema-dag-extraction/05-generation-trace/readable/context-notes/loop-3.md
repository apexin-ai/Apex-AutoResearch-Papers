# director / loop_3.md

**How Does Schema Complexity Predict Performance in Training-Free LLM Information Extraction?** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/director/loop_3.md`
- **Structured JSON:** [`27992c414a99caab58d7.json`](../../sessions/27/27992c414a99caab58d7.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 3
reason: max_messages
updated: '2026-05-15T16:17:47+00:00'
---

### 1. 🔴 硬约束 / 红线
- 本项目只有 cqa1-38874 的 cuda:0（1× RTX PRO 6000 Blackwell 98GB），严禁使用其他 GPU
- exp-012 LLaMA 多模型验证已失败两轮（r1 flashinfer 不兼容 Blackwell, r2 也 failed），当前 r3 在跑，AWQ 量化方案是备选——不要再尝试原始 FP16/BF16 加载 70B 模型
- Claim 3（SDGD）已正式放弃（D019），不要再投 GPU 做 exp-008/009/010/011/013/014，只作为 negative result + future work
- ARR May 25 DDL（距今 10 天），所有决策以此为硬约束
- 弹性 GPU 未启用，需要加卡走 `director_post_to_manager` 申请

### 2. 🖥️ 基础设施快照
- 服务器：cqa1-38874 (connect.cqa1.seetacloud.com)，账号 root
- 工作目录：`/root/schema-dag-extraction`
- GPU：1× RTX PRO 6000 Blackwell (98GB)，cuda:0
- Python/conda：未明确记录（aml-train 镜像，Agent 连接后自动检测）
- W&B：未配置
- 活跃实验进程：
  - `exp_fewrel_40rel` — RUNNING（40-rel 中间点，补强 scaling curve）
  - `exp012_llama_fewnerd_r3` — RUNNING（LLaMA 多模型第三次尝试）
- 待处理：exp012_llama_awq（AWQ 量化方案）、exp012_llama_8b（8B fallback）

### 3. 📊 当前状态
- **刚做完**：启动 Paper Agent Full Draft (D020)，SDGD 正式放弃 (D019)，40-rel 中间点升 P0 (D021)
- **RUNNING**：exp_fewrel_40rel + exp012_llama_fewnerd_r3（共占 cuda:0，可能串行）
- **Paper Agent**：Full Draft pipeline 已启动（首次 session），等待产出 writing_plan.yaml
- **等待中**：
  - Agent 文献检索（25+ refs）交付 Paper Agent
  - exp_fewrel_40rel 完成 → 录入 registry → Patch 进论文
  - exp-012 系列结果 → 决定多模型 claim 强度
- **审稿阶段已激活**：review_chat_id = `oc_ac7ab7270b6b5caecee04f89b11aab3e`，Group C 独立处理
- **Dream 两轮均 Weak Reject**，主因写作质量（related work / effect size / metric），已作为 Paper Agent 约束
- **Agent 队列**：空闲（depth=0, idle 40s）

### 4. 📋 待办（条件触发式）
- exp_fewrel_40rel 完成 → 录入 registry，分析 scaling curve 中间点是否补强证据 → Patch 进论文
- exp012_llama_fewnerd_r3 完成 → 若成功：录入 registry，多模型 claim 成立；若失败 → 启动 AWQ 方案（exp012_llama_awq）
- exp012_llama_awq 也失败 → 尝试 8B fallback（exp012_llama_8b），或 acknowledge single-model limitation
- Paper Agent 产出 writing_plan.yaml → 审批（检查 claim 方向 / 章节 / 投稿目标对齐）
- Paper Agent Full Draft 完成 → Reviewer 对抗循环
- 两个 RUNNING 实验都完成后 GPU 空闲 → 立即派 P1 候选（40-rel 补点 / 其他 ablation），禁止空卡

### 5. 🎯 战略上下文
- **核心结论**：type confusability 独立于 type count 驱动 training-free LLM IE 质量下降。Multi-channel degradation model: count→recall, confusability→type confusion。三任务验证完成（Few-NERD ✓, FewRel 80-rel ✓, MAVEN ✓）
- **论文定位**：2-claim analysis paper（Claim 1: confusability independence, Claim 2: multi-channel mechanism）+ SDGD negative result as future work。目标 EMNLP 2026 via ARR May 25
- **决策链关键节点**：D012（证据层级重排：pairwise SCS→confusion 为主证据）→ D013（narrative 精化）→ D014/D019（SDGD 放弃）→ D017（Reviewer 调整实验矩阵）→ D020（启动写作）→ D021（40-rel 升 P0）
- **最容易判断错的事**：
  1. exp-012 LLaMA 已失败两轮，Blackwell GPU 兼容性是主因，不要假设常规方法能加载 70B——必须走 AWQ 量化
  2. Dream 两轮 Weak Reject 不代表方向有问题，是写作质量问题（related work 薄、effect size 未量化、metric 选择未论证），Paper Agent 已知这些约束
  3. per-type BCS 在 MAVEN 上是正向的（exp004_maven_bcs negative），因为 FrameNet hierarchy 的 centrality confound——不要用 per-type 作为 MAVEN 主证据，用 pairwise


---
