# data cliff curve csv — Part 3 of 3

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Worker execution logs

[← Part 2](part-002.md) · [Transcript overview](../data-cliff-curve-csv.md) · [Structured JSON](../../../sessions/a6/a67ce1741c3e766a3929.json)

## Before a recorded user message

### Tool result

_source line 29 · 2026-05-27T04:32:10.412Z_

<details><summary>↩ Tool result · `toolu_012tdwJiYpdoaiWGzX3aSpgU`</summary>

```text
Total rows: 273

OpenVLA|libero_10|attention|0.07|24.0|yes|eval_openvla_attn_k07_long_seed42_v2|westd-38929|
OpenVLA|libero_10|attention|0.075|37.4|yes|eval_openvla_attn_k075_long_seed42|westd-41074|[PARTIAL: 430/500 episodes] timeout EXIT_CODE=124 on westd-4
OpenVLA|libero_10|attention|0.085|45.8|yes|eval_openvla_attn_k085_long_seed42_v5|westd-38929|
OpenVLA|libero_10|attention|0.09|44.0|yes|eval_openvla_attn_k09_long_seed42_v3|westd-38929|
OpenVLA|libero_10|attention|0.5|14.6|yes|eval_openvla_attn_k05_long_seed42|westd-27271|
OpenVLA|libero_10|l2norm|0.07|0.312|yes|eval_openvla_l2norm_k07_long_seed42_v2|westd-38929|
OpenVLA|libero_10|l2norm|0.085|0.388|yes|eval_openvla_l2norm_k085_long_seed42_v2|westd-38929|
OpenVLA|libero_10|l2norm|0.09|43.6|yes|eval_openvla_l2norm_k09_long_seed42_v3|westd-38929|
OpenVLA|libero_10|random|0.05|18.6|yes|eval_openvla_random_k05_long_seed42_v2|westd-38929|
OpenVLA|libero_10|random|0.07|0.388|yes|eval_openvla_random_k07_long_seed42_v2|westd-38929|
OpenVLA|libero_10|random|0.085|0.45|yes|eval_openvla_random_k085_long_seed42_v3|westd-38929|
OpenVLA|libero_10|random|0.09|46.8|yes|eval_openvla_random_k09_long_seed42_v3|westd-38929|
OpenVLA|libero_goal|attention|0.05|44.2|yes|eval_openvla_attn_k05_goal_seed42|westd-27271|
OpenVLA|libero_goal|attention|0.07|0.664|yes|eval_openvla_attn_k07_goal_seed42|westd-38929|
OpenVLA|libero_goal|attention|0.085|74.6|yes|eval_openvla_attn_k085_goal_seed42_v3|westd-38929|
OpenVLA|libero_goal|attention|0.09|73.2|yes|eval_openvla_attn_k09_goal_seed43_v4|westd-27271|
OpenVLA|libero_goal|attention|0.09|0.732|yes|eval_openvla_attn_k09_goal_seed42|westd-27271|
OpenVLA|libero_goal|attention|0.75|67.4|yes|eval_openvla_attn_k075_goal_seed42|westd-27271|
OpenVLA|libero_goal|l2norm|0.05|0.434|yes|eval_openvla_l2norm_k05_goal_seed42|westd-41074|
OpenVLA|libero_goal|l2norm|0.05|0.434|yes|eval_openvla_l2norm_k05_goal_seed42_v3|westd-27271|
OpenVLA|libero_goal|l2norm|0.07|0.684|yes|eval_openvla_l2norm_k07_goal_seed42|westd-27271|
OpenVLA|libero_goal|l2norm|0.075|70.2|yes|eval_openvla_l2norm_k075_goal_seed42_v2|westd-27271|
OpenVLA|libero_goal|l2norm|0.085|75.4|yes|eval_openvla_l2norm_k085_goal_seed42|westd-27271|
OpenVLA|libero_goal|l2norm|0.09|75.2|yes|eval_openvla_l2norm_k09_goal_seed43|westd-27271|
OpenVLA|libero_goal|l2norm|0.09|0.752|yes|eval_openvla_l2norm_k09_goal_seed43_v3|westd-27271|
OpenVLA|libero_goal|l2norm|0.09|0.748|yes|eval_openvla_l2norm_k09_goal_seed42|westd-27271|
OpenVLA|libero_goal|random|0.05|0.522|yes|eval_openvla_random_k05_goal_seed42|westd-27271|
OpenVLA|libero_goal|random|0.05|0.522|yes|eval_openvla_random_k05_goal_seed42_v2|westd-27271|失败原因: 进程在 Task 2/10 开头无错误退出（日志仅 21 行，无 Traceback/OOM）。v2 使用了
OpenVLA|libero_goal|random|0.07|68.4|yes|eval_openvla_random_k07_goal_seed42_v4|westd-27271|
OpenVLA|libero_goal|random|0.085|78.6|yes|eval_openvla_random_k085_goal_seed42|westd-38929|
OpenVLA|libero_goal|random|0.09|80.4|yes|eval_openvla_random_k09_goal_seed43|westd-27271|
OpenVLA|libero_goal|random|0.09|79.6|yes|eval_openvla_random_k09_goal_seed42||
OpenVLA|libero_goal|random|0.75|72.0|yes|eval_openvla_random_k075_goal_seed42|westd-38929|False alarm: 实验无 spec（可能未正确启动或 cqa1 代码修复前部署的无效实验）。Random k=0
OpenVLA|libero_object||0.03|0.206|yes|eval_openvla_pruning_k03_restart|westd-27271|
OpenVLA|libero_object||0.07|0.49|yes|eval_openvla_pruning_k07|westd-27271|
OpenVLA|libero_object||0.095|69.4|yes|eval_openvla_prune_k095|westd-27271|
OpenVLA|libero_object|attention|0.07|43.8|yes|eval_openvla_attn_k07_object_seed42_v3|westd-41074|
OpenVLA|libero_object|attention|0.075|53.2|yes|eval_openvla_attn_k075_object_seed42|westd-41074|
OpenVLA|libero_object|attention|0.085|0.55|yes|eval_openvla_attn_k085_object_seed42|westd-38929|
OpenVLA|libero_object|l2norm|0.03|25.0|yes|eval_openvla_l2norm_k03_object_seed43|westd-38929|
OpenVLA|libero_object|l2norm|0.03|25.0|yes|eval_openvla_l2norm_k03_object_seed42|westd-38929|
OpenVLA|libero_object|l2norm|0.03|0.25|yes|eval_openvla_prune_l2norm_k03|westd-38929|
OpenVLA|libero_object|l2norm|0.03|0.25|yes|eval_openvla_prune_l2norm_k03_seed42|westd-38929|[D124] Registered from westd-38929 eval_results.
OpenVLA|libero_object|l2norm|0.05|0.392|yes|eval_openvla_l2norm_k05_object_seed42_v4|westd-41074|
OpenVLA|libero_object|l2norm|0.05|0.392|yes|eval_openvla_l2norm_k05_object_seed42_v5|westd-38929|
OpenVLA|libero_object|l2norm|0.05|39.2|yes|eval_openvla_l2norm_k05_object_seed43|westd-27271|
OpenVLA|libero_object|l2norm|0.05|39.2|yes|eval_openvla_l2norm_k05_object_seed42|westd-38929|失败原因: process dead 5× with no sentinel/W&B — 与 westd-38929 上
OpenVLA|libero_object|l2norm|0.05|0.392|yes|eval_openvla_prune_l2norm_k05|westd-38929|
OpenVLA|libero_object|l2norm|0.05|0.392|yes|eval_openvla_prune_l2norm_k05_seed42|westd-38929|[D124] Registered from westd-38929 eval_results.
OpenVLA|libero_object|l2norm|0.07|0.498|yes|eval_openvla_l2norm_k07_object_seed42_v3|westd-38929|
OpenVLA|libero_object|l2norm|0.07|0.498|yes|eval_openvla_l2norm_k07_object_seed42_v2|westd-38929|Cron 误判 failed。日志显示实验完成: Overall SR 49.8% (249/500)。结果文件: /r
OpenVLA|libero_object|l2norm|0.07|49.8|yes|eval_openvla_prune_l2norm_k07_seed43_v2|westd-27271|
OpenVLA|libero_object|l2norm|0.075|0.574|yes|eval_openvla_l2norm_k075_object_seed42|westd-41074|
OpenVLA|libero_object|l2norm|0.09|0.688|yes|eval_openvla_zeromask_l2norm_k09_object_seed42|westd-41074|
OpenVLA|libero_object|l2norm|0.09|0.706|yes|eval_openvla_l2norm_k09_object_seed42|westd-27271|
OpenVLA|libero_object|l2norm|0.09|0.706|yes|eval_openvla_prune_l2norm_k09|westd-38929|
OpenVLA|libero_object|l2norm|0.09|0.706|yes|eval_openvla_prune_l2norm_k09_seed42|westd-38929|[D124] Registered from westd-38929 eval_results.
OpenVLA|libero_object|l2norm|0.095|0.706|yes|eval_openvla_prune_l2norm_k095|westd-38929|
OpenVLA|libero_object|l2norm|0.095|0.706|yes|eval_openvla_prune_l2norm_k095_seed42|westd-38929|[D124] Registered from westd-38929 eval_results.
OpenVLA|libero_object|random|0.03|0.214|yes|eval_openvla_random_k03_object_seed42_v2|westd-38929|
OpenVLA|libero_object|random|0.05|35.8|yes|eval_openvla_random_k05_object_seed42_v3|westd-41074|
OpenVLA|libero_object|random|0.05|35.8|yes|eval_openvla_prune_random_k05_seed42|westd-41074|Confirmed running on westd-41074:cuda:0; PID 659206
OpenVLA|libero_object|random|0.05|0.356|yes|eval_openvla_prune_random_k05_seed43_v2|westd-41074|
OpenVLA|libero_object|random|0.07|0.444|yes|eval_openvla_random_k07_object_seed42_v2|westd-38929|Cron 误判 process gone。日志显示实验完成: Overall SR 44.4% (222/500)。结果
OpenVLA|libero_object|random|0.07|0.526|yes|eval_openvla_random_k07_object_seed43|westd-38929|
OpenVLA|libero_object|random|0.07|0.526|yes|eval_openvla_prune_random_k07_seed43_v2|westd-41074|
OpenVLA|libero_object|random|0.09|0.718|yes|eval_openvla_zeromask_random_k09_object_seed42|westd-41074|
OpenVLA|libero_object|random|0.09|0.646|yes|eval_openvla_prune_random_k09_seed42|westd-41074|
OpenVLA|libero_object|random|0.09|0.622|yes|eval_openvla_prune_random_k09_seed43|westd-27271|
OpenVLA|libero_object|random|0.095|0.668|yes|eval_openvla_prune_random_k095_seed43|westd-41074|
OpenVLA|libero_object|random|0.95|67.4|yes|eval_openvla_random_k095_object_seed42||
OpenVLA|libero_spatial|attention|0.09|0.804|yes|eval_openvla_attn_k09_spatial_seed42|westd-27271|
OpenVLA|libero_spatial|l2norm|0.09|0.75|yes|eval_openvla_l2norm_k09_spatial_seed42|westd-27271|
OpenVLA|libero_spatial|random|0.05|0.5|yes|eval_openvla_random_k05_spatial_seed42|westd-27271|
OpenVLA|libero_spatial|random|0.09|79.8|yes|eval_openvla_random_k09_spatial_seed42|westd-41074|
pi0.5|libero_10|attention|0.05|49.8|no|eval_pi05_attention_k05_long_seed42_v2|cqa1-33015|[CONTAMINATED: lenient success condition] cqa1 V-C code uses
pi0.5|libero_10|attention|0.075|52.4|no|eval_pi05_attention_k075_long_seed42_v2|cqa1-33015|[CONTAMINATED: lenient success condition] cqa1 V-C code uses
pi0.5|libero_10|attention|0.075|51.8|no|eval_pi05_attention_k075_long_seed42|cqa1-33015|
pi0.5|libero_10|attention|0.085|51.6|no|eval_pi05_attention_k085_long_seed42_v2|cqa1-33015|[CONTAMINATED: lenient success condition] cqa1 V-C code uses
pi0.5|libero_10|attention|0.09|0.638|no|eval_pi05_attention_k09_long_seed42_postfix|cqa1-33015|
pi0.5|libero_10|attention|0.095|77.0|no|eval_pi05_attn_k095_long_seed42|cqa1-33015|
pi0.5|libero_10|attention|0.7|50.8|no|eval_pi05_attention_k07_long_seed42_v2|cqa1-33015|[CONTAMINATED: lenient success condition] cqa1 V-C code uses
pi0.5|libero_10|l2norm|0.03|39.2|yes|eval_pi05_l2norm_k03_long_seed43_postfix_v2|westd-38929|
pi0.5|libero_10|l2norm|0.05|50.0|no|eval_pi05_l2norm_k05_long_seed42_v4|cqa1-33015|[CONTAMINATED: lenient success condition] cqa1 V-C code uses
pi0.5|libero_10|l2norm|0.05|0.502|no|eval_pi05_l2norm_k05_long_seed42|cqa1-33015|
pi0.5|libero_10|l2norm|0.05|0.53|no|eval_pi05_l2norm_k05_long_seed43_postfix_v2|cqa1-33015|
pi0.5|libero_10|l2norm|0.05|51.4|yes|eval_pi05_l2norm_k05_long_seed42_v3|westd-41074|
pi0.5|libero_10|l2norm|0.07|0.65|no|eval_pi05_l2norm_k07_long_seed43_v3|cqa1-33015|
pi0.5|libero_10|l2norm|0.07|62.6|yes|eval_pi05_l2norm_k07_long_seed42_postfix|westd-27271|
pi0.5|libero_10|l2norm|0.07|0.654|yes|eval_pi05_l2norm_k07_long_seed43_v4|westd-41074|
pi0.5|libero_10|l2norm|0.075|73.4|no|eval_pi05_l2norm_k075_long_seed42|cqa1-33015|
pi0.5|libero_10|l2norm|0.085|78.8|yes|eval_pi05_l2norm_k085_long_seed42_v3||
pi0.5|libero_10|l2norm|0.085|80.0|no|eval_pi05_l2norm_k085_long_seed43_v3|cqa1-33015|
pi0.5|libero_10|l2norm|0.085|0.78|no|eval_pi05_l2norm_k085_long_seed42_postfix_v3|cqa1-33015|
pi0.5|libero_10|l2norm|0.085|78.6|yes|eval_pi05_l2norm_k085_long_seed43_postfix|westd-41074|
pi0.5|libero_10|l2norm|0.085|78.4|yes|eval_pi05_l2norm_k085_long_seed42_postfix|westd-41074|
pi0.5|libero_10|l2norm|0.085|0.77|yes|eval_pi05_l2norm_k085_long_seed43_v4|westd-41074|
pi0.5|libero_10|l2norm|0.09|0.808|no|eval_pi05_l2norm_k09_long_seed43_postfix|cqa1-33015|
pi0.5|libero_10|l2norm|0.09|80.0|no|eval_pi05_l2norm_k09_long_seed42_postfix_v2|cqa1-33015|
pi0.5|libero_10|l2norm|0.09|80.0|yes|eval_pi05_l2norm_k09_long_seed43_postfix_v2|westd-41074|
pi0.5|libero_10|l2norm|0.09|0.81|yes|eval_pi05_l2norm_k09_long_seed42|westd-41074|
pi0.5|libero_10|l2norm|0.0925|0.832|no|eval_pi05_l2norm_k0925_long_seed42_v2|cqa1-33015|
pi0.5|libero_10|l2norm|0.095|87.4|yes|eval_pi05_l2norm_k095_long_seed43_postfix|westd-38929|
pi0.5|libero_10|l2norm|0.7|65.8|yes|eval_pi05_l2norm_k07_long_seed43_v2|westd-38929|
pi0.5|libero_10|l2norm|0.85|77.8|no|eval_pi05_l2norm_k085_long_seed42_v4|cqa1-33015|[CONTAMINATED: lenient success condition] cqa1 V-C code uses
pi0.5|libero_10|l2norm|0.85|79.0|yes|eval_pi05_l2norm_k085_long_seed43_v2|westd-38929|
pi0.5|libero_10|l2norm|0.95|87.0|yes|eval_pi05_l2norm_k095_long_seed42_postfix|westd-38929|
pi0.5|libero_10|random|0.03|0.272|no|eval_pi05_random_k03_long_seed43_v4|cqa1-33015|
pi0.5|libero_10|random|0.03|29.6|yes|eval_pi05_random_k03_long_seed42_postfix|westd-38929|
pi0.5|libero_10|random|0.03|28.0|yes|eval_pi05_random_k03_long_seed43_v2|westd-41074|
pi0.5|libero_10|random|0.03|0.29|yes|eval_pi05_random_k03_long_seed42|westd-38929|
pi0.5|libero_10|random|0.05|50.2|no|eval_pi05_random_k05_long_seed42_v3|cqa1-33015|[CONTAMINATED: lenient success condition] cqa1 V-C code uses
pi0.5|libero_10|random|0.05|0.502|no|eval_pi05_random_k05_long_seed42|cqa1-33015|
pi0.5|libero_10|random|0.05|46.8|no|eval_pi05_random_k05_long_seed43_postfix|cqa1-33015|
pi0.5|libero_10|random|0.07|0.686|no|eval_pi05_random_k07_long_seed43_postfix|cqa1-33015|
pi0.5|libero_10|random|0.075|62.4|no|eval_pi05_random_k075_long_seed42_v2|cqa1-33015|[CONTAMINATED: lenient success condition] cqa1 V-C code uses
pi0.5|libero_10|random|0.085|44.4|no|eval_pi05_random_k085_long_seed42_v2|cqa1-33015|[CONTAMINATED: lenient success condition] cqa1 V-C code uses
pi0.5|libero_10|random|0.085|0.418|no|eval_pi05_random_k085_long_seed43_postfix|cqa1-33015|
pi0.5|libero_10|random|0.085|0.444|no|eval_pi05_random_k085_long_seed42|cqa1-33015|
pi0.5|libero_10|random|0.085|49.4|no|eval_pi05_random_k085_long_seed42_postfix_v3|cqa1-33015|
pi0.5|libero_10|random|0.085|42.0|no|eval_pi05_random_k085_long_seed43_v2|cqa1-33015|
pi0.5|libero_10|random|0.085|0.424|yes|eval_pi05_random_k085_long_seed43_v3|westd-41074|
pi0.5|libero_10|random|0.09|32.0|yes|eval_pi05_random_k09_long_seed42_postfix|westd-41074|Cron 误报失败（日志文件名不匹配：cron 监控 random_k09_long_seed42.log，实际写入 r
pi0.5|libero_10|random|0.09|0.318|yes|eval_pi05_random_k09_long_seed42|westd-38929|
pi0.5|libero_10|random|0.0925|38.6|no|eval_pi05_random_k0925_long_seed42_postfix|cqa1-33015|
pi0.5|libero_10|random|0.095|0.584|no|eval_pi05_random_k095_long_seed43_postfix|cqa1-33015|
pi0.5|libero_10|random|0.3|28.4|yes|eval_pi05_random_k03_long_seed43_v3|westd-38929|
pi0.5|libero_10|random|0.5|46.8|yes|eval_pi05_random_k05_long_seed42_postfix|westd-38929|
pi0.5|libero_10|random|0.5|46.8|yes|eval_pi05_random_k05_long_seed42_v2|westd-41074|
pi0.5|libero_10|random|0.5|51.2|yes|eval_pi05_random_k05_long_seed43_v2|westd-41074|
pi0.5|libero_10|random|0.7|62.4|no|eval_pi05_random_k07_long_seed42|cqa1-33015|[CONTAMINATED: lenient success condition] cqa1 V-C code uses
pi0.5|libero_10|random|0.7|65.8|yes|eval_pi05_random_k07_long_seed42_postfix|westd-38929|
pi0.5|libero_10|random|0.85|45.2|yes|eval_pi05_random_k085_long_seed42_postfix|westd-41074|
pi0.5|libero_10|random|0.85|41.8|yes|eval_pi05_random_k085_long_seed43|westd-41074|
pi0.5|libero_10|random|0.95|63.2|yes|eval_pi05_random_k095_long_seed42_postfix|westd-41074|
pi0.5|libero_10|random|0.95|0.612|yes|eval_pi05_random_k095_long_seed42|westd-38929|
pi0.5|libero_goal|attention|0.05|0.722|yes|eval_pi05_attention_k05_goal_seed43|westd-41074|Attention k=0.5 Goal seed43=72.2%; seed42=70.2%; mean=71.2%.
pi0.5|libero_goal|attention|0.05|70.2|yes|eval_pi05_attention_k05_goal_seed42|westd-41074|
pi0.5|libero_goal|l2norm|0.03|0.518|yes|eval_pi05_l2norm_k03_goal_seed42_postfix|westd-38929|
pi0.5|libero_goal|l2norm|0.03|50.6|no|eval_pi05_l2norm_k03_goal_seed42_v2|cqa1-33015|
pi0.5|libero_goal|l2norm|0.05|59.8|yes|eval_pi05_l2norm_k05_goal_seed42_postfix|westd-41074|
pi0.5|libero_goal|l2norm|0.05|0.592|yes|eval_pi05_l2norm_k05_goal_seed42|westd-41074|
pi0.5|libero_goal|l2norm|0.07|70.2|yes|eval_pi05_l2norm_k07_goal_seed42_postfix|westd-41074|
pi0.5|libero_goal|l2norm|0.07|72.2|yes|eval_pi05_l2norm_k07_goal_seed43_v2|westd-41074|
pi0.5|libero_goal|l2norm|0.07|73.6|no|eval_pi05_l2norm_k07_goal_seed42_v2|cqa1-33015|
pi0.5|libero_goal|l2norm|0.085|87.4|yes|eval_pi05_l2norm_k085_goal_seed42_postfix|westd-41074|
pi0.5|libero_goal|l2norm|0.085|87.0|no|eval_pi05_l2norm_k085_goal_seed43|cqa1-33015|
pi0.5|libero_goal|l2norm|0.09|91.0|yes|eval_pi05_l2norm_k09_goal_seed43_postfix|westd-41074|
pi0.5|libero_goal|l2norm|0.09|88.6|yes|eval_pi05_l2norm_k09_goal_seed42_postfix|westd-41074|
pi0.5|libero_goal|l2norm|0.09|90.6|no|eval_pi05_l2norm_k09_goal_seed42_v2|cqa1-33015|
pi0.5|libero_goal|l2norm|0.09|0.9|yes|eval_pi05_l2norm_k09_goal_seed42|westd-38929|
pi0.5|libero_goal|l2norm|0.0925|89.8|yes|eval_pi05_l2norm_k0925_goal_seed42_postfix|westd-38929|
pi0.5|libero_goal|l2norm|0.0925|89.8|yes|eval_pi05_l2norm_k0925_goal_seed42_v3|westd-41074|
pi0.5|libero_goal|l2norm|0.0925|90.8|yes|eval_pi05_l2norm_k0925_goal_seed43|westd-41074|
pi0.5|libero_goal|l2norm|0.0925|89.0|yes|eval_pi05_l2norm_k0925_goal_seed42_v2|westd-41074|
pi0.5|libero_goal|l2norm|0.095|90.8|no|eval_pi05_l2norm_k095_goal_seed42_postfix|cqa1-33015|
pi0.5|libero_goal|l2norm|0.095|0.908|no|eval_pi05_l2norm_k095_goal_seed42|cqa1-33015|
pi0.5|libero_goal|l2norm|0.095|89.4|no|eval_pi05_l2norm_k095_goal_seed42_v2|cqa1-33015|
pi0.5|libero_goal|l2norm|0.3|0.542|no|eval_pi05_l2norm_k03_goal_seed42|cqa1-33015|
pi0.5|libero_goal|l2norm|0.85|87.0|no|eval_pi05_l2norm_k085_goal_seed43_postfix|cqa1-33015|
pi0.5|libero_goal|l2norm|0.85|88.0|no|eval_pi05_l2norm_k085_goal_seed42|cqa1-33015|
pi0.5|libero_goal|random|0.03|52.8|yes|eval_pi05_random_k03_goal_seed42_postfix|westd-41074|
pi0.5|libero_goal|random|0.03|53.6|no|eval_pi05_random_k03_goal_seed43_v2|cqa1-33015|
pi0.5|libero_goal|random|0.03|0.51|no|eval_pi05_random_k03_goal_seed42|cqa1-33015|
pi0.5|libero_goal|random|0.03|50.6|yes|eval_pi05_random_k03_goal_seed42_v2|westd-41074|
pi0.5|libero_goal|random|0.05|73.6|no|eval_pi05_random_k05_goal_seed42_postfix|cqa1-33015|
pi0.5|libero_goal|random|0.05|73.6|no|eval_pi05_random_k05_goal_seed42_v2|cqa1-33015|
pi0.5|libero_goal|random|0.07|75.6|yes|eval_pi05_random_k07_goal_seed42_postfix|westd-38929|
pi0.5|libero_goal|random|0.07|78.2|yes|eval_pi05_random_k07_goal_seed42_v2|westd-41074|
pi0.5|libero_goal|random|0.07|0.806|no|eval_pi05_random_k07_goal_seed42|cqa1-33015|
pi0.5|libero_goal|random|0.085|53.0|no|eval_pi05_random_k085_goal_seed42_postfix_v3|cqa1-33015|
pi0.5|libero_goal|random|0.085|0.534|yes|eval_pi05_random_k085_goal_seed43_postfix|westd-41074|
pi0.5|libero_goal|random|0.085|52.8|yes|eval_pi05_random_k085_goal_seed42_postfix|westd-38929|
pi0.5|libero_goal|random|0.085|52.4|no|eval_pi05_random_k085_goal_seed42_v4|cqa1-33015|
pi0.5|libero_goal|random|0.085|0.524|yes|eval_pi05_random_k085_goal_seed42_v3|westd-38929|
pi0.5|libero_goal|random|0.09|61.2|yes|eval_pi05_random_k09_goal_seed43_postfix|westd-41074|
pi0.5|libero_goal|random|0.09|61.8|yes|eval_pi05_random_k09_goal_seed42_postfix|westd-38929|
pi0.5|libero_goal|random|0.09|62.2|yes|eval_pi05_random_k09_goal_seed42_v2|westd-41074|
pi0.5|libero_goal|random|0.0925|70.0|yes|eval_pi05_random_k0925_goal_seed42_v3|westd-41074|
pi0.5|libero_goal|random|0.0925|71.2|yes|eval_pi05_random_k0925_goal_seed42_v2|westd-41074|
pi0.5|libero_goal|random|0.095|82.6|yes|eval_pi05_random_k095_goal_seed42_postfix|westd-38929|
pi0.5|libero_goal|random|0.095|83.8|yes|eval_pi05_random_k095_goal_seed42_v2|westd-41074|
pi0.5|libero_goal|random|0.85|0.522|yes|eval_pi05_random_k085_goal_seed43|westd-41074|
pi0.5|libero_goal|random|0.95|0.834|yes|eval_pi05_random_k095_goal_seed43|westd-41074|
pi0.5|libero_object|attention|0.05|0.378|yes|eval_pi05_attention_k05_object_seed42|westd-41074|
pi0.5|libero_object|attention|0.085|0.922|yes|eval_pi05_attention_k085_object_seed42|westd-41074|
pi0.5|libero_object|attention|0.09|0.972|yes|eval_pi05_attention_k09_object_seed42|westd-41074|
pi0.5|libero_object|attention|0.095|0.984|yes|eval_pi05_attention_k095_object_seed42|westd-41074|
pi0.5|libero_object|attention|0.7|0.006|yes|eval_pi05_attention_k07_object_seed42|westd-41074|
pi0.5|libero_object|l2norm|0.01|0.026|yes|eval_pi05_l2norm_k01_object_seed42|westd-41074|
pi0.5|libero_object|l2norm|0.03|0.51|yes|eval_pi05_l2norm_k03_object_seed42|westd-41074|
pi0.5|libero_object|l2norm|0.05|0.336|yes|eval_pi05_l2norm_k05_object_seed43|westd-41074|
pi0.5|libero_object|l2norm|0.07|56.4|yes|eval_pi05_l2norm_k07_object_seed42_postfix|westd-38929|
pi0.5|libero_object|l2norm|0.07|56.4|yes|eval_pi05_l2norm_k07_object_seed43|westd-41074|
pi0.5|libero_object|l2norm|0.07|55.0|yes|eval_pi05_l2norm_k07_object_seed42|westd-41074|
pi0.5|libero_object|l2norm|0.085|98.4|no|eval_pi05_l2norm_k085_object_seed42_postfix_v2|cqa1-33015|
pi0.5|libero_object|l2norm|0.085|0.984|yes|eval_pi05_l2norm_k085_object_seed43|westd-41074|
pi0.5|libero_object|l2norm|0.085|0.98|yes|eval_pi05_l2norm_k085_object_seed42_v4|westd-41074|
pi0.5|libero_object|l2norm|0.09|0.994|no|eval_pi05_zeromask_l2norm_k09_object_seed42|cqa1-33015|
pi0.5|libero_object|l2norm|0.09|98.4|yes|eval_pi05_l2norm_k09_object_seed43_postfix|westd-41074|
pi0.5|libero_object|l2norm|0.09|98.2|yes|eval_pi05_l2norm_k09_object_seed42_v2|westd-41074|
pi0.5|libero_object|l2norm|0.0925|99.2|yes|eval_pi05_l2norm_k0925_object_seed42||
pi0.5|libero_object|l2norm|0.095|98.2|yes|eval_pi05_l2norm_k095_object_seed42_v2|westd-41074|
pi0.5|libero_object|l2norm|0.095|0.984|no|eval_pi05_l2norm_k095_object_seed43|cqa1-33015|
pi0.5|libero_object|l2norm|0.5|33.4|yes|eval_pi05_l2norm_k05_object_seed42|westd-41074|
pi0.5|libero_object|l2norm|0.85|99.0|no|eval_pi05_l2norm_k085_object_seed43_postfix|cqa1-33015|
pi0.5|libero_object|random|0.03|0.322|yes|eval_pi05_random_k03_object_seed43_v4|westd-38929|
pi0.5|libero_object|random|0.03|0.364|yes|eval_pi05_random_k03_object_seed42|westd-41074|
pi0.5|libero_object|random|0.05|0.682|no|eval_pi05_random_k05_object_seed42_v2|cqa1-33015|
pi0.5|libero_object|random|0.05|68.4|yes|eval_pi05_random_k05_object_seed43|westd-41074|
pi0.5|libero_object|random|0.05|0.694|yes|eval_pi05_random_k05_object_seed42|westd-41074|Original PID 899206 crashed (Network unreachable; tokenizer 
pi0.5|libero_object|random|0.07|74.0|no|eval_pi05_random_k07_object_seed42_v4|cqa1-33015|
pi0.5|libero_object|random|0.07|0.74|yes|eval_pi05_random_k07_object_seed42_v3||
pi0.5|libero_object|random|0.07|73.8|yes|eval_pi05_random_k07_object_seed43|westd-41074|
pi0.5|libero_object|random|0.07|0.772|yes|eval_pi05_random_k07_object_seed42|westd-41074|
pi0.5|libero_object|random|0.085|5.6|yes|eval_pi05_random_k085_object_seed42_postfix|westd-41074|
pi0.5|libero_object|random|0.085|0.048|no|eval_pi05_random_k085_object_seed43_postfix|cqa1-33015|
pi0.5|libero_object|random|0.085|0.038|yes|eval_pi05_random_k085_object_seed43|westd-41074|
pi0.5|libero_object|random|0.085|5.0|yes|eval_pi05_random_k085_object_seed42_v2|westd-38929|
pi0.5|libero_object|random|0.09|0.98|yes|eval_pi05_zeromask_random_k09_object_seed42_v3|westd-41074|
pi0.5|libero_object|random|0.09|7.4|yes|eval_pi05_random_k09_object_seed43_postfix|westd-41074|
pi0.5|libero_object|random|0.09|0.09|no|eval_pi05_random_k09_object_seed42_v2|cqa1-33015|Post-fix 重跑完成: 9.0% (45/500)，与 pre-fix v2 结果一致。CRON 误报 faile
pi0.5|libero_object|random|0.09|0.096|yes|eval_pi05_random_k09_object_seed43|westd-41074|
pi0.5|libero_object|random|0.09|9.6|yes|eval_pi05_random_k09_object_seed43_v3|westd-27271|
pi0.5|libero_object|random|0.09|0.17|yes|eval_pi05_random_k09_fixedmask_object_seed42_v2||
pi0.5|libero_object|random|0.0925|27.2|yes|eval_pi05_random_k0925_object_seed42_postfix|westd-41074|
pi0.5|libero_object|random|0.0925|0.3|yes|eval_pi05_random_k0925_object_seed43|westd-38929|
pi0.5|libero_object|random|0.0925|0.276|yes|eval_pi05_random_k0925_object_seed42|westd-41074|
pi0.5|libero_object|random|0.095|74.0|yes|eval_pi05_random_k095_object_seed42_v2||
pi0.5|libero_object|random|0.095|0.728|yes|eval_pi05_random_k095_object_seed43|westd-41074|
pi0.5|libero_object|random|0.9|9.6|yes|eval_pi05_random_k09_object_seed43_v4|westd-41074|
pi0.5|libero_spatial|attention|0.05|0.726|yes|eval_pi05_attention_k05_spatial_seed42|westd-41074|
pi0.5|libero_spatial|l2norm|0.03|0.52|yes|eval_pi05_l2norm_k03_spatial_seed43|westd-38929|
pi0.5|libero_spatial|l2norm|0.03|57.2|yes|eval_pi05_l2norm_k03_spatial_seed42|westd-38929|
pi0.5|libero_spatial|l2norm|0.05|0.574|no|eval_pi05_l2norm_k05_spatial_seed42_postfix|cqa1-33015|
pi0.5|libero_spatial|l2norm|0.05|0.554|yes|eval_pi05_l2norm_k05_spatial_seed43_v2|westd-41074|
pi0.5|libero_spatial|l2norm|0.05|0.582|yes|eval_pi05_l2norm_k05_spatial_seed43|westd-41074|
pi0.5|libero_spatial|l2norm|0.05|55.6|yes|eval_pi05_l2norm_k05_spatial_seed42|westd-38929|
pi0.5|libero_spatial|l2norm|0.07|0.684|yes|eval_pi05_l2norm_k07_spatial_seed43|westd-27271|
pi0.5|libero_spatial|l2norm|0.07|67.0|yes|eval_pi05_l2norm_k07_spatial_seed42|westd-38929|
pi0.5|libero_spatial|l2norm|0.085|0.882|no|eval_pi05_l2norm_k085_spatial_seed43_postfix|cqa1-33015|
pi0.5|libero_spatial|l2norm|0.085|88.4|yes|eval_pi05_l2norm_k085_spatial_seed42_v3|westd-41074|
pi0.5|libero_spatial|l2norm|0.085|88.6|yes|eval_pi05_l2norm_k085_spatial_seed42_v2|westd-41074|
pi0.5|libero_spatial|l2norm|0.085|0.88|yes|eval_pi05_l2norm_k085_spatial_seed43|westd-27271|
pi0.5|libero_spatial|l2norm|0.09|96.2|yes|eval_pi05_l2norm_k09_spatial_seed43_postfix|westd-38929|
pi0.5|libero_spatial|l2norm|0.09|96.0|yes|eval_pi05_l2norm_k09_spatial_seed42_postfix|westd-38929|
pi0.5|libero_spatial|l2norm|0.09|0.956|no|eval_pi05_l2norm_k09_spatial_seed43|cqa1-33015|
pi0.5|libero_spatial|l2norm|0.0925|0.97|no|eval_pi05_l2norm_k0925_spatial_seed42|cqa1-33015|
pi0.5|libero_spatial|l2norm|0.095|0.98|no|eval_pi05_l2norm_k095_spatial_seed43|cqa1-33015|
pi0.5|libero_spatial|l2norm|0.095|0.978|yes|eval_pi05_l2norm_k095_spatial_seed42|westd-38929|
pi0.5|libero_spatial|l2norm|0.3|52.8|no|eval_pi05_l2norm_k03_spatial_seed42_postfix|cqa1-33015|
pi0.5|libero_spatial|random|0.03|43.4|no|eval_pi05_random_k03_spatial_seed42_postfix_v2|cqa1-33015|
pi0.5|libero_spatial|random|0.03|0.512|yes|eval_pi05_random_k03_spatial_seed43|westd-38929|
pi0.5|libero_spatial|random|0.03|49.6|yes|eval_pi05_random_k03_spatial_seed42|westd-38929|
pi0.5|libero_spatial|random|0.05|0.718|no|eval_pi05_random_k05_spatial_seed42_postfix_v3|cqa1-33015|
pi0.5|libero_spatial|random|0.05|71.6|yes|eval_pi05_random_k05_spatial_seed42||
pi0.5|libero_spatial|random|0.05|72.4|yes|eval_pi05_random_k05_spatial_seed43_v2|westd-41074|
pi0.5|libero_spatial|random|0.07|73.8|no|eval_pi05_random_k07_spatial_seed42_postfix|cqa1-33015|
pi0.5|libero_spatial|random|0.07|0.738|yes|eval_pi05_random_k07_spatial_seed43|westd-27271|
pi0.5|libero_spatial|random|0.07|74.4|yes|eval_pi05_random_k07_spatial_seed42|westd-38929|
pi0.5|libero_spatial|random|0.085|59.2|no|eval_pi05_random_k085_spatial_seed43_postfix|cqa1-33015|
pi0.5|libero_spatial|random|0.085|60.2|yes|eval_pi05_random_k085_spatial_seed42_v3|westd-41074|
pi0.5|libero_spatial|random|0.085|60.8|no|eval_pi05_random_k085_spatial_seed42_postfix_v2|cqa1-33015|
pi0.5|libero_spatial|random|0.085|56.6|yes|eval_pi05_random_k085_spatial_seed42_v2|westd-41074|
pi0.5|libero_spatial|random|0.085|0.584|yes|eval_pi05_random_k085_spatial_seed42|westd-41074|
pi0.5|libero_spatial|random|0.085|0.576|yes|eval_pi05_random_k085_spatial_seed43|westd-38929|
pi0.5|libero_spatial|random|0.09|54.0|yes|eval_pi05_random_k09_spatial_seed43_postfix_v2|westd-41074|
pi0.5|libero_spatial|random|0.09|53.4|no|eval_pi05_random_k09_spatial_seed42_postfix_v2|cqa1-33015|
pi0.5|libero_spatial|random|0.09|0.536|no|eval_pi05_random_k09_spatial_seed43|cqa1-33015|
pi0.5|libero_spatial|random|0.0925|58.2|yes|eval_pi05_random_k0925_spatial_seed42_unreg|westd-41074|
pi0.5|libero_spatial|random|0.0925|0.578|no|eval_pi05_random_k0925_spatial_seed43|cqa1-33015|
pi0.5|libero_spatial|random|0.095|76.8|no|eval_pi05_random_k095_spatial_seed42_postfix_v2|cqa1-33015|
pi0.5|libero_spatial|random|0.095|0.768|yes|eval_pi05_random_k095_spatial_seed43|westd-27271|
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "076e70a6-b6da-4158-a720-52786daa428f",
  "uuid": "10961954-9db9-4c83-8441-6b6b77fa7ab1",
  "tool_use_result": {
    "stdout": "Total rows: 273\n\nOpenVLA|libero_10|attention|0.07|24.0|yes|eval_openvla_attn_k07_long_seed42_v2|westd-38929|\nOpenVLA|libero_10|attention|0.075|37.4|yes|eval_openvla_attn_k075_long_seed42|westd-41074|[PARTIAL: 430/500 episodes] timeout EXIT_CODE=124 on westd-4\nOpenVLA|libero_10|attention|0.085|45.8|yes|eval_openvla_attn_k085_long_seed42_v5|westd-38929|\nOpenVLA|libero_10|attention|0.09|44.0|yes|eval_openvla_attn_k09_long_seed42_v3|westd-38929|\nOpenVLA|libero_10|attention|0.5|14.6|yes|eval_openvla_attn_k05_long_seed42|westd-27271|\nOpenVLA|libero_10|l2norm|0.07|0.312|yes|eval_openvla_l2norm_k07_long_seed42_v2|westd-38929|\nOpenVLA|libero_10|l2norm|0.085|0.388|yes|eval_openvla_l2norm_k085_long_seed42_v2|westd-38929|\nOpenVLA|libero_10|l2norm|0.09|43.6|yes|eval_openvla_l2norm_k09_long_seed42_v3|westd-38929|\nOpenVLA|libero_10|random|0.05|18.6|yes|eval_openvla_random_k05_long_seed42_v2|westd-38929|\nOpenVLA|libero_10|random|0.07|0.388|yes|eval_openvla_random_k07_long_seed42_v2|westd-38929|\nOpenVLA|libero_10|random|0.085|0.45|yes|eval_openvla_random_k085_long_seed42_v3|westd-38929|\nOpenVLA|libero_10|random|0.09|46.8|yes|eval_openvla_random_k09_long_seed42_v3|westd-38929|\nOpenVLA|libero_goal|attention|0.05|44.2|yes|eval_openvla_attn_k05_goal_seed42|westd-27271|\nOpenVLA|libero_goal|attention|0.07|0.664|yes|eval_openvla_attn_k07_goal_seed42|westd-38929|\nOpenVLA|libero_goal|attention|0.085|74.6|yes|eval_openvla_attn_k085_goal_seed42_v3|westd-38929|\nOpenVLA|libero_goal|attention|0.09|73.2|yes|eval_openvla_attn_k09_goal_seed43_v4|westd-27271|\nOpenVLA|libero_goal|attention|0.09|0.732|yes|eval_openvla_attn_k09_goal_seed42|westd-27271|\nOpenVLA|libero_goal|attention|0.75|67.4|yes|eval_openvla_attn_k075_goal_seed42|westd-27271|\nOpenVLA|libero_goal|l2norm|0.05|0.434|yes|eval_openvla_l2norm_k05_goal_seed42|westd-41074|\nOpenVLA|libero_goal|l2norm|0.05|0.434|yes|eval_openvla_l2norm_k05_goal_seed42_v3|westd-27271|\nOpenVLA|libero_goal|l2norm|0.07|0.684|yes|eval_openvla_l2norm_k07_goal_seed42|westd-27271|\nOpenVLA|libero_goal|l2norm|0.075|70.2|yes|eval_openvla_l2norm_k075_goal_seed42_v2|westd-27271|\nOpenVLA|libero_goal|l2norm|0.085|75.4|yes|eval_openvla_l2norm_k085_goal_seed42|westd-27271|\nOpenVLA|libero_goal|l2norm|0.09|75.2|yes|eval_openvla_l2norm_k09_goal_seed43|westd-27271|\nOpenVLA|libero_goal|l2norm|0.09|0.752|yes|eval_openvla_l2norm_k09_goal_seed43_v3|westd-27271|\nOpenVLA|libero_goal|l2norm|0.09|0.748|yes|eval_openvla_l2norm_k09_goal_seed42|westd-27271|\nOpenVLA|libero_goal|random|0.05|0.522|yes|eval_openvla_random_k05_goal_seed42|westd-27271|\nOpenVLA|libero_goal|random|0.05|0.522|yes|eval_openvla_random_k05_goal_seed42_v2|westd-27271|失败原因: 进程在 Task 2/10 开头无错误退出（日志仅 21 行，无 Traceback/OOM）。v2 使用了\nOpenVLA|libero_goal|random|0.07|68.4|yes|eval_openvla_random_k07_goal_seed42_v4|westd-27271|\nOpenVLA|libero_goal|random|0.085|78.6|yes|eval_openvla_random_k085_goal_seed42|westd-38929|\nOpenVLA|libero_goal|random|0.09|80.4|yes|eval_openvla_random_k09_goal_seed43|westd-27271|\nOpenVLA|libero_goal|random|0.09|79.6|yes|eval_openvla_random_k09_goal_seed42||\nOpenVLA|libero_goal|random|0.75|72.0|yes|eval_openvla_random_k075_goal_seed42|westd-38929|False alarm: 实验无 spec（可能未正确启动或 cqa1 代码修复前部署的无效实验）。Random k=0\nOpenVLA|libero_object||0.03|0.206|yes|eval_openvla_pruning_k03_restart|westd-27271|\nOpenVLA|libero_object||0.07|0.49|yes|eval_openvla_pruning_k07|westd-27271|\nOpenVLA|libero_object||0.095|69.4|yes|eval_openvla_prune_k095|westd-27271|\nOpenVLA|libero_object|attention|0.07|43.8|yes|eval_openvla_attn_k07_object_seed42_v3|westd-41074|\nOpenVLA|libero_object|attention|0.075|53.2|yes|eval_openvla_attn_k075_object_seed42|westd-41074|\nOpenVLA|libero_object|attention|0.085|0.55|yes|eval_openvla_attn_k085_object_seed42|westd-38929|\nOpenVLA|libero_object|l2norm|0.03|25.0|yes|eval_openvla_l2norm_k03_object_seed43|westd-38929|\nOpenVLA|libero_object|l2norm|0.03|25.0|yes|eval_openvla_l2norm_k03_object_seed42|westd-38929|\nOpenVLA|libero_object|l2norm|0.03|0.25|yes|eval_openvla_prune_l2norm_k03|westd-38929|\nOpenVLA|libero_object|l2norm|0.03|0.25|yes|eval_openvla_prune_l2norm_k03_seed42|westd-38929|[D124] Registered from westd-38929 eval_results.\nOpenVLA|libero_object|l2norm|0.05|0.392|yes|eval_openvla_l2norm_k05_object_seed42_v4|westd-41074|\nOpenVLA|libero_object|l2norm|0.05|0.392|yes|eval_openvla_l2norm_k05_object_seed42_v5|westd-38929|\nOpenVLA|libero_object|l2norm|0.05|39.2|yes|eval_openvla_l2norm_k05_object_seed43|westd-27271|\nOpenVLA|libero_object|l2norm|0.05|39.2|yes|eval_openvla_l2norm_k05_object_seed42|westd-38929|失败原因: process dead 5× with no sentinel/W&B — 与 westd-38929 上\nOpenVLA|libero_object|l2norm|0.05|0.392|yes|eval_openvla_prune_l2norm_k05|westd-38929|\nOpenVLA|libero_object|l2norm|0.05|0.392|yes|eval_openvla_prune_l2norm_k05_seed42|westd-38929|[D124] Registered from westd-38929 eval_results.\nOpenVLA|libero_object|l2norm|0.07|0.498|yes|eval_openvla_l2norm_k07_object_seed42_v3|westd-38929|\nOpenVLA|libero_object|l2norm|0.07|0.498|yes|eval_openvla_l2norm_k07_object_seed42_v2|westd-38929|Cron 误判 failed。日志显示实验完成: Overall SR 49.8% (249/500)。结果文件: /r\nOpenVLA|libero_object|l2norm|0.07|49.8|yes|eval_openvla_prune_l2norm_k07_seed43_v2|westd-27271|\nOpenVLA|libero_object|l2norm|0.075|0.574|yes|eval_openvla_l2norm_k075_object_seed42|westd-41074|\nOpenVLA|libero_object|l2norm|0.09|0.688|yes|eval_openvla_zeromask_l2norm_k09_object_seed42|westd-41074|\nOpenVLA|libero_object|l2norm|0.09|0.706|yes|eval_openvla_l2norm_k09_object_seed42|westd-27271|\nOpenVLA|libero_object|l2norm|0.09|0.706|yes|eval_openvla_prune_l2norm_k09|westd-38929|\nOpenVLA|libero_object|l2norm|0.09|0.706|yes|eval_openvla_prune_l2norm_k09_seed42|westd-38929|[D124] Registered from westd-38929 eval_results.\nOpenVLA|libero_object|l2norm|0.095|0.706|yes|eval_openvla_prune_l2norm_k095|westd-38929|\nOpenVLA|libero_object|l2norm|0.095|0.706|yes|eval_openvla_prune_l2norm_k095_seed42|westd-38929|[D124] Registered from westd-38929 eval_results.\nOpenVLA|libero_object|random|0.03|0.214|yes|eval_openvla_random_k03_object_seed42_v2|westd-38929|\nOpenVLA|libero_object|random|0.05|35.8|yes|eval_openvla_random_k05_object_seed42_v3|westd-41074|\nOpenVLA|libero_object|random|0.05|35.8|yes|eval_openvla_prune_random_k05_seed42|westd-41074|Confirmed running on westd-41074:cuda:0; PID 659206\nOpenVLA|libero_object|random|0.05|0.356|yes|eval_openvla_prune_random_k05_seed43_v2|westd-41074|\nOpenVLA|libero_object|random|0.07|0.444|yes|eval_openvla_random_k07_object_seed42_v2|westd-38929|Cron 误判 process gone。日志显示实验完成: Overall SR 44.4% (222/500)。结果\nOpenVLA|libero_object|random|0.07|0.526|yes|eval_openvla_random_k07_object_seed43|westd-38929|\nOpenVLA|libero_object|random|0.07|0.526|yes|eval_openvla_prune_random_k07_seed43_v2|westd-41074|\nOpenVLA|libero_object|random|0.09|0.718|yes|eval_openvla_zeromask_random_k09_object_seed42|westd-41074|\nOpenVLA|libero_object|random|0.09|0.646|yes|eval_openvla_prune_random_k09_seed42|westd-41074|\nOpenVLA|libero_object|random|0.09|0.622|yes|eval_openvla_prune_random_k09_seed43|westd-27271|\nOpenVLA|libero_object|random|0.095|0.668|yes|eval_openvla_prune_random_k095_seed43|westd-41074|\nOpenVLA|libero_object|random|0.95|67.4|yes|eval_openvla_random_k095_object_seed42||\nOpenVLA|libero_spatial|attention|0.09|0.804|yes|eval_openvla_attn_k09_spatial_seed42|westd-27271|\nOpenVLA|libero_spatial|l2norm|0.09|0.75|yes|eval_openvla_l2norm_k09_spatial_seed42|westd-27271|\nOpenVLA|libero_spatial|random|0.05|0.5|yes|eval_openvla_random_k05_spatial_seed42|westd-27271|\nOpenVLA|libero_spatial|random|0.09|79.8|yes|eval_openvla_random_k09_spatial_seed42|westd-41074|\npi0.5|libero_10|attention|0.05|49.8|no|eval_pi05_attention_k05_long_seed42_v2|cqa1-33015|[CONTAMINATED: lenient success condition] cqa1 V-C code uses\npi0.5|libero_10|attention|0.075|52.4|no|eval_pi05_attention_k075_long_seed42_v2|cqa1-33015|[CONTAMINATED: lenient success condition] cqa1 V-C code uses\npi0.5|libero_10|attention|0.075|51.8|no|eval_pi05_attention_k075_long_seed42|cqa1-33015|\npi0.5|libero_10|attention|0.085|51.6|no|eval_pi05_attention_k085_long_seed42_v2|cqa1-33015|[CONTAMINATED: lenient success condition] cqa1 V-C code uses\npi0.5|libero_10|attention|0.09|0.638|no|eval_pi05_attention_k09_long_seed42_postfix|cqa1-33015|\npi0.5|libero_10|attention|0.095|77.0|no|eval_pi05_attn_k095_long_seed42|cqa1-33015|\npi0.5|libero_10|attention|0.7|50.8|no|eval_pi05_attention_k07_long_seed42_v2|cqa1-33015|[CONTAMINATED: lenient success condition] cqa1 V-C code uses\npi0.5|libero_10|l2norm|0.03|39.2|yes|eval_pi05_l2norm_k03_long_seed43_postfix_v2|westd-38929|\npi0.5|libero_10|l2norm|0.05|50.0|no|eval_pi05_l2norm_k05_long_seed42_v4|cqa1-33015|[CONTAMINATED: lenient success condition] cqa1 V-C code uses\npi0.5|libero_10|l2norm|0.05|0.502|no|eval_pi05_l2norm_k05_long_seed42|cqa1-33015|\npi0.5|libero_10|l2norm|0.05|0.53|no|eval_pi05_l2norm_k05_long_seed43_postfix_v2|cqa1-33015|\npi0.5|libero_10|l2norm|0.05|51.4|yes|eval_pi05_l2norm_k05_long_seed42_v3|westd-41074|\npi0.5|libero_10|l2norm|0.07|0.65|no|eval_pi05_l2norm_k07_long_seed43_v3|cqa1-33015|\npi0.5|libero_10|l2norm|0.07|62.6|yes|eval_pi05_l2norm_k07_long_seed42_postfix|westd-27271|\npi0.5|libero_10|l2norm|0.07|0.654|yes|eval_pi05_l2norm_k07_long_seed43_v4|westd-41074|\npi0.5|libero_10|l2norm|0.075|73.4|no|eval_pi05_l2norm_k075_long_seed42|cqa1-33015|\npi0.5|libero_10|l2norm|0.085|78.8|yes|eval_pi05_l2norm_k085_long_seed42_v3||\npi0.5|libero_10|l2norm|0.085|80.0|no|eval_pi05_l2norm_k085_long_seed43_v3|cqa1-33015|\npi0.5|libero_10|l2norm|0.085|0.78|no|eval_pi05_l2norm_k085_long_seed42_postfix_v3|cqa1-33015|\npi0.5|libero_10|l2norm|0.085|78.6|yes|eval_pi05_l2norm_k085_long_seed43_postfix|westd-41074|\npi0.5|libero_10|l2norm|0.085|78.4|yes|eval_pi05_l2norm_k085_long_seed42_postfix|westd-41074|\npi0.5|libero_10|l2norm|0.085|0.77|yes|eval_pi05_l2norm_k085_long_seed43_v4|westd-41074|\npi0.5|libero_10|l2norm|0.09|0.808|no|eval_pi05_l2norm_k09_long_seed43_postfix|cqa1-33015|\npi0.5|libero_10|l2norm|0.09|80.0|no|eval_pi05_l2norm_k09_long_seed42_postfix_v2|cqa1-33015|\npi0.5|libero_10|l2norm|0.09|80.0|yes|eval_pi05_l2norm_k09_long_seed43_postfix_v2|westd-41074|\npi0.5|libero_10|l2norm|0.09|0.81|yes|eval_pi05_l2norm_k09_long_seed42|westd-41074|\npi0.5|libero_10|l2norm|0.0925|0.832|no|eval_pi05_l2norm_k0925_long_seed42_v2|cqa1-33015|\npi0.5|libero_10|l2norm|0.095|87.4|yes|eval_pi05_l2norm_k095_long_seed43_postfix|westd-38929|\npi0.5|libero_10|l2norm|0.7|65.8|yes|eval_pi05_l2norm_k07_long_seed43_v2|westd-38929|\npi0.5|libero_10|l2norm|0.85|77.8|no|eval_pi05_l2norm_k085_long_seed42_v4|cqa1-33015|[CONTAMINATED: lenient success condition] cqa1 V-C code uses\npi0.5|libero_10|l2norm|0.85|79.0|yes|eval_pi05_l2norm_k085_long_seed43_v2|westd-38929|\npi0.5|libero_10|l2norm|0.95|87.0|yes|eval_pi05_l2norm_k095_long_seed42_postfix|westd-38929|\npi0.5|libero_10|random|0.03|0.272|no|eval_pi05_random_k03_long_seed43_v4|cqa1-33015|\npi0.5|libero_10|random|0.03|29.6|yes|eval_pi05_random_k03_long_seed42_postfix|westd-38929|\npi0.5|libero_10|random|0.03|28.0|yes|eval_pi05_random_k03_long_seed43_v2|westd-41074|\npi0.5|libero_10|random|0.03|0.29|yes|eval_pi05_random_k03_long_seed42|westd-38929|\npi0.5|libero_10|random|0.05|50.2|no|eval_pi05_random_k05_long_seed42_v3|cqa1-33015|[CONTAMINATED: lenient success condition] cqa1 V-C code uses\npi0.5|libero_10|random|0.05|0.502|no|eval_pi05_random_k05_long_seed42|cqa1-33015|\npi0.5|libero_10|random|0.05|46.8|no|eval_pi05_random_k05_long_seed43_postfix|cqa1-33015|\npi0.5|libero_10|random|0.07|0.686|no|eval_pi05_random_k07_long_seed43_postfix|cqa1-33015|\npi0.5|libero_10|random|0.075|62.4|no|eval_pi05_random_k075_long_seed42_v2|cqa1-33015|[CONTAMINATED: lenient success condition] cqa1 V-C code uses\npi0.5|libero_10|random|0.085|44.4|no|eval_pi05_random_k085_long_seed42_v2|cqa1-33015|[CONTAMINATED: lenient success condition] cqa1 V-C code uses\npi0.5|libero_10|random|0.085|0.418|no|eval_pi05_random_k085_long_seed43_postfix|cqa1-33015|\npi0.5|libero_10|random|0.085|0.444|no|eval_pi05_random_k085_long_seed42|cqa1-33015|\npi0.5|libero_10|random|0.085|49.4|no|eval_pi05_random_k085_long_seed42_postfix_v3|cqa1-33015|\npi0.5|libero_10|random|0.085|42.0|no|eval_pi05_random_k085_long_seed43_v2|cqa1-33015|\npi0.5|libero_10|random|0.085|0.424|yes|eval_pi05_random_k085_long_seed43_v3|westd-41074|\npi0.5|libero_10|random|0.09|32.0|yes|eval_pi05_random_k09_long_seed42_postfix|westd-41074|Cron 误报失败（日志文件名不匹配：cron 监控 random_k09_long_seed42.log，实际写入 r\npi0.5|libero_10|random|0.09|0.318|yes|eval_pi05_random_k09_long_seed42|westd-38929|\npi0.5|libero_10|random|0.0925|38.6|no|eval_pi05_random_k0925_long_seed42_postfix|cqa1-33015|\npi0.5|libero_10|random|0.095|0.584|no|eval_pi05_random_k095_long_seed43_postfix|cqa1-33015|\npi0.5|libero_10|random|0.3|28.4|yes|eval_pi05_random_k03_long_seed43_v3|westd-38929|\npi0.5|libero_10|random|0.5|46.8|yes|eval_pi05_random_k05_long_seed42_postfix|westd-38929|\npi0.5|libero_10|random|0.5|46.8|yes|eval_pi05_random_k05_long_seed42_v2|westd-41074|\npi0.5|libero_10|random|0.5|51.2|yes|eval_pi05_random_k05_long_seed43_v2|westd-41074|\npi0.5|libero_10|random|0.7|62.4|no|eval_pi05_random_k07_long_seed42|cqa1-33015|[CONTAMINATED: lenient success condition] cqa1 V-C code uses\npi0.5|libero_10|random|0.7|65.8|yes|eval_pi05_random_k07_long_seed42_postfix|westd-38929|\npi0.5|libero_10|random|0.85|45.2|yes|eval_pi05_random_k085_long_seed42_postfix|westd-41074|\npi0.5|libero_10|random|0.85|41.8|yes|eval_pi05_random_k085_long_seed43|westd-41074|\npi0.5|libero_10|random|0.95|63.2|yes|eval_pi05_random_k095_long_seed42_postfix|westd-41074|\npi0.5|libero_10|random|0.95|0.612|yes|eval_pi05_random_k095_long_seed42|westd-38929|\npi0.5|libero_goal|attention|0.05|0.722|yes|eval_pi05_attention_k05_goal_seed43|westd-41074|Attention k=0.5 Goal seed43=72.2%; seed42=70.2%; mean=71.2%.\npi0.5|libero_goal|attention|0.05|70.2|yes|eval_pi05_attention_k05_goal_seed42|westd-41074|\npi0.5|libero_goal|l2norm|0.03|0.518|yes|eval_pi05_l2norm_k03_goal_seed42_postfix|westd-38929|\npi0.5|libero_goal|l2norm|0.03|50.6|no|eval_pi05_l2norm_k03_goal_seed42_v2|cqa1-33015|\npi0.5|libero_goal|l2norm|0.05|59.8|yes|eval_pi05_l2norm_k05_goal_seed42_postfix|westd-41074|\npi0.5|libero_goal|l2norm|0.05|0.592|yes|eval_pi05_l2norm_k05_goal_seed42|westd-41074|\npi0.5|libero_goal|l2norm|0.07|70.2|yes|eval_pi05_l2norm_k07_goal_seed42_postfix|westd-41074|\npi0.5|libero_goal|l2norm|0.07|72.2|yes|eval_pi05_l2norm_k07_goal_seed43_v2|westd-41074|\npi0.5|libero_goal|l2norm|0.07|73.6|no|eval_pi05_l2norm_k07_goal_seed42_v2|cqa1-33015|\npi0.5|libero_goal|l2norm|0.085|87.4|yes|eval_pi05_l2norm_k085_goal_seed42_postfix|westd-41074|\npi0.5|libero_goal|l2norm|0.085|87.0|no|eval_pi05_l2norm_k085_goal_seed43|cqa1-33015|\npi0.5|libero_goal|l2norm|0.09|91.0|yes|eval_pi05_l2norm_k09_goal_seed43_postfix|westd-41074|\npi0.5|libero_goal|l2norm|0.09|88.6|yes|eval_pi05_l2norm_k09_goal_seed42_postfix|westd-41074|\npi0.5|libero_goal|l2norm|0.09|90.6|no|eval_pi05_l2norm_k09_goal_seed42_v2|cqa1-33015|\npi0.5|libero_goal|l2norm|0.09|0.9|yes|eval_pi05_l2norm_k09_goal_seed42|westd-38929|\npi0.5|libero_goal|l2norm|0.0925|89.8|yes|eval_pi05_l2norm_k0925_goal_seed42_postfix|westd-38929|\npi0.5|libero_goal|l2norm|0.0925|89.8|yes|eval_pi05_l2norm_k0925_goal_seed42_v3|westd-41074|\npi0.5|libero_goal|l2norm|0.0925|90.8|yes|eval_pi05_l2norm_k0925_goal_seed43|westd-41074|\npi0.5|libero_goal|l2norm|0.0925|89.0|yes|eval_pi05_l2norm_k0925_goal_seed42_v2|westd-41074|\npi0.5|libero_goal|l2norm|0.095|90.8|no|eval_pi05_l2norm_k095_goal_seed42_postfix|cqa1-33015|\npi0.5|libero_goal|l2norm|0.095|0.908|no|eval_pi05_l2norm_k095_goal_seed42|cqa1-33015|\npi0.5|libero_goal|l2norm|0.095|89.4|no|eval_pi05_l2norm_k095_goal_seed42_v2|cqa1-33015|\npi0.5|libero_goal|l2norm|0.3|0.542|no|eval_pi05_l2norm_k03_goal_seed42|cqa1-33015|\npi0.5|libero_goal|l2norm|0.85|87.0|no|eval_pi05_l2norm_k085_goal_seed43_postfix|cqa1-33015|\npi0.5|libero_goal|l2norm|0.85|88.0|no|eval_pi05_l2norm_k085_goal_seed42|cqa1-33015|\npi0.5|libero_goal|random|0.03|52.8|yes|eval_pi05_random_k03_goal_seed42_postfix|westd-41074|\npi0.5|libero_goal|random|0.03|53.6|no|eval_pi05_random_k03_goal_seed43_v2|cqa1-33015|\npi0.5|libero_goal|random|0.03|0.51|no|eval_pi05_random_k03_goal_seed42|cqa1-33015|\npi0.5|libero_goal|random|0.03|50.6|yes|eval_pi05_random_k03_goal_seed42_v2|westd-41074|\npi0.5|libero_goal|random|0.05|73.6|no|eval_pi05_random_k05_goal_seed42_postfix|cqa1-33015|\npi0.5|libero_goal|random|0.05|73.6|no|eval_pi05_random_k05_goal_seed42_v2|cqa1-33015|\npi0.5|libero_goal|random|0.07|75.6|yes|eval_pi05_random_k07_goal_seed42_postfix|westd-38929|\npi0.5|libero_goal|random|0.07|78.2|yes|eval_pi05_random_k07_goal_seed42_v2|westd-41074|\npi0.5|libero_goal|random|0.07|0.806|no|eval_pi05_random_k07_goal_seed42|cqa1-33015|\npi0.5|libero_goal|random|0.085|53.0|no|eval_pi05_random_k085_goal_seed42_postfix_v3|cqa1-33015|\npi0.5|libero_goal|random|0.085|0.534|yes|eval_pi05_random_k085_goal_seed43_postfix|westd-41074|\npi0.5|libero_goal|random|0.085|52.8|yes|eval_pi05_random_k085_goal_seed42_postfix|westd-38929|\npi0.5|libero_goal|random|0.085|52.4|no|eval_pi05_random_k085_goal_seed42_v4|cqa1-33015|\npi0.5|libero_goal|random|0.085|0.524|yes|eval_pi05_random_k085_goal_seed42_v3|westd-38929|\npi0.5|libero_goal|random|0.09|61.2|yes|eval_pi05_random_k09_goal_seed43_postfix|westd-41074|\npi0.5|libero_goal|random|0.09|61.8|yes|eval_pi05_random_k09_goal_seed42_postfix|westd-38929|\npi0.5|libero_goal|random|0.09|62.2|yes|eval_pi05_random_k09_goal_seed42_v2|westd-41074|\npi0.5|libero_goal|random|0.0925|70.0|yes|eval_pi05_random_k0925_goal_seed42_v3|westd-41074|\npi0.5|libero_goal|random|0.0925|71.2|yes|eval_pi05_random_k0925_goal_seed42_v2|westd-41074|\npi0.5|libero_goal|random|0.095|82.6|yes|eval_pi05_random_k095_goal_seed42_postfix|westd-38929|\npi0.5|libero_goal|random|0.095|83.8|yes|eval_pi05_random_k095_goal_seed42_v2|westd-41074|\npi0.5|libero_goal|random|0.85|0.522|yes|eval_pi05_random_k085_goal_seed43|westd-41074|\npi0.5|libero_goal|random|0.95|0.834|yes|eval_pi05_random_k095_goal_seed43|westd-41074|\npi0.5|libero_object|attention|0.05|0.378|yes|eval_pi05_attention_k05_object_seed42|westd-41074|\npi0.5|libero_object|attention|0.085|0.922|yes|eval_pi05_attention_k085_object_seed42|westd-41074|\npi0.5|libero_object|attention|0.09|0.972|yes|eval_pi05_attention_k09_object_seed42|westd-41074|\npi0.5|libero_object|attention|0.095|0.984|yes|eval_pi05_attention_k095_object_seed42|westd-41074|\npi0.5|libero_object|attention|0.7|0.006|yes|eval_pi05_attention_k07_object_seed42|westd-41074|\npi0.5|libero_object|l2norm|0.01|0.026|yes|eval_pi05_l2norm_k01_object_seed42|westd-41074|\npi0.5|libero_object|l2norm|0.03|0.51|yes|eval_pi05_l2norm_k03_object_seed42|westd-41074|\npi0.5|libero_object|l2norm|0.05|0.336|yes|eval_pi05_l2norm_k05_object_seed43|westd-41074|\npi0.5|libero_object|l2norm|0.07|56.4|yes|eval_pi05_l2norm_k07_object_seed42_postfix|westd-38929|\npi0.5|libero_object|l2norm|0.07|56.4|yes|eval_pi05_l2norm_k07_object_seed43|westd-41074|\npi0.5|libero_object|l2norm|0.07|55.0|yes|eval_pi05_l2norm_k07_object_seed42|westd-41074|\npi0.5|libero_object|l2norm|0.085|98.4|no|eval_pi05_l2norm_k085_object_seed42_postfix_v2|cqa1-33015|\npi0.5|libero_object|l2norm|0.085|0.984|yes|eval_pi05_l2norm_k085_object_seed43|westd-41074|\npi0.5|libero_object|l2norm|0.085|0.98|yes|eval_pi05_l2norm_k085_object_seed42_v4|westd-41074|\npi0.5|libero_object|l2norm|0.09|0.994|no|eval_pi05_zeromask_l2norm_k09_object_seed42|cqa1-33015|\npi0.5|libero_object|l2norm|0.09|98.4|yes|eval_pi05_l2norm_k09_object_seed43_postfix|westd-41074|\npi0.5|libero_object|l2norm|0.09|98.2|yes|eval_pi05_l2norm_k09_object_seed42_v2|westd-41074|\npi0.5|libero_object|l2norm|0.0925|99.2|yes|eval_pi05_l2norm_k0925_object_seed42||\npi0.5|libero_object|l2norm|0.095|98.2|yes|eval_pi05_l2norm_k095_object_seed42_v2|westd-41074|\npi0.5|libero_object|l2norm|0.095|0.984|no|eval_pi05_l2norm_k095_object_seed43|cqa1-33015|\npi0.5|libero_object|l2norm|0.5|33.4|yes|eval_pi05_l2norm_k05_object_seed42|westd-41074|\npi0.5|libero_object|l2norm|0.85|99.0|no|eval_pi05_l2norm_k085_object_seed43_postfix|cqa1-33015|\npi0.5|libero_object|random|0.03|0.322|yes|eval_pi05_random_k03_object_seed43_v4|westd-38929|\npi0.5|libero_object|random|0.03|0.364|yes|eval_pi05_random_k03_object_seed42|westd-41074|\npi0.5|libero_object|random|0.05|0.682|no|eval_pi05_random_k05_object_seed42_v2|cqa1-33015|\npi0.5|libero_object|random|0.05|68.4|yes|eval_pi05_random_k05_object_seed43|westd-41074|\npi0.5|libero_object|random|0.05|0.694|yes|eval_pi05_random_k05_object_seed42|westd-41074|Original PID 899206 crashed (Network unreachable; tokenizer \npi0.5|libero_object|random|0.07|74.0|no|eval_pi05_random_k07_object_seed42_v4|cqa1-33015|\npi0.5|libero_object|random|0.07|0.74|yes|eval_pi05_random_k07_object_seed42_v3||\npi0.5|libero_object|random|0.07|73.8|yes|eval_pi05_random_k07_object_seed43|westd-41074|\npi0.5|libero_object|random|0.07|0.772|yes|eval_pi05_random_k07_object_seed42|westd-41074|\npi0.5|libero_object|random|0.085|5.6|yes|eval_pi05_random_k085_object_seed42_postfix|westd-41074|\npi0.5|libero_object|random|0.085|0.048|no|eval_pi05_random_k085_object_seed43_postfix|cqa1-33015|\npi0.5|libero_object|random|0.085|0.038|yes|eval_pi05_random_k085_object_seed43|westd-41074|\npi0.5|libero_object|random|0.085|5.0|yes|eval_pi05_random_k085_object_seed42_v2|westd-38929|\npi0.5|libero_object|random|0.09|0.98|yes|eval_pi05_zeromask_random_k09_object_seed42_v3|westd-41074|\npi0.5|libero_object|random|0.09|7.4|yes|eval_pi05_random_k09_object_seed43_postfix|westd-41074|\npi0.5|libero_object|random|0.09|0.09|no|eval_pi05_random_k09_object_seed42_v2|cqa1-33015|Post-fix 重跑完成: 9.0% (45/500)，与 pre-fix v2 结果一致。CRON 误报 faile\npi0.5|libero_object|random|0.09|0.096|yes|eval_pi05_random_k09_object_seed43|westd-41074|\npi0.5|libero_object|random|0.09|9.6|yes|eval_pi05_random_k09_object_seed43_v3|westd-27271|\npi0.5|libero_object|random|0.09|0.17|yes|eval_pi05_random_k09_fixedmask_object_seed42_v2||\npi0.5|libero_object|random|0.0925|27.2|yes|eval_pi05_random_k0925_object_seed42_postfix|westd-41074|\npi0.5|libero_object|random|0.0925|0.3|yes|eval_pi05_random_k0925_object_seed43|westd-38929|\npi0.5|libero_object|random|0.0925|0.276|yes|eval_pi05_random_k0925_object_seed42|westd-41074|\npi0.5|libero_object|random|0.095|74.0|yes|eval_pi05_random_k095_object_seed42_v2||\npi0.5|libero_object|random|0.095|0.728|yes|eval_pi05_random_k095_object_seed43|westd-41074|\npi0.5|libero_object|random|0.9|9.6|yes|eval_pi05_random_k09_object_seed43_v4|westd-41074|\npi0.5|libero_spatial|attention|0.05|0.726|yes|eval_pi05_attention_k05_spatial_seed42|westd-41074|\npi0.5|libero_spatial|l2norm|0.03|0.52|yes|eval_pi05_l2norm_k03_spatial_seed43|westd-38929|\npi0.5|libero_spatial|l2norm|0.03|57.2|yes|eval_pi05_l2norm_k03_spatial_seed42|westd-38929|\npi0.5|libero_spatial|l2norm|0.05|0.574|no|eval_pi05_l2norm_k05_spatial_seed42_postfix|cqa1-33015|\npi0.5|libero_spatial|l2norm|0.05|0.554|yes|eval_pi05_l2norm_k05_spatial_seed43_v2|westd-41074|\npi0.5|libero_spatial|l2norm|0.05|0.582|yes|eval_pi05_l2norm_k05_spatial_seed43|westd-41074|\npi0.5|libero_spatial|l2norm|0.05|55.6|yes|eval_pi05_l2norm_k05_spatial_seed42|westd-38929|\npi0.5|libero_spatial|l2norm|0.07|0.684|yes|eval_pi05_l2norm_k07_spatial_seed43|westd-27271|\npi0.5|libero_spatial|l2norm|0.07|67.0|yes|eval_pi05_l2norm_k07_spatial_seed42|westd-38929|\npi0.5|libero_spatial|l2norm|0.085|0.882|no|eval_pi05_l2norm_k085_spatial_seed43_postfix|cqa1-33015|\npi0.5|libero_spatial|l2norm|0.085|88.4|yes|eval_pi05_l2norm_k085_spatial_seed42_v3|westd-41074|\npi0.5|libero_spatial|l2norm|0.085|88.6|yes|eval_pi05_l2norm_k085_spatial_seed42_v2|westd-41074|\npi0.5|libero_spatial|l2norm|0.085|0.88|yes|eval_pi05_l2norm_k085_spatial_seed43|westd-27271|\npi0.5|libero_spatial|l2norm|0.09|96.2|yes|eval_pi05_l2norm_k09_spatial_seed43_postfix|westd-38929|\npi0.5|libero_spatial|l2norm|0.09|96.0|yes|eval_pi05_l2norm_k09_spatial_seed42_postfix|westd-38929|\npi0.5|libero_spatial|l2norm|0.09|0.956|no|eval_pi05_l2norm_k09_spatial_seed43|cqa1-33015|\npi0.5|libero_spatial|l2norm|0.0925|0.97|no|eval_pi05_l2norm_k0925_spatial_seed42|cqa1-33015|\npi0.5|libero_spatial|l2norm|0.095|0.98|no|eval_pi05_l2norm_k095_spatial_seed43|cqa1-33015|\npi0.5|libero_spatial|l2norm|0.095|0.978|yes|eval_pi05_l2norm_k095_spatial_seed42|westd-38929|\npi0.5|libero_spatial|l2norm|0.3|52.8|no|eval_pi05_l2norm_k03_spatial_seed42_postfix|cqa1-33015|\npi0.5|libero_spatial|random|0.03|43.4|no|eval_pi05_random_k03_spatial_seed42_postfix_v2|cqa1-33015|\npi0.5|libero_spatial|random|0.03|0.512|yes|eval_pi05_random_k03_spatial_seed43|westd-38929|\npi0.5|libero_spatial|random|0.03|49.6|yes|eval_pi05_random_k03_spatial_seed42|westd-38929|\npi0.5|libero_spatial|random|0.05|0.718|no|eval_pi05_random_k05_spatial_seed42_postfix_v3|cqa1-33015|\npi0.5|libero_spatial|random|0.05|71.6|yes|eval_pi05_random_k05_spatial_seed42||\npi0.5|libero_spatial|random|0.05|72.4|yes|eval_pi05_random_k05_spatial_seed43_v2|westd-41074|\npi0.5|libero_spatial|random|0.07|73.8|no|eval_pi05_random_k07_spatial_seed42_postfix|cqa1-33015|\npi0.5|libero_spatial|random|0.07|0.738|yes|eval_pi05_random_k07_spatial_seed43|westd-27271|\npi0.5|libero_spatial|random|0.07|74.4|yes|eval_pi05_random_k07_spatial_seed42|westd-38929|\npi0.5|libero_spatial|random|0.085|59.2|no|eval_pi05_random_k085_spatial_seed43_postfix|cqa1-33015|\npi0.5|libero_spatial|random|0.085|60.2|yes|eval_pi05_random_k085_spatial_seed42_v3|westd-41074|\npi0.5|libero_spatial|random|0.085|60.8|no|eval_pi05_random_k085_spatial_seed42_postfix_v2|cqa1-33015|\npi0.5|libero_spatial|random|0.085|56.6|yes|eval_pi05_random_k085_spatial_seed42_v2|westd-41074|\npi0.5|libero_spatial|random|0.085|0.584|yes|eval_pi05_random_k085_spatial_seed42|westd-41074|\npi0.5|libero_spatial|random|0.085|0.576|yes|eval_pi05_random_k085_spatial_seed43|westd-38929|\npi0.5|libero_spatial|random|0.09|54.0|yes|eval_pi05_random_k09_spatial_seed43_postfix_v2|westd-41074|\npi0.5|libero_spatial|random|0.09|53.4|no|eval_pi05_random_k09_spatial_seed42_postfix_v2|cqa1-33015|\npi0.5|libero_spatial|random|0.09|0.536|no|eval_pi05_random_k09_spatial_seed43|cqa1-33015|\npi0.5|libero_spatial|random|0.0925|58.2|yes|eval_pi05_random_k0925_spatial_seed42_unreg|westd-41074|\npi0.5|libero_spatial|random|0.0925|0.578|no|eval_pi05_random_k0925_spatial_seed43|cqa1-33015|\npi0.5|libero_spatial|random|0.095|76.8|no|eval_pi05_random_k095_spatial_seed42_postfix_v2|cqa1-33015|\npi0.5|libero_spatial|random|0.095|0.768|yes|eval_pi05_random_k095_spatial_seed43|westd-27271|",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  }
}
```

