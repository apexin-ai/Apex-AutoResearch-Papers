---
loop: 6
reason: idle_timeout
updated: '2026-05-29T09:03:17+00:00'
---

### 1. 🔴 硬约束 / 红线
- GPU 白名单: westd-35807:cuda:0,1,2,3 + westd-45947:cuda:0,1。不可用其他卡
- CoRL 2026 DDL (2026-05-28 12:00 UTC) 已过。论文应已提交（`ops:scp-paper-files` Worker 12:07 UTC 完成），但 **未收到 Director 明确确认提交成功**
- eval 结果 JSON 文件名冲突: s0 eval 的磁盘 JSON 被 reeval_lora_s0_30k_v2 覆盖过，**以 registry 为准**，不读磁盘 JSON 做判定
- s1 eval metrics 在 registry 中 CAR=0.585（比例）而 s0 是 CAR=58（百分比），**单位不统一**——做聚合时必须对齐
- 统计检验策略 (D041): 正文双尾 permutation test，脚注单尾 + directional prior，不改

### 2. 🖥️ 基础设施快照
- **westd-35807**: /root/colliforce-vla, conda base (`/root/miniconda3/bin/python`), 磁盘 68% 可用 (~570G)
  - cuda:0,1,2,3 全部空闲
- **westd-45947**: /root/colliforce-vla, conda base (`/root/miniconda3/bin/python`), 磁盘 96% 可用 (~400G)
  - cuda:0,1 全部空闲
- W&B: entity/project 从项目 config 自动加载
- eval 数据集: safelibero_object (4 tasks: orange_juice, chocolate_pudding, milk, bbq_sauce)
- 无活跃进程、无活跃 tmux session、无活跃 cron

### 3. 📊 当前状态
**刚做完**: Loop #6 session-start 初始化。read_registry + reconcile_crons + 读 report.md/ROADMAP.md。已向 Director 汇报当前状态，等待回复。

**Registry**: 0 RUNNING, 0 ANALYZING。131 个实验总计（成功 72 / 负向 25 / 失败 16）。
- 2 个 PREPARING/failed: `eval_multiseed_lora_s1_eseed99` 和 `eval_multiseed_lora_s1_eseed0`（非关键，补充 eval-seed battery，之前提交失败未重试）
- `train_phase2_lambda0_s2_v4`: 已失败，Phase 2 λ=0 seed2 resume，非 DDL 关键路径

**等待中**: Director 回复——确认论文提交状态 + post-submission 指示

### 4. 📋 待办
- Director 确认论文已提交 → 清理遗留 PREPARING/failed 实验状态（标记 killed 或重新提交）
- Director 指示继续 Phase 2 → 诊断 train_phase2_lambda0_s2_v4 失败原因，修复后在 westd-35807:cuda:2 重新提交
- Director 指示补充 multi-eval-seed battery → 修复 eval_multiseed_lora_s1 (eseed0/99) 提交失败问题，重新提交到 westd-45947
- Director 开启新方向 / rebuttal 准备 → 按指示执行
- 无 Director 指示 → 不主动启动新实验，所有 GPU 空闲等待分配

### 5. 🎯 战略上下文
**核心结论链**: Scenario B confirmed (D043)。LoRA baseline 3-seed CAR=54.67%±2.02%。λ=0.1 3-seed CAR=57.00%，perm p=0.0714 单尾 → SDF 冗余，论文采用 negative finding narrative（SDF avoidance 不显著优于 LoRA-only）。

**决策链关键节点**: D041(统计策略) → D042(数据统一用reeval) → D043(Scenario B确认) → D044(审稿回应策略，Claim 3降级，scope收窄)

**易错点**:
- 论文有双叙事模板 + paper_switch.py 自动选版——不要手动改论文 narrative
- Reviewer 13 处修正已由 Worker 完成并验证通过，不要重复做
- memory.md 内容极少（只有 Fig 5 旧数据），大部分上下文在 ROADMAP.md 和 registry 中
- DDL 已过但未收到 Director 明确的"已提交"确认——不要假设提交成功，等 Director 回复
