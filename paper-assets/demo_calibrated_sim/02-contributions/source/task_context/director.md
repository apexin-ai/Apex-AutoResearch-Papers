---
loop: 1
reason: max_messages
updated: '2026-05-12T14:48:52+00:00'
---

### 1. 🔴 硬约束 / 红线
- GPU 只能用 **cuda:2, cuda:3**（cqa1-21977）。cuda:0/1/4/5 属于其他项目。本 session 已发生 2 次越界（cuda:1），被 Reviewer CRITICAL
- 本地代码修改后**必须 ssh_execute 部署到服务器 + ssh_read_only grep 验证**。本 session 发生 4 次"本地改了服务器没同步"，Worker 还曾虚报部署成功
- 服务器有两个路径：新版文件在 `/root/democalib/`（根目录），旧 `/root/democalib/code/` 已清理。所有实验和部署都用根目录
- vLLM 启动必须带 workaround：`enforce_eager=True` + `TORCHDYNAMO_DISABLE=1` + `VLLM_USE_V1=0`

### 2. 🖥️ 基础设施快照
- 服务器：**cqa1-21977**，SSH: `ssh -p 21977 root@connect.cqa1.seetacloud.com`，密码存储于 secret `ssh_password_cqa1_21977`
- 工作目录：`/root/democalib/`
- Python：conda base（`/root/miniconda3/bin/python`），PyTorch 2.10.0+cu128，vLLM 0.18.1
- 模型：Qwen/Qwen2.5-7B-Instruct（HuggingFace cache，14.25 GiB）
- 活跃进程（截至 handoff）：
  - **cuda:2**: vLLM port 8000（mvp-004 实验，PID 111195）
  - **cuda:3**: vLLM port 8001（AAVE 语料生成，PID 142096）
- Cron：mvp-004 监控（180s 间隔）
- 无 W&B / Git 配置

### 3. 📊 当前状态
**MVP 验证阶段**，正在并行跑两件事：
1. **mvp-004**（cuda:2）：20-task 全量实验（uncalibrated baseline + BCP variants），收集 trace 数据。这是首次同时具备所有修复（QuestionDetector precision 100%、###STOP### 终止、context overflow 过滤、H-gate D002 重构）的完整实验
2. **AAVE 合成语料生成**（cuda:3）：generate_synthetic_corpus.py，20 tasks × 5 trials = 100 traces，含后处理到目标率（q=10%, p=20%）。这是 DPO 训练的 preferred 数据

**Phase C DPO pipeline 已验证**：dry-run 通过（QLoRA 4-bit，单卡 4090D 可跑），train_dpo.py + build_dpo_pairs.py 已部署到服务器。

Registry: mvp-001 FAILED（vLLM crash）, mvp-002 KILLED, mvp-003 KILLED（L1 violation）, mvp-004 RUNNING

### 4. 📋 待办
- **mvp-004 完成** → 用修复后检测器重新分析所有 trace → 运行 h_gate_evaluator.py → H1/H2/H3 正式判定
  - H1 PASS（politeness ≥30%，当前 ~45%，几乎确定通过）→ 继续
  - H2：BCP 是否将 politeness gap 缩小 ≥30% relative（降至 ≤37.5%）
  - H2 FAIL on BCP → 不 kill，BCP 失败本身是 finding → 加速 Phase C DPO
  - H3：校准后 task completion ≥80% baseline
- **AAVE 语料生成完成** → build_dpo_pairs.py 构建训练数据（需要 mvp-004 的 uncalibrated traces 作为 rejected）→ train_dpo.py 在 cuda:3 训练
- **DPO 训练完成** → 评估校准效果 → H2/H3 最终判定 → MVP PASS/FAIL
- **MVP PASS** → complete_mvp() → post-mvp-kickoff skill（paper_framing.md → experiment_plan.yaml → dream_simulate）

### 5. 🎯 战略上下文
- **D001**: MVP 聚焦 AAVE 单组，三阶段验证
- **D002**: QuestionDetector 修复后发现 question rate gap 是测量假象（baseline 11.4% ≈ AAVE 真实 ~10%）。**Politeness 是唯一需要校准的维度**（baseline 45% vs 目标 20%）。H-gate 重构为 politeness-primary。这是论文的一个 finding，不是 weakness
- **QLoRA 4-bit 是硬件妥协**：单 4090D 24GB 无法跑 bf16 DPO。Reviewer 建议论文声明 + 可选消融。如果 DPO 效果不显著，需排除量化导致的信号损失
- **易踩的坑**：(1) Worker 反复不同步代码到服务器——必须在同一 task 内部署+验证；(2) 不要在 gpu_ids 外的 GPU 上启动进程，GPU 被占时用白名单内另一张卡；(3) BCP 在 3-task quick test 中使行为率恶化而非改善——全量结果可能确认此方向，但这不 kill 项目（DPO 是 plan B，BCP 失败是 finding）
- **ARR deadline 2026-05-25**（剩 13 天）。Post-MVP 全量研究需 ~6 天（实验+写作），时间紧但可行
