---
loop: 17
reason: max_wall_time
updated: '2026-05-28T22:26:50+00:00'
---

### 1. 🔴 硬约束 / 红线
- cqa1-33015 有 4 张 4090（24GB），westd-41074 有 1 张 H100（98GB），westd-38929 有 1 张 H100（98GB），westd-27271 已下线不可用
- pi0.5 eval 在 4090 上需 ~10GB，在 H100 上也需 ~10GB；OpenVLA 需 ~16GB
- 论文使用 5-seed（s42-s46）作为主结果，seed47 是 6th seed bonus for revision——不要把 seed47 数据混入论文主表
- CoRL 2026 提交：8 页正文含 Limitations，references 和 appendix 不计入

### 2. 🖥️ 基础设施快照
- **cqa1-33015**：`/root/autodl-tmp/importance_margin_vla_compress`，conda base（`/root/miniconda3/bin/python`），HF cache `/root/autodl-tmp/.hf_cache`
- **westd-41074**：同上路径结构，conda base
- **westd-38929**：同上，但最近多次 OOM kill（3 进程共享时不稳定）
- 模型路径：pi0.5 → `/root/autodl-tmp/pi05_libero_finetuned`；OpenVLA → `/root/autodl-tmp/openvla-libero-goal`（cqa1 only，w41 缺文件）
- 活跃进程：`eval_pi05_l2norm_k07_long_seed47_w41` RUNNING on cqa1 GPU 0（log: `~/runs/.../eval_pi05_l2norm_k07_long_seed47_w41.log`），启动于 06:23，预计 ~5h 完成

### 3. 📊 当前状态
**刚完成**：
- 论文最终全文核实（PASS）：零 "??"，所有交叉引用解析正确，8 页限制满足，所有此前 critical/warning 修复在位
- cqa1 幽灵进程 PID 373970 已 kill（GPU 0 释放）
- 3 个 seed47 实验（L2norm k=0.75, Random k=0.7, Random k=0.75）已完成并入 registry
- 2 个 seed46 实验（Random k=0.5, Random k=0.95 on w41）已完成

**RUNNING**：
- `eval_pi05_l2norm_k07_long_seed47_w41`：cqa1 GPU 0，L2norm k=0.7 Long seed47——crossover 配对实验

**关键发现**：Random k=0.7 seed47 = 59.0%，比 5-seed 均值 64.6% 低 5.6pp（~3σ 异常值）。已报告 Director。当前 L2norm k=0.7 seed47 正在运行，结果将决定 6-seed crossover margin 是否缩窄。

### 4. 📋 待办
- `eval_pi05_l2norm_k07_long_seed47_w41` 完成 → 提取 SR，计算 6-seed crossover margin（Random vs L2norm at k=0.7），如果 margin < 0.5pp 或翻转 → 立即 [severity: warning] 报告 Director，建议 revision 措辞调整
- Director 转发新的章节审查请求 → 按 Mode B 审查，必须先 Read `paper-quality-lessons.skill.md`
- Director 转发 Framing 调整提案 → 必须先 Read `negative-framing-review.skill.md`，四维度审查

### 5. 🎯 战略上下文
- **核心结论**：vision connector 架构决定 pruning tolerance，CV 是零成本预测器。CV spectrum: π0(0.038) < π0.5(0.055) < X-VLA(0.151) < OpenVLA(0.215) < SmolVLA(0.314)
- **论文已通过最终格式核实**：零 "??"，8 页，所有引用解析，bib 验证完毕。PDF 时间 18:35
- **最容易判断错的事**：
  1. background.tex / results_v2.tex / results.tex / experimental_setup.tex 是孤立文件，不在 main.tex 编译链中——里面的断引不影响 PDF，不要标 critical
  2. appendix 中有大量 alias labels（如 `app:attention_scoring` 和 `app:attention_pruning` 指向同一 section）——orphan label 是 warning 不是 critical
  3. seed47 数据是 revision bonus，不在 5-seed 主表中——不要因为 seed47 异常值质疑论文现有 claim
  4. check_figures_and_layout 工具扫描所有 .tex 文件（含孤立文件），其 critical 需要交叉验证是否在编译链中
