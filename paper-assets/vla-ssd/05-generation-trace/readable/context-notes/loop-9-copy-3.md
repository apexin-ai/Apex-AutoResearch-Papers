# reviewer / loop_9.md

**Instruction Routing in Fine-Tuned Vision-Language-Action Models: A Cross-Architecture Analysis** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/reviewer/loop_9.md`
- **Structured JSON:** [`971beb4ddc7549c2d2b2.json`](../../sessions/97/971beb4ddc7549c2d2b2.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 9
reason: max_wall_time
updated: '2026-05-17T21:57:17+00:00'
---

### 1. 🔴 硬约束 / 红线
- GPU 白名单：cuda:0 和 cuda:1（gpu_ids=[0,1]），越界立即 critical
- 消融代码用 INSTRUCTION_HEADS_24 = 24 个头，但 Abstract 写 "21--25 heads"、Table 2 写 "25/32"。三个数字不统一，尚未确认 ground truth。审查论文时必须追踪此不一致是否已修复
- Llama-2 base probe 脚本内部写 GPU=0 但 launch 用 CUDA_VISIBLE_DEVICES=1（映射正确），不要误判为越界

### 2. 🖥️ 基础设施快照
- 服务器：westd-19183，代码根目录 /root/vla-ssd
- Python：/root/miniconda3/bin/python3.12
- 模型：/root/autodl-tmp/vla-ssd/checkpoints/openvla-7b（VLA trained）、openvla-7b-llama2base（Llama-2 base）
- 数据：/root/autodl-tmp/vla-ssd/data/libero/libero_goal/（10 tasks × 50 demos）
- 结果：/root/autodl-tmp/vla-ssd/results/（l1_head_ablation/, functional_validation/, attention/, action_probe/）
- 特征缓存：/root/autodl-tmp/vla-ssd/features/llama2base_libero_goal/（10/10 h5 已提取完）
- 活跃进程：llama2base_action_probe PID 913317（tmux 无，直接 bash -c 启动），cuda:1，Phase 2 probe 训练中（CPU-bound，GPU 0% 正常）
- control8 tmux session l1_head_ablation_control8 仍在但进程已退出（EXIT_CODE=0）

### 3. 📊 当前状态
刚完成 50-demo L1 消融全量结果审查并发送 Director 两条报告（主报告 + 特异性配对检验补充）。

**Registry：**
- llama2base_action_probe: RUNNING — Llama-2 base 33 层 action probe，特征提取完成，probe 训练中
- l1_head_ablation_50demos: PREPARING — 旧 entry，实际工作已拆分到 ablation_50demos_main/control8（均 DONE）
- 其余 70 个实验全部 DONE

**等待中：**
- llama2base_action_probe 完成 → 核实三条件梯度（untrained < llama2base < trained）
- Paper Agent Round 5 提交 → 章节写作审查
- head count 不一致修复确认

### 4. 📋 待办
- llama2base_action_probe 完成（检查 /root/autodl-tmp/vla-ssd/results/action_probe/llama2base_action_probe.json 或 exit file）→ 读结果，核实 R² 是否满足 untrained < llama2base < trained 梯度，发 Director 报告
- Paper Agent 提交章节审查 → 按 5.1-5.3 维度审查，重点检查：消融数据是否更新为 50-demo、head count 是否统一、C3 是否降级为 observation、CKA 叙事是否诚实
- Director 转发 framing 调整提案 → Read negative-framing-review skill，四维度审查
- 如发现 cuda:0/1 外有新进程 → 立即 critical

### 5. 🎯 战略上下文
- 论文目标 CoRL 2026（Abstract DDL 5/26，Paper DDL 5/29），接受率估 35-50%
- 核心叙事已 reframe：C1 降为 methodological framework（causal mask 使 image blindness 成架构属性），C2 升为核心 claim（front-loaded routing + 因果消融证据），C3 降为 observation（RSA inverted-U 是 metric-dependent，CKA 单调增）
- 50-demo 消融是 N3 response 的关键弹药：Δ=+0.059, p<0.0001，层特异性 + 头特异性均确认
- **易错点**：
  1. 不要把 5-demo 和 50-demo 消融数据混用（效应量差 ~2×）
  2. RSA "rise" Δρ=+0.016 是 borderline n.s.（p=0.053），论文应写 "stable" 而非 "rises"
  3. control8 有小但可能不显著的效应（Δ=+0.017），不要声称 control 完全无效应
  4. GPU 预算已紧张（~26h 总量，~20-22h 已用），llama2base probe 后基本耗尽


---
