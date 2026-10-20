# reviewer / loop_9.md

**Trace Verbosity Degrades SFT Verdict Prediction: A Case Study in Information Density Effects** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/reviewer/loop_9.md`
- **Structured JSON:** [`e162c5a863485883383a.json`](../../sessions/e1/e162c5a863485883383a.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 9
reason: max_wall_time
updated: '2026-05-16T19:56:01+00:00'
---

### 1. 🔴 硬约束 / 红线
- GPU 白名单：cuda:0 和 cuda:1（仅两张卡，westd-11235）
- GPU 0 有 ~49GB 残留死内存（历史泄漏，无法 reset），实际可用 ~48GB，必须用 --gradient_checkpointing
- nomarker 实验 output_dir 必须显式指定带 seed 后缀（seed123 因缺失 --output_dir 覆盖了 1.5B checkpoint，已发生事故）
- 训练命令必须链式 eval：`python train/train_sft.py ... && python eval/evaluate.py ...`，否则 eval 不会执行（seed123 事故教训）

### 2. 🖥️ 基础设施快照
- 服务器：westd-11235(root)，工作目录 /root/trace-verdict-study
- Python：/root/miniconda3/bin/python（conda base 环境）
- 模型路径：/root/trace-verdict-study/models/Qwen2.5-Coder-7B-Instruct，/root/autodl-tmp/models/CodeLlama-13b-Instruct-hf
- 数据：/root/autodl-tmp/trace-verdict-study-data/
- Checkpoints：/root/autodl-tmp/trace-verdict-study-checkpoints/
- HF_HOME：/root/autodl-tmp/.hf_cache
- 活跃进程：PID 299741 = codellama13b_exception_only_seed123（GPU 0, CUDA_VISIBLE_DEVICES=0）
- GPU 1：空闲（seed456 已完成释放）

### 3. 📊 当前状态
本轮完成的审查：
1. codellama13b_vota_seed42 = 98.57% — PASS，填补 Table 1 最后空格
2. exception_only_nomarker_seed123 — 发现 CRITICAL（eval 未执行，registry 录入了旧 1.5B 数据 97.82%）→ 已修正为真实值 98.32%
3. exception_only_nomarker_seed456 = 98.07% — PASS
4. cross_model_exception_only_overlap 分析 — 5 模型完美重叠（same 2 errors）确认
5. 跨架构 claim 评估 — 已给 Director 四层建议（exception_only 强 claim / VOTA 需 caveat / nomarker 仅 Qwen 内 / 不要 claim nomarker 跨架构）

Registry RUNNING：codellama13b_exception_only_seed123（GPU 0）
Registry ANALYZING：exception_only_nomarker_seed456（Worker 在写结论）
table1_data.md 仍有 CodeLlama VOTA = "*pending*"（多个 Worker 未成功更新，但 LaTeX experiments.tex 已正确写入 98.57%）

### 4. 📋 待办
- codellama13b_exception_only_seed123 完成 → 核实 accuracy（预期 99.83% 匹配 seed42），验证 GPU 合规，确认是否跑了 eval
- exception_only_nomarker_seed456 registry 更新为 DONE → 验证 metrics = 98.07% 是否正确录入
- 若 Director 问 nomarker 3-seed 汇总 → 数据已备好：97.65% ± 0.96pp（seed42 是 outlier）
- 若要求审查论文章节 → 需先 Read `review-reviewer-session-start` skill 和 `paper-visual-review` skill

### 5. 🎯 战略上下文
核心结论链：exception_only traces 提供 architecture-general, scale-invariant 信号（≥99.33% across 4 models）。残余 2/1190 error 是 GeneratorExit 数据标注 artifact，非模型能力问题。

关键决策：D053 升级 signal-limited claim 为 "demonstrate"（非 "suggest"），D054 nomarker 升格为 gatekeeper 实验（阈值 99.5% 未达到但 ~97.65% 仍支持 two-layer signal 叙事）。

易错点：
- `exception_only_nomarker/` 目录现在包含 7B seed123 模型权重（不是 1.5B！），但 eval_results.json 是旧的 1.5B 数据 — 真实 seed123 结果在 `eval_results_seed123_real.json`
- DeepSeek seed123 = 91.09% 是 LoRA init outlier（不是 overfitting），决策 D027 已确认
- CodeLlama VOTA = 98.57% 证明 DeepSeek VOTA 退化（84.45%）是模型特异性问题，不是 VOTA 方法缺陷
- table1_data.md（markdown 版）未更新不代表 paper 未更新 — LaTeX experiments.tex 已有正确数据


---
