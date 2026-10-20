---
loop: 2
reason: max_messages
updated: '2026-05-12T15:31:19+00:00'
---

### 1. 🔴 硬约束 / 红线
- GPU 只能用 `cuda:0` 和 `cuda:1` @ westd-16980，禁止使用其他设备
- 服务器只有 `westd-16980`（connect.westd.seetacloud.com），无其他服务器
- 代码路径 `/root/carc`，模型/数据放 `/root/autodl-tmp/`（根分区小）
- 项目处于 **MVP 阶段**，禁止启动完整研究规划、禁止调 dream_simulate
- 投稿目标 EMNLP 2026 ARR，DDL 2026-05-25（剩 13 天）
- 已有 4 个 negative 结果（mvp_001, sanity_kv_eviction, carc_mvp_seed42, carc_mvp_seed1337），cross-axis 假说已证伪，已 pivot 到 O(1) EMA KV eviction

### 2. 🖥️ 基础设施快照
- 服务器：westd-16980 (connect.westd.seetacloud.com)，2×RTX PRO 6000 96GB
- 工作目录：`/root/carc`
- Python/conda：未详细探测（Agent 连接时自动检测镜像）
- W&B：未配置
- Git：未配置
- 活跃进程：d003_wikitext_32k (RUNNING)、d003_reasoning_traces (RUNNING)——具体 PID/tmux 未知，需 Agent SSH 确认
- carc_generate_rope_test：PREPARING 状态

### 3. 📊 当前状态
- **刚做完**：批准了 D004 决策——允许 d003 最后一次部署尝试 + Plan B contingency
- **正在跑**：d003_wikitext_32k 和 d003_reasoning_traces（D003 sanity check 在 WikiText-2 4K 上 FAIL 后，换条件重试）
- **等待中**：两个 RUNNING 实验的结果回调；carc_generate_rope_test 准备中
- **Agent 队列**：空闲（idle 68s，depth=0，无 pending）
- **Reviewer**：刚批准 RESET_BOTH，新 Reviewer session 将启动
- 趋势：成功 0 / 负向 4 / 失败 0——尚无正面信号

### 4. 📋 待办（条件触发式）
- d003_wikitext_32k 或 d003_reasoning_traces 完成 → 检查 EMA vs random PPL gap 是否 ≥5%；若是 → sanity gate 通过，进入 baseline 复现 + full eval；若否 → 评估是否彻底放弃 EMA eviction 方向或再调参数
- carc_generate_rope_test 就绪 → 审批并分配 GPU 启动
- 两个 d003 都 negative → 需要做 pivot 决策（D005），考虑是否还有时间在 DDL 前完成新方向
- 任何实验 positive → 立即铺 baseline 复现（H2O, R-KV）+ eval 框架（PPL/MATH-500/LongBench），两卡并行

### 5. 🎯 战略上下文
- **核心假说已 pivot**：从 cross-axis（KV similarity→MLP sparsity）转向 O(1) EMA KV eviction with recurrence-aware protection
- **决策链**：D001（MVP 定义）→ D002（MVP FAIL, pivot to Path C）→ D003（sanity FAIL on WikiText-2 4K，但数据/长度条件不匹配动机场景）→ D004（允许最后一次尝试 + Plan B）
- **最易判断错的事**：D003 sanity check 在短文本上 FAIL 不代表方向错——EMA eviction 的动机场景是长序列（32K+），短序列 cache 不满根本不触发 eviction。d003_wikitext_32k 用 32K 长度才是真正的 sanity gate
- **时间压力**：DDL 5/25，如果 d003 再 FAIL，剩余时间可能不足以完成新 pivot + 全套实验 + 论文。此时需决策：(a) 坚持当前方向降低 claim 强度，(b) 放弃本次投稿窗口
- **paper_framing.md 未创建**（MVP 阶段正常），ideas.md 也未创建
