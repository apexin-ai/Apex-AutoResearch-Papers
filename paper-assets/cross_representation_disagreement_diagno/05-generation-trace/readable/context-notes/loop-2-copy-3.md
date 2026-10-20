# reviewer / loop_2.md

**Cross-Representation Disagreement as a Diagnostic Signal for LLM Reasoning Errors** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/reviewer/loop_2.md`
- **Structured JSON:** [`822b52b23da12a523ac3.json`](../../sessions/82/822b52b23da12a523ac3.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 2
reason: max_wall_time
updated: '2026-05-14T14:20:14+00:00'
---

### 1. 🔴 硬约束 / 红线
- autodl-rtx6000pro 是单 GPU 服务器（cuda:0），vLLM 进程 PID 19902 独占，pipeline 通过 API 调用不直接占 GPU
- formalize.py 已被 v5/v5b worker 修改了两次（21:03, 22:05），但 v4 pipeline 进程内存中仍是旧版。**v4 跑完前禁止 resume 或重启 pipeline**，否则会混入 v5b prompt 产生不一致数据
- v5b 必须作为独立实验（新输出文件）注册运行，不得 resume v4 的 mvp_v4_full.json

### 2. 🖥️ 基础设施快照
- 服务器：autodl-rtx6000pro，工作目录 `/root/autodl-tmp/crdd`
- Python：`/root/miniconda3/bin/python`（conda base 环境）
- vLLM：PID 19902，`--quantization awq_marlin --max-model-len 16384 --gpu-memory-utilization 0.90`
- 模型：`/root/autodl-tmp/models/Qwen3-32B-AWQ`，API at `http://localhost:8000/v1`
- 数据集：FOLIO validation set（yale-nlp/FOLIO），204 samples
- Pipeline：PID 29177（v4 全量），tmux 未确认，nohup 方式启动
- 日志：`/root/autodl-tmp/crdd/pipeline_v4_full.log`，结果：`results/mvp_v4_full.json`
- 无 W&B 配置
- 第二台服务器 westd-32608 未使用

### 3. 📊 当前状态
v4 pipeline 正在运行：66/204 done（3h+ elapsed），预计还需 ~6h。GPU 100% utilization 正常。

**已完成审查并发送 Director 的报告：**
1. 中期审查（37样本）：C1 disagree 33.3% PASS，C2 diagnostic 91.7% PASS，但 DISAGREE 极度不对称（FOL对:Code对 = 10:1），Code "Unknown" 偏差是主要分歧来源
2. v5 prompt critical：closed-world + 禁止 Unknown 造成 FOL-Code 语义不对称，已被 v5b 回退
3. v5b prompt 评估：设计合理（收紧 Unknown 而非禁止），降级为 warning
4. Example 3 修复：最后一个 else 分支从 Unknown→False，符合 anti-hardcoding 精神

Registry RUNNING：mvp_pipeline_004, mvp_pipeline_003b（均指向同一物理进程 PID 29177）。003b 是冗余条目。

### 4. 📋 待办
- v4 pipeline 完成（204/204）→ 全量审查所有 5 个 MVP 指标（C1-C5），重点：(1) DISAGREE 不对称比例是否在全量数据中稳定 (2) C4 targeted vs blind repair delta (3) C5 localization accuracy (4) Unknown 共享一致性分析
- v5b 实验启动通知到达 → 审查：确认独立输出文件、registry 条目完整、未 resume v4
- Director 决策 v5b 是否执行 → 如批准，关注 v5b 与 v4 的 Code Unknown 率对比
- registry 清理通知 → 确认 003b 冗余条目被清理

### 5. 🎯 战略上下文
- 项目目标：EMNLP 2026 ARR May 25（还剩 11 天），验证 FOL+Python 双表征分歧是否提供逻辑推理错误诊断信号
- 决策链：D001(MVP方案) → D002(Reviewer修订C4/C5) → D003(应急方案) → D004(回退闭源模型) → D005(v1失败,Z3 crash) → D006(v2改善,Code crash)
- **最容易判断错的事**：DISAGREE 高≠方法有效。当前 33% disagree rate 看起来很好，但 10:1 不对称（几乎全是 FOL 对 Code 错）意味着"分歧诊断"可能退化为"Code 路径更弱"。论文 framing 需要正面处理这个不对称性，否则审稿人会攻击 bidirectional diagnostic signal 的 claim
- **容易踩的坑**：formalize.py 当前是 v5b 版本，v4 pipeline 进程内存是旧版——千万不要以为"文件里写的就是正在跑的"。验证 v4 结果时以日志和 JSON 为准，不要参考当前源文件中的 prompt


---
