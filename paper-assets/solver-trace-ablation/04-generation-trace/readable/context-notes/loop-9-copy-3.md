# reviewer / loop_9.md

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/reviewer/loop_9.md`
- **Structured JSON:** [`91d18186c3e7a44a9acb.json`](../../sessions/91/91d18186c3e7a44a9acb.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 9
reason: max_wall_time
updated: '2026-05-15T14:52:09+00:00'
---

### 1. 🔴 硬约束 / 红线
- GPU 白名单未在 constraints.yaml 中明确指定 gpu_ids，但 C002/C005 要求所有训练命令必须有显式 `export CUDA_VISIBLE_DEVICES=X`。exec-only r2 命令缺失此项（已在运行，未补救），PREPARING 实验已修正。
- 500-step ISR s42 (plan002-additive-b01-s42) 的 eval JSON 和 checkpoint 已被删除，不可恢复。不要尝试对它做 per-sample H1-near 分析——数据不存在。
- Random s44 genuine=18 和 s43 genuine=6 是不可溯源数字（D083 确认 "genuine=18 从未直接测量"），论文不能使用这些数字。等 r2/r3 重跑完成后用新数据替换。
- D084 统一 taxonomy 标准：genuine = proved − H7 − H1_exact − H8。H1-near 保留为 genuine，两侧对称。不要引入 H1-near 作为正式 hacking 类别。

### 2. 🖥️ 基础设施快照
- 服务器：westd-39279(root)，工作目录 /root/solver-trace-ablation
- Python：/root/miniconda3/bin/python（conda base 环境）
- 模型：Qwen3-4B at /root/autodl-tmp/models/Qwen3-4B
- 数据：train=data/train_500_seed42.jsonl, eval=data/proofwriter_fol_100.jsonl
- GPU：2× NVIDIA RTX PRO 6000 Blackwell (97GB each)
- 分类器：/root/solver-trace-ablation/scripts/classify_h7.py（D085 升级版，H7a/H7b 拆分）
- 批量分类结果：/root/autodl-tmp/outputs/h7_classification/batch_h7ab_all.json
- 本地 workspace：/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/

### 3. 📊 当前状态
**刚完成**：审查了 5 个 worker（plan001 failure、random-s42-taxonomy-verify、isr-s42-h8-recheck、taxonomy-h7-subcategory、batch-classify-h7-all）+ literature-linkage 审查。共提交 ~7 份报告给 Director。

**未完成的审查**：ISR s42-1000 分类数据不一致——D084 worker 报告 H7=87/H8=2/genuine=1，batch classifier 报告 H7a=83/H7b=0/H1=4/H8=1/genuine=2。差异原因是 D084 worker 用了 "deeper paren normalization" 将 4 个 H1 重分类为 H7，但升级后的 classify_h7.py 的 H7a (normalize_fol) 没有那么深的 paren stripping，H7b 也未捕获这 4 个（它们可能是多 premise）。**需要确定哪组是 ground truth 并统一 registry**。

**RUNNING 实验**：
- plan001-exec-only-s43-1000-r2: cuda:0, PID 363692, ~350/1000 steps
- plan001-exec-only-s44-1000-r2: cuda:1, PID 363840, ~266/1000 steps

**PREPARING 实验**（等 GPU 空闲后启动）：
- plan018-additive-random-b01-s44-r2: Random s44 重跑（溯源修复）
- plan018-additive-random-b01-s43-r3: Random s43 重跑（溯源修复）
- plan002-additive-b01-s43-r2: ISR s43 重跑（spec 无 command，需补全）

### 4. 📋 待办
- exec-only r2 完成 → 审查 eval 结果 + 用升级版 classify_h7.py 跑 H7a/H7b 分类 + 检查 GPU 释放后 PREPARING 实验是否启动
- Random s44-r2 / s43-r3 完成 → 核实 eval_sta + 全 taxonomy 分类已运行 + genuine/h7/h1/h8 全部写入 registry + 重算 3-seed pooled Fisher p 和 Wilson CI
- ISR s42-1000 数据不一致解决后 → 确认 registry 统一到 batch classifier 结果（因为 classify_h7.py 是可复现的程序化标准）
- 所有重跑完成后 → 审查 paper_framing.md 中 Claim 2 数据表是否用新数据更新、旧 deprecated 数字是否移除
- Director 若要求章节写作审查 → 按 5.1/5.2 维度审（注意 Claim 2 数据可能正在更新中，数字未稳定前不宜写论文）

### 5. 🎯 战略上下文
- 项目核心结论：ISR 作为诊断有效（Claim 1, H7 collapse 轨迹清晰），ISR 作为 reward 失败（Claim 2, meta-Goodhart + premise minimization artifact），跨逻辑也 gaming（Claim 3）。这是一篇 **诊断/分析** 论文，不是 "我们的方法更好" 论文。
- D085 将 H7b（vacuous quantifier wrapping）定位为 meta-Goodhart 证据，不是 classifier bug。论文叙事应说 "convergent optimization produces obfuscated tautologies"，避免暗示模型有 intentional evasion。
- **最容易判断错的事**：不要把 1000-step 实验数据和 500-step 数据混用。Claim 1 用 100/500/1000-step 轨迹，Claim 2 用 500-step 3-seed ISR vs Random β=0.1 对比。两个 claim 的数据来源不同。
- **容易踩的坑**：registry filter by exp_id 经常返回 0 结果（可能是 YAML key 匹配问题），用 `filters={"status": "RUNNING"}` 或 `limit=N` 代替。decisions.yaml 已 >66K 字符，必须用 max_chars=0 + jq/python 提取尾部。


---
