# director / loop_3.md

**Instruction Routing in Fine-Tuned Vision-Language-Action Models: A Cross-Architecture Analysis** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/director/loop_3.md`
- **Structured JSON:** [`99b390c2460d2d02157c.json`](../../sessions/99/99b390c2460d2d02157c.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 3
reason: max_messages
updated: '2026-05-17T08:01:09+00:00'
---

### 1. 🔴 硬约束 / 红线
- GPU 只能用 westd-19183 的 cuda:0 + cuda:1（项目配置 `execution.gpu_ids`）
- 论文 8 页硬限（CoRL 2026），References 从 page 9 开始是 OK 的
- C2 措辞最终决策(D054)：标题用 "Front-Loads"，正文用 "shifts...from...to..."（Option B），不用 "reorganizes" 做 header。正文可说 "consistent with a reorganization" 一次
- Paper Agent 队列中有冲突指令（先 "reorganizes" 升级，后 "shifts/front-loads" 降级）——以最后一条"最终决策 Option B"为准。如果 Paper Agent 汇报用了 "reorganizes" 做标题，需要纠正回 "Front-Loads"
- 审稿阶段已启动（review_chat_id: oc_554a5023cde4d603635cf97e6ab8151a）

### 2. 🖥️ 基础设施快照
- 服务器：westd-19183 (connect.westd.seetacloud.com)，2× RTX PRO 6000
- 远程工作目录：/root/vla-ssd（代码），/root/autodl-tmp/vla-ssd/（数据/结果/checkpoints）
- Checkpoints：/root/autodl-tmp/vla-ssd/checkpoints/openvla-7b-llama2base/（Llama-2 base 控制）
- 结果 JSON：/root/autodl-tmp/vla-ssd/results/attention/full_32layer_attention_summary.json
- 论文本地路径：projects/vla-ssd/docs/paper/（main.tex 等）
- 活跃进程：无 GPU 进程。Agent 有 1 CPU Worker 做 32 层 figure 文件传输

### 3. 📊 当前状态
**刚做完**：Round 1-2 审稿全部修复已派发。P0 实验（Llama-2 base 三条件对照）已完成，32 层 attention 已完成。所有 figures 已生成。

**进行中**：
- Agent 正在重新传输正确的 32 层 attention figure（旧文件是 4 层副本错误，Critical fix）
- Paper Agent 队列有 3-4 条指令待处理：(1) 最终决策 Option B "shifts/front-loads" (2) Hotfix consistency issues (3) 数字不一致确认 (4) figure 整合

**等待**：
- Agent 交付正确的 fig_32layer_attention.pdf → Paper Agent 替换占位图
- Paper Agent 处理完所有 queue → Phase E 验证 → 提交 Round 3 内部审稿

### 4. 📋 待办
- Agent 汇报 32 层 figure 文件到位 → 通知 Paper Agent 替换 `figures/fig_32layer_attention.pdf`，确认 MD5 ≠ 旧 4 层版本
- Paper Agent 完成所有 patch → 确认 §4.3 标题是 "Front-Loads"（不是 "Reorganizes"）→ 启动 Phase E
- Phase E 通过 → `submit_paper_to_review` 提交 Round 3 内部审稿（recommended_review_mode="continue"）
- Round 3 结果到手 → 评估是否达 6/10 accept threshold → 如果是，准备 May 26 Abstract 提交
- GPU 空闲且无实验需求 → 可以考虑 LIBERO-Spatial 交叉验证（experiment_plan 中有 plan010_rsa_spatial 和 plan010_action_probe_spatial 待跑）

### 5. 🎯 战略上下文
- **核心发现**：三条件梯度（random 0 → pretrained 9 → VLA-trained 24-25 instruction heads at L1）+ 深层稳定性来自预训练（非 VLA）+ 32 层 temporal shift pattern
- **决策链**：D048(Plan B reframe) → D049(Llama-2 base P0) → D050(三级梯度确认) → D051(深层稳定性归因修正) → D052(temporal reorganization) → D053(降级 front-loads) → D054(32层数据升级回来，但用 Option B "shifts" 措辞)
- **最容易判断错的事**：Paper Agent 可能仍在用 "reorganizes" 做标题（因为队列先处理了升级指令）。必须确认最终标题是 "VLA Fine-Tuning Front-Loads Instruction Routing"
- **R1-N1 (baseline confound)** 已实质解决（有数据），但论文必须正确整合三条件数据为 lead evidence
- **数据一致性陷阱**：L1 dedicated analysis=25/32, 32层bulk=24/32（±1 threshold boundary）。两组各用各的，加注释说明
- **Timeline**：May 26 Abstract DDL, May 29 Paper DDL。Round 3 审稿 + polish 还有 ~9 天
- **审稿预测**：Path A (数据+修复) → R1:6, R2:5.5, R3:7.5 → 6.3/10 = borderline accept


---
