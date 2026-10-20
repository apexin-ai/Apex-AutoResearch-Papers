---
loop: 4
reason: max_wall_time
updated: '2026-05-15T12:10:35+00:00'
---

### 1. 🔴 硬约束 / 红线
- 本项目 GPU 白名单：rtx6000-diagprobe 的 cuda:0 + cuda:1。当前 MVP 阶段全是 API 调用（DeepSeek-V4-Flash via OpenRouter），GPU 未实际使用，但 Research 阶段 student training 会用到，必须核对
- API endpoint: `http://47.94.22.126/v1`（OpenRouter 代理），key 在 `/root/trace_distill_repair/.env`
- bugsinpy_workspace 中每个实例的 buggy/ 目录是原始状态，**不要写入**——reeval 脚本会临时替换文件再恢复，如果中途崩溃可能留下脏状态，审查时注意检查
- fastapi_1 ground truth 涉及 5 个文件（含 test 文件本身），pipeline 只修 changed_files[0]，这是已知限制不是 bug

### 2. 🖥️ 基础设施快照
- 服务器：rtx6000-diagprobe(root)，工作目录 `/root/trace_distill_repair`
- Python：`/root/miniconda3/bin/python`（conda base），bugsinpy 测试用 `/root/miniconda3/envs/bugsinpy`（Python 3.8）
- 关键数据路径：
  - pipeline 输出：`/root/trace_distill_repair/pipeline_output/`（phase3_results.csv, phase3_checkpoint.json, phase3_summary.json, reeval_test_results.json）
  - 实例定义：`pipeline_output/phase3_instances.json`（33 实例 × changed_files / ground_truth_patch / trace paths）
  - 日志：`~/runs/trace_distill_repair/mvp_phase3_repair.log`
- 活跃进程：截至 handoff 时无活跃训练/API 进程（Phase 3 v1 已完成，v2 pipeline fix 由 Agent 执行中）
- W&B：未配置（本项目不检查 W&B）

### 3. 📊 当前状态
**我刚完成**：
1. 对 Director 5 项系统触发审查的逐项核实（Q1-Q5），发现 Agent 遗漏三个重大 confound（退化 prompt / buggy_code 提取失败 / judge 自评偏差）
2. ROADMAP D021 更新后的审查，提了 5 点建议（httpie_2 纳入 Tier 1 / D016 segment cap / 验证步骤 / registry 状态更新 / 时间线）

**Registry 状态**：
- `mvp_phase3_repair`: ANALYZING / conclusion=negative（应标 invalidated，已建议 Director）
- 其他 15 个实验全部 DONE/killed
- 无 RUNNING/PREPARING 实验

**等待中**：Agent 正在执行 pipeline fix（get_buggy_code 修复 + prompt 格式改 diff/patch + 实例分 Tier）。修完后会重跑 Phase 3 v2。

### 4. 📋 待办
- Phase 3 v2 注册到 registry 且 status=RUNNING → 核查 spec 中 buggy_code 提取是否修复（对比 youtube-dl/tornado/luigi 的 tokens_input 是否合理，不再是 ~289 tokens）
- Phase 3 v2 完成 → 全量审查：(a) 是否仍有实例输出完全无关代码 (b) clean subset h2h 结果 (c) test-based pass rate (d) tokens_input 分布确认无退化 prompt
- 若 v2 clean subset 仍 negative → 审查强模型实验设计（D018 Stage 2），确认 kill criteria 是否已操作化（D019）
- 若 Agent 提交论文章节审查 → 按 §5 写作对抗审查流程，先查 red-section skill 合规

### 5. 🎯 战略上下文
**决策链**：D013/D014（trace 收集 bug）→ D015（v2 重跑）→ D016（segment cap 问题，未修）→ D017（暂缓 MVP 判定）→ D018（两阶段消歧）→ D021（三重 confound，v1 无效）

**核心结论现状**：Phase 3 的 "negative conclusion" 既不能被证实也不能被证伪——实验数据被三重 confound 污染。真正的 MVP 判定要等 v2。

**最容易判断错的事**：
1. **不要信 Phase 3 v1 的任何数字**（h2h 5-23-5、judge mean、line_overlap）——约 14/33 实例 LLM 收到的是错误代码，18/33 实例 structural_filtered≡no_trace
2. **subset_b h2h 的 15 个 tie 不是 "trace 没帮助"**——是 3/4 条件 prompt 完全相同导致的伪 tie
3. **httpie_2 no_trace judge=4 是假阳性**——修的是 args.data isinstance 检查（错误的 bug），不是 max_redirects（正确的 bug）
4. **55% 实例 structural_keep=0 可能不全是 scoring 问题**——D016 的 MAX_SEGMENTS=20 cap 截断了大 trace 的 segment 数量，可能导致本应 keep 的 segment 被丢弃。如果 v2 不修 cap，clean subset 仍然很小
5. **DDL 5/25 剩 10 天**，时间可行但无余量。关键路径是 pipeline fix 速度
