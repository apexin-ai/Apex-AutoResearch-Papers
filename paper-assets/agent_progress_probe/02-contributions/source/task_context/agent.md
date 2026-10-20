---
loop: 8
reason: max_wall_time
updated: '2026-05-16T02:48:19+00:00'
---

### 1. 🔴 硬约束 / 红线
- GPU 白名单：只能用 bjb2-23165 的 cuda:0 和 cuda:1，不可用其他卡
- LLM baseline 模型必须是 `anthropic/claude-sonnet-4.6` via OpenRouter（与 SWE 实验一致），不能换模型
- GB 超参固定：n_estimators=200, lr=0.05, max_depth=5；RF: n_estimators=100, max_depth=10——这是 canonical 值，全项目统一
- `OPENROUTER_API_KEY` 不在项目 secrets 中，A4 (LLM-on-OH) 可能 blocked——不要假设 key 存在，worker 正在服务器上检查环境变量
- early_termination_sim.py 和 pareto_curve.py 已在本地修改但**未 commit**——如果需要同步到服务器，worker 需要读本地文件再 SSH 写远程

### 2. 🖥️ 基础设施快照
- 服务器：bjb2-23165，工作目录 /root/autodl-tmp/agent_progress_probe
- Python：conda base → `source /root/miniconda3/etc/profile.d/conda.sh && conda activate base`，pip/python 在 /root/miniconda3/bin/
- OH 数据：/root/autodl-tmp/openhands_data/（windows_labeled.jsonl + openhands_trajectories.jsonl）
- SWE 数据：/root/autodl-tmp/agent_progress_probe/data/（windows_labeled.jsonl + swe_agent_trajectories_5000.jsonl）
- 本地项目：/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe/
- 活跃进程：无 GPU 训练进程在跑（B1 sim 已完成），A2/A3 probe 训练刚启动应该在跑
- 无活跃 cron

### 3. 📊 当前状态
**刚完成**：
- D072 代码修复（pareto_curve.py 格式兼容 + early_termination_sim.py multi-seed）
- A1 conf=1 error decomposition ✅ — GB 净优势 +13 窗口（纠正 15 MV 错误，仅引入 2 个），集中在 stagnation。强 anti-circularity 证据
- B1+B2 early termination sim + waste audit ✅ — GB k=1 节省 40.4% compute，precision 99.5%。SWE 浪费 3.7x > OH

**Running workers (6/6)**：
| Worker ID | 任务 | 预计时长 |
|-----------|------|---------|
| d073-a2-probe-bge-m3 | BGE-M3 cross-agent probe (cuda:0) | 3-4h |
| d073-a3-probe-e5-large | E5-large cross-agent probe (cuda:1) | 3-4h |
| d073-a4-llm-on-oh | LLM judge on OH (可能 blocked on API key) | 6-12h or blocked |
| d073-c-statistical-robustness | C1 calibration + C2 power + C3 ceiling + C4 2LF coverage | 2-3h |
| d073-d-figures | SHAP + trajectory viz + pareto curve | 2-3h |
| d073-s1-third-agent-trajectories | 搜索第三 agent 公开轨迹 | 2-4h |

**Registry PREPARING**：d073-probe-bge-m3, d073-probe-e5-large, d073-llm-on-oh, d073-figures, d073-statistical-robustness

### 4. 📋 待办（条件触发式）
- A2/A3 probe 完成 → 更新 registry metrics，如果两个 encoder 都在 0.5-0.7 → 确认 gap 是方法论差异，向 Director 汇报
- A4 worker 报告 "API key not found" → 向 Director 报告需要申请 OPENROUTER_API_KEY，用 feishu_send_tum_key_request_card 走 TUM 流程
- C1-C4 完成 → 更新 registry，将 ECE/power/ceiling 数字汇总给 Director
- D figures 完成 → 确认 PDF 生成，汇报 Director
- S1 找到第三 agent 数据 → spawn worker 写 adapter + 跑 cross-agent eval；找不到 → 汇报 Director 讨论替代方案
- **任何 worker 完成释放 slot → 立即 spawn S2 (新 LF 设计) 和 S3 (non-SE 轨迹搜索)**——这两个还没 spawn，等 slot
- B3 pareto curve 已包含在 D figures worker 中，不需要单独处理
- 所有 D073 完成后 → 汇总向 Director 报告，推进论文 patch

### 5. 🎯 战略上下文
- **EMNLP 2026 ARR 5/25 DDL，剩 9 天**。31/32 实验完成，gold set blocked on 人工标注（最晚 5/16 必须启动）
- D073 是 Dream Round 2 审稿前的补强实验包——anti-circularity (A1-A4) + intervention (B1-B3) + statistical robustness (C1-C4) + figures (D1-D2)
- **核心数字**：structural GB cross-agent 0.967 vs best LLM 0.799 = 16.8pp gap。Gold set B (N=505): GB 0.839 显著优于 MV 0.798 (p=0.0001, +4.2pp)
- **易错点**：
  1. 不要混淆 in-domain (0.9919/0.9951) 和 cross-agent (0.967) 的 GB 数字——headline 用 cross-agent
  2. RF conf≥2 cross-agent (0.996) 比 GB (0.992) 高，但 all-windows GB (0.967) > RF (0.912)——scope 不同结论不同
  3. TWV Probe 在 gold 上 (0.854) borderline 不显著 vs GB (0.839, p=0.056)——silver 排序和 gold 排序不一致
  4. CMI=0 是数学必然不是实验发现——用 feature-overlap-ablation (11/19 split) 做 anti-circularity
  5. OH 数据口径：JSONL 150,652 windows vs embeddings 143,057——论文用 JSONL 口径
