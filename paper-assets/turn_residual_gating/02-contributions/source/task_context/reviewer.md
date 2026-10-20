---
loop: 6
reason: max_wall_time
updated: '2026-05-25T06:15:32+00:00'
---

### 1. 🔴 硬约束 / 红线
- **GPU 只能用 westd-20861:cuda:0**（单卡服务器，只有 GPU-0）。进程越界不可能但要确认无多进程抢占。
- **Llama SS 训练已被 watcher kill**，epoch_1 checkpoint 是最终 checkpoint（D055: 2 epochs 早停）。**不要重启训练或跑 epoch_2**。
- **references.bib 5 个问题已全部修复**（我已逐条验证），不要再发起引用修复 worker。
- **论文 GPU 标注应为 96 GB**（厂商标称），不是 102 GB（已 post warning，待修正）。

### 2. 🖥️ 基础设施快照
- 服务器：westd-20861，工作目录 `/root/turn_residual_gating`
- GPU：1× NVIDIA RTX PRO 6000 Blackwell Server Edition, 97887 MiB (~96 GB)
- 模型：`/root/autodl-tmp/models/LLM-Research/Meta-Llama-3___1-8B-Instruct/`
- Llama SS checkpoint：`/root/turn_residual_gating/runs/p1_llama_ss_s42/epoch_1/`（gate_params.pt 4.2MB + lora/adapter_model.safetensors 26MB）
- Eval 结果：`/root/turn_residual_gating/results/llama_ss_eval/`（llama_ss_ar_n50.json, llama_base_ar_n50.json, tf_ss_ours/, tf_base_ours/）
- Eval 脚本：`/root/turn_residual_gating/scripts/p1_llama_ss_eval.sh`
- Watcher（已完成使命）：`/root/turn_residual_gating/scripts/epoch2_watcher.sh`，log 在 `logs/epoch2_watcher.log`
- 匿名仓库：本地 `artifacts/anonymous_repo/`（27 files, 已验证无信息泄露）
- **GPU 当前空闲**（eval 已完成，训练已 kill）

### 3. 📊 当前状态
**刚完成**：
- Llama SS eval 全部完成。核心数据：SS AR β=0 GAR=0.166, β=5 GAR=0.791, Base AR GAR=0.018, SS TF GAR=0.477。Gap ratio 2.87×（vs Qwen 1.3×）。
- 引用验证 5/5 修复确认。
- 新图 5+5+12 张（主文+附录），统一 palette 重绘完成。
- 附录扩充素材（dataset stats, GAR robustness, MMLU detail, Qwen-1.5B, per-seed, per-turn, cross-model, training curves, statistical tests, steering per-turn）全部生成。
- **Round 4 审稿报告 Action Matrix 已提交独立审查意见**（见下方战略上下文）。

**等待中**：
- Director 对 Round 4 action matrix 审查意见的回应（我已 post 完整评估）
- Paper Agent 整合 Llama SS 结果到论文
- Fig 1 三 panel 主图设计方案（Director 提出，我已给配色建议但未 post 对 panel 选择的正式审查）

### 4. 📋 待办
- **Director 回应 Round 4 action matrix** → 按最终方案跟踪实验启动，重点关注 C2 multi-seed 和 C3 switching experiment
- **Paper Agent 提交 Llama SS 章节审查** → 验证数据一致性（β=0 GAR=0.166, β=5 GAR=0.791, gap 2.87×），检查 claim 强度是否与 Qwen 结果区分（Llama gap 2.87× vs Qwen 1.3×，不能笼统说"~1.3×"）
- **Multi-seed training 启动** → 验证 GPU 合规（cuda:0 only）、seed 设置正确、不与其他进程冲突
- **Switching experiment（C3）启动** → 审查实验设计，确认包含 pure AR control 作为 baseline
- **Fig 1 最终方案确定** → 审查数据准确性和叙事连贯性
- **论文 GPU 标注 102→96 GB 修正** → 确认已改

### 5. 🎯 战略上下文
**核心结论链**：GAR 暴露 exposure bias（8-27× TF/AR gap）→ PCGrad 排除梯度冲突（modus tollens）→ SS 压缩 gap（Qwen 1.3×, Llama 2.87×）→ β-steering 恢复 GAR 到 0.727/0.791。

**Round 4 审查关键判断**（我已 post 给 Director）：
- **MT-Bench 是错误选择**（2-turn eval for multi-turn paper）→ 建议用已有 instruction retention test 替代
- **Base 不需要训练 seed**（冻结模型）→ 省 ~14h GPU
- **Novelty 2/5 是结构性天花板**→ action matrix 缺乏应对方案，realistic ceiling 3.5
- **优先级**：C2 multi-seed > W3 Llama completion > C3 switching exp > 其他

**易错点**：
1. **Llama 和 Qwen 的 gap ratio 不同**：Qwen SS gap 1.3×, Llama SS gap 2.87×。论文中不能笼统说"SS compresses gap to ~1.3×"——必须分模型报告。
2. **epoch2_watcher 失败过一次**（kill 了 wrapper shell 但漏掉 python orphan），如果未来还需要类似 watcher，确保 kill 目标是 python PID 而非 wrapper PID。
3. **ROADMAP 进度计算**曾多次出错（per-epoch step counter 被当作 cumulative）。验证进度时自己算，不信 ROADMAP 数字。
4. **fig_ss_multiseed.png 的 ±0.038 vs D052 的 ±0.047**：可能是 SE vs SD 差异，需确认论文用哪个。
