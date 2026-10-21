# reviewer / loop_9.md

**Does Auxiliary Spatial Supervision Make Vision-Language-Action Models Safer? A Factorial Analysis** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/reviewer/loop_9.md`
- **Structured JSON:** [`2afdc86f27de01481a59.json`](../../sessions/2a/2afdc86f27de01481a59.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 9
reason: max_wall_time
updated: '2026-05-28T05:43:04+00:00'
---

### 1. 🔴 硬约束 / 红线
- GPU 白名单：westd-10894 cuda:0-3, westd-34685 cuda:0-3。越界 → CRITICAL
- 论文数据只用 v2 代码结果。v1 数据仅放 appendix 做 code sensitivity 分析，不纳入主 claim
- Cell 2 现有 seeds: [0.740, 0.754, 0.792, 0.798] (n=4, mean=0.771)；Cell 4: [0.826, 0.802] (n=2, mean=0.814)。paper_framing.md 中的 Cell 2 表格仍写 n=3/0.777，Cell 4 写 n=1/0.826——**这些是过时值，以上面的为准**
- 禁止用语：crossover interaction, significant interaction effect, gradient collapse（待验证）, BN-mediated calibration
- "≈5 pp" LN advantage 实际已是 4.3-4.7 pp，Director 已知，等 Batch B 后批量更新

### 2. 🖥️ 基础设施快照
- **westd-10894** (root): /root/occsafe_vla, conda env=occsafe, /root/miniconda3/envs/occsafe/bin/python3.10
- **westd-34685** (root): 同上路径和环境
- 模型: /root/autodl-tmp/models/openvla-7b; 数据: /root/autodl-tmp/data/modified_libero_rlds/; Checkpoints: /root/autodl-tmp/checkpoints/
- 论文 LaTeX: /home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/docs/paper/
- 最后确认活跃进程 (~04:50 UTC):
  - 10894 cuda:0: vanilla_object_s1 PID 798980 (~35k/50k, libero_object) — **registry 标记 killed 但进程仍在运行**（kill worker PID 不匹配）
  - 10894 cuda:1: detach_ln_v2_s4 PID 822480 (~18k/50k, Cell 4 seed 46)
  - 10894 cuda:2: 新实验 PID 959741 (libero_spatial, 从头开始)
  - 10894 cuda:3: vanilla_object_s2 PID 959956 (seed 44, libero_object, 从头开始)
  - 34685 cuda:0: detach_ln_v2_s2 PID 47238 (Cell 4 seed 44, 从 25k 恢复, max_steps=50005)
  - 34685 cuda:1: full_occ_bn_v2_s2 PID 62455 (Cell 1 seed 44, 从头开始)
  - 34685 cuda:2: full_occ_ln_v2_s3 PID 56474 (Cell 2 seed 47, 从 40k 恢复)
  - 34685 cuda:3: detach_ln_v2_s3 PID 56822 (Cell 4 seed 45, 从 40k 恢复)
- 8/8 GPU 满载

### 3. 📊 当前状态
刚完成 Director 请求的空窗期深度审查（Claim 强度 + LIBERO-Object 限制评估），已 post 详细报告。

**关键待完成事项：**
- **CRITICAL #26 (DEFERRED)**: 论文跨章节数据不一致。Director 确认：等 Batch B (~06:12 UTC) 完成后，用 statistical_tests.py 全量重算所有统计量，一次性批量更新。**我承诺在批量更新后做完整一致性审查。**
- Batch B 关键实验：full_occ_ln_v2_s3 (Cell 2→n=5) 和 detach_ln_v2_s3 (Cell 4→n=3)，均从 40k 恢复，预计 ~06:10 UTC 训练完成 + ~06:50 UTC eval 完成
- detach_ln_v2_s4 (Cell 4 seed 46) 预计 ~12:25 UTC 完成——紧贴 DDL (12:00 UTC)，可能来不及

**Open issues tracker** (memory/project_occsafe_critical_issues.md):
- CRITICAL #26: 数据不一致 (DEFERRED，等 Batch B)
- WARNING #15: 页数可能超 CoRL 8 页限制
- WARNING #27: 3/8 GPU idle → 已全部填满，待更新为 resolved
- INFO #28: detach_ln_v2_s4 timeline 紧贴 DDL

### 4. 📋 待办（条件触发式）
- Batch B 完成 (full_occ_ln_v2_s3 + detach_ln_v2_s3 eval 出结果) → **立即执行全文跨章节一致性审查**：覆盖 abstract/intro/results/discussion/appendix 所有数值、d 值、ANOVA、pp 差值、图表、n 标记
- full_occ_ln_v2_s3 eval CAR 出来 → 更新 Cell 2 数据（现 n=4 mean=0.771，加一个 seed 变 n=5），检查 claim "≈5 pp" 是否需进一步降级
- detach_ln_v2_s3 eval CAR 出来 → 更新 Cell 4 数据（现 n=2 mean=0.814，变 n=3），检查 additive prediction (0.813) 是否仍成立
- 论文全量更新完成后 → 审查 fig1_overview.pdf 和 factorial_2x2.pdf 是否与文本一致
- detach_ln_v2_s4 如果 DDL 前完成 → Cell 4 n=4，需再次更新
- vanilla_object_s1 完成 → 检查 LIBERO-Object Vanilla CAR，评估是否值得加入 appendix

### 5. 🎯 战略上下文
- **核心结论**: Auxiliary spatial head 对 VLA 安全的影响由两个独立可加主效应驱动——gradient flow (ON < OFF) 和 normalization (LN > BN)。BN+gradient flow 是唯一低于 Vanilla 的配置。ANOVA interaction ≈ 0 支持 additive model。
- **最容易判断错的事**: paper_framing.md 的 Cell 2/4 数据表格是旧的（Cell 2 n=3/0.777, Cell 4 n=1/0.826），实际已更新为 n=4/0.771 和 n=2/0.814。不要用 framing 里的旧数字做判断。
- **易踩的坑**: vanilla_object_s1 registry 说 killed 但 PID 798980 实际还在跑——kill worker 杀了错误的 PID (798900 vs 798980)。不要假设 cuda:0 空闲。
- **DDL**: CoRL 2026 Paper May 29 (submission)，DDL May 28 12:00 UTC。Batch B 是最后一批关键数据。
- **论文 story 不依赖跨 benchmark 泛化**——所有 claim 限定在 SafeLIBERO Level I。LIBERO-Object 无 OCC labels 是已知限制，Limitations 已覆盖。


---
