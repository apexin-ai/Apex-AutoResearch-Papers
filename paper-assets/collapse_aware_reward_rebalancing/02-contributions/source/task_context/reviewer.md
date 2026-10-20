---
loop: 3
reason: max_wall_time
updated: '2026-05-17T10:39:05+00:00'
---

### 1. 🔴 硬约束 / 红线
- GPU 白名单：**cuda:0, cuda:1** only（项目 execution.gpu_ids）。越界即 CRITICAL。
- C7 registry 绝对值有误：registry 中 C7 gen0/1/2 = 107.81/107.83/107.86，实际 JSON = 108.08/107.85/108.13。**论文用的是正确的 JSON 值**。不要用 registry 值"纠正"论文。
- 论文 Vendi 指标以原始实验 registry 为准（carr_quick_probe_03 等），不用 c1-regen-v2 的指标（regen 仅供 format 分析用，eval 有随机性导致绝对值不同）。

### 2. 🖥️ 基础设施快照
- 服务器：bjb2-23165(root)，工作目录 /root/autodl-tmp/carr
- Python：/root/miniconda3/bin/python（conda base）
- 模型：Qwen3-0.6B（base），ArmoRM-Llama3-8B-v0.1（reward）
- 数据：openbmb/UltraFeedback，cache at /root/autodl-tmp/carr 下
- 嵌入模型：sentence-transformers/all-MiniLM-L6-v2
- 输出目录：outputs_lora_k4_curated/ (C1 regen), outputs_k8/ (C2), outputs_fullft_k4/ (C3), outputs_fullft_lr2e5/ (C4), outputs/ (C5 baseline), outputs_fullft_nocuration/ (C6), outputs_fullft_lr2e5_nocuration/ (C7), outputs_fullft_lr2e5_k16/ (C8/K=16)
- 活跃进程：截至 handoff 时刻 **双 GPU 均空闲（0% util, 0 MiB）**
- c1-regen-v2：实际已完成但 registry 仍 RUNNING，需要更新

### 3. 📊 当前状态
**论文写作 8/8 sections 完成 + K=16 集成完成 + 引用审计完成。**

刚完成审查：
- Fig 2 v2（含 K=16）PASS
- Fig 3（direction reversal）PASS
- Fig 1（pipeline diagram）PASS
- K=16 实验 PASS（Vendi -0.19%，第 6 个 NEGATIVE，确认 Outline A）
- Bibliography audit PASS（LoRA 重复删除，Qwen3 引用添加）
- K=16 paper integration WARNING（C8 无配对 random baseline，table caption 需改）

Registry: 15 entries total。DONE: 13（含 K=16 刚完成），FAILED: 1（c1-regen v1 OOM），RUNNING: 1（c1-regen-v2 实际已完成需更新 registry）。

### 4. 📋 待办
- c1-regen-v2 registry 更新为 DONE → 用其 generation data 跑 C1 vs C5 format diversity 对比 → 更新 analysis.tex（当前用 C2 K=8 vs C5 K=4 不同 K 对比，应改为 C1 vs C5 同 K=4 对比）
- 最终 PDF 编译完成 → 全文 proofread 审查（dash 清零、-ing phrases、数字一致性）
- Discussion Section 6.4 的 r=0.63-0.77 misattribution 是否已修复 → 验证（之前 CRITICAL：该数字是 proxy dimension 间相关性，不是 reward-judge 相关性）
- Experimental setup 的 batch size 错误是否已修复 → 验证（Full-FT effective batch=8 not 16）
- 之前提出的 3 个 CRITICAL + 多个 WARNING 是否全部在最终版中修复 → 逐条核对

### 5. 🎯 战略上下文
- **核心结论**：reward curation 不导致 semantic collapse（6/6 FAIL，K=4/8/16 全 negative）。真正的 collapse 发生在 format 层面（opening entropy -1.13 bits, near-dup 50%→84%）。LoRA 的 diversity suppression 是 capacity artifact 非 curation 本身。
- **决策链**：D001-D011，从 MVP → P1 falsification（5/5 FAIL）→ Direction C CARR（99.3% overlap FAIL）→ Direction D "collapse is real but mischaracterized"（当前）
- **论文路线**：Outline A（pure negative paper），EMNLP 8 页目标
- **易错点**：
  1. 不要混淆 regen 指标和原始实验指标（regen gen0 Vendi=107.21 ≠ 原始 C1 107.54）
  2. C7 registry 值是错的，论文是对的（以远程 JSON 为准）
  3. Format metrics 对比要用同 K 配对（C1 K=4 curated vs C5 K=4 random），不要用 C2 K=8 vs C5 K=4
  4. Discussion 6.4 的 r=0.63-0.77 是 quality/diversity/complexity 三个 proxy 维度的 Pearson 互相关，不是 ArmoRM 与外部 judge 的相关——之前 CRITICAL 过，确认是否已修
