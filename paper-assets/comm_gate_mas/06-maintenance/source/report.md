# Handover — 2026-04-30

> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。

## 运行中
| exp_id | 假设 | 状态 | 关键指标 | W&B |
|--------|------|------|---------|-----|
| distilbert_online_e2e_v2 | Learned DistilBERT ack classifier (F1=0.8669) used as online detection mode achieves comparable pruning accuracy to heuristic baseline on Qwen2.5-7B GSM8K N=300, demonstrating that a lightweight learned classifier can replace hand-crafted rules for online communication pruning. | — | — | — |

## 待处理
- gemma_heuristic_pruning: Gemma heuristic pruning (length<30) safety 与 oracle pruning 一致，将 Gemma 从 exploratory 升为 full participant。已有 oracle pruning 数据: e2e_gemma_gsm8k_ack Δ=-1pp, e2e_gemma_gsm8k_temp07 Δ=+3pp（已分配 westb-28993 GPU:cuda:1，等待提交）
- three_agent_oracle（已分配 bjb2-10838 GPU:cuda:1，等待提交）
- gemma_heuristic_gsm8k（已分配 bjb2-10838 GPU:cuda:0，等待提交）
- deepseek_r1_7b_dissociation（准备中）
- oracle_qwen_gsm8k（准备中）
- p1_oracle_precompute_llama_gpt4omini: GPT-4o-mini oracle precompute for Llama GSM8K traces (297 tasks, 1782 msgs). D201: κ=0.822>0.8 validates GPT-4o-mini as cost-effective substitute ($0.26 vs $13.47). Output: oracle cache JSON for P2 online oracle experiment.（准备中）
- vllm_llama_8192_v2（准备中）
- vllm_llama_8192（准备中）
- 5run_pruned_rerun（准备中）
- p1_oracle_precompute_llama_gpt4omini_recovery（准备中）

## 近期结论
- **distilbert_online_e2e** (failed): —
- **llama_heuristic_threshold_sensitivity** (success): Heuristic detector performance is robust to threshold parametrization (LEN_THRESHOLD, OVERLAP_THRESHOLD, ACK_KEYWORDS)
- **qwen_heuristic_stratqa_4seed** (success): —

## 趋势
成功 91 / 负向 11 / 失败 16 / 共 125

## 下一步
（无活跃 idea，请通过 ideas.md 添加）

## 资源状态
bjb2-10838: 空闲 cuda:0, cuda:1, cuda:2, cuda:3
westb-28993: 空闲 cuda:0, cuda:1, cuda:2, cuda:3

## 告警
- e2e_random_multi_temp07: 训练失败 — unknown
- e2e_five_agent_qwen_gsm8k: 训练失败 — unknown
- e2e_llama_stratqa_n248: 训练失败 — unknown
- vllm_7b_server: 已被终止 — unknown
- oracle_online_llama_gsm8k: 已被终止 — unknown
- oracle_5class_qwen_gsm8k: 已被终止 — unknown
- oracle_llama_n1000_fixed: 已被终止 — unknown
- online_fg_pruning_qwen: 已被终止 — unknown
- qwen_10run_oracle_gsm8k_rerun: 已被终止 — unknown
- oracle_online_llama_gsm8k_v2: 训练失败 — unknown
- llama_length_only_gsm8k_5seed: 已被终止 — unknown
- prompt_mod_qwen25_gsm8k: 训练失败 — unknown
- prompt_mod_qwen25_gsm8k_v2_rerun: 训练失败 — unknown
- p2_oracle_online_llama_v3: 训练失败 — unknown
- p2_oracle_online_llama_v4: 训练失败 — unknown
- llama_heuristic_3seed: 训练失败 — unknown
- llama_heuristic_3seed_v2: 训练失败 — unknown
- llama_heuristic_3seed_v3: 训练失败 — unknown
- llama_heuristic_5seed_ext: 训练失败 — unknown
- oracle_qwen72b_seed123: 训练失败 — unknown
- llama_heuristic_arc: 训练失败 — unknown
- qwen_heuristic_arc: 训练失败 — unknown
- distilbert_online_e2e: 训练失败 — unknown
