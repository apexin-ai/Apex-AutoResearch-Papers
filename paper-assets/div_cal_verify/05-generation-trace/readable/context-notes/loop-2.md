# director / loop_2.md

**The Embedding Alignment Gap: Why Diversity-Based Data Selection Accelerates Model Collapse in Iterative Self-Training** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/director/loop_2.md`
- **Structured JSON:** [`15dca2457d85748b1f29.json`](../../sessions/15/15dca2457d85748b1f29.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 2
reason: max_messages
updated: '2026-05-14T03:09:44+00:00'
---

### 1. 🔴 硬约束 / 红线
- GPU 只能用 westd-11235 的 cuda:0 和 cuda:1（项目分配，不可越界）
- 355M 实验用 GPT2-medium，脚本在 `/root/div_cal_verify/` 下，seed 只改脚本参数不改架构
- S3 claim（random pruning as regularizer）已降级为 directional observation（D017），不可作为核心 claim 使用
- C2 已修正为 C2-revised："问题特异于内部嵌入"（定性强、定量弱化），framing 不可回退到旧版 C2-weak

### 2. 🖥️ 基础设施快照
- 服务器：westd-11235 (connect.westd.seetacloud.com)，用户 root
- 工作目录：/root/div_cal_verify
- GPU：2× RTX PRO 6000 98GB
- 活跃进程：chain_cuda0_s123（medium_uncurated_seed123 → rgds → random50，cuda:0）；medium_external_seed42 + 自动衔接 medium_external_seed123（cuda:1）
- 无 W&B 配置，实验结果通过脚本输出 + 本地日志收集
- 论文源文件在本地 workspace：`projects/div_cal_verify/artifacts/`

### 3. 📊 当前状态
刚完成：medium_random50_seed42（Gen7 PPL=70.25），C3 在 355M 确认成立。
已派 Agent 部署 355M seed=123 chain（cuda:0: uncurated→rgds→random50；cuda:1: external_seed42 完成后接 external_seed123）。
已派 Paper Agent 推进 Results scaling subsection + Discussion 深化 + 统计检验表格模板（用已有 seed=42 数据）。
派了 Agent 确认 GPU 实际利用率（催促提到健康数据不一致），尚未收到回复。

RUNNING：medium_uncurated_seed123（cuda:0）、medium_external_seed42（cuda:1）
预计完成：cuda:1 ~15:00 CST，cuda:0 全 chain ~18:00 CST

审稿阶段已启动（review_chat_id: oc_414af80ee2310359595c5840d1c8b4b9），Group C 独立处理。
Reviewer 刚批准 RESET_BOTH。

### 4. 📋 待办
- medium_external_seed42 完成 → 确认 355M 四方法 seed=42 全景（Random/RGDS/Uncurated/External）→ 更新论文 scaling narrative
- medium_external_seed42 完成 → 自动衔接 medium_external_seed123，确认 chain 启动成功
- cuda:0 chain 全部完成（uncurated/rgds/random50 seed=123）→ 355M 2-seed t-test → 派 Paper Agent Patch 填入统计检验数据
- 全部 355M seed=123 完成 → 更新 ROADMAP dashboard + 决策日志
- Paper Agent 回复 Results/Discussion 初稿 → 审阅叙事线是否与 D014 framing 一致
- Agent GPU 利用率确认回复 → 如有卡空闲立即派补充实验

### 5. 🎯 战略上下文
- DDL：EMNLP 2026 ARR **2026-05-25**（还剩 11 天）
- 三核心 claim：C1（ratio 退化 1.04→0.52）强 ✅ | C3（RGDS > Random 同 budget）强 ✅ 跨 scale | C2-revised（内部嵌入特异性）定性强 ✅
- 355M 关键发现：RGDS 不再是最差（Uncurated 91.66 > RGDS 82.84），但同 budget RGDS 仍劣于 Random（82.84 vs 70.25）→ C3 锚定在"同 budget 对比"而非"绝对最差"
- 125M 与 355M 模式差异：125M RGDS 是唯一灾难性方法（+74%），355M 差距缩小（+18%）→ alignment gap 随 scale 缩小但不消失，这是 Discussion 的核心论点
- 易错点：不要把 355M 的 Uncurated（100% data）与 Random/RGDS（50% data）直接对比得出"裁剪更好"的因果结论——数据量差异是混淆因素，S3 已降级（D017）
- Intro + Methodology 初稿已完成，Related work 36 篇到位，Paper Agent 正在推进 Results
- experiment_plan.yaml 当前为空（实验通过 registry 管理），如需 coverage matrix 用 compute_coverage_matrix() 派生


---
