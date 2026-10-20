---
loop: 22
reason: max_wall_time
updated: '2026-05-25T19:51:14+00:00'
---

### 1. 🔴 硬约束 / 红线
- GPU 白名单：rtx5090-4x cuda:0-3（共 4 张），bjb2-12179 cuda:0 不可用。白名单外的 GPU 即使 Director 指令也要 push back
- 14B 推理每张卡约 6h（dev 985 docs）/ 2h（test 500 docs），排期时按此估算
- evidence tax 定义：tax = no-evi − with-evi（负值=evidence helps）。论文、ROADMAP、汇报必须统一此方向
- multi-seed std 必须用 sample std (÷(n-1), ddof=1)，不用 population std (÷n)。Director 已纠正过一次
- submit_training_job 的 command 里必须自带环境激活（`source /root/miniconda3/etc/profile.d/conda.sh && conda activate base`），不假设 .venv 存在

### 2. 🖥️ 基础设施快照
- **服务器**：rtx5090-4x（4×RTX 5090），工作目录 `/root/autodl-tmp/freige`
- **Python**：`/root/miniconda3/bin/python`（conda base env，不是 venv）
- **镜像**：aml-train（连接后先 `detect_image` 确认）
- **模型路径**：
  - SFT adapters: `/root/autodl-tmp/sft_output` (4B), `sft_output_qwen3_1_7b_bf16`, `sft_output_qwen3_8b_bf16`, `sft_output_14b_s42/s43/s44`
  - RSFT adapters: `/root/autodl-tmp/rsft_output_*` (各 scale × seed)
  - Base models: `/root/autodl-tmp/models/Qwen/Qwen3-{1.7B,4B,8B,14B}`, `/root/autodl-tmp/models/meta-llama/Llama-3.1-8B`
- **数据路径**：DocRED dev `/root/autodl-tmp/data/docred`, Re-DocRED test `/root/autodl-tmp/data/re-docred-repo/data`
- **HF cache**：`/root/autodl-tmp/.hf_cache`（必须设 `HF_HOME`）
- **Eval 结果**：`/root/autodl-tmp/eval_results/<exp_id>/`
- **日志**：`~/runs/faith-evidence-ie/<exp_id>.log`
- **磁盘**：根分区 879GB (3% used)，数据盘 7.3TB (24% used)——充裕
- **活跃进程**：无。全部 GPU 空闲
- **bjb2-12179**：有数据但 GPU 不可用，仅做存储

### 3. 📊 当前状态
**刚完成**：14B RSFT s44 全部 4 个 eval（dev with-evi/no-evi, test with-evi/no-evi）。14B 3-seed 数据已闭环，Director 已确认论文 12 处数字全部更新完毕，PDF 已编译。

**Registry RUNNING/PREPARING**：
- `test_eval_8b_rsft_s44_no_evi`: RUNNING（8B s44 no-evi test eval，可能已完成但 cron 未回收——接手后优先检查）
- `test_eval_llama_rsft_s42`: QUEUED（LLaMA RSFT s42 test eval，待 GPU 分配）
- 若干 PREPARING 状态的旧实验（d158 系列 registry 状态卡在 PREPARING 因为 PREPARING→RUNNING 状态转换不允许直接跳，但实际已完成并录入了 metrics+conclusion）

**等待中**：无 Worker 回调、无 Cron 待处理。Director 说"无新任务，GPU 待命"。

**今日完成的非实验工作**：
- fig_task_example（§3.1 task example 概念图）已生成并插入 method.tex
- fig_paradigms（§3 optimization paradigms 流程图）已生成并插入 method.tex

### 4. 📋 待办（条件触发式）
- test_eval_8b_rsft_s44_no_evi cron 回调到达 → 更新 registry metrics，计算 8B s44 test tax，更新 ROADMAP 8B test tax 表（当前 n=2: -0.34/-1.74，s44 补全后 n=3）
- Director 触发 Round 3 review → 加载 review-reviewer-session-start skill，全文审查
- Director 分配新任务 → 按 resource-saturation skill 检查 GPU 饱和度后执行
- 如果 Director 要求更新论文数字 → 注意 sample std (ddof=1) 约定

### 5. 🎯 战略上下文
- **投稿目标**：EMNLP 2026 Main (ARR July cycle, ~54 天)
- **核心贡献**：(1) RSFT+NLI 有效性 (2) Decoupling spectrum (GRPO catastrophic > DPO gradual > RSFT none) (3) Evidence tax landscape + variance compression
- **当前阶段**：数据审计完成，准备 Round 3 review。Round 2 评分 3.0 (Findings)，升级路径 3.0→3.5→4.0
- **14B evidence tax 叙事**：test tax mean=+0.12±0.64pp (n=3)，CI crosses zero → 论文用 "neutral/uncertain" 框架，Director 确认不需改叙事
- **易错点**：
  - 不要把 evi_f1（TP-only，虚高）和 evi_f1_joint（与 DREEAM 对标的）搞混——memory 里有记录
  - PREPARING 状态的实验不能直接转 RUNNING（状态机限制），已提交的实验靠 cron 监控自动推进
  - AutoDL 实例重启后 SSH 端口会变，连接失败别反复重试
