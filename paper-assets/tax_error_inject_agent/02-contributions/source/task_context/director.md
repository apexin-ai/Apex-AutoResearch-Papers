---
loop: 3
reason: max_messages
updated: '2026-05-16T15:05:46+00:00'
---

### 1. 🔴 硬约束 / 红线
- GPU 只用 autodl-5090 的 cuda:0/1/2/3（项目配置白名单）
- detection_rate 指标是假阳性（"back" 关键词触发），**禁止在论文中引用或作为 claim 支撑**
- LLaMA 模型必须是 3.1-8B-Instruct（3.3 只有 70B，3.2 只有 1B/3B）
- 所有训练进程必须设 `TMPDIR=/root/autodl-tmp/tmp`（/tmp 空间紧张）
- 每个 eval 进程独占一张 GPU（~16GB），严禁两个 eval 共享同一 GPU（之前 OOM 崩过 3 次）
- Worker "done" 通知不可信（本项目出现过 5+ 次虚假完成）——必须验证输出 JSON 文件存在且非空

### 2. 🖥️ 基础设施快照
- 服务器：autodl-5090 (connect.bjb2.seetacloud.com)，root
- 工作目录：`/root/autodl-tmp/tax_error_inject_agent`
- Python：`/root/miniconda3/bin/python`（conda base）
- 模型：Qwen3-8B `/root/autodl-tmp/models/Qwen3-8B/`，LLaMA-3.1-8B-Instruct `/root/autodl-tmp/models/Meta-Llama-3.1-8B-Instruct/`
- Eval 脚本：`eval/recovery.py`（不加 --inject = clean eval），`eval/injected_eval.py`（recovery eval）
- 训练数据量：Vanilla=4,358 samples (1,635 steps)，TaxEI/Random=9,029 samples (3,387 steps)
- 活跃进程：vanilla-s123 injected eval GPU 1，taxei-s123 eval GPU 2，random-s123 eval GPU 3，missing clean evals GPU 0

### 3. 📊 当前状态
LLaMA 3-seed 训练全部完成。s123 eval 正在 4 GPU 并行跑中，预计 30-40 min 全部出齐。

**已确认的 LLaMA 结果**：
| Condition | Clean SR (s42/s0/s123) | Recovery Rate (s42/s0) |
|-----------|------------------------|------------------------|
| Vanilla (4358) | 72.3%/72.3%/72.3% | 74.5%/74.5% |
| TaxEI (9029) | 76.6%/76.6%/— | 74.5%/74.5% |
| Random (9029) | 76.6%/74.5%/— | 76.6%/74.5% |

**Qwen 5-seed 最终**：V=67.3%, T=57.4%, R=57.9%, RP=50.2%

**RUNNING evals**：vanilla-s123 injected, taxei-s123 clean+injected, random-s123 clean+injected
**Recovery eval**：15/15 完成（Qwen Random s42 checkpoint 不存在，4-seed 均值 56.4%）

### 4. 📋 待办
- s123 eval 全部完成 → 编译完整 3-seed 跨模型统计表 → 更新 paper_framing.md（"model-proficiency-dependent effect"）
- 3-seed 表确认 LLaMA 中性 → log_decision → update_roadmap → 通知用户数据齐全
- Framing 定稿后 → dream_simulate(review_mode="full") → 根据结果调整 plan
- Dream 通过后 → director_post_to_paper_agent 启动论文写作
- Scale-up 收集状态待确认（之前停在 ~405/1000，PID 可能已死）

### 5. 🎯 战略上下文
**核��发现**：Error injection 效果 model-dependent。Qwen 受害 -9pp，LLaMA 免疫 0pp。TaxEI≈Random 跨模型成立（taxonomy 标签零收益）。RP 叠加更有害。

**决策链**：D043(RP有害) → D044(scale-up暂停) → D045(scope=长文) → D046(撤销D044,scale-up重启)

**易错点**：
- LLaMA clean eval 中 TaxEI/Random > Vanilla +4pp 是**数据量效应**（9029 vs 4358），不是注入有益。论文中公平对比应聚焦 TaxEI vs Random（数据量一致）
- EXIT_CODE=129 = SIGHUP（SSH/tmux 断开），不代表训练失败——检查 checkpoint 是否完整
- 投稿目标：EMNLP 2026 Findings 8-page long paper，不要 fallback 到更低会议
