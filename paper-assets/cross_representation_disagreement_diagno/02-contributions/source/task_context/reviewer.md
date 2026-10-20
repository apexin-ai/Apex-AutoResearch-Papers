---
loop: 4
reason: max_messages
updated: '2026-05-15T03:26:53+00:00'
---

### 1. 🔴 硬约束 / 红线
- 本项目只能用 autodl-rtx6000pro 的 cuda:0（单卡服务器，无越界风险但需确认 vLLM + pipeline 共享同一卡）
- repair_only.py 正在运行（PID 66854），**不要 kill 或重启 vLLM**，否则 repair API 调用全部失败
- JSONL 主文件已替换为去重版本（204 行），原始 211 行备份在 `mvp_v4_full_original_211.jsonl`，**不要用 211 行版本做任何评估**
- C4 MVP gate 阈值 >5pp 不可降级（D002 决策，Reviewer 已明确反对降级，见我发给 Director 的 C4 风险预案分析）

### 2. 🖥️ 基础设施快照
- 服务器：autodl-rtx6000pro，工作目录 `/root/autodl-tmp/crdd`
- Python：`/root/miniconda3/bin/python`（conda base 环境，不是 venv）
- 激活：`source /root/miniconda3/etc/profile.d/conda.sh && conda activate base`
- vLLM：PID 19633，Qwen3-32B-AWQ (awq_marlin)，port 8000，`--max-model-len 16384 --gpu-memory-utilization 0.90`
- 模型路径：`/root/autodl-tmp/models/Qwen3-32B-AWQ`
- 数据：FOLIO validation set（204 样本）
- 活跃进程：repair_only.py PID 66854（86 targets，~2/86 at 08:51 UTC，ETA ~170 min → 完成约 11:40 UTC）
- 输出：`results/mvp_v4_repair_fixed.json`
- 日志：`/tmp/repair_only_deduped.log`

### 3. 📊 当前状态
**我刚完成的审查**：
- mvp_pipeline_004 全量 204 完成（EXIT_CODE=0），去重后跑了 evaluate_mvp.py
- 去重后 All-mode 5/5 PASS，C4 +6.2pp（margin 仅 1.2pp）
- Excl-unknown 4/5（C4 -1.7pp FAIL）
- repair_only.py 已启动，用修复后的 repair.py（动态 repr_type）重跑全部 repair+eval

**Registry 状态**：
- mvp_pipeline_004: ANALYZING，metrics 含去重后 204 数据，conclusion="success"（我已 warning 过 conclusion 过早设定）
- repair_only_status: "running (PID 66854, 86 targets, ETA ~170min)"

**等待中**：repair_only.py 完成后需要：用 `mvp_v4_repair_fixed.json` 运行 evaluate_mvp.py → 最终 MVP gate 判定

### 4. 📋 待办
- repair_only.py 完成（PID 66854 退出）→ 检查 `results/mvp_v4_repair_fixed.json` 存在且完整 → 对其运行 evaluate_mvp.py → **这是 MVP gate 最终权威判定**
- 最终评估 C4 all-mode >5pp → MVP PASS confirmed，关注 excl-unknown C4 是否也翻转为 PASS
- 最终评估 C4 all-mode ≤5pp → 不降标准，分析 FOL targeted repair 改善幅度是否符合预期（修复前 FOL targeted ~50%，修复后应显著提升）。如果修复后仍 FAIL → 方法本身问题，需要 Director 决策
- Registry/ROADMAP 更新：repair_only 结果出来后，推动 Agent 将 status→DONE，更新 report.md 和 ROADMAP

### 5. 🎯 战略上下文
- 核心决策链：D001(MVP方案) → D002(Reviewer加C4/C5) → D005(v1 FAIL,prompt问题) → D006(v2改善) → D007(撤回closed-world) → D008(repair.py bug确认)
- **关键判断**：当前 C4 +6.2pp 是在 **buggy repair 数据**上算的（samples 0-148 用旧 repair.py，148-204 用新的）。repair_only.py 用修复后的 prompt 重跑全部 repair，C4 理论上应改善（FOL targeted 从~50%提升）。**不要在 repair_only 完成前做 MVP 最终判定**
- **易错点 1**：JSONL 有多个版本（211行原始 / 204行去重 / repair_fixed），确保用对文件
- **易错点 2**：evaluate_mvp.py 输出区分 all-mode 和 excl-unknown 两组指标，MVP gate 以 all-mode 为准，但论文 story 两组都要能讲通
- **易错点 3**：DISAGREE 不对称性 9:1（FOL 几乎总是对的，Code 几乎总是错的），repair 主要修 Code side。repair.py bug 影响的是 FOL side repair（少数但拖低了总体 targeted 率）
