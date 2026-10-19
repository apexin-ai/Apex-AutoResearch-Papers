---
loop: 1
reason: max_messages
updated: '2026-05-21T05:58:30+00:00'
---

### 1. 🔴 硬约束 / 红线
- 本项目 GPU 分配：westd-13176 的 cuda:0-3（4× RTX 6000 PRO 96GB），不得使用其他服务器的卡
- 模型必须下载到 `/root/autodl-tmp/models/`，根分区只有 ~620MB 可用
- HF 下载必须 `HF_HUB_DISABLE_XET=1` + hf-mirror.com，否则 xet 协议 401 超时
- Llama4 路径是 `Llama4-Scout-W4A16`（无连字符），之前因路径不一致浪费过时间（M008）
- GlobalMMLU 无 train split，用 test split 70/30 分（probe_train/eval）；dev 仅 285 样本太小不能用于 MMD

### 2. 🖥️ 基础设施快照
- 服务器：westd-13176 (connect.westd.seetacloud.com)，工作目录 `/root/xling_calib_direction`
- Python：`/root/miniconda3/bin/python`（conda base 环境）
- 模型路径：`/root/autodl-tmp/models/Llama4-Scout-W4A16`（~66GB W4A16）、`/root/autodl-tmp/models/Qwen3-235B-A22B-GPTQ-Int4`（~122GB GPTQ-Int4）
- HF cache：`/root/autodl-tmp/.hf_cache`
- 活跃进程（待确认）：Llama4 下载 PID 53308、Qwen3 下载 PID 53359 — Agent 刚被派去检查状态，尚未回复
- 关键脚本已就绪：`run_plan_001.sh`（Qwen3）、`run_plan_002.sh`（Llama4）、`compute_cka.py`、`pareto_analysis.py`

### 3. 📊 当前状态
刚派出三路任务，均未收到回复：
1. **Agent**：检查 Llama4/Qwen3 下载进度 + 运行 pareto_analysis.py（CPU 任务）+ 诊断 plan_013_v2 失败原因。Agent 正在 processing。
2. **Paper Agent**：Related Work 已写完初稿（~1000 words, 23 citations），Reviewer 审查发现 4 个 warning（CaCLR 写成既定事实、缺 Pires/Wu&Dredze 引用、Simpson's Paradox 过度宣称、CKA 过度宣称），已派 Paper Agent 修订。Method section 已完成并修正。
3. **Dream** `dream_20260521T044911`：status=reviewing（imagine+write 已完成），full review mode，等待完成回调。

Registry：5 个实验全 DONE (4 success)，plan_013_probing_controls_v2 PREPARING(failed) 待诊断。4 张 GPU 全空闲等模型下载。

### 4. 📋 待办
- Agent 回复下载状态 → Llama4 完成则验证模型完整性 → 提交 plan_002 审批 → 分配 GPU 启动
- Qwen3 下载完成 → 验证 → 提交 plan_001 审批 → 分配剩余 GPU
- Dream 完成回调 → Read dream-report-action skill → 按三档审稿结果调整 framing/plan
- plan_001 + plan_002 数据产出后 → 启动 plan_011 全量 CKA 分析（20 languages，决定性新颖性实验）
- Pareto analysis 输出 → 回应审稿 issue R2-N2（Pareto 形式化验证）
- Paper Agent Related Work 修订完成 → Reviewer 再审 → 合入

### 5. 🎯 战略上下文
- **核心 story**：Simpson's Paradox in CKA-transfer（raw correlation negative, partial positive）是论文新颖性支柱（D012）。plan_011 全量 CKA 是决定性实验——Llama pilot rho=+0.41 p=0.006 显著，Qwen pilot rho=+0.18 p=0.274 不显著，20 语言全量数据必须确认。
- **审稿状态**：Round 0 得分 2.5/5 Weak Reject（R1=3.0, R2=2.0）。6 critical + 9 warning，全部 open（review_issues.yaml）。用户要求"迅速针对性修改 + re-dream"，re-dream 已触发。
- **CaCLR 双面叙事**：paper_framing.md 已设计 positive/negative 两种结果叙事。plan_003 未执行前，Related Work 中 CaCLR 结论必须用条件式。
- **易错点**：(1) 模型大小不要凭 Agent 报告拍决策，必须从 HF metadata 验证（M008 教训）；(2) Procrustes 并行对的 EN 端必须用 eval split 不是 train split；(3) CaCLR 的 MMD 必须操作 probe logits 不是 raw activations（M007）
- **决策链关键节点**：D012（novelty strategy：CKA partial correlation 是 pivot，Claim 4 降级，control task + projection 升主体）→ 当前所有实验优先级围绕此决策排列