</details>

---


### Assistant

_source line 30_

<details><summary>Logged reasoning block</summary>

```text
I have a lot of data but there are issues:
1. The k values are being parsed incorrectly. For example, `k07` is being parsed as 0.07 instead of 0.7, `k075` as 0.075 instead of 0.75, etc.
2. SR values are sometimes in decimal (0-1) and sometimes percentage (0-100).
3. There are duplicate experiments (v2, v3, v4 etc.) - need to pick the latest/best one.

Let me fix the k-value parsing and SR normalization and do a proper deduplication.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "076e70a6-b6da-4158-a720-52786daa428f",
  "uuid": "5b37554f-5f1d-4849-a30b-f2d797a7b00e",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XvNFEqfqYT2psYa9FkVDNf",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 15347,
      "cache_read_input_tokens": 32442,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 15347
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---


### Assistant

_source line 31_

I see the k-value parsing has issues (0.07 should be 0.7, 0.075 should be 0.75, etc.) and SR values are mixed (some in %, some in 0-1 range). Let me fix this properly.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "076e70a6-b6da-4158-a720-52786daa428f",
  "uuid": "412db09b-6f41-433f-a572-0406fc9694ab",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XvNFEqfqYT2psYa9FkVDNf",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 15347,
      "cache_read_input_tokens": 32442,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 15347
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---


### Tool call

_source line 32_

<details open><summary>🔧 Tool call — Bash · `toolu_01Y5d9EUv5iPfK59YJkoEnZu`</summary>

```json
{
  "command": "cat /home/ubuntu/.claude-account-4/projects/-home-ubuntu--agent-ml-research-be-idea-gen-0515-2-projects-importance-margin-vla-compress/076e70a6-b6da-4158-a720-52786daa428f/tool-results/mcp-agent-ml-research-read_registry-1779856199105.txt | python3 -c \"\nimport json, sys, re, csv\n\ndata = json.loads(sys.stdin.read())\nresult = json.loads(data['result'])\nexperiments = result['data']['experiments']\n\nrows = []\nfor eid, exp in experiments.items():\n    c = exp.get('conclusion', '')\n    if c not in ('success', 'negative'):\n        continue\n    \n    metrics = exp.get('metrics', {})\n    spec = exp.get('spec', {})\n    server = spec.get('server', '')\n    notes = exp.get('notes', '') or ''\n    hypothesis = exp.get('hypothesis', '') or ''\n    model_name = spec.get('model_name', '') or ''\n    \n    # Get SR\n    sr = metrics.get('overall_sr') or metrics.get('success_rate') or metrics.get('overall_SR') or metrics.get('avg_sr')\n    if sr is None:\n        continue\n    \n    eid_lower = eid.lower()\n    is_openvla = 'openvla' in eid_lower or 'openvla' in model_name.lower()\n    is_pi05 = 'pi05' in eid_lower or 'pi0.5' in model_name.lower() or 'pi05' in model_name.lower()\n    is_eval = 'eval' in eid_lower\n    \n    if not (is_openvla or is_pi05) or not is_eval:\n        continue\n    \n    # Extract method\n    method = ''\n    if 'l2norm' in eid_lower: method = 'l2norm'\n    elif 'attn' in eid_lower or 'attention' in eid_lower: method = 'attention'\n    elif 'random' in eid_lower: method = 'random'\n    elif 'wanda' in eid_lower: method = 'wanda'\n    \n    if not method:\n        method = metrics.get('prune_method', '') or spec.get('prune_method', '')\n    \n    # Extract k - use metrics/spec keep_ratio first, then parse from exp_id\n    k = None\n    kr = metrics.get('keep_ratio') or spec.get('keep_ratio')\n    if kr:\n        k = float(kr)\n    else:\n        # Parse from exp_id patterns like: k05, k07, k075, k085, k09, k095, k0925, k1\n        k_match = re.search(r'_k(\\d+)_', '_' + eid_lower + '_')\n        if not k_match:\n            k_match = re.search(r'_k(\\d+)$', eid_lower)\n        if k_match:\n            kstr = k_match.group(1)\n            # Interpret: k05->0.5, k07->0.7, k075->0.75, k085->0.85, k09->0.9, k095->0.95, k0925->0.925\n            if kstr == '1': k = 1.0\n            elif kstr == '05' or kstr == '5': k = 0.5\n            elif kstr == '07' or kstr == '7': k = 0.7\n            elif kstr == '075': k = 0.75\n            elif kstr == '085': k = 0.85\n            elif kstr == '09' or kstr == '9': k = 0.9\n            elif kstr == '095': k = 0.95\n            elif kstr == '0925': k = 0.925\n            elif kstr == '03' or kstr == '3': k = 0.3\n            elif kstr == '01' or kstr == '1': k = 0.1\n            else:\n                # Generic: prepend '0.' to the string\n                try:\n                    k = float('0.' + kstr)\n                except:\n                    pass\n    \n    if k is None:\n        continue\n    \n    # Detect suite\n    suite_norm = ''\n    suite_raw = (spec.get('data_path', '') or spec.get('eval_data', '') or '').lower()\n    combined = suite_raw + ' ' + eid_lower\n    if 'object' in combined:\n        suite_norm = 'libero_object'\n    elif 'spatial' in combined:\n        suite_norm = 'libero_spatial'\n    elif 'goal' in combined:\n        suite_norm = 'libero_goal'\n    elif 'long' in combined or 'libero_10' in combined:\n        suite_norm = 'libero_10'\n    \n    if not suite_norm:\n        continue\n    \n    model = 'OpenVLA' if is_openvla else 'pi0.5'\n    \n    # Normalize SR to percentage (0-100)\n    sr_val = float(sr)\n    if sr_val <= 1.0 and sr_val > 0:\n        sr_val = sr_val * 100\n    # Round to 1 decimal\n    sr_val = round(sr_val, 1)\n    \n    # Determine reliability\n    reliable = 'yes'\n    if model == 'pi0.5' and 'cqa1' in server:\n        if 'strict' not in eid_lower:\n            reliable = 'no'\n    if 'contaminated' in notes.lower() or 'lenient' in notes.lower():\n        reliable = 'no'\n    \n    # Check for zeromask (different method variant)\n    is_zeromask = 'zeromask' in eid_lower\n    if is_zeromask:\n        method = method + '_zeromask'\n    \n    # Check for fixedmask\n    is_fixedmask = 'fixedmask' in eid_lower\n    if is_fixedmask:\n        method = method + '_fixedmask'\n    \n    rows.append({\n        'model': model,\n        'suite': suite_norm,\n        'method': method,\n        'k': k,\n        'sr': sr_val,\n        'reliable': reliable,\n        'exp_id': eid,\n        'server': server,\n        'notes': notes[:100].replace(',', ';').replace('\\n', ' ')\n    })\n\n# Sort\nrows.sort(key=lambda r: (r['model'], r['suite'], r['method'], r['k'], -r['sr']))\n\nprint(f'Total rows: {len(rows)}')\nprint()\nfor r in rows:\n    print(f\\\"{r['model']}|{r['suite']}|{r['method']}|{r['k']}|{r['sr']}|{r['reliable']}|{r['exp_id']}|{r['server']}\\\")\n\" 2>&1\n",
  "description": "Rebuild with fixed k-value parsing",
  "timeout": 30000
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "076e70a6-b6da-4158-a720-52786daa428f",
  "uuid": "62795931-1b9d-4125-ad12-80281e5f7506",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XvNFEqfqYT2psYa9FkVDNf",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 15347,
      "cache_read_input_tokens": 32442,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 15347
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---


### Tool result

_source line 33 · 2026-05-27T04:33:12.482Z_

<details><summary>↩ Tool result · `toolu_01Y5d9EUv5iPfK59YJkoEnZu`</summary>

```text
Total rows: 273

OpenVLA|libero_10|attention|0.5|14.6|yes|eval_openvla_attn_k05_long_seed42|westd-27271
OpenVLA|libero_10|attention|0.7|24.0|yes|eval_openvla_attn_k07_long_seed42_v2|westd-38929
OpenVLA|libero_10|attention|0.75|37.4|yes|eval_openvla_attn_k075_long_seed42|westd-41074
OpenVLA|libero_10|attention|0.85|45.8|yes|eval_openvla_attn_k085_long_seed42_v5|westd-38929
OpenVLA|libero_10|attention|0.9|44.0|yes|eval_openvla_attn_k09_long_seed42_v3|westd-38929
OpenVLA|libero_10|l2norm|0.7|31.2|yes|eval_openvla_l2norm_k07_long_seed42_v2|westd-38929
OpenVLA|libero_10|l2norm|0.85|38.8|yes|eval_openvla_l2norm_k085_long_seed42_v2|westd-38929
OpenVLA|libero_10|l2norm|0.9|43.6|yes|eval_openvla_l2norm_k09_long_seed42_v3|westd-38929
OpenVLA|libero_10|random|0.5|18.6|yes|eval_openvla_random_k05_long_seed42_v2|westd-38929
OpenVLA|libero_10|random|0.7|38.8|yes|eval_openvla_random_k07_long_seed42_v2|westd-38929
OpenVLA|libero_10|random|0.85|45.0|yes|eval_openvla_random_k085_long_seed42_v3|westd-38929
OpenVLA|libero_10|random|0.9|46.8|yes|eval_openvla_random_k09_long_seed42_v3|westd-38929
OpenVLA|libero_goal|attention|0.5|44.2|yes|eval_openvla_attn_k05_goal_seed42|westd-27271
OpenVLA|libero_goal|attention|0.7|66.4|yes|eval_openvla_attn_k07_goal_seed42|westd-38929
OpenVLA|libero_goal|attention|0.75|67.4|yes|eval_openvla_attn_k075_goal_seed42|westd-27271
OpenVLA|libero_goal|attention|0.85|74.6|yes|eval_openvla_attn_k085_goal_seed42_v3|westd-38929
OpenVLA|libero_goal|attention|0.9|73.2|yes|eval_openvla_attn_k09_goal_seed43_v4|westd-27271
OpenVLA|libero_goal|attention|0.9|73.2|yes|eval_openvla_attn_k09_goal_seed42|westd-27271
OpenVLA|libero_goal|l2norm|0.5|43.4|yes|eval_openvla_l2norm_k05_goal_seed42|westd-41074
OpenVLA|libero_goal|l2norm|0.5|43.4|yes|eval_openvla_l2norm_k05_goal_seed42_v3|westd-27271
OpenVLA|libero_goal|l2norm|0.7|68.4|yes|eval_openvla_l2norm_k07_goal_seed42|westd-27271
OpenVLA|libero_goal|l2norm|0.75|70.2|yes|eval_openvla_l2norm_k075_goal_seed42_v2|westd-27271
OpenVLA|libero_goal|l2norm|0.85|75.4|yes|eval_openvla_l2norm_k085_goal_seed42|westd-27271
OpenVLA|libero_goal|l2norm|0.9|75.2|yes|eval_openvla_l2norm_k09_goal_seed43|westd-27271
OpenVLA|libero_goal|l2norm|0.9|75.2|yes|eval_openvla_l2norm_k09_goal_seed43_v3|westd-27271
OpenVLA|libero_goal|l2norm|0.9|74.8|yes|eval_openvla_l2norm_k09_goal_seed42|westd-27271
OpenVLA|libero_goal|random|0.5|52.2|yes|eval_openvla_random_k05_goal_seed42|westd-27271
OpenVLA|libero_goal|random|0.5|52.2|yes|eval_openvla_random_k05_goal_seed42_v2|westd-27271
OpenVLA|libero_goal|random|0.7|68.4|yes|eval_openvla_random_k07_goal_seed42_v4|westd-27271
OpenVLA|libero_goal|random|0.75|72.0|yes|eval_openvla_random_k075_goal_seed42|westd-38929
OpenVLA|libero_goal|random|0.85|78.6|yes|eval_openvla_random_k085_goal_seed42|westd-38929
OpenVLA|libero_goal|random|0.9|80.4|yes|eval_openvla_random_k09_goal_seed43|westd-27271
OpenVLA|libero_goal|random|0.9|79.6|yes|eval_openvla_random_k09_goal_seed42|
OpenVLA|libero_object||0.3|20.6|yes|eval_openvla_pruning_k03_restart|westd-27271
OpenVLA|libero_object||0.7|49.0|yes|eval_openvla_pruning_k07|westd-27271
OpenVLA|libero_object||0.95|69.4|yes|eval_openvla_prune_k095|westd-27271
OpenVLA|libero_object|attention|0.7|43.8|yes|eval_openvla_attn_k07_object_seed42_v3|westd-41074
OpenVLA|libero_object|attention|0.75|53.2|yes|eval_openvla_attn_k075_object_seed42|westd-41074
OpenVLA|libero_object|attention|0.85|55.0|yes|eval_openvla_attn_k085_object_seed42|westd-38929
OpenVLA|libero_object|l2norm|0.3|25.0|yes|eval_openvla_l2norm_k03_object_seed43|westd-38929
OpenVLA|libero_object|l2norm|0.3|25.0|yes|eval_openvla_l2norm_k03_object_seed42|westd-38929
OpenVLA|libero_object|l2norm|0.3|25.0|yes|eval_openvla_prune_l2norm_k03|westd-38929
OpenVLA|libero_object|l2norm|0.3|25.0|yes|eval_openvla_prune_l2norm_k03_seed42|westd-38929
OpenVLA|libero_object|l2norm|0.5|39.2|yes|eval_openvla_l2norm_k05_object_seed42_v4|westd-41074
OpenVLA|libero_object|l2norm|0.5|39.2|yes|eval_openvla_l2norm_k05_object_seed42_v5|westd-38929
OpenVLA|libero_object|l2norm|0.5|39.2|yes|eval_openvla_l2norm_k05_object_seed43|westd-27271
OpenVLA|libero_object|l2norm|0.5|39.2|yes|eval_openvla_l2norm_k05_object_seed42|westd-38929
OpenVLA|libero_object|l2norm|0.5|39.2|yes|eval_openvla_prune_l2norm_k05|westd-38929
OpenVLA|libero_object|l2norm|0.5|39.2|yes|eval_openvla_prune_l2norm_k05_seed42|westd-38929
OpenVLA|libero_object|l2norm|0.7|49.8|yes|eval_openvla_l2norm_k07_object_seed42_v3|westd-38929
OpenVLA|libero_object|l2norm|0.7|49.8|yes|eval_openvla_l2norm_k07_object_seed42_v2|westd-38929
OpenVLA|libero_object|l2norm|0.7|49.8|yes|eval_openvla_prune_l2norm_k07_seed43_v2|westd-27271
OpenVLA|libero_object|l2norm|0.75|57.4|yes|eval_openvla_l2norm_k075_object_seed42|westd-41074
OpenVLA|libero_object|l2norm|0.9|70.6|yes|eval_openvla_l2norm_k09_object_seed42|westd-27271
OpenVLA|libero_object|l2norm|0.9|70.6|yes|eval_openvla_prune_l2norm_k09|westd-38929
OpenVLA|libero_object|l2norm|0.9|70.6|yes|eval_openvla_prune_l2norm_k09_seed42|westd-38929
OpenVLA|libero_object|l2norm|0.95|70.6|yes|eval_openvla_prune_l2norm_k095|westd-38929
OpenVLA|libero_object|l2norm|0.95|70.6|yes|eval_openvla_prune_l2norm_k095_seed42|westd-38929
OpenVLA|libero_object|l2norm_zeromask|0.9|68.8|yes|eval_openvla_zeromask_l2norm_k09_object_seed42|westd-41074
OpenVLA|libero_object|random|0.3|21.4|yes|eval_openvla_random_k03_object_seed42_v2|westd-38929
OpenVLA|libero_object|random|0.5|35.8|yes|eval_openvla_random_k05_object_seed42_v3|westd-41074
OpenVLA|libero_object|random|0.5|35.8|yes|eval_openvla_prune_random_k05_seed42|westd-41074
OpenVLA|libero_object|random|0.5|35.6|yes|eval_openvla_prune_random_k05_seed43_v2|westd-41074
OpenVLA|libero_object|random|0.7|52.6|yes|eval_openvla_random_k07_object_seed43|westd-38929
OpenVLA|libero_object|random|0.7|52.6|yes|eval_openvla_prune_random_k07_seed43_v2|westd-41074
OpenVLA|libero_object|random|0.7|44.4|yes|eval_openvla_random_k07_object_seed42_v2|westd-38929
OpenVLA|libero_object|random|0.9|64.6|yes|eval_openvla_prune_random_k09_seed42|westd-41074
OpenVLA|libero_object|random|0.9|62.2|yes|eval_openvla_prune_random_k09_seed43|westd-27271
OpenVLA|libero_object|random|0.95|67.4|yes|eval_openvla_random_k095_object_seed42|
OpenVLA|libero_object|random|0.95|66.8|yes|eval_openvla_prune_random_k095_seed43|westd-41074
OpenVLA|libero_object|random_zeromask|0.9|71.8|yes|eval_openvla_zeromask_random_k09_object_seed42|westd-41074
OpenVLA|libero_spatial|attention|0.9|80.4|yes|eval_openvla_attn_k09_spatial_seed42|westd-27271
OpenVLA|libero_spatial|l2norm|0.9|75.0|yes|eval_openvla_l2norm_k09_spatial_seed42|westd-27271
OpenVLA|libero_spatial|random|0.5|50.0|yes|eval_openvla_random_k05_spatial_seed42|westd-27271
OpenVLA|libero_spatial|random|0.9|79.8|yes|eval_openvla_random_k09_spatial_seed42|westd-41074
pi0.5|libero_10|attention|0.5|49.8|no|eval_pi05_attention_k05_long_seed42_v2|cqa1-33015
pi0.5|libero_10|attention|0.7|50.8|no|eval_pi05_attention_k07_long_seed42_v2|cqa1-33015
pi0.5|libero_10|attention|0.75|52.4|no|eval_pi05_attention_k075_long_seed42_v2|cqa1-33015
pi0.5|libero_10|attention|0.75|51.8|no|eval_pi05_attention_k075_long_seed42|cqa1-33015
pi0.5|libero_10|attention|0.85|51.6|no|eval_pi05_attention_k085_long_seed42_v2|cqa1-33015
pi0.5|libero_10|attention|0.9|63.8|no|eval_pi05_attention_k09_long_seed42_postfix|cqa1-33015
pi0.5|libero_10|attention|0.95|77.0|no|eval_pi05_attn_k095_long_seed42|cqa1-33015
pi0.5|libero_10|l2norm|0.3|39.2|yes|eval_pi05_l2norm_k03_long_seed43_postfix_v2|westd-38929
pi0.5|libero_10|l2norm|0.5|53.0|no|eval_pi05_l2norm_k05_long_seed43_postfix_v2|cqa1-33015
pi0.5|libero_10|l2norm|0.5|51.4|yes|eval_pi05_l2norm_k05_long_seed42_v3|westd-41074
pi0.5|libero_10|l2norm|0.5|50.2|no|eval_pi05_l2norm_k05_long_seed42|cqa1-33015
pi0.5|libero_10|l2norm|0.5|50.0|no|eval_pi05_l2norm_k05_long_seed42_v4|cqa1-33015
pi0.5|libero_10|l2norm|0.7|65.8|yes|eval_pi05_l2norm_k07_long_seed43_v2|westd-38929
pi0.5|libero_10|l2norm|0.7|65.4|yes|eval_pi05_l2norm_k07_long_seed43_v4|westd-41074
pi0.5|libero_10|l2norm|0.7|65.0|no|eval_pi05_l2norm_k07_long_seed43_v3|cqa1-33015
pi0.5|libero_10|l2norm|0.7|62.6|yes|eval_pi05_l2norm_k07_long_seed42_postfix|westd-27271
pi0.5|libero_10|l2norm|0.75|73.4|no|eval_pi05_l2norm_k075_long_seed42|cqa1-33015
pi0.5|libero_10|l2norm|0.85|80.0|no|eval_pi05_l2norm_k085_long_seed43_v3|cqa1-33015
pi0.5|libero_10|l2norm|0.85|79.0|yes|eval_pi05_l2norm_k085_long_seed43_v2|westd-38929
pi0.5|libero_10|l2norm|0.85|78.8|yes|eval_pi05_l2norm_k085_long_seed42_v3|
pi0.5|libero_10|l2norm|0.85|78.6|yes|eval_pi05_l2norm_k085_long_seed43_postfix|westd-41074
pi0.5|libero_10|l2norm|0.85|78.4|yes|eval_pi05_l2norm_k085_long_seed42_postfix|westd-41074
pi0.5|libero_10|l2norm|0.85|78.0|no|eval_pi05_l2norm_k085_long_seed42_postfix_v3|cqa1-33015
pi0.5|libero_10|l2norm|0.85|77.8|no|eval_pi05_l2norm_k085_long_seed42_v4|cqa1-33015
pi0.5|libero_10|l2norm|0.85|77.0|yes|eval_pi05_l2norm_k085_long_seed43_v4|westd-41074
pi0.5|libero_10|l2norm|0.9|81.0|yes|eval_pi05_l2norm_k09_long_seed42|westd-41074
pi0.5|libero_10|l2norm|0.9|80.8|no|eval_pi05_l2norm_k09_long_seed43_postfix|cqa1-33015
pi0.5|libero_10|l2norm|0.9|80.0|no|eval_pi05_l2norm_k09_long_seed42_postfix_v2|cqa1-33015
pi0.5|libero_10|l2norm|0.9|80.0|yes|eval_pi05_l2norm_k09_long_seed43_postfix_v2|westd-41074
pi0.5|libero_10|l2norm|0.925|83.2|no|eval_pi05_l2norm_k0925_long_seed42_v2|cqa1-33015
pi0.5|libero_10|l2norm|0.95|87.4|yes|eval_pi05_l2norm_k095_long_seed43_postfix|westd-38929
pi0.5|libero_10|l2norm|0.95|87.0|yes|eval_pi05_l2norm_k095_long_seed42_postfix|westd-38929
pi0.5|libero_10|random|0.3|29.6|yes|eval_pi05_random_k03_long_seed42_postfix|westd-38929
pi0.5|libero_10|random|0.3|29.0|yes|eval_pi05_random_k03_long_seed42|westd-38929
pi0.5|libero_10|random|0.3|28.4|yes|eval_pi05_random_k03_long_seed43_v3|westd-38929
pi0.5|libero_10|random|0.3|28.0|yes|eval_pi05_random_k03_long_seed43_v2|westd-41074
pi0.5|libero_10|random|0.3|27.2|no|eval_pi05_random_k03_long_seed43_v4|cqa1-33015
pi0.5|libero_10|random|0.5|51.2|yes|eval_pi05_random_k05_long_seed43_v2|westd-41074
pi0.5|libero_10|random|0.5|50.2|no|eval_pi05_random_k05_long_seed42_v3|cqa1-33015
pi0.5|libero_10|random|0.5|50.2|no|eval_pi05_random_k05_long_seed42|cqa1-33015
pi0.5|libero_10|random|0.5|46.8|no|eval_pi05_random_k05_long_seed43_postfix|cqa1-33015
pi0.5|libero_10|random|0.5|46.8|yes|eval_pi05_random_k05_long_seed42_postfix|westd-38929
pi0.5|libero_10|random|0.5|46.8|yes|eval_pi05_random_k05_long_seed42_v2|westd-41074
pi0.5|libero_10|random|0.7|68.6|no|eval_pi05_random_k07_long_seed43_postfix|cqa1-33015
pi0.5|libero_10|random|0.7|65.8|yes|eval_pi05_random_k07_long_seed42_postfix|westd-38929
pi0.5|libero_10|random|0.7|62.4|no|eval_pi05_random_k07_long_seed42|cqa1-33015
pi0.5|libero_10|random|0.75|62.4|no|eval_pi05_random_k075_long_seed42_v2|cqa1-33015
pi0.5|libero_10|random|0.85|49.4|no|eval_pi05_random_k085_long_seed42_postfix_v3|cqa1-33015
pi0.5|libero_10|random|0.85|45.2|yes|eval_pi05_random_k085_long_seed42_postfix|westd-41074
pi0.5|libero_10|random|0.85|44.4|no|eval_pi05_random_k085_long_seed42_v2|cqa1-33015
pi0.5|libero_10|random|0.85|44.4|no|eval_pi05_random_k085_long_seed42|cqa1-33015
pi0.5|libero_10|random|0.85|42.4|yes|eval_pi05_random_k085_long_seed43_v3|westd-41074
pi0.5|libero_10|random|0.85|42.0|no|eval_pi05_random_k085_long_seed43_v2|cqa1-33015
pi0.5|libero_10|random|0.85|41.8|no|eval_pi05_random_k085_long_seed43_postfix|cqa1-33015
pi0.5|libero_10|random|0.85|41.8|yes|eval_pi05_random_k085_long_seed43|westd-41074
pi0.5|libero_10|random|0.9|32.0|yes|eval_pi05_random_k09_long_seed42_postfix|westd-41074
pi0.5|libero_10|random|0.9|31.8|yes|eval_pi05_random_k09_long_seed42|westd-38929
pi0.5|libero_10|random|0.925|38.6|no|eval_pi05_random_k0925_long_seed42_postfix|cqa1-33015
pi0.5|libero_10|random|0.95|63.2|yes|eval_pi05_random_k095_long_seed42_postfix|westd-41074
pi0.5|libero_10|random|0.95|61.2|yes|eval_pi05_random_k095_long_seed42|westd-38929
pi0.5|libero_10|random|0.95|58.4|no|eval_pi05_random_k095_long_seed43_postfix|cqa1-33015
pi0.5|libero_goal|attention|0.5|72.2|yes|eval_pi05_attention_k05_goal_seed43|westd-41074
pi0.5|libero_goal|attention|0.5|70.2|yes|eval_pi05_attention_k05_goal_seed42|westd-41074
pi0.5|libero_goal|l2norm|0.3|54.2|no|eval_pi05_l2norm_k03_goal_seed42|cqa1-33015
pi0.5|libero_goal|l2norm|0.3|51.8|yes|eval_pi05_l2norm_k03_goal_seed42_postfix|westd-38929
pi0.5|libero_goal|l2norm|0.3|50.6|no|eval_pi05_l2norm_k03_goal_seed42_v2|cqa1-33015
pi0.5|libero_goal|l2norm|0.5|59.8|yes|eval_pi05_l2norm_k05_goal_seed42_postfix|westd-41074
pi0.5|libero_goal|l2norm|0.5|59.2|yes|eval_pi05_l2norm_k05_goal_seed42|westd-41074
pi0.5|libero_goal|l2norm|0.7|73.6|no|eval_pi05_l2norm_k07_goal_seed42_v2|cqa1-33015
pi0.5|libero_goal|l2norm|0.7|72.2|yes|eval_pi05_l2norm_k07_goal_seed43_v2|westd-41074
pi0.5|libero_goal|l2norm|0.7|70.2|yes|eval_pi05_l2norm_k07_goal_seed42_postfix|westd-41074
pi0.5|libero_goal|l2norm|0.85|88.0|no|eval_pi05_l2norm_k085_goal_seed42|cqa1-33015
pi0.5|libero_goal|l2norm|0.85|87.4|yes|eval_pi05_l2norm_k085_goal_seed42_postfix|westd-41074
pi0.5|libero_goal|l2norm|0.85|87.0|no|eval_pi05_l2norm_k085_goal_seed43_postfix|cqa1-33015
pi0.5|libero_goal|l2norm|0.85|87.0|no|eval_pi05_l2norm_k085_goal_seed43|cqa1-33015
pi0.5|libero_goal|l2norm|0.9|91.0|yes|eval_pi05_l2norm_k09_goal_seed43_postfix|westd-41074
pi0.5|libero_goal|l2norm|0.9|90.6|no|eval_pi05_l2norm_k09_goal_seed42_v2|cqa1-33015
pi0.5|libero_goal|l2norm|0.9|90.0|yes|eval_pi05_l2norm_k09_goal_seed42|westd-38929
pi0.5|libero_goal|l2norm|0.9|88.6|yes|eval_pi05_l2norm_k09_goal_seed42_postfix|westd-41074
pi0.5|libero_goal|l2norm|0.925|90.8|yes|eval_pi05_l2norm_k0925_goal_seed43|westd-41074
pi0.5|libero_goal|l2norm|0.925|89.8|yes|eval_pi05_l2norm_k0925_goal_seed42_postfix|westd-38929
pi0.5|libero_goal|l2norm|0.925|89.8|yes|eval_pi05_l2norm_k0925_goal_seed42_v3|westd-41074
pi0.5|libero_goal|l2norm|0.925|89.0|yes|eval_pi05_l2norm_k0925_goal_seed42_v2|westd-41074
pi0.5|libero_goal|l2norm|0.95|90.8|no|eval_pi05_l2norm_k095_goal_seed42_postfix|cqa1-33015
pi0.5|libero_goal|l2norm|0.95|90.8|no|eval_pi05_l2norm_k095_goal_seed42|cqa1-33015
pi0.5|libero_goal|l2norm|0.95|89.4|no|eval_pi05_l2norm_k095_goal_seed42_v2|cqa1-33015
pi0.5|libero_goal|random|0.3|53.6|no|eval_pi05_random_k03_goal_seed43_v2|cqa1-33015
pi0.5|libero_goal|random|0.3|52.8|yes|eval_pi05_random_k03_goal_seed42_postfix|westd-41074
pi0.5|libero_goal|random|0.3|51.0|no|eval_pi05_random_k03_goal_seed42|cqa1-33015
pi0.5|libero_goal|random|0.3|50.6|yes|eval_pi05_random_k03_goal_seed42_v2|westd-41074
pi0.5|libero_goal|random|0.5|73.6|no|eval_pi05_random_k05_goal_seed42_postfix|cqa1-33015
pi0.5|libero_goal|random|0.5|73.6|no|eval_pi05_random_k05_goal_seed42_v2|cqa1-33015
pi0.5|libero_goal|random|0.7|80.6|no|eval_pi05_random_k07_goal_seed42|cqa1-33015
pi0.5|libero_goal|random|0.7|78.2|yes|eval_pi05_random_k07_goal_seed42_v2|westd-41074
pi0.5|libero_goal|random|0.7|75.6|yes|eval_pi05_random_k07_goal_seed42_postfix|westd-38929
pi0.5|libero_goal|random|0.85|53.4|yes|eval_pi05_random_k085_goal_seed43_postfix|westd-41074
pi0.5|libero_goal|random|0.85|53.0|no|eval_pi05_random_k085_goal_seed42_postfix_v3|cqa1-33015
pi0.5|libero_goal|random|0.85|52.8|yes|eval_pi05_random_k085_goal_seed42_postfix|westd-38929
pi0.5|libero_goal|random|0.85|52.4|no|eval_pi05_random_k085_goal_seed42_v4|cqa1-33015
pi0.5|libero_goal|random|0.85|52.4|yes|eval_pi05_random_k085_goal_seed42_v3|westd-38929
pi0.5|libero_goal|random|0.85|52.2|yes|eval_pi05_random_k085_goal_seed43|westd-41074
pi0.5|libero_goal|random|0.9|62.2|yes|eval_pi05_random_k09_goal_seed42_v2|westd-41074
pi0.5|libero_goal|random|0.9|61.8|yes|eval_pi05_random_k09_goal_seed42_postfix|westd-38929
pi0.5|libero_goal|random|0.9|61.2|yes|eval_pi05_random_k09_goal_seed43_postfix|westd-41074
pi0.5|libero_goal|random|0.925|71.2|yes|eval_pi05_random_k0925_goal_seed42_v2|westd-41074
pi0.5|libero_goal|random|0.925|70.0|yes|eval_pi05_random_k0925_goal_seed42_v3|westd-41074
pi0.5|libero_goal|random|0.95|83.8|yes|eval_pi05_random_k095_goal_seed42_v2|westd-41074
pi0.5|libero_goal|random|0.95|83.4|yes|eval_pi05_random_k095_goal_seed43|westd-41074
pi0.5|libero_goal|random|0.95|82.6|yes|eval_pi05_random_k095_goal_seed42_postfix|westd-38929
pi0.5|libero_object|attention|0.5|37.8|yes|eval_pi05_attention_k05_object_seed42|westd-41074
pi0.5|libero_object|attention|0.7|0.6|yes|eval_pi05_attention_k07_object_seed42|westd-41074
pi0.5|libero_object|attention|0.85|92.2|yes|eval_pi05_attention_k085_object_seed42|westd-41074
pi0.5|libero_object|attention|0.9|97.2|yes|eval_pi05_attention_k09_object_seed42|westd-41074
pi0.5|libero_object|attention|0.95|98.4|yes|eval_pi05_attention_k095_object_seed42|westd-41074
pi0.5|libero_object|l2norm|0.1|2.6|yes|eval_pi05_l2norm_k01_object_seed42|westd-41074
pi0.5|libero_object|l2norm|0.3|51.0|yes|eval_pi05_l2norm_k03_object_seed42|westd-41074
pi0.5|libero_object|l2norm|0.5|33.6|yes|eval_pi05_l2norm_k05_object_seed43|westd-41074
pi0.5|libero_object|l2norm|0.5|33.4|yes|eval_pi05_l2norm_k05_object_seed42|westd-41074
pi0.5|libero_object|l2norm|0.7|56.4|yes|eval_pi05_l2norm_k07_object_seed42_postfix|westd-38929
pi0.5|libero_object|l2norm|0.7|56.4|yes|eval_pi05_l2norm_k07_object_seed43|westd-41074
pi0.5|libero_object|l2norm|0.7|55.0|yes|eval_pi05_l2norm_k07_object_seed42|westd-41074
pi0.5|libero_object|l2norm|0.85|99.0|no|eval_pi05_l2norm_k085_object_seed43_postfix|cqa1-33015
pi0.5|libero_object|l2norm|0.85|98.4|no|eval_pi05_l2norm_k085_object_seed42_postfix_v2|cqa1-33015
pi0.5|libero_object|l2norm|0.85|98.4|yes|eval_pi05_l2norm_k085_object_seed43|westd-41074
pi0.5|libero_object|l2norm|0.85|98.0|yes|eval_pi05_l2norm_k085_object_seed42_v4|westd-41074
pi0.5|libero_object|l2norm|0.9|98.4|yes|eval_pi05_l2norm_k09_object_seed43_postfix|westd-41074
pi0.5|libero_object|l2norm|0.9|98.2|yes|eval_pi05_l2norm_k09_object_seed42_v2|westd-41074
pi0.5|libero_object|l2norm|0.925|99.2|yes|eval_pi05_l2norm_k0925_object_seed42|
pi0.5|libero_object|l2norm|0.95|98.4|no|eval_pi05_l2norm_k095_object_seed43|cqa1-33015
pi0.5|libero_object|l2norm|0.95|98.2|yes|eval_pi05_l2norm_k095_object_seed42_v2|westd-41074
pi0.5|libero_object|l2norm_zeromask|0.9|99.4|no|eval_pi05_zeromask_l2norm_k09_object_seed42|cqa1-33015
pi0.5|libero_object|random|0.3|36.4|yes|eval_pi05_random_k03_object_seed42|westd-41074
pi0.5|libero_object|random|0.3|32.2|yes|eval_pi05_random_k03_object_seed43_v4|westd-38929
pi0.5|libero_object|random|0.5|69.4|yes|eval_pi05_random_k05_object_seed42|westd-41074
pi0.5|libero_object|random|0.5|68.4|yes|eval_pi05_random_k05_object_seed43|westd-41074
pi0.5|libero_object|random|0.5|68.2|no|eval_pi05_random_k05_object_seed42_v2|cqa1-33015
pi0.5|libero_object|random|0.7|77.2|yes|eval_pi05_random_k07_object_seed42|westd-41074
pi0.5|libero_object|random|0.7|74.0|no|eval_pi05_random_k07_object_seed42_v4|cqa1-33015
pi0.5|libero_object|random|0.7|74.0|yes|eval_pi05_random_k07_object_seed42_v3|
pi0.5|libero_object|random|0.7|73.8|yes|eval_pi05_random_k07_object_seed43|westd-41074
pi0.5|libero_object|random|0.85|5.6|yes|eval_pi05_random_k085_object_seed42_postfix|westd-41074
pi0.5|libero_object|random|0.85|5.0|yes|eval_pi05_random_k085_object_seed42_v2|westd-38929
pi0.5|libero_object|random|0.85|4.8|no|eval_pi05_random_k085_object_seed43_postfix|cqa1-33015
pi0.5|libero_object|random|0.85|3.8|yes|eval_pi05_random_k085_object_seed43|westd-41074
pi0.5|libero_object|random|0.9|9.6|yes|eval_pi05_random_k09_object_seed43|westd-41074
pi0.5|libero_object|random|0.9|9.6|yes|eval_pi05_random_k09_object_seed43_v4|westd-41074
pi0.5|libero_object|random|0.9|9.6|yes|eval_pi05_random_k09_object_seed43_v3|westd-27271
pi0.5|libero_object|random|0.9|9.0|no|eval_pi05_random_k09_object_seed42_v2|cqa1-33015
pi0.5|libero_object|random|0.9|7.4|yes|eval_pi05_random_k09_object_seed43_postfix|westd-41074
pi0.5|libero_object|random|0.925|30.0|yes|eval_pi05_random_k0925_object_seed43|westd-38929
pi0.5|libero_object|random|0.925|27.6|yes|eval_pi05_random_k0925_object_seed42|westd-41074
pi0.5|libero_object|random|0.925|27.2|yes|eval_pi05_random_k0925_object_seed42_postfix|westd-41074
pi0.5|libero_object|random|0.95|74.0|yes|eval_pi05_random_k095_object_seed42_v2|
pi0.5|libero_object|random|0.95|72.8|yes|eval_pi05_random_k095_object_seed43|westd-41074
pi0.5|libero_object|random_fixedmask|0.9|17.0|yes|eval_pi05_random_k09_fixedmask_object_seed42_v2|
pi0.5|libero_object|random_zeromask|0.9|98.0|yes|eval_pi05_zeromask_random_k09_object_seed42_v3|westd-41074
pi0.5|libero_spatial|attention|0.5|72.6|yes|eval_pi05_attention_k05_spatial_seed42|westd-41074
pi0.5|libero_spatial|l2norm|0.3|57.2|yes|eval_pi05_l2norm_k03_spatial_seed42|westd-38929
pi0.5|libero_spatial|l2norm|0.3|52.8|no|eval_pi05_l2norm_k03_spatial_seed42_postfix|cqa1-33015
pi0.5|libero_spatial|l2norm|0.3|52.0|yes|eval_pi05_l2norm_k03_spatial_seed43|westd-38929
pi0.5|libero_spatial|l2norm|0.5|58.2|yes|eval_pi05_l2norm_k05_spatial_seed43|westd-41074
pi0.5|libero_spatial|l2norm|0.5|57.4|no|eval_pi05_l2norm_k05_spatial_seed42_postfix|cqa1-33015
pi0.5|libero_spatial|l2norm|0.5|55.6|yes|eval_pi05_l2norm_k05_spatial_seed42|westd-38929
pi0.5|libero_spatial|l2norm|0.5|55.4|yes|eval_pi05_l2norm_k05_spatial_seed43_v2|westd-41074
pi0.5|libero_spatial|l2norm|0.7|68.4|yes|eval_pi05_l2norm_k07_spatial_seed43|westd-27271
pi0.5|libero_spatial|l2norm|0.7|67.0|yes|eval_pi05_l2norm_k07_spatial_seed42|westd-38929
pi0.5|libero_spatial|l2norm|0.85|88.6|yes|eval_pi05_l2norm_k085_spatial_seed42_v2|westd-41074
pi0.5|libero_spatial|l2norm|0.85|88.4|yes|eval_pi05_l2norm_k085_spatial_seed42_v3|westd-41074
pi0.5|libero_spatial|l2norm|0.85|88.2|no|eval_pi05_l2norm_k085_spatial_seed43_postfix|cqa1-33015
pi0.5|libero_spatial|l2norm|0.85|88.0|yes|eval_pi05_l2norm_k085_spatial_seed43|westd-27271
pi0.5|libero_spatial|l2norm|0.9|96.2|yes|eval_pi05_l2norm_k09_spatial_seed43_postfix|westd-38929
pi0.5|libero_spatial|l2norm|0.9|96.0|yes|eval_pi05_l2norm_k09_spatial_seed42_postfix|westd-38929
pi0.5|libero_spatial|l2norm|0.9|95.6|no|eval_pi05_l2norm_k09_spatial_seed43|cqa1-33015
pi0.5|libero_spatial|l2norm|0.925|97.0|no|eval_pi05_l2norm_k0925_spatial_seed42|cqa1-33015
pi0.5|libero_spatial|l2norm|0.95|98.0|no|eval_pi05_l2norm_k095_spatial_seed43|cqa1-33015
pi0.5|libero_spatial|l2norm|0.95|97.8|yes|eval_pi05_l2norm_k095_spatial_seed42|westd-38929
pi0.5|libero_spatial|random|0.3|51.2|yes|eval_pi05_random_k03_spatial_seed43|westd-38929
pi0.5|libero_spatial|random|0.3|49.6|yes|eval_pi05_random_k03_spatial_seed42|westd-38929
pi0.5|libero_spatial|random|0.3|43.4|no|eval_pi05_random_k03_spatial_seed42_postfix_v2|cqa1-33015
pi0.5|libero_spatial|random|0.5|72.4|yes|eval_pi05_random_k05_spatial_seed43_v2|westd-41074
pi0.5|libero_spatial|random|0.5|71.8|no|eval_pi05_random_k05_spatial_seed42_postfix_v3|cqa1-33015
pi0.5|libero_spatial|random|0.5|71.6|yes|eval_pi05_random_k05_spatial_seed42|
pi0.5|libero_spatial|random|0.7|74.4|yes|eval_pi05_random_k07_spatial_seed42|westd-38929
pi0.5|libero_spatial|random|0.7|73.8|no|eval_pi05_random_k07_spatial_seed42_postfix|cqa1-33015
pi0.5|libero_spatial|random|0.7|73.8|yes|eval_pi05_random_k07_spatial_seed43|westd-27271
pi0.5|libero_spatial|random|0.85|60.8|no|eval_pi05_random_k085_spatial_seed42_postfix_v2|cqa1-33015
pi0.5|libero_spatial|random|0.85|60.2|yes|eval_pi05_random_k085_spatial_seed42_v3|westd-41074
pi0.5|libero_spatial|random|0.85|59.2|no|eval_pi05_random_k085_spatial_seed43_postfix|cqa1-33015
pi0.5|libero_spatial|random|0.85|58.4|yes|eval_pi05_random_k085_spatial_seed42|westd-41074
pi0.5|libero_spatial|random|0.85|57.6|yes|eval_pi05_random_k085_spatial_seed43|westd-38929
pi0.5|libero_spatial|random|0.85|56.6|yes|eval_pi05_random_k085_spatial_seed42_v2|westd-41074
pi0.5|libero_spatial|random|0.9|54.0|yes|eval_pi05_random_k09_spatial_seed43_postfix_v2|westd-41074
pi0.5|libero_spatial|random|0.9|53.6|no|eval_pi05_random_k09_spatial_seed43|cqa1-33015
pi0.5|libero_spatial|random|0.9|53.4|no|eval_pi05_random_k09_spatial_seed42_postfix_v2|cqa1-33015
pi0.5|libero_spatial|random|0.925|58.2|yes|eval_pi05_random_k0925_spatial_seed42_unreg|westd-41074
pi0.5|libero_spatial|random|0.925|57.8|no|eval_pi05_random_k0925_spatial_seed43|cqa1-33015
pi0.5|libero_spatial|random|0.95|76.8|no|eval_pi05_random_k095_spatial_seed42_postfix_v2|cqa1-33015
pi0.5|libero_spatial|random|0.95|76.8|yes|eval_pi05_random_k095_spatial_seed43|westd-27271
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "076e70a6-b6da-4158-a720-52786daa428f",
  "uuid": "49a6e632-222d-4a24-873b-0714e6b247f8",
  "tool_use_result": {
    "stdout": "Total rows: 273\n\nOpenVLA|libero_10|attention|0.5|14.6|yes|eval_openvla_attn_k05_long_seed42|westd-27271\nOpenVLA|libero_10|attention|0.7|24.0|yes|eval_openvla_attn_k07_long_seed42_v2|westd-38929\nOpenVLA|libero_10|attention|0.75|37.4|yes|eval_openvla_attn_k075_long_seed42|westd-41074\nOpenVLA|libero_10|attention|0.85|45.8|yes|eval_openvla_attn_k085_long_seed42_v5|westd-38929\nOpenVLA|libero_10|attention|0.9|44.0|yes|eval_openvla_attn_k09_long_seed42_v3|westd-38929\nOpenVLA|libero_10|l2norm|0.7|31.2|yes|eval_openvla_l2norm_k07_long_seed42_v2|westd-38929\nOpenVLA|libero_10|l2norm|0.85|38.8|yes|eval_openvla_l2norm_k085_long_seed42_v2|westd-38929\nOpenVLA|libero_10|l2norm|0.9|43.6|yes|eval_openvla_l2norm_k09_long_seed42_v3|westd-38929\nOpenVLA|libero_10|random|0.5|18.6|yes|eval_openvla_random_k05_long_seed42_v2|westd-38929\nOpenVLA|libero_10|random|0.7|38.8|yes|eval_openvla_random_k07_long_seed42_v2|westd-38929\nOpenVLA|libero_10|random|0.85|45.0|yes|eval_openvla_random_k085_long_seed42_v3|westd-38929\nOpenVLA|libero_10|random|0.9|46.8|yes|eval_openvla_random_k09_long_seed42_v3|westd-38929\nOpenVLA|libero_goal|attention|0.5|44.2|yes|eval_openvla_attn_k05_goal_seed42|westd-27271\nOpenVLA|libero_goal|attention|0.7|66.4|yes|eval_openvla_attn_k07_goal_seed42|westd-38929\nOpenVLA|libero_goal|attention|0.75|67.4|yes|eval_openvla_attn_k075_goal_seed42|westd-27271\nOpenVLA|libero_goal|attention|0.85|74.6|yes|eval_openvla_attn_k085_goal_seed42_v3|westd-38929\nOpenVLA|libero_goal|attention|0.9|73.2|yes|eval_openvla_attn_k09_goal_seed43_v4|westd-27271\nOpenVLA|libero_goal|attention|0.9|73.2|yes|eval_openvla_attn_k09_goal_seed42|westd-27271\nOpenVLA|libero_goal|l2norm|0.5|43.4|yes|eval_openvla_l2norm_k05_goal_seed42|westd-41074\nOpenVLA|libero_goal|l2norm|0.5|43.4|yes|eval_openvla_l2norm_k05_goal_seed42_v3|westd-27271\nOpenVLA|libero_goal|l2norm|0.7|68.4|yes|eval_openvla_l2norm_k07_goal_seed42|westd-27271\nOpenVLA|libero_goal|l2norm|0.75|70.2|yes|eval_openvla_l2norm_k075_goal_seed42_v2|westd-27271\nOpenVLA|libero_goal|l2norm|0.85|75.4|yes|eval_openvla_l2norm_k085_goal_seed42|westd-27271\nOpenVLA|libero_goal|l2norm|0.9|75.2|yes|eval_openvla_l2norm_k09_goal_seed43|westd-27271\nOpenVLA|libero_goal|l2norm|0.9|75.2|yes|eval_openvla_l2norm_k09_goal_seed43_v3|westd-27271\nOpenVLA|libero_goal|l2norm|0.9|74.8|yes|eval_openvla_l2norm_k09_goal_seed42|westd-27271\nOpenVLA|libero_goal|random|0.5|52.2|yes|eval_openvla_random_k05_goal_seed42|westd-27271\nOpenVLA|libero_goal|random|0.5|52.2|yes|eval_openvla_random_k05_goal_seed42_v2|westd-27271\nOpenVLA|libero_goal|random|0.7|68.4|yes|eval_openvla_random_k07_goal_seed42_v4|westd-27271\nOpenVLA|libero_goal|random|0.75|72.0|yes|eval_openvla_random_k075_goal_seed42|westd-38929\nOpenVLA|libero_goal|random|0.85|78.6|yes|eval_openvla_random_k085_goal_seed42|westd-38929\nOpenVLA|libero_goal|random|0.9|80.4|yes|eval_openvla_random_k09_goal_seed43|westd-27271\nOpenVLA|libero_goal|random|0.9|79.6|yes|eval_openvla_random_k09_goal_seed42|\nOpenVLA|libero_object||0.3|20.6|yes|eval_openvla_pruning_k03_restart|westd-27271\nOpenVLA|libero_object||0.7|49.0|yes|eval_openvla_pruning_k07|westd-27271\nOpenVLA|libero_object||0.95|69.4|yes|eval_openvla_prune_k095|westd-27271\nOpenVLA|libero_object|attention|0.7|43.8|yes|eval_openvla_attn_k07_object_seed42_v3|westd-41074\nOpenVLA|libero_object|attention|0.75|53.2|yes|eval_openvla_attn_k075_object_seed42|westd-41074\nOpenVLA|libero_object|attention|0.85|55.0|yes|eval_openvla_attn_k085_object_seed42|westd-38929\nOpenVLA|libero_object|l2norm|0.3|25.0|yes|eval_openvla_l2norm_k03_object_seed43|westd-38929\nOpenVLA|libero_object|l2norm|0.3|25.0|yes|eval_openvla_l2norm_k03_object_seed42|westd-38929\nOpenVLA|libero_object|l2norm|0.3|25.0|yes|eval_openvla_prune_l2norm_k03|westd-38929\nOpenVLA|libero_object|l2norm|0.3|25.0|yes|eval_openvla_prune_l2norm_k03_seed42|westd-38929\nOpenVLA|libero_object|l2norm|0.5|39.2|yes|eval_openvla_l2norm_k05_object_seed42_v4|westd-41074\nOpenVLA|libero_object|l2norm|0.5|39.2|yes|eval_openvla_l2norm_k05_object_seed42_v5|westd-38929\nOpenVLA|libero_object|l2norm|0.5|39.2|yes|eval_openvla_l2norm_k05_object_seed43|westd-27271\nOpenVLA|libero_object|l2norm|0.5|39.2|yes|eval_openvla_l2norm_k05_object_seed42|westd-38929\nOpenVLA|libero_object|l2norm|0.5|39.2|yes|eval_openvla_prune_l2norm_k05|westd-38929\nOpenVLA|libero_object|l2norm|0.5|39.2|yes|eval_openvla_prune_l2norm_k05_seed42|westd-38929\nOpenVLA|libero_object|l2norm|0.7|49.8|yes|eval_openvla_l2norm_k07_object_seed42_v3|westd-38929\nOpenVLA|libero_object|l2norm|0.7|49.8|yes|eval_openvla_l2norm_k07_object_seed42_v2|westd-38929\nOpenVLA|libero_object|l2norm|0.7|49.8|yes|eval_openvla_prune_l2norm_k07_seed43_v2|westd-27271\nOpenVLA|libero_object|l2norm|0.75|57.4|yes|eval_openvla_l2norm_k075_object_seed42|westd-41074\nOpenVLA|libero_object|l2norm|0.9|70.6|yes|eval_openvla_l2norm_k09_object_seed42|westd-27271\nOpenVLA|libero_object|l2norm|0.9|70.6|yes|eval_openvla_prune_l2norm_k09|westd-38929\nOpenVLA|libero_object|l2norm|0.9|70.6|yes|eval_openvla_prune_l2norm_k09_seed42|westd-38929\nOpenVLA|libero_object|l2norm|0.95|70.6|yes|eval_openvla_prune_l2norm_k095|westd-38929\nOpenVLA|libero_object|l2norm|0.95|70.6|yes|eval_openvla_prune_l2norm_k095_seed42|westd-38929\nOpenVLA|libero_object|l2norm_zeromask|0.9|68.8|yes|eval_openvla_zeromask_l2norm_k09_object_seed42|westd-41074\nOpenVLA|libero_object|random|0.3|21.4|yes|eval_openvla_random_k03_object_seed42_v2|westd-38929\nOpenVLA|libero_object|random|0.5|35.8|yes|eval_openvla_random_k05_object_seed42_v3|westd-41074\nOpenVLA|libero_object|random|0.5|35.8|yes|eval_openvla_prune_random_k05_seed42|westd-41074\nOpenVLA|libero_object|random|0.5|35.6|yes|eval_openvla_prune_random_k05_seed43_v2|westd-41074\nOpenVLA|libero_object|random|0.7|52.6|yes|eval_openvla_random_k07_object_seed43|westd-38929\nOpenVLA|libero_object|random|0.7|52.6|yes|eval_openvla_prune_random_k07_seed43_v2|westd-41074\nOpenVLA|libero_object|random|0.7|44.4|yes|eval_openvla_random_k07_object_seed42_v2|westd-38929\nOpenVLA|libero_object|random|0.9|64.6|yes|eval_openvla_prune_random_k09_seed42|westd-41074\nOpenVLA|libero_object|random|0.9|62.2|yes|eval_openvla_prune_random_k09_seed43|westd-27271\nOpenVLA|libero_object|random|0.95|67.4|yes|eval_openvla_random_k095_object_seed42|\nOpenVLA|libero_object|random|0.95|66.8|yes|eval_openvla_prune_random_k095_seed43|westd-41074\nOpenVLA|libero_object|random_zeromask|0.9|71.8|yes|eval_openvla_zeromask_random_k09_object_seed42|westd-41074\nOpenVLA|libero_spatial|attention|0.9|80.4|yes|eval_openvla_attn_k09_spatial_seed42|westd-27271\nOpenVLA|libero_spatial|l2norm|0.9|75.0|yes|eval_openvla_l2norm_k09_spatial_seed42|westd-27271\nOpenVLA|libero_spatial|random|0.5|50.0|yes|eval_openvla_random_k05_spatial_seed42|westd-27271\nOpenVLA|libero_spatial|random|0.9|79.8|yes|eval_openvla_random_k09_spatial_seed42|westd-41074\npi0.5|libero_10|attention|0.5|49.8|no|eval_pi05_attention_k05_long_seed42_v2|cqa1-33015\npi0.5|libero_10|attention|0.7|50.8|no|eval_pi05_attention_k07_long_seed42_v2|cqa1-33015\npi0.5|libero_10|attention|0.75|52.4|no|eval_pi05_attention_k075_long_seed42_v2|cqa1-33015\npi0.5|libero_10|attention|0.75|51.8|no|eval_pi05_attention_k075_long_seed42|cqa1-33015\npi0.5|libero_10|attention|0.85|51.6|no|eval_pi05_attention_k085_long_seed42_v2|cqa1-33015\npi0.5|libero_10|attention|0.9|63.8|no|eval_pi05_attention_k09_long_seed42_postfix|cqa1-33015\npi0.5|libero_10|attention|0.95|77.0|no|eval_pi05_attn_k095_long_seed42|cqa1-33015\npi0.5|libero_10|l2norm|0.3|39.2|yes|eval_pi05_l2norm_k03_long_seed43_postfix_v2|westd-38929\npi0.5|libero_10|l2norm|0.5|53.0|no|eval_pi05_l2norm_k05_long_seed43_postfix_v2|cqa1-33015\npi0.5|libero_10|l2norm|0.5|51.4|yes|eval_pi05_l2norm_k05_long_seed42_v3|westd-41074\npi0.5|libero_10|l2norm|0.5|50.2|no|eval_pi05_l2norm_k05_long_seed42|cqa1-33015\npi0.5|libero_10|l2norm|0.5|50.0|no|eval_pi05_l2norm_k05_long_seed42_v4|cqa1-33015\npi0.5|libero_10|l2norm|0.7|65.8|yes|eval_pi05_l2norm_k07_long_seed43_v2|westd-38929\npi0.5|libero_10|l2norm|0.7|65.4|yes|eval_pi05_l2norm_k07_long_seed43_v4|westd-41074\npi0.5|libero_10|l2norm|0.7|65.0|no|eval_pi05_l2norm_k07_long_seed43_v3|cqa1-33015\npi0.5|libero_10|l2norm|0.7|62.6|yes|eval_pi05_l2norm_k07_long_seed42_postfix|westd-27271\npi0.5|libero_10|l2norm|0.75|73.4|no|eval_pi05_l2norm_k075_long_seed42|cqa1-33015\npi0.5|libero_10|l2norm|0.85|80.0|no|eval_pi05_l2norm_k085_long_seed43_v3|cqa1-33015\npi0.5|libero_10|l2norm|0.85|79.0|yes|eval_pi05_l2norm_k085_long_seed43_v2|westd-38929\npi0.5|libero_10|l2norm|0.85|78.8|yes|eval_pi05_l2norm_k085_long_seed42_v3|\npi0.5|libero_10|l2norm|0.85|78.6|yes|eval_pi05_l2norm_k085_long_seed43_postfix|westd-41074\npi0.5|libero_10|l2norm|0.85|78.4|yes|eval_pi05_l2norm_k085_long_seed42_postfix|westd-41074\npi0.5|libero_10|l2norm|0.85|78.0|no|eval_pi05_l2norm_k085_long_seed42_postfix_v3|cqa1-33015\npi0.5|libero_10|l2norm|0.85|77.8|no|eval_pi05_l2norm_k085_long_seed42_v4|cqa1-33015\npi0.5|libero_10|l2norm|0.85|77.0|yes|eval_pi05_l2norm_k085_long_seed43_v4|westd-41074\npi0.5|libero_10|l2norm|0.9|81.0|yes|eval_pi05_l2norm_k09_long_seed42|westd-41074\npi0.5|libero_10|l2norm|0.9|80.8|no|eval_pi05_l2norm_k09_long_seed43_postfix|cqa1-33015\npi0.5|libero_10|l2norm|0.9|80.0|no|eval_pi05_l2norm_k09_long_seed42_postfix_v2|cqa1-33015\npi0.5|libero_10|l2norm|0.9|80.0|yes|eval_pi05_l2norm_k09_long_seed43_postfix_v2|westd-41074\npi0.5|libero_10|l2norm|0.925|83.2|no|eval_pi05_l2norm_k0925_long_seed42_v2|cqa1-33015\npi0.5|libero_10|l2norm|0.95|87.4|yes|eval_pi05_l2norm_k095_long_seed43_postfix|westd-38929\npi0.5|libero_10|l2norm|0.95|87.0|yes|eval_pi05_l2norm_k095_long_seed42_postfix|westd-38929\npi0.5|libero_10|random|0.3|29.6|yes|eval_pi05_random_k03_long_seed42_postfix|westd-38929\npi0.5|libero_10|random|0.3|29.0|yes|eval_pi05_random_k03_long_seed42|westd-38929\npi0.5|libero_10|random|0.3|28.4|yes|eval_pi05_random_k03_long_seed43_v3|westd-38929\npi0.5|libero_10|random|0.3|28.0|yes|eval_pi05_random_k03_long_seed43_v2|westd-41074\npi0.5|libero_10|random|0.3|27.2|no|eval_pi05_random_k03_long_seed43_v4|cqa1-33015\npi0.5|libero_10|random|0.5|51.2|yes|eval_pi05_random_k05_long_seed43_v2|westd-41074\npi0.5|libero_10|random|0.5|50.2|no|eval_pi05_random_k05_long_seed42_v3|cqa1-33015\npi0.5|libero_10|random|0.5|50.2|no|eval_pi05_random_k05_long_seed42|cqa1-33015\npi0.5|libero_10|random|0.5|46.8|no|eval_pi05_random_k05_long_seed43_postfix|cqa1-33015\npi0.5|libero_10|random|0.5|46.8|yes|eval_pi05_random_k05_long_seed42_postfix|westd-38929\npi0.5|libero_10|random|0.5|46.8|yes|eval_pi05_random_k05_long_seed42_v2|westd-41074\npi0.5|libero_10|random|0.7|68.6|no|eval_pi05_random_k07_long_seed43_postfix|cqa1-33015\npi0.5|libero_10|random|0.7|65.8|yes|eval_pi05_random_k07_long_seed42_postfix|westd-38929\npi0.5|libero_10|random|0.7|62.4|no|eval_pi05_random_k07_long_seed42|cqa1-33015\npi0.5|libero_10|random|0.75|62.4|no|eval_pi05_random_k075_long_seed42_v2|cqa1-33015\npi0.5|libero_10|random|0.85|49.4|no|eval_pi05_random_k085_long_seed42_postfix_v3|cqa1-33015\npi0.5|libero_10|random|0.85|45.2|yes|eval_pi05_random_k085_long_seed42_postfix|westd-41074\npi0.5|libero_10|random|0.85|44.4|no|eval_pi05_random_k085_long_seed42_v2|cqa1-33015\npi0.5|libero_10|random|0.85|44.4|no|eval_pi05_random_k085_long_seed42|cqa1-33015\npi0.5|libero_10|random|0.85|42.4|yes|eval_pi05_random_k085_long_seed43_v3|westd-41074\npi0.5|libero_10|random|0.85|42.0|no|eval_pi05_random_k085_long_seed43_v2|cqa1-33015\npi0.5|libero_10|random|0.85|41.8|no|eval_pi05_random_k085_long_seed43_postfix|cqa1-33015\npi0.5|libero_10|random|0.85|41.8|yes|eval_pi05_random_k085_long_seed43|westd-41074\npi0.5|libero_10|random|0.9|32.0|yes|eval_pi05_random_k09_long_seed42_postfix|westd-41074\npi0.5|libero_10|random|0.9|31.8|yes|eval_pi05_random_k09_long_seed42|westd-38929\npi0.5|libero_10|random|0.925|38.6|no|eval_pi05_random_k0925_long_seed42_postfix|cqa1-33015\npi0.5|libero_10|random|0.95|63.2|yes|eval_pi05_random_k095_long_seed42_postfix|westd-41074\npi0.5|libero_10|random|0.95|61.2|yes|eval_pi05_random_k095_long_seed42|westd-38929\npi0.5|libero_10|random|0.95|58.4|no|eval_pi05_random_k095_long_seed43_postfix|cqa1-33015\npi0.5|libero_goal|attention|0.5|72.2|yes|eval_pi05_attention_k05_goal_seed43|westd-41074\npi0.5|libero_goal|attention|0.5|70.2|yes|eval_pi05_attention_k05_goal_seed42|westd-41074\npi0.5|libero_goal|l2norm|0.3|54.2|no|eval_pi05_l2norm_k03_goal_seed42|cqa1-33015\npi0.5|libero_goal|l2norm|0.3|51.8|yes|eval_pi05_l2norm_k03_goal_seed42_postfix|westd-38929\npi0.5|libero_goal|l2norm|0.3|50.6|no|eval_pi05_l2norm_k03_goal_seed42_v2|cqa1-33015\npi0.5|libero_goal|l2norm|0.5|59.8|yes|eval_pi05_l2norm_k05_goal_seed42_postfix|westd-41074\npi0.5|libero_goal|l2norm|0.5|59.2|yes|eval_pi05_l2norm_k05_goal_seed42|westd-41074\npi0.5|libero_goal|l2norm|0.7|73.6|no|eval_pi05_l2norm_k07_goal_seed42_v2|cqa1-33015\npi0.5|libero_goal|l2norm|0.7|72.2|yes|eval_pi05_l2norm_k07_goal_seed43_v2|westd-41074\npi0.5|libero_goal|l2norm|0.7|70.2|yes|eval_pi05_l2norm_k07_goal_seed42_postfix|westd-41074\npi0.5|libero_goal|l2norm|0.85|88.0|no|eval_pi05_l2norm_k085_goal_seed42|cqa1-33015\npi0.5|libero_goal|l2norm|0.85|87.4|yes|eval_pi05_l2norm_k085_goal_seed42_postfix|westd-41074\npi0.5|libero_goal|l2norm|0.85|87.0|no|eval_pi05_l2norm_k085_goal_seed43_postfix|cqa1-33015\npi0.5|libero_goal|l2norm|0.85|87.0|no|eval_pi05_l2norm_k085_goal_seed43|cqa1-33015\npi0.5|libero_goal|l2norm|0.9|91.0|yes|eval_pi05_l2norm_k09_goal_seed43_postfix|westd-41074\npi0.5|libero_goal|l2norm|0.9|90.6|no|eval_pi05_l2norm_k09_goal_seed42_v2|cqa1-33015\npi0.5|libero_goal|l2norm|0.9|90.0|yes|eval_pi05_l2norm_k09_goal_seed42|westd-38929\npi0.5|libero_goal|l2norm|0.9|88.6|yes|eval_pi05_l2norm_k09_goal_seed42_postfix|westd-41074\npi0.5|libero_goal|l2norm|0.925|90.8|yes|eval_pi05_l2norm_k0925_goal_seed43|westd-41074\npi0.5|libero_goal|l2norm|0.925|89.8|yes|eval_pi05_l2norm_k0925_goal_seed42_postfix|westd-38929\npi0.5|libero_goal|l2norm|0.925|89.8|yes|eval_pi05_l2norm_k0925_goal_seed42_v3|westd-41074\npi0.5|libero_goal|l2norm|0.925|89.0|yes|eval_pi05_l2norm_k0925_goal_seed42_v2|westd-41074\npi0.5|libero_goal|l2norm|0.95|90.8|no|eval_pi05_l2norm_k095_goal_seed42_postfix|cqa1-33015\npi0.5|libero_goal|l2norm|0.95|90.8|no|eval_pi05_l2norm_k095_goal_seed42|cqa1-33015\npi0.5|libero_goal|l2norm|0.95|89.4|no|eval_pi05_l2norm_k095_goal_seed42_v2|cqa1-33015\npi0.5|libero_goal|random|0.3|53.6|no|eval_pi05_random_k03_goal_seed43_v2|cqa1-33015\npi0.5|libero_goal|random|0.3|52.8|yes|eval_pi05_random_k03_goal_seed42_postfix|westd-41074\npi0.5|libero_goal|random|0.3|51.0|no|eval_pi05_random_k03_goal_seed42|cqa1-33015\npi0.5|libero_goal|random|0.3|50.6|yes|eval_pi05_random_k03_goal_seed42_v2|westd-41074\npi0.5|libero_goal|random|0.5|73.6|no|eval_pi05_random_k05_goal_seed42_postfix|cqa1-33015\npi0.5|libero_goal|random|0.5|73.6|no|eval_pi05_random_k05_goal_seed42_v2|cqa1-33015\npi0.5|libero_goal|random|0.7|80.6|no|eval_pi05_random_k07_goal_seed42|cqa1-33015\npi0.5|libero_goal|random|0.7|78.2|yes|eval_pi05_random_k07_goal_seed42_v2|westd-41074\npi0.5|libero_goal|random|0.7|75.6|yes|eval_pi05_random_k07_goal_seed42_postfix|westd-38929\npi0.5|libero_goal|random|0.85|53.4|yes|eval_pi05_random_k085_goal_seed43_postfix|westd-41074\npi0.5|libero_goal|random|0.85|53.0|no|eval_pi05_random_k085_goal_seed42_postfix_v3|cqa1-33015\npi0.5|libero_goal|random|0.85|52.8|yes|eval_pi05_random_k085_goal_seed42_postfix|westd-38929\npi0.5|libero_goal|random|0.85|52.4|no|eval_pi05_random_k085_goal_seed42_v4|cqa1-33015\npi0.5|libero_goal|random|0.85|52.4|yes|eval_pi05_random_k085_goal_seed42_v3|westd-38929\npi0.5|libero_goal|random|0.85|52.2|yes|eval_pi05_random_k085_goal_seed43|westd-41074\npi0.5|libero_goal|random|0.9|62.2|yes|eval_pi05_random_k09_goal_seed42_v2|westd-41074\npi0.5|libero_goal|random|0.9|61.8|yes|eval_pi05_random_k09_goal_seed42_postfix|westd-38929\npi0.5|libero_goal|random|0.9|61.2|yes|eval_pi05_random_k09_goal_seed43_postfix|westd-41074\npi0.5|libero_goal|random|0.925|71.2|yes|eval_pi05_random_k0925_goal_seed42_v2|westd-41074\npi0.5|libero_goal|random|0.925|70.0|yes|eval_pi05_random_k0925_goal_seed42_v3|westd-41074\npi0.5|libero_goal|random|0.95|83.8|yes|eval_pi05_random_k095_goal_seed42_v2|westd-41074\npi0.5|libero_goal|random|0.95|83.4|yes|eval_pi05_random_k095_goal_seed43|westd-41074\npi0.5|libero_goal|random|0.95|82.6|yes|eval_pi05_random_k095_goal_seed42_postfix|westd-38929\npi0.5|libero_object|attention|0.5|37.8|yes|eval_pi05_attention_k05_object_seed42|westd-41074\npi0.5|libero_object|attention|0.7|0.6|yes|eval_pi05_attention_k07_object_seed42|westd-41074\npi0.5|libero_object|attention|0.85|92.2|yes|eval_pi05_attention_k085_object_seed42|westd-41074\npi0.5|libero_object|attention|0.9|97.2|yes|eval_pi05_attention_k09_object_seed42|westd-41074\npi0.5|libero_object|attention|0.95|98.4|yes|eval_pi05_attention_k095_object_seed42|westd-41074\npi0.5|libero_object|l2norm|0.1|2.6|yes|eval_pi05_l2norm_k01_object_seed42|westd-41074\npi0.5|libero_object|l2norm|0.3|51.0|yes|eval_pi05_l2norm_k03_object_seed42|westd-41074\npi0.5|libero_object|l2norm|0.5|33.6|yes|eval_pi05_l2norm_k05_object_seed43|westd-41074\npi0.5|libero_object|l2norm|0.5|33.4|yes|eval_pi05_l2norm_k05_object_seed42|westd-41074\npi0.5|libero_object|l2norm|0.7|56.4|yes|eval_pi05_l2norm_k07_object_seed42_postfix|westd-38929\npi0.5|libero_object|l2norm|0.7|56.4|yes|eval_pi05_l2norm_k07_object_seed43|westd-41074\npi0.5|libero_object|l2norm|0.7|55.0|yes|eval_pi05_l2norm_k07_object_seed42|westd-41074\npi0.5|libero_object|l2norm|0.85|99.0|no|eval_pi05_l2norm_k085_object_seed43_postfix|cqa1-33015\npi0.5|libero_object|l2norm|0.85|98.4|no|eval_pi05_l2norm_k085_object_seed42_postfix_v2|cqa1-33015\npi0.5|libero_object|l2norm|0.85|98.4|yes|eval_pi05_l2norm_k085_object_seed43|westd-41074\npi0.5|libero_object|l2norm|0.85|98.0|yes|eval_pi05_l2norm_k085_object_seed42_v4|westd-41074\npi0.5|libero_object|l2norm|0.9|98.4|yes|eval_pi05_l2norm_k09_object_seed43_postfix|westd-41074\npi0.5|libero_object|l2norm|0.9|98.2|yes|eval_pi05_l2norm_k09_object_seed42_v2|westd-41074\npi0.5|libero_object|l2norm|0.925|99.2|yes|eval_pi05_l2norm_k0925_object_seed42|\npi0.5|libero_object|l2norm|0.95|98.4|no|eval_pi05_l2norm_k095_object_seed43|cqa1-33015\npi0.5|libero_object|l2norm|0.95|98.2|yes|eval_pi05_l2norm_k095_object_seed42_v2|westd-41074\npi0.5|libero_object|l2norm_zeromask|0.9|99.4|no|eval_pi05_zeromask_l2norm_k09_object_seed42|cqa1-33015\npi0.5|libero_object|random|0.3|36.4|yes|eval_pi05_random_k03_object_seed42|westd-41074\npi0.5|libero_object|random|0.3|32.2|yes|eval_pi05_random_k03_object_seed43_v4|westd-38929\npi0.5|libero_object|random|0.5|69.4|yes|eval_pi05_random_k05_object_seed42|westd-41074\npi0.5|libero_object|random|0.5|68.4|yes|eval_pi05_random_k05_object_seed43|westd-41074\npi0.5|libero_object|random|0.5|68.2|no|eval_pi05_random_k05_object_seed42_v2|cqa1-33015\npi0.5|libero_object|random|0.7|77.2|yes|eval_pi05_random_k07_object_seed42|westd-41074\npi0.5|libero_object|random|0.7|74.0|no|eval_pi05_random_k07_object_seed42_v4|cqa1-33015\npi0.5|libero_object|random|0.7|74.0|yes|eval_pi05_random_k07_object_seed42_v3|\npi0.5|libero_object|random|0.7|73.8|yes|eval_pi05_random_k07_object_seed43|westd-41074\npi0.5|libero_object|random|0.85|5.6|yes|eval_pi05_random_k085_object_seed42_postfix|westd-41074\npi0.5|libero_object|random|0.85|5.0|yes|eval_pi05_random_k085_object_seed42_v2|westd-38929\npi0.5|libero_object|random|0.85|4.8|no|eval_pi05_random_k085_object_seed43_postfix|cqa1-33015\npi0.5|libero_object|random|0.85|3.8|yes|eval_pi05_random_k085_object_seed43|westd-41074\npi0.5|libero_object|random|0.9|9.6|yes|eval_pi05_random_k09_object_seed43|westd-41074\npi0.5|libero_object|random|0.9|9.6|yes|eval_pi05_random_k09_object_seed43_v4|westd-41074\npi0.5|libero_object|random|0.9|9.6|yes|eval_pi05_random_k09_object_seed43_v3|westd-27271\npi0.5|libero_object|random|0.9|9.0|no|eval_pi05_random_k09_object_seed42_v2|cqa1-33015\npi0.5|libero_object|random|0.9|7.4|yes|eval_pi05_random_k09_object_seed43_postfix|westd-41074\npi0.5|libero_object|random|0.925|30.0|yes|eval_pi05_random_k0925_object_seed43|westd-38929\npi0.5|libero_object|random|0.925|27.6|yes|eval_pi05_random_k0925_object_seed42|westd-41074\npi0.5|libero_object|random|0.925|27.2|yes|eval_pi05_random_k0925_object_seed42_postfix|westd-41074\npi0.5|libero_object|random|0.95|74.0|yes|eval_pi05_random_k095_object_seed42_v2|\npi0.5|libero_object|random|0.95|72.8|yes|eval_pi05_random_k095_object_seed43|westd-41074\npi0.5|libero_object|random_fixedmask|0.9|17.0|yes|eval_pi05_random_k09_fixedmask_object_seed42_v2|\npi0.5|libero_object|random_zeromask|0.9|98.0|yes|eval_pi05_zeromask_random_k09_object_seed42_v3|westd-41074\npi0.5|libero_spatial|attention|0.5|72.6|yes|eval_pi05_attention_k05_spatial_seed42|westd-41074\npi0.5|libero_spatial|l2norm|0.3|57.2|yes|eval_pi05_l2norm_k03_spatial_seed42|westd-38929\npi0.5|libero_spatial|l2norm|0.3|52.8|no|eval_pi05_l2norm_k03_spatial_seed42_postfix|cqa1-33015\npi0.5|libero_spatial|l2norm|0.3|52.0|yes|eval_pi05_l2norm_k03_spatial_seed43|westd-38929\npi0.5|libero_spatial|l2norm|0.5|58.2|yes|eval_pi05_l2norm_k05_spatial_seed43|westd-41074\npi0.5|libero_spatial|l2norm|0.5|57.4|no|eval_pi05_l2norm_k05_spatial_seed42_postfix|cqa1-33015\npi0.5|libero_spatial|l2norm|0.5|55.6|yes|eval_pi05_l2norm_k05_spatial_seed42|westd-38929\npi0.5|libero_spatial|l2norm|0.5|55.4|yes|eval_pi05_l2norm_k05_spatial_seed43_v2|westd-41074\npi0.5|libero_spatial|l2norm|0.7|68.4|yes|eval_pi05_l2norm_k07_spatial_seed43|westd-27271\npi0.5|libero_spatial|l2norm|0.7|67.0|yes|eval_pi05_l2norm_k07_spatial_seed42|westd-38929\npi0.5|libero_spatial|l2norm|0.85|88.6|yes|eval_pi05_l2norm_k085_spatial_seed42_v2|westd-41074\npi0.5|libero_spatial|l2norm|0.85|88.4|yes|eval_pi05_l2norm_k085_spatial_seed42_v3|westd-41074\npi0.5|libero_spatial|l2norm|0.85|88.2|no|eval_pi05_l2norm_k085_spatial_seed43_postfix|cqa1-33015\npi0.5|libero_spatial|l2norm|0.85|88.0|yes|eval_pi05_l2norm_k085_spatial_seed43|westd-27271\npi0.5|libero_spatial|l2norm|0.9|96.2|yes|eval_pi05_l2norm_k09_spatial_seed43_postfix|westd-38929\npi0.5|libero_spatial|l2norm|0.9|96.0|yes|eval_pi05_l2norm_k09_spatial_seed42_postfix|westd-38929\npi0.5|libero_spatial|l2norm|0.9|95.6|no|eval_pi05_l2norm_k09_spatial_seed43|cqa1-33015\npi0.5|libero_spatial|l2norm|0.925|97.0|no|eval_pi05_l2norm_k0925_spatial_seed42|cqa1-33015\npi0.5|libero_spatial|l2norm|0.95|98.0|no|eval_pi05_l2norm_k095_spatial_seed43|cqa1-33015\npi0.5|libero_spatial|l2norm|0.95|97.8|yes|eval_pi05_l2norm_k095_spatial_seed42|westd-38929\npi0.5|libero_spatial|random|0.3|51.2|yes|eval_pi05_random_k03_spatial_seed43|westd-38929\npi0.5|libero_spatial|random|0.3|49.6|yes|eval_pi05_random_k03_spatial_seed42|westd-38929\npi0.5|libero_spatial|random|0.3|43.4|no|eval_pi05_random_k03_spatial_seed42_postfix_v2|cqa1-33015\npi0.5|libero_spatial|random|0.5|72.4|yes|eval_pi05_random_k05_spatial_seed43_v2|westd-41074\npi0.5|libero_spatial|random|0.5|71.8|no|eval_pi05_random_k05_spatial_seed42_postfix_v3|cqa1-33015\npi0.5|libero_spatial|random|0.5|71.6|yes|eval_pi05_random_k05_spatial_seed42|\npi0.5|libero_spatial|random|0.7|74.4|yes|eval_pi05_random_k07_spatial_seed42|westd-38929\npi0.5|libero_spatial|random|0.7|73.8|no|eval_pi05_random_k07_spatial_seed42_postfix|cqa1-33015\npi0.5|libero_spatial|random|0.7|73.8|yes|eval_pi05_random_k07_spatial_seed43|westd-27271\npi0.5|libero_spatial|random|0.85|60.8|no|eval_pi05_random_k085_spatial_seed42_postfix_v2|cqa1-33015\npi0.5|libero_spatial|random|0.85|60.2|yes|eval_pi05_random_k085_spatial_seed42_v3|westd-41074\npi0.5|libero_spatial|random|0.85|59.2|no|eval_pi05_random_k085_spatial_seed43_postfix|cqa1-33015\npi0.5|libero_spatial|random|0.85|58.4|yes|eval_pi05_random_k085_spatial_seed42|westd-41074\npi0.5|libero_spatial|random|0.85|57.6|yes|eval_pi05_random_k085_spatial_seed43|westd-38929\npi0.5|libero_spatial|random|0.85|56.6|yes|eval_pi05_random_k085_spatial_seed42_v2|westd-41074\npi0.5|libero_spatial|random|0.9|54.0|yes|eval_pi05_random_k09_spatial_seed43_postfix_v2|westd-41074\npi0.5|libero_spatial|random|0.9|53.6|no|eval_pi05_random_k09_spatial_seed43|cqa1-33015\npi0.5|libero_spatial|random|0.9|53.4|no|eval_pi05_random_k09_spatial_seed42_postfix_v2|cqa1-33015\npi0.5|libero_spatial|random|0.925|58.2|yes|eval_pi05_random_k0925_spatial_seed42_unreg|westd-41074\npi0.5|libero_spatial|random|0.925|57.8|no|eval_pi05_random_k0925_spatial_seed43|cqa1-33015\npi0.5|libero_spatial|random|0.95|76.8|no|eval_pi05_random_k095_spatial_seed42_postfix_v2|cqa1-33015\npi0.5|libero_spatial|random|0.95|76.8|yes|eval_pi05_random_k095_spatial_seed43|westd-27271",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  }
}
```

</details>

---


### Assistant

_source line 34_

<details><summary>Logged reasoning block</summary>

```text
Now I have all the data. The k-values are fixed now. I need to:

1. Deduplicate - for each (model, suite, method, k) combination, pick the best reliable data point. When multiple seeds exist, average them. When there are version duplicates of the same seed, pick the latest version.

2. Exclude zeromask and fixedmask variants (they're different methods)

3. Add baseline values for k=1.0

4. Also need to handle the fact that some experiments without a method label exist (OpenVLA Object with no method - those seem to be early experiments, probably l2norm based on patterns)


Now I'm building a script that filters to reliable experiments, selects the latest version for each seed, then averages success rates across seeds for each (model, suite, method, k) combination.

Wait, I need to reconsider what the task actually wants. The CSV should include all data points with reliability flags rather than aggregated averages. But I do need to handle duplicates—when the same experiment appears multiple times with identical results, I should keep only one. For versioned experiments like v2, v3, v4, I should prefer the latest version.

For different seeds, I should keep them as separate rows since the task asks for individual data points with exp_id. Let me write a script that deduplicates exact registrations and version chains while preserving all distinct experimental runs.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "076e70a6-b6da-4158-a720-52786daa428f",
  "uuid": "6aaf105b-b814-4565-94b8-18ab92148ff7",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01M6rrztUBLT2ouXHBVA4icr",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 14902,
      "cache_read_input_tokens": 47789,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 14902
      },
      "output_tokens": 9,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---


### Assistant

_source line 35_

Data looks good now. Let me build the final deduplicated CSV with proper handling.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "076e70a6-b6da-4158-a720-52786daa428f",
  "uuid": "bd554cd6-c729-4301-84f9-2b349a5a3564",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01M6rrztUBLT2ouXHBVA4icr",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 14902,
      "cache_read_input_tokens": 47789,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 14902
      },
      "output_tokens": 9,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---


### Tool call

_source line 36_

<details open><summary>🔧 Tool call — Bash · `toolu_01LBReQujkpaFqjpcX2b4hMi`</summary>

```json
{
  "command": "cat /home/ubuntu/.claude-account-4/projects/-home-ubuntu--agent-ml-research-be-idea-gen-0515-2-projects-importance-margin-vla-compress/076e70a6-b6da-4158-a720-52786daa428f/tool-results/mcp-agent-ml-research-read_registry-1779856199105.txt | python3 << 'PYEOF'\nimport json, sys, re, csv, io\n\ndata = json.loads(sys.stdin.read())\nresult = json.loads(data['result'])\nexperiments = result['data']['experiments']\n\nrows = []\nfor eid, exp in experiments.items():\n    c = exp.get('conclusion', '')\n    if c not in ('success', 'negative'):\n        continue\n    \n    metrics = exp.get('metrics', {})\n    spec = exp.get('spec', {})\n    server = spec.get('server', '')\n    notes = exp.get('notes', '') or ''\n    model_name = spec.get('model_name', '') or ''\n    updated_at = exp.get('updated_at', '')\n    \n    sr = metrics.get('overall_sr') or metrics.get('success_rate') or metrics.get('overall_SR') or metrics.get('avg_sr')\n    if sr is None:\n        continue\n    \n    eid_lower = eid.lower()\n    is_openvla = 'openvla' in eid_lower or 'openvla' in model_name.lower()\n    is_pi05 = 'pi05' in eid_lower or 'pi0.5' in model_name.lower() or 'pi05' in model_name.lower()\n    is_eval = 'eval' in eid_lower\n    \n    if not (is_openvla or is_pi05) or not is_eval:\n        continue\n    \n    # Skip zeromask/fixedmask variants\n    if 'zeromask' in eid_lower or 'fixedmask' in eid_lower:\n        continue\n    \n    # Method\n    method = ''\n    if 'l2norm' in eid_lower: method = 'l2norm'\n    elif 'attn' in eid_lower or 'attention' in eid_lower: method = 'attention'\n    elif 'random' in eid_lower: method = 'random'\n    elif 'wanda' in eid_lower: method = 'wanda'\n    if not method:\n        method = metrics.get('prune_method', '') or spec.get('prune_method', '')\n    if not method:\n        continue  # skip experiments without a method\n    \n    # k value\n    k = None\n    kr = metrics.get('keep_ratio') or spec.get('keep_ratio')\n    if kr:\n        k = float(kr)\n    else:\n        k_match = re.search(r'_k(\\d+)', '_' + eid_lower)\n        if k_match:\n            kstr = k_match.group(1)\n            kmap = {'01':0.1,'03':0.3,'05':0.5,'07':0.7,'075':0.75,'085':0.85,'09':0.9,'0925':0.925,'095':0.95,'1':1.0,'3':0.3,'5':0.5,'7':0.7,'9':0.9}\n            k = kmap.get(kstr)\n            if k is None:\n                try: k = float('0.' + kstr)\n                except: pass\n    if k is None:\n        continue\n    \n    # Suite\n    suite_norm = ''\n    suite_raw = (spec.get('data_path', '') or spec.get('eval_data', '') or '').lower()\n    combined = suite_raw + ' ' + eid_lower\n    if 'object' in combined: suite_norm = 'libero_object'\n    elif 'spatial' in combined: suite_norm = 'libero_spatial'\n    elif 'goal' in combined: suite_norm = 'libero_goal'\n    elif 'long' in combined or 'libero_10' in combined: suite_norm = 'libero_10'\n    if not suite_norm:\n        continue\n    \n    model = 'OpenVLA' if is_openvla else 'pi0.5'\n    \n    # Normalize SR to percentage\n    sr_val = float(sr)\n    if sr_val <= 1.0 and sr_val > 0:\n        sr_val = sr_val * 100\n    sr_val = round(sr_val, 1)\n    \n    # Reliability\n    reliable = 'yes'\n    if model == 'pi0.5' and 'cqa1' in server and 'strict' not in eid_lower:\n        reliable = 'no'\n    if 'contaminated' in notes.lower() or 'lenient' in notes.lower():\n        reliable = 'no'\n    \n    # Extract seed\n    seed_match = re.search(r'seed(\\d+)', eid_lower)\n    seed = int(seed_match.group(1)) if seed_match else 42\n    \n    # Extract version\n    ver_match = re.search(r'_v(\\d+)$', eid_lower)\n    version = int(ver_match.group(1)) if ver_match else 0\n    \n    # Check for postfix\n    has_postfix = 'postfix' in eid_lower\n    \n    rows.append({\n        'model': model, 'suite': suite_norm, 'method': method, 'k': k,\n        'sr': sr_val, 'reliable': reliable, 'exp_id': eid, 'server': server,\n        'notes': notes[:150].replace('\\n', ' '),\n        'seed': seed, 'version': version, 'has_postfix': has_postfix,\n        'updated_at': updated_at\n    })\n\n# Deduplication strategy:\n# For each (model, suite, method, k, seed, reliable_status), keep only the latest version\n# Priority: higher version number > postfix > earlier version\n# If same version, prefer the one with later updated_at\n\ndef dedup_key(r):\n    return (r['model'], r['suite'], r['method'], r['k'], r['seed'], r['reliable'])\n\nfrom collections import defaultdict\ngroups = defaultdict(list)\nfor r in rows:\n    groups[dedup_key(r)].append(r)\n\ndeduped = []\nfor key, group in groups.items():\n    # Sort by version desc, then postfix (True > False), then updated_at desc\n    group.sort(key=lambda x: (x['version'], x['has_postfix'], x['updated_at']), reverse=True)\n    deduped.append(group[0])\n\n# Also remove exact SR duplicates within same (model, suite, method, k) that are clearly the same experiment registered twice\n# (different exp_id but identical SR, same server)\nfinal_dedup = []\nseen = set()\nfor r in deduped:\n    dedup_sig = (r['model'], r['suite'], r['method'], r['k'], r['sr'], r['seed'])\n    if dedup_sig not in seen:\n        seen.add(dedup_sig)\n        final_dedup.append(r)\n\n# Add baseline rows (k=1.0)\nbaselines = [\n    {'model': 'OpenVLA', 'suite': 'libero_object', 'method': 'baseline', 'k': 1.0, 'sr': 74.0, 'reliable': 'yes', 'exp_id': 'baseline_openvla_object', 'server': '', 'notes': 'OpenVLA fine-tuned baseline (no pruning)'},\n    {'model': 'OpenVLA', 'suite': 'libero_goal', 'method': 'baseline', 'k': 1.0, 'sr': 74.8, 'reliable': 'yes', 'exp_id': 'baseline_openvla_goal', 'server': '', 'notes': 'OpenVLA fine-tuned baseline (no pruning)'},\n    {'model': 'OpenVLA', 'suite': 'libero_10', 'method': 'baseline', 'k': 1.0, 'sr': 52.8, 'reliable': 'yes', 'exp_id': 'baseline_openvla_long', 'server': '', 'notes': 'OpenVLA fine-tuned baseline (no pruning)'},\n]\n\n# Find pi0.5 baselines from registry\npi05_baselines = {}\nfor eid, exp in experiments.items():\n    if exp.get('conclusion') not in ('success', 'negative'):\n        continue\n    eid_lower = eid.lower()\n    if 'baseline' in eid_lower and 'pi05' in eid_lower:\n        metrics = exp.get('metrics', {})\n        sr = metrics.get('overall_sr') or metrics.get('success_rate') or metrics.get('overall_SR')\n        if sr is not None:\n            print(f\"PI05 baseline found: {eid} sr={sr} metrics={list(metrics.keys())}\", file=sys.stderr)\n\nfinal_dedup.extend(baselines)\n\n# Sort\nfinal_dedup.sort(key=lambda r: (r['model'], r['suite'], r['method'], r['k']))\n\n# Write CSV\noutput = io.StringIO()\nwriter = csv.writer(output)\nwriter.writerow(['model', 'suite', 'method', 'k', 'sr', 'reliable', 'exp_id', 'server', 'notes'])\nfor r in final_dedup:\n    writer.writerow([r['model'], r['suite'], r['method'], r['k'], r['sr'], r['reliable'], r['exp_id'], r['server'], r['notes'][:100]])\n\ncsv_content = output.getvalue()\nprint(csv_content)\nprint(f\"\\n--- Total rows: {len(final_dedup)} ---\", file=sys.stderr)\nPYEOF\n",
  "description": "Build final deduplicated CSV with baselines",
  "timeout": 30000
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "076e70a6-b6da-4158-a720-52786daa428f",
  "uuid": "ab89949e-dcbf-4d15-a0e5-1024f5784674",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01M6rrztUBLT2ouXHBVA4icr",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 14902,
      "cache_read_input_tokens": 47789,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 14902
      },
      "output_tokens": 9,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---


### Tool result

_source line 37 · 2026-05-27T04:34:16.251Z_

<details><summary>↩ Tool result · reported error · `toolu_01LBReQujkpaFqjpcX2b4hMi`</summary>

```text
Exit code 1
Traceback (most recent call last):
  File "&lt;stdin>", line 3, in &lt;module>
  File "/usr/lib/python3.14/json/__init__.py", line 352, in loads
    return _default_decoder.decode(s)
           ~~~~~~~~~~~~~~~~~~~~~~~^^^
  File "/usr/lib/python3.14/json/decoder.py", line 345, in decode
    obj, end = self.raw_decode(s, idx=_w(s, 0).end())
               ~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/lib/python3.14/json/decoder.py", line 363, in raw_decode
    raise JSONDecodeError("Expecting value", s, err.value) from None
json.decoder.JSONDecodeError: Expecting value: line 1 column 1 (char 0)
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "076e70a6-b6da-4158-a720-52786daa428f",
  "uuid": "b024e7a8-abd0-4ae6-a519-2f580793b197",
  "tool_use_result": "Error: Exit code 1\nTraceback (most recent call last):\n  File \"&lt;stdin>\", line 3, in &lt;module>\n  File \"/usr/lib/python3.14/json/__init__.py\", line 352, in loads\n    return _default_decoder.decode(s)\n           ~~~~~~~~~~~~~~~~~~~~~~~^^^\n  File \"/usr/lib/python3.14/json/decoder.py\", line 345, in decode\n    obj, end = self.raw_decode(s, idx=_w(s, 0).end())\n               ~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^\n  File \"/usr/lib/python3.14/json/decoder.py\", line 363, in raw_decode\n    raise JSONDecodeError(\"Expecting value\", s, err.value) from None\njson.decoder.JSONDecodeError: Expecting value: line 1 column 1 (char 0)"
}
```

</details>

---


### Tool call

_source line 38_

<details open><summary>🔧 Tool call — Bash · `toolu_01J5uiLfqmhkVJusxTiCpZwm`</summary>

```json
{
  "command": "python3 << 'PYEOF'\nimport json, re, csv, io\nfrom collections import defaultdict\n\n# Read the file\nwith open('/home/ubuntu/.claude-account-4/projects/-home-ubuntu--agent-ml-research-be-idea-gen-0515-2-projects-importance-margin-vla-compress/076e70a6-b6da-4158-a720-52786daa428f/tool-results/mcp-agent-ml-research-read_registry-1779856199105.txt') as f:\n    data = json.load(f)\n\nresult = json.loads(data['result'])\nexperiments = result['data']['experiments']\n\nrows = []\nfor eid, exp in experiments.items():\n    c = exp.get('conclusion', '')\n    if c not in ('success', 'negative'):\n        continue\n    \n    metrics = exp.get('metrics', {})\n    spec = exp.get('spec', {})\n    server = spec.get('server', '')\n    notes = exp.get('notes', '') or ''\n    model_name = spec.get('model_name', '') or ''\n    updated_at = exp.get('updated_at', '')\n    \n    sr = metrics.get('overall_sr') or metrics.get('success_rate') or metrics.get('overall_SR') or metrics.get('avg_sr')\n    if sr is None:\n        continue\n    \n    eid_lower = eid.lower()\n    is_openvla = 'openvla' in eid_lower or 'openvla' in model_name.lower()\n    is_pi05 = 'pi05' in eid_lower or 'pi0.5' in model_name.lower() or 'pi05' in model_name.lower()\n    is_eval = 'eval' in eid_lower\n    \n    if not (is_openvla or is_pi05) or not is_eval:\n        continue\n    if 'zeromask' in eid_lower or 'fixedmask' in eid_lower:\n        continue\n    \n    method = ''\n    if 'l2norm' in eid_lower: method = 'l2norm'\n    elif 'attn' in eid_lower or 'attention' in eid_lower: method = 'attention'\n    elif 'random' in eid_lower: method = 'random'\n    elif 'wanda' in eid_lower: method = 'wanda'\n    if not method:\n        method = metrics.get('prune_method', '') or spec.get('prune_method', '')\n    if not method:\n        continue\n    \n    k = None\n    kr = metrics.get('keep_ratio') or spec.get('keep_ratio')\n    if kr:\n        k = float(kr)\n    else:\n        k_match = re.search(r'_k(\\d+)', '_' + eid_lower)\n        if k_match:\n            kstr = k_match.group(1)\n            kmap = {'01':0.1,'03':0.3,'05':0.5,'07':0.7,'075':0.75,'085':0.85,'09':0.9,'0925':0.925,'095':0.95,'1':1.0}\n            k = kmap.get(kstr)\n            if k is None:\n                try: k = float('0.' + kstr)\n                except: pass\n    if k is None:\n        continue\n    \n    suite_norm = ''\n    suite_raw = (spec.get('data_path', '') or spec.get('eval_data', '') or '').lower()\n    combined = suite_raw + ' ' + eid_lower\n    if 'object' in combined: suite_norm = 'libero_object'\n    elif 'spatial' in combined: suite_norm = 'libero_spatial'\n    elif 'goal' in combined: suite_norm = 'libero_goal'\n    elif 'long' in combined or 'libero_10' in combined: suite_norm = 'libero_10'\n    if not suite_norm:\n        continue\n    \n    model = 'OpenVLA' if is_openvla else 'pi0.5'\n    \n    sr_val = float(sr)\n    if sr_val <= 1.0 and sr_val > 0:\n        sr_val = sr_val * 100\n    sr_val = round(sr_val, 1)\n    \n    reliable = 'yes'\n    if model == 'pi0.5' and 'cqa1' in server and 'strict' not in eid_lower:\n        reliable = 'no'\n    if 'contaminated' in notes.lower() or 'lenient' in notes.lower():\n        reliable = 'no'\n    \n    seed_match = re.search(r'seed(\\d+)', eid_lower)\n    seed = int(seed_match.group(1)) if seed_match else 42\n    \n    ver_match = re.search(r'_v(\\d+)', eid_lower)\n    version = int(ver_match.group(1)) if ver_match else 0\n    \n    has_postfix = 'postfix' in eid_lower\n    \n    rows.append({\n        'model': model, 'suite': suite_norm, 'method': method, 'k': k,\n        'sr': sr_val, 'reliable': reliable, 'exp_id': eid, 'server': server,\n        'notes': notes[:150].replace('\\n', ' '),\n        'seed': seed, 'version': version, 'has_postfix': has_postfix,\n        'updated_at': updated_at\n    })\n\n# Dedup: for each (model, suite, method, k, seed, reliable), keep latest version\ndef dedup_key(r):\n    return (r['model'], r['suite'], r['method'], r['k'], r['seed'], r['reliable'])\n\ngroups = defaultdict(list)\nfor r in rows:\n    groups[dedup_key(r)].append(r)\n\ndeduped = []\nfor key, group in groups.items():\n    group.sort(key=lambda x: (x['version'], x['has_postfix'], x['updated_at']), reverse=True)\n    deduped.append(group[0])\n\n# Remove exact SR duplicates\nfinal_dedup = []\nseen = set()\nfor r in deduped:\n    dedup_sig = (r['model'], r['suite'], r['method'], r['k'], r['sr'], r['seed'])\n    if dedup_sig not in seen:\n        seen.add(dedup_sig)\n        final_dedup.append(r)\n\n# Baselines k=1.0\nbaselines = [\n    {'model': 'OpenVLA', 'suite': 'libero_object', 'method': 'baseline', 'k': 1.0, 'sr': 74.0, 'reliable': 'yes', 'exp_id': 'baseline_openvla_object', 'server': '', 'notes': 'OpenVLA fine-tuned baseline (no pruning)'},\n    {'model': 'OpenVLA', 'suite': 'libero_goal', 'method': 'baseline', 'k': 1.0, 'sr': 74.8, 'reliable': 'yes', 'exp_id': 'baseline_openvla_goal', 'server': '', 'notes': 'OpenVLA fine-tuned baseline (no pruning)'},\n    {'model': 'OpenVLA', 'suite': 'libero_10', 'method': 'baseline', 'k': 1.0, 'sr': 52.8, 'reliable': 'yes', 'exp_id': 'baseline_openvla_long', 'server': '', 'notes': 'OpenVLA fine-tuned baseline (no pruning)'},\n]\n\n# Look for pi0.5 baseline (full model, no pruning) from registry\nfor eid, exp in experiments.items():\n    if exp.get('conclusion') not in ('success', 'negative'):\n        continue\n    eid_lower = eid.lower()\n    metrics = exp.get('metrics', {})\n    # Look for pi0.5 baseline experiments\n    if ('pi05' in eid_lower or 'pi0.5' in (exp.get('spec', {}).get('model_name', '') or '').lower()) and 'baseline' in eid_lower:\n        sr = metrics.get('overall_sr') or metrics.get('success_rate') or metrics.get('overall_SR')\n        spec = exp.get('spec', {})\n        suite_raw = (spec.get('data_path', '') or spec.get('eval_data', '') or '').lower()\n        server = spec.get('server', '')\n        print(f\"PI05 baseline: {eid} suite={suite_raw} sr={sr} server={server}\")\n\nfinal_dedup.extend(baselines)\nfinal_dedup.sort(key=lambda r: (r['model'], r['suite'], r['method'], r['k']))\n\n# Write CSV\noutput = io.StringIO()\nwriter = csv.writer(output)\nwriter.writerow(['model', 'suite', 'method', 'k', 'sr', 'reliable', 'exp_id', 'server', 'notes'])\nfor r in final_dedup:\n    writer.writerow([r['model'], r['suite'], r['method'], r['k'], r['sr'], r['reliable'], r['exp_id'], r['server'], r['notes'][:100]])\n\ncsv_content = output.getvalue()\n\n# Save to file\noutpath = '/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/artifacts/cliff_curve_data.csv'\nwith open(outpath, 'w') as f:\n    f.write(csv_content)\n\nprint(f\"Saved {len(final_dedup)} rows to {outpath}\")\nprint()\n\n# Summary\nfrom collections import Counter\ncombos = Counter()\nfor r in final_dedup:\n    combos[(r['model'], r['suite'], r['method'])] += 1\n\nprint(\"Data points per (model, suite, method):\")\nfor key in sorted(combos.keys()):\n    print(f\"  {key}: {combos[key]}\")\nPYEOF\n",
  "description": "Generate final cliff curve CSV",
  "timeout": 30000
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "076e70a6-b6da-4158-a720-52786daa428f",
  "uuid": "32b3006b-f061-49d7-baf9-16110b520f83",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JVRCjW38wykcu2aMPhcE5p",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3636,
      "cache_read_input_tokens": 62691,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3636
      },
      "output_tokens": 44,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---


### Tool result

_source line 39 · 2026-05-27T04:34:53.900Z_

<details><summary>↩ Tool result · `toolu_01J5uiLfqmhkVJusxTiCpZwm`</summary>

```text
PI05 baseline: pi05_baseline_long_seed42 suite=libero_10 sr=92.8 server=cqa1-33015
PI05 baseline: eval_pi05_baseline_spatial_seed42 suite=libero_spatial (10 tasks x 50 eps) sr=97.2 server=westd-38929
PI05 baseline: eval_pi05_baseline_long_seed42 suite=libero_10 sr=92.8 server=cqa1-33015
PI05 baseline: eval_pi05_baseline_object_seed42 suite=libero_object sr=98.2 server=westd-41074
PI05 baseline: eval_pi05_baseline_goal_seed42 suite=libero_goal sr=0.964 server=cqa1-33015
Saved 206 rows to /home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/artifacts/cliff_curve_data.csv

Data points per (model, suite, method):
  ('OpenVLA', 'libero_10', 'attention'): 5
  ('OpenVLA', 'libero_10', 'baseline'): 1
  ('OpenVLA', 'libero_10', 'l2norm'): 3
  ('OpenVLA', 'libero_10', 'random'): 4
  ('OpenVLA', 'libero_goal', 'attention'): 6
  ('OpenVLA', 'libero_goal', 'baseline'): 1
  ('OpenVLA', 'libero_goal', 'l2norm'): 6
  ('OpenVLA', 'libero_goal', 'random'): 6
  ('OpenVLA', 'libero_object', 'attention'): 3
  ('OpenVLA', 'libero_object', 'baseline'): 1
  ('OpenVLA', 'libero_object', 'l2norm'): 9
  ('OpenVLA', 'libero_object', 'random'): 9
  ('OpenVLA', 'libero_spatial', 'attention'): 1
  ('OpenVLA', 'libero_spatial', 'l2norm'): 1
  ('OpenVLA', 'libero_spatial', 'random'): 2
  ('pi0.5', 'libero_10', 'attention'): 6
  ('pi0.5', 'libero_10', 'l2norm'): 19
  ('pi0.5', 'libero_10', 'random'): 19
  ('pi0.5', 'libero_goal', 'attention'): 2
  ('pi0.5', 'libero_goal', 'l2norm'): 15
  ('pi0.5', 'libero_goal', 'random'): 13
  ('pi0.5', 'libero_object', 'attention'): 5
  ('pi0.5', 'libero_object', 'l2norm'): 15
  ('pi0.5', 'libero_object', 'random'): 16
  ('pi0.5', 'libero_spatial', 'attention'): 1
  ('pi0.5', 'libero_spatial', 'l2norm'): 17
  ('pi0.5', 'libero_spatial', 'random'): 20
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "076e70a6-b6da-4158-a720-52786daa428f",
  "uuid": "921f4494-9164-4ace-88e4-2292f0d47396",
  "tool_use_result": {
    "stdout": "PI05 baseline: pi05_baseline_long_seed42 suite=libero_10 sr=92.8 server=cqa1-33015\nPI05 baseline: eval_pi05_baseline_spatial_seed42 suite=libero_spatial (10 tasks x 50 eps) sr=97.2 server=westd-38929\nPI05 baseline: eval_pi05_baseline_long_seed42 suite=libero_10 sr=92.8 server=cqa1-33015\nPI05 baseline: eval_pi05_baseline_object_seed42 suite=libero_object sr=98.2 server=westd-41074\nPI05 baseline: eval_pi05_baseline_goal_seed42 suite=libero_goal sr=0.964 server=cqa1-33015\nSaved 206 rows to /home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/artifacts/cliff_curve_data.csv\n\nData points per (model, suite, method):\n  ('OpenVLA', 'libero_10', 'attention'): 5\n  ('OpenVLA', 'libero_10', 'baseline'): 1\n  ('OpenVLA', 'libero_10', 'l2norm'): 3\n  ('OpenVLA', 'libero_10', 'random'): 4\n  ('OpenVLA', 'libero_goal', 'attention'): 6\n  ('OpenVLA', 'libero_goal', 'baseline'): 1\n  ('OpenVLA', 'libero_goal', 'l2norm'): 6\n  ('OpenVLA', 'libero_goal', 'random'): 6\n  ('OpenVLA', 'libero_object', 'attention'): 3\n  ('OpenVLA', 'libero_object', 'baseline'): 1\n  ('OpenVLA', 'libero_object', 'l2norm'): 9\n  ('OpenVLA', 'libero_object', 'random'): 9\n  ('OpenVLA', 'libero_spatial', 'attention'): 1\n  ('OpenVLA', 'libero_spatial', 'l2norm'): 1\n  ('OpenVLA', 'libero_spatial', 'random'): 2\n  ('pi0.5', 'libero_10', 'attention'): 6\n  ('pi0.5', 'libero_10', 'l2norm'): 19\n  ('pi0.5', 'libero_10', 'random'): 19\n  ('pi0.5', 'libero_goal', 'attention'): 2\n  ('pi0.5', 'libero_goal', 'l2norm'): 15\n  ('pi0.5', 'libero_goal', 'random'): 13\n  ('pi0.5', 'libero_object', 'attention'): 5\n  ('pi0.5', 'libero_object', 'l2norm'): 15\n  ('pi0.5', 'libero_object', 'random'): 16\n  ('pi0.5', 'libero_spatial', 'attention'): 1\n  ('pi0.5', 'libero_spatial', 'l2norm'): 17\n  ('pi0.5', 'libero_spatial', 'random'): 20",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  }
}
```

</details>

---


### Assistant

_source line 40_

<details><summary>Logged reasoning block</summary>

```text
I found pi0.5 baselines:
- pi0.5 Long (libero_10): 92.8 (cqa1 - but baseline doesn't have pruning contamination issue, it's about success condition)
- pi0.5 Spatial: 97.2 (westd)
- pi0.5 Object: 98.2 (westd)
- pi0.5 Goal: 96.4 (cqa1 - sr=0.964 -> 96.4%)

