# agent / loop_5.md

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/agent/loop_5.md`
- **Structured JSON:** [`f879a4702d4be1799b34.json`](../../sessions/f8/f879a4702d4be1799b34.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 5
reason: idle_timeout
updated: '2026-05-15T00:55:43+00:00'
---

### 1. 🔴 硬约束 / 红线
- GPU 白名单 `cuda:0, cuda:1, cuda:2, cuda:3` on rtx5090-4x。不得用其他服务器或 GPU
- GRPO+QLoRA 路线已判死（D031），不要再启动任何 GRPO 训练实验。仅剩 ckpt-80/ckpt-100 的 eval 在跑，跑完即结束 GRPO 篇章
- RSFT 量化在 RTX 5090 上有 bug（memory.md 记录），quantize 参数需测试确认可用后再大规模跑
- submit_training_job 命令必须自带 `source /root/miniconda3/etc/profile.d/conda.sh && conda activate base`，不要假设 .venv 存在
- 论文 publishability 门槛：Evi-F1 > 57.34 AND rel_F1 > 53，CED vs flat-NLI Evi-F1 差 > 2pp

### 2. 🖥️ 基础设施快照
- **服务器**：rtx5090-4x（4× RTX 5090 32GB）
- **工作目录**：`/root/autodl-tmp/`（代码 `/root/autodl-tmp/freige/`）
- **Python**：`/root/miniconda3/bin/python`（conda base env，激活命令 `source /root/miniconda3/etc/profile.d/conda.sh && conda activate base`）
- **模型路径**：`/root/autodl-tmp/models/Qwen3-4B`
- **SFT adapter**：`/root/autodl-tmp/sft_output`
- **数据集**：`/root/autodl-tmp/data/docred/`（train_annotated + dev.json，dev 985 samples）
- **GRPO checkpoints**：`/root/autodl-tmp/grpo_ced_lr5e6/checkpoint-{20,40,60,80,100,...}`
- **RSFT 产出目录**：`/root/autodl-tmp/rsft_generations/`
- **Eval 结果目录**：`/root/autodl-tmp/eval_results/`
- **HF cache**：`/root/autodl-tmp/.hf_cache`
- **活跃进程**：
  - mvp2_rsft_generate: PID 122144, tmux session, cuda:1
  - mvp2_eval_lr5e6_r1_ckpt80: PID 111731, cuda:2
  - mvp2_eval_lr5e6_r1_ckpt100: PID 117635, tmux session, cuda:3
- **Cron 监控**：3 个 RUNNING 实验都注册了 cron 轮询

### 3. 📊 当前状态
**刚做完**：
- diversity_probe（success）：SFT 在 T=0.7 输出 7/8 unique triple-sets，RSFT 路线可行
- mvp2_eval_lr5e6_r1_ckpt60_r2（negative）：rel_f1=0.0093，GRPO ckpt-60 关系能力仍然崩塌
- D031 pivot 决策：GRPO+QLoRA 判死，转 RSFT+DPO+CED
- 已修复 evaluator.py 和 grpo_trainer.py 的字段名解析问题（format_ok_rate 50% → 预计修复后 >90%）

**正在跑**：
| exp_id | GPU | 做什么 | 预计 |
|--------|-----|--------|------|
| mvp2_rsft_generate | cuda:1 | SFT 模型生成 N=8 候选/样本，T=0.7 | 数小时（全 train_annotated） |
| mvp2_eval_lr5e6_r1_ckpt80 | cuda:2 | GRPO ckpt-80 eval | ~100min（已跑数小时，可能已完成） |
| mvp2_eval_lr5e6_r1_ckpt100 | cuda:3 | GRPO ckpt-100 eval，对标 kl001_r4 ckpt-100 (rel_f1=0.217) | ~100min（已跑数小时，可能已完成） |

**cuda:0 空闲**。

**等待中**：3 个 RUNNING 实验的 cron 完成回调。

### 4. 📋 待办（条件触发式）
- **ckpt-80/ckpt-100 eval 完成** → 记录 metrics 到 registry，更新 report.md。预期 rel_f1 仍 < 0.30（GRPO 全线崩塌）。无论结果如何，GRPO 篇章就此收尾，结论写入 memory.md 作为 negative evidence
- **rsft_generate 完成** → spawn Worker 检查生成质量（format_ok_rate、CED 分布、样本数），然后用 CED 打分 + 过滤 top candidates → 准备 RSFT SFT 数据 → 设计 mvp2_rsft_train 实验
- **RSFT 训练数据就绪** → 设计 RSFT 训练实验（SFT on filtered high-CED samples），提交 Director 审批
- **所有 GRPO eval 收尾** → 向 Director 汇报完整 GRPO 轨迹（ckpt-20 到 ckpt-100 的 rel_f1/evi_f1 曲线），确认 D031 pivot 数据支撑充分
- **RSFT 训练完成** → eval，与 SFT baseline（rel_f1=0.4057, evi_f1=0.7979）对比，判断 CED reward 是否带来 Evi-F1 提升

### 5. 🎯 战略上下文
- **核心问题**：LLM 做 DocRE 时能抽对关系但不生成可信证据。FREIGE 用 CED reward 训练生成 faithful evidence
- **GRPO 全线失败**：lr=5e-5 和 lr=5e-6，kl_coef=0/0.001/0.01，rank=4/8，全部 rel_f1 崩塌（0.003-0.21 vs SFT 0.406）。evi_f1 反而上升（reward hacking：模型学会生成高证据分但丢失关系抽取能力）
- **D031 pivot**：转 RSFT（Rejection Sampling FT）——用 SFT 模型多次生成 → CED 打分 → 高分样本再 SFT。避免 online RL 的不稳定性
- **关键风险**：RSFT 是 offline 方法，可能 signal 不够强。如果 RSFT 也 fail，下一步是 DPO+CED（positive/negative pair 对比学习）
- **SFT baseline 数字**（apple-to-apple eval）：rel_f1=0.4057, evi_f1=0.7979。RSFT 至少要保持 rel_f1 ≥ 0.40 且 evi_f1 有提升
- **易踩坑**：(1) 不要混淆不同 eval 协议的数字——SFT baseline r2/r3 用了不同 eval 路径，mvp2_eval_sft_baseline 才是标准对照 (2) format_ok_rate 低是解析器 bug 不是模型问题，已修复 (3) GRPO ckpt eval 都在 rtx5090-4x 上用 --quantize 跑的
- **论文目标**：EMNLP 2026 或 AAAI 2027。Paper framing 在 paper_framing.md，4 个 core claims（CED evidence, CED > flat-NLI, extraction 不牺牲, EDCR 新指标）


---
