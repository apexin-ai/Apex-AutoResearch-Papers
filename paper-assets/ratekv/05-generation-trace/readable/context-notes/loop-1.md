# director / loop_1.md

**When Does Non-Uniform KV Cache Quantization Help? Cardinality Constraints and a Heterogeneity Diagnostic** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/director/loop_1.md`
- **Structured JSON:** [`32f1ad42ff352adf7c6a.json`](../../sessions/32/32f1ad42ff352adf7c6a.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 1
reason: max_messages
updated: '2026-05-13T23:52:00+00:00'
---

### 1. 🔴 硬约束 / 红线
- GPU 白名单：westd-37397 的 cuda:0 和 cuda:1，不可用其他服务器/GPU
- Eviction 路径已全面 falsify（D005-D007），不要再尝试任何 eviction 相关实验
- AutoDL tmux 环境必须显式设 env vars：`source /etc/network_turbo && export HF_ENDPOINT=https://hf-mirror.com && export HF_HOME=/root/autodl-tmp/.hf_cache && export REQUESTS_CA_BUNDLE=/etc/ssl/certs/ca-certificates.crt && export SSL_CERT_FILE=/etc/ssl/certs/ca-certificates.crt`
- 提交实验前必须跑前台 smoke test，连续 6 次崩溃的教训

### 2. 🖥️ 基础设施快照
- 服务器：westd-37397 (connect.westd.seetacloud.com:37397, root), 2× RTX PRO 6000 96GB
- 工作目录：/root/ratekv/（6 个代码文件：profiler.py, ppl_profiler.py, solver.py, eval_ppl.py, run_mvp.py, visualize.py + cliff_test.py, run_ppl_mvp.py）
- Python：/root/miniconda3/bin/python（conda base 环境，不是 venv）
- 模型：7B → /root/autodl-tmp/.hf_cache/Qwen/Qwen2___5-7B/，1.5B → /root/autodl-tmp/models/Qwen2.5-1.5B
- Calibration：/root/ratekv/calibration_data.json（25 条拼接 WikiText-103，≥512 tokens/条，注意不是 C4）
- HF cache：/root/autodl-tmp/.hf_cache/，WikiText-2 eval 已缓存
- 活跃进程：Worker `exp-b-full-bitwidth-mckp` 正在写代码（turn 3），无 GPU 进程运行

### 3. 📊 当前状态
刚完成 MVP 全流程验证（MSE metric → PPL metric → targeted hybrid），全部 negative。已 pivot 到 quant-only per-head bit-width allocation。

**Worker B (`exp-b-full-bitwidth-mckp`)** 正在实现 go/no-go 关键实验：PPL-guided quant-only MCKP with {2,4,8,16}-bit per head, budget=4x。计划：1.5B smoke test (cuda:1) → 7B 完整实验 (cuda:0 + cuda:1 并行)。

Registry: mvp_001-004 全 DONE(negative)，sanity_001-004 全 DONE，p0_1/p0_2 DONE，exp_a DONE(negative)。无 RUNNING 实验。

等待：Worker B 完成代码 + smoke test 后提交实验 → cron 回调。

### 4. 📋 待办
- Worker B 代码完成 + smoke test 通过 → 提交 7B 实验到 cuda:0（两卡并行跑 Exp B）
- Exp B 7B 结果出来 → 用 v3 gate 判定：quant-only MCKP PPL < uniform 4-bit (15.45) by ≥0.5 → PASS，pivot 论文为 "rate-distortion optimal per-head bit-width allocation"；≈ uniform → FAIL → 向用户建议 archive
- 如果 PASS → 进入 post-MVP kickoff 流程：写 paper_framing.md → experiment_plan.yaml → dream_simulate

### 5. 🎯 战略上下文
**决策链**：D001(MVP 设计) → D002(gate v2) → D003(Llama→Qwen) → D004(MSE falsified) → D005(MVP 实质 FAIL) → D006(PPL metric 也失败，eviction compounding) → D007(pivot 到 quant-only MCKP with full bit-width)

**核心发现**：
- Crossover（eviction vs quantization）确实存在，但 eviction 的 compounding effect 违反 per-head 独立性假设，使 joint allocation 无法 work
- Attention MSE 作为 distortion metric 随模型规模指数级恶化（1.5B 1.2× vs 7B 70× 偏离）
- Per-head quantization sensitivity 高度不均匀（Layer 0 对 2-bit +297%，大多数 head <1%）——这是 Exp B 可能成功的理论基础

**最易判断错的事**：
- 不要被 "quant-only MCKP = uniform" 的旧结论误导——那是 fast mode artifact（只有一个 4-bit 选项），不是真实证据
- PPL profiling 分辨率问题（100/112 heads 显示相同 delta 0.1328）——Exp B 需要足够多的 eval tokens
- Calibration 数据实际是 WikiText（不是 C4），文件名 c4_calibration.json 误导


---