Wait, the pi0.5 baselines from cqa1 - these are also affected by the lenient success condition? The D248 contamination rule says cqa1 pi0.5 experiments used lenient condition. 

The baseline should be evaluated under the same condition as the pruned versions, so if both are lenient on cqa1, the relative comparison stays valid even though the absolute values are inflated. The pi0.5 Long baseline of 92.8% from eval_pi05_baseline_long_seed42 on cqa1 is likely inflated compared to the strict condition results on westd. I need to add the pi0.5 baselines to the CSV with reliability flags marking the cqa1 ones as unreliable.

Looking at the available baselines, I have Object and Spatial baselines on westd (98.2% and 97.2% respectively, both reliable), while Goal and Long baselines are only on cqa1 (96.4% and 92.8%, both unreliable). I'll add all four to the CSV with appropriate flags.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "076e70a6-b6da-4158-a720-52786daa428f",
  "uuid": "01037a0e-7b98-47b0-9fe4-872a3cd4dda2",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HxbTGfJjjwqJuKxU5PKLEo",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3528,
      "cache_read_input_tokens": 66327,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3528
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---


### Assistant

_source line 41_

Found pi0.5 baselines. Let me add them and finalize.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "076e70a6-b6da-4158-a720-52786daa428f",
  "uuid": "b7e1e009-53fa-4d9e-805d-641dd26cbec1",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HxbTGfJjjwqJuKxU5PKLEo",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3528,
      "cache_read_input_tokens": 66327,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3528
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---


