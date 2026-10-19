---
loop: 3
reason: max_messages
updated: '2026-05-25T20:18:18+00:00'
---

### 1. 🔴 硬约束 / 红线
- 本项目只能用 westd-14391 的 cuda:0（唯一 1 张 RTX PRO 6000 Blackwell 96GB）
- experiments.tex L161 刚修复了 CRITICAL 数据混用错误（30-test correction: α=+10 p=0.0003 来自 N=201 被错误放在 N=136 上下文），改为 α=-20 p<0.001。**绝不能回滚这个修改**
- Table 1 的 77.6%（全量 N=1368）和 92.7%（matched-condition N=201）是两个不同实验，不要混淆报告
- 论文正文 8 页限制（EMNLP 2026 ARR），当前合规

### 2. 🖥️ 基础设施快照
- 服务器：westd-14391，工作目录 /root/clkc_mech_interp
- Python：/root/miniconda3/bin/python（conda base）
- 模型路径：Llama=/root/autodl-tmp/models/LLM-Research/Meta-Llama-3.1-8B-Instruct, Qwen=/root/autodl-tmp/models/Qwen/Qwen3-8B, Gemma=/root/autodl-tmp/models/AI-ModelScope/gemma-2-9b-it
- 论文本地路径：projects/clkc_mech_interp/docs/paper/
- 活跃进程：刚派了 3 个 Worker（sync-compile-pdf / regen-bootstrap-n2000 / regen-token-overlap），bootstrap 被阻塞等 ZH activations 重生成，已派新指令让 Agent 用 GPU 跑 collect_activations

### 3. 📊 当前状态
刚完成全文 ~260 个数字的数据真实性审计，已向用户发送完整报告。发现并修复 1 个 CRITICAL 错误（30-test correction 数据混用）。

Agent 正在执行：
1. Worker 1: 同步修复后的 experiments.tex + 编译 PDF — 应该快完成或已完成
2. Worker 2: 被阻塞 → 已追加指令让 Agent 用 cuda:0 重新生成 Llama/Qwen ZH activations（collect_activations.py），完成后跑 bootstrap_n2000
3. Worker 3: token overlap 脚本也被阻塞（同一根因：ZH/DE 数据缺失）

等待中：Agent 的 Worker 回调（编译结果 + ZH activations 进度）

### 4. 📋 待办
- Worker 1 (compile) 完成 → 下载 PDF 到 artifacts/ 并上传给用户
- Llama ZH activations 生成完成 → 接着跑 Qwen ZH activations → 两者完成后跑 bootstrap_n2000
- bootstrap_n2000 输出 → 核对 Table 1：Llama EN→EN=77.6% @L15, ZH→EN=70.6%, Δ=+7.3 CI [0.4,14.0]; Qwen EN→EN=75.0% @L24, Δ=+7.2 CI [-0.6,13.7]
- 如果数字不匹配 → CRITICAL 上报用户；匹配 → 确认审计完成
- token overlap 数据生成后核对：EN-ZH Jaccard ~3-4%, EN-DE ~14.8%, r=-0.15
- 全部验证通过 → 通知用户审计彻底完成，所有数字可追溯
- 项目已进入审稿阶段（review_chat_id: oc_8b9aa92fafaf69b48d2c44b41c2fe9d9），修复后可能需要重新提交审稿

### 5. 🎯 战略上下文
- 核心论文：跨语言知识冲突信号的线性可检测性 + detection≠decision 解离，投 EMNLP 2026 ARR
- 关键发现：ZH→EN 迁移优势 ~7pp 匹配 XNLI baseline（一般跨语言属性，非冲突特有）；Llama L13 causal steering 成功但 Qwen/Gemma 失败（Gemma 88.9% probe acc 仍无 steering effect）
- 易错点：服务器上 N=136 原始 steering 文件已被 N=201 覆盖，不要把 N=201 的 p 值放进 N=136 上下文（刚修的 bug）
- 易错点：probe_per_layer.json 是 matched-condition 数据，Table 1 是全量数据，准确率差 ~15pp 是正常的
- paper_provenance.yaml 仍有旧值（77.1%/75.3%），已跑 auto_build_provenance 但手动更新可能仍需要
- decisions.yaml D004 的 ZH→EN=71.3% 是旧值（n=100 bootstrap），论文用 70.6%（n=2000），不是错误
