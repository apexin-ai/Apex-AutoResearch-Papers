---
loop: 3
reason: max_wall_time
updated: '2026-05-25T03:22:03+00:00'
---

### 1. 🔴 硬约束 / 红线
- autodl-8gpu 只有 4 张 GPU (0-3)，worker 报告中提到的 "GPU 4-7" 不存在
- Sonnet/Gemini API 采集因 OpenRouter 403 地域封锁（中国 IP）已永久停滞，无法在 autodl-8gpu 上恢复，需非中国 IP 服务器或代理
- Mistral-large-2 仅 118 行，已决定排除（D043），不要尝试重启
- JSONL 行数 ≠ 有效记录数（24-39% 重复/无效），进度监控必须用去重计数或 cell 覆盖率，不能只看 wc -l
- exp-006 数据显示 J=6 的 G-MFRM advantage 仅 +2.1pp（vs J=9 的 +7.1pp），N=17 结果如果 Δτ 小不要惊讶——这是预期的

### 2. 🖥️ 基础设施快照
- 服务器：autodl-8gpu (root)，工作目录 /root/gated_mfrm_judge_bias
- Python：/root/miniconda3/bin/python（conda base 环境）
- rtx6000-4x 已不可用，westd-25068 端口不通
- GPU 状态：GPU 0 被 MCMC Phase 1 占用 (PID 614592, 667 MiB)，GPU 1-3 空闲
- 活跃进程：
  - MCMC Phase 1: PID 614592, CUDA_VISIBLE_DEVICES=0, 日志 /root/gated_mfrm_judge_bias/logs/exp020_mcmc.log
  - MCMC monitor: PID 605265（已触发，可能自行退出）
  - DeepSeek 采集: PID 592328, 16,257/18,000 (90.3%)
  - tmux: orchestrator2（run_remaining.sh）
- MCMC 脚本：/root/gated_mfrm_judge_bias/run_mcmc_n17_exp020.py
- 分析脚本：/root/gated_mfrm_judge_bias/analysis/n17_update/ 下 4 个脚本

### 3. 📊 当前状态
**MCMC Phase 1 正在运行**（~20:39 UTC 启动），33,931 obs / 18 models / 500 items / J=6。raw_average 已完成，mfrm_only 在 warmup（4.33 it/s, acc_prob=0.92）。预计 2-4h 完成（~22:30-00:30 UTC）。

**采集完成情况：**
| Judge | 状态 | 行数 |
|-------|------|------|
| LLaMA | ✅ DONE | 18,093 |
| Qwen local | ✅ DONE | 17,994 |
| Qwen3-235B | ✅ DONE | ~18,000+ |
| DeepSeek | 🔄 90.3% | 16,257 |
| Sonnet | ⛔ 403 frozen | 14,255 |
| Gemini | ⛔ 403 frozen | 11,253 |

Registry: exp-020 RUNNING（N=17 数据采集+MCMC）。其余 exp 全 DONE/killed。

**Fig1 framework 最终版审过**：fig1_framework_v2.png (v3-paperbanana)，公式符号 +c_n·e_i 已修正，32/32 checklist 通过。

### 4. 📋 待办（条件触发式）
- MCMC Phase 1 完成 → 立即审查：(1) 收敛性 R̂<1.05 + ESS>100, (2) joint_gmfrm τ vs baseline τ 的 Δτ, (3) 用 analysis/n17_update/ 脚本生成表格
- DeepSeek 采集完成 → 启动 MCMC Phase 2 re-run，然后用 check_phase_diff.py 比较 SAFE/CAUTION/UNSAFE
- MCMC τ 结果出来 → 关键判断：N=17/J=6 的 Δτ 是否与 exp-006 的 k=6 预测一致（+0.021），还是更大（N 增加的 power 是否补偿了 J 减少）
- Director 提交章节写作审查 → 加载 paper-quality-lessons.skill.md，按 §5.1-5.2 审查模式 B 执行
- 任何新实验 RUNNING → 检查 CUDA_VISIBLE_DEVICES 是否在 gpu_ids 白名单内

### 5. 🎯 战略上下文
- **核心 claim**：G-MFRM joint estimation 通过同时建模 judge bias (d_j) 和 contamination (c_n·e_i) 改善模型排名（vs Arena ELO τ）。N=8/J=9 已证明 Δτ=+7.1pp (exp-003b)。
- **最大风险**：N=17/J=6 的 Δτ 可能远小于 +7.1pp。被排除的 3 个 judge（opus/gpt-5.5/mistral）恰好是 d_j 分布两端极值，剩余 J=6 的 d_j 范围压缩近半 [-0.42, +0.31]。如果 Δτ ≈ +2pp，需要调整论文 framing——以 N=8/J=9 为 primary result，N=17 为 scaling validation。
- **OpenAI/GPT 家族完全缺失**——审稿人最可能攻击的点。N=8 有 GPT 作为 target model 但不是 judge。
- **易错判断**：不要用"人类时间直觉"评估 DDL 风险——只看 GPU-hours 够不够。AI 团队分钟级写代码、并行跑实验、24h 出初稿。
- **决策链**：D043（MCMC cutoff plan，被 TP 切换 invalidated）→ D044（mistral-large-2407 restored to τ）→ 当前 J=6 配置是 budget/region 限制的结果，非方法论选择。
