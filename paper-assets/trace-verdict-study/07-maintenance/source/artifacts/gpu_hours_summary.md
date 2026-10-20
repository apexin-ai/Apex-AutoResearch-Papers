# GPU-Hours Summary (W4 fix)

## 总计
- Total experiments: 115
- Total GPU-hours: **322.2h**
- Experiments with GPU-hours data: 102 / 115
- GPU-hours source breakdown: field=55, timestamps=47, unknown=13
- Note: 13 experiments (queued/preparing/allocated) have no runtime data

## 按模型
| Model | Experiments | GPU-hours | % of total |
|-------|------------|-----------|------------|
| Analysis/Eval | 1 | 0.4h | 0.1% |
| CodeLlama-13B | 22 | 40.4h | 12.5% |
| DeepSeek-Coder-6.7B | 18 | 30.8h | 9.6% |
| Qwen2.5-Coder-1.5B | 18 | 15.0h | 4.7% |
| Qwen2.5-Coder-7B | 56 | 235.6h | 73.1% |
| **Total** | **115** | **322.2h** | **100%** |

## 按状态
| Status | Experiments | GPU-hours | % of total |
|--------|------------|-----------|------------|
| allocated | 2 | 0.0h | 0.0% |
| failed | 6 | 2.0h | 0.6% |
| killed | 10 | 114.9h | 35.6% |
| negative | 15 | 35.7h | 11.1% |
| preparing | 3 | 0.0h | 0.0% |
| queued | 7 | 0.0h | 0.0% |
| success | 72 | 169.7h | 52.7% |
| **Total** | **115** | **322.2h** | **100%** |

