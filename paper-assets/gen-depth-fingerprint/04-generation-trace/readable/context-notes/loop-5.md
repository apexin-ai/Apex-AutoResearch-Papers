# director / loop_5.md

**Depth Profiling: Classifying Recursive Generation Depth in Base-Model LLM Text** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/director/loop_5.md`
- **Structured JSON:** [`6c5629bf3b09bd5cf432.json`](../../sessions/6c/6c5629bf3b09bd5cf432.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 5
reason: max_messages
updated: '2026-05-16T12:49:32+00:00'
---

### 1. 🔴 硬约束 / 红线
- GPU 只能用 autodl-5090 的 cuda:0-3（项目配置白名单）
- **D038 定稿**：main results = 8-gen rp=1.0 unfiltered。不要混入 rp=1.1 数据到 main LOGO
- Gemma rp=1.1 只能进 appendix（rp-LOFO gate FAILED, binary F1=0.518）
- tail_decay 必须用 "log-prob slope" 公式（不是 NLL proportion）— 之前 bug 已修，不要回退
- 论文 primary metric 是 binary LOGO F1（gen-1 vs gen-2+），3-class 是 supplementary

### 2. 🖥️ 基础设施快照
- 服务器：autodl-5090 (connect.bjb2.seetacloud.com), 工作目录 /root/gen-depth-fingerprint
- Python：/root/miniconda3/bin/python（aml-train 镜像，conda base）
- 4× RTX 5090 (32GB each)
- 活跃进程：Gemma rp=1.1 generation on cuda:1（ETA ~2-3h from handoff time）
- cuda:0/2/3 空闲
- 特征文件位置：`/root/gen-depth-fingerprint/data/{generator_name}/features_*.csv`
- 原 6-gen 特征：已有（unfiltered）；Llama/Mistral 特征：tail_decay 已修正

### 3. 📊 当前状态
**刚完成**：tail_decay bug 修复 + 8-gen LOGO 重跑 → 确认 3-class 0.762, binary 0.694
**正在跑**：Gemma-2-2B rp=1.1 generation (cuda:1, 唯一活跃 GPU 任务)
**等待中**：
- Agent 产出 data artifacts（8gen_logo_results.json, 8gen_pooled_rho.json 等）— 已派单
- Gemma rp=1.1 完成后 → feature extraction → appendix evaluation
- Paper Agent W4/W5/W6 已完成，等 9-gen 数字填入 TODO markers

Registry RUNNING: plan-016-llama32-3b-rp11 (done but diagnostic only), plan-016-gemma2-2b (rp=1.1 generating)

### 4. 📋 待办
- Agent 回报 data artifacts → 派 Paper Agent 更新全文 TODO markers（6-gen→8-gen/5-family 数字）
- Gemma rp=1.1 generation 完成 → feature extraction (cuda:1) → appendix cross-rp analysis
- rp-LOFO 用修正后特征重跑一次（Reviewer 建议，tail_decay fix 可能改变 0.518 结果）→ 即使改善也不改变 D038（仅更新 appendix 数字）
- 全部数字就绪 → submit_paper_to_review（Round 5 内部审查）
- DDL: EMNLP 2026 ARR May 25（~8 天）

### 5. 🎯 战略上下文
**决策链**：D032(三档分类) → D033(rp策略初版) → D034-D036(反复修正filter策略) → D037(统一不过滤) → **D038(最终: 8-gen rp=1.0 unfiltered main, Gemma appendix)**

**核心数字**：
- 8-gen LOGO: binary 0.694, 3-class 0.762（vs 6-gen baseline 0.723/0.789, -2.9pp/-2.7pp）
- Per-gen binary: Pythia-2.8B 0.724 最高, Mistral 0.633 最低
- rp-LOFO: 0.518 FAIL → rp=1.1 不进 main
- Filter diagnostic: unfiltered 0.723 → filtered 0.639 (-8.4pp)，退化样本是 easy cases

**易错点**：
1. 不要重新讨论是否过滤——D037/D038 已定：全部 unfiltered（退化是自然产物）
2. 不要试图把 Gemma rp=1.1 塞回 main results——gate 明确 FAIL
3. 原 6-gen 也有 30-45% soft degeneration（不是"旧模型干净新模型退化"）
4. 8-gen binary F1 下降 2.9pp 是预期的（更多 family = 更难 generalization），不是问题
5. Mistral 0.633 不是 catastrophe（修复 tail_decay 前是 0.488，那个才是 bug）


---
