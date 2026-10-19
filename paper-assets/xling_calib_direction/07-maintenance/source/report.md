# Handover — 2026-05-21

> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。

## 运行中
（无）

## 待处理
- plan_001_v2: Cross-lingual correctness direction transfers across languages in Qwen3-235B-A22B (94-layer MoE, GPTQ-Int4): English-trained linear probes at 24 probed layers (every 4th + final layer 93) will transfer to 19 non-English languages with AUROC ≥ 0.58 for ≥15/19 languages at best layer, with depth-dependent transfer pattern. Retry with GPTQModel.from_quantized() API after AutoModelForCausalLM meta device crash.（已分配 ? GPU:?，等待提交）

## 近期结论
- **plan_001** (failed): Cross-lingual correctness direction transfers across languages in Qwen3-235B-A22B (94-layer MoE, GPTQ-Int4): English-trained linear probes at 24 probed layers (every 4th + final layer 93) will transfer to 19 non-English languages with AUROC ≥ 0.58 for ≥15/19 languages at best layer, with depth-dependent transfer pattern. 235B MoE architecture with 22B active params provides scale contrast to 7-8B dense models (mvp_001/003).
- **plan_002_v3** (killed): Cross-lingual correctness direction transfers across languages in Llama 4 Scout (48-layer MoE, W4A16): English-trained linear probes at 13 probed layers (0,4,8,...,44,47) will transfer to 19 non-English languages with AUROC ≥ 0.58 for ≥15/19 languages at best layer, with depth-dependent transfer pattern (shallow→deep ΔAUROC ≥ 5pp). MoE architecture with 17B active params provides architectural contrast to dense Qwen models. Retry after killing Qwen3 dry run (PID 482839) that was occupying GPU 1-3. ← 基于 plan_002_4gpu
- **plan_002_4gpu** (failed): Cross-lingual correctness direction transfers across languages in Llama 4 Scout (48-layer MoE, W4A16): English-trained linear probes at 13 probed layers (0,4,8,...,44,47) will transfer to 19 non-English languages with AUROC ≥ 0.58 for ≥15/19 languages at best layer, with depth-dependent transfer pattern (shallow→deep ΔAUROC ≥ 5pp). MoE architecture with 17B active params provides architectural contrast to dense Qwen models. Retry of plan_002 with 4 GPUs (single-GPU OOM confirmed by dry-run). ← 基于 plan_002

## 趋势
成功 4 / 负向 0 / 失败 4 / 共 9

## 下一步
（无活跃 idea，请通过 ideas.md 添加）

## 资源状态
westd-13176: 无 GPU 信息

## 告警
- plan_013_probing_controls_v2: 训练失败 — unknown
- plan_002: 训练失败 — unknown
- plan_002_4gpu: 训练失败 — unknown
- plan_002_v3: 已被终止 — unknown
- plan_001: 训练失败 — unknown
