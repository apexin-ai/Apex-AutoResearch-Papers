# reviewer / loop_5.md

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/reviewer/loop_5.md`
- **Structured JSON:** [`772ee52964f2bcdd038b.json`](../../sessions/77/772ee52964f2bcdd038b.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 5
reason: max_wall_time
updated: '2026-05-14T14:59:03+00:00'
---

### 1. 🔴 硬约束 / 红线
- GPU 白名单：cuda:0 + cuda:1（westd-16980 仅 2 卡）。之前出过 duplicate PID 事故（PID 190246 + 190653 同时写一个文件），检查进程时必须 nvidia-smi 交叉验证 PID→GPU 映射
- registry 中 `llama_docred_unconstrained` 的 spec.command 写的 `--device cuda:0` 但实际跑在 cuda:1（通过 CUDA_VISIBLE_DEVICES 重映射）。reproduce.command 同样有误。不要因为 command 文本写 cuda:0 就误判 GPU 违规
- ET 指标有两种口径：violation_checker_docred.py 用 entity-level（per-entity），analyze 脚本用 triple-level（per-triple all_set）。两者数值差异大（如 18.44% vs 2.47%）。**对比不同实验 ET 时必须确认口径一致**，fix worker 声称修了但代码时间戳未变
- F1 必须用 all_set 方法（OOV 计入分母）。recognized_set 会过滤 unconstrained 的 5189 个 OOV predictions 人为抬高 precision，已被确认为错误方法

### 2. 🖥️ 基础设施快照
- 服务器：westd-16980 (root)，2× NVIDIA RTX PRO 6000 Blackwell (98GB each)
- 工作目录：`/root/schema_semantic_constrained_ie`
- Python：`/root/miniconda3/bin/python3`（conda base 环境）
- 模型路径：Qwen3-8B 和 Llama-3.1-8B-Instruct 均在 `/root/autodl-tmp/models/LLM-Research/`
- 数据：`data/scierc/` + `data/docred/dev.json` + `data/docred/ontology_constraints_docred.json`
- 输出：`outputs/llama_docred_full_s1.jsonl` + `outputs/llama_docred_unconstrained.jsonl`
- 活跃进程（截至 handoff）：
  - PID 194300 (python3 子进程, tmux session llama_docred_full_s1) → cuda:0, 39/998
  - PID 193610 (python3 子进程, tmux session llama_docred_unconstrained) → cuda:1, 53/998
- 本地 workspace：`/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/`

### 3. 📊 当前状态
本 session 完成了 8 次 reviewer_post_to_director：llama_scierc_unconstrained (WARNING), duplicate PID 事故 (CRITICAL×4), llama_scierc_full_s1 recovery (PASS), phase2_docred_semantic_only (WARNING/CRITICAL for ET spike→后降级), ET 测量不一致 (WARNING), registry 格式不一致 (WARNING)。

**RUNNING（2 个，最后的 D009 cross-model 实验）：**
- `llama_docred_full_s1`：cuda:0, 39/998 (~3.9%), ~10s/doc, 预计还需 ~2.5h。日志显示 grammar-first fallback 已触发 47 次（semantic mask 过紧导致回退），这个比率在实验完成时需要关注
- `llama_docred_unconstrained`：cuda:1, 53/998 (~5.3%), ~18s/doc, 预计还需 ~4.5h

**等待：** 两个实验的 cron on_complete 回调 → 需要审查

### 4. 📋 待办
- `llama_docred_unconstrained` cron 回调 → 核实 998 行完整性 + 无 duplicate + GPU 合规 + violation 分布 vs Qwen DocRED unconstrained + registry 指标交叉验证
- `llama_docred_full_s1` cron 回调 → 同上 + **重点关注 grammar-first fallback 总次数**（若 >>100 说明 semantic 层在 Llama+DocRED 上过紧，影响 constraint tightness narrative）+ DR 对比 Qwen DocRED full_s1 (10.19%)
- 两个 Llama DocRED 都完成 → 综合 cross-model 审查：4 组对比（SciERC×2 + DocRED×2），验证 "model-agnostic" claim 是否站得住。特别关注 DocRED 上 Llama DR 降幅是否与 Qwen 一致（Qwen 仅 ↓44.8%，远低于 SciERC ↓94%）
- ET 归一化修复仍未落地 → 若 Agent 声称修了，`stat` 验证文件时间戳是否变化
- experiment_plan.yaml 仍为空 → 提交前需要补全 claim-experiment 映射（低优先级）

### 5. 🎯 战略上下文
- **项目核心结论**：OntoCoDec grammar+semantic 双层约束在 SciERC 上 DR↓94%、F1 不变。DocRED 上 DR↓44.8%（弱于 SciERC，但 RV/ET→0%）。S2 降级为 ablation，S1 为主推
- **D009 是 Risk #2 的唯一缓解**：paper_framing.md 标 "Single model limitation" 为 MEDIUM-HIGH。Llama SciERC 已完成且非常好（DR 13.3%→0.08%, ↓99.4%）。DocRED 是最后一块拼图
- **最容易判断错的事**：
  1. 不要因为 Llama F1 低（R-F1=2.54% vs Qwen 8.36%）就质疑实验有效性——F1 是 control variable 不是 target，两模型差异反映 instruction-following 能力差异
  2. DocRED full_s1 DR 预期不会像 SciERC 那样降到 <1%（96 relations 约束空间太大），Qwen 也只到 10.19%。如果 Llama DocRED DR 在 8-15% 范围内，仍是正常结果，不要标 CRITICAL
  3. registry 格式已统一为小数（之前的 percentage 问题已修复），但 ET 口径不一致是真问题——entity-level 和 triple-level 差异可达 8× (18.44% vs 2.47%)
- **DDL 压力**：EMNLP ARR May 25，内部稿 DDL May 19（距今 5 天）。论文大部分章节已写完，§5 DocRED + Cross-model subsection 等实验结果填充


---
