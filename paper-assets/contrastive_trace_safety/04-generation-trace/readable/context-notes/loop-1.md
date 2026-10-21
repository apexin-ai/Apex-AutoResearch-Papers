# director / loop_1.md

**Layer Selection Sensitivity in Hidden-State Safety Probes for Reasoning Models** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/director/loop_1.md`
- **Structured JSON:** [`2aad17d2b3db2e55bf2f.json`](../../sessions/2a/2aad17d2b3db2e55bf2f.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 1
reason: max_messages
updated: '2026-05-17T08:38:20+00:00'
---

### 1. 🔴 硬约束 / 红线
- 本项目 GPU 只能用 autodl-rtx6000 的 2 卡（2× RTX PRO 6000 Blackwell 98GB）。bjb1-42106/cqa1/home-1x5090 是其他项目的，不可使用
- OpenThinker-7B bootstrap 用 matched W=3 对比（HS 和 Text 同 W），这是已验证的正确协议。不要改成 mismatched W
- Transfer 实验结论 framing 必须是 "fails entirely"，禁止写 "partial transfer observed"（Reviewer 特别警告过）
- CP 定义统一为 "safety label 最后出现的 step + 1"，不用 "首个 DKE"
- 论文 Holm-Bonferroni 现在是 12 tests（4 models × 3 metrics），不是之前的 9 tests

### 2. 🖥️ 基础设施快照
- 服务器：autodl-rtx6000 (connect.bjb1.seetacloud.com)，账号 root
- 工作目录：/root/autodl-tmp/contrastive_trace_safety
- GPU：2× RTX PRO 6000 Blackwell (98GB each)，当前两卡空闲
- 模型缓存：OT-7B (15GB) 已下载到服务器；R1-8B/R1-32B/QwQ-32B 已缓存 (62GB each)
- HarmThoughts 数据集已在服务器，4 模型 traces 全部可用
- 磁盘：~85GB 可用
- 活跃进程：无（OT-7B pipeline 已完成）
- Cron：无活跃实验 cron

### 3. 📊 当前状态
**刚完成**：OT-7B full pipeline (exp_ot7b_full_pipeline) — SUCCESS，Bonferroni 显著 (bal_acc p=0.001, FPR p=0.007)。这是第二个显著模型，跨架构+跨训练方法验证。

**审稿 Round 2 修复全部完成**：W1 Holm-Bonferroni ✅, W2 Transfer appendix ✅, W3-W14 文本修改 ✅, W6 excluded traces ✅, W7 GRU per-seed ✅。Paper Agent 两批 Patch 已写入 main.tex（15 pages, 编译 PASS）。

**Path C (adaptive window)**：降级为 Discussion mention + Appendix figure（改进在噪声范围内）。

**Path B (32B 数据扩充)**：降级。本地分类器 annotation validation FAIL (F1=0.59)，LLM API 可行但 4 模型已足够，不再需要。

**Registry**：17 experiments (8 success, 9 negative, 0 running)。exp_ot7b_full_pipeline 是最新成功。

**等待中**：Agent 正在处理我发的 W 匹配验证指令（确认 bootstrap 协议一致性）。Reviewer 已确认 W=3 matched 对比是正确的。

### 4. 📋 待办
- Agent 汇报 W 匹配验证结果 → 如确认一致 → 进入论文全面修订
- **论文 framing 升级（最重要）**：更新 paper_framing.md，从 "model-dependent" 升级为 "scale-dependent: 7-8B definitive, 32B directional"。Claim 2 从 3 模型扩为 4 模型
- **Claim 1 需 nuance**：OT-7B HS temporal gains 在 W>3 后反转（W=3 peak → W=25 下降）。改为 "temporal context universally improves text probes; for HS probes, gain is model-dependent (3/4 improve, OT-7B peaks at W=3)"
- **Layer 0 讨论**：OT-7B best layer = embedding (0% depth)，与其他模型不同。需在 Discussion 讨论，可选报告 layer 16 作为 best transformer layer
- **Holm-Bonferroni 更新为 12 tests**：重新计算 step-down。R1-8B precision (<0.001) + OT-7B bal_acc (0.001) + R1-8B accuracy (0.005) 应仍通过
- **Paper Agent 大 Patch**：整合 OT-7B 到全文（新 Table 行、新 Figure 数据点、Abstract/Intro/Method/Results/Discussion 全面更新）
- **提交最终审稿**：完成修订后 submit_paper_to_review (continue mode)

### 5. 🎯 战略上下文
**核心突破**：D023 — OT-7B 是 STILL-trained Qwen-7B，与 R1-8B (R1-distilled Llama-8B) 形成 2×2 验证。Architecture confound 和 training method confound 同时解决。论文从 Findings track (3.25/5) 升级瞄准 Main Conference。

**四模型格局**：
- R1-8B (Llama, distilled): precision p<0.001 ✅, accuracy p=0.005 ✅
- OT-7B (Qwen, STILL): bal_acc p=0.001 ✅, FPR p=0.007 ✅
- R1-32B (Qwen, distilled): directional (+8.4pp acc, p=0.08)
- QwQ-32B (Qwen, native): no significant difference

**易错点**：
1. OT-7B precision 只有 35.7%（其他模型 58-77%），因 trace 长度 80 sentences。不要因此怀疑 OT-7B 结果——这是预期的，在 Results 中解释即可
2. OT-7B HS temporal gains 反转 ≠ Claim 1 失败。Claim 1 核心是 "temporal context helps"，OT-7B 只是 peak 在 W=3 而非 W=25。Text probes 仍然 W↑ 提升
3. D012 曾排除 OT-7B（"加剧 Qwen 占比"），现在重新纳入是因为审稿人要求更多模型 + 非蒸馏独立验证价值。D023 覆盖了这个决策
4. DDL May 25（8 天）。论文当前 15 pages (8 main + appendix)，需要整合 OT-7B 后保持 ≤8 page main body
5. 审稿群 (Group C) review_chat_id: oc_4a087be8d8cfffc128323993d357d229。修订完成后用 submit_paper_to_review 提交


---
