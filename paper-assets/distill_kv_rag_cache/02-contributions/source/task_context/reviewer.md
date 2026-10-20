---
loop: 1
reason: max_wall_time
updated: '2026-05-14T08:28:46+00:00'
---

### 1. 🔴 硬约束 / 红线
- GPU 白名单：autodl-rtx6000 的 cuda:0 和 cuda:1，禁止其他服务器或 GPU（C001）
- Registry 当前仅 2 个 failed 实验，但服务器上有 8+ 组有效结果未注册——审查时必须直接读服务器 results/ 目录，不能只看 registry
- 结果文件全在 `/root/autodl-tmp/compresslink/results/` 下各子目录的 `mvp_results.json`，不是 registry

### 2. 🖥️ 基础设施快照
- 服务器：autodl-rtx6000（root），备用 gpu-6000pro-2（root，未使用）
- 工作目录：`/root/autodl-tmp/compresslink`
- Python：`/root/miniconda3/bin/python`（conda base 环境）
- 模型：`/root/autodl-tmp/models/Llama-3.1-8B-Instruct`（ModelScope 下载）
- 数据：`/root/autodl-tmp/compresslink/data/hotpotqa_500.jsonl`（500 bridge samples）
- 校准：`/root/autodl-tmp/compresslink/calibration/hotpotqa_50/calibration.pt`（offline PCA basis）
- 活跃进程：无。两张 RTX PRO 6000 (97GB) 全部空闲 0%/0MiB
- 无 tmux session / cron 任务

### 3. 📊 当前状态
刚完成两轮审查并 post 给 Director：

**已发布的 critical 审查**：
1. CEGR 修复（min-max 归一化 ε）后 C 配置在 per-sample 和 offline PCA 8x 下均 F1=0.0，低于 A(ProphetKV) 的 F1=0.2/0.114。compression error 信号与正确恢复目标反相关。
2. D(RABA+CEGR) 在 offline PCA 8x 下表现最差（F1=0.0），方向与 MVP 假设完全相反。

**等待 Director 决策**：kill / pivot / 继续。GPU 全部空闲，DDL 5/25 仅剩 11 天。

Registry: 2 experiments (mvp_hotpot_gpu0, mvp_hotpot_gpu1)，均 DONE/failed。无 RUNNING/PREPARING。

### 4. 📋 待办
- Director 回复 kill/pivot 决策 → 根据方向调整审查焦点
- 若 Director 要求跑 6x offline PCA 验证 → 审查结果是否 D ≤ A（kill 条件第一条需两个 ratio 同时成立）
- 新 worker 完成通知 → 读 results/ 新目录交叉核实，重点关注 RABA/CEGR 组件是否仍然有害
- 若 Agent 提出 framing pivot（如把 negative 结果包装成"重要发现"）→ 立即 Read `negative-framing-review.skill.md` 按四维度审查

### 5. 🎯 战略上下文
**核心结论链**：
- D001: MVP 4 组对比验证联合优化价值
- D002: 加 kill criteria（D≤A 两个 ratio → kill）
- D003: NQ→HotpotQA（NQ context 太短）

**实验数据汇总**（最关键的几组）：

| 条件 | A | C | D | E |
|------|---|---|---|---|
| per-sample 6x | 0.35 | 0.35 | 0.35 | 0.314 | → 全同（cliff effect，6x 无损）
| per-sample 8x | 0.2 | 0.2 | 0.2 | 0.314 | → 全同
| offline 8x | 0.114 | 0.114 | **0.0** | 0.314 | → D 最差
| CEGR fix per-sample 8x | 0.2 | **0.0** | — | 0.314 | → C 反向
| CEGR fix offline 8x | 0.114 | **0.0** | — | 0.314 | → C 反向

**下一个"我"最容易判断错的事**：
1. 不要因为 per-sample PCA 6x 结果全同就认为"方法 OK"——那是 cliff effect（per-sample PCA 6x 近乎无损，区分度为零），不代表方法有效
2. 不要只看 registry——实际有价值的结果都在服务器 results/ 目录下未注册的 JSON 文件里
3. A=C（修复前）不代表 CEGR"没有害"——而是 CEGR 退化为 ProphetKV（ε 近均匀），真正生效后反而更差
4. 压缩无恢复在 4x-32x 全部 EM=F1=0（stress_test），所以"压缩质量"本身不是核心贡献——恢复才是唯一救命机制，但 F1 天花板 0.2 vs 0.314
5. Kill 条件尚未完全触发（缺 6x offline PCA 数据），但 8x 方向已明确反向