### Tool call

_source line 42_

<details open><summary>🔧 Tool call — Bash · `toolu_01VzVkjgQVsmjxSpHxWFtziN`</summary>

```json
{
  "command": "python3 << 'PYEOF'\nimport csv, io\n\n# Read existing CSV\ninpath = '/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/artifacts/cliff_curve_data.csv'\nwith open(inpath) as f:\n    reader = csv.DictReader(f)\n    rows = list(reader)\n\n# Add pi0.5 baselines\npi05_baselines = [\n    {'model': 'pi0.5', 'suite': 'libero_object', 'method': 'baseline', 'k': '1.0', 'sr': '98.2', 'reliable': 'yes', 'exp_id': 'eval_pi05_baseline_object_seed42', 'server': 'westd-41074', 'notes': 'pi0.5 full model baseline (no pruning)'},\n    {'model': 'pi0.5', 'suite': 'libero_spatial', 'method': 'baseline', 'k': '1.0', 'sr': '97.2', 'reliable': 'yes', 'exp_id': 'eval_pi05_baseline_spatial_seed42', 'server': 'westd-38929', 'notes': 'pi0.5 full model baseline (no pruning)'},\n    {'model': 'pi0.5', 'suite': 'libero_goal', 'method': 'baseline', 'k': '1.0', 'sr': '96.4', 'reliable': 'no', 'exp_id': 'eval_pi05_baseline_goal_seed42', 'server': 'cqa1-33015', 'notes': 'pi0.5 baseline on cqa1 (lenient condition)'},\n    {'model': 'pi0.5', 'suite': 'libero_10', 'method': 'baseline', 'k': '1.0', 'sr': '92.8', 'reliable': 'no', 'exp_id': 'eval_pi05_baseline_long_seed42', 'server': 'cqa1-33015', 'notes': 'pi0.5 baseline on cqa1 (lenient condition)'},\n]\n\nrows.extend(pi05_baselines)\n\n# Sort\nrows.sort(key=lambda r: (r['model'], r['suite'], r['method'], float(r['k'])))\n\n# Write\noutpath = inpath\nwith open(outpath, 'w', newline='') as f:\n    writer = csv.DictWriter(f, fieldnames=['model', 'suite', 'method', 'k', 'sr', 'reliable', 'exp_id', 'server', 'notes'])\n    writer.writeheader()\n    writer.writerows(rows)\n\n# Print summary stats\nreliable_count = sum(1 for r in rows if r['reliable'] == 'yes')\nunreliable_count = sum(1 for r in rows if r['reliable'] == 'no')\nprint(f\"Total: {len(rows)} rows ({reliable_count} reliable, {unreliable_count} unreliable)\")\nprint()\n\n# Print reliable data summary per model/suite/method\nfrom collections import defaultdict\nreliable_data = defaultdict(list)\nfor r in rows:\n    if r['reliable'] == 'yes':\n        reliable_data[(r['model'], r['suite'], r['method'])].append((float(r['k']), float(r['sr'])))\n\nprint(\"Reliable data points:\")\nfor key in sorted(reliable_data.keys()):\n    pts = sorted(reliable_data[key])\n    k_range = f\"k=[{pts[0][0]:.2f}..{pts[-1][0]:.2f}]\"\n    sr_range = f\"SR=[{min(p[1] for p in pts):.1f}%..{max(p[1] for p in pts):.1f}%]\"\n    print(f\"  {key[0]:8s} {key[1]:15s} {key[2]:10s}: {len(pts):2d} pts  {k_range}  {sr_range}\")\nPYEOF\n",
  "description": "Add pi0.5 baselines and print summary",
  "timeout": 15000
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "076e70a6-b6da-4158-a720-52786daa428f",
  "uuid": "0c17e503-6464-4b34-9f80-0c4c372bd87b",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HxbTGfJjjwqJuKxU5PKLEo",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3528,
      "cache_read_input_tokens": 66327,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3528
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---


### Tool result

_source line 43 · 2026-05-27T04:35:19.990Z_

<details><summary>↩ Tool result · `toolu_01VzVkjgQVsmjxSpHxWFtziN`</summary>

```text
Total: 210 rows (150 reliable, 60 unreliable)

