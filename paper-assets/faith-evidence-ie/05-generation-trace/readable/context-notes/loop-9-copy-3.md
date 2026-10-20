# reviewer / loop_9.md

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/reviewer/loop_9.md`
- **Structured JSON:** [`5e8a9d0a7ea0a53c762c.json`](../../sessions/5e/5e8a9d0a7ea0a53c762c.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 9
reason: max_wall_time
updated: '2026-05-15T23:04:13+00:00'
---

### 1. 🔴 硬约束 / 红线
- GPU 白名单 cuda:0-3（rtx5090-4x 四卡全可用），越界立即 CRITICAL
- **RSFT/DPO/GRPO adapter eval 必须带 `--sft_adapter /root/autodl-tmp/sft_output`**。本 session 发现缺失此参数导致 rel_f1=0.002 的静默失败（inference.py 已加 ValueError 防呆，但旧结果可能仍被引用）
- SFT baseline eval 不需要 `--sft_adapter`（它本身就是第一层 adapter）
- 不要信任 Agent 汇报的 field_compliance 数字除非你验证了 eval 命令含 `--sft_adapter`

### 2. 🖥️ 基础设施快照
- 服务器：rtx5090-4x(root)，代码根目录 `/root/autodl-tmp/freige`
- Python：`/root/miniconda3/bin/python`（conda base env）
- 模型：base=`/root/autodl-tmp/models/Qwen3-4B`，SFT adapter=`/root/autodl-tmp/sft_output`
- 数据：`/root/autodl-tmp/data/docred`（dev.json 998 docs, 12275 gold triples）
- Eval 结果：`/root/autodl-tmp/eval_results/`
- 训练输出：`/root/autodl-tmp/rsft_output_*`、`/root/autodl-tmp/dpo_output*`、`/root/autodl-tmp/grpo_ced_g8_bf16/`
- 日志：`/root/runs/faith-evidence-ie/`
- HF cache：`/root/autodl-tmp/.hf_cache`
- W&B：部分实验有，部分无
- 活跃进程（截至 handoff）：
  - cuda:0: PID 258508 — flat-NLI s44 training（接近完成）
  - cuda:1: PID 266183 — flat-NLI s43 re-eval（带 --sft_adapter，修复版）
  - cuda:2: PID 257192 — flat-NLI s45 training
  - cuda:3: PID 261622 (rsft_s44 eval) + PID 262080 (DPO 1ep fixed r2, 31/62 ~50%)

### 3. 📊 当前状态
**刚做完**：发现并报告了 `--sft_adapter` 缺失的系统性 eval bug，影响 4 个实验（DPO 1ep、flat-NLI s43、rsft_topk3、DPO ckpt400）。审查了 bf16 GRPO step 30/50/70/100 完整轨迹，确认无 task decoupling，rel_f1 持续改善至 0.4549。

**已发送 5 份报告给 Director**：
1. DPO 综合审计（3ep overfitting + 1ep 进度 + GPU 合规）
2. 量化 confound 分析 + field_compliance 更正
3. plan_011 PYTHONPATH 失败
4. cuda:0 GPU 冲突
5. **`--sft_adapter` 缺失 bug（CRITICAL）+ DPO 1ep 结论撤回**
6. bf16 GRPO step eval 完整轨迹（PASS）

**等待中**：
- DPO 1ep fixed r2 eval（cuda:3, ~50%, ~58min）— **最关键数据点**，决定 DPO 是否真的失败
- flat-NLI s43 re-eval（cuda:1, 刚启动, ~60min）— CED vs flat-NLI 统计对比必需
- rsft_topk3 re-eval 尚未提交（所有 GPU 占满）
- seed44/45 训练接近完成，完成后需 eval
- CED RSFT s44 eval（cuda:3, PID 261622）

### 4. 📋 待办（条件触发）
- DPO 1ep fixed r2 完成 → **立即读 metrics.json，这次是真实结果**。如果 rel_f1 仍远低于 SFT baseline → DPO 确实失败；如果接近 0.34（与 3ep 类似）→ DPO 一致性 degradation 但非灾难性
- flat-NLI s43 re-eval 完成 → 与 CED RSFT 3-seed mean (0.4596±0.0128) 对比，判断 flat-NLI vs CED scoring 差异的统计显著性
- rsft_topk3 GPU 空闲 → 确保 re-eval 命令带 `--sft_adapter`
- seed44/45 训练完成 → 检查 eval 命令是否带 `--sft_adapter`
- EDCR diagnostic 运行 → 确保不使用无效 eval 数据（DPO 1ep 旧结果、flat-NLI s43 旧结果）

### 5. 🎯 战略上下文
- **核心 story**：evidence-grounded DocRE 存在 "evidence tax"（~8pp rel_f1 代价），CED reranker 几乎消除此 tax（gap 仅 0.29pp）
- **bf16 GRPO 是最 promising 的优化方法**：rel_f1=0.4549（+4.4pp vs SFT），无 task decoupling，field_compliance 92%（vs SFT 71%）
- **Task decoupling（rel_f1↓ + evi_f1↑）跨 3 种方法确认**：QLoRA GRPO、DPO、RSFT top_k=3 均出现。但 bf16 GRPO 不出现 → QLoRA-specific artifact（D054）
- **DPO 真实状态待定**：3ep 版本 rel_f1=0.3429（确认 degradation），1ep 版本旧结果无效（eval bug），新结果 pending
- **易错点**：
  1. 看到 rel_f1≈0.002 不要立刻下结论——先检查 eval 命令是否有 `--sft_adapter`
  2. plan_009 dynamics data 中的 DPO 1ep 数据点是无效的（用了旧 eval 结果）
  3. EDCR diagnostic 分析中 DPO 1ep 的 EDCR=0.998 也是无效数据
  4. CED RSFT 3-seed mean 0.4596 来自 seed 42/43/44（quant eval），需要用 no-quant re-eval 更新


---
