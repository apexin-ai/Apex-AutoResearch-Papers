Leave-One-Model-Out Stability Analysis (Dream #3 Response)

Data: 345,600 records (4-model bf16 balanced), 4× 3-model G-studies

| Dropped | item_id% | model×item% | G_item |
|---|---:|---:|---:|
| (none — full 4-model) | 51.29 | 25.25 | 0.8801 |
| gemma-2-9b-it | 52.88 | 22.50 | 0.8629 |
| llama-3.1-8b-instruct | 52.70 | 24.68 | 0.8536 |
| mistral-7b-instruct-v0.3 | 56.57 | 21.47 | 0.8764 |
| qwen3-8b | 54.52 | 21.17 | 0.8728 |

G_item spread: 0.023 (highly stable)
model×item range: 21.17-24.68% (all 3-model subsets below 25%)
Qwen removal has largest m×i impact (-4.08pp); Llama smallest (-0.57pp)
File on server: results/analysis/leave_one_model_out.json