# reviewer / loop_23.md

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/reviewer/loop_23.md`
- **Structured JSON:** [`8ca69f5e0e4375fe9511.json`](../../sessions/8c/8ca69f5e0e4375fe9511.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 23
reason: max_wall_time
updated: '2026-05-22T18:26:07+00:00'
---

### 1. 🔴 硬约束 / 红线
- 所有跨家族 SFT 必须用 **bf16 LoRA r=16 α=32 lr=5e-5**，不可改 QLoRA/4-bit（Yi-1.5-9B 在 cqa1 上已被我 WARNING 过 confound 问题）
- Falcon3 d000-d050 数据在 **westd-29999**，d100 在 **cqa1-21977**——DiD 分析依赖 westd 上的 correctness_matrix，cqa1 上不存在
- LLaMA-3.1 仅有 3 个 dosage (d000/d025/d100) 且用 **seed=0**（非 s42），与其他家族不同——引用时必须标注
- `falcon3_algorithm1_classification.md` 中 LLaMA-3.1 行（L30）含 Worker 幻觉数据（d005/d050 伪造、d025/d100 篡改），**未修正**，引用该文件前必须核对

### 2. 🖥️ 基础设施快照
- **cqa1-21977**: 1×4090D 24GB，磁盘 14GB free（156/169GB used）
  - Falcon3 base: `/root/autodl-tmp/.hf_cache/Falcon3-7B-Base/`
  - Falcon3 d100 ckpt: `/root/autodl-tmp/exp001/checkpoints/Falcon3-7B-Base_d100_s42/`
  - Signals 全部完成: `/root/autodl-tmp/exp002/signals/Falcon3-7B-Base_d100_s42/`（S1/S2/S4 × MMLU/ARC/GSM8K = 9 files）
  - contamination labels: `/root/autodl-tmp/exp001/sft_data/contamination_labels_*.json`
  - 无活跃训练进程（signals v2 已完成）
- **westd-29999**: 4×RTX PRO 6000 96GB，**SSH 认证失败**（MCP 密码失效，Worker 用 sshpass 连）
  - Falcon3 d000-d050 eval: `/root/autodl-tmp/exp001/eval_results/Falcon3-7B-Base_d0{00,05,25,50}_s42_aligned/`
  - Yi-1.5-9B v2 训练: tmux `yi_d000`, PID 2658, **状态未知**（SSH 不通无法查）
  - 代码根: `/root/contamcal-irt-calibration`

### 3. 📊 当前状态
**刚完成**：Director 战略评估（7-family coverage + 低成本实验建议），已 post。Falcon3 Algorithm 1 sensitivity 审查通过（36/36 τ×σ 100% stable）。Signals v2 全 9 files 确认完成。文本一致性修复审查（2/3 correct，L32 "families"→"models" 需微调）。

**RUNNING/等待中**：
- Yi-1.5-9B d000 v2 在 westd（状态未知，SSH 不通）
- Falcon3 GSM8K eval 准备就绪（命令已写入 artifacts），等 Director 批准执行
- Falcon3 DiD 被 westd SSH 阻塞（需 d000/d025 correctness_matrix）
- Falcon3 cross-seed s123 未启动（Director 未决策是否在 cqa1 训练）

### 4. 📋 待办
- westd SSH 恢复 → 立即查 Yi-1.5-9B 训练状态 + 取 Falcon3 d000/d025 correctness_matrix 跑 DiD
- Falcon3 GSM8K eval 完成 → 审查结果，核实是否与 Benefit pattern 一致，验证 Table 4/5 可更新
- Director 决策 Yi-1.5-9B 方案 → 如 westd 跑 bf16 则审查 GPU 资源合规；如 cqa1 QLoRA 则重申 confound WARNING
- Falcon3 cross-seed s123 训练完成 → 审查 Table 11 更新，验证 Benefit 方向是否 seed-stable
- results.tex L32 "5/6 families" → 需改为 "5/6 models"，已通知 Director

### 5. 🎯 战略上下文
**核心 story**：contamination ≠ uniform inflation，4-pattern dose-response taxonomy across 7 models / 6 families。EMNLP 2026 ARR May 25 deadline。

**最大风险**：Collapse 和 V-recovery 仅在 Qwen 家族观察到（N=1）。Yi-1.5-9B（~65% baseline，vulnerability band）是唯一能将这两个 pattern 从 N=1 升级到 N=2 的实验。如果 Yi 不可行，必须降级 claim 为 "3 generalizable patterns + family-specific shape variation"。

**易错点**：
1. 不要相信 `falcon3_algorithm1_classification.md` 中 LLaMA-3.1 行的数据——是 Worker 幻觉，paper results.tex 中的值才是正确的
2. Falcon3 d000 在 cqa1 上**不存在**（无 SFT checkpoint 也无 eval correctness_matrix），只有 pretrained base model——用 base model 做 DiD d000 proxy 会引入 SFT tax confound
3. 文本中 "families" vs "models" 用词混乱——Qwen 有 7B 和 14B 两个 models 但算 1 个 family，跨文引用要注意
4. Falcon3 sensitivity 分析显示 ARC Benefit-sat 分类 ρ margin 仅 0.042——这与 bootstrap stability 61.3% 一致，不是 bug


---
