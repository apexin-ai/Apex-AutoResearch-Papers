# reviewer / loop_5.md

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/reviewer/loop_5.md`
- **Structured JSON:** [`56eab1ee8e790648856f.json`](../../sessions/56/56eab1ee8e790648856f.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 5
reason: max_wall_time
updated: '2026-05-16T18:43:20+00:00'
---

### 1. 🔴 硬约束 / 红线
- 本项目只有 1 张 GPU：cuda:0（RTX PRO 6000 Blackwell 98GB）。`gpu_ids=[0]`，无其他卡可用
- vLLM 服务 (PID 174298) 常驻 GPU 0，实验通过 localhost:8000 API 调用，不要 kill vLLM 除非换模型
- Mistral-7B 模型截断 (81%, 11.78/14.50 GB)——不要尝试用它跑推理，会 load 失败
- exp-001 的 `raw_constraints` 字段为空（pipeline.py 在进程启动后才修改，Python 不热加载）——不要基于 exp-001 结果文件中的 raw_constraints 做分析

### 2. 🖥️ 基础设施快照
- 服务器：`westd-32608`（root），工作目录 `/root/symb_invariant_consensus`
- Python：`/root/miniconda3/bin/python`（conda base 环境）
- vLLM 服务：PID 174298，模型 `/root/autodl-tmp/models/Qwen2.5-14B-Instruct`，port 8000
- Llama-8B：`/root/autodl-tmp/models/Llama-3.1-8B-Instruct/LLM-Research/Meta-Llama-3___1-8B-Instruct/` — 完整可用
- Mistral-7B：`/root/autodl-tmp/models/Mistral-7B-Instruct-v0.3/mistralai/Mistral-7B-Instruct-v0___3/` — 截断，需重下
- 数据：`/root/symb_invariant_consensus/data/`（proofwriter_full 600, folio_full 204, strategyqa_200, arc_challenge_200, math_l45_100, gsm8k_200）
- 活跃进程：exp-001 PID 181491（elapsed 13h+，762/804，ETA ~40min from last check）

### 3. 📊 当前状态
- **刚完成**：ROADMAP D025 pivot 审查（已 post 给 Director，severity: warning）
- **exp-001 (sica_expanded_14b)**：RUNNING，762/804 (94.8%)，SICA 76.51% vs SC 76.25% Δ=+0.26pp，预计几十分钟内完成
- **Registry RUNNING**: 仅 `sica_expanded_14b`
- **Registry QUEUED**: `sica_k_sensitivity_14b`
- **等待中**：exp-001 完成后的 worker_done 回调 → 需审查 per-domain breakdown（特别是 FOLIO 子集）
- **Director 未决策**：我报告了 paper_framing.md 内部矛盾 + Mistral blocker deadline 建议，待 Director 响应

### 4. 📋 待办
- exp-001 完成 worker_done → 审查最终结果，重点：(1) FOLIO 204 题单域 gap 是否 >3pp 且 p<0.1（存活则保留 sub-finding）(2) per-domain C0 分布 (3) tiebreak win rate 实际值
- exp-013 constraint ablation 启动 → 验证数据源：如果用 exp-001 的 raw_constraints 则为空（需用 exp-002 或重跑 pipeline 单独提取）→ 标 WARNING 如果 Agent 尝试用空 constraints
- Mistral-7B 重新下载 worker_done → 验证文件完整性：3 shards 总和 ≥ 14.50 GB
- 任何新模型加载到 vLLM → 验证 `nvidia-smi` GPU 利用 + 确认 CUDA_VISIBLE_DEVICES=0
- Paper Agent 收到写作任务 → 确认 paper_framing.md headline result 已更新（旧的 "+6.7pp on FOLIO" 是噪声数据）

### 5. 🎯 战略上下文
- **核心结论**：SICA ≈ SC。D012 的 +3.3pp 是 N=60 噪声，exp-001 (N=762) 确认 gap ≈ 0。项目已 pivot 到 Analysis Paper "The Capability Trap"
- **决策链**：D016(QwQ FAIL→pivot 14B) → D017/D018(D012 pass but p=0.23) → D021(scope 扩展) → D023(contingency plan) → D025(activate contingency)
- **下一个"我"最容易判断错的事**：
  1. 不要被 D012 metrics (sica_accuracy=0.733, +3.3pp) 迷惑——那是已被推翻的小样本结果，registry conclusion 仍写 "success" 但这是历史遗留
  2. FOLIO 子 claim 可能存活——exp-001 全量 FOLIO (204题) 结果出来前不要判死，D012 中 FOLIO 30 题是 80% vs 73.3%
  3. Claim 2 "Operating Regime is Vacuous" 是极强断言——任意一个 model×domain cell 显著正即推翻，审查时警惕 Agent 的 cherry-pick 或 underreport
  4. prepare_strategyqa.py 的 `/tmp/prep_strategyqa.log` 显示失败但文件实际已生成（script 有 fallback sources）——不要误报


---
