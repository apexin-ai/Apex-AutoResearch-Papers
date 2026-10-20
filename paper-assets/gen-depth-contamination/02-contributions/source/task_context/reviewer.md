---
loop: 24
reason: idle_timeout
updated: '2026-05-25T15:40:11+00:00'
---

### 1. 🔴 硬约束 / 红线
- GPU 白名单 cuda:0-3（4 张卡），越界即 critical
- registry 为数据真源，report.md 可能滞后（gemma27b_filtering / code_domain_olmo 在 report.md 仍显示 "failed"，实际 DONE/success）
- 论文已提交 EMNLP 2026 ARR（DDL 2026-05-25），正文 claims 冻结，后续实验数据仅供 rebuttal/revision
- pp 单位：1pp = 0.01（两次犯过 10× 错误，报告前必须二次核验）

### 2. 🖥️ 基础设施快照
- 服务器：cqa1-22115(root)，工作目录 /root/autodl-tmp/gen-depth-contamination
- Python：conda base（/root/miniconda3/bin/python）
- HF cache：/root/autodl-tmp/.hf_cache
- 活跃进程：
  - exp_014_naturalistic_v2（PID 233962，tmux=exp_014_naturalistic_v2，cuda:1）：下载 FineWeb 50K + OBD 特征提取/预测。注意：CC-MAIN-2025-26 下载失败，已降级到 CC-MAIN-2024-51
  - exp_014_independent_metrics（PID 234919，tmux 同上，cuda:1）：在 sleep 循环等 v2 数据（data_exp014_v2/cc_predictions.csv），v2 完成后自动启动。计算 GPT-2 PPL/MTLD/HDD/n-gram rep/Zipf 6 个独立指标

### 3. 📊 当前状态
本轮完成 3 项审查：
1. **runtime_benchmark**：假设被 falsified（OBD 44.3ms/doc 是最慢方法，非最快），已报 Director。Agent 已修正 conclusion→negative 并补录 metrics
2. **exp_014_naturalistic（原版）**：发现 critical 循环依赖——10 个 correlation 指标中 7 个是 OBD 自身特征，freq_entropy ρ=-0.78 是伪验证。已报 Director
3. **exp_014 v2 + independent_metrics**：Agent 响应审查，正在用真正独立的 6 个指标重跑。进行中，预计 2-3 小时后可审查

Registry：RUNNING=0，PREPARING=36（含 runtime_benchmark 残留 + exp_014_independent_metrics + killed sweep），DONE=139

### 4. 📋 待办
- exp_014_naturalistic_v2 完成通知 → 检查 data_exp014_v2/ 生成完整性 + CC 快照版本是否在 registry 中准确标注
- exp_014_independent_metrics 完成通知 → 核心审查：独立指标（GPT-2 PPL/MTLD/HDD/Zipf）与 OBD depth 的 correlation 强度是否支撑 ecological validity claim。重点看 |ρ| 是否 >0.3 才有 practical significance
- Director 转发审稿意见 → Read rebuttal.skill.md → 协助准备数据支撑
- Director 转发章节写作审查 → Read paper-quality-lessons.skill.md → 模式 B 对抗审查

### 5. 🎯 战略上下文
**核心结论链**：K* bounded & domain-dependent。Domain ceiling 阶梯：Wiki=1, C4/Code=2, arXiv=3。Model competence 调制但不超越 ceiling。OLMo 全域 K*=1（competence-limited 例外）。Cross-model transfer 80-92% 证明 depth signal text-intrinsic。

**易错点**：
- exp_014 原版 metrics（registry 中 ttr_rho=0.17, cc_depth0_ratio=0.89）与原始 JSON 不一致（实际 0.145 和 0.902/0.929），v2 完成后需确保新 metrics 精确
- runtime_benchmark notes 说"不写入正文，仅 reviewer 显式要求时使用"——但若 rebuttal 中引用，OBD 更慢（44ms vs 14ms）这个事实不能回避
- Cross-transfer 矩阵中 avg_acc 排除了 LLaMA-8B（只算 ~1B 模型），直接算均值会对不上
- LLaMA Wiki 1v2 CI [0.5788, 0.6049] 跨 θ=0.60，Mistral Code 1v2 CI lower=0.6024 仅高出 θ 0.24pp——两个 borderline 是审稿人攻击面
- FineWeb 降级到 CC-MAIN-2024-51（非 2025-26），若引用需标注实际版本