Reliable data points:
  OpenVLA  libero_10       attention :  5 pts  k=[0.50..0.90]  SR=[14.6%..45.8%]
  OpenVLA  libero_10       baseline  :  1 pts  k=[1.00..1.00]  SR=[52.8%..52.8%]
  OpenVLA  libero_10       l2norm    :  3 pts  k=[0.70..0.90]  SR=[31.2%..43.6%]
  OpenVLA  libero_10       random    :  4 pts  k=[0.50..0.90]  SR=[18.6%..46.8%]
  OpenVLA  libero_goal     attention :  6 pts  k=[0.50..0.90]  SR=[44.2%..74.6%]
  OpenVLA  libero_goal     baseline  :  1 pts  k=[1.00..1.00]  SR=[74.8%..74.8%]
  OpenVLA  libero_goal     l2norm    :  6 pts  k=[0.50..0.90]  SR=[43.4%..75.4%]
  OpenVLA  libero_goal     random    :  6 pts  k=[0.50..0.90]  SR=[52.2%..80.4%]
  OpenVLA  libero_object   attention :  3 pts  k=[0.70..0.85]  SR=[43.8%..55.0%]
  OpenVLA  libero_object   baseline  :  1 pts  k=[1.00..1.00]  SR=[74.0%..74.0%]
  OpenVLA  libero_object   l2norm    :  9 pts  k=[0.30..0.95]  SR=[25.0%..70.6%]
  OpenVLA  libero_object   random    :  9 pts  k=[0.30..0.95]  SR=[21.4%..67.4%]
  OpenVLA  libero_spatial  attention :  1 pts  k=[0.90..0.90]  SR=[80.4%..80.4%]
  OpenVLA  libero_spatial  l2norm    :  1 pts  k=[0.90..0.90]  SR=[75.0%..75.0%]
  OpenVLA  libero_spatial  random    :  2 pts  k=[0.50..0.90]  SR=[50.0%..79.8%]
  pi0.5    libero_10       l2norm    : 10 pts  k=[0.30..0.95]  SR=[39.2%..87.4%]
  pi0.5    libero_10       random    :  9 pts  k=[0.30..0.95]  SR=[28.4%..65.8%]
  pi0.5    libero_goal     attention :  2 pts  k=[0.50..0.50]  SR=[70.2%..72.2%]
  pi0.5    libero_goal     l2norm    :  9 pts  k=[0.30..0.93]  SR=[51.8%..91.0%]
  pi0.5    libero_goal     random    :  8 pts  k=[0.30..0.95]  SR=[50.6%..83.8%]
  pi0.5    libero_object   attention :  5 pts  k=[0.50..0.95]  SR=[0.6%..98.4%]
  pi0.5    libero_object   baseline  :  1 pts  k=[1.00..1.00]  SR=[98.2%..98.2%]
  pi0.5    libero_object   l2norm    : 12 pts  k=[0.10..0.95]  SR=[2.6%..99.2%]
  pi0.5    libero_object   random    : 12 pts  k=[0.30..0.95]  SR=[3.8%..74.0%]
  pi0.5    libero_spatial  attention :  1 pts  k=[0.50..0.50]  SR=[72.6%..72.6%]
  pi0.5    libero_spatial  baseline  :  1 pts  k=[1.00..1.00]  SR=[97.2%..97.2%]
  pi0.5    libero_spatial  l2norm    : 11 pts  k=[0.30..0.95]  SR=[52.0%..97.8%]
  pi0.5    libero_spatial  random    : 11 pts  k=[0.30..0.95]  SR=[49.6%..76.8%]
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "076e70a6-b6da-4158-a720-52786daa428f",
  "uuid": "5707db9d-c8e0-4f5e-a548-24d1520fdadf",
  "tool_use_result": {
    "stdout": "Total: 210 rows (150 reliable, 60 unreliable)\n\nReliable data points:\n  OpenVLA  libero_10       attention :  5 pts  k=[0.50..0.90]  SR=[14.6%..45.8%]\n  OpenVLA  libero_10       baseline  :  1 pts  k=[1.00..1.00]  SR=[52.8%..52.8%]\n  OpenVLA  libero_10       l2norm    :  3 pts  k=[0.70..0.90]  SR=[31.2%..43.6%]\n  OpenVLA  libero_10       random    :  4 pts  k=[0.50..0.90]  SR=[18.6%..46.8%]\n  OpenVLA  libero_goal     attention :  6 pts  k=[0.50..0.90]  SR=[44.2%..74.6%]\n  OpenVLA  libero_goal     baseline  :  1 pts  k=[1.00..1.00]  SR=[74.8%..74.8%]\n  OpenVLA  libero_goal     l2norm    :  6 pts  k=[0.50..0.90]  SR=[43.4%..75.4%]\n  OpenVLA  libero_goal     random    :  6 pts  k=[0.50..0.90]  SR=[52.2%..80.4%]\n  OpenVLA  libero_object   attention :  3 pts  k=[0.70..0.85]  SR=[43.8%..55.0%]\n  OpenVLA  libero_object   baseline  :  1 pts  k=[1.00..1.00]  SR=[74.0%..74.0%]\n  OpenVLA  libero_object   l2norm    :  9 pts  k=[0.30..0.95]  SR=[25.0%..70.6%]\n  OpenVLA  libero_object   random    :  9 pts  k=[0.30..0.95]  SR=[21.4%..67.4%]\n  OpenVLA  libero_spatial  attention :  1 pts  k=[0.90..0.90]  SR=[80.4%..80.4%]\n  OpenVLA  libero_spatial  l2norm    :  1 pts  k=[0.90..0.90]  SR=[75.0%..75.0%]\n  OpenVLA  libero_spatial  random    :  2 pts  k=[0.50..0.90]  SR=[50.0%..79.8%]\n  pi0.5    libero_10       l2norm    : 10 pts  k=[0.30..0.95]  SR=[39.2%..87.4%]\n  pi0.5    libero_10       random    :  9 pts  k=[0.30..0.95]  SR=[28.4%..65.8%]\n  pi0.5    libero_goal     attention :  2 pts  k=[0.50..0.50]  SR=[70.2%..72.2%]\n  pi0.5    libero_goal     l2norm    :  9 pts  k=[0.30..0.93]  SR=[51.8%..91.0%]\n  pi0.5    libero_goal     random    :  8 pts  k=[0.30..0.95]  SR=[50.6%..83.8%]\n  pi0.5    libero_object   attention :  5 pts  k=[0.50..0.95]  SR=[0.6%..98.4%]\n  pi0.5    libero_object   baseline  :  1 pts  k=[1.00..1.00]  SR=[98.2%..98.2%]\n  pi0.5    libero_object   l2norm    : 12 pts  k=[0.10..0.95]  SR=[2.6%..99.2%]\n  pi0.5    libero_object   random    : 12 pts  k=[0.30..0.95]  SR=[3.8%..74.0%]\n  pi0.5    libero_spatial  attention :  1 pts  k=[0.50..0.50]  SR=[72.6%..72.6%]\n  pi0.5    libero_spatial  baseline  :  1 pts  k=[1.00..1.00]  SR=[97.2%..97.2%]\n  pi0.5    libero_spatial  l2norm    : 11 pts  k=[0.30..0.95]  SR=[52.0%..97.8%]\n  pi0.5    libero_spatial  random    : 11 pts  k=[0.30..0.95]  SR=[49.6%..76.8%]",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  }
}
```

</details>

---


### Assistant

_source line 44_

Now let me register the artifact.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "076e70a6-b6da-4158-a720-52786daa428f",
  "uuid": "a6b3c6a1-b75f-4c1d-8d83-72a79badad72",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CpxNB2oqZogJvMEMRBczbT",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3069,
      "cache_read_input_tokens": 69855,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3069
      },
      "output_tokens": 2,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---


### Tool call

_source line 45_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__register_artifact · `toolu_01WFC5C4DicZy619RXr4D8ry`</summary>

```json
{
  "name": "Cliff Curve Data CSV",
  "type": "data",
  "description": "All pruning evaluation data points for cliff curve figures. 210 rows covering OpenVLA and pi0.5 across 4 LIBERO suites, 3 methods (l2norm/attention/random), k=0.1-1.0. Includes reliability flags for D248 cqa1 contamination.",
  "project": "importance_margin_vla_compress",
  "source_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/artifacts/cliff_curve_data.csv",
  "tags": [
    "cliff_curve",
    "paper_figure",
    "evaluation_data"
  ]
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "076e70a6-b6da-4158-a720-52786daa428f",
  "uuid": "e5014c08-695d-4448-97cc-59642cd30ba8",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CpxNB2oqZogJvMEMRBczbT",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3069,
      "cache_read_input_tokens": 69855,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3069
      },
      "output_tokens": 2,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---


