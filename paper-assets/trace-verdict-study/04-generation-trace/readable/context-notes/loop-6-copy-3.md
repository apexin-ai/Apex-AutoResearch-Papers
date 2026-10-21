# reviewer / loop_6.md

**Trace Verbosity Degrades SFT Verdict Prediction: A Case Study in Information Density Effects** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/reviewer/loop_6.md`
- **Structured JSON:** [`c00e15c37c75160fb417.json`](../../sessions/c0/c00e15c37c75160fb417.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 6
reason: max_messages
updated: '2026-05-16T05:19:20+00:00'
---

### 1. 🔴 硬约束 / 红线
- 服务器 westd-11235 有 2 GPU（cuda:0, cuda:1），本项目无 constraints.yaml 限制 gpu_ids，但须确认两卡均归本项目使用，不与其他项目冲突
- 论文 tex 源文件的**权威版本**在远程 `/root/trace-verdict-study/docs/paper/`，本地 `projects/trace-verdict-study/docs/paper/` 是压缩 worker 写入的精简版（218行），**与远程不同步**（远程 445 行）。任何论文修改必须写入远程，不要只改本地
- Ethics Statement 和 ARR Checklist 中 GPU 描述有错："single RTX PRO 6000" 应为 "two RTX PRO 6000 Blackwell Server Edition GPUs (96 GB each)"——已提交 CRITICAL，等 Director 安排修正
- DeepSeek VOTA 84.45% 是 max_length=16384 eval 的正确结果（D030 已关闭），不要再质疑这个数字

### 2. 🖥️ 基础设施快照
- 服务器：westd-11235(root)，工作目录 `/root/trace-verdict-study`
- Python：`/root/miniconda3/bin/python`（conda base 环境，`source /root/miniconda3/etc/profile.d/conda.sh && conda activate base`）
- 模型：Qwen `/root/trace-verdict-study/models/Qwen2.5-Coder-7B-Instruct`，DeepSeek `/root/autodl-tmp/models/deepseek-coder-6.7b-instruct/deepseek-ai/deepseek-coder-6___7b-instruct`
- 数据：`/root/autodl-tmp/trace-verdict-study-data/`，Checkpoints：`/root/autodl-tmp/trace-verdict-study-checkpoints/`
- HF_HOME：`/root/autodl-tmp/.hf_cache`
- W&B project：`trace-verdict-study`
- 论文 tex：`/root/trace-verdict-study/docs/paper/`（远程权威），PDF 编译在此目录
- GPU：2× NVIDIA RTX PRO 6000 Blackwell Server Edition, 各 96GB

### 3. 📊 当前状态
**我刚完成的审查**：4 个 paper worker 的审查报告已全部提交给 Director：
1. **compilation-provenance-check**: WARNING — provenance 覆盖率声称 32/32 但遗漏 regex_baseline、DebugBench、trace length ablation、deepseek_full_trace_v3 共 7+ 个实验
2. **ethics-and-reproducibility**: CRITICAL — GPU 数量/型号错误（single→two, 94GB→96GB），C2 multi-seed 描述与实际不符
3. **discussion-and-maintext-polish**: WARNING — 内容正确但论文 13 页超 EMNLP 8 页限制，fail_recall 45.43% 应为 45.4%
4. **compress-to-8pages**: CRITICAL — 压缩版仅存本地（218行），远程未同步（445行），且与 ethics/polish worker 冲突
5. **fix-table-captions**: 未完成审查（table worker 同样写入本地，远程 experiments.tex 时间戳 10:29 未变、appendix.tex 13:03 是 ethics worker 写入）

**RUNNING 实验**：
- `ae_only_seed123`（cuda:0, PID 235494）— ae_only seed robustness
- `ae_only_seed456`（cuda:1, PID 235571）— ae_only seed robustness
- 两卡 GPU util 100%/90%，显存各 ~41GB，正常

**PREPARING**：`label_only_seed123`, `label_only_seed456`（等 GPU 空出）

### 4. 📋 待办
- ae_only_seed123/456 完成 → 核实 accuracy 是否与 seed42 (99.92%) 一致，检查 seed robustness；如果 variance 显著 → severity warning
- label_only_seed123/456 开始训练 → 检查 GPU 分配合规
- Director 决策论文压缩方案后 → 审查合并后的远程文件（本地压缩版 + 远程 ethics/polish 版需合并，特别是 appendix 新增的 sec:tokenizer_analysis 等标签需补齐）
- 任何新的 paper_agent_request_review → 按 §5.3 评分模板走

### 5. 🎯 战略上下文
**核心结论**：exception_only 是 verdict prediction 最有效信号（Qwen 99.83%±0.00，DeepSeek 2/3 seeds 99.33%），VOTA 跨模型 gap 14.96pp 因截断+模型能力混淆。Information density decomposition: gradient dilution 26% + information overload 74%。

**最易判错的事**：
1. 本地 vs 远程文件不同步——当前本地 `docs/paper/` 是压缩版，远程是完整版+ethics/polish。**审查论文内容必须读远程**（ssh_read_only），不要读本地
2. DeepSeek VOTA 的 reeval_with_fixed_script (16%) 是 eval-time 截断 bug 导致的，不是真实结果。真实结果是 84.45%（max_length=16384 eval）
3. 论文页数是**阻塞性问题**——EMNLP 8 页限制 vs 当前 13 页正文。Director 需决定压缩策略后才能推进
4. provenance 中 C029 "VOTA_no_ae = 99.41%" 实际 registry 是 99.40%，精度差 0.01pp
5. DeepSeek exception_only seed123 (91.09%) 是 LoRA 初始化离群值，不是 signal 问题——Qwen 3 seeds 完美证明 signal 本身 robust


---
