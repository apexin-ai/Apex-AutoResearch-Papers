# knowledge update memory scaling stats

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 7
- **Recorded user turns:** 0
- **Tool calls:** 3
- **Original source:** `logs/chats/worker_knowledge_update_memory_scaling_stats_20260519T001114.jsonl`
- **Structured JSON:** [`dde901fcb10e949f043f.json`](../../sessions/dd/dde901fcb10e949f043f.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

7 recorded events

### Tool call

_source line 1 · 2026-05-19T00:11:58.651599+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__save_project_file",
  "max_results": "2"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_knowledge_update_memory_scaling_stats_20260519T001114",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__save_project_file",
    "max_results": "2"
  }
}
```

</details>

---

### Tool result

_source line 2 · 2026-05-19T00:11:58.652020+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_knowledge_update_memory_scaling_stats_20260519T001114",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-19T00:11:58.652225+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "faith-evidence-ie",
  "file": "memory.md",
  "max_chars": "0"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_knowledge_update_memory_scaling_stats_20260519T001114",
  "tool": "mcp__agent-ml-research__read_project_file",
  "tool_args": {
    "project": "faith-evidence-ie",
    "file": "memory.md",
    "max_chars": "0"
  }
}
```

</details>

---

### Tool result

_source line 4 · 2026-05-19T00:11:58.653109+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/memory.md\", \"content\": \"# D112 Pipeline Plan: RSFT from SFT s44\\n\\n## 概述\\n验证 RSFT 在最强 SFT seed（s44, ign_f1=0.4734）上的效果。之前所有 4B RSFT 都基于 SFT s42（最弱 seed, ign_f1≈0.40）。\\n\\n## 脚本位置\\n`/root/autodl-tmp/scripts/d112/` 下 4 个脚本\\n\\n## Pipeline 步骤\\n\\n### Step 1: 候选生成\\n**脚本**: `step1_generate_candidates.sh`\\n**命令**:\\n```bash\\n# 4-GPU 并行（推荐，总计约 3-4h）\\nGPU=0 SHARD=0 bash step1_generate_candidates.sh &\\nGPU=1 SHARD=1 bash step1_generate_candidates.sh &\\nGPU=2 SHARD=2 bash step1_generate_candidates.sh &\\nGPU=3 SHARD=3 bash step1_generate_candidates.sh &\\nwait\\n\\n# 或单 GPU（约 12-16h）\\nGPU=0 bash step1_generate_candidates.sh\\n```\\n**参数**: N=8, temperature=0.7, top_p=0.95, batch_size=1, max_new_tokens=1024, seed=42\\n**输入**: base=Qwen3-4B, adapter=sft_output_seed44, data=DocRED train_annotated (3053 docs)\\n**输出**: `/root/autodl-tmp/rsft_generations_4b_sft_s44/`\\n**预估时间**: 4-GPU 并行 ~3-4h, 单 GPU ~12-16h\\n**GPU**: 每个 shard 1 GPU（4 GPU 最优）\\n\\n### Step 2: CED 打分 + k=1 筛选\\n**脚本**: `step2_ced_score.sh`\\n**命令**:\\n```bash\\nGPU=0 bash step2_ced_score.sh\\n```\\n**参数**: CED scoring (format_w=0.2, f1_w=0.4, ced_w=0.4), selection_strategy=top_k, k=1, tau=0.5\\n**NLI 模型**: cross-encoder/nli-deberta-v3-base（HF cache 已有）\\n**输入**: step1 输出目录（自动合并 shard）\\n**输出**: `/root/autodl-tmp/rsft_scored_4b_sft_s44/`\\n**预估时间**: ~30-60 min\\n**GPU**: 1 GPU（NLI 模型很小）\\n**预期产出**: ~2700-2800 条训练样本（k=1, 每 doc 最多 1 条）\\n\\n### Step 3: RSFT 训练\\n**脚本**: `step3_k1_filter_and_train.sh`\\n**命令**:\\n```bash\\nGPU=0 bash step3_k1_filter_and_train.sh\\n```\\n**参数**: lr=2e-5, epochs=3, batch_size=4, grad_accum=4 (eff_batch=16), warmup=100, LoRA r=64 alpha=128, QLoRA 4-bit, max_length=2048\\n**输入**: step2 的 rsft_train.jsonl, SFT s44 adapter（merge 后重新 LoRA）\\n**输出**: `/root/autodl-tmp/rsft_output_4b_sft_s44/`\\n**预估时间**: ~1.5-2h（~2700 samples, 3 epochs, QLoRA）\\n**
…[truncated 1963 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_knowledge_update_memory_scaling_stats_20260519T001114",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-19T00:11:58.653453+00:00_

called mcp__agent-ml-research__save_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__save_project_file</summary>

````json
{
  "project": "faith-evidence-ie",
  "file": "memory.md",
  "content": "# D112 Pipeline Plan: RSFT from SFT s44\n\n## 概述\n验证 RSFT 在最强 SFT seed（s44, ign_f1=0.4734）上的效果。之前所有 4B RSFT 都基于 SFT s42（最弱 seed, ign_f1≈0.40）。\n\n## 脚本位置\n`/root/autodl-tmp/scripts/d112/` 下 4 个脚本\n\n## Pipeline 步骤\n\n### Step 1: 候选生成\n**脚本**: `step1_generate_candidates.sh`\n**命令**:\n```bash\n# 4-GPU 并行（推荐，总计约 3-4h）\nGPU=0 SHARD=0 bash step1_generate_candidates.sh &\nGPU=1 SHARD=1 bash step1_generate_candidates.sh &\nGPU=2 SHARD=2 bash step1_generate_candidates.sh &\nGPU=3 SHARD=3 bash step1_generate_candidates.sh &\nwait\n\n# 或单 GPU（约 12-16h）\nGPU=0 bash step1_generate_candidates.sh\n```\n**参数**: N=8, temperature=0.7, top_p=0.95, batch_size=1, max_new_tokens=1024, seed=42\n**输入**: base=Qwen3-4B, adapter=sft_output_seed44, data=DocRED train_annotated (3053 docs)\n**输出**: `/root/autodl-tmp/rsft_generations_4b_sft_s44/`\n**预估时间**: 4-GPU 并行 ~3-4h, 单 GPU ~12-16h\n**GPU**: 每个 shard 1 GPU（4 GPU 最优）\n\n### Step 2: CED 打分 + k=1 筛选\n**脚本**: `step2_ced_score.sh`\n**命令**:\n```bash\nGPU=0 bash step2_ced_score.sh\n```\n**参数**: CED scoring (format_w=0.2, f1_w=0.4, ced_w=0.4), selection_strategy=top_k, k=1, tau=0.5\n**NLI 模型**: cross-encoder/nli-deberta-v3-base（HF cache 已有）\n**输入**: step1 输出目录（自动合并 shard）\n**输出**: `/root/autodl-tmp/rsft_scored_4b_sft_s44/`\n**预估时间**: ~30-60 min\n**GPU**: 1 GPU（NLI 模型很小）\n**预期产出**: ~2700-2800 条训练样本（k=1, 每 doc 最多 1 条）\n\n### Step 3: RSFT 训练\n**脚本**: `step3_k1_filter_and_train.sh`\n**命令**:\n```bash\nGPU=0 bash step3_k1_filter_and_train.sh\n```\n**参数**: lr=2e-5, epochs=3, batch_size=4, grad_accum=4 (eff_batch=16), warmup=100, LoRA r=64 alpha=128, QLoRA 4-bit, max_length=2048\n**输入**: step2 的 rsft_train.jsonl, SFT s44 adapter（merge 后重新 LoRA）\n**输出**: `/root/autodl-tmp/rsft_output_4b_sft_s44/`\n**预估时间**: ~1.5-2h（~2700 samples, 3 epochs, QLoRA）\n**GPU**: 1 GPU\n**W&B run**: d112-rsft-ced-k1-from-sft-s44\n\n### Step 4: 评估\n**脚本**: `step4_eval.sh`\n**命令**:\n```bash\n# 先确认 GPU 空闲 (C001)\nnvidia-smi\nGPU=0 bash step4_eval.sh\n```\n**参数**: D076 protocol, batch_size=4, max_new_tokens=1024, seed=42, no-quantize (bf16 full precision)\n**加载**: base Qwen3-4B -> merge SFT s44 -> load RSFT adapter\n**输出**: `/root/autodl-tmp/eval_results/d112_rsft_from_sft_s44/`\n**预估时间**: ~20-30 min\n**GPU**: 1 GPU（显存需 < 2GB 空闲才可提交）\n\n## 依赖关系\n```\nStep 1 (生成) → Step 2 (打分) → Step 3 (训练) → Step 4 (评估)\n```\nStep 1 可 4-GPU 并行加速。Step 2-4 串行，各需 1 GPU。\n\n## 总预估时间\n- 4-GPU 生成: ~3-4h + 打分 ~1h + 训练 ~2h + eval ~0.5h = **~6.5-7.5h**\n- 单 GPU 全程: ~12-16h + 1h + 2h + 0.5h = **~15.5-19.5h**\n\n## 关键路径\n| 输入 | 路径 | 状态 |\n|------|------|------|\n| Base model | /root/autodl-tmp/models/Qwen3-4B | ✅ |\n| SFT s44 adapter | /root/autodl-tmp/sft_output_seed44 | ✅ |\n| DocRED data | /root/autodl-tmp/data/docred | ✅ (3053 docs) |\n| NLI model | cross-encoder/nli-deberta-v3-base | ✅ (HF cache) |\n\n## Canonical s42 参数对照\n所有超参与 canonical s42 RSFT pipeline 完全一致，仅替换了 SFT adapter 路径（sft_output → sft_output_seed44）和输出目录。\n\n---\n\n# GRPO bf16 G=4 学习曲线结论\n\n## 评估结果\n| checkpoint | ign_f1 | rel_f1 | evi_f1 | edcr |\n|-----------|--------|--------|--------|------|\n| ckpt-100 | 0.4431 | 0.4511 | 0.8010 | 0.6453 |\n| ckpt-200 | 0.4446 | 0.4513 | 0.8053 | 0.6489 |\n| Δ | +0.0015 | +0.0002 | +0.0043 | +0.0036 |\n\n## 结论\n- 模型在 step 100 已收敛，ckpt-200 仅 +0.15pp ign_f1，所有指标几乎持平。**ckpt-100 是最优 checkpoint**（性价比最高）。\n- vs SFT baseline (ign_f1=0.4036): GRPO bf16 **+3.95pp**，证明 bf16 full-precision GRPO 在 IE 任务上有正向增益。\n- 与 QLoRA GRPO catastrophic forgetting 形成鲜明对比：bf16 GRPO 避免了量化训练的灾难性遗忘。\n- **论文意义**: Claim 3 (decoupling spectrum) 的关键数据点。bf16 GRPO 是 spectrum 上 SFT → GRPO → RSFT 的中间锚点，证明精度是 GRPO 成功的必要条件。\n\n---\n\n# 4B SFT 3-seed D076 统一基准 (2026-05-19)\n\n| Seed | ign_f1 | evi_f1 | edcr |\n|------|--------|--------|------|\n| s42 | 0.3974 | 0.7986 | 0.6982 |\n| s43 | 0.4365 | — | — |\n| s44 | 0.4734 | — | — |\n\nMean ign_f1 = 0.4358, sample_std = 3.80pp\ns42 是最弱 seed，s44 最强。方差 3.80pp 较大 → SFT 对 seed 敏感 → 支持 D112（验证 RSFT 在强 seed 上的效果）\n\n---\n\n# 8B SFT 2-seed 对比 (2026-05-19)\n\n| Seed | ign_f1 |\n|------|--------|\n| s42 | 0.5051 |\n| s44 | 0.4681 |\n\nMean = 0.4866, sample_std = 2.62pp\n注意：8B 尺度 s42 是强 seed（与 4B 相反）\n\n---\n\n# D112 重叠修复 (2026-05-19)\n- 原始非分片 run 处理全部 3027 docs，与 shard 1/2 重叠\n- 已 kill 并重启为 4-shard 并行（各 ~756 docs）\n- step2 load_generations 原生支持 shard_*/ 合并去重\n- 教训：submit_training_job 时如果脚本支持 SHARD 变量，必须显式传入\n"
}
````

</details>

<details><summary>Recorded metadata</summary>

````json
{
  "recorded_role": "tool",
  "session": "worker_knowledge_update_memory_scaling_stats_20260519T001114",
  "tool": "mcp__agent-ml-research__save_project_file",
  "tool_args": {
    "project": "faith-evidence-ie",
    "file": "memory.md",
    "content": "# D112 Pipeline Plan: RSFT from SFT s44\n\n## 概述\n验证 RSFT 在最强 SFT seed（s44, ign_f1=0.4734）上的效果。之前所有 4B RSFT 都基于 SFT s42（最弱 seed, ign_f1≈0.40）。\n\n## 脚本位置\n`/root/autodl-tmp/scripts/d112/` 下 4 个脚本\n\n## Pipeline 步骤\n\n### Step 1: 候选生成\n**脚本**: `step1_generate_candidates.sh`\n**命令**:\n```bash\n# 4-GPU 并行（推荐，总计约 3-4h）\nGPU=0 SHARD=0 bash step1_generate_candidates.sh &\nGPU=1 SHARD=1 bash step1_generate_candidates.sh &\nGPU=2 SHARD=2 bash step1_generate_candidates.sh &\nGPU=3 SHARD=3 bash step1_generate_candidates.sh &\nwait\n\n# 或单 GPU（约 12-16h）\nGPU=0 bash step1_generate_candidates.sh\n```\n**参数**: N=8, temperature=0.7, top_p=0.95, batch_size=1, max_new_tokens=1024, seed=42\n**输入**: base=Qwen3-4B, adapter=sft_output_seed44, data=DocRED train_annotated (3053 docs)\n**输出**: `/root/autodl-tmp/rsft_generations_4b_sft_s44/`\n**预估时间**: 4-GPU 并行 ~3-4h, 单 GPU ~12-16h\n**GPU**: 每个 shard 1 GPU（4 GPU 最优）\n\n### Step 2: CED 打分 + k=1 筛选\n**脚本**: `step2_ced_score.sh`\n**命令**:\n```bash\nGPU=0 bash step2_ced_score.sh\n```\n**参数**: CED scoring (format_w=0.2, f1_w=0.4, ced_w=0.4), selection_strategy=top_k, k=1, tau=0.5\n**NLI 模型**: cross-encoder/nli-deberta-v3-base（HF cache 已有）\n**输入**: step1 输出目录（自动合并 shard）\n**输出**: `/root/autodl-tmp/rsft_scored_4b_sft_s44/`\n**预估时间**: ~30-60 min\n**GPU**: 1 GPU（NLI 模型很小）\n**预期产出**: ~2700-2800 条训练样本（k=1, 每 doc 最多 1 条）\n\n### Step 3: RSFT 训练\n**脚本**: `step3_k1_filter_and_train.sh`\n**命令**:\n```bash\nGPU=0 bash step3_k1_filter_and_train.sh\n```\n**参数**: lr=2e-5, epochs=3, batch_size=4, grad_accum=4 (eff_batch=16), warmup=100, LoRA r=64 alpha=128, QLoRA 4-bit, max_length=2048\n**输入**: step2 的 rsft_train.jsonl, SFT s44 adapter（merge 后重新 LoRA）\n**输出**: `/root/autodl-tmp/rsft_output_4b_sft_s44/`\n**预估时间**: ~1.5-2h（~2700 samples, 3 epochs, QLoRA）\n**GPU**: 1 GPU\n**W&B run**: d112-rsft-ced-k1-from-sft-s44\n\n### Step 4: 评估\n**脚本**: `step4_eval.sh`\n**命令**:\n```bash\n# 先确认 GPU 空闲 (C001)\nnvidia-smi\nGPU=0 bash step4_eval.sh\n```\n**参数**: D076 protocol, batch_size=4, max_new_tokens=1024, seed=42, no-quantize (bf16 full precision)\n**加载**: base Qwen3-4B -> merge SFT s44 -> load RSFT adapter\n**输出**: `/root/autodl-tmp/eval_results/d112_rsft_from_sft_s44/`\n**预估时间**: ~20-30 min\n**GPU**: 1 GPU（显存需 < 2GB 空闲才可提交）\n\n## 依赖关系\n```\nStep 1 (生成) → Step 2 (打分) → Step 3 (训练) → Step 4 (评估)\n```\nStep 1 可 4-GPU 并行加速。Step 2-4 串行，各需 1 GPU。\n\n## 总预估时间\n- 4-GPU 生成: ~3-4h + 打分 ~1h + 训练 ~2h + eval ~0.5h = **~6.5-7.5h**\n- 单 GPU 全程: ~12-16h + 1h + 2h + 0.5h = **~15.5-19.5h**\n\n## 关键路径\n| 输入 | 路径 | 状态 |\n|------|------|------|\n| Base model | /root/autodl-tmp/models/Qwen3-4B | ✅ |\n| SFT s44 adapter | /root/autodl-tmp/sft_output_seed44 | ✅ |\n| DocRED data | /root/autodl-tmp/data/docred | ✅ (3053 docs) |\n| NLI model | cross-encoder/nli-deberta-v3-base | ✅ (HF cache) |\n\n## Canonical s42 参数对照\n所有超参与 canonical s42 RSFT pipeline 完全一致，仅替换了 SFT adapter 路径（sft_output → sft_output_seed44）和输出目录。\n\n---\n\n# GRPO bf16 G=4 学习曲线结论\n\n## 评估结果\n| checkpoint | ign_f1 | rel_f1 | evi_f1 | edcr |\n|-----------|--------|--------|--------|------|\n| ckpt-100 | 0.4431 | 0.4511 | 0.8010 | 0.6453 |\n| ckpt-200 | 0.4446 | 0.4513 | 0.8053 | 0.6489 |\n| Δ | +0.0015 | +0.0002 | +0.0043 | +0.0036 |\n\n## 结论\n- 模型在 step 100 已收敛，ckpt-200 仅 +0.15pp ign_f1，所有指标几乎持平。**ckpt-100 是最优 checkpoint**（性价比最高）。\n- vs SFT baseline (ign_f1=0.4036): GRPO bf16 **+3.95pp**，证明 bf16 full-precision GRPO 在 IE 任务上有正向增益。\n- 与 QLoRA GRPO catastrophic forgetting 形成鲜明对比：bf16 GRPO 避免了量化训练的灾难性遗忘。\n- **论文意义**: Claim 3 (decoupling spectrum) 的关键数据点。bf16 GRPO 是 spectrum 上 SFT → GRPO → RSFT 的中间锚点，证明精度是 GRPO 成功的必要条件。\n\n---\n\n# 4B SFT 3-seed D076 统一基准 (2026-05-19)\n\n| Seed | ign_f1 | evi_f1 | edcr |\n|------|--------|--------|------|\n| s42 | 0.3974 | 0.7986 | 0.6982 |\n| s43 | 0.4365 | — | — |\n| s44 | 0.4734 | — | — |\n\nMean ign_f1 = 0.4358, sample_std = 3.80pp\ns42 是最弱 seed，s44 最强。方差 3.80pp 较大 → SFT 对 seed 敏感 → 支持 D112（验证 RSFT 在强 seed 上的效果）\n\n---\n\n# 8B SFT 2-seed 对比 (2026-05-19)\n\n| Seed | ign_f1 |\n|------|--------|\n| s42 | 0.5051 |\n| s44 | 0.4681 |\n\nMean = 0.4866, sample_std = 2.62pp\n注意：8B 尺度 s42 是强 seed（与 4B 相反）\n\n---\n\n# D112 重叠修复 (2026-05-19)\n- 原始非分片 run 处理全部 3027 docs，与 shard 1/2 重叠\n- 已 kill 并重启为 4-shard 并行（各 ~756 docs）\n- step2 load_generations 原生支持 shard_*/ 合并去重\n- 教训：submit_training_job 时如果脚本支持 SHARD 变量，必须显式传入\n"
  }
}
````

</details>

---

### Tool result

_source line 6 · 2026-05-19T00:11:58.653766+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/memory.md\", \"saved\": true}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_knowledge_update_memory_scaling_stats_20260519T001114",
  "tool": "mcp__agent-ml-research__save_project_file",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 7 · 2026-05-19T00:11:58.653948+00:00_

已追加三段内容（4B SFT 3-seed 统计、8B SFT 2-seed 统计、D112 重叠修复记录），原有内容保持不变。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_knowledge_update_memory_scaling_stats_20260519T001114"
}
```

</details>

---
