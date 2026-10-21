# director / loop_12.md

**Generational Depth Estimation of Recursive Synthetic Text: Measuring the Discrimination Boundary** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/director/loop_12.md`
- **Structured JSON:** [`35f053870d75be4ccad5.json`](../../sessions/35/35f053870d75be4ccad5.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 12
reason: max_messages
updated: '2026-05-25T06:26:23+00:00'
---

### 1. 🔴 硬约束 / 红线
- GPU 只能用 cqa1-22115 上的 cuda:0/1/2/3（项目配置 gpu_ids）
- 论文正文严格 8 页（EMNLP 2026），用户对页数极其敏感，每次改动后必须视觉验证第 8 页底部
- Abstract 不超过 200 words
- 正文行文中不用破折号（专有名词除外）
- AI usage disclosure 已被用户手动指定，不要改动
- 论文已进入审稿阶段（review_chat_id: oc_0f6dcb30efaa4f47425ef1d9874a89d7），你不参与审稿材料准备
- DDL 是 2026-05-25（今天），用户尚未在 OpenReview 提交

### 2. 🖥️ 基础设施快照
- 服务器：cqa1-22115 (connect.cqa1.seetacloud.com) [root]
- 工作目录：/root/autodl-tmp/gen-depth-contamination
- 论文目录：projects/gen-depth-contamination/docs/paper/
- 匿名仓库：https://github.com/anonymous-nlp-2026-2/gen-depth-contamination
- 4 张 GPU 全部空闲，所有实验已完成（174 个，138 completed）
- 无活跃进程/Worker/Cron

### 3. 📊 当前状态
论文处于可提交状态。本轮 session 主要做了大量论文修复：
- 数据整合：OLMo 3-domain cross-scorer、Gemma-27B filtering、arXiv bootstrap CI 等全部整合到 Table 4/appendix
- 一致性修复：Figure 1 θ=0.55→0.60、Table 4 OLMo 列错位、"100% synthetic"→"~83%"、θ范围 [0.59,0.61]→[0.59,0.60]、"two borderline"→"one borderline (Pythia)"、Table 14 "three families"→"four groups"、Table 4 补 C4-Mistral 行和 arXiv LLaMA-8B 行、Figure 4 caption 修复、Appendix 配置数量统一、"5000 texts"加限定语
- 结构改动：Related Work 4→3 subsection、正文新增 Figure 5 (JSD decay) + Figure 6 (filtering)、Limitations 缩短为 3 点、删除 Ethics Statement、缩写自检 13 处
- Figure 5 重新生成对齐 Table 5 数据
- AI disclosure 替换为用户指定安全版本
- 编译 19 页，0 critical warnings，consistency check 0 critical/0 warning
- Registry 无 RUNNING/PREPARING 实验

### 4. 📋 待办
- 用户在 OpenReview 提交 → 可能还有最后的格式调整需求
- 用户发现新的不一致 → 派 Paper Agent patch
- provenance 检查工具报技术错误（'str' object has no attribute 'get'）→ 排查 paper_provenance.yaml 格式，但不阻塞提交
- 提交后 → 审稿阶段实验已全部完成（Gemma-27B cross-transfer、Mistral 4-domain、OLMo 3-domain cross-scorer），rebuttal 素材就绪

### 5. 🎯 战略上下文
- 核心发现：K*_empirical ≤ 2 跨 6 个架构家族（Qwen/Pythia/OLMo/LLaMA/Mistral/Gemma），domain-dependent（C4/Code K*≤2, Wiki 1-2, arXiv K*=3）
- OLMo 是唯一全域 K*=1 的模型（competence-limited），Mistral 有 monotonic staircase（Wiki=1, C4=1, Code=2, arXiv=3）
- 用户（冯元宁 + 周俊伟）对论文细节极其严格，每个数字/caption/表述都会人工核对。不要假设 Paper Agent 的修改一定准确，关键改动需要视觉验证
- 页数是最高频的修改触发点——每次改动后都要检查正文是否严格 8 页（不多不少）
- 两位用户 ou_892b8a1f2776e36eaf541a0c90fc4619（冯元宁）和 ou_65b0ed556ac2ebb328fa5fe31249f36e（周俊伟）都会直接发修改指令


---
