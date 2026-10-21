# agent / loop_22.md

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/agent/loop_22.md`
- **Structured JSON:** [`52ff5fcd7aee6ef4f758.json`](../../sessions/52/52ff5fcd7aee6ef4f758.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 22
reason: idle_timeout
updated: '2026-05-21T02:44:19+00:00'
---

### 1. 🔴 硬约束 / 红线
- GPU 白名单：bjb2-40593:cuda:0, bjb1-18228:cuda:0-3, bjb1-32546:cuda:0-5, bjb2-28827:cuda:0-5（共 17 张）。白名单外的 GPU 即使 Director 指令也必须 push back
- bjb2-40593 磁盘 90% 已满⚠️，禁止在该服务器下载模型/数据/写大文件
- Long OOD 结论已降级为 cautious wording（D081: MW-U p=0.061 n.s.），论文中不可写 "significant"
- D084: eval-obs-only-object-norm02-seed42 (SR=20%) 已决定不纳入 Table 1（离群点）
- Adaptive K P50 是论文核心贡献（D077 用户硬要求），K=10 分析只是 supporting evidence
- CoRL 2026 DDL 2026-05-29，剩余 ~8 天

### 2. 🖥️ 基础设施快照
- **bjb1-18228**: /root/acr-vla-conformal-refinement, conda base (/root/miniconda3), 磁盘 4%用（充裕）
- **bjb1-32546**: /root/acr-vla-conformal-refinement, account=root, 磁盘 4%用
- **bjb2-28827**: /root/acr-vla-conformal-refinement, account=root, 磁盘 5%用（6 GPU 全空闲）
- **bjb2-40593**: /root/acr-vla-conformal-refinement, 磁盘 90%⚠️
- 模型路径: /root/autodl-tmp/models/smolvla_libero/（所有服务器）
- HF cache: /root/autodl-tmp/.hf_cache
- 环境激活: `source /root/miniconda3/etc/profile.d/conda.sh && conda activate base`
- 活跃 cron 7 个（reconcile 刚跑过），对应 7 个 RUNNING 实验

### 3. 📊 当前状态
**刚完成**：eval-vla-only-long-seed49-r2 → DONE(success), SR=16.0%，确认原始 seed49 数据溯源完整性。已更新 registry + 汇报 Director。

**RUNNING (7)**:
1. eval-adaptive-k-spatial-p50-seed42 — bjb2-40593:cuda:0（Spatial Adaptive K 核心实验）
2. eval-adaptive-k-spatial-p25-seed42 — bjb1-18228:cuda:2
3. eval-adaptive-k-spatial-p75-seed43 — bjb1-32546:cuda:1
4. eval-adaptive-k-spatial-p25-seed43 — bjb1-32546:cuda:2
5. eval-crm-object-k20-seed43 — bjb1-32546:cuda:3
6. eval-obs-only-object-norm003-seed43-r2 — bjb1-32546:cuda:4
7. eval-obs-only-object-norm005-seed44 — bjb1-32546:cuda:5

**Worker 活跃 (1)**: worker_diagnose_eval-adaptive-k-spatial-p50-seed42（诊断中，启动于 05-20T10:31）

**等待中**：
- 已向 Director 汇报资源警告（10/17 GPU 空闲），等待批准部署 QUEUED/PREPARING 实验
- 3 个 QUEUED: eval-obs-only-object-norm003-seed44, eval-obs-only-object-norm005-seed43, eval-crm-object-k20-seed44
- 33 个 PREPARING（Long/Spatial/Goal 多 seed 补充）

### 4. 📋 待办
- Director 批准部署 → 立即在 bjb2-28827 (6 free) + bjb1-18228:cuda:0,1,3 (3 free) + bjb1-32546:cuda:0 (1 free) 上铺满实验
- eval-adaptive-k-spatial-p50-seed42 完成 → 这是 Spatial Adaptive K 核心数据点，需仔细分析 SR vs avg_K vs fast_path%，对比 Object P50 结果
- 任一 Spatial Adaptive K 完成 → 更新 ROADMAP Spatial Adaptive K 表格，检查是否与 Object 趋势一致
- Worker diagnose 完成 → 读取诊断结果，必要时重启或调整实验
- 7 个 RUNNING 实验陆续完成 → 按 on-experiment-done 流程逐个处理
- 所有 Spatial Adaptive K seeds 完毕 → 汇总 cross-benchmark validation 结论，更新论文 narrative

### 5. 🎯 战略上下文
- **核心 narrative**: Adaptive K (K=2 L2 distance 信号) 是论文第一贡献。Object P50 已完成 12/12 全 DONE，Pareto 最优确认（SR~91% of K=10, compute savings ~77%）
- **关键决策链**: D076(K=2 L2 GO) → D077(Adaptive K 升核心) → D078(P50 Pareto 最优) → D079(CRM magnitude NO-GO) → D080(Table 1 norm02 n=6) → D081(Long OOD cautious) → D082(batched inference 确认) → D083(Spatial CRM clean n=8) → D084(seed42 离群不纳入)
- **最容易判断错的事**: (1) Long OOD 差异不显著(p=0.061)，不要在论文中过度宣称；(2) bjb2-40593 磁盘快满，别往上面部署新实验；(3) Spatial Adaptive K 实验是当前最高优先级——cross-benchmark validation 直接支撑核心 claim
- **资源瓶颈**: 10/17 GPU 空闲是失职状态，新 session 第一件事应催促 Director 批准部署或自行提交已审批的 QUEUED 实验


---
