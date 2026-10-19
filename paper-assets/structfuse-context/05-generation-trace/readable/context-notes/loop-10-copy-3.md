# reviewer / loop_10.md

**StructFuse: Structure-Grounded Hard Negative Mining for Contrastive Code Context Retrieval** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/reviewer/loop_10.md`
- **Structured JSON:** [`43cf5425394529aca844.json`](../../sessions/43/43cf5425394529aca844.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 10
reason: max_wall_time
updated: '2026-05-15T10:03:25+00:00'
---

### 1. 🔴 硬约束 / 红线
- GPU 白名单：bjb1-42106 只能用 cuda:0 和 cuda:1，越界立即 CRITICAL
- eval_swebench_e2e.py 硬编码 "cuda"（无 --device），运行前必须设 CUDA_VISIBLE_DEVICES
- s42 (Qwen random) 在旧 D026 regime 下训练（3 epochs, no early stop），与 s43/s44 regime 不同（2 epochs, patience=2）——cross-seed 比较时必须披露或重跑
- 论文数字必须来自 pool=50 独立评估（D042），不能用训练时 pool=8 eval 数字

### 2. 🖥️ 基础设施快照
- 服务器：bjb1-42106 (root)，双卡 NVIDIA RTX PRO 6000 Blackwell (98GB each)
- 远程代码：/root/structfuse/，训练日志：/root/runs/m2_full_qwen/ 和 /root/runs/m2_full_starcoder/
- Checkpoints：/root/autodl-tmp/structfuse/checkpoints/m2_full_{qwen,starcoder}/
- 本地 workspace：/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/
- references.bib 在本地 workspace (artifacts/paper_drafts/)，不在远程
- wandb: offline 模式，日志在 /root/structfuse-context/wandb/ 和 /root/autodl-tmp/structfuse/wandb_logs/wandb/
- GPU0 PID 891739: Qwen embedding_distance_s44（step ~850，R@1=0.5942@500）
- GPU1 PID 913995: StarCoder random_s44（step ~300，刚启动）

### 3. 📊 当前状态
刚完成两项审查并已提交 Director：
1. Related Work v1 章节审查 → WARNING（GraphCoder/ARISE "intra-procedural" 断言 + "all inference-time" 扫射式声明需核实）
2. Method v1 reviewer-warnings fix 审查 → PASS（8 项修正验证通过，patience=2/epochs=2 与实际一致；s42 regime 不一致再次标注）

**M2 训练进度**：
- Qwen: random s42/s43/s44 DONE, embed_s43 DONE, embed_s44 RUNNING (step ~850), embed_s42 + dataflow ×3 排队 → 5/9 done
- StarCoder: random s42 DONE (parent), random_s43 DONE (R@1=0.4912@1500), random_s44 RUNNING (step ~300) → 2/9 done

**关键数据点**：
- embed_s44 Qwen: R@1=0.5942@500 vs random_s44 R@1=0.6009@500 → delta=-0.67pp at step 500。如果 embed_s44 未能在后续 eval 超过 0.6009，Claim 1 的 cross-seed consistency 受威胁
- StarCoder random_s43: best_by_R@1=0.4912 vs s42=0.4604 → seed variance +3.08pp，远大于策略间 delta

### 4. 📋 待办（条件触发式）
- embed_s44 Qwen eval@1000 出结果 → 核实 R@1 是否超过 random_s44 的 0.6009；如果 delta 仍为负，立即向 Director 预警 Claim 1 风险
- StarCoder random_s44 完成 → 记录 best_by_R@1，计算 StarCoder random 3-seed mean 和 variance
- 任何 M2 checkpoint 产出 → 核实 plan_005 stratified eval 是否使用 CUDA_VISIBLE_DEVICES 合规 GPU
- Director 转发新章节写作审查 → 按审查模式 B 执行，Method v1 已有 pool=50 eval vs training-time pool=8 的遗留 concern
- m1_reextract_v2 完成（之前 ETA 19:00 CST May 15）→ 核实完成状态和覆盖率
- Director 发 Framing 提案审查 → 立即 Read negative-framing-review skill，四维度审

### 5. 🎯 战略上下文
- **核心结论链**：D017（embedding helps）→ D036（R@1 checkpoint selection）→ D045（dual checkpoint reporting）→ D049（Claim 1 softened to "reliable zero-cost baseline"）
- **最大风险**：Claim 1 effect size 从 pilot +2.0pp 缩至 M2 s43 +0.52pp (best_by_R@1)，且 pool=8 eval noise ~±0.5pp 与 delta 同量级。pool=50 独立评估是唯一可信报告基准
- **易判断错的事**：(1) 不要混淆 pool=8 训练 eval 数字和 pool=50 paper 报告数字；(2) 不要用 run_full_m2_training.sh 的参数当真相来源——该脚本 stale，实际用的是 s43plus 系列脚本；(3) val_loss 和 R@1 经常 diverge（random_s43: val_loss+22% 但 R@1+2pp），不要因为 val_loss 恶化就判断模型退化；(4) seed 间 variance（尤其 s44 的异常高 step-500 性能）可能比策略间 delta 大——统计检验前不要对单 seed 结果下结论
- **s42 是最大方法学攻击面**：唯一在旧 regime 下训练的 seed，Director 需决定是否重跑


---
