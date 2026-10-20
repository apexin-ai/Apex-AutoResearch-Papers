# director / loop_18.md

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/director/loop_18.md`
- **Structured JSON:** [`a4f87d7662ec03e50125.json`](../../sessions/a4/a4f87d7662ec03e50125.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 18
reason: max_messages
updated: '2026-05-21T02:46:26+00:00'
---

### 1. 🔴 硬约束 / 红线
- GPU 白名单：westd cuda:0/1/2/3 + cqa1 cuda:0，严禁用白名单外的卡
- Qwen-14B d050_s0 正在 cuda:1 retrain（PID 455006），不要 kill 或抢占
- evaluate.py 有两个版本（37591 vs 37775 bytes），s0 用新版，s42/s123 用旧版。差异 <0.01pp，不影响结论但不要混用同一 seed 的 eval 结果
- lora_alpha=32 是 C006 硬约束，每次 adapter 验证必须确认
- 论文 8 页主体限制（EMNLP 2026），Limitations/Ethics/References/Appendix 不计入
- Abstract 中 "+3.8pp" 是 s42 单 seed 数值——现在 n=3 mean 是 +2.38pp，Paper Agent 正在检查是否需要更新

### 2. 🖥️ 基础设施快照
- **westd-29999**: connect.westd.seetacloud.com, root, 代码 `/root/contamcal-irt-calibration`
- **cqa1-21977**: connect.cqa1.seetacloud.com, root, 代码 `/root/contamcal-irt-calibration`
- 两台均为 aml-train 镜像（conda 环境：`source /root/miniconda3/etc/profile.d/conda.sh && conda activate base`）
- Checkpoints: `/root/autodl-tmp/exp001/checkpoints/{model}_{dosage}_{seed}/lora_adapter/`
- Eval 结果: `/root/contamcal-irt-calibration/results/` (mmlu_eval/, arc_eval/)
- 论文本地路径: `projects/contamcal-irt-calibration/docs/paper/`
- 活跃进程：
  - westd cuda:1: Qwen-14B d050_s0 retrain (PID 455006, ~57%, ETA ~1.5h)
  - westd cuda:3: Qwen-14B ARC partial eval d000/d005/d025/d100 (PID 467742)
  - westd cuda:0: Qwen-14B d100 MMLU eval (刚启动)
  - westd cuda:2: Qwen-14B d100 ARC eval (刚启动，但 d100 ARC 已由 cuda:3 batch 覆盖)
  - cqa1 cuda:0: Qwen-7B GSM8K PPP eval (R6-W4)
  - DGP 模拟: 已完成 400/400，结果已写入 appendix
- Cron 活跃: retrain_qwen14b_d050_s0

### 3. 📊 当前状态
**刚做完**：
- Gemma-2 n=3 BCa CI：MMLU [+1.49, +3.14] Benefit 确认，ARC [-1.97, +1.42] 过零
- Qwen-7B n=3 BCa CI：MMLU [-1.82, -0.34] V-recovery 确认，ARC [-2.90, -2.08]
- R3-W10 DGP 400/400 完成→appendix+limitations 写入完成→Reviewer 验证 PASS→标记 resolved
- Qwen-14B position bias 发现→Limitations 已更新（Qwen 家族特有，跨家族对比确认）
- Paper Agent 完成：Table 3 Qwen-7B n=3 更新 + DGP appendix + position bias 跨家族对比
- Paper Agent 正在处理：Gemma-2 n=3 Table 3 更新（刚派单）

**n=3 进度 4/5**：
| Family | MMLU CI | ARC CI | Status |
|--------|---------|--------|--------|
| Phi-4 | [-0.17,+1.39] Immune | [+0.51,+0.77] | ✅ |
| OLMo-2 | [-0.55,+2.60] Benefit† | [+2.90,+3.78] | ✅ |
| Qwen-7B | [-1.82,-0.34] V-recovery | [-2.90,-2.08] | ✅ |
| Gemma-2 | [+1.49,+3.14] Benefit | [-1.97,+1.42] | ✅ |
| Qwen-14B | pending | partial eval 中 | ⏳ |

**等待中**：
- Qwen-14B d050 retrain 完成 → d050 eval → 全 5 dosage n=3 bootstrap
- Qwen-14B ARC partial eval (d000/d005/d025/d100) 完成
- Qwen-14B d100 MMLU eval 完成
- R6-W4 GSM8K PPP (cqa1, info-level)
- Paper Agent Gemma-2 Table 3 patch 回复

### 4. 📋 待办（条件触发式）
- Qwen-14B d050 retrain cron 回调（~1.5h）→ 检查 adapter 完整性 → 在空闲 GPU 上跑 d050 MMLU+ARC eval
- Qwen-14B ARC partial eval 完成 → 收集 d000/d005/d025/d100 ARC 结果
- Qwen-14B d100 MMLU eval 完成 → 收集结果，与 sweep 内置 eval (43.85%) 交叉验证
- **全部 Qwen-14B eval 齐了** → 计算 n=3 BCa bootstrap CI → 派 Paper Agent patch Table 3 → 这是最后一个家族，完成后 **5/5 n=3 全齐**
- 5/5 n=3 完成 → 更新 ROADMAP → 全面论文一致性检查 → submit_paper_to_review（目标 D+5 = May 24）
- Paper Agent Gemma-2 patch 回复 → 检查 Abstract "+3.8pp" 是否已更新为 n=3 均值
- R6-W4 GSM8K PPP 结果 → 如有意义写入 appendix（info-level，不阻塞提交）
- R6-W2 S4 details / R6-W3 training curves → info-level，有 GPU 空闲时处理，不阻塞

### 5. 🎯 战略上下文
- **核心论文**: "Not All Models Are Inflated" — SFT contamination 产生 4 种 dose-response pattern（Immune/Collapse/V-recovery/Benefit），非统一 inflation
- **关键决策链**: D184(taxonomy 命名) → D187(bootstrap 方法) → D193(Immune 双条件) → D194(Gemma-2 d025 ARC outlier 保留) → D195(Qwen-7B n=3 确认) → D196(DGP 稳健) → D197(Qwen-14B position bias) → D198(Gemma-2 benchmark-conditional)
- **review_issues**: 16/18 resolved。R1-C2 (warning, cross-family MAE CI) + R6-W2/W3/W4 (info) 未关闭，均不阻塞
- **最大风险**: Qwen-14B s0 极端 collapse (-24.99pp) + position bias (A-rate 77%) 会使 n=3 CI 极宽。但 3/3 seed 方向一致（全负），CI 应排除零
- **易踩的坑**:
  - Cron 经常误报 failed（registry 停在 PREPARING，cron 找不到 sentinel）→ 先看日志再信 cron
  - eval 重复提交问题（M038）→ 提交前检查输出目录是否已有 .done sentinel
  - sweep 静默失败（M036/M037）→ 大模型高 dosage 必须 gradient checkpointing + adapter 存在性验证
  - `check_paper_consistency` 报告 3 个 orphan bib 是误报（`\citealp{}` 不被解析）
  - `paper_compile_and_check` 有 UTF-8 解码 bug → 用 bash pdflatex 直接编译验证


---
