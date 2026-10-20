---
loop: 1
reason: max_messages
updated: '2026-05-12T02:55:32+00:00'
---

### 1. 🔴 硬约束 / 红线
- 只能用 seetacloud-bjb2-structtts，home-1x5090 不属于本项目（用户 D002 明令禁止）
- GPU 只有 cuda:0（1× RTX 5090 32GB），account=sonny
- DeepSeek-R1-Distill-Qwen-7B **不是 MLA 架构**，是 Qwen2 GQA (4 KV heads)。所有 "MLA" 叙述已被 D005 标记为无事实基础，禁止在论文/分析/汇报中使用 MLA 描述该模型
- Δpert 标准公式：`(mean_novel - mean_redundant) / (mean_novel + 1e-10) * 100`，layer-analysis 脚本用了错误分母（除以 redundant），需统一
- HF 下载在该服务器不可用，用 ModelScope 或 hardcoded fallback problems

### 2. 🖥️ 基础设施快照
- 服务器：seetacloud-bjb2-structtts (connect.bjb2.seetacloud.com)，account=sonny
- 工作目录：/home/sonny/redundancy-compound-sparsity
- Python：/home/sonny/redundancy-compound-sparsity/.venv/bin/python (torch 2.11.0+cu128)
- DeepSeek-R1-Distill-Qwen-7B：/root/autodl-tmp/.ms_cache/ 下（15GB，完整）
- Llama-3.1-8B-Instruct：/root/autodl-tmp/.ms_cache/LLM-Research/Meta-Llama-3___1-8B-Instruct/（30GB，完整）
- DeepSeek-R1-Distill-Llama-8B：下载中 via ModelScope (PID 18706)，目标同 .ms_cache
- Qwen2-7B-Instruct：下载中 via ModelScope，目标同 .ms_cache
- 活跃进程：llama-sparsity-sweep PID 18296/18306 (cuda:0, tmux)
- KV eviction 代码：src/kv_eviction/（13 files, 4 策略）
- 实验结果：results/mvp/, results/neg_cross_model/
- layer-analysis 可视化：results/neg_cross_model/analysis/（6 张 PDF+PNG）

### 3. 📊 当前状态
**刚做完**：D005 架构误判修正——发现 DeepSeek-R1-Distill-Qwen-7B 是 GQA 不是 MLA，设计了 2×2 confound 对照实验，更新了 ROADMAP/experiment_plan/paper_framing，派 Agent 最高优先级执行 confound-ctrl-001。llama-layer-analysis 完成（数据有效但 MLA 解释无效）。

**Registry 状态**：
- llama-sparsity-sweep: RUNNING（cuda:0, PID 18296, 测 50-70% sparsity）
- kv-bench-001: DONE/failed（静默失败，只处理了 1/10 texts，需重跑）
- confound-ctrl-001: PREPARING（模型下载中 + 脚本就绪，等 GPU 释放）
- confound-ctrl-002: PREPARING（模型下载中 + 脚本就绪）

**等待中**：
- llama-sparsity-sweep 完成回调 → 立即启动 confound-ctrl-001
- dream_simulate (dream_20260512T022430) 异步运行中 → **注意：基于错误 MLA narrative，结果需丢弃**
- Reviewer 正在 reset

### 4. 📋 待办（条件触发式）
- llama-sparsity-sweep 完成 → 记录 Δpert 数据 → 立即提交 confound-ctrl-001 到 cuda:0
- confound-ctrl-001 结果出来 → **关键判定**：r~0.15 → 推理训练是 confound，narrative 转 "generation regime dependence"；r~0.47 → 架构(KV head count)有影响，修正架构描述继续
- confound-ctrl-001 完成 → 紧接 confound-ctrl-002 (Qwen2-7B-Instruct)
- 2×2 矩阵填满 → 重写 paper_framing.md（根据 confound 结果选新 narrative）→ 重跑 dream_simulate
- dream_20260512T022430 结果到达 → 丢弃（基于错误 MLA narrative）
- kv-bench-001 需调查失败原因后重跑（排在 confound 对照之后）
- layer-analysis 脚本 Δpert 公式需统一（除以 novel mean），MLA 标签需替换

### 5. 🎯 战略上下文
- **决策链**：D001(选模型) → D002(换服务器) → D003(MVP FAIL→Option B) → D004(GQA positive→Option A) → D005(MLA误判→confound resolution)
- **核心数据**：r=0.147/Δpert=-2.2% (DeepSeek-Distill-Qwen, 推理, Qwen2 GQA 4KV) vs r=0.471/Δpert=+6.6% (Llama-Instruct, 指令, Llama GQA 8KV)
- **最容易判断错的事**：Agent 和旧分析仍大量使用 "MLA" 术语描述 DeepSeek-R1-Distill-Qwen-7B——这是 GQA，不要被历史文本误导
- **Δpert=6.6% 不满足项目自有 suggestive 门槛**（需 AND: r≥0.4 且 Δpert≥10%），ROADMAP 标 "borderline PASS" 不准确
- **DDL 压力**：EMNLP 2026 ARR 5/25，还剩 ~13 天。confound 实验 1-2h 出结果，是当前唯一阻塞项。narrative 方向确定后才能启动论文写作
- **两个可能的 narrative 方向**：(A) generation regime dependence（推理 vs 指令）— 如果 Distill-Llama r~0.15；(B) GQA configuration dependence（KV head count/group ratio）— 如果 Distill-Llama r~0.47。前者更可能但故事较弱，后者不太可能但需要更多 GQA 配置数据点