## 详细列表
| exp_id | model | status | gpu_hours | wall_clock_s | source |
|--------|-------|--------|-----------|-------------|--------|
| regex_baseline_analysis | Analysis/Eval | success | 0.41 | - | timestamps |
| codellama13b_exception_only_seed123 | CodeLlama-13B | success | 2.76 | 9933 | field |
| codellama13b_exception_only_seed42 | CodeLlama-13B | success | 2.75 | 9885 | field |
| codellama13b_exception_only_seed456 | CodeLlama-13B | success | 2.73 | 9834 | field |
| codellama13b_full_trace_head2048_seed42 | CodeLlama-13B | success | 3.91 | 14086 | field |
| codellama13b_full_trace_tail1024_seed42 | CodeLlama-13B | failed | 0.95 | 3407 | field |
| codellama13b_full_trace_tail1024_seed42_v2 | CodeLlama-13B | negative | 2.82 | 10170 | field |
| codellama13b_full_trace_tail1024_seed42_v3 | CodeLlama-13B | success | 3.08 | - | timestamps |
| codellama13b_full_trace_tail2048_seed42 | CodeLlama-13B | failed | 0.08 | 291 | field |
| codellama13b_full_trace_tail2048_seed42_v2 | CodeLlama-13B | negative | 3.97 | 14281 | field |
| codellama13b_full_trace_tail2048_seed42_v3 | CodeLlama-13B | negative | 4.27 | - | timestamps |
| codellama13b_full_trace_tail256_seed42 | CodeLlama-13B | success | 1.86 | 6714 | field |
| codellama13b_full_trace_tail384_seed42 | CodeLlama-13B | negative | 3.75 | - | timestamps |
| codellama13b_full_trace_tail512_seed123 | CodeLlama-13B | preparing | - | - | unknown |
| codellama13b_full_trace_tail512_seed42 | CodeLlama-13B | success | 2.19 | 7898 | field |
| codellama13b_full_trace_tail512_seed456 | CodeLlama-13B | preparing | - | - | unknown |
| codellama13b_no_trace_seed42 | CodeLlama-13B | success | 0.68 | 2452 | field |
| codellama13b_nomarker_seed42 | CodeLlama-13B | killed | 0.33 | 1176 | field |
| codellama13b_vota_seed42 | CodeLlama-13B | success | 4.04 | 14538 | field |
| codellama_exception_only_seed42 | CodeLlama-13B | queued | - | - | unknown |
| codellama_no_trace_seed42 | CodeLlama-13B | queued | - | - | unknown |
| codellama_vota_seed42 | CodeLlama-13B | queued | - | - | unknown |
| zeroshot_codellama13b_exception_only | CodeLlama-13B | success | 0.24 | - | timestamps |
| deepseek_exception_only_seed123 | DeepSeek-Coder-6.7B | negative | 1.88 | 6786 | field |
| deepseek_exception_only_seed42 | DeepSeek-Coder-6.7B | success | 2.04 | 7359 | field |
| deepseek_exception_only_seed456 | DeepSeek-Coder-6.7B | success | 1.90 | - | timestamps |
| deepseek_full_trace_head2048_seed42 | DeepSeek-Coder-6.7B | success | 2.59 | - | timestamps |
| deepseek_full_trace_seed42 | DeepSeek-Coder-6.7B | negative | 2.85 | 10254 | field |
| deepseek_full_trace_seed42_v2 | DeepSeek-Coder-6.7B | killed | 0.24 | - | timestamps |
| deepseek_full_trace_seed42_v3 | DeepSeek-Coder-6.7B | success | 4.80 | - | timestamps |
| deepseek_full_trace_tail1024_seed42 | DeepSeek-Coder-6.7B | success | 1.84 | - | timestamps |
| deepseek_full_trace_tail2048_seed42 | DeepSeek-Coder-6.7B | success | 2.44 | - | timestamps |
| deepseek_full_trace_tail256_seed42 | DeepSeek-Coder-6.7B | success | 0.54 | 1960 | field |
| deepseek_full_trace_tail384_seed42 | DeepSeek-Coder-6.7B | success | 1.78 | - | timestamps |
| deepseek_full_trace_tail512_seed123 | DeepSeek-Coder-6.7B | failed | 0.70 | 2537 | field |
| deepseek_full_trace_tail512_seed123_v2 | DeepSeek-Coder-6.7B | allocated | - | - | unknown |
| deepseek_full_trace_tail512_seed42 | DeepSeek-Coder-6.7B | success | 1.30 | 4666 | field |
| deepseek_full_trace_tail512_seed456 | DeepSeek-Coder-6.7B | success | 2.18 | 7836 | field |
| deepseek_no_trace_seed42 | DeepSeek-Coder-6.7B | negative | 0.50 | 1791 | field |
| deepseek_vota_seed42 | DeepSeek-Coder-6.7B | success | 2.46 | 8840 | field |
| zeroshot_deepseek7b_exception_only | DeepSeek-Coder-6.7B | success | 0.78 | - | timestamps |
| qwen1.5b_exception_only_seed42 | Qwen2.5-Coder-1.5B | queued | - | - | unknown |
| qwen1.5b_full_trace_seed42 | Qwen2.5-Coder-1.5B | queued | - | - | unknown |
| qwen1.5b_no_trace_seed42 | Qwen2.5-Coder-1.5B | queued | - | - | unknown |
| qwen1.5b_vota_seed42 | Qwen2.5-Coder-1.5B | queued | - | - | unknown |
| qwen15b_exception_only_seed42 | Qwen2.5-Coder-1.5B | success | 0.55 | 1990 | field |
| qwen15b_full_trace_head2048_seed42 | Qwen2.5-Coder-1.5B | success | 1.53 | - | timestamps |
| qwen15b_full_trace_seed42 | Qwen2.5-Coder-1.5B | success | 0.90 | 3228 | field |
| qwen15b_full_trace_tail1024_seed42 | Qwen2.5-Coder-1.5B | success | 2.89 | 10407 | field |
| qwen15b_full_trace_tail2048_seed42 | Qwen2.5-Coder-1.5B | success | 2.44 | - | timestamps |
| qwen15b_full_trace_tail256_seed42 | Qwen2.5-Coder-1.5B | negative | 0.25 | - | timestamps |
| qwen15b_full_trace_tail384_seed42 | Qwen2.5-Coder-1.5B | negative | 3.18 | - | timestamps |
| qwen15b_full_trace_tail512_seed123 | Qwen2.5-Coder-1.5B | success | 0.58 | 2094 | field |
| qwen15b_full_trace_tail512_seed42 | Qwen2.5-Coder-1.5B | success | 0.37 | - | timestamps |
| qwen15b_full_trace_tail512_seed456 | Qwen2.5-Coder-1.5B | success | 0.66 | 2370 | field |
| qwen15b_no_trace_seed42 | Qwen2.5-Coder-1.5B | success | 0.32 | 1139 | field |
| qwen15b_nomarker_seed42 | Qwen2.5-Coder-1.5B | success | 0.31 | - | timestamps |
| qwen15b_vota_seed42 | Qwen2.5-Coder-1.5B | success | 0.90 | 3252 | field |
| zeroshot_qwen15b_exception_only | Qwen2.5-Coder-1.5B | success | 0.14 | - | timestamps |
| ae_only_seed123 | Qwen2.5-Coder-7B | success | 2.58 | - | timestamps |
| ae_only_seed456 | Qwen2.5-Coder-7B | success | 2.74 | - | timestamps |
| calibration_analysis_seed42 | Qwen2.5-Coder-7B | success | 0.16 | - | timestamps |
| debugbench_exception_bug_fix | Qwen2.5-Coder-7B | success | 0.20 | - | timestamps |
| debugbench_exception_only_seed42 | Qwen2.5-Coder-7B | success | 0.35 | 1255 | field |
| debugbench_no_trace_seed42 | Qwen2.5-Coder-7B | success | 1.64 | - | timestamps |
| debugbench_vota_seed42 | Qwen2.5-Coder-7B | success | 1.40 | - | timestamps |
| eval_missing_predictions_batch | Qwen2.5-Coder-7B | success | 0.41 | 1480 | field |
| eval_missing_predictions_batch_v2 | Qwen2.5-Coder-7B | success | 0.53 | 1906 | field |
| exception_only_nomarker_seed123 | Qwen2.5-Coder-7B | success | 11.92 | - | timestamps |
| exception_only_nomarker_seed42 | Qwen2.5-Coder-7B | success | 9.78 | - | timestamps |
| exception_only_nomarker_seed456 | Qwen2.5-Coder-7B | success | 12.58 | - | timestamps |
| exception_only_seed123 | Qwen2.5-Coder-7B | success | 2.54 | - | timestamps |
| exception_only_seed456 | Qwen2.5-Coder-7B | success | 2.46 | - | timestamps |
| fewshot_qwen7b_exception_only | Qwen2.5-Coder-7B | success | 0.18 | - | timestamps |
| full_trace_1024tok_seed42 | Qwen2.5-Coder-7B | negative | 3.49 | - | timestamps |
| full_trace_2048tok_seed42 | Qwen2.5-Coder-7B | killed | 2.54 | 9136 | field |
| full_trace_256tok_seed42 | Qwen2.5-Coder-7B | negative | 1.61 | - | timestamps |
| full_trace_512tok_seed42 | Qwen2.5-Coder-7B | negative | 1.79 | - | timestamps |
| full_trace_label_only_seed42 | Qwen2.5-Coder-7B | success | 3.37 | - | timestamps |
| full_trace_seed42 | Qwen2.5-Coder-7B | killed | 3.12 | 11248 | field |
| full_trace_seed42_v2 | Qwen2.5-Coder-7B | negative | 2.18 | 7860 | field |
| full_trace_seed42_v5 | Qwen2.5-Coder-7B | success | 2.18 | 7852 | field |
| full_trace_tail256_seed42 | Qwen2.5-Coder-7B | negative | 0.95 | - | timestamps |
| full_trace_tail_1024_seed42 | Qwen2.5-Coder-7B | success | 2.17 | 7810 | field |
| full_trace_tail_256_seed42 | Qwen2.5-Coder-7B | negative | 2.17 | 7821 | field |
| full_trace_tail_512_seed42 | Qwen2.5-Coder-7B | success | 2.55 | 9194 | field |
| full_trace_tail_seed42 | Qwen2.5-Coder-7B | success | 3.24 | 11653 | field |
| label_only_seed123 | Qwen2.5-Coder-7B | success | 4.36 | - | timestamps |
| label_only_seed456 | Qwen2.5-Coder-7B | success | 4.71 | - | timestamps |
| loop_only_seed123 | Qwen2.5-Coder-7B | success | 2.16 | 7780 | field |
| loop_only_seed456 | Qwen2.5-Coder-7B | success | 2.19 | 7893 | field |
| no_trace_seed42 | Qwen2.5-Coder-7B | killed | 25.92 | 93295 | field |
| no_trace_seed42_v2 | Qwen2.5-Coder-7B | killed | 25.89 | 93212 | field |
| no_trace_seed42_v3 | Qwen2.5-Coder-7B | killed | 1.28 | 4618 | field |
| no_trace_seed42_v4 | Qwen2.5-Coder-7B | success | 0.35 | 1275 | field |
| no_trace_seed42_v5 | Qwen2.5-Coder-7B | success | 4.98 | - | timestamps |
| qwen7b_full_trace_head2048_seed42 | Qwen2.5-Coder-7B | success | 4.10 | - | timestamps |
| qwen7b_full_trace_tail384_seed42 | Qwen2.5-Coder-7B | success | 1.78 | - | timestamps |
| qwen7b_full_trace_tail512_seed123 | Qwen2.5-Coder-7B | success | 2.18 | 7841 | field |
| qwen7b_full_trace_tail512_seed42 | Qwen2.5-Coder-7B | preparing | - | - | unknown |
| qwen7b_full_trace_tail512_seed456 | Qwen2.5-Coder-7B | allocated | - | - | unknown |
| vota_ae_only_seed42 | Qwen2.5-Coder-7B | success | 7.03 | - | timestamps |
| vota_exception_only_seed42 | Qwen2.5-Coder-7B | failed | 0.23 | - | timestamps |
| vota_exception_only_seed42_v2 | Qwen2.5-Coder-7B | success | - | - | unknown |
| vota_loop_only_seed42 | Qwen2.5-Coder-7B | success | 2.21 | 7952 | field |
| vota_no_ae_seed42 | Qwen2.5-Coder-7B | success | 1.92 | 6902 | field |
| vota_seed123 | Qwen2.5-Coder-7B | failed | 0.05 | - | timestamps |
| vota_seed42 | Qwen2.5-Coder-7B | killed | 25.91 | 93291 | field |
| vota_seed42_v2 | Qwen2.5-Coder-7B | killed | 25.89 | 93207 | field |
| vota_seed42_v3 | Qwen2.5-Coder-7B | killed | 3.74 | 13469 | field |
| vota_seed42_v4 | Qwen2.5-Coder-7B | success | 2.27 | 8160 | field |
| vota_seed42_v5 | Qwen2.5-Coder-7B | success | 2.35 | 8443 | field |
| vota_seed456 | Qwen2.5-Coder-7B | failed | 0.02 | 88 | field |
| vota_seed456_v2 | Qwen2.5-Coder-7B | success | 2.42 | - | timestamps |
| zeroshot_qwen7b_exception_only | Qwen2.5-Coder-7B | success | 0.78 | - | timestamps |
