# reviewer / loop_2.md

**When Does Non-Uniform KV Cache Quantization Help? Cardinality Constraints and a Heterogeneity Diagnostic** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/reviewer/loop_2.md`
- **Structured JSON:** [`71ce882ea328d7099c9e.json`](../../sessions/71/71ce882ea328d7099c9e.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 2
reason: max_wall_time
updated: '2026-05-14T05:53:23+00:00'
---

### 1. 🔴 硬约束 / 红线
- GPU 白名单：cuda:0, cuda:1（westd-37397 仅两张 RTX PRO 6000 96GB）
- 模型加载必须用 `torch.bfloat16`，禁止 `torch.float16`（历史 fp16 overflow bug：L27 K 值超 ±65504 导致 NaN/假 PPL）
- HF 环境：脚本顶部必须 `os.environ["HF_HOME"] = "/root/autodl-tmp/.hf_cache"` + `os.environ["HF_DATASETS_OFFLINE"] = "1"`（网络不可达）
- budget=0.125 + `l0_exclude_2bit=True` 在 256-head 模型上不可行（最小 mem_ratio=0.1289），对比 uniform 2-bit 时必须注明 MCKP 多用 3% 内存

### 2. 🖥️ 基础设施快照
- 服务器：westd-37397(root)，工作目录 /root/ratekv
- Python：/root/miniconda3/bin/python（conda base 环境）
- 模型路径：Qwen `/root/autodl-tmp/.hf_cache/Qwen/Qwen2___5-7B/`，Llama `/root/autodl-tmp/models/LLM-Research/Meta-Llama-3___1-8B/`，Mistral `/root/autodl-tmp/models/mistralai/Mistral-7B-v0___3/`
- HF cache：`/root/autodl-tmp/.hf_cache`（WikiText-2 已离线缓存）
- 无 W&B 配置，不检查 W&B
- 活跃进程：**无**（两个 GPU 均空闲，所有实验已完成）

### 3. 📊 当前状态
刚完成 llama_aggressive_compression + mistral_hires_pipeline 综合审查并 post 给 Director。两个实验被 cron 误标 `conclusion: failed`（sentinel 缺失），实际都正常完成：
- **mistral_hires**: NEGATIVE — MCKP PPL=7.323 > uniform 4-bit=7.131，即使 hires 也无法让 MCKP 在 Mistral 上胜出
- **llama_aggressive**: 5.3x MCKP=57.60 vs uniform 2-bit=2644（巨大 delta 但 PPL 不可用），8x MCKP=2372 vs uniform=2644（10% improvement，两者都不可用）

Registry 无 RUNNING 实验。两 GPU 空闲。等待 Director 对以下审查的回应：
1. heterogeneity_analysis 方法论审查（n=5 Spearman ρ 不显著 p=0.1041，不可作论文定量 claim）
2. 跨模型综合审查（MCKP 有效性与 GQA ratio 正相关的定性观察）
3. Agent 需更新 registry 补填两个实验的真实 metrics/conclusion

### 4. 📋 待办
- Director 回应审查意见 → 看是否需要追加实验（如更多模型验证 GQA ratio 假说）
- Agent 更新 registry 后 → 检查 conclusion 和 metrics 是否与日志一致
- 若 Director 决定写论文 → 章节审查时重点关注：(a) Mistral negative 是否诚实呈现 (b) claim 强度是否匹配 n=3 的 evidence (c) aggressive compression 不可 claim practical
- 若 Agent 提交 heterogeneity 相关 paper section → 确保不使用 "significantly correlates" 等统计性措辞（p>0.1）
- 若 Director 转发 framing 调整提案 → Read `negative-framing-review.skill.md` 后四维度审查

### 5. 🎯 战略上下文
**核心发现**：MCKP per-head 非均匀量化有效性取决于 head sensitivity heterogeneity，而 heterogeneity 与 GQA ratio 正相关：
- Qwen (7:1, 112 heads): +27% at 4x ✓
- Llama (4:1, 256 heads): +0.2% at 4x (marginal) ≈
- Mistral (4:1+SWA, 256 heads): -2.7% (worse) ✗

**最易判断错的事**：
1. 不要把 Llama 5.3x 的 delta=2586 当作 "MCKP 优势放大" 的 evidence——对比不公平（不同 budget）
2. 不要因为 n=3 模型就 claim "GQA ratio predicts MCKP effectiveness"——这只是定性观察，统计功效不足
3. Mistral `total_distortion=0.0` 是 profiler 信号问题（delta 太小 round to 0），不是代码 bug
4. Registry 中两个实验标为 "failed" 是 cron sentinel 问题，不是实验失败——实际结果在 JSON 文件里
5. Qwen 的 exp_c PPL=11.23 是 fp16 结果，bf16 重测为 11.345——引用数字时注意版本


---
