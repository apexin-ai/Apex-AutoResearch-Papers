---
loop: 20
reason: max_messages
updated: '2026-05-28T05:59:06+00:00'
---

### 1. 🔴 硬约束 / 红线
- 4 台服务器各自的 GPU 全部属于本项目：westd-27271(2卡), westd-38929(4卡), westd-41074(4卡), cqa1-33015(4卡) = 14 张
- w27 **不支持 attention scoring**——只能跑 L2norm 或 Random 实验
- 实验硬截止 C002：**May 28 20:00 BJT**（12:00 UTC），之后停止新部署，全面收割
- CoRL 2026 论文截止：**May 29**
- seed 编号：s42/s43=2-seed baseline, s44=third seed, s45=fourth seed, s46=fifth seed（刚部署）
- experiment_plan.yaml 当前为空（0 entries），覆盖率通过 provenance 追踪（101/109）
- 审稿阶段已启动，review_chat_id: oc_83179cdc26b856fbbaf531d145edb3bd

### 2. 🖥️ 基础设施快照
- 4 台 AutoDL 服务器，工作目录均为 `/root/autodl-tmp/importance_margin_vla_compress`
- westd-27271: connect.westd.seetacloud.com, root
- westd-38929: connect.westd.seetacloud.com, root
- westd-41074: connect.westd.seetacloud.com, root
- cqa1-33015: connect.cqa1.seetacloud.com, root
- 镜像：aml-train（conda base 环境，Python at /root/miniconda3/bin/python）
- HF cache: /root/autodl-tmp/.hf_cache
- W&B: 未配置
- Paper artifacts: 本地 `projects/importance_margin_vla_compress/artifacts/`

### 3. 📊 当前状态
**刚做完**：全服务器 GPU 诊断 + 大批 s45 收割（8 个实验）+ 最终批次 s46 部署 + OV seed43 加固

**RUNNING 实验（13 个）**：
| 服务器 | GPU | 实验 | ETA |
|--------|-----|------|-----|
| w38:0 | random_k095_s45 | ~2h |
| w38:1 | l2norm_k095_s45 | ~1h |
| w38:2 | random_k07_s45 | ~2h |
| w38:3 | attn_k085_s46 | ~3h |
| w41:0 | random_k085_s46 | ~3h |
| w41:1 | ov_random_k095_long_s43 | ~3h |
| w41:2 | l2norm_k075_s46 | ~3h |
| w41:3 | attn_k07_s45 | ~2h |
| w27:0 | ov_l2norm_k095_long_s43 | ~3h |
| w27:1 | random_k07_s44 | 即将完成 |
| cqa1:0 | l2norm_k05_s45 | ~30min |
| cqa1:1 | attn_k095_s45 | ~15min |
| cqa1:2 | ov_random_k095_goal_v4 | ~3h |

**cqa1:cuda:3 预留**，等数据整合 Worker 结果决定部署什么。

**等待中**：数据整合 Worker（CPU，汇总 s42-s46 四/五 seed 表，5-10min 出结果）

### 4. 📋 待办
- 数据整合 Worker 完成 → 审查 outlier 报告 → 有问题用 cqa1:cuda:3 做验证性重跑，无问题部署 s46 下一个高 variance 点
- w27:cuda:1 random_k07_s44 完成（~几分钟）→ 收割，部署 s46 或 OV seed43
- cqa1:cuda:1 attn_k095_s45 完成（~15min）→ 收割，确认四 seed 数据（前三 seed 均值 77.8%）
- cqa1:cuda:0 l2norm_k05_s45 完成（~30min）→ 收割，与在跑的 s45 52.9% 中间值对比
- 所有 s45 实验完成 → 更新 ROADMAP Importance Margin Profile 表为四 seed 版本
- 所有 s46 实验完成 → 五 seed 误差棒更新到论文
- **11:30 UTC（截止前 30min）→ 停止所有新部署，全面收割**
- 全部收割完 → Paper Agent 更新 figures + tables → 最终编译 → 提交审稿

### 5. 🎯 战略上下文
**核心结论**：VLA vision token 的 importance scoring（L2norm）在中-高压缩率（k=0.7-0.95）显著优于 Random，margin 呈 inverted-U 形状，peak 在 k=0.9（+46pp）。Attention scoring 呈 cliff+plateau（k>0.9 有效，k≤0.85 崩到 Random 水平）。k=0.7 处 L2norm 与 Random crossover。

**关键数据质量**：
- Peak margin k=0.9 四 seed 高度收敛：L2norm 80.4%±0.5, Random 33.6%±1.3
- Attn k=0.9 四 seed 64.0%±0.8pp
- L2 k=0.5 修正后 margin +1.0pp（s42 seed 对调问题已纠正，Paper Agent v226 已更新）

**易踩的坑**：
- Attn k=0.75 seed43 有跨服务器 discrepancy（w27=49.0% vs cqa1=52.0%），统一用 cqa1=52.0%，因为 w27 不支持 attention scoring
- Random k=0.9 seed43 用 v2=35.0%（D292），不引用旧版 32.4%
- ROADMAP 中的 Importance Margin Profile 表还是旧的 L2norm k=0.5=51.0%，Paper Agent 已修正为 51.5%
- Registry 与实际 GPU 状态容易漂移——诊断时 SSH 实查，不要只看 registry
- report.md 资源状态段全显示"无 GPU 信息"（数据陈旧），需调 auto_build_report_facts 刷新
