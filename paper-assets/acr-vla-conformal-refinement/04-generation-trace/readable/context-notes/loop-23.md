# director / loop_23.md

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/director/loop_23.md`
- **Structured JSON:** [`54013ea07cfb223ffc21.json`](../../sessions/54/54013ea07cfb223ffc21.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 23
reason: max_messages
updated: '2026-05-26T05:53:15+00:00'
---

### 1. 🔴 硬约束 / 红线
- 方法核心是 **K=2 + gating**，evaluate.py hardcodes K=2 for Adaptive。CRM 模式用 `--K 2`（π0.5）或 `--K 10`（SmolVLA）。**不要改 K=2 硬编码。**
- Table 1 (SmolVLA) 统一用 **s42/s43/44**，论文只说"3 seeds"**不标具体编号**（D157 最终决策）
- Appendix 放 3 seed 的 analytical metrics（trigger rate, uncertainty），**不放 SR 值，不标 seed 编号**
- π0.5 CRM checkpoint 和 SmolVLA CRM checkpoint 输入维度不同（2118 vs 990），**不可互换**——已验证无误
- cqa1 上 **最多同时 3-4 个 π0.5 进程**，6 个并发会 OOM crash（已发生过）
- bjb2-40593 已下线，替代为 bjb2-24035（1 GPU）和 westd-49937（6 GPU）

### 2. 🖥️ 基础设施快照
| 服务器 | GPU | 用途 | 备注 |
|--------|-----|------|------|
| bjb1-18228 | 4× RTX 4090 | π0.5 实验 | AutoDL，重启后恢复 |
| bjb1-32546 | 6× RTX 4090 | π0.5 CRM K=2（刚从 SmolVLA 转） | SmolVLA Table 1 数据源服务器 |
| bjb2-28827 | 6× RTX 4090 | π0.5 部署中 | 需先传 π0.5 模型/CRM checkpoint |
| bjb2-24035 | 1× RTX 4090D | π0.5 Adaptive Object s43 | 替代旧 bjb2-40593 |
| cqa1-32758 | 6× RTX 4090 | GPU 0-2 τ-sweep, GPU 3-5 π0.5 部署中 | 最多 3-4 并发 π0.5 |
| westd-49937 | 6× RTX PRO 6000 (98GB) | π0.5 Adaptive Goal×3 + Object + K2mean + CRM Goal | 新增，Manager 批的扩容 |

- 模型路径（各服务器）：`/root/autodl-tmp/models/pi05_libero_finetuned/` 或 `/root/models/pi05_libero_finetuned/`
- CRM checkpoint：`crm_pi05_unified_3suite/crm_best.pt`（π0.5），`crm_best.pt`（SmolVLA）
- 代码：evaluate.py（各服务器本地），Adaptive 模式 K=2 硬编码在 line ~464

### 3. 📊 当前状态
**刚做完**：westd-49937 搭建完成 6 实验全跑起；bjb1-32546/bjb2-28827/cqa1 空闲 GPU 紧急部署指令已发。

**RUNNING 实验（~26 GPU）**：
- westd-49937 (6): Adaptive Goal s42/43/44, Adaptive Object s42, K2mean Goal s42, CRM Goal s42
- bjb1-18228 (4): CRM Long s42-r2, CRM Long s43-r2, K2mean Goal s42-r2, Adaptive Long s42-r2
- bjb1-32546 (6): CRM K=2 Goal s42/43/44, CRM K=2 Object s42/43/44（刚部署）
- bjb2-28827 (6): CRM Spatial s42/43/44 + Adaptive Spatial s42/43/44（部署中，需传模型）
- bjb2-24035 (1): Adaptive Object s43
- cqa1 GPU 0-2 (3): τ-sweep τ=0.50/0.70/0.90 Goal s42
- cqa1 GPU 3-5 (3): Adaptive Object s44 + Adaptive Long s43/s44（部署中）

**等待中**：bjb2-28827 部署 Worker 回调、cqa1 GPU 3-5 部署 Worker 回调、τ-sweep 完成

**已完成关键数据**：
- SmolVLA Table 1 已锁定（s42/43/44）
- π0.5 CRM Long s44 = 80.0%（VLA-only 95.0% → Δ=-15pp）
- π0.5 VLA-only baselines 全 4 suite × 3 seed 完成（Spatial 98.2%, Goal 97.8%, Object 99.3%, Long 95.0%）

### 4. 📋 待办（条件触发式）
- bjb2-28827 Worker 回调 → 确认 6 个 π0.5 实验启动成功，否则排查模型传输问题
- cqa1 τ-sweep 完成 → harvest τ=0.50/0.70/0.90 结果，分析 π0.5 τ-sweep 曲线
- π0.5 CRM Goal/Object/Spatial 3-seed 完成 → 汇总 Table 2，与 VLA-only baseline 对比
- π0.5 Adaptive 全 4 suite × 3 seed 完成 → Table 2 定稿，计算 Δ 和 trigger rate
- Table 2 数据齐全 → 派 Paper Agent 写论文（用户要求 π0.5 专门一段分析机理）
- bjb1-32546 SmolVLA 已完成 → 如还有未 harvest 的 SmolVLA 数据，先收割再转 π0.5
- 用户要求 abstract：单段 4-6 句，不罗列数字（已发送修订版，用户未反馈是否满意）

### 5. 🎯 战略上下文
**核心结论**：ACR-VLA 对 SmolVLA（弱模型）有效，对 π0.5（强模型）CRM 造成严重退化（Goal -11.7pp, Object -11.3pp, Long -14.5pp）。用户决定将 π0.5 负向结果作为**贡献**——专门一段分析"方法有效性与模型能力的关系"，需实验验证机理。

**决策链关键节点**：
- D152: Table 1 统一 s42/43/44
- D153: π0.5 CRM 从 K=10 切 K=2
- D155: 放弃 MC3 "cross-model generalization" claim，改为 analysis contribution
- D157: 论文不标 seed 编号

**易错点**：
- Agent 曾混淆 SmolVLA baseline（~58%）和 π0.5 baseline（~95%），已纠正。核实任何 baseline 数据必须标 exp_id 来源
- π0.5 r3 vs r4 版本差距 15-18pp（代码版本不同），Table 2 必须用 r4 版本
- CRM 模式的 `--K` 参数对 π0.5 必须是 2（D153），对 SmolVLA 是 10
- CoRL DDL **May 29**（还有 ~3 天），Paper Agent 尚未启动，Table 2 数据齐全后需立即启动论文写作


---
