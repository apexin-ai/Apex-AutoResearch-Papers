---
loop: 25
reason: idle_timeout
updated: '2026-05-23T03:14:42+00:00'
---

### 1. 🔴 硬约束 / 红线
- GPU 白名单：westd-29999 的 gpu_ids 需从 `get_project_status` 确认，report.md 显示分配了 cqa1-21977:cuda:0 和 westd-29999:cuda:0，但 westd-29999:cuda:3 也在跑 sft_falcon3_7b_d050_s42_v2——以 registry 实际分配为准
- D215 决策：Falcon3 结果不论好坏，直接提交 ARR，不再加内审轮次
- ARR deadline: May 25 (D+4)，main text 严格 8 页
- 三个 eval 实验 (eval_falcon3_d000/d005/d025_s42) 已标记 DONE(failed)，修复后需要新 exp_id 重跑，不能复用旧 ID

### 2. 🖥️ 基础设施快照
- **westd-29999**: 4× RTX PRO 6000 Blackwell, 磁盘 427G/879G (49%), /autodl-pub 5.3T/7.3T (24%)
- **cqa1-21977**: 1× RTX 4090 D, 磁盘 /autodl-pub 360G/7.0T (95%⚠️), /usr/bin/nvidia-smi 818G/879G (2%)
- 项目代码路径：远程 `/root/projects/contamcal-irt-calibration/`（需 Worker SSH 确认具体结构）
- 活跃进程：
  - sft_falcon3_7b_d100_s42: cqa1-21977, PID 666107, cuda:0, RUNNING（reconcile 确认存活）
  - sft_falcon3_7b_d050_s42_v2: westd-29999, PID 600596, cuda:3, RUNNING
- 活跃 cron：sft_falcon3_7b_d100_s42 监控中

### 3. 📊 当前状态
**刚发生的事**：收到 cron 回调，eval_falcon3_d025_s42 进程异常退出 (EXIT_CODE=1)。实际上三个 eval (d000/d005/d025) 全部在 2026-05-22 11:06-11:07 UTC 以 EXIT_CODE=1 失败，创建到失败仅 3-4 分钟，是系统性问题。

**正在进行**：已有诊断 Worker `worker_diagnose_eval_falcon3_failed_20260522T110904` 在运行（turn_count=3，刚开始读日志），等待其回调。

**Registry 概览**：406 实验，DONE 360 (success 269, failed 65, negative 10, killed 16), PREPARING 42, QUEUED 2, RUNNING 2

**等待中**：
- Worker 诊断回调 → 拿到根因后决定修复方案并重跑 eval
- sft_falcon3_7b_d100_s42 完成回调 → 跑 d100 eval
- sft_falcon3_7b_d050_s42_v2 完成回调 → 跑 d050 eval

### 4. 📋 待办
- 诊断 Worker 回调到达 → 读根因，修复 eval 脚本/环境，用新 exp_id 重新提交 d000/d005/d025 eval（westd-29999:cuda:0 空闲可用）
- sft_falcon3_7b_d100_s42 cron 回调 (cqa1) → 提交 d100 eval
- sft_falcon3_7b_d050_s42_v2 完成 → 提交 d050 eval
- 全部 5 个 dosage (d000/d005/d025/d050/d100) eval 完成 → 汇总 Falcon3 dose-response profile，分类到 4-pattern taxonomy，更新论文
- D215: Falcon3 结果出齐 → 不管结果如何直接更新论文提交 ARR

### 5. 🎯 战略上下文
- **核心结论**：SFT-route benchmark contamination 产生 family-dependent dose-response profiles，4-pattern taxonomy: Immune (Phi-4, LLaMA-3) / Collapse (Qwen-14B) / V-recovery (Qwen-7B) / Benefit (Gemma-2, OLMo-2)
- **Falcon3 的角色**：第 6 个 model family，用于 cross-family replication。结果将决定 Falcon3 属于哪个 pattern，增强 taxonomy 的泛化性
- **论文状态**：Round 10 action matrix 全部完成，终稿就绪，编译通过 8 页 main text。等 Falcon3 结果填入后即可提交
- **易错点**：
  - 三个 eval 同时失败是系统性问题（脚本 bug / checkpoint 路径 / 环境），不是个别实验问题——修一个就全修了
  - SFT v1 系列 (sft_falcon3_7b_d000/d005/d025/d050_s42 无 v2 后缀) 也是 failed 的，v2 才是成功的训练——eval 必须指向 v2 checkpoint
  - westd-29999:cuda:0 显示"分配了没跑"，这是因为 eval 失败释放了——修复后应立即利用这张卡
  - cqa1 磁盘 /autodl-pub 已用 95%，如果要在 cqa1 跑 eval 需先检查空间
