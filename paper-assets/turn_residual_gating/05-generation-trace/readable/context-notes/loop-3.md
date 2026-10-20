# director / loop_3.md

**Exposure Bias Collapses Auxiliary Attention Losses in Multi-Turn Dialogue** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/director/loop_3.md`
- **Structured JSON:** [`6418c168e70dda8fac66.json`](../../sessions/64/6418c168e70dda8fac66.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 3
reason: max_messages
updated: '2026-05-21T19:41:40+00:00'
---

### 1. 🔴 硬约束 / 红线
- **GPU 白名单**：仅 `westd-20861:cuda:0`（1×RTX PRO 6000 Blackwell, 102GB）。home-1x5090/westd-22162/westd-16980 **不在项目 gpu_ids 和 SSH config 中**（D043 Reviewer 确认）。已向用户提出扩卡请求，用户未回复。
- **seetacloud-bjb2-structtts 不属于本项目**，连接问题不管。
- **训练期间 GPU 不可共享**（M019 OOM 教训）。
- **paper_framing.md SP1**：30× gap 在 **GAR-ours** 上测得（非 GAR-Dongre）。
- **nGAR 归一化陷阱**（M020）：TF nGAR=11.88 vs AR nGAR=0.493，gap 24×——"归一化伪影" 叙事已被证伪，论文禁用。
- **训练完成后必须先 eval 再启动下一个训练**（M021，本轮教训）。

### 2. 🖥️ 基础设施快照
- **服务器**：westd-20861 (connect.westd.seetacloud.com)，工作目录 `/root/turn_residual_gating`
- **Python**：conda base 环境（`/root/miniconda3/bin/python`），aml-train 镜像
- **模型**：Qwen `/root/.cache/modelscope/Qwen/Qwen2___5-7B-Instruct`；Llama `/root/autodl-tmp/models/LLM-Research/Meta-Llama-3___1-8B-Instruct/`
- **数据**：`/root/turn_residual_gating/data/ultrachat_8k` (8000 samples)
- **活跃进程**：v7 TG s123 训练 PID 245628（应已完成，Agent 空闲 16h 未回调）。Cron 120s 间隔已注册但回调历史不可靠（连续 3+ 次丢失）。
- **论文**：`/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/`，最新 commit e4522a3，编译需手动 `pdflatex→bibtex→pdflatex×2`（`clean=true` 会触发 ACL 模板 bibtex bug）。

### 3. 📊 当前状态
**刚做完**：
- Llama TG 训练+eval 完成（C5 confirmed D045，gap 12.5×）
- Instruction retention test 完成（D046，content +23.8pp, p=0.007）
- Matched Llama AR eval（N=50/T=4）+ nGAR 错误修正（M020）
- v8b SS s123 训练完成（seed robustness 训练指标确认，Δ<15%）
- Paper patch e4522a3（Llama 整合 + critical 修复 + Abstract 压缩，8 页合规）

**大概率已完成但未确认**：
- v7 TG s123 训练（PID 245628，ETA 约 05-21 21:16 UTC，Agent 空闲 16h 说明早已结束但 cron 回调又丢了）

**未完成**：
- v8b SS s123 eval（脚本 `scripts/eval_v8b_ss_s123.sh` 已就绪，需 GPU）
- v7 TG s123 eval（脚本 `scripts/eval_v7_tg_s123.sh` 已就绪，需 GPU）

### 4. 📋 待办（条件触发式）
- **第一步（立即）**：SSH 检查 v7 TG s123 是否已完成 → 如已完成，更新 registry → DONE，然后按序执行 v8b s123 eval → v7 s123 eval
- **v8b s123 eval 完成** → 对比 s42 baseline（Reviewer 模板：gap ratio 1.57× baseline, PPL 1.38, GAR-ours modelgen 0.318）→ 如 gap ∈[1.2×,2.5×] PASS
- **v7 s123 eval 完成** → 对比 s42（GAR-ours 0.50 TF, 0.016 AR, gap ~32×）→ 汇报 multi-seed 对比
- **C7 multi-seed 全部完成** → 派 Paper Agent patch 论文写入 mean±std → 更新 ROADMAP
- **用户回复 GPU 扩卡** → 如果获得新卡，启动 Llama LoRA-only (plan_011, `scripts/launch_llama_lora.sh` 已就绪)
- **所有 MUST-DO 完成后** → 如 GPU 仍可用，跑 Llama LoRA-only（7h）完成跨模型四路消融

### 5. 🎯 战略上下文
- **论文定位**："First empirical characterization of how exposure bias selectively destroys auxiliary attention loss generalization, with dual mitigation paths"。Diagnostic + constructive directions paper，非 solution paper。
- **评分预估**：multi-seed 完成后 Overall 8/10 → **ARR 3.0-3.5 (Findings-Borderline Conference)**。Originality 天花板 3/4。
- **决策链**：D037(steering 里程碑) → D041(v8b SUCCESS) → D043(ablation 精简) → D045(C5 confirmed Llama 12.5×) → D046(W3 instruction retention p=0.007)
- **易踩的坑**：
  1. Cron 回调不可靠（连续 4+ 次丢失），训练 ETA 到了必须主动派 Agent 检查
  2. Agent 可能混淆 raw GAR 和 nGAR（M020），涉及归一化指标时要求 Reviewer 交叉验证
  3. 训练脚本不自带 eval（M021），完成后必须手动启动 eval 脚本
  4. `paper_compile_and_check` 用 `clean=true` 会导致 bibtex 失败，避免使用
  5. System 会反复追问空闲 GPU（westd-22162 等），直接引用 D043 终结
  6. "phase transition" 已改为 "sharp nonlinearity"，全文已清理但新增文本不要用旧术语


---
