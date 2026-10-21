# director / loop_10.md

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/director/loop_10.md`
- **Structured JSON:** [`14279e0e853144d7b95c.json`](../../sessions/14/14279e0e853144d7b95c.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 10
reason: max_messages
updated: '2026-05-23T19:40:30+00:00'
---

### 1. 🔴 硬约束 / 红线
- 本项目 GPU 白名单：bjb1-40020 (cuda:0, cuda:1) + bjb1-45299 (cuda:0, cuda:1)，共 4 张，严禁使用其他服务器/GPU
- Registry 工具存在缓存 bug：显示"无实验注册但 GPU 在用"是已知问题，YAML 文件本身正确。不要因此重复注册或误判实验状态
- GPU 利用率 ~20% 是 DreamerV3 架构固有特征（imagination rollout 在 CPU，GPU 仅 model update 短暂活跃），不是问题
- D143 混合机制 claim 已被 D146 正式撤回——PegInsertion 是环境随机性，非 CIVO。论文中不得出现 "mixed mechanism" / "dt_emb amplification in manipulation" 相关表述
- CoRL 2026 DDL 2026-05-29，数据锁定 5/27。不要 fallback 到其他会议

### 2. 🖥️ 基础设施快照
- 服务器 1：bjb1-45299，工作目录 /root/autodl-tmp/event-gated-adaptive-horizon
- 服务器 2：bjb1-40020，工作目录 /root/autodl-tmp/event-gated-adaptive-horizon
- 两台均为 aml-train 镜像，conda base 环境：`source /root/miniconda3/etc/profile.d/conda.sh && conda activate base`
- 活跃进程：
  - bjb1-45299:cuda:0 — exp_058 Cheetah frozen s1 (PID 164830)，刚启动
  - bjb1-45299:cuda:1 — exp_057 Walker frozen s2 (PID 157775)，105K/210K
  - bjb1-40020:cuda:0 — exp_055 PegInsertion trained s1 (PID 345223)，144K/210K
  - bjb1-40020:cuda:1 — exp_056 PegInsertion frozen s1 (PID 346430)，137K/210K

### 3. 📊 当前状态
刚完成：D146 撤回后论文全文修正 + Reviewer 三项终检（全 PASS）+ cross-domain reproducibility table 添加 + ROADMAP 更新 + exp_054 收尾 + exp_058 部署。

4 个实验 RUNNING，预计完成时间：
- exp_055/056：~12h（PegInsertion s1 paired，描述性数据，非 CIVO）
- exp_057：~16h（Walker frozen s2，目前全程 <1.0，极佳）
- exp_058：~20h（Cheetah frozen s1，验证极端 CIVO 场景 frozen n=2）

论文状态：8 页正文 + 33 页含附录，0 warnings。所有 D146 修正已完成，cross-domain table (6/6 locomotion vs 0/5 manipulation) 已在 appendix。Paper Agent patches 全部落地。

### 4. 📋 待办
- exp_055/056 完成 → 提取 PegInsertion s1 最终 ve_ratio/eval_return → Paper Agent final patch 更新脚注中的 interim 数据为最终值
- exp_057 完成 → 确认 Walker frozen n=3 全部 <1.5 NVE → 更新 appendix Table 3/4 frozen seed 计数
- exp_058 完成 → 提取 Cheetah frozen s1 NVE → 如 <1.5 则 Cheetah frozen 0/2 → 更新 cross-domain table + appendix
- 全部完成后 → 一次性 comprehensive final patch（所有最终数据）→ 提交 Review Director Round 2（`submit_paper_to_review`）
- Reviewer 终检提到 analysis.tex L11 比较基准不对称（2.48 vs peak 3.08）→ 可在 final patch 中顺便修正为 "vs. trained s1 peak $3.08\times$"

### 5. 🎯 战略上下文
- **核心结论**：CIVO 是 locomotion-specific（Walker 4/4 + Cheetah 2/2 trained CIVO，6/6）。Manipulation 0/5 均为环境 transient。Frozen dt_emb 在 locomotion 稳健阻止 CIVO（Walker 0/3, Cheetah 0/1→待 exp_058）
- **关键决策链**：D141 StackCube→环境 transient → D142 PegInsertion 初分类 → D143 混合机制（已撤回）→ D146 PegInsertion 重分类为环境随机性（s1 因果方向反转）
- **最易判断错的事**：不要因为 manipulation 全是 negative 就认为论文弱——0/5 manipulation 是 scope boundary + diagnostic specificity 的有力证据，6/6 vs 0/5 的干净分离反而是论文强项
- **容易踩的坑**：(1) exp_055/056 的 interim 数据（132.5K/142.5K）已写入论文脚注，完成后必须更新为最终值；(2) 不要重新提出 D143 混合机制——s1 数据已彻底否证（frozen 11.32 > trained 2.48）；(3) Registry 缓存 bug 会反复被 system keepalive 提醒，解释即可不必反复修


---
