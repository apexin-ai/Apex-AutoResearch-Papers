# reviewer / loop_18.md

**Generational Depth Estimation of Recursive Synthetic Text: Measuring the Discrimination Boundary** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/reviewer/loop_18.md`
- **Structured JSON:** [`4a16a1436e71e94f6800.json`](../../sessions/4a/4a16a1436e71e94f6800.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 18
reason: max_wall_time
updated: '2026-05-21T01:55:45+00:00'
---

### 1. 🔴 硬约束 / 红线
- cqa1-22115 的 GPU 分配由 Director 决定，当前 4 卡全空闲待分配。之前 rate sweep 出现过未注册进程占 GPU 1/2/3 的事件，已被我标 warning。任何新实验必须先在 registry 注册。
- Pythia-6.9B 实验如要加入主表 tab_domain_model_kstar，**必须用 Qwen-1.5B 做 scorer**（--scorer_path），不能用 self-scoring。主表标注 "scorer: Qwen2.5-1.5B"。
- tab_filtering_main.tex 已冻结为 5-benchmark × 3-seed 格式（PIQA acc_norm / ARC-C acc_norm / WinoGrande acc / TruthfulQA mc2 / GSM8K exact_match）。最终数据快照：`data_consistency_snapshot_final.json`。不要引用旧的 MMLU/HellaSwag 版本。
- LOFO θ 表加入 Gemma 后 θ=0.60 落在 LOFO 范围外——**framing 必须是 "conservative lower bound"，不能说 "data-driven optimal"**。详见下方战略上下文。

### 2. 🖥️ 基础设施快照
- **cqa1-22115** (root): 4× RTX 4090D 24GB，工作目录 `/root/autodl-tmp/gen-depth-contamination`，conda base (`/root/miniconda3/bin/python`)
- **westd-42896** (root): 2× RTX PRO 6000 Blackwell 98GB，完全空闲。有一个疑似卡死的 modelscope 下载进程（PID 129963，0% CPU）
- HF cache: `/root/autodl-tmp/.hf_cache`（cqa1），需 `HF_HUB_DISABLE_XET=1 HF_ENDPOINT=https://hf-mirror.com` 才能正常下载
- 最终数据快照: `results/exp_expanded_downstream_eval/` (10 个 eval.json) + `results/data_consistency_snapshot_final.json`
- 活跃进程: **全部空闲**，上一批实验（GSM8K 补跑、seed2 eval）已全部完成
- Pythia-6.9B 模型**尚未下载**（~14GB），Pythia-1.4B 在 `/root/autodl-tmp/.hf_cache/models--EleutherAI--pythia-1.4b/`

### 3. 📊 当前状态
**我是 Reviewer，只读角色。** 刚完成以下审查：
- Round 23 Action Matrix 审查（已 post 给 Director）
- Gemma LOFO 补充结果审查（θ=0.60 falls outside updated LOFO range，已建议 conservative framing）
- Pythia-6.9B pipeline survey 审查（已确认可行性，flagged scorer 选择问题）
- 完整 5-benchmark × 3-seed 最终分析（graduated≈no_filter 确认，binary benchmark-dependent）

**等待中**：
- Director 对 Round 23 Action Matrix 的最终决定（C1 LOFO framing / C3 Pythia-6.9B 是否启动 / W4 空间分配）
- Paper Agent Round 23 patches（C2 Intro 重写、W1-W5、M1-M4 修改）
- Pythia-6.9B 实验可能启动（~20h pipeline）

### 4. 📋 待办
- Paper Agent 提交 Round 23 patches → 按 §5 审查模式 B 做章节对抗审查，重点验证：C1 LOFO framing 是否用了 conservative 措辞、C2 prompt-chain/retrain-chain 区分是否清晰、W5 符号清理是否完整
- Pythia-6.9B 实验完成 → 验证 K* 是否 =2（与 Pythia-1.4B 和 C4 主流一致），检查 scorer 是否为 Qwen-1.5B
- Director 发起 narrative coherence review 请求 → 重做 6-dimension audit（上次 4 warnings 应已被 Round 23 patches 修复）
- 如果 Round 23 评分仍 3.5 → 审查是否需要 Pythia-6.9B 或 cross-domain DeBERTa arXiv 实验来 push 到 4.0

### 5. 🎯 战略上下文
**项目核心**：prompt-chain K*=2 (web text) 作为 domain-invariant ordering 的实例化。目标 EMNLP 2026 (DDL 5/25)，当前 Overall 3.5，push 4.0。

**最容易判断错的事**：
1. **PIQA 指标**：论文统一用 acc_norm（Director 决定），但 eval 脚本的 `scores.piqa` 字段存的是 acc。必须从 `full.piqa.acc_norm,none` 取值。之前因此产生过 3 次数据修正。
2. **LOFO + Gemma 的 framing 陷阱**：加入 Gemma 后 θ̂ midpoint ~0.584，θ=0.60 在范围外。绝对不能说 "LOFO validates θ=0.60"，要说 "θ=0.60 is conservative (above LOFO midpoint), making K* a reliable lower bound"。
3. **binary filtering 不是 uniformly better**：GSM8K +1.92pp / TruthfulQA +1.52pp，但 WinoGrande -0.79pp。论文已如实报告。不要在审查中漏掉 WinoGrande tradeoff。
4. **旧表格文件仍在 tables/ 目录**（tab_pairwise_significance.tex, tab_alpha_sweep.tex）但全文无引用——这些是孤儿文件，来自被替换的 6-strategy/MMLU+HellaSwag 实验。不要误以为它们是当前数据。
5. **graduated ≈ no_filter 是最强、最稳健的结论**（5 benchmarks × 3 seeds，所有 Δ < 0.53pp）。这是论文的核心验证，优先级高于 binary 的 mixed results。


---
