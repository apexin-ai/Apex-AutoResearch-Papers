# director / loop_1.md

**Trace Verbosity Degrades SFT Verdict Prediction: A Case Study in Information Density Effects** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/director/loop_1.md`
- **Structured JSON:** [`184d7573c4967691cec6.json`](../../sessions/18/184d7573c4967691cec6.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 1
reason: max_messages
updated: '2026-05-14T22:11:33+00:00'
---

### 1. 🔴 硬约束 / 红线
- GPU 白名单：westd-11235 cuda:0, cuda:1 only（gpu_constraint 已配置）
- GPU 0 有 ~49GB 显存残留（无活跃进程），训练前考虑 reset 或优先用 GPU 1
- **MVP 第一轮结果全部无效**（D002）：VOTA 99.16% 来自 match=True/False 信息泄漏，full_trace 28.4% 来自 label 截断。当前 checkpoint 全部作废，不可用于任何结论
- memory.md 中的"MVP 结论"section 包含错误信息（基于泄漏数据），不可引用

### 2. 🖥️ 基础设施快照
- 服务器：westd-11235 (connect.westd.seetacloud.com:11235)，2×RTX PRO 6000 Blackwell 98GB
- 工作目录：/root/trace-verdict-study/（data/, scripts/, src/, traces/, models/, results/）
- 模型目录：models → /root/autodl-tmp/trace-verdict-study-models（symlink 到数据盘）
- Qwen2.5-Coder-7B-Instruct 已下载（4 个 safetensors 分片）
- Python：/root/miniconda3/bin/python（conda base 环境）
- CUDA 12.8, PyTorch 2.10.0+cu128, vLLM 0.18.1
- 数据盘 201GB 可用
- 已废弃 checkpoint：/root/autodl-tmp/trace-verdict-study-checkpoints/（no_trace/vota/full_trace 的 final/ 目录，全部作废）
- 活跃进程：无（所有训练已完成，GPU 空闲）

### 3. 📊 当前状态
刚完成 MVP 第一轮训练 + 评估，发现两个 critical bug（D002）。已向 Agent 下达修复指令（去 VOTA match 字段 + 智能截断保留 label），Agent 重置前正在处理该指令。

Registry 实验：
- no_trace_seed42_v3: DONE (success) — 75.13% accuracy, 有效但需重训（对照组）
- vota_seed42_v3: DONE — 99.16%，无效（信息泄漏）
- full_trace_seed42: DONE — 28.4%，无效（label 截断）
- 4 个 v1/v2 实验：已标记 killed

数据资产：
- raw_traces.jsonl (250MB, 5910 samples, 67% pass / 33% fail) — 有效，已修复管线
- VOTA compress 后的数据需要重新生成（去 match 字段后）
- format 后的训练数据需要重新生成（智能截断后）

### 4. 📋 待办
- Agent 新 session 启动 → 确认是否已收到修复指令；如未收到，重新下达：(1) vota.py 去 match=True/False 字段 (2) format_training_data.py 智能截断 trace 保留 label (3) 重新 compress + format + 训练 3 组 + 评估
- 修复后重训完成 → 用修复后的结果判断 MVP pass/fail（标准：VOTA ≥ no_trace + 2pp 且 bootstrap CI 不含 0）
- MVP PASS → complete_mvp() 进入 research 阶段
- MVP WEAK PASS → 追加 CRUXEval verdict variant 验证
- MVP FAIL → 排查 1 天，clean fail 则 pivot negative-result framing

### 5. 🎯 战略上下文
- 项目核心假设：trace SFT 对 verdict 任务（二分类 pass/fail）的收益 > 对生成任务的收益；VOTA 比 full-trace 更高效
- D001：MVP pass 阈值统一为 ≥2pp + bootstrap CI 不含 0
- D002：第一轮结果无效，需修复后重训
- **最容易判断错的事**：不要把第一轮 VOTA 99.16% 当成 MVP PASS。那是信息泄漏，不是代码理解能力。修复后 VOTA 准确率会大幅下降（文献提示可能在 75-85% 范围），做好 WEAK PASS 或 FAIL 的心理准备
- Reviewer 提醒：Wang et al. (EMNLP 2025) 已证明 raw trace 对 SFT 帮助有限，修复后 VOTA lift 可能远小于 24pp
- no_trace baseline 75.13%（lift +3.6pp over majority 71.5%）— 模型仅看 code + test 已有一定信号，VOTA 需要在此基础上再提 2pp
- 目标：EMNLP 2026，建议 June 15 ARR（原 May 25 太紧）
- MVP deadline: May 17（还有 2.5 天）


---
