---
loop: 2
reason: idle_timeout
updated: '2026-05-16T02:43:07+00:00'
---

### 1. 🔴 硬约束 / 红线
- 本项目只能用 rtx6000-diagprobe 的 cuda:0 和 cuda:1，无其他 GPU 分配
- 预注册 pass/fail 标准（D002/D003）**不可中途修改**：ρ<0.5@Gen3 且 Gen0-1 |ρ|>0.7，信号 mean 单调退化≥15%，2 seed 均观测到
- `HF_HUB_OFFLINE=1` 必须设置——服务器无法直连 HuggingFace
- 环境用 conda base，**不要创建 venv**：`source /root/miniconda3/etc/profile.d/conda.sh && conda activate base`
- submit_on_allocated 命令必须自带 conda 激活（不能假设 shell profile 自动加载）
- Condition 2（D004 裁定）检查 **signal mean 退化**，不是 |ρ| 退化——Worker 曾误读，已修正回滚

### 2. 🖥️ 基础设施快照
- **服务器**: rtx6000-diagprobe, 2× NVIDIA RTX PRO 6000 Blackwell (94GB each)
- **工作目录**: `/root/prism_collapse_mixing`
- **Python**: `/root/miniconda3/bin/python` (3.12.3), PyTorch 2.10.0+cu128
- **环境激活**: `source /root/miniconda3/etc/profile.d/conda.sh && conda activate base`
- **模型**: `EleutherAI/pythia-410m-deduped` (405M params), 已缓存本地
- **数据**: `/root/prism_collapse_mixing/data/` (579,255 条)
- **日志**: `/root/prism_collapse_mixing/pipeline.log`
- **活跃进程**: PID 197985 (mvp_collapse_decoupling_v2), tmux session 存在, cuda:0+cuda:1
- **Cron**: 两条活跃 cron 均追踪 PID 197985（mvp_collapse_decoupling 和 mvp_collapse_decoupling_v2 两个 cron entry 指向同一进程）
- **W&B**: 未配置（本项目信号从本地 log/checkpoint 计算）
- **已写好待用的代码**: bootstrap CI 分析脚本、5 代扩展脚本、collapse 轨迹绘图脚本、论文骨架

### 3. 📊 当前状态
mvp_collapse_decoupling_v2 正在运行，当前阶段 `gen2_mixing`（即 Gen 2 的合成数据混合+训练）。Gen 0 和 Gen 1 数据已完成，metrics 已入 registry。

**已有数据**:
- Gen 0: ρ(loss,entropy)=0.929, entropy_mean=3.156, spectral_rank_mean=163.7, corpus_spectral=4.42
- Gen 1: ρ=0.912 (两 seed), entropy_mean=3.044, spectral_rank_mean=165, corpus_spectral=4.68
- Gen 0→1 Δρ=0.017，衰减极慢。线性外推 Gen3 ρ≈0.88，远不到 pass 线 0.5

**Registry**: mvp_collapse_decoupling_v2 RUNNING; mvp_collapse_decoupling DONE(failed/OOM, 已被 v2 接替)
**Workers**: 全部 20 个历史 Worker 已完成，无 running worker
**等待**: cron 回调——pipeline 完成 Gen 2 训练+信号计算后会推进到 gen3 或触发完成回调

### 4. 📋 待办（条件触发式）
- **Gen 2 信号计算完成（cron 回调或手动检查）** → 立即读 metrics，更新 registry，计算 Gen1→2 Δρ：
  - Δρ ≥ 0.03 → 确认非线性加速，Gen 3 完成后启动 5 代扩展（D006/D007），代码已就绪
  - Δρ 在 0.02-0.03（灰区）→ 先完成 Gen 3，看 3 点趋势（Gen0/1/2）再决定是否扩展
  - Δρ < 0.02 → 线性衰减确认，3 代 MVP 极大概率 fail；需汇报 Director 重新评估实验条件（加代数 vs 加 tokens/gen vs 换更大模型），按 Contingency Plan 优先级 (a)→(b)→(c)
- **MVP 全 3 代完成（pipeline 跑完 Gen 3 信号计算）** → spawn Worker 运行 bootstrap CI 分析 + 绘图 → 判定 pass/fail → 汇报 Director
  - Pass → 进入 Research 阶段，准备 PRISM mixing 算法实验
  - Fail（预期概率高）→ 走 5 代扩展（若 Δρ 趋势支持）或产出 Framing 调整提案（red-section）
  - 弱 pass（1 seed 满足另一不满足）→ 追加 seed 3
- **5 代扩展实验启动前** → 需 Director 审批 + 确认 GPU 继续占用

### 5. 🎯 战略上下文
- **核心科学问题**: collapse 信号（entropy/spectral rank/diversity）是否包含 loss 无法捕获的退化信息？
- **决策链**: D001(MVP方案) → D002(量化阈值+2seed) → D003(entropy为主信号) → D004(Condition2检查signal mean) → D005(预判3代fail) → D006(5代扩展设计) → D007(bootstrap CI框架替代统计检验)
- **最大风险**: 3 代 ρ 衰减不足（D005 已预判），但这不等于假设错误——文献支持 collapse 在更多代后加速。5 代扩展是最温和的 escalation。
- **易错点**:
  1. 不要把 corpus-level spectral rank（SIGMA-style, 值~4-5）和 per-example spectral rank（值~160+）混淆——前者是辅助观测，后者因基线 ρ 低（-0.21）不参与 pass/fail 判断
  2. 两 seed 的 Gen 0 metrics 几乎相同是**正确的**（共享同一个预训练 checkpoint + 同一个 probe set），不是 bug
  3. D007 的证据框架是 bootstrap CI + effect size **为主**，统计检验为辅（因 n=6 generations 统计功效不足）
  4. Gen 0→1 entropy_mean 下降 3.5% 但 ρ 仅降 1.8%——说明 loss 和 entropy 同步下降，脱钩尚未开始
- **目标会议**: EMNLP 2026 ARR DDL 5/25（9天后），但如果 MVP fail 需要 5 代扩展，时间线会推到 ICLR 2027（~9月）
- **论文准备**: 骨架已写、Figure/Table layout 已规划（见 memory.md），待 MVP 结果确定后填充
