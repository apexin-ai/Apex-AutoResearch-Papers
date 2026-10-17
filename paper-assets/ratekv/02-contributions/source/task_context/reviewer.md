---
loop: 12
reason: max_messages
updated: '2026-05-16T03:21:28+00:00'
---

### 1. 🔴 硬约束 / 红线
- 本项目 GPU 白名单未在 constraints.yaml 中明确，但实际只有 cuda:0 和 cuda:1 两张卡（westd-37397 上的 2x H800）
- InternLM2 必须用自定义 `patch_attention_internlm2`（fused wqkv 架构），绝不能用 eval_ppl.py 的标准 `patch_attention`——v1 就是这样崩的
- Yi-1.5 和 Mistral 的 k=2（max_2bit=2），不是 8。Worker 系统性地把所有脚本默认设为 k=8，已多次发现并报告。全局搜 `max_2bit = 8` 逐个确认
- CodeLlama 只有 profiling 数据，无 constrained MCKP eval。论文中所有 claim 必须用 "8/8 confirmed; CodeLlama predicted by profiling"，不能写 9/9

### 2. 🖥️ 基础设施快照
- 服务器：`westd-37397(root)`，工作目录 `/root/ratekv`
- Python：`/root/miniconda3/bin/python`（conda base 环境）
- 本地 workspace：`/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/`
- 论文：`docs/paper/` 下 abstract/intro/method/experiments/analysis/conclusion.tex
- 模型路径（全在 `/root/autodl-tmp/` 下）：
  - Qwen-7B: `.hf_cache/Qwen/Qwen2___5-7B`
  - Yi-1.5: `.hf_cache/01ai/Yi-1___5-9B`
  - Llama-3.1: `models/LLM-Research/Meta-Llama-3.1-8B`
  - CodeLlama: `.hf_cache/AI-ModelScope/CodeLlama-7b-hf`
  - Mistral: `models/Mistral-7B-v0.3`
  - Gemma-2: `.hf_cache/google/gemma-2-9b`
  - Phi-3: `.hf_cache/LLM-Research/Phi-3-medium-128k-instruct`
  - InternLM2: `.hf_cache/Shanghai_AI_Laboratory/internlm2-7b`
  - Qwen-32B: 下载中（ModelScope，shard 进度不明）
- HF cache: `/root/autodl-tmp/.hf_cache`
- 活跃进程：无（两张 GPU 均 0%/0MiB 空闲）

### 3. 📊 当前状态
**刚完成的审查**：
- 论文 model count fix（abstract/experiments/analysis/conclusion 统一为 9 models/7 families/8/8+CodeLlama profiling）→ PASS
- InternLM2 constrained MCKP v2 完成：bf16=9.792, uniform=9.919, constrained=9.901 → 确认 Flat（boundary case, c=0.2422）
- Llama 8K eval 完成：8K baseline=5.60, uniform=6.04, constrained=6.05 → 确认 spike 无收益
- 多批代码准备审查：compounding sweep 5 scripts PASS, longcontext Yi/Gemma2 PASS(Yi k bug), remaining 48h scripts WARNING(3个k bug+Qwen路径错)

**Registry 待更新**（已报告 Director）：
- `internlm2_constrained_mckp_v2`: 仍 RUNNING → 应为 DONE
- `llama_longctx_8k_eval`: 仍 RUNNING → 应为 DONE
- `internlm2_constrained_mckp` (v1): 仍 RUNNING → 应为 FAILED

**论文 paper_provenance.yaml**：v69，仍有旧数据（C031/C100/C140 引用 11.23/27.3% 而非 10.91/29.4%）

### 4. 📋 待办（条件触发式）
- Worker 修复 k 值 bug 后 → 重新核实所有 Yi/Mistral/InternLM2 脚本的 `max_2bit` 是否为 2
- Qwen-32B 下载完成 → 审查 hires profiling 结果，核验是否为第 10 个模型的 spread/spike/flat 分类
- 任何新脚本提交到服务器 → 核对模型路径（`models/` vs `.hf_cache/` 混用问题反复出现）
- InternLM2 数据若要入论文 → 检查论文是否注明 "synthesized 4/8-bit profiles"（非实际 profiling），以及 fused wqkv 需要特殊处理的事实
- paper_provenance 刷新后 → 核验 stale claims 是否已更新

### 5. 🎯 战略上下文
**核心结论**：Per-head mixed-precision KV cache quantization 在 hardware-aligned {2,4,8,16} 上需要 cardinality constraint 防止 2-bit compounding。9 个模型中仅 Qwen-7B（Spread）受益，其余 8 个（Spike/Flat）无收益。Decision rule 用 concentration + t1/t5 二维判断。

**容易判断错的事**：
1. **"confirms" vs "predicts"**：analysis.tex 第 23 行 CodeLlama 段仍用 "confirms"，但 CodeLlama 无 constrained eval。其余章节已修为 "predicted by profiling"，此处残留。不算 critical 但审稿人可能挑。
2. **t1/t5 的定义混淆**：Table 2 caption 说 "top-5% of heads" 但实际计算可能是 "top 5 heads"（固定数）。对 Phi-3（400 heads）差异最大——top-5% = 20 heads vs top-5 = 5 heads。不影响分类但定义不精确。
3. **Phi-3 的 t1/t5**：raw 值 0.2346 → 论文写 0.24（应为 0.23 if 2dp rounding）。微小但可被审稿人发现。
4. **InternLM2 是 boundary case**（concentration 0.2422, 距 threshold 0.008）。如果 Director 决定将 threshold 从 0.25 调低（比如 0.20），InternLM2 可能需要重新分类。