### Tool result

_source line 46 · 2026-05-27T04:35:38.958Z_

<details><summary>↩ Tool result · `toolu_01WFC5C4DicZy619RXr4D8ry`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"artifact\": {\"id\": \"art_20260527_6e85d5\", \"name\": \"Cliff Curve Data CSV\", \"type\": \"data\", \"description\": \"All pruning evaluation data points for cliff curve figures. 210 rows covering OpenVLA and pi0.5 across 4 LIBERO suites, 3 methods (l2norm/attention/random), k=0.1-1.0. Includes reliability flags for D248 cqa1 contamination.\", \"path\": \"projects/importance_margin_vla_compress/artifacts/_project/data/cliff_curve_data.csv\", \"url\": null, \"project\": \"importance_margin_vla_compress\", \"exp_id\": null, \"skill\": \"\", \"created_at\": \"2026-05-27T04:35:38.728452+00:00\", \"tags\": [\"cliff_curve\", \"paper_figure\", \"evaluation_data\"]}, \"manifest\": \"/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/artifacts/manifest.yaml\"}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "076e70a6-b6da-4158-a720-52786daa428f",
  "uuid": "ba7e04b2-c88a-4272-966c-83cab211aeab",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"artifact\\\": {\\\"id\\\": \\\"art_20260527_6e85d5\\\", \\\"name\\\": \\\"Cliff Curve Data CSV\\\", \\\"type\\\": \\\"data\\\", \\\"description\\\": \\\"All pruning evaluation data points for cliff curve figures. 210 rows covering OpenVLA and pi0.5 across 4 LIBERO suites, 3 methods (l2norm/attention/random), k=0.1-1.0. Includes reliability flags for D248 cqa1 contamination.\\\", \\\"path\\\": \\\"projects/importance_margin_vla_compress/artifacts/_project/data/cliff_curve_data.csv\\\", \\\"url\\\": null, \\\"project\\\": \\\"importance_margin_vla_compress\\\", \\\"exp_id\\\": null, \\\"skill\\\": \\\"\\\", \\\"created_at\\\": \\\"2026-05-27T04:35:38.728452+00:00\\\", \\\"tags\\\": [\\\"cliff_curve\\\", \\\"paper_figure\\\", \\\"evaluation_data\\\"]}, \\\"manifest\\\": \\\"/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/artifacts/manifest.yaml\\\"}, \\\"error\\\": null, \\\"metadata\\\": {}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"artifact\": {\"id\": \"art_20260527_6e85d5\", \"name\": \"Cliff Curve Data CSV\", \"type\": \"data\", \"description\": \"All pruning evaluation data points for cliff curve figures. 210 rows covering OpenVLA and pi0.5 across 4 LIBERO suites, 3 methods (l2norm/attention/random), k=0.1-1.0. Includes reliability flags for D248 cqa1 contamination.\", \"path\": \"projects/importance_margin_vla_compress/artifacts/_project/data/cliff_curve_data.csv\", \"url\": null, \"project\": \"importance_margin_vla_compress\", \"exp_id\": null, \"skill\": \"\", \"created_at\": \"2026-05-27T04:35:38.728452+00:00\", \"tags\": [\"cliff_curve\", \"paper_figure\", \"evaluation_data\"]}, \"manifest\": \"/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/artifacts/manifest.yaml\"}, \"error\": null, \"metadata\": {}}"
    }
  }
}
```

</details>

---


### Assistant

_source line 47_

CSV 已生成并注册。

**文件**: `artifacts/cliff_curve_data.csv`
**数据量**: 210 行（150 reliable, 60 unreliable）

覆盖范围:
- **OpenVLA**: Object/Goal/Long/Spatial × l2norm/attention/random, k=0.3-0.95 + baseline(k=1.0)
- **π0.5**: Object/Goal/Long/Spatial × l2norm/attention/random, k=0.1-0.95 + baseline(k=1.0)

注意:
- π0.5 Goal 和 Long baseline 来自 cqa1，标记 reliable=no（lenient condition）
- 所有 cqa1 上的 π0.5 非 strict 实验均标记 reliable=no
- π0.5 Long attention 全部数据为 cqa1 unreliable（无 westd strict 重跑）

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "076e70a6-b6da-4158-a720-52786daa428f",
  "uuid": "cf28e8d8-d22d-478b-8514-0d45f84c2190",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WjBHFxW1noTfCkXSzkYpJh",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 621,
      "cache_read_input_tokens": 72924,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 621
      },
      "output_tokens": 1,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---


### Task result

_source line 48_

CSV 已生成并注册。

**文件**: `artifacts/cliff_curve_data.csv`
**数据量**: 210 行（150 reliable, 60 unreliable）

覆盖范围:
- **OpenVLA**: Object/Goal/Long/Spatial × l2norm/attention/random, k=0.3-0.95 + baseline(k=1.0)
- **π0.5**: Object/Goal/Long/Spatial × l2norm/attention/random, k=0.1-0.95 + baseline(k=1.0)

注意:
- π0.5 Goal 和 Long baseline 来自 cqa1，标记 reliable=no（lenient condition）
- 所有 cqa1 上的 π0.5 非 strict 实验均标记 reliable=no
- π0.5 Long attention 全部数据为 cqa1 unreliable（无 westd strict 重跑）

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "type": "result",
  "subtype": "success",
  "is_error": false,
  "api_error_status": null,
  "duration_ms": 370991,
  "duration_api_ms": 366312,
  "num_turns": 16,
  "stop_reason": "end_turn",
  "session_id": "076e70a6-b6da-4158-a720-52786daa428f",
  "total_cost_usd": 1.090584,
  "usage": {
    "input_tokens": 20,
    "cache_creation_input_tokens": 61704,
    "cache_read_input_tokens": 604112,
    "output_tokens": 16044,
    "server_tool_use": {
      "web_search_requests": 0,
      "web_fetch_requests": 0
    },
    "service_tier": "standard",
    "cache_creation": {
      "ephemeral_1h_input_tokens": 61704,
      "ephemeral_5m_input_tokens": 0
    },
    "inference_geo": "",
    "iterations": [
      {
        "input_tokens": 1,
        "output_tokens": 246,
        "cache_read_input_tokens": 72924,
        "cache_creation_input_tokens": 621,
        "cache_creation": {
          "ephemeral_5m_input_tokens": 0,
          "ephemeral_1h_input_tokens": 621
        },
        "type": "message"
      }
    ],
    "speed": "standard"
  },
  "modelUsage": {
    "claude-haiku-4-5-20251001": {
      "inputTokens": 1603,
      "outputTokens": 15,
      "cacheReadInputTokens": 0,
      "cacheCreationInputTokens": 0,
      "webSearchRequests": 0,
      "costUSD": 0.001678,
      "contextWindow": 200000,
      "maxOutputTokens": 32000
    },
    "claude-opus-4-6": {
      "inputTokens": 20,
      "outputTokens": 16044,
      "cacheReadInputTokens": 604112,
      "cacheCreationInputTokens": 61704,
      "webSearchRequests": 0,
      "costUSD": 1.088906,
      "contextWindow": 200000,
      "maxOutputTokens": 64000
    }
  },
  "permission_denials": [],
  "terminal_reason": "completed",
  "fast_mode_state": "off",
  "uuid": "c20456e3-53fc-4720-bd64-28a2b1d32553"
}
```

</details>

---
