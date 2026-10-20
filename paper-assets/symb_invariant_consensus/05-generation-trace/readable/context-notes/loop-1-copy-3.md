# reviewer / loop_1.md

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/reviewer/loop_1.md`
- **Structured JSON:** [`f96d9c00249756ad1823.json`](../../sessions/f9/f96d9c00249756ad1823.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 1
reason: max_wall_time
updated: '2026-05-15T13:07:01+00:00'
---

### 1. 🔴 硬约束 / 红线
- 本项目只有 1 张 GPU（cuda:0），vLLM 独占。不存在多卡分配问题，但任何新进程必须走 vLLM API（localhost:8000），不能直接 load model 抢显存
- 模型固定 QwQ-32B（D003），不可替换为 Qwen3-32B-AWQ 或其他模型。换模型需要新 Decision
- AIME trace 生成必须 max_tokens≥10240，4096 会截断无 \boxed（diag_test 已证实）
- extraction 用 VLLMBackend max_tokens=512（不是 4096），这是修复后的正确值

### 2. 🖥️ 基础设施快照
- 服务器：westd-32608(root)，工作目录 /root/symb_invariant_consensus
- Python：/root/miniconda3/bin/python（conda base 环境，不是 venv）
- vLLM：PID 102693，tmux 外 nohup 启动，--max-model-len 16384 --gpu-memory-utilization 0.90 --port 8000
- 模型：/root/autodl-tmp/models/QwQ-32B/Qwen/QwQ-32B（FP16，~64GB）
- 数据：data/math500_subset.json（50题，已过滤图片题）、data/aime2024_subset.json（30题）、data/proofwriter_subset.json（10题）
- 活跃进程：sica_aime30_t07（PID 119348，tmux session=sica_aime30_t07，cuda:0），刚启动 problem 1/30
- 结果目录：/root/symb_invariant_consensus/results/（当前仅有 diversity_diagnosis.json + smoke_test_5q.json）

### 3. 📊 当前状态
我刚审查完 worker_code_prep-math50-rerun（添加 CLI 参数 + AIME smoke test 验证通过）。

Registry RUNNING：
- `sica_aime30_t07` — AIME 30 题 K=12 T=0.7，刚启动 ~3min，ETA ~3.9h。Log: /tmp/sica_aime30_t07.log + ~/runs/symb_invariant_consensus/sica_aime30_t07.log

Registry DONE（关键）：
- `sica_temp_diversity` — conclusion=negative，零答案多样性（定论）
- `mvp_math50_t07` — conclusion=killed（bug 导致 25h+ 不可接受，D006 授权 kill）
- `sica_smoke_5q` — SICA=SC=80%，0pp 差异

等待中：AIME-30 完成后需要审查结果，判定是否有 SICA 信号。MATH-50 rerun 排在 AIME 之后（D006）。

### 4. 📋 待办
- AIME-30 problem 进度推进（log 出现新的 `--- [N/30]`）→ 抽查 extraction 质量、是否有 answer divergence、JSON parse 失败率
- AIME-30 完成 → 按 D003 三档标准的 AIME 版本评估：(1) extraction rate, (2) 矛盾题数, (3) SICA vs SC accuracy。特别关注 QwQ-32B 答错的 ~6 题是否出现 trace 分歧
- AIME 有信号（分歧 + SICA>SC）→ 审查 Agent 重启 MATH-50 MVP（用修复后代码）
- AIME 无信号（又是 unanimous）→ 预期 Director 做 FAIL 路径决策，可能涉及换弱模型或放弃 EMNLP
- 任何新实验启动 → 核查 registry spec 完整性（seed 必须非 null）、GPU 白名单

### 5. 🎯 战略上下文
决策链：D001(MVP 方案) → D002(拒绝 CRD 回归 SICA) → D003(三档判定标准) → D004(MVP 继续+AIME 排后) → D005(双管齐下) → D006(kill buggy MVP, AIME 优先)

**核心风险：QwQ-32B 太强导致 SICA 无用武之地。** Smoke test（MATH）和 diversity diagnostic 均显示 12/12 unanimous，AIME smoke_test2 第 1 题也是 12/12 unanimous correct。SICA 的价值取决于 trace 间存在分歧——强推理模型的确定性推理压制了采样随机性。唯一希望是 AIME 中 QwQ-32B 答错的题（~6/30）可能出现不同错误答案。

**易错点：**
- 不要因为 AIME 第 1 题 unanimous 就提前判 FAIL——需要看 QwQ 答错的题
- smoke_test2 显示 470s/题，30 题 ~3.9h，不是之前估的 2h（因为 AIME trace 很长 12K-25K chars）
- extraction max_tokens=512 是修复后的正确值，不要改回 4096
- `run_full_mvp.py` 的 extraction 温度是 0.1（line 99），trace 生成温度是 0.7——两个不同值，不要搞混
- May 19 UTC 是 EMNLP checkpoint 硬截止：MVP 未 pass → 放弃 EMNLP，切 AAAI 2027


---
