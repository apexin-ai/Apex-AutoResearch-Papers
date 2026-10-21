# figure tables — Part 2 of 3

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Worker execution logs

[← Part 1](part-001.md) · [Transcript overview](../figure-tables.md) · [Part 3 →](part-003.md) · [Structured JSON](../../../sessions/af/af3833744bc8952c4b40.json)

## Before a recorded user message

### Large event (continued)

```text
training_job\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-23T18:42:39.253Z\"}, \"eval_pi05_l2norm_k03_goal_seed42_v2\": {\"checkpoint_path\": \"N/A (eval only)\", \"completed_at\": \"2026-05-23T18:21:43.187Z\", \"conclusion\": \"negative\", \"created_at\": \"2026-05-23T15:49:40.493Z\", \"hypothesis\": \"CPU RNG 修复后 π0.5 L2norm k=0.3 Goal。L2norm 在 Object 上表现稳定（无 cliff），验证 Goal 套件上 L2norm 是否也无 cliff，与 Random 对比确认 importance-based pruning 的优势。\", \"metrics\": {\"per_task\": {\"T0\": 66, \"T1\": 22, \"T2\": 76, \"T3\": 32, \"T4\": 62, \"T5\": 30, \"T6\": 20, \"T7\": 96, \"T8\": 78, \"T9\": 24}, \"success_rate\": 50.6, \"total_episodes\": 500, \"total_successes\": 253}, \"retry_count\": 0, \"spec\": {\"account\": \"root\", \"backend\": \"tmux\", \"command\": \"eval_pi05_pruning_libero.py --prune_mode l2norm --keep_ratio 0.3 --suite libero_goal --seed 42\", \"data_count\": 500, \"data_path\": \"libero_goal\", \"gpu\": [\"cuda:3\"], \"gpu_hours\": 2.53, \"log_path\": \"~/runs/importance_margin_vla_compress/eval_pi05_l2norm_k03_goal_seed42_v2.log\", \"model_name\": \"pi0.5\", \"pid\": \"872978\", \"seed\": 42, \"server\": \"cqa1-33015\", \"submitted_at\": \"2026-05-23T15:49:38.613Z\", \"submitted_via\": \"submit_training_job\", \"wall_clock_seconds\": 9124.6}, \"status\": \"DONE\", \"updated_at\": \"2026-05-23T18:21:43.187Z\"}, \"eval_xvla_random_k05_goal_seed42\": {\"completed_at\": \"2026-05-23T09:03:33.363Z\", \"conclusion\": \"failed\", \"created_at\": \"2026-05-23T06:11:45.093Z\", \"extra\": {\"hook_events\": [{\"action\": \"agent\", \"event\": \"on_failed\", \"ts\": \"2026-05-23T09:03:47.420256+00:00\"}]}, \"failure_reason\": \"INVALIDATED: domain_id=2 bug. 使用了错误的 action decoder (Spatial decoder 而非 Robot decoder)，导致 SR=0%。正确结果见 eval_e5_xvla_random_goal_k05_v2 (SR=67.2%, domain_id=3)。\", \"hypothesis\": \"X-VLA Random k=0.5 Goal seed42: Table 2 gap. L2 k=0.5 Goal=61.0%. Goal 的 task complexity 在 50% pruning 下如何影响 random performance。\", \"metrics\": {\"elapsed_min\": 158.9, \"episodes\": 500, \"per_task_sr\": {\"task0_open_middle_drawer\": 0, \"task1_bowl_on_stove\": 0, \"task2_wine_on_cabinet\": 0, \"task3_open_drawer_bowl_inside\": 0, \"task4_bowl_on_cabinet\": 0, \"task5_push_plate_front_stove\": 0, \"task6_cream_cheese_in_bowl\": 0, \"task7_turn_on_stove\": 0, \"task8_bowl_on_plate\": 0, \"task9_wine_on_rack\": 0}, \"success_rate\": 0, \"tasks\": 10, \"wilson_ci_95\": [0, 0.8]}, \"reproduce\": {\"finished_at\": \"2026-05-23T09:03:36.638Z\"}, \"retry_count\": 0, \"spec\": {\"checkpoint_path\": \"N/A - eval experiment\", \"checkpoint_source\": \"/root/autodl-tmp/X-VLA-Libero\", \"command\": \"HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 HF_HOME=/root/autodl-tmp/.hf_cache MUJOCO_GL=egl CUDA_VISIBLE_DEVICES=0 python -u eval_xvla_pruning_libero.py --model_path /root/autodl-tmp/X-VLA-Libero --suite libero_goal --keep_ratio 0.5 --mode random --num_episodes 50 --seed 42 --domain_id 2 --gpu 0\", \"data_count\": 500, \"data_path\": \"libero_goal\", \"eval_data\": \"libero_goal\", \"gpu\": 0, \"log_path\": \"logs/eval_xvla_random_k05_goal_seed42.log\", \"model_name\": \"X-VLA-Libero\", \"pid\": 250272, \"seed\": 42, \"server\": \"westd-27271\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-23T18:19:55.750Z\"}, \"eval_pi05_l2norm_k07_goal_seed42_v2\": {\"checkpoint_path\": \"N/A (eval only)\", \"completed_at\": \"2026-05-23T18:09:05.382Z\", \"conclusion\": \"negative\", \"created_at\": \"2026-05-23T15:49:35.207Z\", \"hypothesis\": \"CPU RNG 修复后 π0.5 L2norm k=0.7 Goal。L2norm 在 Object 上表现稳定（无 cliff），验证 Goal 套件上 L2norm 是否也无 cliff，与 Random 对比确认 importance-based pruning 的优势。\", \"metrics\": {\"source\": \"SSH log harvest by diagnostic worker\", \"success_rate\": 73.6, \"total_episodes\": 500}, \"retry_count\": 0, \"spec\": {\"account\": \"root\", \"backend\": \"tmux\", \"command\": \"eval_pi05_pruning_libero.py --prune_mode l2norm --keep_ratio 0.7 --suite libero_goal --n_episodes 50 --seed 42 --gpu 0\", \"data_count\": 500, \"data_path\": \"libero_goal\", \"gpu\": [\"cuda:2\"], \"gpu_hours\": 2.33, \"log_path\": \"~/runs/importance_margin_vla_compress/eval_pi05_l2norm_k07_goal_seed42_v2.log\", \"model_name\": \"pi0.5\", \"pid\": \"872735\", \"seed\": 42, \"server\": \"cqa1-33015\", \"submitted_at\": \"2026-05-23T15:49:34.070Z\", \"submitted_via\": \"submit_training_job\", \"wall_clock_seconds\": 8371.3}, \"status\": \"DONE\", \"updated_at\": \"2026-05-23T18:09:05.382Z\"}, \"eval_pi05_l2norm_k09_goal_seed42_v2\": {\"checkpoint_path\": \"N/A (eval only)\", \"completed_at\": \"2026-05-23T18:09:01.717Z\", \"conclusion\": \"success\", \"created_at\": \"2026-05-23T15:49:31.241Z\", \"hypothesis\": \"CPU RNG 修复后 π0.5 L2norm k=0.9 Goal。L2norm 在 Object 上表现稳定（无 cliff），验证 Goal 套件上 L2norm 是否也无 cliff，与 Random 对比确认 importance-based pruning 的优势。\", \"metrics\": {\"source\": \"SSH log harvest by diagnostic worker\", \"success_rate\": 90.6, \"total_episodes\": 500}, \"retry_count\": 0, \"spec\": {\"account\": \"root\", \"backend\": \"tmux\", \"command\": \"eval_pi05_pruning_libero.py --prune_mode l2norm --keep_ratio 0.9 --suite libero_goal --n_episodes 50 --seed 42 --gpu 0\", \"data_count\": 500, \"data_path\": \"libero_goal\", \"gpu\": [\"cuda:1\"], \"gpu_hours\": 2.33, \"log_path\": \"~/runs/importance_margin_vla_compress/eval_pi05_l2norm_k09_goal_seed42_v2.log\", \"model_name\": \"pi0.5\", \"pid\": \"872589\", \"seed\": 42, \"server\": \"cqa1-33015\", \"submitted_at\": \"2026-05-23T15:49:30.090Z\", \"submitted_via\": \"submit_training_job\", \"wall_clock_seconds\": 8371.6}, \"status\": \"DONE\", \"updated_at\": \"2026-05-23T18:09:01.717Z\"}, \"eval_pi05_l2norm_k095_goal_seed42_v2\": {\"checkpoint_path\": \"N/A (eval only)\", \"completed_at\": \"2026-05-23T18:08:58.191Z\", \"conclusion\": \"success\", \"created_at\": \"2026-05-23T15:49:27.316Z\", \"hypothesis\": \"CPU RNG 修复后 π0.5 L2norm k=0.95 Goal。L2norm 在 Object 上表现稳定（无 cliff），验证 Goal 套件上 L2norm 是否也无 cliff，与 Random 对比确认 importance-based pruning 的优势。\", \"metrics\": {\"source\": \"SSH log harvest by diagnostic worker\", \"success_rate\": 89.4, \"total_episodes\": 500}, \"retry_count\": 0, \"spec\": {\"account\": \"root\", \"backend\": \"tmux\", \"command\": \"eval_pi05_pruning_libero.py --prune_mode l2norm --keep_ratio 0.95 --suite libero_goal --n_episodes 50 --seed 42 --gpu 0\", \"data_count\": 500, \"data_path\": \"libero_goal\", \"gpu\": [\"cuda:0\"], \"gpu_hours\": 2.33, \"log_path\": \"~/runs/importance_margin_vla_compress/eval_pi05_l2norm_k095_goal_seed42_v2.log\", \"model_name\": \"pi0.5\", \"pid\": \"872508\", \"seed\": 42, \"server\": \"cqa1-33015\", \"submitted_at\": \"2026-05-23T15:49:26.137Z\", \"submitted_via\": \"submit_training_job\", \"wall_clock_seconds\": 8372.1}, \"status\": \"DONE\", \"updated_at\": \"2026-05-23T18:08:58.191Z\"}, \"eval_e5_xvla_attn_rollout_goal_k05_v2\": {\"checkpoint_path\": \"N/A (eval only)\", \"completed_at\": \"2026-05-23T18:01:04.224Z\", \"conclusion\": \"success\", \"created_at\": \"2026-05-23T16:50:04.341Z\", \"hypothesis\": \"E5 X-VLA attention_rollout pruning k=0.5 Goal v2 重跑。Rollout综合多层attention信息，在50%极端剪枝下Goal表现。与last/mean/random对比评估attention rollout的有效性。\", \"metrics\": {\"elapsed_min\": 31.1, \"success_rate\": 96.8, \"total_episodes\": 500, \"total_successes\": 484, \"wilson_ci_95\": [94.9, 98]}, \"retry_count\": 0, \"spec\": {\"account\": \"root\", \"backend\": \"tmux\", \"command\": \"eval_xvla_attention_pruning_libero.py --mode attention_rollout --keep_ratio 0.5 --suite libero_goal --seed 42\", \"data_count\": 500, \"data_path\": \"libero_goal\", \"gpu\": [\"cuda:2\"], \"gpu_hours\": 1.18, \"log_path\": \"~/runs/importance_margin_vla_compress/eval_e5_xvla_attn_rollout_goal_k05_v2.log\", \"model_name\": \"X-VLA-Libero\", \"pid\": \"743734\", \"seed\": 42, \"server\": \"westd-38929\", \"submitted_at\": \"2026-05-23T16:50:03.180Z\", \"submitted_via\": \"submit_training_job\", \"wall_clock_seconds\": 4261.0}, \"status\": \"DONE\", \"updated_at\": \"2026-05-23T18:04:48.242Z\"}, \"eval_e5_xvla_attn_mean_goal_k05_v2\": {\"checkpoint_path\": \"N/A (eval only)\", \"completed_at\": \"2026-05-23T18:01:00.513Z\", \"conclusion\": \"success\", \"created_at\": \"2026-05-23T16:50:00.083Z\", \"hypothesis\": \"E5 X-VLA attention_mean pruning k=0.5 Goal v2 重跑。mean attention作为token重要性指标，在50%极端剪枝下Goal表现。与last/rollout/random对比评估不同attention聚合策略。\", \"metrics\": {\"elapsed_min\": 30.2, \"success_rate\": 97.4, \"total_episodes\": 500, \"total_successes\": 487, \"wilson_ci_95\": [95.6, 98.5]}, \"retry_count\": 0, \"spec\": {\"account\": \"root\", \"backend\": \"tmux\", \"command\": \"eval_xvla_attention_pruning_libero.py --mode attention_mean --keep_ratio 0.5 --suite libero_goal --seed 42\", \"data_count\": 500, \"data_path\": \"libero_goal\", \"gpu\": [\"cuda:1\"], \"gpu_hours\": 1.18, \"log_path\": \"~/runs/importance_margin_vla_compress/eval_e5_xvla_attn_mean_goal_k05_v2.log\", \"model_name\": \"X-VLA-Libero\", \"pid\": \"743486\", \"seed\": 42, \"server\": \"westd-38929\", \"submitted_at\": \"2026-05-23T16:49:58.923Z\", \"submitted_via\": \"submit_training_job\", \"wall_clock_seconds\": 4261.6}, \"status\": \"DONE\", \"updated_at\": \"2026-05-23T18:04:46.083Z\"}, \"eval_e5_xvla_attn_last_goal_k05_v2\": {\"checkpoint_path\": \"N/A (eval only)\", \"completed_at\": \"2026-05-23T18:00:56.588Z\", \"conclusion\": \"success\", \"created_at\": \"2026-05-23T16:49:56.234Z\", \"hypothesis\": \"E5 X-VLA attention_last pruning k=0.5 Goal v2 重跑。保留50%视觉token时，last-layer attention分数能否识别Goal任务的关键视觉信息。与random k=0.5(67.2%)对比验证importance-based优势。\", \"metrics\": {\"elapsed_min\": 30, \"success_rate\": 98.2, \"total_episodes\": 500, \"total_successes\": 491, \"wilson_ci_95\": [96.6, 99.1]}, \"retry_count\": 0, \"spec\": {\"account\": \"root\", \"backend\": \"tmux\", \"command\": \"eval_xvla_attention_pruning_libero.py --mode attention_last --keep_ratio 0.5 --suite libero_goal --seed 42\", \"data_count\": 500, \"data_path\": \"libero_goal\", \"gpu\": [\"cuda:0\"], \"gpu_hours\": 1.18, \"log_path\": \"~/runs/importance_margin_vla_compress/eval_e5_xvla_attn_last_goal_k05_v2.log\", \"model_name\": \"X-VLA-Libero\", \"pid\": \"743341\", \"seed\": 42, \"server\": \"westd-38929\", \"submitted_at\": \"2026-05-23T16:49:55.112Z\", \"submitted_via\": \"submit_training_job\", \"wall_clock_seconds\": 4261.5}, \"status\": \"DONE\", \"updated_at\": \"2026-05-23T18:04:44.027Z\"}, \"eval_e5_xvla_random_goal_k05_v2\": {\"checkpoint_path\": \"N/A (eval only)\", \"completed_at\": \"2026-05-23T18:01:07.760Z\", \"conclusion\": \"negative\", \"created_at\": \"2026-05-23T17:58:52.568Z\", \"hypothesis\": \"E5 X-VLA random pruning k=0.5 Goal v2 重跑。Random baseline在50%剪枝下Goal套件表现，作为importance-based方法(attn_last/mean/rollout)的对照基准。\", \"metrics\": {\"elapsed_min\": 58.2, \"success_rate\": 67.2, \"total_episodes\": 500, \"total_successes\": 336, \"wilson_ci_95\": [63, 71.2]}, \"retry_count\": 0, \"spec\": {\"account\": \"root\", \"command\": \"eval_xvla_attention_pruning_libero.py --mode random --keep_ratio 0.5 --suite libero_goal --seed 42\", \"data_count\": 500, \"data_path\": \"libero_goal\", \"log_path\": \"~/runs/importance_margin_vla_compress/eval_xvla_random_k05_goal_seed42_v2.log\", \"model_name\": \"X-VLA-Libero\", \"seed\": 42, \"server\": \"westd-38929\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-23T18:01:07.760Z\"}, \"eval_pi05_random_k03_goal_seed42_v2\": {\"checkpoint_path\": \"N/A (eval only)\", \"completed_at\": \"2026-05-23T17:58:27.874Z\", \"conclusion\": \"negative\", \"created_at\": \"2026-05-23T15:02:04.475Z\", \"hypothesis\": \"CPU RNG 修复后 π0.5 Random k=0.3 Goal 重跑。修复前 cqa1-33015 数据=51.8%，现用 westd-41074 统一服务器。极端剪枝点，验证 Goal 套件在 k=0.3 的真实退化程度。\", \"metrics\": {\"source\": \"westd-41074 diag harvested, CPU RNG fixed\", \"success_rate\": 50.6, \"total_episodes\": 500, \"total_successes\": 253}, \"retry_count\": 0, \"spec\": {\"account\": \"root\", \"backend\": \"tmux\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/importance_margin_vla_compress && HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 HF_HOME=/root/autodl-tmp/.hf_cache MUJOCO_GL=egl python -u eval_pi05_pruning_libero.py --prune_mode random --keep_ratio 0.3 --suite libero_goal --n_episodes 50 --seed 42 --gpu 0\\\"\", \"gpu\": [\"cuda:2\"], \"gpu_hours\": 2.3, \"log_path\": \"~/runs/importance_margin_vla_compress/eval_pi05_random_k03_goal_seed42_v2.log\", \"pid\": \"224548\", \"server\": \"westd-41074\", \"submitted_at\": \"2026-05-23T15:40:20.564Z\", \"submitted_via\": \"submit_training_job\", \"wall_clock_seconds\": 8287.3}, \"status\": \"DONE\", \"updated_at\": \"2026-05-23T17:58:27.874Z\"}, \"eval_e5_xvla_attn_last_obj_k03\": {\"completed_at\": \"2026-05-23T15:47:09.978Z\", \"conclusion\": \"success\", \"created_at\": \"2026-05-23T13:26:46.065Z\", \"hypothesis\": \"E5 attention_last Object k=0.3: 极端剪枝（保留15/50 tokens）。attention_last k=0.5 Object=74.4%。k=0.3 测试 last-layer attention 在极端条件下的退化。与 mean k=0.3 (96%) 和 rollout k=0.3 (92%) 对比。\", \"metrics\": {\"elapsed_min\": 45.2, \"source\": \"Worker harvested from westd-27271\", \"success_rate\": 84.2, \"total_episodes\": 500, \"total_successes\": 421, \"wilson_ci_95\": [80.7, 87.1]}, \"retry_count\": 0, \"spec\": {\"account\": \"root\", \"backend\": \"tmux\", \"checkpoint_path\": \"N/A\", \"checkpoint_source\": \"X-VLA-Libero\", \"command\": \"python -u eval_xvla_attention_pruning_libero.py --model_path /root/autodl-tmp/X-VLA-Libero --suite libero_object --keep_ratio 0.3 --mode attention_last --num_episodes 50 --seed 42 --gpu 0\", \"data_count\": 500, \"data_path\": \"libero_object\", \"eval_data\": \"libero_object\", \"gpu\": [\"cuda:1\"], \"gpu_hours\": 0.75, \"log_path\": \"~/runs/importance_margin_vla_compress/eval_e5_xvla_attn_last_obj_k03.log\", \"model_name\": \"X-VLA-Libero\", \"pid\": \"166323\", \"seed\": 42, \"server\": \"westd-27271\", \"submitted_at\": \"2026-05-23T13:26:44.994Z\", \"submitted_via\": \"submit_training_job\", \"wall_clock_seconds\": 2712}, \"status\": \"DONE\", \"updated_at\": \"2026-05-23T15:47:09.978Z\"}, \"eval_e5_xvla_attn_rollout_obj_k03\": {\"completed_at\": \"2026-05-23T15:20:49.500Z\", \"conclusion\": \"success\", \"created_at\": \"2026-05-23T14:08:57.564Z\", \"hypothesis\": \"E5 attention_rollout Object k=0.3: 极端剪枝。rollout k=0.5=97.4%——k=0.3 测试 rollout 在极端条件下的退化。与 last 和 mean k=0.3 对比三种模式的鲁棒性排序。\", \"metrics\": {\"source\": \"Director harvested from westd-38929\", \"success_rate\": 92, \"total_episodes\": 500, \"total_successes\": 460}, \"retry_count\": 0, \"spec\": {\"account\": \"root\", \"backend\": \"tmux\", \"checkpoint_path\": \"N/A\", \"command\": \"eval_xvla_attention_pruning_libero.py --mode attention_rollout --suite libero_object --keep_ratio 0.3 --seed 42\", \"data_count\": 500, \"data_path\": \"LIBERO libero_object 10 tasks\", \"gpu\": [\"cuda:1\"], \"gpu_hours\": 1.2, \"log_path\": \"~/runs/importance_margin_vla_compress/eval_e5_xvla_attn_rollout_obj_k03.log\", \"model_name\": \"X-VLA-Libero\", \"pid\": \"967125\", \"seed\": 42, \"server\": \"westd-38929\", \"submitted_at\": \"2026-05-23T14:08:56.446Z\", \"submitted_via\": \"submit_training_job\", \"wall_clock_seconds\": 4313.1}, \"status\": \"DONE\", \"updated_at\": \"2026-05-23T15:42:45.611Z\"}, \"eval_e5_xvla_attn_mean_spatial_k03\": {\"completed_at\": \"2026-05-23T15:20:56.427Z\", \"conclusion\": \"success\", \"created_at\": \"2026-05-23T14:09:05.719Z\", \"hypothesis\": \"E5 attention_mean Spatial k=0.3: 极端剪枝。mean Spatial k=0.5=91.6%。与 last Spatial k=0.3 对比——Spatial 上 mode ranking reversal (rollout>mean>last) 在极端 k 下是否保持。\", \"metrics\": {\"source\": \"Director harvested from westd-38929\", \"success_rate\": 90.4, \"total_episodes\": 500, \"total_successes\": 452}, \"retry_count\": 0, \"spec\": {\"account\": \"root\", \"backend\": \"tmux\", \"checkpoint_path\": \"N/A\", \"command\": \"eval_xvla_attention_pruning_libero.py --mode attention_mean --suite libero_spatial --keep_ratio 0.3 --seed 42\", \"data_count\": 500, \"data_path\": \"LIBERO libero_spatial 10 tasks\", \"gpu\": [\"cuda:3\"], \"gpu_hours\": 1.2, \"log_path\": \"~/runs/importance_margin_vla_compress/eval_e5_xvla_attn_mean_spatial_k03.log\", \"model_name\": \"X-VLA-Libero\", \"pid\": \"967621\", \"seed\": 42, \"server\": \"westd-38929\", \"submitted_at\": \"2026-05-23T14:09:04.460Z\", \"submitted_via\": \"submit_training_job\", \"wall_clock_seconds\": 4312.0}, \"status\": \"DONE\", \"updated_at\": \"2026-05-23T15:20:56.427Z\"}, \"eval_e5_xvla_attn_last_spatial_k03\": {\"completed_at\": \"2026-05-23T15:20:53.050Z\", \"conclusion\": \"success\", \"created_at\": \"2026-05-23T14:09:01.448Z\", \"hypothesis\": \"E5 attention_last Spatial k=0.3: 极端剪枝。last Spatial k=0.5=88.8%。Spatial 对 pruning 更敏感（Object k=0.5=99.2%），k=0.3 预测退化更大。\", \"metrics\": {\"source\": \"Director harvested from westd-38929\", \"success_rate\": 85.6, \"total_episodes\": 500, \"total_successes\": 428}, \"retry_count\": 0, \"spec\": {\"account\": \"root\", \"backend\": \"tmux\", \"checkpoint_path\": \"N/A\", \"command\": \"eval_xvla_attention_pruning_libero.py --mode attention_last --suite libero_spatial --keep_ratio 0.3 --seed 42\", \"data_count\": 500, \"data_path\": \"LIBERO libero_spatial 10 tasks\", \"gpu\": [\"cuda:2\"], \"gpu_hours\": 1.2, \"log_path\": \"~/runs/importance_margin_vla_compress/eval_e5_xvla_attn_last_spatial_k03.log\", \"model_name\": \"X-VLA-Libero\", \"pid\": \"967372\", \"seed\": 42, \"server\": \"westd-38929\", \"submitted_at\": \"2026-05-23T14:09:00.235Z\", \"submitted_via\": \"submit_training_job\", \"wall_clock_seconds\": 4312.8}, \"status\": \"DONE\", \"updated_at\": \"2026-05-23T15:20:53.050Z\"}, \"eval_e5_xvla_attn_mean_obj_k03\": {\"completed_at\": \"2026-05-23T15:20:45.946Z\", \"conclusion\": \"success\", \"created_at\": \"2026-05-23T14:08:53.787Z\", \"hypothesis\": \"E5 attention_mean Object k=0.3: 极端剪枝（保留15/50 tokens）。attention_last k=0.3 正在跑。attention_mean k=0.5=98.4%——k=0.3 测试 mean 模式在极端条件下的退化点。\", \"metrics\": {\"source\": \"Director harvested from westd-38929\", \"success_rate\": 96, \"total_episodes\": 500, \"total_successes\": 480}, \"retry_count\": 0, \"spec\": {\"account\": \"root\", \"backend\": \"tmux\", \"checkpoint_path\": \"N/A\", \"command\": \"eval_xvla_attention_pruning_libero.py --mode attention_mean --suite libero_object --keep_ratio 0.3 --seed 42\", \"data_count\": 500, \"data_path\": \"LIBERO libero_object 10 tasks\", \"gpu\": [\"cuda:0\"], \"gpu_hours\": 1.2, \"log_path\": \"~/runs/importance_margin_vla_compress/eval_e5_xvla_attn_mean_obj_k03.log\", \"model_name\": \"X-VLA-Libero\", \"pid\": \"966968\", \"seed\": 42, \"server\": \"westd-38929\", \"submitted_at\": \"2026-05-23T14:08:52.581Z\", \"submitted_via\": \"submit_training_job\", \"wall_clock_seconds\": 4313.4}, \"status\": \"DONE\", \"updated_at\": \"2026-05-23T15:20:45.946Z\"}, \"eval_pi05_l2norm_k0925_spatial_seed42\": {\"completed_at\": \"2026-05-22T08:34:51.401Z\", \"conclusion\": \"success\", \"created_at\": \"2026-05-22T05:05:06.348Z\", \"hypothesis\": \"π0.5 L2norm k=0.925 Spatial: L2norm 在 Object k=0.925 无 cliff。Spatial L2norm 在 cliff zone 是否同样免疫？与 Random k=0.925 Spatial 对照。\", \"metrics\": {\"overall_SR\": 0.97, \"per_task\": {\"T0\": 1, \"T1\": 0.98, \"T2\": 0.98, \"T3\": 0.94, \"T4\": 0.92, \"T5\": 0.94, \"T6\": 1, \"T7\": 0.98, \"T8\": 1, \"T9\": 0.96}, \"total_episodes\": 500, \"total_successes\": 485}, \"retry_count\": 0, \"spec\": {\"account\": \"root\", \"backend\": \"tmux\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/importance_margin_vla_compress && MUJOCO_GL=egl TRANSFORMERS_OFFLINE=1 HF_HUB_OFFLINE=1 python -u eval_pi05_pruning_libero.py --suite libero_spatial --prune_mode l2norm --keep_ratio 0.925 --seed 42 --gpu 0 --n_episodes 50\\\"\", \"gpu\": [\"cuda:1\"], \"log_path\": \"~/runs/importance_margin_vla_compress/eval_pi05_l2norm_k0925_spatial_seed42.log\", \"pid\": \"747791\", \"server\": \"cqa1-33015\", \"submitted_at\": \"2026-05-23T14:09:27.491Z\", \"submitted_via\": \"submit_training_job\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-23T14:11:28.719Z\"}, \"eval_pi05_random_k085_spatial_seed42\": {\"checkpoint_path\": \"/root/autodl-tmp/importance_margin_vla_compress/eval_results/pi05_random_k0.85_libero_spatial_seed42.json\", \"completed_at\": \"2026-05-22T02:41:28.273Z\", \"conclusion\": \"success\", \"created_at\": \"2026-05-21T23:58:09.030Z\", \"extra\": {\"hook_events\": [{\"action\": \"agent\", \"event\": \"on_complete\", \"ts\": \"2026-05-22T01:49:19.291285+00:00\"}]}, \"hypothesis\": \"π0.5 Random k=0.85 Spatial: Object cliff 在 k=0.85 已跌至 5%。Spatial 的 cliff 位置在哪？如果 Spatial cliff 在不同位置则支持\\\"cliff 位置因 suite 而异\\\"的 claim。\", \"metrics\": {\"seed\": 42, \"success_rate\": 0.584, \"suite\": \"libero_spatial\"}, \"reproduce\": {\"finished_at\": \"2026-05-22T01:49:08.902Z\"}, \"retry_count\": 0, \"spec\": {\"account\": \"root\", \"backend\": \"tmux\", \"command\": \"bash -c \\\"cd /root/pi05_pruning_eval && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && python -u eval_pi05_pruning_libero.py --suite libero_spatial --prune_mode random --keep_ratio 0.85 --seed 42 --gpu 0 --n_episodes 50\\\"\", \"gpu\": [\"cuda:2\"], \"log_path\": \"~/runs/importance_margin_vla_compress/eval_pi05_random_k085_spatial_seed42.log\", \"pid\": \"unknown\", \"server\": \"westd-41074\", \"submitted_at\": \"2026-05-23T14:09:16.015Z\", \"submitted_via\": \"submit_training_job\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-23T14:11:19.422Z\"}, \"eval_e5_xvla_attn_mean_spatial_k05\": {\"completed_at\": \"2026-05-23T11:59:17.266Z\", \"conclusion\": \"success\", \"created_at\": \"2026-05-23T11:03:49.621Z\", \"hypothesis\": \"Attention-mean pruning at k=0.5 on X-VLA Spatial preserves performance because averaging attention across heads identifies globally important tokens more robustly than single-head attention.\", \"metrics\": {\"episodes\": 500, \"success_rate\": 91.6, \"successes\": 458, \"wilson_ci_95\": [88.8, 93.7]}, \"retry_count\": 0, \"spec\": {\"account\": \"root\", \"backend\": \"tmux\", \"checkpoint_path\": \"N/A - eval experiment\", \"checkpoint_source\": \"/root/autodl-tmp/X-VLA-Libero\", \"command\": \"bash -c \\\"source /etc/network_turbo 2>/dev/null; source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/importance_margin_vla_compress && HF_HOME=/root/autodl-tmp/.hf_cache MUJOCO_GL=egl python -u eval_xvla_attention_pruning_libero.py --model_path /root/autodl-tmp/X-VLA-Libero --suite libero_spatial --keep_ratio 0.5 --mode attention_mean --num_episodes 50 --seed 42 --gpu 0\\\"\", \"data_count\": 500, \"data_path\": \"libero_spatial\", \"eval_data\": \"libero_spatial\", \"gpu\": [\"cuda:0\"], \"gpu_hours\": 0.92, \"log_path\": \"~/runs/importance_margin_vla_compress/eval_e5_xvla_attn_mean_spatial_k05.log\", \"model_name\": \"X-VLA-Libero\", \"pid\": \"793357\", \"seed\": 42, \"server\": \"westd-27271\", \"submitted_at\": \"2026-05-23T11:03:48.562Z\", \"submitted_via\": \"submit_training_job\", \"wall_clock_seconds\": 3328.7}, \"status\": \"DONE\", \"updated_at\": \"2026-05-23T12:17:08.198Z\"}, \"eval_pi05_l2norm_k09_goal_seed42\": {\"completed_at\": \"2026-05-22T19:30:35.741Z\", \"conclusion\": \"negative\", \"created_at\": \"2026-05-22T10:56:42.238Z\", \"hypothesis\": \"π0.5 L2norm k=0.9 Goal seed42: Table 2 gap fill. L2norm 轻度 10% pruning on Goal. 预期接近 baseline，验证 Goal 上 cliff 位置\", \"metrics\": {\"num_episodes\": 500, \"num_success\": 450, \"seed\": 42, \"success_rate\": 0.9, \"suite\": \"libero_goal\"}, \"retry_count\": 0, \"spec\": {\"checkpoint_path\": \"eval_results/pi05_l2norm_k09_goal.json\", \"command\": \"CUDA_VISIBLE_DEVICES=2 HF_HOME=/root/autodl-tmp/.hf_cache TRANSFORMERS_OFFLINE=1 python -u eval_pi05_pruning_libero.py --prune_mode l2norm --keep_ratio 0.9 --suite libero_goal --n_episodes 500 --seed 42 --gpu 0\", \"data_count\": 500, \"data_path\": \"LIBERO-Goal\", \"gpu\": 2, \"log_path\": \"logs/eval_pi05_l2norm_k09_goal_seed42.log\", \"model_name\": \"pi0.5\", \"pid\": 932076, \"seed\": 42, \"server\": \"westd-38929\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-23T12:00:24.941Z\"}, \"eval_pi05_random_k07_goal_seed42\": {\"completed_at\": \"2026-05-22T19:12:45.452Z\", \"conclusion\": \"success\", \"created_at\": \"2026-05-22T16:36:38.476Z\", \"hypothesis\": \"π0.5 Random k=0.7 Goal seed42: Table 2 gap fill. Random 30% pruning on Goal suite. 对比 L2norm k=0.7 Goal 验证 importance-aware vs random 差距\", \"metrics\": {\"num_episodes\": 500, \"num_success\": 403, \"seed\": 42, \"success_rate\": 0.806, \"suite\": \"libero_goal\"}, \"retry_count\": 0, \"spec\": {\"checkpoint_path\": \"eval_results/pi05_random_0.7_libero_goal.json\", \"command\": \"python eval_pi05_pruning_libero.py --prune_mode random --keep_ratio 0.7 --suite libero_goal --n_episodes 50 --seed 42 --gpu 0\", \"data_count\": 50, \"data_path\": \"libero_goal\", \"log_path\": \"logs/pi05_random_0.7_libero_goal.log\", \"model_name\": \"pi0.5\", \"seed\": 42, \"server\": \"cqa1-33015\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-23T12:00:22.984Z\"}, \"eval_pi05_l2norm_k05_goal_seed42\": {\"completed_at\": \"2026-05-22T17:24:23.071Z\", \"conclusion\": \"negative\", \"created_at\": \"2026-05-22T15:46:53.768Z\", \"hypothesis\": \"π0.5 L2norm k=0.5 Goal seed42: Table 2 gap fill. L2norm 50% pruning on Goal suite. Goal tolerance 高于 Object，预测 L2norm k=0.5 Goal ≥ Object (52.6%)\", \"metrics\": {\"num_episodes\": 500, \"num_success\": 296, \"seed\": 42, \"success_rate\": 0.592, \"suite\": \"libero_goal\"}, \"retry_count\": 0, \"spec\": {\"checkpoint_path\": \"/root/autodl-tmp/importance_margin_vla_compress/eval_results/pi05_l2norm_k0.50_libero_goal_seed42.json\", \"command\": \"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/importance_margin_vla_compress && TRANSFORMERS_OFFLINE=1 HF_HOME=/root/autodl-tmp/.hf_cache python eval_pi05_pruning_libero.py --prune_mode l2norm --keep_ratio 0.5 --suite libero_goal --n_episodes 50 --seed 42 --gpu 1\", \"data_count\": 500, \"data_path\": \"/root/autodl-tmp/importance_margin_vla_compress\", \"log_path\": \"/root/autodl-tmp/importance_margin_vla_compress/logs/eval_pi05_l2norm_k05_goal_seed42.log\", \"model_name\": \"pi0.5\", \"seed\": 42, \"server\": \"westd-41074\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-23T12:00:20.927Z\"}, \"eval_pi05_l2norm_k085_long_seed43_v4\": {\"checkpoint_path\": \"/root/autodl-tmp/importance_margin_vla_compress/eval_results/pi05_l2norm_k0.85_libero_10_seed43.json\", \"completed_at\": \"2026-05-23T11:59:39.319Z\", \"conclusion\": \"success\", \"created_at\": \"2026-05-23T08:58:52.596Z\", \"hypothesis\": \"π0.5 L2 k=0.85 Long seed43: L2 轻度剪枝在 Long 上的 seed43 验证。预期 L2 k=0.85 ≥ Random k=0.85（L2 优于 random 在高保留比例）\", \"log_path\": \"~/runs/importance_margin_vla_compress/eval_pi05_l2norm_k085_long_seed43_v4.log\", \"metrics\": {\"elapsed_min\": 140.4, \"overall_sr\": 0.77, \"total_episodes\": 500, \"total_successes\": 385}, \"retry_count\": 0, \"spec\": {\"account\": \"root\", \"backend\": \"tmux\", \"command\": \"bash -c \\\"source /etc/network_turbo 2>/dev/null; export REQUESTS_CA_BUNDLE=/etc/ssl/certs/ca-certificates.crt; export SSL_CERT_FILE=/etc/ssl/certs/ca-certificates.crt; export HF_HUB_DISABLE_XET=1; source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/importance_margin_vla_compress && HF_HOME=/root/autodl-tmp/.hf_cache MUJOCO_GL=egl python -u eval_pi05_pruning_libero.py --prune_mode l2norm --keep_ratio 0.85 --suite libero_10 --n_episodes 50 --seed 43 --gpu 0\\\"\", \"data_count\": 500, \"data_path\": \"libero_10\", \"gpu\": [\"cuda:3\"], \"gpu_hours\": 3.01, \"log_path\": \"~/runs/importance_margin_vla_compress/eval_pi05_l2norm_k085_long_seed43_v4.log\", \"model_name\": \"pi05\", \"pid\": \"560924\", \"seed\": 43, \"server\": \"westd-41074\", \"submitted_at\": \"2026-05-23T08:58:51.546Z\", \"submitted_via\": \"submit_training_job\", \"wall_clock_seconds\": 10847.8}, \"status\": \"DONE\", \"updated_at\": \"2026-05-23T11:59:39.319Z\"}, \"eval_pi05_random_k085_long_seed43_v3\": {\"checkpoint_path\": \"/root/autodl-tmp/importance_margin_vla_compress/eval_results/pi05_random_k0.85_libero_10_seed43.json\", \"completed_at\": \"2026-05-23T11:59:36.023Z\", \"conclusion\": \"success\", \"created_at\": \"2026-05-23T08:58:49.076Z\", \"hypothesis\": \"π0.5 Random k=0.85 Long seed43: 轻度剪枝（保留 85%）在 Long 上的 seed43 验证。预期接近 baseline 性能\", \"log_path\": \"~/runs/importance_margin_vla_compress/eval_pi05_random_k085_long_seed43_v3.log\", \"metrics\": {\"elapsed_min\": 170.8, \"overall_sr\": 0.424, \"total_episodes\": 500, \"total_successes\": 212}, \"retry_count\": 0, \"spec\": {\"account\": \"root\", \"backend\": \"tmux\", \"command\": \"bash -c \\\"source /etc/network_turbo 2>/dev/null; export REQUESTS_CA_BUNDLE=/etc/ssl/certs/ca-certificates.crt; export SSL_CERT_FILE=/etc/ssl/certs/ca-certificates.crt; export HF_HUB_DISABLE_XET=1; source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/importance_margin_vla_compress && HF_HOME=/root/autodl-tmp/.hf_cache MUJOCO_GL=egl python -u eval_pi05_pruning_libero.py --prune_mode random --keep_ratio 0.85 --suite libero_10 --n_episodes 50 --seed 43 --gpu 0\\\"\", \"data_count\": 500, \"data_path\": \"libero_10\", \"gpu\": [\"cuda:2\"], \"gpu_hours\": 3.01, \"log_path\": \"~/runs/importance_margin_vla_compress/eval_pi05_random_k085_long_seed43_v3.log\", \"model_name\": \"pi05\", \"pid\": \"560674\", \"seed\": 43, \"server\": \"westd-41074\", \"submitted_at\": \"2026-05-23T08:58:48.046Z\", \"submitted_via\": \"submit_training_job\", \"wall_clock_seconds\": 10848.0}, \"status\": \"DONE\", \"updated_at\": \"2026-05-23T11:59:36.023Z\"}, \"eval_pi05_l2norm_k07_long_seed43_v4\": {\"checkpoint_path\": \"/root/autodl-tmp/importance_margin_vla_compress/eval_results/pi05_l2norm_k0.70_libero_10_seed43.json\", \"completed_at\": \"2026-05-23T11:59:32.864Z\", \"conclusion\": \"success\", \"created_at\": \"2026-05-23T08:58:45.513Z\", \"hypothesis\": \"π0.5 L2 k=0.7 Long seed43: L2 norm 中度剪枝在 Long 上的 seed43 验证。seed42 SR 已知，对比检验 variance\", \"log_path\": \"~/runs/importance_margin_vla_compress/eval_pi05_l2norm_k07_long_seed43_v4.log\", \"metrics\": {\"elapsed_min\": 148, \"overall_sr\": 0.654, \"total_episodes\": 500, \"total_successes\": 327}, \"retry_count\": 0, \"spec\": {\"account\": \"root\", \"backend\": \"tmux\", \"command\": \"bash -c \\\"source /etc/network_turbo 2>/dev/null; export REQUESTS_CA_BUNDLE=/etc/ssl/certs/ca-certificates.crt; export SSL_CERT_FILE=/etc/ssl/certs/ca-certificates.crt; export HF_HUB_DISABLE_XET=1; source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/importance_margin_vla_compress && HF_HOME=/root/autodl-tmp/.hf_cache MUJOCO_GL=egl python -u eval_pi05_pruning_libero.py --prune_mode l2norm --keep_ratio 0.7 --suite libero_10 --n_episodes 50 --seed 43 --gpu 0\\\"\", \"data_count\": 500, \"data_path\": \"libero_10\", \"gpu\": [\"cuda:1\"], \"gpu_hours\": 3.01, \"log_path\": \"~/runs/importance_margin_vla_compress/eval_pi05_l2norm_k07_long_seed43_v4.log\", \"model_name\": \"pi05\", \"pid\": \"560424\", \"seed\": 43, \"server\": \"westd-41074\", \"submitted_at\": \"2026-05-23T08:58:44.396Z\", \"submitted_via\": \"submit_training_job\", \"wall_clock_seconds\": 10848.5}, \"status\": \"DONE\", \"updated_at\": \"2026-05-23T11:59:32.864Z\"}, \"eval_e5_xvla_attn_rollout_spatial_k05\": {\"completed_at\": \"2026-05-23T11:59:22.601Z\", \"conclusion\": \"success\", \"created_at\": \"2026-05-23T11:03:53.245Z\", \"hypothesis\": \"Attention-rollout pruning at k=0.5 on X-VLA Spatial preserves performance because rollout captures cumulative token importance across layers, outperforming single-layer attention methods.\", \"metrics\": {\"elapsed_min\": 42.8, \"episodes\": 500, \"overall_sr\": 92.8, \"per_task_sr\": {\"T0_bowl_between_plate_ramekin\": 100, \"T1_bowl_next_ramekin\": 100, \"T2_bowl_table_center\": 100, \"T3_bowl_on_cookie_box\": 100, \"T4_bowl_top_drawer_cabinet\": 90, \"T5_bowl_on_ramekin\": 46, \"T6_bowl_next_cookie_box\": 100, \"T7_bowl_on_stove\": 94, \"T8_bowl_next_plate\": 98, \"T9_bowl_on_cabinet\": 100}, \"tasks\": 10, \"wilson_ci_95\": [90.2, 94.8]}, \"retry_count\": 0, \"spec\": {\"account\": \"root\", \"backend\": \"tmux\", \"checkpoint_path\": \"N/A - eval experiment\", \"checkpoint_source\": \"/root/autodl-tmp/X-VLA-Libero\", \"command\": \"bash -c \\\"source /etc/network_turbo 2>/dev/null; source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/importance_margin_vla_compress && HF_HOME=/root/autodl-tmp/.hf_cache MUJOCO_GL=egl python -u eval_xvla_attention_pruning_libero.py --model_path /root/autodl-tmp/X-VLA-Libero --suite libero_spatial --keep_ratio 0.5 --mode attention_rollout --num_episodes 50 --seed 42 --gpu 0\\\"\", \"data_count\": 500, \"data_path\": \"libero_spatial\", \"eval_data\": \"libero_spatial\", \"gpu\": [\"cuda:1\"], \"gpu_hours\": 0.93, \"log_path\": \"~/runs/importance_margin_vla_compress/eval_e5_xvla_attn_rollout_spatial_k05.log\", \"model_name\": \"X-VLA-Libero\", \"pid\": \"793628\", \"seed\": 42, \"server\": \"westd-27271\", \"submitted_at\": \"2026-05-23T11:03:52.186Z\", \"submitted_via\": \"submit_training_job\", \"wall_clock_seconds\": 3330.4}, \"status\": \"DONE\", \"updated_at\": \"2026-05-23T11:59:22.601Z\"}, \"eval_xvla_l2norm_k07_long_seed42_v2\": {\"completed_at\": \"2026-05-23T09:02:37.188Z\", \"conclusion\": \"killed\", \"created_at\": \"2026-05-23T08:04:20.474Z\", \"hypothesis\": \"X-VLA L2norm k=0.7 Long seed42 v2: 重跑 v1（进程死亡无结果）。Table 2 gap. L2 k=0.9 Long=27.5%, L2 k=0.95 Long=47.0%. L2 在 Long 上非单调，k=0.7 是否继续下降。\", \"parent\": \"eval_xvla_l2norm_k07_long_seed42\", \"retry_count\": 0, \"spec\": {\"checkpoint_path\": \"N/A - killed\", \"checkpoint_source\": \"/root/autodl-tmp/X-VLA-Libero\", \"command\": \"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/importance_margin_vla_compress && HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 HF_HOME=/root/autodl-tmp/.hf_cache MUJOCO_GL=egl CUDA_VISIBLE_DEVICES=0 python -u eval_xvla_pruning_libero.py --model_path /root/autodl-tmp/X-VLA-Libero --suite libero_10 --keep_ratio 0.7 --mode l2_norm --num_episodes 50 --seed 42 --domain_id 3 --gpu 0\", \"data_count\": 500, \"data_path\": \"libero_10_long_domain3\", \"eval_data\": \"libero_10_long_domain3\", \"log_path\": \"~/runs/importance_margin_vla_compress/eval_xvla_l2norm_k07_long_seed42_v2.log\", \"model_name\": \"X-VLA-Libero\", \"seed\": 42, \"server\": \"westd-38929\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-23T09:02:37.188Z\"}, \"eval_xvla_l2norm_k07_long_seed42\": {\"completed_at\": \"2026-05-23T08:01:12.678Z\", \"conclusion\": \"success\", \"created_at\": \"2026-05-23T06:11:48.575Z\", \"extra\": {\"hook_events\": [{\"action\": \"agent\", \"event\": \"on_failed\", \"ts\": \"2026-05-23T08:01:50.962295+00:00\"}]}, \"failure_reason\": \"process dead 5× with no sentinel/W&B — auto-resolved as failed\", \"hypothesis\": \"X-VLA L2norm k=0.7 Long seed42: Table 2 gap. L2 k=0.9 Long=27.5%, L2 k=0.95 Long=47.0%. L2 在 Long 上非单调（k=0.9 < k=0.95），k=0.7 是否继续下降。\", \"metrics\": {\"overall_SR\": 0.494, \"per_task_SR\": {\"T0_alphabet_soup_tomato\": 0.12, \"T1_cream_cheese_butter\": 0.04, \"T2_stove_moka\": 0.56, \"T3_bowl_drawer\": 0.98, \"T4_mugs_plates\": 0.68, \"T5_book_caddy\": 0.94, \"T6_mug_pudding\": 0.78, \"T7_soup_cream_cheese\": 0.76, \"T8_two_moka_pots\": 0, \"T9_mug_microwave\": 0.08}, \"total_episodes\": 500, \"total_successes\": 247}, \"notes\": \"失败原因: 标记 RUNNING 但从未实际提交（无 server/pid/spec/command）。cron 检测进程不存在 (miss 3/5)。无日志文件。需要重新提交。\", \"reproduce\": {\"finished_at\": \"2026-05-23T08:01:23.404Z\"}, \"retry_count\": 0, \"spec\": {\"checkpoint_path\": \"/root/autodl-tmp/importance_margin_vla_compress/xvla_checkpoints/\", \"checkpoint_source\": \"/root/autodl-tmp/X-VLA-Libero\", \"command\": \"python eval_xvla_pruning_libero.py --prune_mode l2norm --keep_ratio 0.7 --suite libero_10 --n_episodes 50 --seed 42\", \"data_count\": 500, \"data_path\": \"LIBERO-Long\", \"eval_data\": \"libero_10\", \"gpu\": 0, \"log_path\": \"/root/autodl-tmp/importance_margin_vla_compress/logs/\", \"model_name\": \"X-VLA\", \"pid\": 457656, \"seed\": 42, \"server\": \"westd-27271\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-23T08:10:05.695Z\"}, \"eval_xvla_random_k09_long_seed42\": {\"completed_at\": \"2026-05-23T08:01:30.670Z\", \"conclusion\": \"success\", \"created_at\": \"2026-05-23T06:11:46.837Z\", \"hypothesis\": \"X-VLA Random k=0.9 Long seed42: Table 2 gap. L2 k=0.9 Long=27.5%, Random k=0.95 Long=48.2%. L2 在 k=0.9 已 catastrophic，Random 是否也 catastrophic 或保持更高。\", \"metrics\": {\"elapsed_min\": 104.4, \"episodes\": 500, \"overall_sr\": 29.6, \"per_task_sr\": {\"task_0_alphabet_soup_tomato_sauce\": 0, \"task_1_cream_cheese_butter\": 16, \"task_2_stove_moka_pot\": 0, \"task_3_black_bowl_drawer\": 96, \"task_4_white_mug_yellow_mug\": 36, \"task_5_book_caddy\": 98, \"task_6_white_mug_chocolate_pudding\": 0, \"task_7_alphabet_soup_cream_cheese\": 0, \"task_8_both_moka_pots\": 0, \"task_9_mug_microwave\": 50}, \"wilson_ci_95\": [25.8, 33.7]}, \"retry_count\": 0, \"spec\": {\"checkpoint_path\": \"N/A - eval experiment\", \"checkpoint_source\": \"/root/autodl-tmp/X-VLA-Libero\", \"command\": \"HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 HF_HOME=/root/autodl-tmp/.hf_cache MUJOCO_GL=egl CUDA_VISIBLE_DEVICES=1 python -u eval_xvla_pruning_libero.py --model_path /root/autodl-tmp/X-VLA-Libero --suite libero_10 --keep_ratio 0.9 --mode random --num_episodes 50 --seed 42 --domain_id 3 --gpu 0\", \"data_count\": 500, \"data_path\": \"libero_10\", \"eval_data\": \"libero_10\", \"gpu\": 1, \"log_path\": \"logs/eval_xvla_random_k09_long_seed42.log\", \"model_name\": \"X-VLA-Libero\", \"pid\": 251117, \"seed\": 42, \"server\": \"westd-27271\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-23T08:01:30.670Z\"}, \"eval_xvla_random_k07_long_seed42\": {\"completed_at\": \"2026-05-23T07:49:58.127Z\", \"conclusion\": \"success\", \"created_at\": \"2026-05-23T06:11:50.264Z\", \"hypothesis\": \"X-VLA Random k=0.7 Long seed42: Table 2 gap. Random k=0.95 Long=48.2%. 30% pruning 下 random 在 Long suite 的表现。\", \"metrics\": {\"keep_ratio\": 0.7, \"per_task_sr\": [10, 8, 66, 98, 82, 100, 82, 70, 4, 10], \"prune_method\": \"random\", \"seed\": 42, \"success_rate\": 53, \"suite\": \"libero_10\", \"tokens_kept\": \"35/50\", \"total_episodes\": 500, \"total_successes\": 265, \"wall_time_min\": 87, \"wilson_ci_95\": [48.6, 57.3]}, \"retry_count\": 0, \"spec\": {\"checkpoint_path\": \"N/A - eval experiment\", \"checkpoint_source\": \"/root/autodl-tmp/X-VLA-Libero\", \"command\": \"HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 HF_HOME=/root/autodl-tmp/.hf_cache MUJOCO_GL=egl CUDA_VISIBLE_DEVICES=1 python -u eval_xvla_pruning_libero.py --model_path /root/autodl-tmp/X-VLA-Libero --suite libero_10 --keep_ratio 0.7 --mode random --num_episodes 50 --seed 42 --domain_id 3 --gpu 0\", \"data_count\": 500, \"data_path\": \"libero_10\", \"eval_data\": \"libero_10\", \"gpu\": 1, \"log_path\": \"logs/eval_xvla_random_k07_long_seed42.log\", \"model_name\": \"X-VLA-Libero\", \"pid\": 458574, \"seed\": 42, \"server\": \"westd-38929\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-23T07:49:58.127Z\"}, \"eval_pi05_l2norm_k095_object_seed42_v2\": {\"checkpoint_path\": \"/root/autodl-tmp/pi05_libero_finetuned\", \"completed_at\": \"2026-05-22T01:40:56.708Z\", \"conclusion\": \"success\", \"created_at\": \"2026-05-22T00:30:25.866Z\", \"extra\": {\"hook_events\": [{\"action\": \"agent\", \"event\": \"on_complete\", \"ts\": \"2026-05-22T01:35:57.662928+00:00\"}], \"previous_failure\": {\"conclusion\": \"success\", \"metrics\": {\"eval_episodes_per_task\": 50, \"keep_ratio\": 0.95, \"per_task_sr\": [96, 98, 96, 96, 96, 100, 100, 100, 100, 100], \"prune_method\": \"l2norm\", \"seed\": 42, \"success_rate\": 98.2, \"suite\": \"libero_object\", \"tokens_kept\": \"243/256\", \"total_episodes\": 500, \"total_success\": 491, \"wall_time_min\": 63.2}}}, \"hypothesis\": \"π0.5 L2norm k=0.95 Object seed42 v2: 补充 registry 缺失数据点。k=0.9 L2=98.2%, k=0.85 L2=98.0% 形成 plateau，k=0.95 预期 ≥98.0%。v1 卡在 PREPARING 从未执行。\", \"log_path\": \"/root/autodl-tmp/importance_margin_vla_compress/logs/eval_pi05_l2norm_k095_object_seed42_v2.log\", \"metrics\": {\"per_task_sr\": [96, 98, 96, 96, 96, 100, 100, 100, 100, 100], \"success_rate\": 98.2, \"tokens_kept\": 243, \"tokens_total\": 256, \"total_episodes\": 500, \"total_successes\": 491, \"wall_time_min\": 63.2}, \"parent\": \"eval_pi05_l2norm_k095_object_seed42\", \"reproduce\": {\"finished_at\": \"2026-05-22T01:35:48.127Z\"}, \"retry_count\": 1, \"spec\": {\"checkpoint_source\": \"/root/autodl-tmp/pi05_libero_finetuned\", \"command\": \"python eval_pi05_prune.py --prune-mode l2norm --keep-ratio 0.95 --suite libero_object --seed 42\", \"data_count\": 500, \"data_path\": \"/root/autodl-tmp/importance_margin_vla_compress/eval_results/pi05_l2norm_k0.95_libero_object_seed42.json\", \"eval_data\": \"libero_object\", \"model_name\": \"pi05\", \"seed\": 42, \"server\": \"westd-41074\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-23T07:48:39.254Z\"}, \"eval_pi05_random_k09_object_seed43_v4\": {\"checkpoint_path\": \"/root/autodl-tmp/pi05_libero_finetuned\", \"completed_at\": \"2026-05-23T07:48:12.783Z\", \"conclusion\": \"success\", \"created_at\": \"2026-05-23T03:50:06.423Z\", \"hypothesis\": \"π0.5 Random k=0.9 Object seed43 cliff 验证 v4。seed42=12.0%。v1/v2/v3 均因环境问题失败。本次确保 HF 离线环境变量完整。\", \"log_path\": \"/root/autodl-tmp/importance_margin_vla_compress/logs/eval_pi05_random_k09_object_seed43_v4.log\", \"metrics\": {\"keep_ratio\": 0.9, \"per_task_sr\": [16, 16, 10, 2, 6, 14, 14, 2, 8, 8], \"prune_method\": \"random\", \"seed\": 43, \"success_rate\": 9.6, \"suite\": \"libero_object\", \"tokens_kept\": 230, \"tokens_total\": 256, \"total_episodes\": 500, \"total_successes\": 48, \"wall_time_min\": 119.5}, \"parent\": \"eval_pi05_random_k09_object_seed43_v3\", \"retry_count\": 0, \"spec\": {\"checkpoint_source\": \"/root/autodl-tmp/pi05_libero_finetuned\", \"command\": \"eval_pi05_pruning_libero.py --prune_mode random --keep_ratio 0.9 --suite libero_object --n_episodes 50 --seed 43\", \"data_count\": 500, \"data_path\": \"/root/autodl-tmp/importance_margin_vla_compress\", \"eval_data\": \"libero_object\", \"model_name\": \"pi05\", \"seed\": 43, \"server\": \"westd-41074\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-23T07:48:12.783Z\"}, \"eval_xvla_random_k07_spatial_seed42\": {\"checkpoint_path\": \"n/a (inference-only eval)\", \"completed_at\": \"2026-05-22T22:24:48.210Z\", \"conclusion\": \"negative\", \"created_at\": \"2026-05-22T20:36:32.966Z\", \"hypothesis\": \"X-VLA Random k=0.7 Spatial seed42: Table 2 gap. L2 k=0.7 Spatial=72.0%. BART encoder 的 cross-token 依赖在 30% pruning 下 random vs L2 的 gap 大小。\", \"log_path\": \"logs/eval_xvla_random_k07_spatial_seed42.log\", \"metrics\": {\"overall_SR\": 0.766, \"total_episodes\": 500, \"total_successes\": 383}, \"retry_count\": 0, \"status\": \"DONE\", \"updated_at\": \"2026-05-23T06:11:43.217Z\"}, \"eval_xvla_random_k095_long_seed42\": {\"checkpoint_path\": \"N/A (eval-only)\", \"completed_at\": \"2026-05-23T04:23:41.303Z\", \"conclusion\": \"success\", \"created_at\": \"2026-05-23T02:49:13.642Z\", \"hypothesis\": \"X-VLA Random k=0.95 Long seed42: L2 k=0.95=47.0% (-47pp from 94.0% baseline)。Random pruning 在 50 tokens 上对 Long suite 的影响。BART encoder 的 cross-token 依赖在 Long horizon 下是否使 random/L2 差异放大。\", \"metrics\": {\"eval_episodes_per_task\": 50, \"keep_ratio\": 0.95, \"per_task_sr\": [0, 46, 72, 90, 54, 98, 18, 10, 92, 2], \"prune_method\": \"random\", \"seed\": 42, \"success_rate\": 48.2, \"suite\": \"libero_10\", \"tokens_kept\": \"47/50\", \"total_episodes\": 500, \"total_success\": 241, \"wall_time_min\": 91.2, \"wilson_ci_95\": [43.9, 52.6]}, \"retry_count\": 0, \"spec\": {\"checkpoint_source\": \"/root/autodl-tmp/X-VLA-Libero\", \"command\": \"HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 HF_HOME=/root/autodl-tmp/.hf_cache MUJOCO_GL=egl python -u eval_xvla_pruning_libero.py --model_path /root/autodl-tmp/X-VLA-Libero --suite libero_10 --keep_ratio 0.95 --mode random --num_episodes 50 --seed 42 --domain_id 3 --gpu 0\", \"data_count\": 500, \"data_path\": \"libero_10\", \"eval_data\": \"libero_10\", \"log_path\": \"/root/autodl-tmp/importance_margin_vla_compress/logs/eval_xvla_random_k095_long_seed42.log\", \"model_name\": \"X-VLA-Libero\", \"pid\": 126840, \"seed\": 42, \"server\": \"westd-27271\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-23T04:23:41.303Z\"}, \"eval_pi05_random_k09_object_seed43_v3\": {\"completed_at\": \"2026-05-23T03:44:05.430Z\", \"conclusion\": \"success\", \"created_at\": \"2026-05-23T01:57:37.489Z\", \"failure_reason\": \"startup recovery: RUNNING with no cron and no server/pid info\", \"hypothesis\": \"π0.5 Random k=0.9 Object seed43 验证实验。seed42=12.0%，v2 seed43=9.6%，v3 重新确认 cliff 底部的 seed 稳定性。\", \"metrics\": {\"note\": \"Harvested from eval_results/pi05_random_k0.90_libero_object_seed43.json on westd-27271. Reviewer-confirmed.\", \"seed\": 43, \"success_rate\": 9.6, \"total_episodes\": 500, \"total_successes\": 48}, \"retry_count\": 0, \"spec\": {\"checkpoint_source\": \"N/A\", \"command\": \"python -u eval_pi05_pruning_libero.py --prune_mode random --keep_ratio 0.9 --suite libero_object --n_episodes 50 --seed 43 --gpu 0\", \"data_count\": 50, \"data_path\": \"libero_object\", \"eval_data\": \"libero_object\", \"model_name\": \"pi0.5\", \"seed\": 43, \"server\": \"westd-27271\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-23T04:11:07.275Z\"}, \"eval_pi05_random_k05_long_seed43_v2\": {\"completed_at\": \"2026-05-23T03:43:24.375Z\", \"conclusion\": \"success\", \"created_at\": \"2026-05-22T22:53:33.116Z\", \"failure_reason\": \"startup recovery: RUNNING with no cron and no server/pid info\", \"hypothesis\": \"π0.5 Random k=0.5 Long seed43 v2: seed42=50.2%, 需要 seed43 验证。之前 v1 在 westd-41074 因缺环境变量失败，本次修复后重试。\", \"metrics\": {\"benchmark\": \"libero_10\", \"keep_ratio\": 0.5, \"prune_method\": \"random\", \"success_rate\": 51.2, \"total_episodes\": 500, \"total_success\": 256}, \"retry_count\": 0, \"spec\": {\"checkpoint_path\": \"n/a (inference-only eval)\", \"checkpoint_source\": \"pi0.5_pretrained\", \"command\": \"TRANSFORMERS_OFFLINE=1 HF_HOME=/root/autodl-tmp/.hf_cache HF_HUB_OFFLINE=1 CUDA_VISIBLE_DEVICES=2 python -u eval_pi05_pruning_libero.py --prune_mode random --keep_ratio 0.5 --suite libero_10 --n_episodes 50 --seed 43 --gpu 0\", \"data_count\": 500, \"data_path\": \"libero_10\", \"eval_data\": \"libero_10\", \"log_path\": \"logs/eval_pi05_random_k05_long_seed43_v2.log\", \"model_name\": \"pi0.5\", \"seed\": 43, \"server\": \"westd-41074\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-23T03:48:23.605Z\"}, \"eval_pi05_random_k085_long_seed43\": {\"completed_at\": \"2026-05-23T03:43:30.402Z\", \"conclusion\": \"success\", \"created_at\": \"2026-05-22T22:53:35.448Z\", \"failure_reason\": \"startup recovery: RUNNING with no cron and no server/pid info\", \"hypothesis\": \"π0.5 Random k=0.85 Long seed43：seed42 Random Long 曲线非单调（k=0.7=64.6% > k=0.85=44.4% > k=0.9=31.8%）。seed43 验证这一异常模式是否可复现。\", \"metrics\": {\"benchmark\": \"libero_10\", \"keep_ratio\": 0.85, \"prune_method\": \"random\", \"success_rate\": 41.8, \"total_episodes\": 500, \"total_success\": 209}, \"retry_count\": 0, \"spec\": {\"checkpoint_path\": \"n/a (inference-only eval)\", \"checkpoint_source\": \"pi0.5_pretrained\", \"command\": \"CUDA_VISIBLE_DEVICES=0 TRANSFORMERS_OFFLINE=1 HF_HOME=/root/autodl-tmp/.hf_cache HF_HUB_OFFLINE=1 python -u eval_pi05_pruning_libero.py --prune_mode random --keep_ratio 0.85 --suite libero_10 --n_episodes 50 --seed 43 --gpu 0\", \"data_count\": 500, \"data_path\": \"libero_10\", \"eval_data\": \"libero_10\", \"log_path\": \"logs/eval_pi05_random_k085_long_seed43.log\", \"model_name\": \"pi0.5\", \"seed\": 43, \"server\": \"westd-41074\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-23T03:48:21.531Z\"}, \"eval_pi05_l2norm_k07_long_seed43_v2\": {\"completed_at\": \"2026-05-23T03:43:45.109Z\", \"conclusion\": \"success\", \"created_at\": \"2026-05-23T00:32:57.840Z\", \"failure_reason\": \"startup recovery: process dead, no active cron monitor\", \"hypothesis\": \"π0.5 L2norm k=0.7 Long seed43 v2: v1 静默崩溃（缺少HF离线环境变量）。seed42=60.0%。Method crossover 参考点（Random k=0.7=64.6% > L2=60.0%）。验证 crossover 的 reproducibility。\", \"metrics\": {\"benchmark\": \"libero_10\", \"keep_ratio\": 0.7, \"prune_method\": \"l2norm\", \"success_rate\": 65.8, \"total_episodes\": 500, \"total_success\": 329}, \"retry_count\": 0, \"spec\": {\"checkpoint_path\": \"n/a (inference-only eval)\", \"checkpoint_source\": \"pi0.5_pretrained\", \"command\": \"CUDA_VISIBLE_DEVICES=1 TRANSFORMERS_OFFLINE=1 HF_HUB_OFFLINE=1 HF_HOME=/root/autodl-tmp/.hf_cache python -u eval_pi05_pruning_libero.py --prune_mode l2norm --keep_ratio 0.7 --suite libero_10 --n_episodes 50 --seed 43 --gpu 0\", \"data_count\": 500, \"data_path\": \"libero_10\", \"eval_data\": \"libero_10\", \"gpu\": [\"cuda:1\"], \"log_path\": \"~/runs/importance_margin_vla_compress/eval_pi05_l2norm_k07_long_seed43_v2.log\", \"model_name\": \"pi0.5\", \"pid\": \"289572\", \"seed\": 43, \"server\": \"westd-38929\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-23T03:48:19.498Z\"}, \"eval_pi05_random_k03_long_seed43_v3\": {\"completed_at\": \"2026-05-23T03:43:52.378Z\", \"conclusion\": \"success\", \"created_at\": \"2026-05-23T00:32:59.653Z\", \"failure_reason\": \"startup recovery: process dead, no active cron monitor\", \"hypothesis\": \"π0.5 Random k=0.3 Long seed43 v3: v1 exit=1, v2 静默崩溃（缺少HF离线环境变量）。seed42=29.0%。V-shape extreme floor 验证。\", \"metrics\": {\"benchmark\": \"libero_10\", \"keep_ratio\": 0.3, \"prune_method\": \"random\", \"success_rate\": 28.4, \"total_episodes\": 500, \"total_success\": 142}, \"retry_count\": 0, \"spec\": {\"checkpoint_path\": \"n/a (inference-only eval)\", \"checkpoint_source\": \"pi0.5_pretrained\", \"command\": \"CUDA_VISIBLE_DEVICES=2 TRANSFORMERS_OFFLINE=1 HF_HUB_OFFLINE=1 HF_HOME=/root/autodl-tmp/.hf_cache python -u eval_pi05_pruning_libero.py --prune_mode random --keep_ratio 0.3 --suite libero_10 --n_episodes 50 --seed 43 --gpu 0\", \"data_count\": 500, \"data_path\": \"libero_10\", \"eval_data\": \"libero_10\", \"gpu\": [\"cuda:2\"], \"log_path\": \"~/runs/importance_margin_vla_compress/eval_pi05_random_k03_long_seed43_v3.log\", \"model_name\": \"pi0.5\", \"pid\": \"289643\", \"seed\": 43, \"server\": \"westd-38929\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-23T03:48:17.386Z\"}, \"eval_pi05_l2norm_k085_long_seed43_v2\": {\"completed_at\": \"2026-05-23T03:43:59.406Z\", \"conclusion\": \"success\", \"created_at\": \"2026-05-23T00:33:01.293Z\", \"failure_reason\": \"startup recovery: process dead, no active cron monitor\", \"hypothesis\": \"π0.5 L2norm k=0.85 Long seed43 v2: v1 静默崩溃（缺少HF离线环境变量）。seed42=78.0%。L2norm 单调下降曲线验证。\", \"metrics\": {\"benchmark\": \"libero_10\", \"keep_ratio\": 0.85, \"per_task_sr\": {\"T2\": 88, \"T3\": 96, \"T4\": 70, \"T5\": 98, \"T6\": 12, \"T7\": 80, \"T8\": 64, \"T9\": 88}, \"prune_method\": \"l2norm\", \"success_rate\": 79, \"total_episodes\": 500, \"total_success\": 395}, \"retry_count\": 0, \"spec\": {\"checkpoint_path\": \"n/a (inference-only eval)\", \"checkpoint_source\": \"pi0.5_pretrained\", \"command\": \"CUDA_VISIBLE_DEVICES=3 TRANSFORMERS_OFFLINE=1 HF_HUB_OFFLINE=1 HF_HOME=/root/autodl-tmp/.hf_cache python -u eval_pi05_pruning_libero.py --prune_mode l2norm --keep_ratio 0.85 --suite libero_10 --n_episodes 50 --seed 43 --gpu 0\", \"data_count\": 500, \"data_path\": \"libero_10\", \"eval_data\": \"libero_10\", \"gpu\": [\"cuda:3\"], \"log_path\": \"~/runs/importance_margin_vla_compress/eval_pi05_l2norm_k085_long_seed43_v2.log\", \"model_name\": \"pi0.5\", \"pid\": \"289780\", \"seed\": 43, \"server\": \"westd-38929\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-23T03:48:15.118Z\"}, \"eval_pi05_random_k05_spatial_seed43_v2\": {\"completed_at\": \"2026-05-23T03:20:45.440Z\", \"conclusion\": \"success\", \"created_at\": \"2026-05-23T01:41:55.447Z\", \"hypothesis\": \"π0.5 Random k=0.5 Spatial seed43 v2 re-run。v1 stale after 14h with no metrics。重新部署到 westd-41074:1 验证。\", \"log_path\": \"/root/autodl-tmp/importance_margin_vla_compress/logs/eval_pi05_random_k05_spatial_seed43.log\", \"metrics\": {\"elapsed_min\": 80.6, \"per_task_sr\": {\"T0_between_plate_ramekin\": 88, \"T1_next_to_ramekin\": 88, \"T2_table_center\": 88, \"T3_on_cookie_box\": 56, \"T4_top_drawer\": 38, \"T5_on_ramekin\": 32, \"T6_next_to_cookie_box\": 86, \"T7_on_stove\": 92, \"T8_next_to_plate\": 72, \"T9_on_wooden_cabinet\": 84}, \"success_rate\": 72.4, \"total_episodes\": 500, \"total_successes\": 362}, \"retry_count\": 0, \"spec\": {\"checkpoint_path\": \"n/a (inference-only eval)\", \"checkpoint_source\": \"pi0.5_pretrained\", \"command\": \"CUDA_VISIBLE_DEVICES=1 bash -c 'source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/importance_margin_vla_compress && HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 HF_HOME=/root/autodl-tmp/.hf_cache MUJOCO_GL=egl python -u eval_pi05_pruning_libero.py --prune_mode random --keep_ratio 0.5 --suite libero_spatial --n_episodes 50 --seed 43 --gpu 0'\", \"data_count\": 500, \"data_path\": \"libero_spatial\", \"eval_data\": \"libero_spatial\", \"log_path\": \"logs/eval_pi05_random_k05_spatial_seed43_v2.log\", \"model_name\": \"pi0.5\", \"seed\": 43, \"server\": \"westd-41074\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-23T03:20:45.440Z\"}, \"eval_xvla_baseline_spatial_seed42\": {\"completed_at\": \"2026-05-21T00:48:55.660Z\", \"conclusion\": \"success\", \"created_at\": \"2026-05-20T22:55:31.536Z\", \"hypothesis\": \"X-VLA baseline (no pruning, keep_ratio=1.0) on libero_spatial establishes the unpruned reference performance for spatial reasoning tasks, expected ~90%+ SR matching published results.\", \"metrics\": {\"note\": \"Corrected from 0.916 to 0.930 per Reviewer SSH verification of xvla_prune_k1.0_libero_spatial.json (465/500)\", \"num_episodes\": 500, \"success_rate\": 0.93, \"total_successes\": 465, \"wilson_ci_95\": [0.904, 0.95]}, \"retry_count\": 0, \"spec\": {\"checkpoint_path\": \"/root/autodl-tmp/X-VLA-Libero\", \"command\": \"CUDA_VISIBLE_DEVICES=0 MUJOCO_GL=egl python -u eval_xvla_pruning_libero.py --model_path /root/autodl-tmp/X-VLA-Libero --suite libero_spatial --keep_ratio 1.0 --num_episodes 50 --seed 42 --domain_id 3 --gpu 0 --output eval_results/xvla_baseline_libero_spatial_seed42.json\", \"data_count\": 50, \"data_path\": \"libero_spatial\", \"gpu\": \"cuda:0\", \"log_path\": \"/root/autodl-tmp/importance_margin_vla_compress/eval_results/xvla_baseline_libero_spatial_seed42.json\", \"model_name\": \"X-VLA-Libero\", \"seed\": 42, \"server\": \"cqa1-33015\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-23T03:07:51.703Z\"}, \"eval_xvla_baseline_goal_seed42\": {\"completed_at\": \"2026-05-21T00:48:57.213Z\", \"conclusion\": \"success\", \"created_at\": \"2026-05-20T22:55:34.464Z\", \"hypothesis\": \"X-VLA baseline (no pruning, keep_ratio=1.0) on libero_goal establishes the unpruned reference performance for goal-conditioned tasks, expected ~95%+ SR matching published results.\", \"metrics\": {\"note\": \"Corrected from 0.98 to 0.984 per Reviewer SSH verification (492/500)\", \"num_episodes\": 500, \"success_rate\": 0.984, \"total_successes\": 492, \"wilson_ci_95\": [0.969, 0.992]}, \"retry_count\": 0, \"spec\": {\"checkpoint_path\": \"/root/autodl-tmp/X-VLA-Libero\", \"command\": \"CUDA_VISIBLE_DEVICES=3 MUJOCO_GL=egl python -u eval_xvla_pruning_libero.py --model_path /root/autodl-tmp/X-VLA-Libero --suite libero_goal --keep_ratio 1.0 --num_episodes 50 --seed 42 --domain_id 3 --gpu 0 --output eval_results/xvla_baseline_libero_goal_seed42.json\", \"data_count\": 50, \"data_path\": \"libero_goal\", \"gpu\": \"cuda:3\", \"log_path\": \"/root/autodl-tmp/importance_margin_vla_compress/eval_results/xvla_baseline_libero_goal_seed42.json\", \"model_name\": \"X-VLA-Libero\", \"seed\": 42, \"server\": \"cqa1-33015\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-23T02:48:04.584Z\"}, \"eval_xvla_prune_k09_seed42\": {\"completed_at\": \"2026-05-23T01:49:39.840Z\", \"conclusion\": \"success\", \"created_at\": \"2026-05-23T01:49:07.119Z\", \"hypothesis\": \"X-VLA L2 norm pruning k=0.9 on LIBERO-Object seed42. X-VLA baseline=99.2%. At 10% token removal, L2 norm selection should maintain near-baseline performance given BART encoder's moderate CV=0.151. Establishes the k=0.9 reference point for the X-VLA Object degradation curve.\", \"metrics\": {\"note\": \"Reconstructed entry. SR=99.2% (seed42). Cross-seed range 97.6%–99.2% (seed43=97.6%, seed44=98.2%). Original JSON may exist on cqa1-33015.\", \"num_episodes\": 500, \"seed\": 42, \"success_rate\": 0.992}, \"retry_count\": 0, \"spec\": {\"checkpoint_path\": \"N/A (eval only)\", \"checkpoint_source\": \"/root/autodl-tmp/X-VLA-Libero\", \"command\": \"CUDA_VISIBLE_DEVICES=0 python -u eval_xvla_pruning_libero.py --model_path /root/autodl-tmp/X-VLA-Libero --suite libero_object --keep_ratio 0.9 --num_episodes 50 --seed 42 --domain_id 3 --gpu 0\", \"data_count\": 500, \"data_path\": \"libero_object\", \"eval_data\": \"LIBERO-Object (10 tasks x 50 episodes)\", \"log_path\": \"N/A (reconstructed entry)\", \"model_name\": \"X-VLA-Libero\", \"seed\": 42, \"server\": \"cqa1-33015\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-23T01:49:39.840Z\"}, \"eval_pi05_random_k09_long_seed43\": {\"completed_at\": \"2026-05-23T01:42:56.008Z\", \"conclusion\": \"success\", \"created_at\": \"2026-05-22T22:25:17.282Z\", \"hypothesis\": \"π0.5 Random k=0.9 Long seed43: seed42=31.8% 出现 V-shape dip（k=0.85=44.4% > k=0.9=31.8%）。需要 multi-seed 确认这个 dip 是真实现象还是 seed noise。\", \"metrics\": {\"sr\": 0.308, \"total_episodes\": 500}, \"retry_count\": 0, \"spec\": {\"checkpoint_path\": \"n/a (inference-only eval)\", \"checkpoint_source\": \"pi0.5_pretrained\", \"command\": \"TRANSFORMERS_OFFLINE=1 HF_HOME=/root/autodl-tmp/.hf_cache HF_HUB_OFFLINE=1 CUDA_VISIBLE_DEVICES=0 python -u eval_pi05_pruning_libero.py --prune_mode random --keep_ratio 0.9 --suite libero_10 --n_episodes 50 --seed 43 --gpu 0\", \"data_count\": 500, \"data_path\": \"libero_10\", \"eval_data\": \"libero_10\", \"log_path\": \"logs/eval_pi05_random_k09_long_seed43.log\", \"model_name\": \"pi0.5\", \"seed\": 43, \"server\": \"westd-38929\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-23T01:42:56.007Z\"}, \"eval_pi05_random_k05_spatial_seed43\": {\"checkpoint_path\": \"N/A - eval experiment\", \"completed_at\": \"2026-05-22T20:14:39.620Z\", \"conclusion\": \"negative\", \"created_at\": \"2026-05-22T05:40:55.533Z\", \"failure_reason\": \"stale RUNNING, no metrics after 14h\", \"hypothesis\": \"π0.5 Random k=0.5 Spatial seed43 验证实验。seed42 数据已有。Random 在 Spatial suite 中等压缩区间的 seed 稳定性验证。\", \"log_path\": \"~/runs/importance_margin_vla_compress/eval_pi05_random_k05_spatial_seed43.log\", \"retry_count\": 0, \"spec\": {\"account\": \"root\", \"backend\": \"tmux\", \"checkpoint_source\": \"pi0-fast-pruned-random-k05\", \"command\": \"eval_pi05_pruning_libero.py --prune_mode random --keep_ratio 0.5 --suite libero_spatial --seed 43\", \"data_count\": 500, \"data_path\": \"libero_spatial\", \"eval_data\": \"libero_spatial\", \"gpu\": [\"cuda:0\"], \"gpu_hours\": 14.56, \"log_path\": \"~/runs/importance_margin_vla_compress/eval_pi05_random_k05_spatial_seed43.log\", \"model_name\": \"pi0-fast\", \"pid\": \"603678\", \"seed\": 43, \"server\": \"cqa1-33015\", \"submitted_at\": \"2026-05-22T05:41:03.001Z\", \"submitted_via\": \"submit_training_job\", \"wall_clock_seconds\": 52416.6}, \"status\": \"DONE\", \"updated_at\": \"2026-05-23T01:38:39.534Z\"}, \"eval_pi05_random_k085_spatial_seed43\": {\"completed_at\": \"2026-05-22T08:38:32.686Z\", \"conclusion\": \"success\", \"created_at\": \"2026-05-22T04:14:58.160Z\", \"hypothesis\": \"π0.5 Random k=0.85 Spatial seed43 验证实验。seed42 数据已有。Random 在 Spatial suite moderate pruning 区域的 seed 稳定性验证。\", \"metrics\": {\"overall_SR\": 0.576, \"per_task\": {\"T0\": 0.82, \"T1\": 0.62, \"T2\": 0.9, \"T3\": 0.08, \"T4\": 0.48, \"T5\": 0.38, \"T6\": 0.38, \"T7\": 0.74, \"T8\": 0.92, \"T9\": 0.44}, \"total_episodes\": 500, \"total_successes\": 288}, \"retry_count\": 0, \"spec\": {\"account\": \"root\", \"backend\": \"tmux\", \"checkpoint_path\": \"N/A-eval-only\", \"checkpoint_source\": \"pi0-fast-pruned-random-k085\", \"command\": \"eval_pi05_pruning_libero.py --prune_mode random --keep_ratio 0.85 --suite libero_spatial --seed 43\", \"data_count\": 500, \"data_path\": \"libero_spatial\", \"eval_data\": \"libero_spatial\", \"gpu\": [\"cuda:1\"], \"gpu_hours\": 4.39, \"log_path\": \"~/runs/importance_margin_vla_compress/eval_pi05_random_k085_spatial_seed43.log\", \"model_name\": \"pi0-fast\", \"pid\": \"486890\", \"seed\": 43, \"server\": \"westd-38929\", \"submitted_at\": \"2026-05-22T04:15:02.433Z\", \"submitted_via\": \"submit_training_job\", \"wall_clock_seconds\": 15810.3}, \"status\": \"DONE\", \"updated_at\": \"2026-05-23T01:38:37.892Z\"}, \"eval_pi05_l2norm_k085_spatial_seed43\": {\"completed_at\": \"2026-05-22T06:40:48.753Z\", \"conclusion\": \"success\", \"created_at\": \"2026-05-22T04:30:48.223Z\", \"hypothesis\": \"π0.5 L2norm k=0.85 Spatial seed43 验证实验。seed42 数据已有。L2norm k=0.85 Spatial 曲线 knee 区域的 seed 稳定性验证。\", \"metrics\": {\"overall_SR\": 0.88, \"per_task\": {\"T0\": 1, \"T1\": 0.92, \"T2\": 1, \"T3\": 0.78, \"T4\": 0.62, \"T5\": 0.84, \"T6\": 0.96, \"T7\": 0.9, \"T8\": 0.96, \"T9\": 0.82}, \"total_episodes\": 500, \"total_successes\": 440}, \"retry_count\": 0, \"spec\": {\"account\": \"root\", \"backend\": \"tmux\", \"checkpoint_path\": \"/root/autodl-tmp/importance_margin_vla_compress/eval_results/pi05_l2norm_k0.85_libero_spatial_seed43.json\", \"command\": \"eval_pi05_pruning_libero.py --prune_mode l2norm --keep_ratio 0.85 --suite libero_spatial --n_episodes 50 --seed 43 --gpu 1\", \"data_count\": 500, \"data_path\": \"libero_spatial\", \"gpu\": [\"cuda:1\"], \"gpu_hours\": 2.04, \"log_path\": \"~/runs/importance_margin_vla_compress/eval_pi05_l2norm_k085_spatial_seed43.log\", \"model_name\": \"pi05_libero_finetuned\", \"pid\": \"9608\", \"seed\": 43, \"server\": \"westd-27271\", \"submitted_at\": \"2026-05-22T04:38:28.724Z\", \"submitted_via\": \"submit_training_job\", \"wall_clock_seconds\": 7340.0}, \"status\": \"DONE\", \"updated_at\": \"2026-05-23T01:38:36.231Z\"}, \"eval_pi05_l2norm_k095_spatial_seed43\": {\"completed_at\": \"2026-05-22T08:05:04.451Z\", \"conclusion\": \"success\", \"created_at\": \"2026-05-22T04:19:56.585Z\", \"hypothesis\": \"π0.5 L2norm k=0.95 Spatial seed43 验证实验。seed42 数据已有。验证 L2norm 在 Spatial suite 高 keep ratio 的 seed 稳定性。\", \"metrics\": {\"overall_SR\": 0.98, \"total_episodes\": 500, \"total_successes\": 490}, \"retry_count\": 0, \"spec\": {\"account\": \"root\", \"backend\": \"tmux\", \"checkpoint_path\": \"N/A (eval only)\", \"checkpoint_source\": \"physical-intelligence/pi0.5\", \"command\": \"python -u eval_pi05_pruning_libero.py --prune_mode l2norm --keep_ratio 0.95 --suite libero_spatial --n_episodes 50 --seed 43 --gpu 2\", \"data_count\": 500, \"data_path\": \"LIBERO-Spatial\", \"eval_data\": \"LIBERO-Spatial 10 tasks x 50 episodes\", \"gpu\": 2, \"gpu_hours\": 3.75, \"log_path\": \"~/runs/importance_margin_vla_compress/eval_pi05_l2norm_k095_spatial_seed43.log\", \"model_name\": \"pi0.5\", \"pid\": 5943, \"seed\": 43, \"server\": \"cqa1-33015\", \"submitted_at\": \"2026-05-22T04:20:14.418Z\", \"submitted_via\": \"submit_training_job\", \"wall_clock_seconds\": 13490.0}, \"status\": \"DONE\", \"updated_at\": \"2026-05-23T01:38:34.379Z\"}, \"eval_pi05_l2norm_k07_long_seed43\": {\"completed_at\": \"2026-05-23T01:37:53.771Z\", \"conclusion\": \"failed\", \"created_at\": \"2026-05-23T00:09:25.953Z\", \"hypothesis\": \"π0.5 L2norm k=0.7 Long seed43: seed42=60.0%，L2norm 曲线关键中点。需要 seed43 交叉验证。L2norm k=0.5 seed42=50.2%, k=0.85 seed42=running(cqa1)。\", \"retry_count\": 0, \"spec\": {\"checkpoint_path\": \"n/a (inference-only eval)\", \"checkpoint_source\": \"pi0.5_pretrained\", \"command\": \"CUDA_VISIBLE_DEVICES=1 python -u eval_pi05_pruning_libero.py --prune_mode l2norm --keep_ratio 0.7 --suite libero_10 --n_episodes 50 --seed 43 --gpu 0\", \"data_count\": 500, \"data_path\": \"libero_10\", \"eval_data\": \"libero_10\", \"gpu\": [\"cuda:1\"], \"log_path\": \"/tmp/eval_l2norm_k07_long_s43.log\", \"model_name\": \"pi0.5\", \"seed\": 43, \"server\": \"westd-38929\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-23T01:37:53.771Z\"}, \"eval_pi05_random_k03_long_seed43\": {\"completed_at\": \"2026-05-23T01:37:50.930Z\", \"conclusion\": \"failed\", \"created_at\": \"2026-05-22T22:57:54.075Z\", \"hypothesis\": \"π0.5 Random k=0.3 Long seed43: seed42=29.0%，极端压缩 floor data point。Random k=0.5 seed42=50.2%。需要 seed43 验证 floor 是否可复现。\", \"retry_count\": 0, \"spec\": {\"account\": \"root\", \"backend\": \"tmux\", \"checkpoint_path\": \"n/a (inference-only eval)\", \"checkpoint_source\": \"pi0.5_pretrained\", \"command\": \"CUDA_VISIBLE_DEVICES=2 python -u eval_pi05_pruning_libero.py --prune_mode random --keep_ratio 0.3 --suite libero_10 --n_episodes 50 --seed 43 --gpu 0\", \"data_count\": 500, \"data_path\": \"libero_10\", \"eval_data\": \"libero_10\", \"gpu\": [\"cuda:2\"], \"gpu_hours\": 2.67, \"log_path\": \"/tmp/eval_random_k03_long_s43.log\", \"model_name\": \"pi0.5\", \"pid\": \"239581\", \"seed\": 43, \"server\": \"westd-38929\", \"submitted_at\": \"2026-05-22T22:57:53.130Z\", \"submitted_via\": \"submit_training_job\", \"wall_clock_seconds\": 9597.8}, \"status\": \"DONE\", \"updated_at\": \"2026-05-23T01:37:50.930Z\"}, \"eval_pi05_l2norm_k085_long_seed43\": {\"completed_at\": \"2026-05-23T01:37:48.060Z\", \"conclusion\": \"failed\", \"created_at\": \"2026-05-23T00:09:31.035Z\", \"hypothesis\": \"π0.5 L2norm k=0.85 Long seed43: L2norm k=0.85 Long seed42 在 cqa1 运行中。seed43 提供 multi-seed 验证。L2norm k=0.7 seed42=60.0%, k=0.95 seed42=已有数据。k=0.85 填充曲线 knee。\", \"retry_count\": 0, \"spec\": {\"checkpoint_path\": \"n/a (inference-only eval)\", \"checkpoint_source\": \"pi0.5_pretrained\", \"command\": \"CUDA_VISIBLE_DEVICES=3 python -u eval_pi05_pruning_libero.py --prune_mode l2norm --keep_ratio 0.85 --suite libero_10 --n_episodes 50 --seed 43 --gpu 0\", \"data_count\": 500, \"data_path\": \"libero_10\", \"eval_data\": \"libero_10\", \"gpu\": [\"cuda:3\"], \"log_path\": \"/tmp/eval_l2norm_k085_long_s43.log\", \"model_name\": \"pi0.5\", \"seed\": 43, \"server\": \"westd-38929\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-23T01:37:48.060Z\"}, \"eval_pi05_random_k095_goal_seed42\": {\"completed_at\": \"2026-05-23T01:37:45.131Z\", \"conclusion\": \"success\", \"created_at\": \"2026-05-22T21:00:15.861Z\", \"hypothesis\": \"π0.5 Random k=0.95 Goal seed42: Object Rnd k=0.95=69.4%, Spatial=76.4%, Long=61.2%。Goal 的 Random k=0.95 sensitivity level? 填补 ROADMAP Goal Rnd k=0.95 缺口。\", \"metrics\": {\"sr\": 0.84, \"total_episodes\": 500, \"total_successes\": 420}, \"retry_count\": 0, \"spec\": {\"checkpoint_path\": \"N/A - eval experiment\", \"checkpoint_source\": \"pi0.5_pretrained\", \"command\": \"CUDA_VISIBLE_DEVICES=1 python -u eval_pi05_pruning_libero.py --prune_mode random --keep_ratio 0.95 --suite libero_goal --n_episodes 50 --seed 42 --gpu 0\", \"data_count\": 500, \"data_path\": \"libero_goal\", \"eval_data\": \"libero_goal\", \"log_path\": \"logs/eval_pi05_random_k095_goal_seed42.log\", \"model_name\": \"pi0.5\", \"seed\": 42, \"server\": \"cqa1-33015\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-23T01:37:45.130Z\"}, \"eval_pi05_l2norm_k03_long_seed42\": {\"checkpoint_path\": \"n/a (inference-only eval)\", \"completed_at\": \"2026-05-23T01:37:39.408Z\", \"conclusion\": \"success\", \"created_at\": \"2026-05-22T22:04:38.176Z\", \"hypothesis\": \"π0.5 L2norm k=0.3 Long seed42: Long L2 k=0.5=🏃, k=0.7=60.0%. k=0.3 是极端压缩的 floor data point。Long suite 最后 L2 缺口。\", \"log_path\": \"/root/autodl-tmp/importance_margin_vla_compress/logs/eval_pi05_l2norm_k03_long_seed42.log\", \"metrics\": {\"sr\": 0.39, \"total_episodes\": 500, \"total_successes\": 195}, \"retry_count\": 0, \"spec\": {\"checkpoint_source\": \"/root/autodl-tmp/pi05_libero_finetuned\", \"command\": \"CUDA_VISIBLE_DEVICES=0 python -u eval_pi05_pruning_libero.py --prune_mode l2norm --keep_ratio 0.3 --suite libero_10 --n_episodes 50 --seed 42 --gpu 0\", \"data_count\": 500, \"data_path\": \"libero_10\", \"eval_data\": \"libero_10\", \"model_name\": \"pi05_libero_finetuned\", \"seed\": 42, \"server\": \"westd-27271\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-23T01:37:39.408Z\"}, \"eval_xvla_random_k095_object_seed42_v2\": {\"completed_at\": \"2026-05-23T00:08:58.020Z\", \"conclusion\": \"success\", \"created_at\": \"2026-05-22T23:09:50.683Z\", \"hypothesis\": \"X-VLA Random k=0.95 Object seed42 v2: 重部署。v1 在 westd-27271 启动即崩溃（transformers 5.5.4 与 Florence2 _tied_weights_keys 不兼容，已修复）。fig_method_gap 必需数据。L2norm k=0.95=97.6%, 预期 Random 也接近 → 确认 method-independence (Claim 3)。\", \"metrics\": {\"elapsed_seconds\": 2068.5, \"success_rate\": 0.988, \"total_episodes\": 500, \"total_successes\": 494}, \"retry_count\": 0, \"spec\": {\"checkpoint_path\": \"n/a (inference-only eval)\", \"command\": \"python -u eval_xvla_pruning_libero.py --mode random --keep_ratio 0.95 --suite libero_object --num_episodes 50 --seed 42 --model_path /root/autodl-tmp/X-VLA-Libero --gpu 0\", \"data_count\": 50, \"data_path\": \"/root/autodl-tmp/X-VLA-Libero\", \"log_path\": \"/root/autodl-tmp/importance_margin_vla_compress/eval_results/xvla_prune_k0.95_libero_object.json\", \"model_name\": \"X-VLA\", \"seed\": 42, \"server\": \"westd-27271\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-23T00:08:58.020Z\"}, \"eval_pi05_random_k03_long_seed42\": {\"completed_at\": \"2026-05-23T00:08:52.554Z\", \"conclusion\": \"success\", \"created_at\": \"2026-05-22T20:35:23.898Z\", \"hypothesis\": \"π0.5 Random k=0.3 on LIBERO-Long: extreme 70% random token removal on 520-step horizon. Object Random k=0.3=8.2%. Expecting severe degradation — floor data point for Long random curve.\", \"metrics\": {\"elapsed_min\": 171, \"success_rate\": 0.29, \"total_episodes\": 500, \"total_successes\": 145}, \"retry_count\": 0, \"spec\": {\"checkpoint_path\": \"n/a (inference-only eval)\", \"checkpoint_source\": \"/root/autodl-tmp/pi05_libero_finetuned\", \"command\": \"CUDA_VISIBLE_DEVICES=1 TRANSFORMERS_OFFLINE=1 HF_HOME=/root/autodl-tmp/.hf_cache python -u eval_pi05_pruning_libero.py --prune_mode random --keep_ratio 0.3 --suite libero_10 --n_episodes 50 --seed 42 --gpu 0\", \"data_count\": 500, \"data_path\": \"/root/autodl-tmp/pi05_libero_finetuned\", \"eval_data\": \"libero_10\", \"log_path\": \"/root/autodl-tmp/importance_margin_vla_compress/eval_results/pi05_random_k0.30_libero_10_seed42.json\", \"model_name\": \"pi05\", \"seed\": 42, \"server\": \"westd-38929\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-23T00:08:52.554Z\"}, \"eval_pi05_attention_k07_object_seed42\": {\"completed_at\": \"2026-05-22T20:07:40.094Z\", \"conclusion\": \"negative\", \"created_at\": \"2026-05-22T20:06:57.110Z\", \"hypothesis\": \"π0.5 Attention k=0.7 Object seed42: attention-based pruning 30% token removal on Object suite. Testing attention scoring as importance metric vs random/l2norm.\", \"metrics\": {\"elapsed_min\": 117.26, \"keep_ratio\": 0.7, \"prune_mode\": \"attention\", \"seed\": 42, \"success_rate\": 0.006, \"suite\": \"libero_object\", \"total_episodes\": 500, \"total_successes\": 3}, \"retry_count\": 0, \"spec\": {\"checkpoint_path\": \"/root/autodl-tmp/pi05_libero_finetuned\", \"checkpoint_source\": \"/root/autodl-tmp/pi05_libero_finetuned\", \"command\": \"python -u eval_pi05_pruning_libero.py --prune_mode attention --keep_ratio 0.7 --suite libero_object --n_episodes 50 --seed 42 --gpu 0\", \"data_count\": 500, \"data_path\": \"libero_object\", \"eval_data\": \"libero_object\", \"log_path\": \"/root/autodl-tmp/importance_margin_vla_compress/logs/pi05_attention_k07_object_s42.log\", \"model_name\": \"pi05\", \"seed\": 42, \"server\": \"westd-41074\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-22T22:27:28.482Z\"}, \"eval_smolvla_baseline_spatial_seed42_cqa1\": {\"checkpoint_path\": \"n/a\", \"completed_at\": \"2026-05-22T22:24:50.893Z\", \"conclusion\": \"failed\", \"created_at\": \"2026-05-22T20:51:11.601Z\", \"failure_reason\": \"HFValidationError — 环境问题导致模型加载失败\", \"hypothesis\": \"SmolVLA baseline (no pruning) on LIBERO-Spatial on cqa1: establishing authoritative per-suite baseline. Object baseline=83.6%. Cross-suite baseline needed for paper.\", \"log_path\": \"logs/smolvla_baseline_spatial_s42.log\", \"retry_count\": 0, \"spec\": {\"checkpoint_source\": \"/root/autodl-tmp/.hf_cache/smolvla_libero_official\", \"command\": \"CUDA_VISIBLE_DEVICES=1 python -u eval_official_libero.py --mode baseline --suite libero_spatial --num_episodes 50 --gpu 0 --seed 42 --pretrained_dir /root/autodl-tmp/.hf_cache/smolvla_libero_official\", \"data_count\": 500, \"data_path\": \"libero_spatial\", \"eval_data\": \"libero_spatial\", \"log_path\": \"logs/smolvla_baseline_spatial_s42.log\", \"model_name\": \"SmolVLA\", \"seed\": 42, \"server\": \"cqa1-33015\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-22T22:24:53.693Z\"}, \"eval_xvla_random_k07_goal_seed42\": {\"checkpoint_path\": \"n/a (inference-only eval)\", \"completed_at\": \"2026-05-22T22:24:45.435Z\", \"conclusion\": \"negative\", \"created_at\": \"2026-05-22T20:36:28.618Z\", \"hypothesis\": \"X-VLA Random k=0.7 on LIBERO-Goal: 30% random removal. Aggressive pruning data point for Goal random curve. Chained after k=0.9 Goal on cuda:0.\", \"log_path\": \"logs/eval_xvla_random_k07_goal_seed42.log\", \"metrics\": {\"overall_SR\": 0.572, \"total_episodes\": 500, \"total_successes\": 286}, \"retry_count\": 0, \"status\": \"DONE\", \"updated_at\": \"2026-05-22T22:24:45.435Z\"}, \"eval_pi05_random_k09_long_seed42\": {\"checkpoint_path\": \"n/a (inference-only eval)\", \"completed_at\": \"2026-05-22T22:24:42.592Z\", \"conclusion\": \"negative\", \"created_at\": \"2026-05-22T21:13:15.386Z\", \"hypothesis\": \"π0.5 Random k=0.9 Long seed42: Long suite 对 random pruning 最敏感，k=0.95=61.2%。k=0.9 移除更多 token 的影响。\", \"log_path\": \"logs/eval_pi05_random_k09_long_seed42.log\", \"metrics\": {\"overall_SR\": 0.318, \"total_episodes\": 500, \"total_successes\": 159}, \"retry_count\": 0, \"spec\": {\"command\": \"eval_pi05_pruning_libero.py --prune_mode random --keep_ratio 0.9 --suite libero_10 --n_episodes 50 --seed 42 --gpu 0\", \"data_count\": 500, \"data_path\": \"libero_10\", \"gpu\": \"cuda:0\", \"model_name\": \"pi0.5\", \"pid\": 989045, \"seed\": 42, \"server\": \"westd-38929\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-22T22:24:42.592Z\"}, \"eval_pi05_random_k085_long_seed42\": {\"checkpoint_path\": \"n/a (inference-only eval)\", \"completed_at\": \"2026-05-22T22:24:38.597Z\", \"conclusion\": \"negative\", \"created_at\": \"2026-05-22T19:10:48.164Z\", \"hypothesis\": \"π0.5 Random k=0.85 on LIBERO-Long: 15% random removal on 520-step tasks. Filling Long Random degradation curve.\", \"log_path\": \"logs/eval_pi05_random_k085_long_seed42.log\", \"metrics\": {\"overall_SR\": 0.444, \"total_episodes\": 500, \"total_successes\": 222}, \"retry_count\": 0, \"spec\": {\"checkpoint_source\": \"pi0.5_pretrained\", \"command\": \"CUDA_VISIBLE_DEVICES=0 TRANSFORMERS_OFFLINE=1 HF_HOME=/root/autodl-tmp/.hf_cache python -u eval_pi05_pruning_libero.py --prune_mode random --keep_ratio 0.85 --suite libero_10 --n_episodes 50 --seed 42 --gpu 0\", \"data_count\": 500, \"data_path\": \"libero_10\", \"eval_data\": \"libero_10\", \"model_name\": \"pi0.5\", \"seed\": 42, \"server\": \"westd-41074\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-22T22:24:38.597Z\"}, \"eval_pi05_l2norm_k09_long_seed42\": {\"completed_at\": \"2026-05-22T20:34:59.738Z\", \"conclusion\": \"success\", \"created_at\": \"2026-05-22T15:56:35.737Z\", \"hypothesis\": \"π0.5 L2norm k=0.9 Long seed42: 10% L2norm token removal on 520-step horizon. L2norm outperforms Random at same k on Object/Spatial. Testing if same advantage holds on Long tasks.\", \"metrics\": {\"overall_SR\": 0.81, \"total_episodes\": 500, \"total_successes\": 405}, \"result_notes\": \"L2Norm k=0.9 Long (libero_10): overall_sr=81.0% (405/500). Per-task: T0=96%, T1=100%, T2=88%, T3=100%, T4=92%, T5=96%, T6=10%, T7=84%, T8=46%, T9=98%. T6 (white mug + pudding) is the weak point at 10%. Elapsed: 132.5min.\", \"retry_count\": 0, \"spec\": {\"checkpoint_path\": \"n/a (inference-only eval)\", \"command\": \"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/importance_margin_vla_compress && CUDA_VISIBLE_DEVICES=1 TRANSFORMERS_OFFLINE=1 HF_HOME=/root/autodl-tmp/.hf_cache python eval_pi05_pruning_libero.py --prune_mode l2norm --keep_ratio 0.9 --suite libero_10 --n_episodes 50 --seed 42 --gpu 0\", \"data_count\": 500, \"data_path\": \"/root/autodl-tmp/importance_margin_vla_compress\", \"log_path\": \"/root/autodl-tmp/importance_margin_vla_compress/eval_results/pi05_l2norm_k0.90_libero_10_seed42.json\", \"model_name\": \"pi0.5\", \"seed\": 42, \"server\": \"westd-41074\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-22T22:24:13.177Z\"}, \"eval_pi05_random_k07_long_seed42\": {\"completed_at\": \"2026-05-22T21:54:17.624Z\", \"conclusion\": \"success\", \"created_at\": \"2026-05-22T19:10:50.961Z\", \"hypothesis\": \"π0.5 Random k=0.7 on LIBERO-Long: 30% random removal on long-horizon tasks. Aggressive random pruning data point.\", \"metrics\": {\"elapsed_min\": 156.4, \"overall_sr\": 0.646, \"total_episodes\": 500, \"total_successes\": 323}, \"retry_count\": 0, \"spec\": {\"checkpoint_path\": \"n/a (inference-only eval)\", \"checkpoint_source\": \"pi0.5_pretrained\", \"command\": \"CUDA_VISIBLE_DEVICES=1 TRANSFORMERS_OFFLINE=1 HF_HOME=/root/autodl-tmp/.hf_cache python -u eval_pi05_pruning_libero.py --prune_mode random --keep_ratio 0.7 --suite libero_10 --n_episodes 50 --seed 42 --gpu 0\", \"data_count\": 500, \"data_path\": \"libero_10\", \"eval_data\": \"libero_10\", \"log_path\": \"/root/autodl-tmp/importance_margin_vla_compress/eval_results/pi05_random_k0.70_libero_10_seed42.json\", \"model_name\": \"pi0.5\", \"seed\": 42, \"server\": \"westd-41074\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-22T21:54:17.624Z\"}, \"eval_xvla_random_k09_spatial_seed42\": {\"completed_at\": \"2026-05-22T21:12:50.578Z\", \"conclusion\": \"negative\", \"created_at\": \"2026-05-22T20:36:26.783Z\", \"hypothesis\": \"X-VLA Random k=0.9 Spatial: k=0.95=70.2%。k=0.9 移除 5/50 tokens。\", \"metrics\": {\"overall_SR\": 0.778, \"total_episodes\": 500, \"total_successes\": 389}, \"retry_count\": 0, \"spec\": {\"checkpoint_path\": \"/root/autodl-tmp/importance_margin_vla_compress/eval_results/xvla_random_k0.9_libero_spatial_seed42.json\", \"command\": \"CUDA_VISIBLE_DEVICES=1 python -u eval_xvla_pruning_libero.py --mode random --keep_ratio 0.9 --suite libero_spatial --num_episodes 50 --seed 42 --gpu 0 --model_path /root/autodl-tmp/X-VLA-Libero\", \"data_count\": 500, \"data_path\": \"libero_spatial\", \"log_path\": \"/root/autodl-tmp/importance_margin_vla_compress/logs/xvla_random_k09_spatial.log\", \"model_name\": \"X-VLA\", \"seed\": 42, \"server\": \"westd-27271\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-22T21:12:50.578Z\"}, \"eval_xvla_random_k09_goal_seed42\": {\"completed_at\": \"2026-05-22T21:12:47.838Z\", \"conclusion\": \"negative\", \"created_at\": \"2026-05-22T20:36:22.144Z\", \"hypothesis\": \"X-VLA Random k=0.9 Goal: k=0.95=54.0%。k=0.9 移除 5/50 tokens，预期进一步下降。\", \"metrics\": {\"overall_SR\": 0.706, \"total_episodes\": 500, \"total_successes\": 353}, \"retry_count\": 0, \"spec\": {\"checkpoint_path\": \"/root/autodl-tmp/importance_margin_vla_compress/eval_results/xvla_random_k0.9_libero_goal_seed42.json\", \"command\": \"CUDA_VISIBLE_DEVICES=0 python -u eval_xvla_pruning_libero.py --mode random --keep_ratio 0.9 --suite libero_goal --num_episodes 50 --seed 42 --gpu 0 --model_path /root/autodl-tmp/X-VLA-Libero\", \"data_count\": 500, \"data_path\": \"libero_goal\", \"log_path\": \"/root/autodl-tmp/importance_margin_vla_compress/logs/xvla_random_k09_goal.log\", \"model_name\": \"X-VLA\", \"seed\": 42, \"server\": \"westd-27271\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-22T21:12:47.838Z\"}, \"eval_xvla_random_k095_spatial_seed42\": {\"checkpoint_path\": \"/root/autodl-tmp/importance_margin_vla_compress/eval_results/xvla_prune_k0.95_libero_spatial.json\", \"completed_at\": \"2026-05-22T20:10:23.417Z\", \"conclusion\": \"negative\", \"created_at\": \"2026-05-22T18:46:35.052Z\", \"hypothesis\": \"X-VLA Random k=0.95 Spatial: baseline=93.0%。检验 50-token BART connector 在 Spatial 上对 random pruning 的敏感度。\", \"log_path\": \"/root/autodl-tmp/importance_margin_vla_compress/logs/xvla_random_k095_spatial.log\", \"metrics\": {\"overall_SR\": 0.702, \"total_episodes\": 500, \"total_successes\": 351}, \"retry_count\": 0, \"spec\": {\"checkpoint_source\": \"2toINF/X-VLA-Libero\", \"command\": \"python -u eval_xvla_pruning_libero.py --suite libero_spatial --keep_ratio 0.95 --mode random --seed 42 --num_episodes 50 --gpu 0\", \"data_count\": 50, \"data_path\": \"libero_spatial\", \"eval_data\": \"libero_spatial\", \"model_name\": \"X-VLA-Libero\", \"seed\": 42, \"server\": \"westd-27271\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-22T21:12:39.654Z\"}, \"eval_xvla_random_k095_goal_seed42\": {\"checkpoint_path\": \"/root/autodl-tmp/importance_margin_vla_compress/eval_results/xvla_prune_k0.95_libero_goal.json\", \"completed_at\": \"2026-05-22T20:10:20.685Z\", \"conclusion\": \"negative\", \"created_at\": \"2026-05-22T18:46:33.526Z\", \"hypothesis\": \"X-VLA Random k=0.95 Goal: 仅移除 2.5/50 tokens 的 random pruning 对 Goal 的影响。baseline=98.4%。50 tokens 的 BART connector 对 random removal 极度敏感。\", \"log_path\": \"/root/autodl-tmp/importance_margin_vla_compress/logs/xvla_random_k095_goal.log\", \"metrics\": {\"overall_SR\": 0.54, \"total_episodes\": 500, \"total_successes\": 270}, \"retry_count\": 0, \"spec\": {\"checkpoint_source\": \"2toINF/X-VLA-Libero\", \"command\": \"python -u eval_xvla_pruning_libero.py --suite libero_goal --keep_ratio 0.95 --mode random --seed 42 --num_episodes 50 --gpu 0\", \"data_count\": 50, \"data_path\": \"libero_goal\", \"eval_data\": \"libero_goal\", \"model_name\": \"X-VLA-Libero\", \"seed\": 42, \"server\": \"westd-27271\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-22T21:12:38.023Z\"}, \"eval_openvla_baseline_spatial_seed42\": {\"completed_at\": \"2026-05-22T21:01:37.395Z\", \"conclusion\": \"failed\", \"created_at\": \"2026-05-22T21:00:18.539Z\", \"failure_reason\": \"环境问题：spatial-finetuned 模型在 cqa1 上全部 task 0% SR，非实验结论\", \"hypothesis\": \"OpenVLA baseline Spatial seed42: 验证 OpenVLA spatial-finetuned 模型在 LIBERO-Spatial 上的 baseline SR，作为后续 pruning 实验对照。\", \"retry_count\": 0, \"spec\": {\"checkpoint_path\": \"N/A - eval experiment\", \"checkpoint_source\": \"openvla-libero-spatial\", \"command\": \"CUDA_VISIBLE_DEVICES=0 python -u eval_openvla_pruning_libero.py --model_path /root/autodl-tmp/openvla-libero-spatial --suite libero_spatial --keep_ratio 1.0 --num_episodes 50 --seed 42 --gpu 0\", \"data_count\": 500, \"data_path\": \"libero_spatial\", \"eval_data\": \"libero_spatial\", \"log_path\": \"logs/openvla_baseline_spatial_s42.log\", \"model_name\": \"openvla\", \"seed\": 42, \"server\": \"cqa1-33015\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-22T21:01:37.395Z\"}, \"eval_pi05_l2norm_k095_spatial_seed42\": {\"checkpoint_path\": \"N/A (eval only)\", \"completed_at\": \"2026-05-22T03:19:41.642Z\", \"conclusion\": \"success\", \"created_at\": \"2026-05-22T01:58:53.983Z\", \"extra\": {\"hook_events\": [{\"action\": \"agent\", \"event\": \"on_failed\", \"ts\": \"2026-05-22T01:59:15.682522+00:00\"}]}, \"failure_reason\": \"process dead 5× with no sentinel/W&B — auto-resolved as failed\", \"hypothesis\": \"π0.5 L2norm k=0.95 Spatial seed42: L2norm 在 cliff zone 外应保持 plateau。Object k=0.95=98.2%，验证 Spatial 同样免疫。\", \"log_path\": \"/root/runs/importance_margin_vla_compress/eval_pi05_l2norm_k095_spatial_seed42.log\", \"metrics\": {\"seed\": 42, \"success_rate\": 0.978, \"suite\": \"libero_spatial\"}, \"reproduce\": {\"finished_at\": \"2026-05-22T01:59:00.130Z\"}, \"retry_count\": 0, \"spec\": {\"account\": \"root\", \"backend\": \"tmux\", \"checkpoint_path\": \"N/A\", \"checkpoint_source\": \"physical-intelligence/pi0.5\", \"command\": \"HF_HUB_OFFLINE=1 MUJOCO_GL=egl python -u eval_pi05_pruning_libero.py --prune_mode l2norm --keep_ratio 0.95 --suite libero_spatial --n_episodes 50 --seed 42 --gpu 0\", \"data_count\": 500, \"data_path\": \"LIBERO-Spatial\", \"eval_data\": \"LIBERO-Spatial 500 episodes\", \"gpu\": \"cuda:1\", \"gpu_hours\": 1.03, \"log_path\": \"~/runs/importance_margin_vla_compress/eval_pi05_l2norm_k095_spatial_seed42.log\", \"model_name\": \"pi0.5\", \"pid\": 260899, \"seed\": 42, \"server\": \"westd-38929\", \"submitted_at\": \"2026-05-22T02:17:41.504Z\", \"submitted_via\": \"submit_training_job\", \"wall_clock_seconds\": 3720.1}, \"status\": \"DONE\", \"updated_at\": \"2026-05-22T20:52:07.658Z\"}, \"eval_pi05_random_k0925_object_seed43\": {\"checkpoint_path\": \"/root/autodl-tmp/importance_margin_vla_compress/eval_results/pi05_random_k0.93_libero_object_seed43.json\", \"completed_at\": \"2026-05-22T02:41:30.566Z\", \"conclusion\": \"success\", \"created_at\": \"2026-05-22T00:07:09.764Z\", \"extra\": {\"hook_events\": [{\"action\": \"agent\", \"event\": \"on_complete\", \"ts\": \"2026-05-22T01:49:02.912126+00:00\"}]}, \"hypothesis\": \"π0.5 random k=0.925 Object seed43: cliff 入口双种子验证。seed42=27.6%，验证 cliff 入口点的跨 seed 一致性。\", \"metrics\": {\"seed\": 43, \"success_rate\": 0.3, \"suite\": \"libero_object\"}, \"parent\": \"eval_pi05_random_k0925_object_seed42\", \"reproduce\": {\"finished_at\": \"2026-05-22T01:48:47.427Z\"}, \"retry_count\": 0, \"spec\": {\"account\": \"root\", \"backend\": \"tmux\", \"checkpoint_source\": \"/root/autodl-tmp/pi05_libero_finetuned\", \"command\": \"eval_pi05_pruning_libero.py --prune_mode random --keep_ratio 0.925 --suite libero_object --n_episodes 50 --seed 43\", \"data_count\": 500, \"data_path\": \"libero_object\", \"eval_data\": \"libero_object\", \"gpu\": [\"cuda:2\"], \"gpu_hours\": 2.57, \"log_path\": \"~/runs/importance_margin_vla_compress/eval_pi05_random_k0925_object_seed43.log\", \"model_name\": \"pi05_libero_finetuned\", \"pid\": \"68029\", \"seed\": 43, \"server\": \"westd-38929\", \"submitted_at\": \"2026-05-22T00:07:20.338Z\", \"submitted_via\": \"submit_training_job\", \"wall_clock_seconds\": 9250.2}, \"status\": \"DONE\", \"updated_at\": \"2026-05-22T20:51:20.865Z\"}, \"eval_smolvla_baseline_spatial_seed42\": {\"conclusion\": \"failed\", \"created_at\": \"2026-05-21T01:15:01.901Z\", \"hypothesis\": \"SmolVLA baseline (no pruning) on LIBERO-Spatial: establishing per-suite baseline. Object baseline=83.6%. Spatial may differ due to task complexity.\", \"metrics\": {\"failure_reason\": \"Ghost process: no GPU assigned, PID 224849 likely dead after westd-38929 GPUs reassigned to OpenVLA experiments\"}, \"notes\": \"westd-38929 OffScreenRenderEnv — data not comparable with cqa1 LiberoEnv results. cqa1 data is authoritative (baseline=43.8%, k=0.5=0.6%).\", \"retry_count\": 0, \"spec\": {\"checkpoint_path\": \"/root/autodl-tmp/.hf_cache/smolvla_libero_official/model.safetensors\", \"checkpoint_source\": \"/root/autodl-tmp/.hf_cache/smolvla_libero_official/\", \"command\": \"CUDA_VISIBLE_DEVICES=2 MUJOCO_GL=egl python -u eval_official_libero.py --pretrained_dir /root/autodl-tmp/.hf_cache/smolvla_libero_official/ --suite libero_spatial --mode baseline --num_episodes 50 --seed 42 --gpu 0 --output eval_results/smolvla_baseline_spatial_seed42.json\", \"data_count\": \"10 tasks x 50 episodes = 500 total episodes\", \"data_path\": \"/root/autodl-tmp/LIBERO-plus/libero/libero/bddl_files/libero_spatial/\", \"eval_data\": \"LIBERO-Spatial (10 standard base tasks, 280 max steps each)\", \"gpu_id\": 2, \"log_path\": \"/root/autodl-tmp/importance_margin_vla_compress/logs/smolvla_baseline_spatial_seed42.log\", \"model_name\": \"SmolVLA (SmolVLM2-500M-Instruct + expert policy head)\", \"pid\": 224849, \"seed\": 42, \"server\": \"westd-38929\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-22T20:50:56.964Z\"}, \"eval_pi05_l2norm_k085_long_seed42\": {\"checkpoint_path\": \"/root/autodl-tmp/pi05_libero_finetuned\", \"completed_at\": \"2026-05-22T20:34:14.301Z\", \"conclusion\": \"success\", \"created_at\": \"2026-05-22T16:35:52.945Z\", \"hypothesis\": \"π0.5 L2norm k=0.85 on LIBERO-Long (libero_10): 15% token removal on 520-step horizon tasks. Object k=0.85=98.0%. Testing if Long suite shows similar resilience or begins to degrade.\", \"log_path\": \"eval_results/pi05_l2norm_k0.85_libero_10_seed42.json\", \"metrics\": {\"elapsed_min\": 133.4, \"keep_ratio\": 0.85, \"num_episodes\": 500, \"num_success\": 390, \"prune_mode\": \"l2norm\", \"seed\": 42, \"success_rate\": 0.78, \"suite\": \"libero_10\"}, \"retry_count\": 0, \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=0 TRANSFORMERS_OFFLINE=1 HF_HOME=/root/autodl-tmp/.hf_cache python eval_pi05_pruning_libero.py --prune_mode l2norm --keep_ratio 0.85 --suite libero_10 --n_episodes 50 --seed 42 --gpu 0\", \"data_count\": 500, \"data_path\": \"/root/autodl-tmp/importance_margin_vla_compress\", \"model_name\": \"pi0.5\", \"seed\": 42, \"server\": \"westd-38929\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-22T20:34:14.301Z\"}, \"eval_pi05_random_k095_long_seed42\": {\"checkpoint_path\": \"/root/autodl-tmp/pi05_libero_finetuned\", \"completed_at\": \"2026-05-22T20:34:11.241Z\", \"conclusion\": \"success\", \"created_at\": \"2026-05-22T16:35:54.626Z\", \"hypothesis\": \"π0.5 Random k=0.95 on LIBERO-Long (libero_10): Random baseline for Long suite. Object Random k=0.95=97.6%. Establishing random pruning reference for long-horizon tasks.\", \"log_path\": \"eval_results/pi05_random_k0.95_libero_10_seed42.json\", \"metrics\": {\"elapsed_min\": 157.6, \"keep_ratio\": 0.95, \"num_episodes\": 500, \"num_success\": 306, \"prune_mode\": \"random\", \"seed\": 42, \"success_rate\": 0.612, \"suite\": \"libero_10\"}, \"retry_count\": 0, \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=3 TRANSFORMERS_OFFLINE=1 HF_HOME=/root/autodl-tmp/.hf_cache python eval_pi05_pruning_libero.py --prune_mode random --keep_ratio 0.95 --suite libero_10 --n_episodes 50 --seed 42 --gpu 0\", \"data_count\": 500, \"data_path\": \"/root/autodl-tmp/importance_margin_vla_compress\", \"model_name\": \"pi0.5\", \"seed\": 42, \"server\": \"westd-38929\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-22T20:34:11.241Z\"}, \"eval_pi05_random_k085_goal_seed42_v3\": {\"checkpoint_path\": \"/root/autodl-tmp/pi05_libero_finetuned\", \"completed_at\": \"2026-05-22T20:34:07.958Z\", \"conclusion\": \"success\", \"created_at\": \"2026-05-22T18:48:35.710Z\", \"hypothesis\": \"π0.5 Random k=0.85 on LIBERO-Goal: Goal Random k=0.9=62.6%. Testing if 15% removal causes further drop or stabilizes. Cliff sweep data point.\", \"log_path\": \"eval_results/pi05_random_k0.85_libero_goal_seed42.json\", \"metrics\": {\"num_episodes\": 500, \"num_success\": 262, \"seed\": 42, \"success_rate\": 0.524, \"suite\": \"libero_goal\"}, \"retry_count\": 0, \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=2 TRANSFORMERS_OFFLINE=1 HF_HOME=/root/autodl-tmp/.hf_cache python -u eval_pi05_pruning_libero.py --prune_mode random --keep_ratio 0.85 --suite libero_goal --n_episodes 50 --seed 42 --gpu 0\", \"data_count\": 500, \"data_path\": \"libero_goal\", \"model_name\": \"pi0.5\", \"seed\": 42, \"server\": \"westd-38929\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-22T20:34:07.958Z\"}, \"eval_pi05_l2norm_k07_long_seed42\": {\"checkpoint_path\": \"/root/autodl-tmp/pi05_libero_finetuned\", \"completed_at\": \"2026-05-22T20:34:03.285Z\", \"conclusion\": \"success\", \"created_at\": \"2026-05-22T17:45:34.517Z\", \"hypothesis\": \"π0.5 L2norm k=0.7 on LIBERO-Long: 30% token removal on 520-step horizon. Object k=0.7=97.2%. Testing if Long tasks show more degradation with aggressive pruning.\", \"log_path\": \"eval_results/pi05_l2norm_k0.70_libero_10_seed42.json\", \"metrics\": {\"elapsed_min\": 152.3, \"keep_ratio\": 0.7, \"num_episodes\": 500, \"num_success\": 300, \"prune_mode\": \"l2norm\", \"seed\": 42, \"success_rate\": 0.6, \"suite\": \"libero_10\"}, \"retry_count\": 0, \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=1 TRANSFORMERS_OFFLINE=1 HF_HOME=/root/autodl-tmp/.hf_cache python eval_pi05_pruning_libero.py --prune_mode l2norm --keep_ratio 0.7 --suite libero_10 --n_episodes 50 --seed 42 --gpu 0\", \"data_count\": 500, \"data_path\": \"libero_10\", \"model_name\": \"pi0.5\", \"seed\": 42, \"server\": \"westd-38929\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-22T20:34:03.285Z\"}, \"eval_pi05_l2norm_k0925_spatial_seed43\": {\"checkpoint_path\": \"N/A - eval experiment\", \"completed_at\": \"2026-05-22T20:14:42.766Z\", \"conclusion\": \"negative\", \"created_at\": \"2026-05-22T05:05:09.169Z\", \"failure_reason\": \"stale RUNNING, no metrics after 14h\", \"hypothesis\": \"π0.5 L2norm k=0.925 Spatial seed43: cliff 入口处 L2norm 双种子验证。Object k=0.925 L2norm=99.2%。seed42 待收割。验证 L2norm 在 cliff zone 保持 plateau 的跨 seed 一致性。\", \"log_path\": \"~/runs/importance_margin_vla_compress/eval_pi05_l2norm_k0925_spatial_seed43.log\", \"retry_count\": 0, \"spec\": {\"account\": \"root\", \"backend\": \"tmux\", \"checkpoint_source\": \"pi0-fast-pruned-l2norm-k0925\", \"command\": \"eval_pi05_pruning_libero.py --prune_mode l2norm --keep_ratio 0.925 --suite libero_spatial --seed 43\", \"data_count\": 500, \"data_path\": \"libero_spatial\", \"eval_data\": \"libero_spatial\", \"gpu\": [\"cuda:1\"], \"gpu_hours\": 15.16, \"log_path\": \"~/runs/importance_margin_vla_compress/eval_pi05_l2norm_k0925_spatial_seed43.log\", \"model_name\": \"pi0-fast\", \"pid\": \"133112\", \"seed\": 43, \"server\": \"cqa1-33015\", \"submitted_at\": \"2026-05-22T05:05:16.877Z\", \"submitted_via\": \"submit_training_job\", \"wall_clock_seconds\": 54565.9}, \"status\": \"DONE\", \"updated_at\": \"2026-05-22T20:14:42.766Z\"}, \"eval_pi05_l2norm_k09_object_seed43\": {\"checkpoint_path\": \"N/A - eval experiment\", \"completed_at\": \"2026-05-22T20:14:36.241Z\", \"conclusion\": \"negative\", \"created_at\": \"2026-05-22T08:36:01.447Z\", \"failure_reason\": \"stale RUNNING, no metrics after 11h\", \"hypothesis\": \"π0.5 L2norm k=0.9 Object seed43: 双种子验证。seed42 Object l2norm k=0.9 未测。Spatial seed42=95.6%, seed43=95.6%。预期 Object 在 plateau ~90-98%。\", \"log_path\": \"N/A - stale\", \"retry_count\": 0, \"spec\": {\"checkpoint_source\": \"pi0-fast-pruned-l2norm-k09\", \"command\": \"eval_pi05_pruning_libero.py --prune_mode l2norm --keep_ratio 0.9 --suite libero_object --seed 43\", \"data_count\": 500, \"data_path\": \"libero_object\", \"eval_data\": \"libero_object\", \"model_name\": \"pi0-fast\", \"seed\": 43, \"server\": \"cqa1-33015\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-22T20:14:36.241Z\"}, \"eval_pi05_l2norm_k095_object_seed43_v2\": {\"checkpoint_path\": \"N/A - eval experiment\", \"completed_at\": \"2026-05-22T20:14:33.634Z\", \"conclusion\": \"negative\", \"created_at\": \"2026-05-22T09:23:21.773Z\", \"failure_reason\": \"stale RUNNING, no metrics after 10h\", \"hypothesis\": \"L2norm pruning at k=0.95 on pi0.5 retains most important vision tokens for libero_object tasks, maintaining performance close to unpruned baseline while removing 5% of tokens. Re-run of killed experiment.\", \"log_path\": \"N/A - stale\", \"retry_count\": 0, \"spec\": {\"checkpoint_source\": \"/root/autodl-tmp/pi05_libero_finetuned\", \"command\": \"CUDA_VISIBLE_DEVICES=1 python -u eval_pi05_pruning_libero.py --prune_mode l2norm --keep_ratio 0.95 --suite libero_object --n_episodes 500 --seed 43 --gpu 0\", \"data_count\": 500, \"data_path\": \"/root/autodl-tmp/importance_margin_vla_compress\", \"eval_data\": \"libero_object\", \"model_name\": \"pi05_libero_finetuned\", \"seed\": 43, \"server\": \"westd-27271\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-22T20:14:33.634Z\"}, \"eval_pi05_l2norm_k0925_object_seed43_v2\": {\"checkpoint_path\": \"N/A - eval experiment\", \"completed_at\": \"2026-05-22T20:14:31.007Z\", \"conclusion\": \"negative\", \"created_at\": \"2026-05-22T09:36:53.576Z\", \"failure_reason\": \"stale RUNNING, no metrics after 10h\", \"hypothesis\": \"π0.5 L2norm k=0.925 Object seed43 v2: 重新部署。seed42=99.2%。L2norm 在 cliff zone 完全免疫的双种子验证。\", \"log_path\": \"N/A - stale\", \"parent\": \"eval_pi05_l2norm_k0925_object_seed42\", \"retry_count\": 0, \"spec\": {\"checkpoint_source\": \"eval_pi05_l2norm_k0925_object_seed42\", \"command\": \"CUDA_VISIBLE_DEVICES=0 python -u eval_pi05_pruning_libero.py --prune_mode l2norm --keep_ratio 0.925 --suite libero_object --n_episodes 500 --seed 43 --gpu 0\", \"data_count\": 500, \"data_path\": \"libero_object\", \"eval_data\": \"libero_object\", \"gpu\": 0, \"model_name\": \"pi05_libero_finetuned\", \"pid\": 327105, \"seed\": 43, \"server\": \"westd-27271\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-22T20:14:31.007Z\"}, \"eval_pi05_l2norm_k095_long_seed42\": {\"checkpoint_path\": \"N/A - eval experiment\", \"completed_at\": \"2026-05-22T20:14:28.420Z\", \"conclusion\": \"negative\", \"created_at\": \"2026-05-22T10:56:36.809Z\", \"failure_reason\": \"stale RUNNING, no metrics after 8h\", \"hypothesis\": \"π0.5 L2norm k=0.95 LIBERO-Long seed42: Phase 2 cliff zone sweep。L2norm 在 Object/Spatial 上 k=0.95 均接近 baseline。如果 Long 也接近 baseline → L2norm 跨 4 suite 一致免疫 cliff。\", \"log_path\": \"N/A - stale\", \"retry_count\": 0, \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=0 HF_HOME=/root/autodl-tmp/.hf_cache TRANSFORMERS_OFFLINE=1 python -u eval_pi05_pruning_libero.py --prune_mode l2norm --keep_ratio 0.95 --suite libero_10 --n_episodes 500 --seed 42 --gpu 0\", \"data_count\": 500, \"data_path\": \"LIBERO-Long\", \"gpu\": 0, \"model_name\": \"pi0.5\", \"pid\": 931551, \"seed\": 42, \"server\": \"westd-38929\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-22T20:14:28.420Z\"}, \"eval_pi05_l2norm_k085_goal_seed42_w38929\": {\"checkpoint_path\": \"N/A - eval experiment\", \"completed_at\": \"2026-05-22T20:14:23.155Z\", \"conclusion\": \"negative\", \"created_at\": \"2026-05-22T13:22:54.323Z\", \"failure_reason\": \"stale RUNNING, no metrics after 6h\", \"hypothesis\": \"π0.5 L2norm k=0.85 LIBERO-Goal seed42: Goal baseline=96.4%. L2norm k=0.85 在 Object=98.0%。Goal suite 补充 cliff zone sweep，测试 L2norm 在 Goal 上 k=0.85 是否仍保持高 SR。\", \"log_path\": \"logs/pi05_l2norm_k085_goal_s42.log\", \"retry_count\": 0, \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=1 /root/miniconda3/bin/python -u eval_pi05_pruning_libero.py --prune_mode l2norm --keep_ratio 0.85 --suite libero_goal --n_episodes 500 --seed 42 --gpu 0\", \"data_count\": 500, \"data_path\": \"LIBERO-Goal\", \"gpu\": 1, \"log_path\": \"logs/pi05_l2norm_k085_goal_s42.log\", \"model_name\": \"pi0.5\", \"pid\": 179967, \"seed\": 42, \"server\": \"westd-38929\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-22T20:14:23.155Z\"}, \"random_k095_goal_seed42\": {\"checkpoint_path\": \"N/A - eval experiment\", \"completed_at\": \"2026-05-22T20:14:15.069Z\", \"conclusion\": \"negative\", \"created_at\": \"2026-05-22T09:45:15.687Z\", \"failure_reason\": \"stale RUNNING, 50-ep eval, no metrics after 10h\", \"hypothesis\": \"Cross-suite expansion: π0.5 random k=0.95 on LIBERO-Goal, testing cliff behavior generalization\", \"log_path\": \"logs/eval_pi05_random_k095_goal_seed42.log\", \"retry_count\": 0, \"spec\": {\"checkpoint_source\": \"/root/autodl-tmp/pi05_libero_finetuned\", \"command\": \"CUDA_VISIBLE_DEVICES=1 python -u eval_pi05_pruning_libero.py --prune_mode random --keep_ratio 0.95 --suite libero_goal --n_episodes 50 --seed 42 --gpu 0\", \"data_count\": 500, \"data_path\": \"libero_goal\", \"eval_data\": \"libero_goal\", \"log_path\": \"logs/eval_pi05_random_k095_goal_seed42.log\", \"model_name\": \"pi05_libero_finetuned\", \"pid\": 391150, \"seed\": 42, \"server\": \"westd-41074\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-22T20:14:15.069Z\"}, \"pi05_l2norm_k09_goal_s42\": {\"checkpoint_path\": \"N/A - eval experiment\", \"completed_at\": \"2026-05-22T20:14:12.352Z\", \"conclusion\": \"negative\", \"created_at\": \"2026-05-22T10:29:40.899Z\", \"failure_reason\": \"stale RUNNING, 50-ep eval, no metrics after 9h\", \"hypothesis\": \"Cross-suite expansion: π0.5 l2norm k=0.9 on LIBERO-Goal, testing cliff behavior generalization\", \"log_path\": \"logs/eval_pi05_l2norm_k09_goal_seed42.log\", \"retry_count\": 0, \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=2 HF_HOME=/root/autodl-tmp/.hf_cache TRANSFORMERS_OFFLINE=1 python -u eval_pi05_pruning_libero.py --prune_mode l2norm --keep_ratio 0.9 --suite libero_goal --n_episodes 50 --seed 42 --gpu 0\", \"data_count\": 500, \"data_path\": \"libero_goal\", \"log_path\": \"logs/eval_pi05_l2norm_k09_goal_seed42.log\", \"model_name\": \"pi05_libero_finetuned\", \"seed\": 42, \"server\": \"westd-38929\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-22T20:14:12.352Z\"}, \"eval_pi05_random_k085_goal_seed42_v2\": {\"checkpoint_path\": \"N/A - eval experiment\", \"completed_at\": \"2026-05-22T20:14:09.657Z\", \"conclusion\": \"negative\", \"created_at\": \"2026-05-22T15:47:54.038Z\", \"failure_reason\": \"superseded by eval_pi05_random_k085_goal_seed42_v3\", \"hypothesis\": \"π0.5 Random k=0.85 on LIBERO-Goal: Goal Random k=0.9=62.6% (significant drop from 96.4% baseline). Testing k=0.85 to map the cliff — does SR drop further or stabilize? This locates the critical pruning threshold for random pruning on Goal.\", \"log_path\": \"N/A - superseded by v3\", \"retry_count\": 0, \"spec\": {\"command\": \"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/importance_margin_vla_compress && TRANSFORMERS_OFFLINE=1 HF_HOME=/root/autodl-tmp/.hf_cache python -u eval_pi05_pruning_libero.py --prune_mode random --keep_ratio 0.85 --suite libero_goal --n_episodes 50 --seed 42 --gpu 1\", \"data_count\": 500, \"data_path\": \"/root/autodl-tmp/importance_margin_vla_compress\", \"model_name\": \"pi0.5\", \"seed\": 42, \"server\": \"cqa1-33015\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-22T20:14:09.657Z\"}, \"l2norm_k095_goal_seed42\": {\"checkpoint_path\": \"N/A - eval experiment\", \"completed_at\": \"2026-05-22T20:14:06.984Z\", \"conclusion\": \"negative\", \"created_at\": \"2026-05-22T09:45:18.484Z\", \"failure_reason\": \"duplicate of eval_pi05_l2norm_k095_goal_seed42\", \"hypothesis\": \"Cross-suite expansion: π0.5 l2norm k=0.95 on LIBERO-Goal, testing cliff behavior generalization\", \"log_path\": \"logs/eval_pi05_l2norm_k095_goal_seed42.log\", \"retry_count\": 0, \"spec\": {\"checkpoint_source\": \"/root/autodl-tmp/pi05_libero_finetuned\", \"command\": \"CUDA_VISIBLE_DEVICES=1 python -u eval_pi05_pruning_libero.py --prune_mode l2norm --keep_ratio 0.95 --suite libero_goal --n_episodes 50 --seed 42 --gpu 0\", \"data_count\": 500, \"data_path\": \"libero_goal\", \"eval_data\": \"libero_goal\", \"log_path\": \"logs/eval_pi05_l2norm_k095_goal_seed42.log\", \"model_name\": \"pi05_libero_finetuned\", \"pid\": 327841, \"seed\": 42, \"server\": \"westd-27271\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-22T20:14:06.984Z\"}, \"random_k095_long_seed42\": {\"checkpoint_path\": \"N/A - eval experiment\", \"completed_at\": \"2026-05-22T20:14:04.301Z\", \"conclusion\": \"negative\", \"created_at\": \"2026-05-22T09:45:20.992Z\", \"failure_reason\": \"duplicate of eval_pi05_random_k095_long_seed42\", \"hypothesis\": \"Cross-suite expansion: π0.5 random k=0.95 on LIBERO-Long, testing cliff behavior generalization\", \"log_path\": \"logs/eval_pi05_random_k095_long_seed42.log\", \"retry_count\": 0, \"spec\": {\"checkpoint_source\": \"/root/autodl-tmp/pi05_libero_finetuned\", \"command\": \"CUDA_VISIBLE_DEVICES=3 python -u eval_pi05_pruning_libero.py --prune_mode random --keep_ratio 0.95 --suite libero_10 --n_episodes 50 --seed 42 --gpu 0\", \"data_count\": 500, \"data_path\": \"libero_10\", \"eval_data\": \"libero_10\", \"log_path\": \"logs/eval_pi05_random_k095_long_seed42.log\", \"model_name\": \"pi05_libero_finetuned\", \"pid\": 335132, \"seed\": 42, \"server\": \"cqa1-33015\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-22T20:14:04.301Z\"}, \"pi05_l2norm_k095_long_s42\": {\"checkpoint_path\": \"N/A - eval experiment\", \"completed_at\": \"2026-05-22T20:14:01.662Z\", \"conclusion\": \"negative\", \"created_at\": \"2026-05-22T10:29:35.527Z\", \"failure_reason\": \"duplicate of eval_pi05_l2norm_k095_long_seed42\", \"hypothesis\": \"Cross-suite expansion: π0.5 l2norm k=0.95 on LIBERO-Long, testing cliff behavior generalization\", \"log_path\": \"logs/eval_pi05_l2norm_k095_long_seed42.log\", \"retry_count\": 0, \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=0 HF_HOME=/root/autodl-tmp/.hf_cache TRANSFORMERS_OFFLINE=1 python -u eval_pi05_pruning_libero.py --prune_mode l2norm --keep_ratio 0.95 --suite libero_10 --n_episodes 50 --seed 42 --gpu 0\", \"data_count\": 500, \"data_path\": \"libero_10\", \"log_path\": \"logs/eval_pi05_l2norm_k095_long_seed42.log\", \"model_name\": \"pi05_libero_finetuned\", \"seed\": 42, \"server\": \"westd-38929\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-22T20:14:01.662Z\"}, \"pi05_random_k09_goal_s42\": {\"checkpoint_path\": \"N/A - eval experiment\", \"completed_at\": \"2026-05-22T20:13:58.986Z\", \"conclusion\": \"negative\", \"created_at\": \"2026-05-22T10:29:38.376Z\", \"failure_reason\": \"duplicate of eval_pi05_random_k09_goal_seed42\", \"hypothesis\": \"Cross-suite expansion: π0.5 random k=0.9 on LIBERO-Goal, testing cliff behavior generalization\", \"log_path\": \"logs/eval_pi05_random_k09_goal_seed42.log\", \"retry_count\": 0, \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=1 HF_HOME=/root/autodl-tmp/.hf_cache TRANSFORMERS_OFFLINE=1 python -u eval_pi05_pruning_libero.py --prune_mode random --keep_ratio 0.9 --suite libero_goal --n_episodes 50 --seed 42 --gpu 0\", \"data_count\": 500, \"data_path\": \"libero_goal\", \"log_path\": \"logs/eval_pi05_random_k09_goal_seed42.log\", \"model_name\": \"pi05_libero_finetuned\", \"seed\": 42, \"server\": \"westd-38929\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-22T20:13:58.986Z\"}, \"pi05_l2norm_k085_goal_s42\": {\"checkpoint_path\": \"N/A - eval experiment\", \"completed_at\": \"2026-05-22T20:13:56.338Z\", \"conclusion\": \"negative\", \"created_at\": \"2026-05-22T10:29:45.863Z\", \"failure_reason\": \"duplicate of eval_pi05_l2norm_k085_goal_seed42_w38929\", \"hypothesis\": \"Cross-suite expansion: π0.5 l2norm k=0.85 on LIBERO-Goal, testing cliff behavior generalization\", \"log_path\": \"logs/eval_pi05_l2norm_k085_goal_seed42.log\", \"retry_count\": 0, \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=0 HF_HOME=/root/autodl-tmp/.hf_cache TRANSFORMERS_OFFLINE=1 python -u eval_pi05_pruning_libero.py --prune_mode l2norm --keep_ratio 0.85 --suite libero_goal --n_episodes 50 --seed 42 --gpu 0\", \"data_count\": 500, \"data_path\": \"libero_goal\", \"log_path\": \"logs/eval_pi05_l2norm_k085_goal_seed42.log\", \"model_name\": \"pi05_libero_finetuned\", \"seed\": 42, \"server\": \"westd-41074\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-22T20:13:56.338Z\"}, \"train_openvla_sc_m96_seed42_v3\": {\"checkpoint_path\": \"N/A - stale, no checkpoint saved\", \"completed_at\": \"2026-05-22T20:13:53.566Z\", \"conclusion\": \"negative\", \"created_at\": \"2026-05-20T06:16:25.780Z\", \"failure_reason\": \"stale RUNNING, no metrics after 24h\", \"hypothesis\": \"OpenVLA VTC-only M=96 (256→96 tokens, 62.5% compression). M-sweep data point. Retracked from orphan PID 68539 after config-missing failure. Training from step 0, currently at ~2000+. If M=96 SR falls between M=128 and M=64, confirms graded degradation for MLP-projector VTC re-encoding on OpenVLA.\", \"log_path\": \"N/A - stale\", \"parent\": \"train_openvla_sc_m128_vtconly_seed42\", \"retry_count\": 0, \"spec\": {\"checkpoint_source\": \"openvla/openvla-7b\", \"command\": \"python train_openvla_smart_compress.py --config configs/openvla_smart_compress_m96.yaml\", \"data_count\": 50000, \"data_path\": \"LIBERO\", \"eval_data\": \"N/A - training experiment\", \"gpu\": \"cuda:2\", \"model_name\": \"openvla-7b\", \"pid\": 68539, \"seed\": 42, \"server\": \"westd-41074\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-22T20:13:53.566Z\"}, \"train_openvla_sc_m64_seed42_v6\": {\"checkpoint_path\": \"N/A - stale, no checkpoint saved\", \"completed_at\": \"2026-05-22T20:13:50.371Z\", \"conclusion\": \"negative\", \"created_at\": \"2026-05-21T18:14:05.043Z\", \"failure_reason\": \"stale RUNNING, no metrics after 24h\", \"hypothesis\": \"OpenVLA VTC-only M=64 (256→64 tokens, 75% compression) v6 retry. v5 SIGKILL at step 17050 (原因不明，疑似磁盘空间). 验证 VTC re-encoding 在 M=64 的效果，与 M=96/M=32 形成 M-sweep 曲线。\", \"log_path\": \"N/A - stale\", \"parent\": \"train_openvla_sc_m64_seed42_v5\", \"retry_count\": 0, \"spec\": {\"checkpoint_source\": \"openvla/openvla-7b\", \"command\": \"python train_openvla_smart_compress.py --config configs/openvla_smart_compress_m64.yaml\", \"data_count\": 50000, \"data_path\": \"LIBERO\", \"eval_data\": \"N/A - training experiment\", \"gpu_id\": 3, \"model_name\": \"openvla-7b + VTC(M=64)\", \"pid\": 59671, \"seed\": 42, \"server\": \"westd-41074\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-22T20:13:50.371Z\"}, \"eval_pi05_attention_k085_object_seed42\": {\"completed_at\": \"2026-05-22T19:12:22.719Z\", \"conclusion\": \"success\", \"created_at\": \"2026-05-22T19:08:59.913Z\", \"hypothesis\": \"π0.5 Attention k=0.85 Object: 15% attention-based removal. Testing cliff zone.\", \"metrics\": {\"num_episodes\": 500, \"num_success\": 461, \"seed\": 42, \"success_rate\": 0.922, \"suite\": \"libero_object\"}, \"retry_count\": 0, \"spec\": {\"checkpoint_path\": \"eval_results/pi05_attention_0.85_libero_object.json\", \"command\": \"python eval_pi05_pruning_libero.py --prune_mode attention --keep_ratio 0.85 --suite libero_object --n_episodes 50 --seed 42\", \"data_count\": 500, \"data_path\": \"libero_object\", \"log_path\": \"logs/pi05_attention_0.85_libero_object.log\", \"model_name\": \"pi0.5\", \"seed\": 42, \"server\": \"westd-41074\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-22T19:12:22.719Z\"}, \"eval_pi05_attention_k09_object_seed42\": {\"completed_at\": \"2026-05-22T19:12:20.074Z\", \"conclusion\": \"success\", \"created_at\": \"2026-05-22T19:06:10.900Z\", \"hypothesis\": \"π0.5 Attention pruning k=0.9 on Object: 10% attention-based removal. Attention k=0.95=98.4%. Testing if attention pruning maintains advantage over L2norm at more aggressive pruning.\", \"metrics\": {\"num_episodes\": 500, \"num_success\": 486, \"seed\": 42, \"success_rate\": 0.972, \"suite\": \"libero_object\"}, \"retry_count\": 0, \"spec\": {\"checkpoint_path\": \"eval_results/pi05_attention_0.9_libero_object.json\", \"command\": \"python eval_pi05_pruning_libero.py --prune_mode attention --keep_ratio 0.9 --suite libero_object --n_episodes 50 --seed 42\", \"data_count\": 500, \"data_path\": \"libero_object\", \"log_path\": \"logs/pi05_attention_0.9_libero_object.log\", \"model_name\": \"pi0.5\", \"seed\": 42, \"server\": \"westd-41074\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-22T19:12:20.074Z\"}, \"smolvla_random_k095_long_seed42\": {\"completed_at\": \"2026-05-22T19:12:14.893Z\", \"conclusion\": \"negative\", \"created_at\": \"2026-05-22T19:08:58.420Z\", \"hypothesis\": \"SmolVLA Random k=0.95 Long: 5% random removal on long-horizon tasks.\", \"metrics\": {\"num_episodes\": 500, \"num_success\": 0, \"seed\": 42, \"success_rate\": 0, \"suite\": \"libero_10\"}, \"retry_count\": 0, \"spec\": {\"checkpoint_path\": \"results/smolvla_random_libero_10.json\", \"command\": \"python eval_official_libero.py --mode random_prune --k_ratio 0.95 --suite libero_10 --num_episodes 50 --seed 42\", \"data_count\": 500, \"data_path\": \"libero_10\", \"log_path\": \"logs/smolvla_random_libero_10.log\", \"model_name\": \"SmolVLA\", \"seed\": 42, \"server\": \"westd-38929\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-22T19:12:14.893Z\"}, \"smolvla_l2norm_k095_long_seed42\": {\"completed_at\": \"2026-05-22T19:12:12.184Z\", \"conclusion\": \"negative\", \"created_at\": \"2026-05-22T19:08:56.897Z\", \"hypothesis\": \"SmolVLA L2norm k=0.95 Long: 5% removal on long-horizon tasks.\", \"metrics\": {\"num_episodes\": 500, \"num_success\": 0, \"seed\": 42, \"success_rate\": 0, \"suite\": \"libero_10\"}, \"retry_count\": 0, \"spec\": {\"checkpoint_path\": \"results/smolvla_l2norm_libero_10.json\", \"command\": \"python eval_official_libero.py --mode l2_norm --k_ratio 0.95 --suite libero_10 --num_episodes 50 --seed 42\", \"data_count\": 500, \"data_path\": \"libero_10\", \"log_path\": \"logs/smolvla_l2norm_libero_10.log\", \"model_name\": \"SmolVLA\", \"seed\": 42, \"server\": \"westd-38929\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-22T19:12:12.184Z\"}, \"smolvla_random_k095_goal_seed42\": {\"completed_at\": \"2026-05-22T19:12:09.549Z\", \"conclusion\": \"negative\", \"created_at\": \"2026-05-22T19:08:55.300Z\", \"hypothesis\": \"SmolVLA Random k=0.95 Goal: 5% random removal on goal tasks.\", \"metrics\": {\"num_episodes\": 500, \"num_success\": 21, \"seed\": 42, \"success_rate\": 0.042, \"suite\": \"libero_goal\"}, \"retry_count\": 0, \"spec\": {\"checkpoint_path\": \"results/smolvla_random_libero_goal.json\", \"command\": \"python eval_official_libero.py --mode random_prune --k_ratio 0.95 --suite libero_goal --num_episodes 50 --seed 42\", \"data_count\": 500, \"data_path\": \"libero_goal\", \"log_path\": \"logs/smolvla_random_libero_goal.log\", \"model_name\": \"SmolVLA\", \"seed\": 42, \"server\": \"westd-38929\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-22T19:12:09.549Z\"}, \"smolvla_l2norm_k095_goal_seed42\": {\"completed_at\": \"2026-05-22T19:12:06.722Z\", \"conclusion\": \"negative\", \"created_at\": \"2026-05-22T19:08:53.830Z\", \"hypothesis\": \"SmolVLA L2norm k=0.95 Goal: 5% removal on goal-conditioned tasks.\", \"metrics\": {\"num_episodes\": 500, \"num_success\": 17, \"seed\": 42, \"success_rate\": 0.034, \"suite\": \"libero_goal\"}, \"retry_count\": 0, \"spec\": {\"checkpoint_path\": \"results/smolvla_l2norm_libero_goal.json\", \"command\": \"python eval_official_libero.py --mode l2_norm --k_ratio 0.95 --suite libero_goal --num_episodes 50 --seed 42\", \"data_count\": 500, \"data_path\": \"libero_goal\", \"log_path\": \"logs/smolvla_l2norm_libero_goal.log\", \"model_name\": \"SmolVLA\", \"seed\": 42, \"server\": \"westd-38929\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-22T19:12:06.722Z\"}, \"smolvla_random_k095_spatial_seed42\": {\"completed_at\": \"2026-05-22T19:12:03.693Z\", \"conclusion\": \"negative\", \"created_at\": \"2026-05-22T19:08:52.300Z\", \"hypothesis\": \"SmolVLA Random k=0.95 Spatial: 5% random removal on 64-token pixel-shuffle.\", \"metrics\": {\"num_episodes\": 500, \"num_success\": 21, \"seed\": 42, \"success_rate\": 0.042, \"suite\": \"libero_spatial\"}, \"retry_count\": 0, \"spec\": {\"checkpoint_path\": \"results/smolvla_random_libero_spatial.json\", \"command\": \"python eval_official_libero.py --mode random_prune --k_ratio 0.95 --suite libero_spatial --num_episodes 50 --seed 42\", \"data_count\": 500, \"data_path\": \"libero_spatial\", \"log_path\": \"logs/smolvla_random_libero_spatial.log\", \"model_name\": \"SmolVLA\", \"seed\": 42, \"server\": \"westd-38929\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-22T19:12:03.693Z\"}, \"smolvla_l2norm_k095_spatial_seed42\": {\"completed_at\": \"2026-05-22T19:12:00.950Z\", \"conclusion\": \"negative\", \"created_at\": \"2026-05-22T19:06:31.842Z\", \"hypothesis\": \"SmolVLA L2norm k=0.95 on Spatial: pixel-shuffle with only 64 tokens. Even 5% removal expected to be catastrophic given zero_mask results.\", \"metrics\": {\"num_episodes\": 500, \"num_success\": 33, \"seed\": 42, \"success_rate\": 0.066, \"suite\": \"libero_spatial\"}, \"retry_count\": 0, \"spec\": {\"checkpoint_path\": \"results/smolvla_l2norm_libero_spatial.json\", \"command\": \"python eval_official_libero.py --mode l2_norm --k_ratio 0.95 --suite libero_spatial --num_episodes 50 --seed 42\", \"data_count\": 500, \"data_path\": \"libero_spatial\", \"log_path\": \"logs/smolvla_l2norm_libero_spatial.log\", \"model_name\": \"SmolVLA\", \"seed\": 42, \"server\": \"westd-38929\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-22T19:12:00.950Z\"}, \"smolvla_baseline_long_seed42\": {\"completed_at\": \"2026-05-22T19:11:58.268Z\", \"conclusion\": \"success\", \"created_at\": \"2026-05-22T19:06:30.381Z\", \"hypothesis\": \"SmolVLA baseline on LIBERO-Long: unpruned performance reference for long-horizon tasks with pixel-shuffle connector (64 tokens).\", \"metrics\": {\"num_episodes\": 500, \"num_success\": 183, \"seed\": 42, \"success_rate\": 0.366, \"suite\": \"libero_10\"}, \"retry_count\": 0, \"spec\": {\"checkpoint_path\": \"results/smolvla_baseline_libero_10.json\", \"command\": \"python eval_official_libero.py --mode baseline --suite libero_10 --num_episodes 50 --seed 42\", \"data_count\": 500, \"data_path\": \"libero_10\", \"log_path\": \"logs/smolvla_baseline_libero_10.log\", \"model_name\": \"SmolVLA\", \"seed\": 42, \"server\": \"westd-38929\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-22T19:11:58.268Z\"}, \"eval_xvla_l2norm_k09_spatial_seed42\": {\"completed_at\": \"2026-05-22T19:06:25.901Z\", \"conclusion\": \"negative\", \"created_at\": \"2026-05-22T19:04:42.156Z\", \"hypothesis\": \"X-VLA L2norm k=0.9 on LIBERO-Spatial: 10% token removal on spatial reasoning tasks. Baseline Spatial=78.4%.\", \"metrics\": {\"num_episodes\": 500, \"num_success\": 394, \"seed\": 42, \"success_rate\": 0.788, \"suite\": \"libero_spatial\"}, \"retry_count\": 0, \"spec\": {\"checkpoint_path\": \"results/xvla_spatial_l2norm_k09.json\", \"command\": \"python eval_xvla_pruning_libero.py --suite libero_spatial --keep_ratio 0.9 --mode l2_norm --seed 42\", \"data_count\": 500, \"data_path\": \"libero_spatial\", \"log_path\": \"logs/xvla_l2norm_k09_spatial.log\", \"model_name\": \"X-VLA\", \"seed\": 42, \"server\": \"westd-27271\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-22T19:06:25.901Z\"}, \"eval_xvla_l2norm_k09_goal_seed42\": {\"completed_at\": \"2026-05-22T19:05:49.641Z\", \"conclusion\": \"negative\", \"created_at\": \"2026-05-22T19:04:40.719Z\", \"hypothesis\": \"X-VLA L2norm k=0.9 on LIBERO-Goal: 10% token removal. Goal baseline=92.2%. Testing degradation curve.\", \"metrics\": {\"num_episodes\": 500, \"num_success\": 351, \"seed\": 42, \"success_rate\": 0.702, \"suite\": \"libero_goal\"}, \"retry_count\": 0, \"spec\": {\"checkpoint_path\": \"results/xvla_goal_l2norm_k09.json\", \"command\": \"python eval_xvla_pruning_libero.py --suite libero_goal --keep_ratio 0.9 --mode l2_norm --seed 42\", \"data_count\": 500, \"data_path\": \"libero_goal\", \"log_path\": \"logs/xvla_l2norm_k09_goal.log\", \"model_name\": \"X-VLA\", \"seed\": 42, \"server\": \"westd-27271\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-22T19:05:49.641Z\"}, \"eval_xvla_l2norm_k095_goal_seed42\": {\"completed_at\": \"2026-05-22T19:05:24.366Z\", \"conclusion\": \"negative\", \"created_at\": \"2026-05-22T15:10:32.676Z\", \"hypothesis\": \"L2-norm based vision token pruning at 95% keep ratio on X-VLA libero_goal should preserve most performance (within 2-3% of baseline) since only 5% of least-important tokens are removed.\", \"metrics\": {\"num_episodes\": 500, \"num_success\": 269, \"seed\": 42, \"success_rate\": 0.538, \"suite\": \"libero_goal\"}, \"retry_count\": 0, \"spec\": {\"checkpoint_path\": \"results/xvla_goal_l2norm_k095.json\", \"checkpoint_source\": \"/root/autodl-tmp/X-VLA-Libero\", \"command\": \"CUDA_VISIBLE_DEVICES=1 TRANSFORMERS_OFFLINE=1 MUJOCO_GL=egl python -u eval_xvla_pruning_libero.py --model_path /root/autodl-tmp/X-VLA-Libero --suite libero_goal --keep_ratio 0.95 --mode l2_norm --num_episodes 50 --seed 42 --gpu 0\", \"data_count\": 50, \"data_path\": \"libero_goal\", \"eval_data\": \"libero_goal\", \"gpu\": \"cuda:1\", \"log_path\": \"logs/xvla_l2norm_k095_goal.log\", \"model_name\": \"X-VLA-Libero\", \"seed\": 42, \"server\": \"westd-27271\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-22T19:05:24.366Z\"}, \"eval_xvla_l2norm_k095_spatial_seed42\": {\"completed_at\": \"2026-05-22T19:05:21.806Z\", \"conclusion\": \"negative\", \"created_at\": \"2026-05-22T15:10:31.187Z\", \"hypothesis\": \"L2-norm based vision token pruning at 95% keep ratio on X-VLA libero_spatial should preserve most performance (within 2-3% of baseline) since only 5% of least-important tokens are removed.\", \"metrics\": {\"num_episodes\": 500, \"num_success\": 358, \"seed\": 42, \"success_rate\": 0.716, \"suite\": \"libero_spatial\"}, \"retry_count\": 0, \"spec\": {\"checkpoint_path\": \"results/xvla_spatial_l2norm_k095.json\", \"checkpoint_source\": \"/root/autodl-tmp/X-VLA-Libero\", \"command\": \"CUDA_VISIBLE_DEVICES=0 TRANSFORMERS_OFFLINE=1 MUJOCO_GL=egl python -u eval_xvla_pruning_libero.py --model_path /root/autodl-tmp/X-VLA-Libero --suite libero_spatial --keep_ratio 0.95 --mode l2_norm --num_episodes 50 --seed 42 --gpu 0\", \"data_count\": 50, \"data_path\": \"libero_spatial\", \"eval_data\": \"libero_spatial\", \"gpu\": \"cuda:0\", \"log_path\": \"logs/xvla_l2norm_k095_spatial.log\", \"model_name\": \"X-VLA-Libero\", \"seed\": 42, \"server\": \"westd-27271\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-22T19:05:21.806Z\"}, \"eval_pi05_attention_k095_object_seed42\": {\"completed_at\": \"2026-05-22T16:01:16.962Z\", \"conclusion\": \"success\", \"created_at\": \"2026-05-22T16:00:19.432Z\", \"hypothesis\": \"π0.5 attention-based pruning k=0.95 on LIBERO-Object: cross-attention importance scores should identify truly important tokens better than L2norm, yielding higher SR at same keep ratio.\", \"metrics\": {\"keep_tokens\": 690, \"num_episodes\": 500, \"seed\": 42, \"success_rate\": 0.984, \"suite\": \"libero_object\", \"total_tokens\": 768, \"wilson_ci_95\": [0.969, 0.992]}, \"retry_count\": 0, \"spec\": {\"checkpoint_path\": \"eval_results/pi05_attention_k0.95_libero_object_seed42.json\", \"command\": \"python eval_pi05_pruning_libero.py --prune_mode attention --keep_ratio 0.95 --suite libero_object --n_episodes 50 --seed 42\", \"data_count\": 500, \"data_path\": \"libero_object\", \"log_path\": \"eval_results/pi05_attention_k0.95_libero_object_seed42.json\", \"model_name\": \"pi0.5\", \"seed\": 42, \"server\": \"westd-41074\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-22T16:01:16.962Z\"}, \"eval_xvla_l2norm_k09_long_seed42\": {\"completed_at\": \"2026-05-22T16:01:14.509Z\", \"conclusion\": \"negative\", \"created_at\": \"2026-05-22T16:00:17.701Z\", \"hypothesis\": \"X-VLA L2norm k=0.9 on LIBERO-Long: testing if 10% token removal degrades performance on long-horizon tasks. Baseline=92.5%.\", \"metrics\": {\"num_episodes\": 500, \"seed\": 42, \"success_rate\": 0.275, \"suite\": \"libero_10\", \"wilson_ci_95\": [0.218, 0.341]}, \"retry_count\": 0, \"spec\": {\"checkpoint_path\": \"results/xvla_long_l2norm_k09.json\", \"command\": \"python eval_xvla_pruning_libero.py --suite libero_10 --prune_mode l2norm --keep_ratio 0.9 --seed 42\", \"data_count\": 500, \"data_path\": \"libero_10\", \"log_path\": \"results/xvla_long_l2norm_k09.json\", \"model_name\": \"X-VLA\", \"seed\": 42, \"server\": \"westd-41074\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-22T16:01:14.509Z\"}, \"eval_xvla_l2norm_k095_long_seed42\": {\"completed_at\": \"2026-05-22T16:01:12.012Z\", \"conclusion\": \"negative\", \"created_at\": \"2026-05-22T16:00:16.262Z\", \"hypothesis\": \"X-VLA L2norm k=0.95 on LIBERO-Long: testing if 5% token removal preserves performance on long-horizon tasks. X-VLA uses linear projection (256 tokens).\", \"metrics\": {\"num_episodes\": 500, \"seed\": 42, \"success_rate\": 0.47, \"suite\": \"libero_10\", \"wilson_ci_95\": [0.402, 0.539]}, \"retry_count\": 0, \"spec\": {\"checkpoint_path\": \"results/xvla_long_l2norm_k095.json\", \"command\": \"python eval_xvla_pruning_libero.py --suite libero_10 --prune_mode l2norm --keep_ratio 0.95 --seed 42\", \"data_count\": 500, \"data_path\": \"libero_10\", \"log_path\": \"results/xvla_long_l2norm_k095.json\", \"model_name\": \"X-VLA\", \"seed\": 42, \"server\": \"westd-41074\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-22T16:01:12.012Z\"}, \"eval_xvla_baseline_long_seed42\": {\"completed_at\": \"2026-05-21T02:35:47.190358+00:00\", \"conclusion\": \"success\", \"created_at\": \"2026-05-21T00:49:09.251Z\", \"hypothesis\": \"X-VLA baseline on LIBERO-Long (LIBERO-10). Long-horizon tasks may have different baseline SR. Establishes reference for C1 cross-suite analysis\", \"metrics\": {\"num_episodes\": 500, \"per_task\": [0.96, 0.68, 1.0, 0.98, 0.94, 0.96, 0.94, 0.96, 1.0, 0.98], \"seed\": 42, \"success_rate\": 0.94, \"suite\": \"libero_10\", \"wilson_ci_95\": [0.916, 0.958]}, \"notes\": \"Suite is libero_10 (LIBERO-Long). Baseline for cross-suite pruning comparison.\", \"retry_count\": 0, \"spec\": {\"checkpoint_path\": \"results/xvla_long_baseline.json\", \"checkpoint_source\": \"/root/autodl-tmp/X-VLA-Libero\", \"command\": \"python eval_xvla_pruning_libero.py --suite libero_10 --prune_mode none --seed 42\", \"data_count\": 500, \"data_path\": \"libero_10\", \"eval_data\": \"libero_10 (10 tasks x 50 episodes)\", \"gpu\": \"cuda:1\", \"log_path\": \"results/xvla_long_baseline.json\", \"model_name\": \"X-VLA\", \"seed\": 42, \"server\": \"westd-41074\", \"tmux_session\": \"eval_xvla_baseline_long\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-22T15:59:58.416Z\"}, \"pi05_random_k085_goal_s42\": {\"completed_at\": \"2026-05-22T15:10:27.219Z\", \"conclusion\": \"failed\", \"created_at\": \"2026-05-22T10:29:43.375Z\", \"hypothesis\": \"Cross-suite expansion: π0.5 random k=0.85 on LIBERO-Goal, testing cliff behavior generalization\", \"retry_count\": 0, \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=3 python -u eval_pi05_pruning_libero.py --prune_mode random --keep_ratio 0.85 --suite libero_goal --n_episodes 50 --seed 42 --gpu 0\", \"data_count\": 500, \"data_path\": \"libero_goal\", \"log_path\": \"logs/eval_pi05_random_k085_goal_seed42.log\", \"model_name\": \"pi05_libero_finetuned\", \"seed\": 42, \"server\": \"westd-38929\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-22T15:10:27.219Z\"}, \"smolvla_official_goal_baseline_s42\": {\"completed_at\": \"2026-05-22T15:09:33.408Z\", \"conclusion\": \"success\", \"created_at\": \"2026-05-22T15:08:13.920Z\", \"hypothesis\": \"SmolVLA official checkpoint establishes the baseline success rate on libero_goal without any pruning, providing the reference point for evaluating compression methods.\", \"metrics\": {\"success_rate\": 0.608, \"total_episodes\": 500, \"total_successes\": 304, \"wilson_ci_95\": [0.5645, 0.6498]}, \"retry_count\": 0, \"spec\": {\"checkpoint_path\": \"N/A\", \"checkpoint_source\": \"/root/autodl-tmp/.hf_cache/smolvla_libero_official\", \"command\": \"eval_official_libero.py --mode baseline --suite libero_goal --num_episodes 50 --seed 42\", \"data_count\": 500, \"data_path\": \"libero_goal\", \"eval_data\": \"libero_goal\", \"log_path\": \"logs/smolvla_baseline_goal_s42.log\", \"model_name\": \"smolvla_libero_official\", \"seed\": 42, \"server\": \"westd-38929\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-22T15:09:33.408Z\"}, \"smolvla_official_object_l2norm_k095_s42\": {\"completed_at\": \"2026-05-22T15:09:30.608Z\", \"conclusion\": \"negative\", \"created_at\": \"2026-05-22T15:08:11.446Z\", \"hypothesis\": \"L2-norm based pruning at k=0.95 on SmolVLA official checkpoint preserves most performance on libero_object by removing only the least important 5% of expert neurons.\", \"metrics\": {\"success_rate\": 0.002, \"total_episodes\": 500, \"total_successes\": 1, \"wilson_ci_95\": [0.0004, 0.0112]}, \"retry_count\": 0, \"spec\": {\"checkpoint_path\": \"N/A\", \"checkpoint_source\": \"/root/autodl-tmp/.hf_cache/smolvla_libero_official\", \"command\": \"eval_official_libero.py --mode l2_norm --k_ratio 0.95 --suite libero_object --num_episodes 50 --seed 42\", \"data_count\": 500, \"data_path\": \"libero_object\", \"eval_data\": \"libero_object\", \"log_path\": \"logs/smolvla_l2norm_k095_object_s42.log\", \"model_name\": \"smolvla_libero_official\", \"seed\": 42, \"server\": \"westd-38929\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-22T15:09:30.608Z\"}, \"smolvla_official_spatial_baseline_s42\": {\"completed_at\": \"2026-05-22T15:09:27.993Z\", \"conclusion\": \"success\", \"created_at\": \"2026-05-22T15:08:09.043Z\", \"hypothesis\": \"SmolVLA official checkpoint establishes the baseline success rate on libero_spatial without any pruning, providing the reference point for evaluating compression methods.\", \"metrics\": {\"success_rate\": 0.446, \"total_episodes\": 500, \"total_successes\": 223, \"wilson_ci_95\": [0.403, 0.4898]}, \"retry_count\": 0, \"spec\": {\"checkpoint_path\": \"N/A\", \"checkpoint_source\": \"/root/autodl-tmp/.hf_cache/smolvla_libero_official\", \"command\": \"eval_official_libero.py --mode baseline --suite libero_spatial --num_episodes 50 --seed 42\", \"data_count\": 500, \"data_path\": \"libero_spatial\", \"eval_data\": \"libero_spatial\", \"log_path\": \"logs/smolvla_baseline_spatial_s42.log\", \"model_name\": \"smolvla_libero_official\", \"seed\": 42, \"server\": \"westd-38929\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-22T15:09:27.993Z\"}, \"eval_pi05_baseline_goal_seed42\": {\"completed_at\": \"2026-05-22T13:19:07.384Z\", \"conclusion\": \"success\", \"created_at\": \"2026-05-22T09:39:56.232Z\", \"hypothesis\": \"Cross-suite expansion: π0.5 baseline (no pruning) on LIBERO-Goal, establishing reference SR for pruning comparisons. Goal suite tests goal-conditioned manipulation with max_steps=400.\", \"metrics\": {\"elapsed_min\": 49.7, \"overall_sr\": 0.964, \"per_task\": {\"bowl_on_cabinet\": 1, \"bowl_on_plate\": 1, \"bowl_on_stove\": 1, \"cream_cheese_in_bowl\": 0.96, \"open_middle_drawer\": 0.9, \"open_top_drawer_bowl_inside\": 0.9, \"push_plate_front_stove\": 1, \"turn_on_stove\": 1, \"wine_bottle_on_cabinet\": 0.98, \"wine_bottle_on_rack\": 0.9}, \"total_episodes\": 500, \"total_successes\": 482}, \"retry_count\": 0, \"spec\": {\"checkpoint_path\": \"/root/autodl-tmp/pi05_libero_finetuned\", \"command\": \"CUDA_VISIBLE_DEVICES=0 python -u eval_pi05_pruning_libero.py --prune_mode none --suite libero_goal --n_episodes 50 --seed 42 --gpu 0\", \"data_count\": 500, \"data_path\": \"libero_goal\", \"gpu\": 0, \"log_path\": \"logs/eval_pi05_baseline_goal_seed42.log\", \"model_name\": \"pi0.5\", \"pid\": 329795, \"seed\": 42, \"server\": \"cqa1-33015\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-22T13:19:07.384Z\"}, \"eval_smolvla_zeromask_l2norm_k095_object_seed42\": {\"completed_at\": \"2026-05-22T12:30:26.712Z\", \"conclusion\": \"negative\", \"created_at\": \"2026-05-22T11:43:39.042Z\", \"hypothesis\": \"SmolVLA zero_mask l2norm k=0.95: 将 5% 最低 L2 norm tokens 置零但不删除。与 random zero_mask 配对。如果两者都 0% → 确认 64-token 表示中每个 token 不可替代。\", \"metrics\": {\"per_task\": {\"task0_alphabet_soup\": 0, \"task1_cream_cheese\": 0, \"task2_salad_dressing\": 0, \"task3_bbq_sauce\": 0, \"task4_ketchup\": 0, \"task5_tomato_sauce\": 0, \"task6_butter\": 0, \"task7_milk\": 0, \"task8_chocolate_pudding\": 0, \"task9_orange_juice\": 0}, \"success_rate\": 0, \"total_episodes\": 500, \"total_successes\": 0, \"wilson_ci_95\": [0, 0.0076]}, \"retry_count\": 0, \"spec\": {\"checkpoint_path\": \"/root/autodl-tmp/.hf_cache/smolvla_libero_official\", \"checkpoint_source\": \"HuggingFaceVLA/smolvla_libero\", \"command\": \"CUDA_VISIBLE_DEVICES=1 python -u eval_smolvla_pruning_official.py --mode l2_norm --k_ratio 0.95 --prune_type zero_mask --suite libero_object --num_episodes 50 --seed 42 --gpu 0\", \"data_count\": 500, \"data_path\": \"LIBERO-Object\", \"eval_data\": \"LIBERO-Object 500 episodes\", \"gpu\": 1, \"log_path\": \"/root/autodl-tmp/importance_margin_vla_compress/logs/smolvla_zeromask_l2norm_k095.log\", \"model_name\": \"SmolVLA-official\", \"pid\": 398985, \"seed\": 42, \"server\": \"westd-27271\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-22T12:30:26.711Z\"}, \"eval_smolvla_zeromask_random_k095_object_seed42\": {\"completed_at\": \"2026-05-22T12:30:24.102Z\", \"conclusion\": \"negative\", \"created_at\": \"2026-05-22T11:43:36.591Z\", \"hypothesis\": \"SmolVLA zero_mask random k=0.95: 将 5% random tokens 置零但不删除（保持序列长度 64）。如果 SR=0% 同 true_removal → token 信息本身不可丢（信息密度解释）。如果 SR>0% → true_removal 的 0% 由 position shift 导致。\", \"metrics\": {\"per_task\": {\"task0_alphabet_soup\": 0, \"task1_cream_cheese\": 0, \"task2_salad_dressing\": 0, \"task3_bbq_sauce\": 0, \"task4_ketchup\": 0, \"task5_tomato_sauce\": 0.02, \"task6_butter\": 0, \"task7_milk\": 0, \"task8_chocolate_pudding\": 0, \"task9_orange_juice\": 0}, \"success_rate\": 0.002, \"total_episodes\": 500, \"total_successes\": 1, \"wilson_ci_95\": [0.0004, 0.0112]}, \"retry_count\": 0, \"spec\": {\"checkpoint_path\": \"/root/autodl-tmp/.hf_cache/smolvla_libero_official\", \"checkpoint_source\": \"HuggingFaceVLA/smolvla_libero\", \"command\": \"CUDA_VISIBLE_DEVICES=0 python -u eval_smolvla_pruning_official.py --mode random --k_ratio 0.95 --prune_type zero_mask --suite libero_object --num_episodes 50 --seed 42 --gpu 0\", \"data_count\": 500, \"data_path\": \"LIBERO-Object\", \"eval_data\": \"LIBERO-Object 500 episodes\", \"gpu\": 0, \"log_path\": \"/root/autodl-tmp/importance_margin_vla_compress/logs/smolvla_zeromask_random_k095.log\", \"model_name\": \"SmolVLA-official\", \"pid\": 396732, \"seed\": 42, \"server\": \"westd-27271\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-22T12:30:24.102Z\"}, \"train_openvla_sc_m96_seed42\": {\"completed_at\": \"2026-05-20T04:03:07.628Z\", \"conclusion\": \"success\", \"created_at\": \"2026-05-20T03:28:39.563Z\", \"extra\": {\"hook_events\": [{\"action\": \"agent\", \"event\": \"on_failed\", \"ts\": \"2026-05-20T04:03:12.154753+00:00\"}], \"previous_failure\": {\"conclusion\": \"failed\"}}, \"failure_reason\": \"process dead 5× with no sentinel/W&B — auto-resolved as failed\", \"hypothesis\": \"OpenVLA VTC-only M=96 (256→96 tokens, 62.5% compression). M-sweep data point between M=128 and M=64. If M=96 SR falls between M=128 and M=64 SR, confirms graded degradation pattern for MLP-projector VTC re-encoding on OpenVLA. Retry of vtconly variant after D096 approved early M-sweep start.\", \"metrics\": {\"final_eval_loss\": 2.6575, \"final_train_loss\": 2.4509, \"steps_completed\": 99999, \"steps_total\": 100000}, \"parent\": \"train_openvla_sc_m128_vtconly_seed42\", \"reproduce\": {\"finished_at\": \"2026-05-20T04:03:05.586Z\"}, \"retry_count\": 1, \"spec\": {\"checkpoint_path\": \"/root/autodl-tmp/importance_margin_vla_compress/checkpoints/openvla_sc_m96_seed42/checkpoint_step99999.pt\", \"checkpoint_source\": \"openvla/openvla-7b\", \"command\": \"python train_openvla_smart_compress.py --n_queries 96 --seed 42\", \"data_count\": 500, \"data_path\": \"LIBERO-Object\", \"eval_data\": \"N/A (training)\", \"gpu\": 2, \"log_path\": \"/root/autodl-tmp/importance_margin_vla_compress/logs/train_openvla_sc_m96_seed42.log\", \"model_name\": \"OpenVLA + VTC M=96\", \"seed\": 42, \"server\": \"westd-41074\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-22T12:21:40.498Z\"}, \"eval_smolvla_official_l2norm_k090_object_seed42\": {\"completed_at\": \"2026-05-21T18:13:38.608Z\", \"conclusion\": \"negative\", \"created_at\": \"2026-05-21T15:43:18.958Z\", \"hypothesis\": \"SmolVLA L2-norm k=0.9 on official checkpoint. Expected ~0% SR given cliff at k=0.95.\", \"metrics\": {\"SR\": 0, \"episodes\": 500, \"note\": \"all 10 tasks 0% SR, mean_steps=280 (max)\"}, \"retry_count\": 0, \"spec\": {\"checkpoint_path\": \"N/A\", \"log_path\": \"cqa1:/root/autodl-tmp/importance_margin_vla_compress/eval_results/\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-22T11:42:34.932Z\"}, \"eval_pi05_random_k03_object_seed43_v4\": {\"completed_at\": \"2026-05-22T11:01:14.704Z\", \"conclusion\": \"success\", \"created_at\": \"2026-05-22T08:36:06.946Z\", \"hypothesis\": \"π0.5 Random k=0.3 Object seed43 v4: v1-v3 均失败。极端压缩率 random pruning，预期 SR 接近 0%。验证 random 在 70% 剪枝下完全崩溃。\", \"metrics\": {\"overall_SR\": 0.322, \"total_episodes\": 500, \"total_successes\": 161}, \"retry_count\": 0, \"spec\": {\"checkpoint_path\": \"N/A (eval only)\", \"checkpoint_source\": \"physical-intelligence/pi0.5\", \"command\": \"eval_pi05_pruning_libero.py --prune_mode random --keep_ratio 0.3 --suite libero_object --seed 43\", \"data_count\": 500, \"data_path\": \"libero_object\", \"eval_data\": \"libero_object\", \"log_path\": \"westd-38929:/root/autodl-tmp/importance_margin_vla_compress/logs/\", \"model_name\": \"pi0.5\", \"seed\": 43, \"server\": \"westd-38929\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-22T11:01:14.704Z\"}, \"eval_pi05_random_k085_object_seed43\": {\"completed_at\": \"2026-05-21T23:16:46.122Z\", \"conclusion\": \"negative\", \"created_at\": \"2026-05-21T22:03:25.605Z\", \"extra\": {\"previous_failure\": {\"conclusion\": \"failed\"}}, \"hypothesis\": \"π0.5 random k=0.85 Object seed43: seed 验证。seed42 v2 正在 westd-38929 跑（早期数据 ~8% SR）。如果 seed43 也崩→确认 cliff 在 k=0.7-0.85 之间。\", \"metrics\": {\"overall_SR\": 0.038, \"total_episodes\": 500, \"total_successes\": 19}, \"parent\": \"eval_pi05_random_k085_object_seed42_v2\", \"retry_count\": 1, \"spec\": {\"checkpoint_path\": \"N/A (eval only)\", \"checkpoint_source\": \"physical-intelligence/pi0.5\", \"command\": \"python eval_pi05_pruning_libero.py --prune_mode random --keep_ratio 0.85 --suite libero_object --n_episodes 500 --seed 43 --gpu 0\", \"data_count\": 500, \"data_path\": \"LIBERO-Object\", \"eval_data\": \"LIBERO-Object 500 episodes\", \"log_path\": \"westd-41074:/root/autodl-tmp/importance_margin_vla_compress/logs/\", \"model_name\": \"pi0.5\", \"seed\": 43, \"server\": \"westd-41074\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-22T11:00:39.360Z\"}, \"eval_pi05_l2norm_k03_spatial_seed43\": {\"completed_at\": \"2026-05-22T11:00:36.736Z\", \"conclusion\": \"success\", \"created_at\": \"2026-05-22T10:56:30.510Z\", \"hypothesis\": \"π0.5 L2norm k=0.3 Spatial seed43: 双种子验证。L2norm 极端压缩下 Spatial 表现。与 random k=0.3 Spatial 配对形成方法对比。\", \"metrics\": {\"overall_SR\": 0.52, \"total_episodes\": 500, \"total_successes\": 260}, \"retry_count\": 0, \"spec\": {\"checkpoint_path\": \"N/A (eval only)\", \"command\": \"python eval_pi05_pruning_libero.py --prune_mode l2norm --keep_ratio 0.3 --suite libero_spatial --n_episodes 500 --seed 43 --gpu 0\", \"data_count\": 500, \"data_path\": \"LIBERO-Spatial\", \"log_path\": \"westd-38929:/root/autodl-tmp/importance_margin_vla_compress/logs/\", \"model_name\": \"pi0.5\", \"seed\": 43, \"server\": \"westd-38929\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-22T11:00:36.736Z\"}, \"eval_pi05_random_k03_spatial_seed43\": {\"completed_at\": \"2026-05-22T11:00:34.089Z\", \"conclusion\": \"success\", \"created_at\": \"2026-05-22T10:56:27.850Z\", \"hypothesis\": \"π0.5 random k=0.3 Spatial seed43: 双种子验证。与 Object seed43 random k=0.3 (32.2%) 配对。确认 random 极端压缩下 Spatial vs Object 的差异。\", \"metrics\": {\"overall_SR\": 0.512, \"total_episodes\": 500, \"total_successes\": 256}, \"retry_count\": 0, \"spec\": {\"checkpoint_path\": \"N/A (eval only)\", \"command\": \"python eval_pi05_pruning_libero.py --prune_mode random --keep_ratio 0.3 --suite libero_spatial --n_episodes 500 --seed 43 --gpu 0\", \"data_count\": 500, \"data_path\": \"LIBERO-Spatial\", \"log_path\": \"westd-38929:/root/autodl-tmp/importance_margin_vla_compress/logs/\", \"model_name\": \"pi0.5\", \"seed\": 43, \"server\": \"westd-38929\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-22T11:00:34.089Z\"}, \"eval_pi05_l2norm_k0925_object_seed43\": {\"completed_at\": \"2026-05-22T09:25:07.539Z\", \"conclusion\": \"killed\", \"created_at\": \"2026-05-22T09:23:17.890Z\", \"hypothesis\": \"L2norm pruning at k=0.925 on pi0.5 retains most important vision tokens for libero_object tasks, maintaining performance close to unpruned baseline while removing 7.5% of tokens.\", \"metrics\": {\"overall_SR\": 0.984, \"total_episodes\": 500, \"total_successes\": 492}, \"retry_count\": 0, \"spec\": {\"checkpoint_path\": \"N/A (eval only)\", \"checkpoint_source\": \"/root/autodl-tmp/pi05_libero_finetuned\", \"command\": \"CUDA_VISIBLE_DEVICES=0 python -u eval_pi05_pruning_libero.py --prune_mode l2norm --keep_ratio 0.925 --suite libero_object --n_episodes 500 --seed 43 --gpu 0\", \"data_count\": 500, \"data_path\": \"/root/autodl-tmp/importance_margin_vla_compress\", \"eval_data\": \"libero_object\", \"log_path\": \"westd-41074:/root/autodl-tmp/importance_margin_vla_compress/eval_results/pi05_l2norm_k0.925_libero_object_seed43.json\", \"model_name\": \"pi05_libero_finetuned\", \"seed\": 43, \"server\": \"westd-27271\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-22T09:33:31.493Z\"}, \"eval_pi05_l2norm_k095_object_seed43\": {\"completed_at\": \"2026-05-22T09:25:10.106Z\", \"conclusion\": \"success\", \"created_at\": \"2026-05-22T08:35:59.676Z\", \"hypothesis\": \"π0.5 L2norm k=0.95 Object seed43: 双种子验证。seed42 Object l2norm k=0.95 未测。Spatial seed42=98.0%, seed43=98.0%。预期 Object 也在 plateau 区间 ~95-99%。\", \"metrics\": {\"overall_SR\": 0.984, \"total_episodes\": 500, \"total_successes\": 492}, \"retry_count\": 0, \"spec\": {\"checkpoint_path\": \"/root/autodl-tmp/pi05_libero_finetuned\", \"checkpoint_source\": \"pi0-fast-pruned-l2norm-k095\", \"command\": \"eval_pi05_pruning_libero.py --prune_mode l2norm --keep_ratio 0.95 --suite libero_object --seed 43\", \"data_count\": 500, \"data_path\": \"libero_object\", \"eval_data\": \"libero_object\", \"log_path\": \"/root/autodl-tmp/importance_margin_vla_compress/eval_results/pi05_l2norm_k0.95_libero_object_seed43.json\", \"model_name\": \"pi0-fast\", \"seed\": 43, \"server\": \"cqa1-33015\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-22T09:25:54.954Z\"}, \"eval_pi05_l2norm_k07_spatial_seed43\": {\"completed_at\": \"2026-05-22T09:14:48.890Z\", \"conclusion\": \"success\", \"created_at\": \"2026-05-22T06:39:24.566Z\", \"hypothesis\": \"π0.5 L2norm k=0.7 Spatial seed43: 双种子验证。seed42=67.0%。L2norm k=0.7 Spatial 在 V-shape 恢复点的跨 seed 一致性。\", \"metrics\": {\"overall_SR\": 0.684, \"total_episodes\": 500, \"total_successes\": 342}, \"retry_count\": 0, \"spec\": {\"checkpoint_path\": \"N/A (eval only)\", \"command\": \"eval_pi05_pruning_libero.py --prune_mode l2norm --keep_ratio 0.7 --suite libero_spatial --n_episodes 50 --seed 43 --gpu 1\", \"data_count\": 500, \"data_path\": \"libero_spatial\", \"gpu\": [\"cuda:1\"], \"log_path\": \"westd-27271:/root/autodl-tmp/importance_margin_vla_compress/logs/eval_pi05_l2norm_k07_spatial_seed43.log\", \"model_name\": \"pi05_libero_finetuned\", \"pid\": \"119442\", \"seed\": 43, \"server\": \"westd-27271\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-22T09:14:48.890Z\"}, \"eval_pi05_random_k07_spatial_seed43\": {\"completed_at\": \"2026-05-22T09:14:46.323Z\", \"conclusion\": \"success\", \"created_at\": \"2026-05-22T06:39:23.035Z\", \"hypothesis\": \"π0.5 random k=0.7 Spatial seed43: 双种子验证。seed42 Spatial random k=0.7 未测。Object random k=0.7=75.5%。Spatial 上 random cliff 更温和，k=0.7 预期 >Object。\", \"metrics\": {\"overall_SR\": 0.738, \"total_episodes\": 500, \"total_successes\": 369}, \"retry_count\": 0, \"spec\": {\"checkpoint_path\": \"N/A (eval only)\", \"command\": \"eval_pi05_pruning_libero.py --prune_mode random --keep_ratio 0.7 --suite libero_spatial --n_episodes 50 --seed 43 --gpu 0\", \"data_count\": 500, \"data_path\": \"libero_spatial\", \"gpu\": [\"cuda:0\"], \"log_path\": \"westd-27271:/root/autodl-tmp/importance_margin_vla_compress/logs/eval_pi05_random_k07_spatial_seed43.log\", \"model_name\": \"pi05_libero_finetuned\", \"pid\": \"119106\", \"seed\": 43, \"server\": \"westd-27271\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-22T09:14:46.323Z\"}, \"eval_smart_compress_m32_official\": {\"completed_at\": \"2026-05-19T11:08:55.783Z\", \"conclusion\": \"killed\", \"created_at\": \"2026-05-19T10:06:45.019Z\", \"hypothesis\": \"Smart Compress M=32 trained from official SmolVLA checkpoint (baseline SR=59.2%) eval on LIBERO-Object (50 episodes/task). If official checkpoint yields higher SR than smolvla_base M=32 (seed42=61.6%), confirms stronger pretrained features improve compression performance.\", \"metrics\": {\"CI_95_wilson\": \"49.0-57.7\", \"SR\": 53.4, \"episodes\": 500, \"per_task_SR\": [64, 48, 56, 46, 46, 28, 78, 42, 66, 60]}, \"parent\": \"train_smart_compress_m32_official\", \"retry_count\": 0, \"spec\": {\"checkpoint_path\": \"/root/autodl-tmp/importance_margin_vla_compress/checkpoints/smart_compress_m32_official/checkpoint.pt\", \"checkpoint_source\": \"checkpoints/smart_compress_m32_official/checkpoint.pt\", \"command\": \"CUDA_VISIBLE_DEVICES=3 python eval_smart_compress_libero.py --n_queries 32 --checkpoint_path checkpoints/smart_compress_m32_official/checkpoint.pt --suite libero_object --num_episodes 50 --gpu 0 --seed 42\", \"data_count\": 50, \"data_path\": \"libero_object\", \"eval_data\": \"libero_object (50 episodes/task)\", \"gpu_ids\": [\"cuda:3\"], \"log_path\": \"/root/autodl-tmp/importance_margin_vla_compress/logs/eval_smart_compress_m32_official.log\", \"model_name\": \"smolvla_official + VisionTokenCompressor(M=32)\", \"pid\": 160116, \"seed\": 42, \"server\": \"cqa1-33015\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-22T09:09:34.573Z\"}, \"eval_pi05_random_k05_object_seed43\": {\"completed_at\": \"2026-05-21T14:48:49.642Z\", \"conclusion\": \"success\", \"created_at\": \"2026-05-21T09:55:41.090Z\", \"hypothesis\": \"π0.5 Random k=0.5 Object seed43: 双种子验证。Random k=0.5 deep pruning on Object suite。预期 SR 很低（~5-15%），验证 random 在高压缩率下的崩溃模式。\", \"metrics\": {\"elapsed_min\": 82.3, \"success_rate\": 68.4, \"total_episodes\": 500, \"total_successes\": 342}, \"parent\": \"eval_pi05_random_k05_object_seed42\", \"retry_count\": 0, \"spec\": {\"checkpoint_path\": \"eval_results/pi05_random_k0.50_libero_object.json\", \"checkpoint_source\": \"/root/autodl-tmp/pi05_libero_finetuned\", \"command\": \"python -u eval_pi05_pruning_libero.py --prune_mode random --keep_ratio 0.5 --suite libero_object --seed 43 --n_episodes 50 --gpu 1\", \"data_count\": 50, \"data_path\": \"/root/autodl-tmp/importance_margin_vla_compress\", \"eval_data\": \"libero_object\", \"log_path\": \"logs/eval_pi05_random_k05_object_seed43.log\", \"model_name\": \"pi05_libero_finetuned\", \"seed\": 43, \"server\": \"westd-41074\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-22T08:36:05.172Z\"}, \"eval_pi05_random_k07_object_seed43\": {\"completed_at\": \"2026-05-21T14:48:47.757Z\", \"conclusion\": \"success\", \"created_at\": \"2026-05-21T13:16:57.776Z\", \"hypothesis\": \"π0.5 Random k=0.7 Object seed43: 双种子验证。seed42 Object random k=0.7=52.6% (OpenVLA)。Pi05 版本尚未测试。Random 在 cliff zone，预期 ~30-60%。\", \"metrics\": {\"elapsed_min\": 86.9, \"success_rate\": 73.8, \"total_episodes\": 500, \"total_successes\": 369}, \"parent\": \"eval_pi05_random_k07_object_seed42\", \"retry_count\": 0, \"spec\": {\"checkpoint_path\": \"eval_results/pi05_random_k0.70_libero_object_seed43.json\", \"checkpoint_source\": \"/root/autodl-tmp/pi05_libero_finetuned\", \"command\": \"python -u eval_pi05_pruning_libero.py --prune_mode random --keep_ratio 0.7 --suite libero_object --n_episodes 50 --seed 43 --gpu 0\", \"data_count\": 500, \"data_path\": \"libero_object\", \"eval_data\": \"libero_object\", \"gpu_id\": 0, \"log_path\": \"logs/eval_pi05_random_k07_object_seed43.log\", \"model_name\": \"pi05\", \"seed\": 43, \"server\": \"westd-41074\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-22T08:36:02.987Z\"}, \"eval_pi05_l2norm_k085_object_seed43\": {\"completed_at\": \"2026-05-22T08:34:54.160Z\", \"conclusion\": \"success\", \"created_at\": \"2026-05-22T05:07:11.332Z\", \"hypothesis\": \"π0.5 L2norm k=0.85 Object seed43: L2norm plateau 双种子验证。seed42=98.0%。验证 L2norm 在 cliff zone (random=5.0%) 保持 ~98% 的跨 seed 稳定性。\", \"metrics\": {\"overall_SR\": 0.984, \"per_task\": {\"T0\": 1, \"T1\": 1, \"T2\": 1, \"T3\": 0.98, \"T4\": 1, \"T5\": 0.96, \"T6\": 0.98, \"T7\": 0.92, \"T8\": 1, \"T9\": 1}, \"total_episodes\": 500, \"total_successes\": 492}, \"retry_count\": 0, \"spec\": {\"account\": \"root\", \"backend\": \"tmux\", \"checkpoint_path\": \"N/A-eval-only\", \"checkpoint_source\": \"pi0-fast-pruned-l2norm-k085\", \"command\": \"eval_pi05_pruning_libero.py --prune_mode l2norm --keep_ratio 0.85 --suite libero_object --seed 43\", \"data_count\": 500, \"data_path\": \"libero_object\", \"eval_data\": \"libero_object\", \"gpu\": [\"cuda:2\"], \"gpu_hours\": 3.46, \"log_path\": \"~/runs/importance_margin_vla_compress/eval_pi05_l2norm_k085_object_seed43.log\", \"model_name\": \"pi0-fast\", \"pid\": \"562137\", \"seed\": 43, \"server\": \"westd-41074\", \"submitted_at\": \"2026-05-22T05:07:14.142Z\", \"submitted_via\": \"submit_training_job\", \"wall_clock_seconds\": 12460.0}, \"status\": \"DONE\", \"updated_at\": \"2026-05-22T08:34:54.160Z\"}, \"eval_pi05_l2norm_k09_spatial_seed43\": {\"completed_at\": \"2026-05-22T08:05:09.887Z\", \"conclusion\": \"success\", \"created_at\": \"2026-05-22T04:19:57.910Z\", \"hypothesis\": \"π0.5 L2norm k=0.9 Spatial seed43: seed42=95.0%。双种子验证 L2norm 在 Spatial 上的 plateau 特性——如果 seed43 也 >90% → 确认 L2norm 跨种子稳定。\", \"metrics\": {\"overall_SR\": 0.956, \"total_episodes\": 500, \"total_successes\": 478}, \"retry_count\": 0, \"spec\": {\"account\": \"root\", \"backend\": \"tmux\", \"checkpoint_path\": \"N/A (eval only)\", \"checkpoint_source\": \"physical-intelligence/pi0.5\", \"command\": \"python -u eval_pi05_pruning_libero.py --prune_mode l2norm --keep_ratio 0.9 --suite libero_spatial --n_episodes 50 --seed 43 --gpu 3\", \"data_count\": 500, \"data_path\": \"LIBERO-Spatial\", \"eval_data\": \"LIBERO-Spatial 10 tasks x 50 episodes\", \"gpu\": 3, \"gpu_hours\": 3.75, \"log_path\": \"~/runs/importance_margin_vla_compress/eval_pi05_l2norm_k09_spatial_seed43.log\", \"model_name\": \"pi0.5\", \"pid\": 6087, \"seed\": 43, \"server\": \"cqa1-33015\", \"submitted_at\": \"2026-05-22T04:20:17.207Z\", \"submitted_via\": \"submit_training_job\", \"wall_clock_seconds\": 13492.7}, \"status\": \"DONE\", \"updated_at\": \"2026-05-22T08:05:09.887Z\"}, \"eval_pi05_random_k09_spatial_seed43\": {\"completed_at\": \"2026-05-22T08:05:07.080Z\", \"conclusion\": \"success\", \"created_at\": \"2026-05-22T04:19:54.793Z\", \"hypothesis\": \"π0.5 random k=0.9 Spatial seed43: seed42=54.6% 的双种子验证。random k=0.9 是 Spatial cliff 关键点（Object 上 k=0.9 已完全崩溃至 ~5%），seed43 验证 Spatial 的 cliff 是否更平缓。\", \"metrics\": {\"overall_SR\": 0.536, \"total_episodes\": 500, \"total_successes\": 268}, \"retry_count\": 0, \"spec\": {\"account\": \"root\", \"backend\": \"tmux\", \"checkpoint_path\": \"N/A (eval only)\", \"checkpoint_source\": \"physical-intelligence/pi0.5\", \"command\": \"python -u eval_pi05_pruning_libero.py --prune_mode random --keep_ratio 0.9 --suite libero_spatial --n_episodes 50 --seed 43 --gpu 1\", \"data_count\": 500, \"data_path\": \"LIBERO-Spatial\", \"eval_data\": \"LIBERO-Spatial 10 tasks x 50 episodes\", \"gpu\": 1, \"gpu_hours\": 3.75, \"log_path\": \"~/runs/importance_margin_vla_compress/eval_pi05_random_k09_spatial_seed43.log\", \"model_name\": \"pi0.5\", \"pid\": 5866, \"seed\": 43, \"server\": \"cqa1-33015\", \"submitted_at\": \"2026-05-22T04:20:11.634Z\", \"submitted_via\": \"submit_training_job\", \"wall_clock_seconds\": 13495.4}, \"status\": \"DONE\", \"updated_at\": \"2026-05-22T08:05:07.080Z\"}, \"eval_pi05_random_k0925_spatial_seed43\": {\"completed_at\": \"2026-05-22T08:05:01.773Z\", \"conclusion\": \"success\", \"created_at\": \"2026-05-22T04:19:53.394Z\", \"hypothesis\": \"π0.5 random k=0.925 Spatial seed43: seed42=54.6% 的双种子验证。如果 seed43 也在 50-60% 范围 → 确认 Spatial random k=0.9 的 cliff 位置，为跨 suite cliff 对比提供 error bar。\", \"metrics\": {\"overall_SR\": 0.578, \"total_episodes\": 500, \"total_successes\": 289}, \"retry_count\": 0, \"spec\": {\"account\": \"root\", \"backend\": \"tmux\", \"checkpoint_path\": \"N/A (eval only)\", \"checkpoint_source\": \"physical-intelligence/pi0.5\", \"command\": \"python -u eval_pi05_pruning_libero.py --prune_mode random --keep_ratio 0.925 --suite libero_spatial --n_episodes 50 --seed 43 --gpu 0\", \"data_count\": 500, \"data_path\": \"LIBERO-Spatial\", \"eval_data\": \"LIBERO-Spatial 10 tasks x 50 episodes\", \"gpu\": 0, \"gpu_hours\": 3.75, \"log_path\": \"~/runs/importance_margin_vla_compress/eval_pi05_random_k0925_spatial_seed43.log\", \"model_name\": \"pi0.5\", \"pid\": 5786, \"seed\": 43, \"server\": \"cqa1-33015\", \"submitted_at\": \"2026-05-22T04:20:08.640Z\", \"submitted_via\": \"submit_training_job\", \"wall_clock_seconds\": 13493.1}, \"status\": \"DONE\", \"updated_at\": \"2026-05-22T08:05:01.773Z\"}, \"eval_openvla_l2norm_k05_object_seed42_v5\": {\"completed_at\": \"2026-05-22T08:03:04.830Z\", \"conclusion\": \"success\", \"created_at\": \"2026-05-22T02:36:30.442Z\", \"hypothesis\": \"OpenVLA L2norm k=0.5 Object seed42 v5: D132 crossover evidence — OpenVLA (MLP projector, CV=0.215) at k=0.5 shows L2norm≈random. v4 因 westd-38929 GPU 缩减被 kill。Table 3 关键数据点。\", \"metrics\": {\"overall_SR\": 0.392, \"per_task\": {\"T0\": 0.56, \"T1\": 0.14, \"T2\": 0.38, \"T3\": 0.32, \"T4\": 0.7, \"T5\": 0.32, \"T6\": 0.12, \"T7\": 0.5, \"T8\": 0.44, \"T9\": 0.44}, \"total_episodes\": 500, \"total_successes\": 196}, \"retry_count\": 0, \"spec\": {\"account\": \"root\", \"backend\": \"tmux\", \"checkpoint_path\": \"N/A (eval only)\", \"checkpoint_source\": \"openvla/openvla-7b\", \"command\": \"CUDA_VISIBLE_DEVICES=3 HF_HUB_OFFLINE=1 MUJOCO_GL=egl python -u eval_openvla_l2norm_libero.py --mode l2norm_prune --k_ratio 0.5 --suite libero_object --num_episodes 50 --seed 42\", \"data_count\": 500, \"data_path\": \"LIBERO-Object\", \"eval_data\": \"LIBERO-Object 500 episodes\", \"gpu\": \"cuda:3\", \"gpu_hours\": 5.35, \"log_path\": \"~/runs/importance_margin_vla_compress/eval_openvla_l2norm_k05_object_seed42_v5.log\", \"model_name\": \"OpenVLA\", \"pid\": 311261, \"seed\": 42, \"server\": \"westd-38929\", \"submitted_at\": \"2026-05-22T02:42:21.697Z\", \"submitted_via\": \"submit_training_job\", \"wall_clock_seconds\": 19243.1}, \"status\": \"DONE\", \"updated_at\": \"2026-05-22T08:03:04.830Z\"}, \"eval_pi05_random_k095_spatial_seed43\": {\"completed_at\": \"2026-05-22T06:40:45.709Z\", \"conclusion\": \"success\", \"created_at\": \"2026-05-22T04:30:46.725Z\", \"hypothesis\": \"π0.5 random k=0.95 Spatial seed43: seed42=84.4%。双种子验证 random k=0.95 在 Spatial 上的表现稳定性。\", \"metrics\": {\"overall_SR\": 0.768, \"per_task\": {\"T0\": 1, \"T1\": 0.94, \"T2\": 1, \"T3\": 0.6, \"T4\": 0.36, \"T5\": 0.76, \"T6\": 0.9, \"T7\": 0.74, \"T8\": 1, \"T9\": 0.38}, \"total_episodes\": 500, \"total_successes\": 384}, \"retry_count\": 0, \"spec\": {\"account\": \"root\", \"backend\": \"tmux\", \"checkpoint_path\": \"/root/autodl-tmp/importance_margin_vla_compress/eval_results/pi05_random_k0.95_libero_spatial_seed43.json\", \"command\": \"eval_pi05_pruning_libero.py --prune_mode random --keep_ratio 0.95 --suite libero_spatial --n_episodes 50 --seed 43 --gpu 0\", \"data_count\": 500, \"data_path\": \"libero_spatial\", \"gpu\": [\"cuda:0\"], \"gpu_hours\": 2.04, \"log_path\": \"~/runs/importance_margin_vla_compress/eval_pi05_random_k095_spatial_seed43.log\", \"model_name\": \"pi05_libero_finetuned\", \"pid\": \"9465\", \"seed\": 43, \"server\": \"westd-27271\", \"submitted_at\": \"2026-05-22T04:38:24.912Z\", \"submitted_via\": \"submit_training_job\", \"wall_clock_seconds\": 7340.8}, \"status\": \"DONE\", \"updated_at\": \"2026-05-22T07:01:42.225Z\"}, \"eval_pi05_random_k03_object_seed43_v2\": {\"completed_at\": \"2026-05-22T05:07:09.054Z\", \"conclusion\": \"killed\", \"created_at\": \"2026-05-21T23:32:50.404Z\", \"hypothesis\": \"π0.5 random k=0.3 Object seed43 v2: seed 验证 (v1 failed due to cqa1 env mismatch). seed42=36.4%。确认 random k=0.3 的 SR 在 seed 间可重复。\", \"parent\": \"eval_pi05_random_k03_object_seed43\", \"retry_count\": 0, \"spec\": {\"checkpoint_path\": \"N/A\", \"checkpoint_source\": \"/root/autodl-tmp/pi05_libero_finetuned\", \"command\": \"CUDA_VISIBLE_DEVICES=2 HF_HUB_OFFLINE=1 HF_HOME=/root/autodl-tmp/.hf_cache MUJOCO_GL=egl python -u eval_pi05_pruning_libero.py --prune_mode random --keep_ratio 0.3 --suite libero_object --n_episodes 50 --seed 43 --gpu 0\", \"data_count\": 500, \"data_path\": \"/root/autodl-tmp/pi05_libero_finetuned\", \"eval_data\": \"libero_object\", \"gpu_id\": 2, \"log_path\": \"N/A\", \"model_name\": \"pi05\", \"pid\": 806010, \"seed\": 43, \"server\": \"cqa1-33015\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-22T05:07:09.054Z\"}, \"eval_pi05_random_k085_object_seed43_v2\": {\"completed_at\": \"2026-05-22T05:07:06.673Z\", \"conclusion\": \"killed\", \"created_at\": \"2026-05-21T23:32:45.558Z\", \"hypothesis\": \"π0.5 random k=0.85 Object seed43 v2: cliff boundary seed 验证 (v1 failed due to cqa1 env mismatch). seed42 v2 在 westd-38929 显示 ~4.4% SR，确认 cliff 在 k=0.7-0.85 之间。\", \"parent\": \"eval_pi05_random_k085_object_seed43\", \"retry_count\": 0, \"spec\": {\"checkpoint_path\": \"N/A\", \"checkpoint_source\": \"/root/autodl-tmp/pi05_libero_finetuned\", \"command\": \"CUDA_VISIBLE_DEVICES=0 HF_HUB_OFFLINE=1 HF_HOME=/root/autodl-tmp/.hf_cache MUJOCO_GL=egl python -u eval_pi05_pruning_libero.py --prune_mode random --keep_ratio 0.85 --suite libero_object --n_episodes 50 --seed 43 --gpu 0\", \"data_count\": 500, \"data_path\": \"/root/autodl-tmp/pi05_libero_finetuned\", \"eval_data\": \"libero_object\", \"gpu_id\": 0, \"log_path\": \"N/A\", \"model_name\": \"pi05\", \"pid\": 805698, \"seed\": 43, \"server\": \"cqa1-33015\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-22T05:07:06.673Z\"}, \"eval_pi05_random_k095_spatial_seed42_v2\": {\"completed_at\": \"2026-05-22T05:07:04.203Z\", \"conclusion\": \"killed\", \"created_at\": \"2026-05-22T02:16:01.871Z\", \"hypothesis\": \"π0.5 random k=0.95 Spatial seed42 v2: v1 因 n_episodes=500 bug 导致 IndexError。Object 上 random k=0.95=71.1% (dual seed mean). Spatial baseline=97.2%, 如果 Spatial random k=0.95 也 >70% → cliff 强度跨 suite 一致; 如果 >90% → Spatial 更 tolerant to random pruning.\", \"parent\": \"eval_pi05_random_k095_spatial_seed42\", \"retry_count\": 0, \"spec\": {\"checkpoint_path\": \"N/A\", \"checkpoint_source\": \"pi05_libero_finetuned\", \"command\": \"HF_HUB_OFFLINE=1 MUJOCO_GL=egl python -u eval_pi05_pruning_libero.py --prune_mode random --keep_ratio 0.95 --suite libero_spatial --n_episodes 50 --seed 42 --gpu 0\", \"data_count\": 500, \"data_path\": \"libero_spatial\", \"eval_data\": \"libero_spatial\", \"gpu\": \"cuda:0\", \"log_path\": \"~/runs/importance_margin_vla_compress/eval_pi05_random_k095_spatial_seed42_v2.log\", \"model_name\": \"pi05\", \"pid\": 943114, \"seed\": 42, \"server\": \"westd-41074\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-22T05:07:04.203Z\"}, \"eval_pi05_l2norm_k07_object_seed43_v3\": {\"completed_at\": \"2026-05-22T05:06:45.229Z\", \"conclusion\": \"success\", \"created_at\": \"2026-05-21T23:50:24.243Z\", \"hypothesis\": \"π0.5 L2norm k=0.7 Object seed43 v3: V-shape 恢复点 seed 验证。seed42=55.0%, westd-41074 seed43=57.8%。cqa1 环境修复后在 westd-38929 重跑，验证 V-shape recovery (k=0.7) 跨 seed 一致性。\", \"metrics\": {\"success_rate_mean\": 57.2}, \"parent\": \"eval_pi05_l2norm_k07_object_seed43_v2\", \"retry_count\": 0, \"spec\": {\"account\": \"root\", \"backend\": \"tmux\", \"checkpoint_path\": \"N/A\", \"checkpoint_source\": \"physical-intelligence/pi0.5\", \"command\": \"HF_HUB_OFFLINE=1 MUJOCO_GL=egl python -u eval_pi05_pruning_libero.py --prune_mode l2norm --keep_ratio 0.7 --suite libero_object --n_episodes 50 --seed 43 --gpu 0\", \"data_count\": 500, \"data_path\": \"LIBERO-Object\", \"eval_data\": \"LIBERO-Object 500 episodes\", \"gpu\": \"cuda:2\", \"gpu_hours\": 2.19, \"log_path\": \"~/runs/importance_margin_vla_compress/eval_pi05_l2norm_k07_object_seed43_v3.log\", \"model_name\": \"pi0.5\", \"pid\": 348884, \"seed\": 43, \"server\": \"westd-38929\", \"submitted_at\": \"2026-05-22T02:55:24.463Z\", \"submitted_via\": \"submit_training_job\", \"wall_clock_seconds\": 7880.8}, \"status\": \"DONE\", \"updated_at\": \"2026-05-22T05:06:45.229Z\"}, \"eval_pi05_random_k095_spatial_seed42_v4\": {\"completed_at\": \"2026-05-22T04:46:42.361Z\", \"conclusion\": \"success\", \"created_at\": \"2026-05-22T03:14:20.916Z\", \"hypothesis\": \"π0.5 random k=0.95 Spatial seed42 v4: v2 僵尸(EXIT_CODE=129)，v3 冗余被kill。Object k=0.95=71.1%。Spatial baseline=97.2%。Spatial 表最后2个缺失数据点之一。\", \"metrics\": {\"success_rate_mean\": 76.4}, \"parent\": \"eval_pi05_random_k095_spatial_seed42_v2\", \"retry_count\": 0, \"spec\": {\"account\": \"root\", \"backend\": \"tmux\", \"checkpoint_path\": \"N/A\", \"checkpoint_source\": \"physical-intelligence/pi0.5\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/importance_margin_vla_compress && HF_HUB_OFFLINE=1 MUJOCO_GL=egl python -u eval_pi05_pruning_libero.py --prune_mode random --keep_ratio 0.95 --suite libero_spatial --n_episodes 50 --seed 42 --gpu 0\\\"\", \"data_count\": 500, \"data_path\": \"LIBERO-Spatial\", \"eval_data\": \"LIBERO-Spatial 500 episodes\", \"gpu\": [\"cuda:0\"], \"gpu_hours\": 1.53, \"log_path\": \"~/runs/importance_margin_vla_compress/eval_pi05_random_k095_spatial_seed42_v4.log\", \"model_name\": \"pi0.5\", \"pid\": \"13526\", \"seed\": 42, \"server\": \"westd-41074\", \"submitted_at\": \"2026-05-22T03:14:36.852Z\", \"submitted_via\": \"submit_training_job\", \"wall_clock_seconds\": 5525.5}, \"status\": \"DONE\", \"updated_at\": \"2026-05-22T04:46:44.657Z\"}, \"eval_pi05_random_k095_object_seed43\": {\"completed_at\": \"2026-05-21T23:51:48.784Z\", \"conclusion\": \"success\", \"created_at\": \"2026-05-21T22:13:38.768Z\", \"extra\": {\"hook_events\": [{\"action\": \"agent\", \"event\": \"on_failed\", \"ts\": \"2026-05-21T23:51:58.512612+00:00\"}]}, \"failure_reason\": \"process dead 5× with no sentinel/W&B — auto-resolved as failed\", \"hypothesis\": \"π0.5 random k=0.95 Object seed43: cliff 入口点双种子验证。seed42=71.1%。k=0.95 是 cliff 的起始位置（k=0.925=28.8% 急剧下降），error bar 对论文 cliff profile figure 至关重要。\", \"metrics\": {\"elapsed_min\": 85.5, \"per_task_sr\": {\"T0_alphabet_soup\": 0.7, \"T1_cream_cheese\": 0.9, \"T2_salad_dressing\": 0.78, \"T3_bbq_sauce\": 0.66, \"T4_ketchup\": 0.54, \"T5_tomato_sauce\": 0.8, \"T6_butter\": 0.82, \"T7_milk\": 0.66, \"T8_chocolate_pudding\": 0.78, \"T9_orange_juice\": 0.64}, \"success_rate\": 0.728, \"total_episodes\": 500, \"total_successes\": 364}, \"parent\": \"eval_pi05_random_k095_object_seed42_v2\", \"reproduce\": {\"finished_at\": \"2026-05-21T23:51:42.370Z\"}, \"retry_count\": 0, \"spec\": {\"account\": \"root\", \"backend\": \"tmux\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/importance_margin_vla_compress && HF_HUB_OFFLINE=1 MUJOCO_GL=egl python -u eval_pi05_pruning_libero.py --prune_mode random --keep_ratio 0.95 --suite libero_object --n_episodes 50 --seed 43 --gpu 0\\\"\", \"gpu\": [\"cuda:1\"], \"log_path\": \"~/runs/importance_margin_vla_compress/eval_pi05_random_k095_object_seed43.log\", \"pid\": \"121024\", \"server\": \"westd-41074\", \"submitted_at\": \"2026-05-22T04:44:41.724Z\", \"submitted_via\": \"submit_training_job\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-22T04:44:42.523Z\"}, \"eval_pi05_random_k085_object_seed43_v3\": {\"completed_at\": \"2026-05-22T04:36:51.658Z\", \"conclusion\": \"negative\", \"created_at\": \"2026-05-22T02:16:03.484Z\", \"hypothesis\": \"π0.5 random k=0.85 Object seed43 v3: 重部署。seed42=5.0%。验证 random k=0.85 cliff 深度在 seed43 上的可重复性。\", \"metrics\": {\"success_rate_mean\": 3.8}, \"retry_count\": 0, \"spec\": {\"account\": \"root\", \"backend\": \"tmux\", \"checkpoint_path\": \"N/A\", \"checkpoint_source\": \"pi05_libero_finetuned\", \"command\": \"HF_HUB_OFFLINE=1 MUJOCO_GL=egl python -u eval_pi05_pruning_libero.py --prune_mode random --keep_ratio 0.85 --suite libero_object --n_episodes 50 --seed 43 --gpu 0\", \"data_count\": 500, \"data_path\": \"libero_object\", \"eval_data\": \"libero_object\", \"gpu\": \"cuda:1\", \"gpu_hours\": 2.34, \"log_path\": \"~/runs/importance_margin_vla_compress/eval_pi05_random_k085_object_seed43_v3.log\", \"model_name\": \"pi05\", \"pid\": 922934, \"seed\": 43, \"server\": \"westd-41074\", \"submitted_at\": \"2026-05-22T02:16:19.470Z\", \"submitted_via\": \"submit_training_job\", \"wall_clock_seconds\": 8432.2}, \"status\": \"DONE\", \"updated_at\": \"2026-05-22T04:36:51.658Z\"}, \"eval_pi05_l2norm_k0925_object_seed42\": {\"completed_at\": \"2026-05-22T01:52:52.551Z\", \"conclusion\": \"success\", \"created_at\": \"2026-05-21T23:04:09.094Z\", \"extra\": {\"hook_events\": [{\"action\": \"agent\", \"event\": \"on_complete\", \"ts\": \"2026-05-22T00:04:35.419712+00:00\"}]}, \"hypothesis\": \"π0.5 L2norm k=0.925 Object seed42: L2norm 在 cliff zone 的精细数据点。k=0.95=98.2%, k=0.9=98.2%, k=0.85=98.0%。k=0.925 预计 ~99%，量化 L2norm plateau 在 random cliff zone 内的稳定性。与 random k=0.925=28.8% 形成对比。\", \"metrics\": {\"n_episodes\": 500, \"per_task\": {\"T0_alphabet_soup\": 98, \"T1_cream_cheese\": 98, \"T2_salad_dressing\": 96, \"T3_bbq_sauce\": 100, \"T4_ketchup\": 100, \"T5_tomato_sauce\": 100, \"T6_butter\": 100, \"T7_milk\": 100, \"T8_chocolate_pudding\": 100, \"T9_orange_juice\": 100}, \"success_rate\": 99.2, \"successes\": 496}, \"parent\": \"eval_pi05_l2norm_k09_object_seed42_v2\", \"reproduce\": {\"finished_at\": \"2026-05-22T00:04:27.512Z\"}, \"retry_count\": 0, \"spec\": {\"checkpoint_path\": \"N/A-eval\", \"log_path\": \"~/runs/importance_margin_vla_compress/eval_pi05_l2norm_k0925_object_seed42.log\", \"results_json\": \"/root/autodl-tmp/importance_margin_vla_compress/eval_results/pi05_l2norm_k0.93_libero_object_seed42.json\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-22T03:19:47.031Z\"}, \"eval_pi05_random_k095_spatial_seed42_v3\": {\"completed_at\": \"2026-05-22T03:14:18.422Z\", \"conclusion\": \"killed\", \"created_at\": \"2026-05-22T02:36:27.524Z\", \"hypothesis\": \"π0.5 random k=0.95 Spatial seed42 v3: westd-38929 备份部署。Object 上 random k=0.95=71.1% (dual seed mean)。Spatial baseline=97.2%。如果 Spatial random k=0.95 也 >70% → cliff 强度跨 suite 一致; 如果 >90% → Spatial 更 tolerant to random pruning。\", \"retry_count\": 0, \"spec\": {\"account\": \"root\", \"backend\": \"tmux\", \"checkpoint_path\": \"N/A\", \"checkpoint_source\": \"physical-intelligence/pi0.5\", \"command\": \"HF_HUB_OFFLINE=1 MUJOCO_GL=egl python -u eval_pi05_pruning_libero.py --prune_mode random --keep_ratio 0.95 --suite libero_spatial --n_episodes 50 --seed 42 --gpu 0\", \"data_count\": 500, \"data_path\": \"LIBERO-Spatial\", \"eval_data\": \"LIBERO-Spatial 500 episodes\", \"gpu\": \"cuda:2\", \"gpu_hours\": 0.62, \"log_path\": \"~/runs/importance_margin_vla_compress/eval_pi05_random_k095_spatial_seed42_v3.log\", \"model_name\": \"pi0.5\", \"pid\": 293413, \"seed\": 42, \"server\": \"westd-38929\", \"submitted_at\": \"2026-05-22T02:36:56.714Z\", \"submitted_via\": \"submit_training_job\", \"wall_clock_seconds\": 2241.7}, \"status\": \"DONE\", \"updated_at\": \"2026-05-22T03:14:18.422Z\"}, \"eval_pi05_l2norm_k095_spatial_seed42_v2\": {\"completed_at\": \"2026-05-22T03:14:15.787Z\", \"conclusion\": \"killed\", \"created_at\": \"2026-05-22T02:36:21.914Z\", \"hypothesis\": \"π0.5 L2norm k=0.95 Spatial seed42 v2: v1 因缺少 HF_HUB_OFFLINE=1 导致 Network unreachable 崩溃。Object 上 L2norm k=0.95=98.2%。如果 Spatial k=0.95 也 >90% → L2norm cliff immunity 跨 suite 一致。Spatial baseline=97.2%。\", \"parent\": \"eval_pi05_l2norm_k095_spatial_seed42\", \"retry_count\": 0, \"spec\": {\"account\": \"root\", \"backend\": \"tmux\", \"checkpoint_path\": \"N/A\", \"checkpoint_source\": \"physical-intelligence/pi0.5\", \"command\": \"HF_HUB_OFFLINE=1 MUJOCO_GL=egl python -u eval_pi05_pruning_libero.py --prune_mode l2norm --keep_ratio 0.95 --suite libero_spatial --n_episodes 50 --seed 42 --gpu 0\", \"data_count\": 500, \"data_path\": \"LIBERO-Spatial\", \"eval_data\": \"LIBERO-Spatial 500 episodes\", \"gpu\": \"cuda:1\", \"gpu_hours\": 0.62, \"log_path\": \"~/runs/importance_margin_vla_compress/eval_pi05_l2norm_k095_spatial_seed42_v2.log\", \"model_name\": \"pi0.5\", \"pid\": 293268, \"seed\": 42, \"server\": \"westd-38929\", \"submitted_at\": \"2026-05-22T02:36:53.790Z\", \"submitted_via\": \"submit_training_job\", \"wall_clock_seconds\": 2242.0}, \"status\": \"DONE\", \"updated_at\": \"2026-05-22T03:14:15.787Z\"}, \"eval_pi05_l2norm_k07_spatial_seed42\": {\"completed_at\": \"2026-05-21T23:14:51.202Z\", \"conclusion\": \"success\", \"created_at\": \"2026-05-21T21:25:05.094Z\", \"extra\": {\"hook_events\": [{\"action\": \"agent\", \"event\": \"on_failed\", \"ts\": \"2026-05-21T23:15:02.991583+00:00\"}]}, \"failure_reason\": \"process dead 5× with no sentinel/W&B — auto-resolved as failed\", \"hypothesis\": \"π0.5 L2norm k=0.7 Spatial seed42: L2norm Spatial 曲线最后缺失点。k=0.85=90.4%, k=0.5=55.6%。如果 k=0.7 在 60-85% 之间 → L2norm 在 Spatial 上也呈现 graceful degradation（非 cliff）。补全 L2norm Spatial 完整曲线。\", \"log_path\": \"logs/eval_pi05_l2norm_k07_spatial_seed42.log\", \"metrics\": {\"duration_min\": 98.8, \"episodes\": 500, \"per_task_sr\": \"10 tasks completed, overall 335/500\", \"success_rate\": 67, \"tasks\": 10}, \"parent\": \"eval_pi05_l2norm_k05_spatial_seed42\", \"reproduce\": {\"finished_at\": \"2026-05-21T23:14:47.829Z\"}, \"retry_count\": 0, \"spec\": {\"checkpoint_path\": \"/root/autodl-tmp/pi05_libero_finetuned\", \"checkpoint_source\": \"eval_pi05_l2norm_k05_spatial_seed42\", \"command\": \"HF_HUB_OFFLINE=1 MUJOCO_GL=egl python -u eval_pi05_pruning_libero.py --prune_mode l2norm --keep_ratio 0.7 --suite libero_spatial --n_episodes 50 --seed 42 --gpu 0\", \"data_count\": 500, \"data_path\": \"LIBERO-Spatial\", \"eval_data\": \"libero_spatial\", \"gpu\": \"cuda:1\", \"log_path\": \"~/runs/importance_margin_vla_compress/eval_pi05_l2norm_k07_spatial_seed42.log\", \"model_name\": \"pi05_libero_finetuned\", \"seed\": 42, \"server\": \"westd-38929\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-22T03:02:44.178Z\"}, \"eval_pi05_l2norm_k09_spatial_seed42\": {\"checkpoint_path\": \"/root/autodl-tmp/importance_margin_vla_compress/eval_results/pi05_l2norm_k0.90_libero_spatial_seed42.json\", \"completed_at\": \"2026-05-22T02:41:35.108Z\", \"conclusion\": \"success\", \"created_at\": \"2026-05-21T23:58:06.094Z\", \"extra\": {\"hook_events\": [{\"action\": \"agent\", \"event\": \"on_complete\", \"ts\": \"2026-05-22T01:01:33.996301+00:00\"}]}, \"hypothesis\": \"π0.5 l2norm k=0.9 Spatial: l2norm 在 Object suite k=0.9 维持 ~80% SR。如果 Spatial 上 l2norm k=0.9 也远高于 random k=0.9 (54.6%) → l2norm 优势跨 suite 通用，importance-based 选择性保留关键视觉 tokens。\", \"metrics\": {\"episodes_per_task\": 50, \"keep_ratio\": 0.9, \"prune_mode\": \"l2norm\", \"seed\": 42, \"success_rate_mean\": 0.95, \"suite\": \"libero_spatial\", \"tasks_evaluated\": 10, \"total_episodes\": 500, \"total_success\": 475}, \"reproduce\": {\"finished_at\": \"2026-05-22T01:01:24.338Z\"}, \"retry_count\": 0, \"spec\": {\"account\": \"root\", \"backend\": \"tmux\", \"checkpoint_source\": \"/root/autodl-tmp/pi05_libero_finetuned\", \"command\": \"eval_pi05_pruning_libero.py --prune_mode l2norm --keep_ratio 0.9 --suite libero_spatial --n_episodes 50 --seed 42\", \"data_count\": 500, \"data_path\": \"libero_spatial\", \"eval_data\": \"libero_spatial\", \"gpu\": [\"cuda:0\"], \"gpu_hours\": 2.72, \"log_path\": \"~/runs/importance_margin_vla_compress/eval_pi05_l2norm_k09_spatial_seed42.log\", \"model_name\": \"pi05_libero_finetuned\", \"pid\": \"48423\", \"seed\": 42, \"server\": \"westd-38929\", \"submitted_at\": \"2026-05-21T23:58:05.308Z\", \"submitted_via\": \"submit_training_job\", \"wall_clock_seconds\": 9809.8}, \"status\": \"DONE\", \"updated_at\": \"2026-05-22T02:41:35.108Z\"}, \"eval_pi05_random_k09_spatial_seed42\": {\"checkpoint_path\": \"/root/autodl-tmp/importance_margin_vla_compress/eval_results/pi05_random_k0.90_libero_spatial_seed42.json\", \"completed_at\": \"2026-05-22T02:41:32.849Z\", \"conclusion\": \"success\", \"created_at\": \"2026-05-21T23:27:44.454Z\", \"extra\": {\"hook_events\": [{\"action\": \"agent\", \"event\": \"on_complete\", \"ts\": \"2026-05-22T01:25:06.248727+00:00\"}]}, \"hypothesis\": \"π0.5 random k=0.9 Spatial seed42: Object 上 k=0.9=10.8%（V-dip cliff）。如果 Spatial 也 ~10% → cliff 是 model-intrinsic，跨 task 普遍现象；如果 ~90% → cliff 是 Object-specific。Spatial baseline=97.2%。\", \"metrics\": {\"episodes_per_task\": 50, \"keep_ratio\": 0.9, \"prune_mode\": \"random\", \"seed\": 42, \"success_rate_mean\": 0.546, \"suite\": \"libero_spatial\", \"tasks_evaluated\": 10, \"total_episodes\": 500, \"total_success\": 273}, \"parent\": \"eval_pi05_random_k07_spatial_seed42\", \"reproduce\": {\"finished_at\": \"2026-05-22T01:25:00.501Z\"}, \"retry_count\": 0, \"spec\": {\"account\": \"root\", \"backend\": \"tmux\", \"checkpoint_source\": \"/root/autodl-tmp/pi05_libero_finetuned\", \"command\": \"eval_pi05_pruning_libero.py --prune_mode random --keep_ratio 0.9 --suite libero_spatial --n_episodes 50 --seed 42\", \"data_count\": 500, \"data_path\": \"libero_spatial\", \"eval_data\": \"libero_spatial\", \"gpu\": [\"cuda:1\"], \"gpu_hours\": 3.23, \"log_path\": \"~/runs/importance_margin_vla_compress/eval_pi05_random_k09_spatial_seed42.log\", \"model_name\": \"pi05_libero_finetuned\", \"pid\": \"9126\", \"seed\": 42, \"server\": \"westd-38929\", \"submitted_at\": \"2026-05-21T23:27:55.100Z\", \"submitted_via\": \"submit_training_job\", \"wall_clock_seconds\": 11617.7}, \"status\": \"DONE\", \"updated_at\": \"2026-05-22T02:41:32.849Z\"}, \"eval_pi05_random_k07_spatial_seed42_v2\": {\"completed_at\": \"2026-05-22T02:10:11.162Z\", \"conclusion\": \"failed\", \"created_at\": \"2026-05-22T01:59:32.551Z\", \"failure_reason\": \"IndexError: --n_episodes=500 导致数组越界 (line 220), 应为 50\", \"hypothesis\": \"π0.5 random k=0.7 Spatial seed42: Object 上 random k=0.7=55.0% (V-dip recovery). 如果 Spatial 也 ~55% → recovery 是 model-intrinsic; 如果更高 → Spatial 的 random robustness 整体更好 (与 D152 task-specificity 一致).\", \"retry_count\": 0, \"spec\": {\"checkpoint_path\": \"N/A\", \"checkpoint_source\": \"pi05_libero_finetuned\", \"command\": \"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/importance_margin_vla_compress && HF_HUB_OFFLINE=1 CUDA_VISIBLE_DEVICES=0 python -u eval_pi05_pruning_libero.py --prune_mode random --keep_ratio 0.7 --suite libero_spatial --n_episodes 500 --seed 42 --gpu 0\", \"data_count\": 500, \"data_path\": \"libero_spatial\", \"eval_data\": \"libero_spatial\", \"log_path\": \"/root/runs/importance_margin_vla_compress/eval_pi05_random_k07_spatial_seed42.log\", \"model_name\": \"pi05\", \"seed\": 42, \"server\": \"westd-41074\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-22T02:31:07.291Z\"}, \"eval_pi05_random_k095_spatial_seed42\": {\"completed_at\": \"2026-05-22T02:10:06.109Z\", \"conclusion\": \"failed\", \"created_at\": \"2026-05-22T01:54:42.181Z\", \"failure_reason\": \"IndexError: --n_episodes=500 导致数组越界 (line 220), 应为 50\", \"hypothesis\": \"π0.5 random k=0.95 Spatial seed42: Object 上 random k=0.95=71.1% (dual seed mean). Spatial baseline=97.2%, 如果 Spatial random k=0.95 也 >70% → cliff 强度跨 suite 一致; 如果 >90% → Spatial 更 tolerant to random pruning.\", \"retry_count\": 0, \"spec\": {\"checkpoint_path\": \"N/A\", \"checkpoint_source\": \"pi05_libero_finetuned\", \"command\": \"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/importance_margin_vla_compress && HF_HUB_OFFLINE=1 CUDA_VISIBLE_DEVICES=1 python -u eval_pi05_pruning_libero.py --prune_mode random --keep_ratio 0.95 --suite libero_spatial --n_episodes 500 --seed 42 --gpu 0\", \"data_count\": 500, \"data_path\": \"libero_spatial\", \"eval_data\": \"libero_spatial\", \"log_path\": \"/root/runs/importance_margin_vla_compress/eval_pi05_random_k095_spatial_seed42.log\", \"model_name\": \"pi05\", \"seed\": 42, \"server\": \"westd-41074\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-22T02:31:05.718Z\"}, \"eval_pi05_l2norm_k085_object_seed42_v4\": {\"completed_at\": \"2026-05-22T01:41:14.544Z\", \"conclusion\": \"success\", \"created_at\": \"2026-05-22T00:30:23.166Z\", \"extra\": {\"hook_events\": [{\"action\": \"agent\", \"event\": \"on_complete\", \"ts\": \"2026-05-22T01:38:11.534323+00:00\"}]}, \"hypothesis\": \"π0.5 L2norm k=0.85 Object seed42 v4: v3 crashed due to lerobot groot dataclass bug (Python 3.12 incompatible field ordering). Patched groot_n1.py. L2norm k=0.9=98.2%. If k=0.85 still high → L2norm monotonic degradation, no cliff.\", \"metrics\": {\"elapsed_min\": 64.35, \"overall_sr\": 0.98, \"per_task_sr\": {\"T0_alphabet_soup\": 1, \"T1_cream_cheese\": 1, \"T2_salad_dressing\": 0.98, \"T3_bbq_sauce\": 0.98, \"T4_ketchup\": 0.98, \"T5_tomato_sauce\": 0.98, \"T6_butter\": 1, \"T7_milk\": 0.88, \"T8_chocolate_pudding\": 1, \"T9_orange_juice\": 1}, \"total_episodes\": 500, \"total_successes\": 490}, \"reproduce\": {\"finished_at\": \"2026-05-22T01:38:05.349Z\"}, \"retry_count\": 0, \"spec\": {\"checkpoint_path\": \"N/A\", \"command\": \"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/importance_margin_vla_compress && HF_HUB_OFFLINE=1 MUJOCO_GL=egl python -u eval_pi05_pruning_libero.py --prune_mode l2norm --keep_ratio 0.85 --suite libero_object --n_episodes 50 --seed 42 --gpu 0\", \"data_count\": 500, \"data_path\": \"libero_object\", \"log_path\": \"/root/runs/importance_margin_vla_compress/eval_pi05_l2norm_k085_object_seed42_v4.log\", \"model_name\": \"pi05\", \"results_json\": \"/root/autodl-tmp/importance_margin_vla_compress/eval_results/pi05_l2norm_k0.85_libero_object_seed42.json\", \"seed\": 42, \"server\": \"westd-41074\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-22T01:58:30.102Z\"}, \"eval_pi05_l2norm_k085_object_seed42_v2\": {\"completed_at\": \"2026-05-22T00:30:12.115Z\", \"conclusion\": \"failed\", \"created_at\": \"2026-05-21T23:32:48.735Z\", \"hypothesis\": \"π0.5 L2norm k=0.85 Object seed42 v2: 与 random k=0.85 配对。L2norm k=0.9=98.2%。如果 L2norm k=0.85 仍高→L2norm 无 cliff，是 monotonic degradation (v1 failed due to cqa1 env mismatch).\", \"parent\": \"eval_pi05_l2norm_k085_object_seed42\", \"retry_count\": 0, \"spec\": {\"checkpoint_path\": \"/root/autodl-tmp/pi05_libero_finetuned\", \"checkpoint_source\": \"/root/autodl-tmp/pi05_libero_finetuned\", \"command\": \"CUDA_VISIBLE_DEVICES=1 HF_HUB_OFFLINE=1 HF_HOME=/root/autodl-tmp/.hf_cache MUJOCO_GL=egl python -u eval_pi05_pruning_libero.py --prune_mode l2norm --keep_ratio 0.85 --suite libero_object --n_episodes 50 --seed 42 --gpu 0\", \"data_count\": 500, \"data_path\": \"/root/autodl-tmp/pi05_libero_finetuned\", \"eval_data\": \"libero_object\", \"gpu_id\": 1, \"log_path\": \"/root/autodl-tmp/logs/eval_pi05_l2norm_k085_seed42_v2.log\", \"model_name\": \"pi05\", \"pid\": 805839, \"seed\": 42, \"server\": \"cqa1-33015\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-22T00:30:12.115Z\"}, \"eval_openvla_baseline_spatial_seed42_v3\": {\"completed_at\": \"2026-05-22T00:20:01.422Z\", \"conclusion\": \"failed\", \"created_at\": \"2026-05-21T22:42:47.914Z\", \"extra\": {\"hook_events\": [{\"action\": \"agent\", \"event\": \"on_failed\", \"ts\": \"2026-05-22T00:20:07.550389+00:00\"}]}, \"failure_reason\": \"SSH check failed 5x — last error: [Errno None] Unable to connect to port 27271 on 36.103.198.204\", \"hypothesis\": \"OpenVLA baseline on LIBERO-Spatial v3 (新脚本，env.seed 已修复，--model_path 支持)。建立 cross-suite anchor，验证 pruning tolerance 是模型内在属性而非 task-specific。\", \"notes\": \"westd-27271 服务器不可达 (SSH failed 5x)。需在其他服务器重试。这是 v3 (v1/v2 也因各种原因失败)。OpenVLA Spatial baseline 是 cross-suite anchor，对论文 Table 3 重要。\", \"parent\": \"eval_openvla_baseline_spatial_seed42_v2\", \"retry_count\": 0, \"spec\": {\"checkpoint_path\": \"/root/autodl-tmp/openvla-7b-finetuned-libero-spatial\", \"checkpoint_source\": \"/root/autodl-tmp/openvla-7b-finetuned-libero-spatial\", \"command\": \"HF_HUB_OFFLINE=1 MUJOCO_GL=egl python -u eval_openvla_l2norm_libero.py --mode baseline --model_path /root/autodl-tmp/openvla-7b-finetuned-libero-spatial --unnorm_key libero_spatial --suite libero_spatial --num_episodes 50 --gpu 0 --seed 42\", \"data_count\": 500, \"data_path\": \"libero_spatial (LIBERO benchmark)\", \"eval_data\": \"libero_spatial\", \"log_path\": \"/root/autodl-tmp/importance_margin_vla_compress/logs/eval_openvla_baseline_spatial_seed42_v3.log\", \"model_name\": \"openvla-7b-finetuned-libero-spatial\", \"seed\": 42, \"server\": \"westd-27271\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-22T00:23:00.192Z\"}, \"train_openvla_sc_m32_vtconly_seed42\": {\"completed_at\": \"2026-05-20T10:41:33.455Z\", \"conclusion\": \"failed\", \"created_at\": \"2026-05-20T01:13:01.057Z\", \"extra\": {\"hook_events\": [{\"action\": \"agent\", \"event\": \"on_failed\", \"ts\": \"2026-05-20T10:41:38.206200+00:00\"}, {\"action\": \"agent\", \"event\": \"on_failed\", \"ts\": \"2026-05-22T00:20:39.042270+00:00\"}], \"previous_failure\": {\"conclusion\": \"failed\", \"notes\": \"失败原因: 磁盘写入失败 — step 20000 checkpoint 保存时 RuntimeError: PytorchStreamWriter failed writing file data/1007: file write failed (pos 16157571008). 训练本身正常 (loss ~2.8, eval_loss=2.8768@20K). | 已有成果: 训练正常到 step 20000/100K, 可能有 step 10K/15K 的 checkpoint | 建议: 检查磁盘空间, 清理旧 checkpoint, 从最新 checkpoint resume\"}}, \"failure_reason\": \"SSH check failed 5x — last error: [Errno None] Unable to connect to port 27271 on 36.103.198.204\", \"hypothesis\": \"OpenVLA VTC-only M=32 (256→32 tokens, 87.5% compression) on westd-27271. Most aggressive OpenVLA compression point. Independent of 20K gate — even if C4-ext fails, M=32 data point contributes to M-sweep curve. If VTC M=32 > random pruning k=0.3 (20.6% SR), demonstrates learned re-encoding value at extreme compression.\", \"notes\": \"Resume from step 10001 (checkpoint.pt). 修复: 1) 删除损坏的 step20000.pt (16G) 和冗余 step10000.pt (19G), 释放 35G; 2) 修改 save_checkpoint 添加旧 checkpoint 自动清理 (只保留最新 1 个 step checkpoint), 防止再次磁盘满; 3) 磁盘 67G 可用, 足够完成剩余训练.\", \"parent\": \"train_openvla_sc_m128_vtconly_seed42\", \"reproduce\": {\"finished_at\": \"2026-05-20T10:41:31.047Z\"}, \"retry_count\": 1, \"spec\": {\"account\": \"root\", \"checkpoint_path\": \"checkpoints/openvla_sc_m32_seed42/\", \"checkpoint_source\": \"openvla/openvla-7b (libero finetuned)\", \"command\": \"bash -c 'source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/importance_margin_vla_compress && CUDA_VISIBLE_DEVICES=1 HF_HOME=/root/autodl-tmp/.hf_cache TRANSFORMERS_OFFLINE=1 WANDB_MODE=offline python -u train_openvla_smart_compress.py --config configs/openvla_smart_compress_m32.yaml --resume checkpoints/openvla_sc_m32_seed42'\", \"data_count\": \"273465\", \"data_path\": \"HuggingFaceVLA/libero\", \"eval_data\": \"N/A (training experiment)\", \"gpu\": \"cuda:1\", \"log_path\": \"/root/autodl-tmp/importance_margin_vla_compress/logs/train_openvla_sc_m32_seed42_resume.log\", \"model_name\": \"openvla + VTC(M=32)\", \"pid\": \"921279\", \"seed\": 42, \"server\": \"westd-27271\", \"tmux_session\": \"train_openvla_sc_m32_seed42\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-22T00:20:29.905Z\"}, \"eval_pi05_random_k0925_object_seed42\": {\"completed_at\": \"2026-05-21T23:52:44.479Z\", \"conclusion\": \"negative\", \"created_at\": \"2026-05-21T21:53:09.140Z\", \"extra\": {\"hook_events\": [{\"action\": \"agent\", \"event\": \"on_failed\", \"ts\": \"2026-05-21T23:52:59.959002+00:00\"}]}, \"failure_reason\": \"process dead 5× with no sentinel/W&B — auto-resolved as failed\", \"hypothesis\": \"π0.5 random k=0.925 Object seed42: 定位 k=0.95(69.4%) → k=0.9(10.8%) 之间 58.6pp cliff 的精确过渡点。如果 k=0.925 > 50% 则 cliff 在 [0.9, 0.925]，如果 < 20% 则 cliff 从 k=0.95 就开始陡降。n_keep=237/256。\", \"metrics\": {\"elapsed_min\": 108.9, \"overall_sr\": 0.276, \"per_task_sr\": [0.34, 0.42, 0.24, 0.14, 0.08, 0.42, 0.4, 0.12, 0.34, 0.26], \"total_episodes\": 500, \"total_successes\": 138}, \"parent\": \"eval_pi05_random_k095_object_seed42_v2\", \"reproduce\": {\"finished_at\": \"2026-05-21T23:52:38.365Z\"}, \"retry_count\": 0, \"spec\": {\"checkpoint_path\": \"/root/autodl-tmp/importance_margin_vla_compress/eval_results/pi05_random_k0.93_libero_object_seed42.json\", \"checkpoint_source\": \"/root/autodl-tmp/pi05_libero_finetuned\", \"command\": \"HF_HUB_OFFLINE=1 MUJOCO_GL=egl python -u eval_pi05_pruning_libero.py --prune_mode random --keep_ratio 0.925 --suite libero_object --n_episodes 50 --seed 42 --gpu 0\", \"data_count\": 500, \"data_path\": \"libero_object\", \"eval_data\": \"libero_object_50ep_x_10tasks\", \"log_path\": \"/root/autodl-tmp/importance_margin_vla_compress/logs/eval_pi05_random_k0925_object_seed42.log\", \"model_name\": \"pi0.5\", \"seed\": 42, \"server\": \"westd-41074\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-21T23:53:03.078Z\"}, \"eval_pi05_random_k03_object_seed43\": {\"completed_at\": \"2026-05-21T23:16:50.702Z\", \"conclusion\": \"failed\", \"created_at\": \"2026-05-21T21:52:57.780Z\", \"hypothesis\": \"π0.5 random k=0.3 Object seed43: seed 验证，seed42=36.4%。确认 random k=0.3 的 SR 在 seed 间可重复。\", \"parent\": \"eval_pi05_random_k03_object_seed42\", \"retry_count\": 0, \"spec\": {\"checkpoint_path\": \"N/A\", \"checkpoint_source\": \"/root/autodl-tmp/pi05_libero_finetuned\", \"command\": \"CUDA_VISIBLE_DEVICES=3 HF_HUB_OFFLINE=1 HF_HOME=/root/autodl-tmp/.hf_cache MUJOCO_GL=egl python -u eval_pi05_pruning_libero.py --prune_mode random --keep_ratio 0.3 --suite libero_object --n_episodes 50 --seed 43 --gpu 0\", \"data_count\": 500, \"data_path\": \"/root/autodl-tmp/pi05_libero_finetuned\", \"eval_data\": \"libero_object\", \"failure_reason\": \"cqa1 environment mismatch: transformers 4.53.2 (need 5.5.3) + lerobot 0.5.1 (need 0.5.2 editable) → PI05Policy inference produces 0% SR.\", \"log_path\": \"N/A\", \"model_name\": \"pi05\", \"seed\": 43, \"server\": \"cqa1-33015\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-21T23:49:03.208Z\"}, \"eval_pi05_l2norm_k085_object_seed42\": {\"completed_at\": \"2026-05-21T23:16:48.511Z\", \"conclusion\": \"failed\", \"created_at\": \"2026-05-21T21:52:55.538Z\", \"hypothesis\": \"π0.5 L2norm k=0.85 Object seed42: 与 random k=0.85 配对对比。L2norm 在 k=0.9 时 98.2%（接近 baseline），在 cliff 区间 L2norm 是否也下降？如果 L2norm k=0.85 仍高→证实 L2norm 的 monotonic degradation vs random 的 cliff behavior。\", \"retry_count\": 0, \"spec\": {\"checkpoint_path\": \"N/A\", \"checkpoint_source\": \"/root/autodl-tmp/pi05_libero_finetuned\", \"command\": \"CUDA_VISIBLE_DEVICES=2 HF_HUB_OFFLINE=1 HF_HOME=/root/autodl-tmp/.hf_cache MUJOCO_GL=egl python -u eval_pi05_pruning_libero.py --prune_mode l2norm --keep_ratio 0.85 --suite libero_object --n_episodes 50 --seed 42 --gpu 0\", \"data_count\": 500, \"data_path\": \"/root/autodl-tmp/pi05_libero_finetuned\", \"eval_data\": \"libero_object\", \"failure_reason\": \"cqa1 environment mismatch: transformers 4.53.2 (need 5.5.3) + lerobot 0.5.1 (need 0.5.2 editable) → PI05Policy inference produces 0% SR.\", \"log_path\": \"N/A\", \"model_name\": \"pi05\", \"seed\": 42, \"server\": \"cqa1-33015\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-21T23:49:00.980Z\"}, \"eval_pi05_random_k085_object_seed42_v2\": {\"completed_at\": \"2026-05-21T23:18:32.933Z\", \"conclusion\": \"negative\", \"created_at\": \"2026-05-21T21:20:40.718Z\", \"extra\": {\"hook_events\": [{\"action\": \"agent\", \"event\": \"on_failed\", \"ts\": \"2026-05-21T23:18:41.423944+00:00\"}]}, \"failure_reason\": \"process dead 5× with no sentinel/W&B — auto-resolved as failed\", \"hypothesis\": \"π0.5 random k=0.85 seed42: 定位 cliff boundary。k=0.7→75.5% vs k=0.9→10.8%，如果 k=0.85 也崩→cliff 在 0.7-0.85 之间；如果 k=0.85 高→cliff 在 0.85-0.9 之间。关键数据点。\", \"log_path\": \"/tmp/eval_pi05_random_k085_object_seed42_v2.log\", \"metrics\": {\"duration_min\": 108.5, \"episodes\": 500, \"per_task_sr\": \"10 tasks completed, overall 25/500\", \"success_rate\": 5, \"tasks\": 10}, \"parent\": \"eval_pi05_random_k09_object_seed42_v2\", \"reproduce\": {\"finished_at\": \"2026-05-21T23:18:28.484Z\"}, \"retry_count\": 0, \"spec\": {\"checkpoint_source\": \"pi0.5-pretrained\", \"command\": \"HF_HUB_OFFLINE=1 MUJOCO_GL=egl python -u eval_pi05_pruning_libero.py --prune_mode random --keep_ratio 0.85 --suite libero_object --n_episodes 50 --gpu 0 --seed 42\", \"data_count\": 500, \"data_path\": \"/root/autodl-tmp/importance_margin_vla_compress\", \"eval_data\": \"libero_object\", \"gpu_id\": 3, \"log_path\": \"/tmp/eval_pi05_random_k085_object_seed42_v2.log\", \"model_name\": \"pi0.5\", \"pid\": 824147, \"seed\": 42, \"server\": \"westd-38929\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-21T23:48:19.656Z\"}, \"eval_pi05_random_k03_spatial_seed42\": {\"completed_at\": \"2026-05-21T23:05:16.811Z\", \"conclusion\": \"success\", \"created_at\": \"2026-05-21T20:55:20.520Z\", \"extra\": {\"hook_events\": [{\"action\": \"agent\", \"event\": \"on_complete\", \"ts\": \"2026-05-21T22:56:38.149173+00:00\"}]}, \"hypothesis\": \"π0.5 random k=0.3 on LIBERO-Spatial seed42. Object suite 上 D140 发现 k=0.3 method reversal (L2norm=51.0% > random=36.4%)。验证该 reversal 是否跨 suite 复现。与运行中的 L2norm k=0.3 spatial 实验配对。\", \"metrics\": {\"per_task_sr\": {\"T0_between_plate\": 66, \"T1_next_to_ramekin\": 80, \"T2_from_table_center\": 62, \"T3_on_cookie_box\": 14, \"T4_in_top_drawer\": 30, \"T5_on_ramekin\": 28, \"T6_next_to_cookie\": 32, \"T7_on_stove\": 64, \"T8_next_to_plate\": 82, \"T9_on_wooden_cab\": 38}, \"success_rate\": 49.6, \"total_episodes\": 500}, \"reproduce\": {\"finished_at\": \"2026-05-21T22:56:30.879Z\"}, \"retry_count\": 0, \"spec\": {\"checkpoint_path\": \"/root/autodl-tmp/pi05_libero_finetuned\", \"checkpoint_source\": \"/root/autodl-tmp/pi05_libero_finetuned\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/importance_margin_vla_compress && HF_HUB_OFFLINE=1 python -u eval_pi05_pruning_libero.py --prune_mode random --keep_ratio 0.3 --suite libero_spatial --n_episodes 50 --seed 42 --gpu 0\\\"\", \"data_count\": 500, \"data_path\": \"libero_spatial (10 tasks x 50 eps)\", \"eval_data\": \"libero_spatial\", \"gpu\": [\"cuda:0\"], \"log_path\": \"~/runs/importance_margin_vla_compress/eval_pi05_random_k03_spatial_seed42.log\", \"model_name\": \"pi05_libero_finetuned\", \"pid\": \"788113\", \"seed\": 42, \"server\": \"westd-38929\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-21T23:05:16.811Z\"}, \"eval_pi05_random_k09_fixedmask_object_seed42_v2\": {\"completed_at\": \"2026-05-21T22:37:05.645Z\", \"conclusion\": \"negative\", \"created_at\": \"2026-05-21T20:15:58.542Z\", \"extra\": {\"hook_events\": [{\"action\": \"agent\", \"event\": \"on_complete\", \"ts\": \"2026-05-21T22:10:35.317039+00:00\"}]}, \"hypothesis\": \"π0.5 fixed-mask random k=0.9 seed42 v2: 判别 k=0.9 ~10% SR 根因。per-episode 固定 random mask 消除 temporal inconsistency。恢复~90%+ → stochastic mask 是根因; 仍~12% → specific tokens critical。网络修复后重跑。\", \"metrics\": {\"per_task_sr\": [0.12, 0.26, 0.16, 0.14, 0.12, 0.24, 0.18, 0.14, 0.24, 0.1], \"success_rate\": 0.17, \"successes\": 85, \"total_episodes\": 500}, \"parent\": \"eval_pi05_random_k09_fixedmask_object_seed42\", \"reproduce\": {\"finished_at\": \"2026-05-21T22:10:27.937Z\"}, \"retry_count\": 0, \"spec\": {\"checkpoint_path\": \"pi0.5_pretrained (no finetuning)\", \"log_path\": \"~/runs/importance_margin_vla_compress/eval_pi05_random_k09_fixedmask_object_seed42_v2.log\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-21T22:37:05.644Z\"}, \"train_smart_compress_m16_seed44_v3\": {\"completed_at\": \"2026-05-21T22:37:03.303Z\", \"conclusion\": \"success\", \"created_at\": \"2026-05-19T17:05:30.575Z\", \"hypothesis\": \"Third attempt of M=16 seed44 training (v1 failed: server restart, v2 failed: disk full at step=1000). Disk now cleared to 73GB free. Third seed for extreme compression point (87.5%). Prior: seed42=55.8%. Completes 3-seed data for M=16 on M-curve.\", \"metrics\": {\"eval_action_loss\": 0.0495, \"total_steps\": 99999, \"train_action_loss\": 0.0677, \"train_grad_norm\": 1.88821}, \"retry_count\": 0, \"spec\": {\"checkpoint_path\": \"/root/autodl-tmp/importance_margin_vla_compress/checkpoints/smart_compress_m16_seed44/checkpoint.pt\", \"log_path\": \"~/runs/importance_margin_vla_compress/train_smart_compress_m16_seed44_v3.log\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-21T22:37:03.303Z\"}, \"train_smart_compress_m16_seed43\": {\"completed_at\": \"2026-05-21T22:37:01.029Z\", \"conclusion\": \"success\", \"created_at\": \"2026-05-19T15:22:07.244Z\", \"hypothesis\": \"Second seed (seed=43) for Smart Compress M=16 (87.5% compression). Prior: seed42=55.8%. M=16 showed lowest SR among tested M values, confirming information bottleneck at extreme compression. Second seed establishes variance at this extreme point for M-curve robustness.\", \"metrics\": {\"eval_action_loss\": 0.06236, \"total_steps\": 99999, \"train_action_loss\": 0.07652, \"train_grad_norm\": 0.97135}, \"retry_count\": 0, \"spec\": {\"account\": \"root\", \"backend\": \"tmux\", \"checkpoint_path\": \"checkpoints/smart_compress_m16_seed43/checkpoint.pt\", \"checkpoint_source\": \"smolvla_base\", \"command\": \"python -u train_smart_compress.py --config configs/smart_compress_m16_seed43.yaml --wandb_run smart_compress_m16_seed43 --seed 43 --gpu 0\", \"data_count\": \"all\", \"data_path\": \"HuggingFaceVLA/libero\", \"gpu\": \"cuda:2\", \"gpu_hours\": 55.23, \"log_path\": \"~/runs/importance_margin_vla_compress/train_smart_compress_m16_seed43.log\", \"model_name\": \"smolvla_base + VisionTokenCompressor(M=16)\", \"pid\": \"649840\", \"seed\": 43, \"server\": \"cqa1-33015\", \"submitted_at\": \"2026-05-19T15:23:19.286Z\", \"submitted_via\": \"submit_training_job\", \"wall_clock_seconds\": 198821.7}, \"status\": \"DONE\", \"updated_at\": \"2026-05-21T22:37:01.029Z\"}, \"train_smart_compress_m128_seed43\": {\"completed_at\": \"2026-05-21T22:36:58.789Z\", \"conclusion\": \"success\", \"created_at\": \"2026-05-19T15:22:04.812Z\", \"hypothesis\": \"Third seed (seed=43) for Smart Compress M=128 passthrough control. Prior seeds: seed42=59.8%, seed44=60.2%. M=128 retains all 128 tokens through cross-attention re-encoding, isolating architecture effect from compression. Third seed makes \\\"re-encoding > compression\\\" argument 3-seed bulletproof (C4).\", \"metrics\": {\"eval_action_loss\": 0.06125, \"total_steps\": 99999, \"train_action_loss\": 0.05584, \"train_grad_norm\": 0.95519}, \"retry_count\": 0, \"spec\": {\"account\": \"root\", \"backend\": \"tmux\", \"checkpoint_path\": \"checkpoints/smart_compress_m128_seed43/checkpoint.pt\", \"checkpoint_source\": \"smolvla_base\", \"command\": \"python -u train_smart_compress.py --config configs/smart_compress_m128_seed43.yaml --wandb_run smart_compress_m128_seed43 --seed 43 --gpu 0\", \"data_count\": \"all\", \"data_path\": \"HuggingFaceVLA/libero\", \"gpu\": \"cuda:1\", \"gpu_hours\": 55.23, \"log_path\": \"~/runs/importance_margin_vla_compress/train_smart_compress_m128_seed43.log\", \"model_name\": \"smolvla_base + VisionTokenCompressor(M=128)\", \"pid\": \"649692\", \"seed\": 43, \"server\": \"cqa1-33015\", \"submitted_at\": \"2026-05-19T15:23:13.016Z\", \"submitted_via\": \"submit_training_job\", \"wall_clock_seconds\": 198825.8}, \"status\": \"DONE\", \"updated_at\": \"2026-05-21T22:36:58.789Z\"}, \"train_smart_compress_m96_seed44\": {\"completed_at\": \"2026-05-21T22:35:52.363Z\", \"conclusion\": \"success\", \"created_at\": \"2026-05-19T01:10:52.530Z\", \"hypothesis\": \"Third seed (seed=44) for Smart Compress M=96 to strengthen multi-seed robustness. Prior seeds: seed42=52.6%, seed43=58.2%. If seed44 narrows variance, confirms non-monotonic M-curve is robust at M=96.\", \"metrics\": {\"eval_action_loss\": 0.05259, \"total_steps\": 99999, \"train_action_loss\": 0.04668, \"train_grad_norm\": 0.97222}, \"parent\": \"\", \"retry_count\": 0, \"spec\": {\"checkpoint_path\": \"/root/autodl-tmp/importance_margin_vla_compress/checkpoints/smart_compress_m96_seed44/checkpoint.pt\", \"checkpoint_source\": \"smolvla_base (from scratch)\", \"command\": \"source /root/miniconda3/bin/activate && cd /root/autodl-tmp/importance_margin_vla_compress && HF_HOME=/root/autodl-tmp/.hf_cache HF_HUB_OFFLINE=1 WANDB_MODE=offline python -u train_smart_compress.py --config configs/smart_compress_m96_seed44.yaml --wandb_run smart_compress_m96_seed44 --seed 44 --gpu 0\", \"data_count\": -1, \"data_path\": \"HuggingFaceVLA/libero\", \"log_path\": \"/root/autodl-tmp/importance_margin_vla_compress/logs/smart_compress_m96_seed44.log\", \"model_name\": \"smolvla_base + VisionTokenCompressor(M=96)\", \"seed\": 44, \"server\": \"cqa1-33015\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-21T22:35:52.363Z\"}, \"train_smart_compress_m32_seed44\": {\"completed_at\": \"2026-05-21T22:35:50.226Z\", \"conclusion\": \"success\", \"created_at\": \"2026-05-19T01:10:50.362Z\", \"hypothesis\": \"Smart compress with M=32 vision token compression trained with seed 44 will achieve comparable performance to seed 43, confirming reproducibility of the importance-margin-based compression approach.\", \"metrics\": {\"eval_action_loss\": 0.0635, \"total_steps\": 99999, \"train_action_loss\": 0.04146, \"train_grad_norm\": 0.57272}, \"parent\": \"\", \"retry_count\": 0, \"spec\": {\"checkpoint_path\": \"/root/autodl-tmp/importance_margin_vla_compress/checkpoints/smart_compress_m32_seed44/checkpoint.pt\", \"checkpoint_source\": \"smolvla_base (from scratch)\", \"command\": \"source /root/miniconda3/bin/activate && cd /root/autodl-tmp/importance_margin_vla_compress && HF_HOME=/root/autodl-tmp/.hf_cache HF_HUB_OFFLINE=1 WANDB_MODE=offline python -u train_smart_compress.py --config configs/smart_compress_m32_seed44.yaml --wandb_run smart_compress_m32_seed44 --seed 44 --gpu 0\", \"data_count\": -1, \"data_path\": \"HuggingFaceVLA/libero\", \"log_path\": \"/root/autodl-tmp/importance_margin_vla_compress/logs/smart_compress_m32_seed44.log\", \"model_name\": \"smolvla_base + VisionTokenCompressor(M=32)\", \"seed\": 44, \"server\": \"cqa1-33015\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-21T22:35:50.226Z\"}, \"train_smart_compress_m64_seed44\": {\"completed_at\": \"2026-05-21T22:35:47.995Z\", \"conclusion\": \"success\", \"created_at\": \"2026-05-19T01:10:51.474Z\", \"hypothesis\": \"Third seed (seed=44) for Smart Compress M=64 to strengthen multi-seed robustness. Prior seeds: seed42=61.6%, seed43=60.0%. If seed44 yields ~60% SR, confirms M=64 matches M=32 performance with mean ~60% across 3 seeds.\", \"metrics\": {\"eval_action_loss\": 0.06994, \"total_steps\": 99999, \"train_action_loss\": 0.031, \"train_grad_norm\": 1.08378}, \"parent\": \"\", \"retry_count\": 0, \"spec\": {\"checkpoint_path\": \"/root/autodl-tmp/importance_margin_vla_compress/checkpoints/smart_compress_m64_seed44/checkpoint.pt\", \"checkpoint_source\": \"smolvla_base (from scratch)\", \"command\": \"source /root/miniconda3/bin/activate && cd /root/autodl-tmp/importance_margin_vla_compress && CUDA_VISIBLE_DEVICES=1 HF_HOME=/root/autodl-tmp/.hf_cache HF_HUB_OFFLINE=1 WANDB_MODE=offline python -u train_smart_compress.py --config configs/smart_compress_m64_seed44.yaml --wandb_run smart_compress_m64_seed44 --seed 44 --gpu 0\", \"data_count\": \"all\", \"data_path\": \"HuggingFaceVLA/libero\", \"log_path\": \"/root/autodl-tmp/importance_margin_vla_compress/logs/train_smart_compress_m64_seed44.log\", \"model_name\": \"smolvla_base + VisionTokenCompressor(M=64)\", \"seed\": 44, \"server\": \"cqa1-33015\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-21T22:35:47.995Z\"}, \"train_smart_compress_m128_resume\": {\"completed_at\": \"2026-05-21T22:35:43.265Z\", \"conclusion\": \"success\", \"created_at\": \"2026-05-18T05:27:32.368Z\", \"extra\": {\"hook_events\": [{\"action\": \"agent\", \"event\": \"on_complete\", \"ts\": \"2026-05-18T10:06:20.885052+00:00\"}]}, \"hypothesis\": \"Resume of train_smart_compress_m128 from step 32,000 checkpoint. Cross-attention pooling with M=128 queries (no compression, passthrough control). If SR similar to M=32/M=64 (61.6%), improvement comes from cross-attention architecture itself. If lower/equal to baseline (44.8%), compression provides the benefit.\", \"metrics\": {\"eval_action_loss\": 0.05743, \"resumed_from_step\": 32001, \"total_steps\": 99999, \"train_action_loss\": 0.05412, \"train_grad_norm\": 0.92663}, \"parent\": \"train_smart_compress_m128\", \"reproduce\": {\"finished_at\": \"2026-05-18T10:06:16.992Z\"}, \"retry_count\": 0, \"spec\": {\"checkpoint_path\": \"/root/autodl-tmp/importance_margin_vla_compress/checkpoints/smart_compress_m128/checkpoint.pt\", \"log_path\": \"~/runs/importance_margin_vla_compress/train_smart_compress_m128_resume.log\", \"wandb_offline_run\": \"/root/autodl-tmp/importance_margin_vla_compress/wandb/offline-run-20260518_132800-x610qzvt\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-21T22:35:43.265Z\"}, \"eval_pi05_random_k07_spatial_seed42\": {\"checkpoint_path\": \"/root/autodl-tmp/pi05_libero_finetuned\", \"completed_at\": \"2026-05-21T22:29:46.227Z\", \"conclusion\": \"success\", \"created_at\": \"2026-05-21T20:55:22.277Z\", \"extra\": {\"hook_events\": [{\"action\": \"agent\", \"event\": \"on_complete\", \"ts\": \"2026-05-21T22:26:58.674174+00:00\"}]}, \"hypothesis\": \"π0.5 random k=0.7 on LIBERO-Spatial seed42. Object suite 上 random k=0.7=77.2% > L2norm k=0.7=55.0%。验证低 CV(0.055) 模型的 method preference (random > L2norm at k=0.7) 是否跨 suite 一致。\", \"metrics\": {\"per_task_sr\": {\"T0_between_plate\": 90, \"T1_next_to_ramekin\": 96, \"T2_table_center\": 94, \"T3_on_cookie_box\": 52, \"T4_in_top_drawer\": 60, \"T5_on_ramekin\": 42, \"T6_next_to_cookie\": 58, \"T7_on_stove\": 76, \"T8_next_to_plate\": 80, \"T9_on_wooden_cab\": 96}, \"success_rate\": 74.4, \"total_episodes\": 500}, \"reproduce\": {\"finished_at\": \"2026-05-21T22:26:50.626Z\"}, \"retry_count\": 0, \"spec\": {\"checkpoint_source\": \"/root/autodl-tmp/pi05_libero_finetuned\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/importance_margin_vla_compress && HF_HUB_OFFLINE=1 python -u eval_pi05_pruning_libero.py --prune_mode random --keep_ratio 0.7 --suite libero_spatial --n_episodes 50 --seed 42 --gpu 0\\\"\", \"data_count\": 500, \"data_path\": \"libero_spatial (10 tasks x 50 eps)\", \"eval_data\": \"libero_spatial\", \"gpu\": [\"cuda:2\"], \"log_path\": \"~/runs/importance_margin_vla_compress/eval_pi05_random_k07_spatial_seed42.log\", \"model_name\": \"pi05_libero_finetuned\", \"pid\": \"788353\", \"seed\": 42, \"server\": \"westd-38929\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-21T22:29:46.227Z\"}, \"eval_pi05_l2norm_k03_object_seed43\": {\"completed_at\": \"2026-05-21T13:00:46.690Z\", \"conclusion\": \"success\", \"created_at\": \"2026-05-21T11:27:32.180Z\", \"hypothesis\": \"π0.5 L2norm k=0.3 Object seed43: seed 验证 L2norm 非单调性。seed42 L2norm k=0.3=51.0% > k=0.5=33.4%。确认 V-shape 恢复跨 seed 可复现——这是论文要用的发现。\", \"metrics\": {\"SR\": 0.554, \"elapsed_min\": 85.15, \"per_task\": {\"alphabet_soup\": 0.16, \"bbq_sauce\": 0.54, \"butter\": 0.52, \"chocolate_pudding\": 0.92, \"cream_cheese\": 0.56, \"ketchup\": 0.4, \"milk\": 0.14, \"orange_juice\": 0.54, \"salad_dressing\": 0.9, \"tomato_sauce\": 0.86}, \"total_episodes\": 500, \"total_successes\": 277}, \"parent\": \"eval_pi05_l2norm_k03_object_seed42\", \"retry_count\": 0, \"spec\": {\"checkpoint_path\": \"/root/autodl-tmp/pi05_libero_finetuned\", \"checkpoint_source\": \"/root/autodl-tmp/pi05_libero_finetuned\", \"command\": \"python eval_pi05_pruning_libero.py --prune_mode l2norm --keep_ratio 0.3 --suite libero_object --n_episodes 50 --seed 43 --gpu 1\", \"data_count\": 500, \"data_path\": \"libero_object\", \"eval_data\": \"libero_object_10tasks_50eps\", \"gpu_id\": 1, \"log_path\": \"/root/autodl-tmp/importance_margin_vla_compress/eval_results/pi05_l2norm_k0.30_libero_object_seed43.json\", \"model_name\": \"pi05_libero_finetuned\", \"pid\": 207154, \"seed\": 43, \"server\": \"westd-41074\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-21T22:09:26.332Z\"}, \"eval_openvla_l2norm_k09_object_seed42\": {\"checkpoint_path\": \"/root/autodl-tmp/importance_margin_vla_compress/eval_results/openvla_l2norm_prune_k09_object_seed42.json\", \"completed_at\": \"2026-05-21T22:07:51.904Z\", \"conclusion\": \"success\", \"created_at\": \"2026-05-21T18:34:31.828Z\", \"hypothesis\": \"OpenVLA L2norm k=0.9 (保留90% tokens) on LIBERO-object seed42. 接近无压缩baseline，验证L2norm在高保留率下是否维持性能，完善scaling law k-sweep数据点。\", \"log_path\": \"/root/autodl-tmp/logs/eval_openvla_l2norm_k09_object_seed42.log\", \"metrics\": {\"elapsed_minutes\": 228.5, \"overall_sr\": 0.706, \"per_task_sr\": {\"alphabet_soup\": 0.66, \"bbq_sauce\": 0.48, \"butter\": 0.74, \"chocolate_pudding\": 0.78, \"cream_cheese\": 0.58, \"ketchup\": 0.9, \"milk\": 0.74, \"orange_juice\": 0.88, \"salad_dressing\": 0.66, \"tomato_sauce\": 0.64}, \"total_episodes\": 500, \"total_successes\": 353}, \"retry_count\": 0, \"spec\": {\"checkpoint_source\": \"openvla_finetuned\", \"command\": \"CUDA_VISIBLE_DEVICES=0 python -u eval_openvla_l2norm_libero.py --mode l2norm_prune --k_ratio 0.9 --suite libero_object --seed 42\", \"data_count\": 500, \"data_path\": \"libero_object\", \"eval_data\": \"libero_object\", \"gpu_id\": 0, \"model_name\": \"openvla\", \"pid\": 306593, \"seed\": 42, \"server\": \"westd-27271\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-21T22:07:51.904Z\"}, \"eval_pi05_l2norm_k05_object_seed43\": {\"completed_at\": \"2026-05-21T13:17:08.902Z\", \"conclusion\": \"success\", \"created_at\": \"2026-05-21T11:27:29.169Z\", \"hypothesis\": \"π0.5 L2norm k=0.5 Object seed43: seed 验证 V-shape valley。seed42=33.4%（最低点）。确认 V-shape valley 跨 seed 可复现。\", \"metrics\": {\"overall_sr\": 0.336, \"per_task_sr\": {\"alphabet_soup\": 0.44, \"bbq_sauce\": 0.04, \"butter\": 0.32, \"chocolate_pudding\": 0.46, \"cream_cheese\": 0.08, \"ketchup\": 0.6, \"milk\": 0.52, \"orange_juice\": 0.52, \"salad_dressing\": 0, \"tomato_sauce\": 0.38}, \"total_episodes\": 500, \"total_successes\": 168}, \"parent\": \"eval_pi05_l2norm_k05_object_seed42\", \"retry_count\": 0, \"spec\": {\"checkpoint_path\": \"N/A\", \"checkpoint_source\": \"/root/autodl-tmp/pi05_libero_finetuned\", \"command\": \"python eval_pi05_pruning_libero.py --prune_mode l2norm --keep_ratio 0.5 --suite libero_object --n_episodes 50 --seed 43 --gpu 0\", \"data_count\": 500, \"data_path\": \"libero_object\", \"eval_data\": \"libero_object_10tasks_50eps\", \"gpu_id\": 0, \"log_path\": \"/root/autodl-tmp/importance_margin_vla_compress/eval_results/pi05_l2norm_k0.50_libero_object_seed43.json\", \"model_name\": \"pi05_libero_finetuned\", \"pid\": 206999, \"seed\": 43, \"server\": \"westd-41074\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-21T22:03:27.880Z\"}, \"eval_smolvla_official_random_k050_object_seed42\": {\"completed_at\": \"2026-05-21T21:27:06.452Z\", \"conclusion\": \"success\", \"created_at\": \"2026-05-21T15:42:19.468Z\", \"hypothesis\": \"SmolVLA official random k=0.5 (50% removal) will show ~0% SR, confirming SmolVLA cliff-edge at all pruning ratios\", \"log_path\": \"/root/autodl-tmp/importance_margin_vla_compress/eval_results/smolvla_official_random_k050_object_seed42.json\", \"metrics\": {\"overall_sr\": 0, \"per_task_sr\": {\"task0\": 0, \"task1\": 0, \"task2\": 0, \"task3\": 0, \"task4\": 0, \"task5\": 0, \"task6\": 0, \"task7\": 0, \"task8\": 0, \"task9\": 0}, \"total_episodes\": 500, \"total_successes\": 0, \"wilson_ci_95\": [0, 0.0076]}, \"notes\": \"SmolVLA official checkpoint catastrophic degradation at random prune k=0.5 confirmed. 0/500 successes. Cliff-edge at all pruning ratios verified.\", \"retry_count\": 0, \"spec\": {\"checkpoint_path\": \"N/A - eval only\", \"checkpoint_source\": \"HuggingFaceVLA/smolvla_libero\", \"command\": \"python -u eval_official_libero.py --pretrained_dir /root/autodl-tmp/.hf_cache/hub/models--HuggingFaceVLA--smolvla_libero/snapshots/6721902bc4d61e50a3bfdb11dfb4cb626f05d102/ --mode random_prune --k_ratio 0.5 --suite libero_object --num_episodes 50 --gpu 0 --seed 42\", \"data_count\": 500, \"data_path\": \"libero_object\", \"gpu_id\": \"1\", \"log_path\": \"/root/autodl-tmp/importance_margin_vla_compress/eval_results/\", \"model_name\": \"SmolVLA-LIBERO-official\", \"seed\": 42, \"server\": \"cqa1-33015\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-21T21:28:02.923Z\"}, \"eval_smolvla_official_random_k090_object_seed42\": {\"completed_at\": \"2026-05-21T21:27:04.107Z\", \"conclusion\": \"success\", \"created_at\": \"2026-05-21T15:43:22.230Z\", \"hypothesis\": \"SmolVLA official random k=0.9; k=0.95 已 0% SR，确认 cliff-edge 延续到 k=0.9\", \"log_path\": \"/root/autodl-tmp/importance_margin_vla_compress/eval_results/smolvla_official_random_k090_object_seed42.json\", \"metrics\": {\"overall_sr\": 0, \"per_task_sr\": {\"task0\": 0, \"task1\": 0, \"task2\": 0, \"task3\": 0, \"task4\": 0, \"task5\": 0, \"task6\": 0, \"task7\": 0, \"task8\": 0, \"task9\": 0}, \"total_episodes\": 500, \"total_successes\": 0, \"wilson_ci_95\": [0, 0.0076]}, \"notes\": \"SmolVLA official checkpoint catastrophic degradation at random prune k=0.9 confirmed. 0/500 successes. Even 10% removal destroys SmolVLA completely.\", \"retry_count\": 0, \"spec\": {\"checkpoint_path\": \"N/A - eval only\", \"checkpoint_source\": \"HuggingFaceVLA/smolvla_libero\", \"command\": \"python -u eval_official_libero.py --pretrained_dir /root/autodl-tmp/.hf_cache/hub/models--HuggingFaceVLA--smolvla_libero/snapshots/6721902bc4d61e50a3bfdb11dfb4cb626f05d102/ --mode random_prune --k_ratio 0.9 --suite libero_object --num_episodes 50 --gpu 0 --seed 42\", \"data_count\": 500, \"data_path\": \"libero_object\", \"gpu_id\": \"0\", \"log_path\": \"/root/autodl-tmp/importance_margin_vla_compress/eval_results/\", \"model_name\": \"SmolVLA-LIBERO-official\", \"seed\": 42, \"server\": \"cqa1-33015\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-21T21:28:01.433Z\"}, \"eval_smolvla_official_l2norm_k030_object_seed42\": {\"checkpoint_path\": \"N/A - eval only\", \"completed_at\": \"2026-05-21T21:26:55.944Z\", \"conclusion\": \"success\", \"created_at\": \"2026-05-21T15:43:21.066Z\", \"hypothesis\": \"SmolVLA L2-norm k=0.3 on official checkpoint. Expected ~0% SR.\", \"log_path\": \"/root/autodl-tmp/importance_margin_vla_compress/eval_results/smolvla_official_l2norm_k030_object_seed42.json\", \"metrics\": {\"overall_sr\": 0, \"per_task_sr\": {\"task0\": 0, \"task1\": 0, \"task2\": 0, \"task3\": 0, \"task4\": 0, \"task5\": 0, \"task6\": 0, \"task7\": 0, \"task8\": 0, \"task9\": 0}, \"total_episodes\": 500, \"total_successes\": 0, \"wilson_ci_95\": [0, 0.0076]}, \"notes\": \"SmolVLA official checkpoint catastrophic degradation at L2norm prune k=0.3 confirmed. 0/500 successes across all 10 tasks. Hypothesis verified.\", \"retry_count\": 0, \"spec\": {\"checkpoint_source\": \"/root/autodl-tmp/.hf_cache/smolvla_libero_official\", \"command\": \"CUDA_VISIBLE_DEVICES=2 python3 -u eval_official_libero.py --pretrained_dir /root/autodl-tmp/.hf_cache/smolvla_libero_official --suite libero_object --num_episodes 50 --gpu 0 --seed 42 --mode l2_norm --k_ratio 0.3\", \"data_count\": 50, \"data_path\": \"libero_object\", \"eval_data\": \"libero_object\", \"model_name\": \"smolvla_libero_official\", \"seed\": 42, \"server\": \"cqa1-33015\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-21T21:27:58.750Z\"}, \"eval_smolvla_official_random_k070_object_seed42\": {\"checkpoint_path\": \"N/A - eval only\", \"completed_at\": \"2026-05-21T21:26:58.037Z\", \"conclusion\": \"success\", \"created_at\": \"2026-05-21T15:43:23.388Z\", \"hypothesis\": \"SmolVLA random prune k=0.7 on official checkpoint. Expected ~0% SR.\", \"log_path\": \"/root/autodl-tmp/importance_margin_vla_compress/eval_results/smolvla_official_random_k070_object_seed42.json\", \"metrics\": {\"overall_sr\": 0, \"per_task_sr\": {\"task0\": 0, \"task1\": 0, \"task2\": 0, \"task3\": 0, \"task4\": 0, \"task5\": 0, \"task6\": 0, \"task7\": 0, \"task8\": 0, \"task9\": 0}, \"total_episodes\": 500, \"total_successes\": 0, \"wilson_ci_95\": [0, 0.0076]}, \"notes\": \"SmolVLA official checkpoint catastrophic degradation at random prune k=0.7 confirmed. 0/500 successes across all 10 tasks. Hypothesis verified.\", \"retry_count\": 0, \"spec\": {\"checkpoint_source\": \"/root/autodl-tmp/.hf_cache/smolvla_libero_official\", \"command\": \"CUDA_VISIBLE_DEVICES=1 python3 -u eval_official_libero.py --pretrained_dir /root/autodl-tmp/.hf_cache/smolvla_libero_official --suite libero_object --num_episodes 50 --gpu 0 --seed 42 --mode random_prune --k_ratio 0.7\", \"data_count\": 50, \"data_path\": \"libero_object\", \"eval_data\": \"libero_object\", \"model_name\": \"smolvla_libero_official\", \"seed\": 42, \"server\": \"cqa1-33015\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-21T21:27:57.528Z\"}, \"eval_smolvla_official_random_k030_object_seed42\": {\"checkpoint_path\": \"N/A - eval only\", \"completed_at\": \"2026-05-21T21:27:00.344Z\", \"conclusion\": \"success\", \"created_at\": \"2026-05-21T15:43:24.427Z\", \"hypothesis\": \"SmolVLA random prune k=0.3 on official checkpoint. Expected ~0% SR.\", \"log_path\": \"/root/autodl-tmp/importance_margin_vla_compress/eval_results/smolvla_official_random_k030_object_seed42.json\", \"metrics\": {\"overall_sr\": 0, \"per_task_sr\": {\"task0\": 0, \"task1\": 0, \"task2\": 0, \"task3\": 0, \"task4\": 0, \"task5\": 0, \"task6\": 0, \"task7\": 0, \"task8\": 0, \"task9\": 0}, \"total_episodes\": 500, \"total_successes\": 0, \"wilson_ci_95\": [0, 0.0076]}, \"notes\": \"SmolVLA official checkpoint catastrophic degradation at random prune k=0.3 confirmed. 0/500 successes across all 10 tasks. Hypothesis verified.\", \"retry_count\": 0, \"spec\": {\"checkpoint_source\": \"/root/autodl-tmp/.hf_cache/smolvla_libero_official\", \"command\": \"CUDA_VISIBLE_DEVICES=0 python3 -u eval_official_libero.py --pretrained_dir /root/autodl-tmp/.hf_cache/smolvla_libero_official --suite libero_object --num_episodes 50 --gpu 0 --seed 42 --mode random_prune --k_ratio 0.3\", \"data_count\": 50, \"data_path\": \"libero_object\", \"eval_data\": \"libero_object\", \"model_name\": \"smolvla_libero_official\", \"seed\": 42, \"server\": \"cqa1-33015\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-21T21:27:56.235Z\"}, \"eval_smolvla_official_l2norm_k050_object_seed42\": {\"completed_at\": \"2026-05-21T18:13:34.742Z\", \"conclusion\": \"success\", \"created_at\": \"2026-05-21T15:42:18.304Z\", \"hypothesis\": \"SmolVLA official L2norm k=0.5 补 sweep 数据点，预期与 random k=0.5 一样接近 0% SR\", \"metrics\": {\"seed\": 42, \"success_rate\": 0, \"total_episodes\": 500}, \"retry_count\": 0, \"spec\": {\"checkpoint_path\": \"N/A - eval only\", \"checkpoint_source\": \"HuggingFaceVLA/smolvla_libero\", \"command\": \"python -u eval_official_libero.py --mode l2_norm --k_ratio 0.5 --suite libero_object --num_episodes 50 --seed 42\", \"data_count\": 500, \"data_path\": \"libero_object\", \"gpu_id\": \"3\", \"log_path\": \"/root/autodl-tmp/importance_margin_vla_compress/eval_results/\", \"model_name\": \"SmolVLA-LIBERO-official\", \"seed\": 42, \"server\": \"cqa1-33015\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-21T21:21:10.125Z\"}, \"eval_pi05_l2norm_k05_spatial_seed42\": {\"completed_at\": \"2026-05-21T21:04:43.483Z\", \"conclusion\": \"success\", \"created_at\": \"2026-05-21T19:04:43.315Z\", \"extra\": {\"hook_events\": [{\"action\": \"agent\", \"event\": \"on_complete\", \"ts\": \"2026-05-21T21:02:50.761973+00:00\"}]}, \"hypothesis\": \"π0.5 L2norm k=0.5 on LIBERO-Spatial seed42, 验证 CV=0.055 linear projection 下 L2norm 在 Spatial 任务上是否也接近 random（与 Object 上一致）\", \"log_path\": \"~/runs/importance_margin_vla_compress/eval_pi05_l2norm_k05_spatial_seed42.log\", \"metrics\": {\"comparison\": {\"vs_baseline_spatial\": \"55.6 vs 97.2 (-41.6pp)\", \"vs_l2norm_k05_object\": \"55.6 vs 33.4 (+22.2pp)\", \"vs_random_k05_spatial\": \"55.6 vs 71.6 (-16.0pp)\"}, \"elapsed_min\": 108.9, \"overall_sr\": 55.6, \"per_task_sr\": {\"T0_pick_up_black_bowl_between_plate\": 74, \"T1_pick_up_black_bowl_next_to_ramekin\": 82, \"T2_pick_up_black_bowl_on_plate\": 78, \"T3_pick_up_black_bowl_on_cookie_box\": 28, \"T4_pick_up_black_bowl_in_top_drawer\": 38, \"T5_pick_up_black_bowl_on_ramekin\": 44, \"T6_pick_up_black_bowl_next_to_cookie\": 32, \"T7_pick_up_black_bowl_on_stove\": 74, \"T8_pick_up_black_bowl_next_to_plate\": 62, \"T9_pick_up_black_bowl_on_wooden_cab\": 44}, \"total_episodes\": 500, \"total_successes\": 278}, \"reproduce\": {\"finished_at\": \"2026-05-21T21:02:42.865Z\"}, \"retry_count\": 0, \"spec\": {\"account\": \"root\", \"backend\": \"tmux\", \"checkpoint_path\": \"/root/autodl-tmp/pi05_libero_finetuned\", \"checkpoint_source\": \"/root/autodl-tmp/pi05_libero_finetuned\", \"command\": \"python -u eval_pi05_pruning_libero.py --prune_mode l2norm --keep_ratio 0.5 --suite libero_spatial --n_episodes 50 --seed 42 --gpu 1\", \"data_count\": 500, \"data_path\": \"libero_spatial (10 tasks x 50 eps)\", \"eval_data\": \"libero_spatial\", \"gpu\": [\"cuda:1\"], \"gpu_hours\": 1.92, \"log_path\": \"~/runs/importance_margin_vla_compress/eval_pi05_l2norm_k05_spatial_seed42.log\", \"model_name\": \"pi05_libero_finetuned\", \"pid\": \"590423\", \"seed\": 42, \"server\": \"westd-38929\", \"submitted_at\": \"2026-05-21T19:09:44.831Z\", \"submitted_via\": \"submit_training_job\", \"wall_clock_seconds\": 6898.7}, \"status\": \"DONE\", \"updated_at\": \"2026-05-21T21:05:43.902Z\"}, \"eval_pi05_l2norm_k03_spatial_seed42\": {\"completed_at\": \"2026-05-21T21:04:40.771Z\", \"conclusion\": \"negative\", \"created_at\": \"2026-05-21T19:04:48.329Z\", \"extra\": {\"hook_events\": [{\"action\": \"agent\", \"event\": \"on_complete\", \"ts\": \"2026-05-21T21:00:40.481357+00:00\"}]}, \"hypothesis\": \"π0.5 L2norm k=0.3 on LIBERO-Spatial seed42, 验证 k=0.3 处 method reversal (L2norm > random) 是否跨 suite 复现\", \"metrics\": {\"checkpoint_path\": \"/root/autodl-tmp/pi05_libero_finetuned\", \"elapsed_min\": 108.4, \"log_path\": \"~/runs/importance_margin_vla_compress/eval_pi05_l2norm_k03_spatial_seed42.log\", \"overall_sr\": 57.2, \"per_task_sr\": {\"T0_bowl_between_plate\": 62, \"T1_bowl_next_to_ramekin\": 72, \"T2_bowl_from_table_center\": 78, \"T3_bowl_on_cookie_box\": 24, \"T4_bowl_in_top_drawer\": 34, \"T5_bowl_on_ramekin\": 26, \"T6_bowl_next_to_cookie\": 74, \"T7_bowl_on_stove\": 90, \"T8_bowl_next_to_plate\": 66, \"T9_bowl_on_wooden_cabinet\": 46}, \"result_json\": \"/root/autodl-tmp/importance_margin_vla_compress/eval_results/pi05_l2norm_k0.30_libero_spatial_seed42.json\", \"seed\": 42, \"total_episodes\": 500, \"total_successes\": 286}, \"reproduce\": {\"finished_at\": \"2026-05-21T21:00:31.958Z\"}, \"retry_count\": 0, \"spec\": {\"account\": \"root\", \"backend\": \"tmux\", \"checkpoint_path\": \"/root/autodl-tmp/pi05_libero_finetuned\", \"checkpoint_source\": \"/root/autodl-tmp/pi05_libero_finetuned\", \"command\": \"python -u eval_pi05_pruning_libero.py --prune_mode l2norm --keep_ratio 0.3 --suite libero_spatial --n_episodes 50 --seed 42 --gpu 3\", \"data_count\": 500, \"data_path\": \"libero_spatial (10 tasks x 50 eps)\", \"eval_data\": \"libero_spatial\", \"gpu\": [\"cuda:3\"], \"gpu_hours\": 1.91, \"log_path\": \"~/runs/importance_margin_vla_compress/eval_pi05_l2norm_k03_spatial_seed42.log\", \"model_name\": \"pi05_libero_finetuned\", \"pid\": \"590816\", \"seed\": 42, \"server\": \"westd-38929\", \"submitted_at\": \"2026-05-21T19:09:50.353Z\", \"submitted_via\": \"submit_training_job\", \"wall_clock_seconds\": 6890.4}, \"status\": \"DONE\", \"updated_at\": \"2026-05-21T21:04:40.771Z\"}, \"eval_pi05_random_k085_object_seed42\": {\"completed_at\": \"2026-05-21T20:11:53.085Z\", \"conclusion\": \"failed\", \"created_at\": \"2026-05-21T19:04:01.513Z\", \"extra\": {\"hook_events\": [{\"action\": \"agent\", \"event\": \"on_failed\", \"ts\": \"2026-05-21T20:12:03.069992+00:00\"}]}, \"failure_reason\": \"Network unreachable - AutoTokenizer.from_pretrained(\\\"google/paligemma-3b-pt-224\\\") failed, 0 episodes executed. Same root cause as k095 and fixed-mask v1.\", \"hypothesis\": \"π0.5 random k=0.85 seed42: 补充 k=0.7-0.9 之间的数据点。k=0.7→75.5% vs k=0.9→10%，确认 random pruning 曲线在此区间的急剧下降行为，排除 k=0.9 为孤立异常的可能。\", \"parent\": \"eval_pi05_random_k09_object_seed42_v2\", \"reproduce\": {\"finished_at\": \"2026-05-21T20:11:49.422Z\"}, \"retry_count\": 0, \"spec\": {\"account\": \"root\", \"backend\": \"tmux\", \"checkpoint_source\": \"/root/autodl-tmp/pi05_libero_finetuned\", \"command\": \"CUDA_VISIBLE_DEVICES=1 python -u eval_pi05_pruning_libero.py --prune_mode random --keep_ratio 0.85 --n_episodes 50 --suite libero_object --seed 42 --gpu 0\", \"data_count\": 500, \"data_path\": \"libero_object\", \"eval_data\": \"libero_object\", \"gpu\": [\"cuda:1\"], \"gpu_hours\": 0.17, \"gpu_id\": 1, \"log_path\": \"~/runs/importance_margin_vla_compress/eval_pi05_random_k085_object_seed42.log\", \"model_name\": \"pi05_libero_finetuned\", \"pid\": 626630, \"seed\": 42, \"server\": \"westd-41074\", \"submitted_at\": \"2026-05-21T20:01:51.062Z\", \"submitted_via\": \"submit_training_job\", \"wall_clock_seconds\": 602.0}, \"status\": \"DONE\", \"updated_at\": \"2026-05-21T20:15:51.002Z\"}, \"eval_pi05_random_k09_fixedmask_object_seed42\": {\"completed_at\": \"2026-05-21T20:10:50.143Z\", \"conclusion\": \"failed\", \"created_at\": \"2026-05-21T19:09:35.064Z\", \"extra\": {\"hook_events\": [{\"action\": \"agent\", \"event\": \"on_complete\", \"ts\": \"2026-05-21T20:08:30.930267+00:00\"}]}, \"hypothesis\": \"判别 k=0.9 ~10% SR 的根因是 per-call stochastic mask 导致时序不一致还是 random 90% subset 本身不够\", \"metrics\": {\"error\": \"Network unreachable - AutoTokenizer.from_pretrained('google/paligemma-3b-pt-224') failed because AutoDL network was not enabled (source /etc/network_turbo not run). No episodes executed.\", \"overall_sr\": null, \"total_episodes\": 0}, \"parent\": \"eval_pi05_random_k09_object_seed43\", \"reproduce\": {\"finished_at\": \"2026-05-21T20:08:13.719Z\"}, \"retry_count\": 0, \"spec\": {\"account\": \"root\", \"backend\": \"tmux\", \"checkpoint_path\": \"N/A_eval_only\", \"checkpoint_source\": \"/root/autodl-tmp/pi05_libero_finetuned\", \"command\": \"python -u eval_pi05_pruning_libero.py --prune_mode random --keep_ratio 0.9 --suite libero_object --n_episodes 50 --seed 42 --gpu 0 --fixed_mask\", \"data_count\": 500, \"data_path\": \"libero_object\", \"eval_data\": \"libero_object\", \"gpu\": [\"cuda:1\"], \"gpu_hours\": 0.23, \"gpu_id\": 1, \"log_path\": \"/root/autodl-tmp/importance_margin_vla_compress/logs/eval_pi05_random_k09_fixedmask_seed42.log\", \"model_name\": \"pi05_libero_finetuned\", \"pid\": 625841, \"seed\": 42, \"server\": \"westd-41074\", \"submitted_at\": \"2026-05-21T19:57:07.867Z\", \"submitted_via\": \"submit_training_job\", \"wall_clock_seconds\": 822.3}, \"status\": \"DONE\", \"updated_at\": \"2026-05-21T20:10:57.961Z\"}, \"eval_pi05_random_k095_object_seed42\": {\"completed_at\": \"2026-05-21T20:04:44.217Z\", \"conclusion\": \"failed\", \"created_at\": \"2026-05-21T19:03:59.633Z\", \"extra\": {\"hook_events\": [{\"action\": \"agent\", \"event\": \"on_failed\", \"ts\": \"2026-05-21T20:04:53.846959+00:00\"}]}, \"failure_reason\": \"Network unreachable - AutoTokenizer.from_pretrained(\\\"google/paligemma-3b-pt-224\\\") failed, no episodes executed\", \"hypothesis\": \"π0.5 random k=0.95 seed42: 定位 random pruning 单调性违反的精确转折点。k=0.9→10% vs k=0.7→75.5%，去除更少 token 反而更差。如果 k=0.95 也很低，问题在高 retention ratio 本身；如果正常(~95%+)，转折在(0.9,0.95)之间。\", \"parent\": \"eval_pi05_random_k09_object_seed42_v2\", \"reproduce\": {\"finished_at\": \"2026-05-21T20:04:45.682Z\"}, \"retry_count\": 0, \"spec\": {\"account\": \"root\", \"backend\": \"tmux\", \"checkpoint_source\": \"/root/autodl-tmp/pi05_libero_finetuned\", \"command\": \"python -u eval_pi05_pruning_libero.py --prune_mode random --keep_ratio 0.95 --suite libero_object --n_episodes 50 --seed 42 --gpu 0\", \"data_count\": 50, \"data_path\": \"/root/autodl-tmp/importance_margin_vla_compress/\", \"eval_data\": \"libero_object (50 episodes)\", \"gpu\": [\"cuda:0\"], \"gpu_hours\": 0.15, \"log_path\": \"~/runs/importance_margin_vla_compress/eval_pi05_random_k095_object_seed42.log\", \"model_name\": \"pi05_libero_finetuned\", \"pid\": \"625487\", \"seed\": 42, \"server\": \"westd-41074\", \"submitted_at\": \"2026-05-21T19:55:38.624Z\", \"submitted_via\": \"submit_training_job\", \"wall_clock_seconds\": 545.6}, \"status\": \"DONE\", \"updated_at\": \"2026-05-21T20:08:53.282Z\"}, \"eval_pi05_l2norm_k01_object_seed42\": {\"checkpoint_path\": \"N/A_eval_only\", \"completed_at\": \"2026-05-21T19:54:04.430Z\", \"conclusion\": \"success\", \"created_at\": \"2026-05-21T05:45:27.000Z\", \"hypothesis\": \"At extreme compression (keep=10%), L2norm pruning on π0.5 will retain minimal task performance on libero_object, providing a lower-bound data point for the scaling law curve.\", \"log_path\": \"/root/autodl-tmp/importance_margin_vla_compress/logs/eval_pi05_l2norm_k01_seed42.log\", \"metrics\": {\"elapsed_min\": 117.55, \"overall_sr\": 0.026, \"per_task_sr\": {\"T0_alphabet_soup\": 0.02, \"T1_cream_cheese\": 0.06, \"T2_salad_dressing\": 0.04, \"T3_bbq_sauce\": 0.02, \"T4_ketchup\": 0.04, \"T5_tomato_sauce\": 0.02, \"T6_butter\": 0, \"T7_milk\": 0, \"T8_chocolate_pudding\": 0.02, \"T9_orange_juice\": 0.04}, \"total_episodes\": 500, \"total_successes\": 13}, \"parent\": \"eval_pi05_baseline_object_seed42\", \"spec\": {\"checkpoint_source\": \"/root/autodl-tmp/pi05_libero_finetuned\", \"command\": \"python -u eval_pi05_pruning_libero.py --prune_mode l2norm --keep_ratio 0.1 --suite libero_object --n_episodes 50 --seed 42 --gpu 0\", \"data_count\": 50, \"data_path\": \"libero_object\", \"eval_data\": \"libero_object\", \"gpu_id\": 0, \"log_path\": \"/root/autodl-tmp/importance_margin_vla_compress/logs/eval_pi05_l2norm_k01_seed42.log\", \"model_name\": \"pi05_libero_finetuned\", \"pid\": 531007, \"seed\": 42, \"server\": \"westd-41074\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-21T19:54:11.368Z\"}, \"eval_smolvla_official_random_k050_object_seed43\": {\"completed_at\": \"2026-05-21T18:39:45.023Z\", \"conclusion\": \"success\", \"created_at\": \"2026-05-21T17:11:31.520Z\", \"failure_reason\": \"FALSE POSITIVE: Experiment completed successfully (0.0% SR, 0/500). Cron misclassified normal exit as failure.\", \"hypothesis\": \"SmolVLA random k=0.5 seed43 多种子; seed42 在 cqa1 上跑（预期 0% based on cliff-edge），seed43 交叉确认\", \"parent\": \"eval_smolvla_official_baseline_object_seed43\", \"retry_count\": 0, \"spec\": {\"checkpoint_path\": \"N/A_eval_only\", \"checkpoint_source\": \"HuggingFaceVLA/smolvla_libero\", \"command\": \"CUDA_VISIBLE_DEVICES=2 python3 -u eval_official_libero.py --pretrained_dir /root/autodl-tmp/.hf_cache/smolvla_libero_official --suite libero_object --num_episodes 50 --gpu 0 --seed 43 --mode random_prune --k_ratio 0.5\", \"data_count\": 500, \"data_path\": \"libero_object\", \"eval_data\": \"libero_object\", \"gpu_id\": 2, \"log_path\": \"eval_results/smolvla_random_k050_object_seed43.json\", \"model_name\": \"smolvla\", \"seed\": 43, \"server\": \"westd-38929\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-21T18:39:45.023Z\"}, \"eval_smolvla_official_l2norm_k095_object_seed43\": {\"completed_at\": \"2026-05-21T18:24:00.157Z\", \"conclusion\": \"success\", \"created_at\": \"2026-05-21T17:26:19.909Z\", \"extra\": {\"hook_events\": [{\"action\": \"agent\", \"event\": \"on_failed\", \"ts\": \"2026-05-21T18:24:05.907988+00:00\"}]}, \"failure_reason\": \"FALSE POSITIVE: Experiment completed successfully (0.0% SR, 0/500). Process exited normally after finishing all 500 episodes. Cron monitor misclassified normal exit as failure due to no W&B signal. Results saved to eval_results/official_libero_object_l2_norm_k0.95_true_removal.json\", \"hypothesis\": \"SmolVLA L2norm k=0.95 seed43; seed42 sanity=0%, 多种子确认 pixel-shuffle cliff\", \"parent\": \"eval_smolvla_official_baseline_object_seed43\", \"reproduce\": {\"finished_at\": \"2026-05-21T18:23:55.969Z\"}, \"retry_count\": 0, \"spec\": {\"checkpoint_source\": \"HuggingFaceVLA/smolvla_libero\", \"command\": \"CUDA_VISIBLE_DEVICES=3 python3 -u eval_official_libero.py --pretrained_dir /root/autodl-tmp/.hf_cache/smolvla_libero_official --suite libero_object --num_episodes 50 --gpu 0 --seed 43 --mode l2_norm --k_ratio 0.95\", \"data_count\": 500, \"data_path\": \"libero_object\", \"eval_data\": \"libero_object\", \"gpu_id\": 3, \"model_name\": \"smolvla\", \"pid\": 425135, \"seed\": 43, \"server\": \"westd-38929\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-21T18:29:29.357Z\"}, \"eval_smolvla_official_random_k095_object_seed43\": {\"completed_at\": \"2026-05-21T18:24:59.542Z\", \"conclusion\": \"success\", \"created_at\": \"2026-05-21T17:10:51.519Z\", \"extra\": {\"hook_events\": [{\"action\": \"agent\", \"event\": \"on_failed\", \"ts\": \"2026-05-21T18:25:05.368347+00:00\"}]}, \"failure_reason\": \"FALSE POSITIVE: Experiment completed successfully (0.2% SR, 1/500). Process exited normally after finishing all 500 episodes. Cron monitor misclassified normal exit as failure due to no W&B signal. Results saved to eval_results/smolvla_random_prune_k095_object_seed43.json\", \"hypothesis\": \"SmolVLA official checkpoint random k=0.95 seed43; prior seed42 showed near-zero SR at 5% removal, seed43 confirms catastrophic sensitivity to even minimal random pruning in SmolVLA linear connector\", \"reproduce\": {\"finished_at\": \"2026-05-21T18:24:56.164Z\"}, \"retry_count\": 0, \"spec\": {\"checkpoint_source\": \"HuggingFaceVLA/smolvla_libero\", \"command\": \"python3 eval_official_libero.py --pretrained_dir /root/autodl-tmp/.hf_cache/smolvla_libero_official --suite libero_object --num_episodes 50 --gpu 1 --seed 43 --mode random_prune --k_ratio 0.95\", \"data_count\": 500, \"data_path\": \"libero_object\", \"eval_data\": \"libero_object\", \"gpu_id\": 1, \"model_name\": \"smolvla\", \"seed\": 43, \"server\": \"westd-38929\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-21T18:29:27.955Z\"}, \"eval_smolvla_official_baseline_object_seed43\": {\"completed_at\": \"2026-05-21T18:24:44.535Z\", \"conclusion\": \"success\", \"created_at\": \"2026-05-21T17:10:49.196Z\", \"extra\": {\"hook_events\": [{\"action\": \"agent\", \"event\": \"on_failed\", \"ts\": \"2026-05-21T18:24:53.535423+00:00\"}]}, \"failure_reason\": \"FALSE POSITIVE: Experiment completed successfully (59.6% SR, 298/500). Process exited normally after finishing all 500 episodes. Cron monitor misclassified normal exit as failure due to no W&B signal. Results saved to eval_results/smolvla_baseline_object_seed43.json\", \"hypothesis\": \"SmolVLA official checkpoint baseline seed43 on westd-38929; multi-seed verification of unpruned SmolVLA performance on LIBERO-object (paper reports ~87% SR)\", \"reproduce\": {\"finished_at\": \"2026-05-21T18:24:40.937Z\"}, \"retry_count\": 0, \"spec\": {\"checkpoint_source\": \"HuggingFaceVLA/smolvla_libero\", \"command\": \"python3 eval_official_libero.py --pretrained_dir /root/autodl-tmp/.hf_cache/smolvla_libero_official --suite libero_object --num_episodes 50 --gpu 0 --seed 43 --mode baseline\", \"data_count\": 500, \"data_path\": \"libero_object\", \"eval_data\": \"libero_object\", \"gpu_id\": 0, \"model_name\": \"smolvla\", \"seed\": 43, \"server\": \"westd-38929\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-21T18:29:26.445Z\"}, \"eval_smolvla_official_l2norm_k095_object_seed42\": {\"completed_at\": \"2026-05-21T18:13:36.676Z\", \"conclusion\": \"success\", \"created_at\": \"2026-05-21T15:42:14.575Z\", \"hypothesis\": \"SmolVLA official checkpoint with L2-norm pruning at k=0.95 (5% removal) will likely show near-zero SR, confirming SmolVLA's extreme sensitivity to vision token pruning even at minimal removal ratios.\", \"metrics\": {\"seed\": 42, \"success_rate\": 0.4, \"total_episodes\": 500}, \"retry_count\": 0, \"spec\": {\"checkpoint_path\": \"N/A - eval only\", \"log_path\": \"/root/autodl-tmp/importance_margin_vla_compress/eval_results/\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-21T18:13:36.676Z\"}, \"eval_smolvla_official_random_k095_object_seed42\": {\"completed_at\": \"2026-05-21T18:13:32.754Z\", \"conclusion\": \"success\", \"created_at\": \"2026-05-21T15:42:16.529Z\", \"hypothesis\": \"SmolVLA official checkpoint with random pruning at k=0.95 (5% removal) will show near-zero SR, consistent with prior result on our fine-tuned checkpoint (0/500 at k=0.95).\", \"metrics\": {\"seed\": 42, \"success_rate\": 0, \"total_episodes\": 500}, \"retry_count\": 0, \"spec\": {\"checkpoint_path\": \"N/A - eval only\", \"checkpoint_source\": \"HuggingFaceVLA/smolvla_libero\", \"command\": \"python -u eval_official_libero.py --mode random_prune --k_ratio 0.95 --suite libero_object --num_episodes 50 --seed 42\", \"data_count\": 500, \"data_path\": \"libero_object\", \"gpu_id\": \"2\", \"log_path\": \"/root/autodl-tmp/importance_margin_vla_compress/eval_results/\", \"model_name\": \"SmolVLA-LIBERO-official\", \"seed\": 42, \"server\": \"cqa1-33015\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-21T18:13:32.754Z\"}, \"eval_smolvla_official_baseline_object_seed42\": {\"completed_at\": \"2026-05-21T18:13:30.811Z\", \"conclusion\": \"success\", \"created_at\": \"2026-05-21T15:31:26.472Z\", \"hypothesis\": \"Official SmolVLA LIBERO checkpoint (HuggingFaceVLA/smolvla_libero) should achieve ~87% SR on LIBERO-object as reported in the paper, establishing the unpruned baseline for the pruning cliff-edge sweep.\", \"metrics\": {\"note\": \"Official checkpoint, paper reports ~87% - significant gap\", \"seed\": 42, \"success_rate\": 57.2, \"total_episodes\": 500}, \"retry_count\": 0, \"spec\": {\"checkpoint_path\": \"N/A - eval only\", \"checkpoint_source\": \"HuggingFaceVLA/smolvla_libero\", \"command\": \"python -u eval_official_libero.py --pretrained_dir HuggingFaceVLA/smolvla_libero --suite libero_object --mode baseline --num_episodes 50 --gpu 0 --seed 42\", \"data_count\": 500, \"data_path\": \"libero_object\", \"gpu_id\": \"1\", \"log_path\": \"/root/autodl-tmp/importance_margin_vla_compress/eval_results/\", \"model_name\": \"SmolVLA-LIBERO-official\", \"seed\": 42, \"server\": \"cqa1-33015\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-21T18:13:30.811Z\"}, \"eval_openvla_l2norm_k05_object_seed43\": {\"completed_at\": \"2026-05-21T18:13:28.912Z\", \"conclusion\": \"success\", \"created_at\": \"2026-05-21T12:58:41.055Z\", \"hypothesis\": \"OpenVLA L2norm k=0.5 seed43 multi-seed; seed42=39.2%, 验证MLP connector L2norm pruning一致性\", \"metrics\": {\"seed\": 43, \"success_rate\": 39.2, \"total_episodes\": 500}, \"parent\": \"eval_openvla_l2norm_k05_object_seed42_v2\", \"retry_count\": 0, \"spec\": {\"checkpoint_path\": \"N/A - eval only\", \"checkpoint_source\": \"openvla-7b\", \"command\": \"CUDA_VISIBLE_DEVICES=0 python -u /root/autodl-tmp/importance_margin_vla_compress/eval_openvla_l2norm_libero.py --mode l2norm_prune --k_ratio 0.5 --suite libero_object --seed 43\", \"data_count\": 0, \"data_path\": \"libero_object\", \"eval_data\": \"libero_object\", \"gpu_id\": 0, \"log_path\": \"/root/autodl-tmp/importance_margin_vla_compress/eval_results/\", \"model_name\": \"openvla-7b\", \"seed\": 43, \"server\": \"westd-27271\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-21T18:13:28.912Z\"}, \"train_openvla_sc_m64_seed42_v5\": {\"completed_at\": \"2026-05-21T17:52:17.412Z\", \"conclusion\": \"failed\", \"created_at\": \"2026-05-21T08:29:42.217Z\", \"hypothesis\": \"OpenVLA VTC-only M=64 (256→64 tokens, 75% compression) can maintain action prediction quality with cross-attention compression, matching or exceeding M=96/M=128 efficiency-performance tradeoff\", \"parent\": \"train_openvla_sc_m64_seed42_v3\", \"retry_count\": 0, \"spec\": {\"checkpoint_path\": \"checkpoints/openvla_sc_m64_seed42/\", \"checkpoint_source\": \"/root/autodl-tmp/openvla-libero-object\", \"command\": \"CUDA_VISIBLE_DEVICES=3 python -u train_openvla_smart_compress.py --config configs/openvla_smart_compress_m64.yaml\", \"data_count\": 273465, \"data_path\": \"/root/autodl-tmp/importance_margin_vla_compress/\", \"eval_data\": \"HuggingFaceVLA/libero\", \"failure_reason\": \"Silent crash at step 17050/100000 (17%). No traceback — likely SIGKILL (OOM or system kill). Last checkpoint at step 10000. Actual training log was train_m64v6.log (v5 was a failed startup due to network unreachable). Training metrics were normal before crash (loss ~2.8-3.0, grad norm ~0.8-1.0).\", \"gpu\": \"cuda:3\", \"log_path\": \"logs/train_openvla_sc_m64_seed42_v5.log\", \"model_name\": \"openvla-7b\", \"pid\": 996937, \"seed\": 42, \"server\": \"westd-41074\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-21T17:52:17.412Z\"}, \"eval_pi05_l2norm_k09_object_seed42_v2\": {\"completed_at\": \"2026-05-21T17:48:18.083Z\", \"conclusion\": \"success\", \"created_at\": \"2026-05-21T15:52:06.118Z\", \"hypothesis\": \"π0.5 L2norm k=0.9 seed42 v2; 填充 scaling curve k=1.0(98.2%) 到 k=0.7(55.0%) 之间。低 CV=0.055 linear projection 模型在 10% pruning 下 L2norm 表现\", \"metrics\": {\"seed\": 42, \"success_rate\": 98.2, \"total_episodes\": 500, \"total_successes\": 491}, \"parent\": \"eval_pi05_l2norm_k07_object_seed42\", \"retry_count\": 0, \"spec\": {\"checkpoint_path\": \"N/A - eval only\", \"checkpoint_source\": \"/root/autodl-tmp/pi05_libero_finetuned\", \"command\": \"HF_HUB_OFFLINE=1 python -u eval_pi05_pruning_libero.py --prune_mode l2norm --keep_ratio 0.9 --suite libero_object --n_episodes 50 --seed 42 --gpu 0\", \"data_count\": 500, \"data_path\": \"libero_object\", \"eval_data\": \"libero_object\", \"gpu_id\": 0, \"log_path\": \"/root/autodl-tmp/importance_margin_vla_compress/eval_results/\", \"model_name\": \"pi0.5\", \"pid\": 437038, \"seed\": 42, \"server\": \"westd-41074\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-21T17:48:18.083Z\"}, \"eval_openvla_l2norm_k03_object_seed43\": {\"checkpoint_path\": \"N/A\", \"completed_at\": \"2026-05-21T17:25:02.632Z\", \"conclusion\": \"success\", \"created_at\": \"2026-05-21T12:13:31.307Z\", \"hypothesis\": \"OpenVLA L2norm k=0.3 seed43 multi-seed验证; seed42=25.0%(待确认rerun中)，seed43提供第二个数据点确认extreme compression下L2norm表现\", \"log_path\": \"N/A\", \"metrics\": {\"num_episodes\": 500, \"per_task\": {\"alphabet_soup\": 42, \"bbq_sauce\": 10, \"butter\": 8, \"chocolate_pudding\": 28, \"cream_cheese\": 6, \"ketchup\": 66, \"milk\": 36, \"orange_juice\": 26, \"salad_dressing\": 28, \"tomato_sauce\": 0}, \"success_rate\": 25}, \"parent\": \"eval_openvla_l2norm_k03_object_seed42_rerun\", \"retry_count\": 0, \"spec\": {\"checkpoint_source\": \"openvla/openvla-7b\", \"command\": \"CUDA_VISIBLE_DEVICES=3 python -u /root/autodl-tmp/importance_margin_vla_compress/eval_openvla_l2norm_libero.py --mode l2norm_prune --k_ratio 0.3 --suite libero_object --seed 43 --device cuda:0\", \"data_count\": 0, \"data_path\": \"libero_object\", \"eval_data\": \"libero_object\", \"gpu_id\": 3, \"model_name\": \"openvla-7b\", \"seed\": 43, \"server\": \"westd-38929\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-21T17:25:02.632Z\"}, \"eval_openvla_random_k07_object_seed43\": {\"completed_at\": \"2026-05-21T17:10:39.949Z\", \"conclusion\": \"success\", \"created_at\": \"2026-05-21T12:36:00.675Z\", \"hypothesis\": \"OpenVLA random k=0.7 seed43 3rd seed; seed7=49.0%, seed42=44.4%, 差异4.6pp较大，seed43确认均值\", \"metrics\": {\"elapsed_min\": 272.6, \"overall_sr\": 0.526, \"per_task\": {\"alphabet_soup\": 0.84, \"bbq_sauce\": 0.42, \"butter\": 0.1, \"chocolate_pudding\": 0.36, \"cream_cheese\": 0.2, \"ketchup\": 0.7, \"milk\": 0.6, \"orange_juice\": 0.84, \"salad_dressing\": 0.66, \"tomato_sauce\": 0.54}, \"total_episodes\": 500, \"total_successes\": 263}, \"parent\": \"eval_openvla_random_k07_object_seed42_v2\", \"retry_count\": 0, \"spec\": {\"checkpoint_path\": \"/root/autodl-tmp/openvla-libero-object\", \"checkpoint_source\": \"openvla/openvla-7b\", \"command\": \"CUDA_VISIBLE_DEVICES=1 python -u eval_openvla_l2norm_libero.py --mode random_prune --k_ratio 0.7 --suite libero_object --seed 43\", \"data_count\": 0, \"data_path\": \"libero_object\", \"eval_data\": \"libero_object\", \"gpu_id\": 1, \"log_path\": \"/root/autodl-tmp/importance_margin_vla_compress/logs/eval_openvla_random_k07_object_seed43.log\", \"model_name\": \"openvla-7b\", \"seed\": 43, \"server\": \"westd-38929\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-21T17:10:39.949Z\"}, \"eval_openvla_baseline_object_seed42\": {\"checkpoint_path\": \"N/A\", \"completed_at\": \"2026-05-21T16:41:46.064Z\", \"conclusion\": \"success\", \"created_at\": \"2026-05-21T12:03:41.128Z\", \"hypothesis\": \"OpenVLA baseline seed42: 当前 baseline 来自 seed=7 (74.0%)，需 seed=42 作为所有 degradation 计算的锚点。如果 seed42 ≈ 74%，数据一致；差异 >3pp 则需重算所有 degradation。\", \"log_path\": \"logs/eval_openvla_baseline_object_seed42.log\", \"metrics\": {\"num_episodes\": 500, \"source\": \"log extraction - full eval completed but results/ dir missing caused save failure\", \"success_rate\": 74}, \"retry_count\": 0, \"spec\": {\"checkpoint_source\": \"/root/autodl-tmp/openvla-libero-object\", \"command\": \"CUDA_VISIBLE_DEVICES=2 python -u eval_openvla_l2norm_libero.py --mode baseline --suite libero_object --seed 42 --num_episodes 50\", \"data_count\": 50, \"data_path\": \"libero_object (LIBERO env eval)\", \"eval_data\": \"libero_object\", \"gpu_id\": 2, \"log_path\": \"logs/eval_openvla_baseline_object_seed42.log\", \"model_name\": \"openvla-7b\", \"pid\": 363254, \"seed\": 42, \"server\": \"westd-38929\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-21T16:41:46.064Z\"}, \"eval_xvla_l2norm_k03_object_seed44\": {\"checkpoint_path\": \"N/A\", \"completed_at\": \"2026-05-21T16:18:29.109Z\", \"conclusion\": \"success\", \"created_at\": \"2026-05-21T13:23:17.071Z\", \"hypothesis\": \"X-VLA L2norm k=0.3 seed44 3rd seed; seed42=22.2%, seed43=21.0%, 完成triple确认extreme compression下L2norm灾难性\", \"log_path\": \"N/A\", \"metrics\": {}, \"parent\": \"eval_xvla_l2norm_k03_object_seed42\", \"retry_count\": 0, \"spec\": {\"checkpoint_source\": \"/root/autodl-tmp/X-VLA-Libero\", \"command\": \"CUDA_VISIBLE_DEVICES=0 python -u eval_xvla_pruning_libero.py --mode l2_norm --keep_ratio 0.3 --suite libero_object --seed 44 --gpu 0 --num_episodes 50 --model_path /root/autodl-tmp/X-VLA-Libero\", \"data_count\": 500, \"data_path\": \"libero_object\", \"eval_data\": \"libero_object\", \"gpu_id\": 0, \"model_name\": \"X-VLA\", \"seed\": 44, \"server\": \"cqa1-33015\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-21T16:18:29.109Z\"}, \"eval_xvla_random_k07_object_seed42_v2\": {\"checkpoint_path\": \"N/A\", \"completed_at\": \"2026-05-21T16:18:27.125Z\", \"conclusion\": \"success\", \"created_at\": \"2026-05-21T13:17:18.210Z\", \"hypothesis\": \"X-VLA random k=0.7 seed42 multi-seed; seed43=65.0%, seed44=65.0% — expect ~65% confirming random pruning resilience\", \"log_path\": \"N/A\", \"metrics\": {\"num_episodes\": 500, \"success_rate\": 65.2}, \"retry_count\": 0, \"spec\": {\"checkpoint_source\": \"/root/autodl-tmp/X-VLA-Libero\", \"command\": \"python -u eval_xvla_pruning_libero.py --mode random --keep_ratio 0.7 --suite libero_object --seed 42 --gpu 3 --num_episodes 50 --model_path /root/autodl-tmp/X-VLA-Libero\", \"data_count\": 500, \"data_path\": \"libero_object\", \"eval_data\": \"libero_object\", \"gpu_id\": 3, \"model_name\": \"xvla\", \"seed\": 42, \"server\": \"cqa1-33015\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-21T16:18:27.125Z\"}, \"eval_xvla_random_k085_object_seed43\": {\"checkpoint_path\": \"N/A\", \"completed_at\": \"2026-05-21T16:18:25.135Z\", \"conclusion\": \"success\", \"created_at\": \"2026-05-21T12:03:43.362Z\", \"hypothesis\": \"X-VLA random k=0.85 seed43 threshold-graded转折点验证; seed42=63.6%, k=0.85是关键转折点\", \"log_path\": \"N/A\", \"metrics\": {\"num_episodes\": 500, \"success_rate\": 63.2}, \"parent\": \"eval_xvla_random_k085_object_seed42\", \"retry_count\": 0, \"spec\": {\"checkpoint_source\": \"/root/autodl-tmp/X-VLA-Libero\", \"command\": \"CUDA_VISIBLE_DEVICES=2 python -u eval_xvla_pruning_libero.py --mode random --keep_ratio 0.85 --suite libero_object --seed 43 --gpu 0 --num_episodes 50 --model_path /root/autodl-tmp/X-VLA-Libero\", \"data_count\": 50, \"data_path\": \"libero_object\", \"eval_data\": \"libero_object\", \"gpu_id\": 2, \"model_name\": \"X-VLA\", \"seed\": 43, \"server\": \"cqa1-33015\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-21T16:18:25.135Z\"}, \"eval_xvla_random_k085_object_seed42_v2\": {\"checkpoint_path\": \"N/A\", \"completed_at\": \"2026-05-21T16:18:23.258Z\", \"conclusion\": \"success\", \"created_at\": \"2026-05-21T13:24:05.495Z\", \"hypothesis\": \"X-VLA random k=0.85 seed42 v2 rerun; prior seed42=63.6%, seed43在跑，补充cliff boundary random数据\", \"log_path\": \"N/A\", \"metrics\": {\"num_episodes\": 500, \"success_rate\": 63.6}, \"parent\": \"eval_xvla_random_k07_object_seed42\", \"retry_count\": 0, \"spec\": {\"checkpoint_source\": \"/root/autodl-tmp/X-VLA-Libero\", \"command\": \"CUDA_VISIBLE_DEVICES=1 python -u eval_xvla_pruning_libero.py --mode random --keep_ratio 0.85 --suite libero_object --seed 42 --gpu 0 --num_episodes 50 --model_path /root/autodl-tmp/X-VLA-Libero\", \"data_count\": 500, \"data_path\": \"libero_object\", \"eval_data\": \"libero_object\", \"gpu_id\": 1, \"model_name\": \"X-VLA\", \"seed\": 42, \"server\": \"cqa1-33015\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-21T16:18:23.258Z\"}, \"eval_pi05_l2norm_k07_object_seed43\": {\"completed_at\": \"2026-05-21T14:48:51.506Z\", \"conclusion\": \"success\", \"created_at\": \"2026-05-21T11:30:15.371Z\", \"hypothesis\": \"π0.5 L2norm k=0.7 seed43 multi-seed验证D141非单调性; seed42的L2norm k=0.7结果即将出炉(GPU0)，seed43提供第二个数据点确认趋势是否系统性\", \"metrics\": {\"elapsed_min\": 100.3, \"success_rate\": 56.4, \"total_episodes\": 500, \"total_successes\": 282}, \"parent\": \"eval_pi05_l2norm_k07_object_seed42\", \"retry_count\": 0, \"spec\": {\"checkpoint_path\": \"eval_results/pi05_l2norm_k0.70_libero_object_seed43.json\", \"checkpoint_source\": \"/root/autodl-tmp/pi05_libero_finetuned\", \"command\": \"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && HF_HUB_OFFLINE=1 python -u /root/autodl-tmp/importance_margin_vla_compress/eval_pi05_pruning_libero.py --prune_mode l2norm --keep_ratio 0.7 --suite libero_object --n_episodes 50 --seed 43 --gpu 3\", \"data_count\": 500, \"data_path\": \"libero_object\", \"eval_data\": \"libero_object (10 tasks x 50 episodes)\", \"gpu_id\": 3, \"log_path\": \"logs/eval_pi05_random_k07_object_seed43.log\", \"model_name\": \"pi0.5\", \"seed\": 43, \"server\": \"westd-41074\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-21T14:49:05.793Z\"}, \"eval_pi05_l2norm_k07_object_seed42\": {\"completed_at\": \"2026-05-21T14:48:45.793Z\", \"conclusion\": \"success\", \"created_at\": \"2026-05-21T09:32:30.027Z\", \"hypothesis\": \"π0.5 L2norm k=0.7 fills scaling law curve. With L2norm k=0.5=33.4%, expect L2norm k=0.7 > 33.4%. D132 predicts random >> L2norm — compare with random k=0.7 result.\", \"metrics\": {\"elapsed_min\": 91.7, \"success_rate\": 55, \"total_episodes\": 500, \"total_successes\": 275}, \"parent\": \"eval_pi05_l2norm_k05_object_seed42\", \"retry_count\": 0, \"spec\": {\"checkpoint_path\": \"eval_results/pi05_l2norm_k0.70_libero_object.json\", \"checkpoint_source\": \"/root/autodl-tmp/pi05_libero_finetuned\", \"command\": \"HF_HUB_OFFLINE=1 python -u eval_pi05_pruning_libero.py --prune_mode l2norm --keep_ratio 0.7 --suite libero_object --seed 42 --n_episodes 50 --gpu 0\", \"data_count\": 50, \"data_path\": \"/root/autodl-tmp/importance_margin_vla_compress\", \"eval_data\": \"libero_object\", \"gpu\": 0, \"log_path\": \"/tmp/eval_pi05_l2norm_k07_seed42.log\", \"model_name\": \"pi05_libero_finetuned\", \"pid\": 68568, \"seed\": 42, \"server\": \"westd-41074\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-21T14:49:01.972Z\"}, \"eval_xvla_l2norm_k03_object_seed42_v2\": {\"completed_at\": \"2026-05-21T13:23:57.455Z\", \"conclusion\": \"killed\", \"created_at\": \"2026-05-21T13:17:16.261Z\", \"hypothesis\": \"X-VLA l2_norm k=0.3 seed42 multi-seed; seed43=21.0% — expect similar severe degradation at 70% pruning\", \"retry_count\": 0, \"spec\": {\"checkpoint_source\": \"/root/autodl-tmp/X-VLA-Libero\", \"command\": \"python -u eval_xvla_pruning_libero.py --mode l2_norm --keep_ratio 0.3 --suite libero_object --seed 42 --gpu 1 --num_episodes 50 --model_path /root/autodl-tmp/X-VLA-Libero\", \"data_count\": 500, \"data_path\": \"libero_object\", \"eval_data\": \"libero_object\", \"gpu_id\": 1, \"model_name\": \"xvla\", \"seed\": 42, \"server\": \"cqa1-33015\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-21T13:23:57.455Z\"}, \"eval_xvla_l2norm_k085_object_seed43\": {\"completed_at\": \"2026-05-21T13:23:55.563Z\", \"conclusion\": \"killed\", \"created_at\": \"2026-05-21T12:03:38.973Z\", \"hypothesis\": \"X-VLA L2norm k=0.85 seed43 cliff boundary验证; seed42=68.0%, 验证cliff是否在k=0.85稳定存在\", \"parent\": \"eval_xvla_l2norm_k085_object_seed42\", \"retry_count\": 0, \"spec\": {\"checkpoint_source\": \"/root/autodl-tmp/X-VLA-Libero\", \"command\": \"CUDA_VISIBLE_DEVICES=0 python -u eval_xvla_pruning_libero.py --mode l2_norm --keep_ratio 0.85 --suite libero_object --seed 43 --gpu 0 --num_episodes 50 --model_path /root/autodl-tmp/X-VLA-Libero\", \"data_count\": 50, \"data_path\": \"libero_object\", \"eval_data\": \"libero_object\", \"gpu_id\": 0, \"model_name\": \"X-VLA\", \"seed\": 43, \"server\": \"cqa1-33015\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-21T13:23:55.563Z\"}, \"eval_xvla_l2norm_k03_object_seed43\": {\"completed_at\": \"2026-05-21T13:18:35.261Z\", \"conclusion\": \"success\", \"created_at\": \"2026-05-21T09:55:26.639Z\", \"hypothesis\": \"X-VLA L2norm k=0.3 seed43 multi-seed. seed42 running on GPU2. Prior L2norm k=0.3 data: seed43=21.0%, seed44=22.8%. Expect similar ~20-22%. vs random k=0.3 seed42=62.8% → confirms +40pp D132 gap.\", \"metrics\": {\"SR\": 0.21}, \"retry_count\": 0, \"spec\": {\"checkpoint_path\": \"N/A (eval experiment)\", \"checkpoint_source\": \"/root/autodl-tmp/X-VLA-Libero\", \"command\": \"CUDA_VISIBLE_DEVICES=0 python -u eval_xvla_pruning_libero.py --mode l2_norm --keep_ratio 0.3 --suite libero_object --seed 43 --gpu 0 --num_episodes 50 --model_path /root/autodl-tmp/X-VLA-Libero\", \"data_count\": 50, \"data_path\": \"libero_object\", \"eval_data\": \"libero_object\", \"gpu\": \"cuda:0\", \"log_path\": \"logs/eval_xvla_l2norm_k03_object_seed43.log\", \"model_name\": \"X-VLA-Libero\", \"seed\": 43, \"server\": \"cqa1-33015\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-21T13:18:35.261Z\"}, \"eval_xvla_random_k03_object_seed43\": {\"completed_at\": \"2026-05-21T13:18:28.218Z\", \"conclusion\": \"success\", \"created_at\": \"2026-05-21T09:55:28.615Z\", \"hypothesis\": \"X-VLA random k=0.3 seed43 multi-seed. seed42=62.8%. Expect similar ~60-65%. vs L2norm k=0.3 ~21% → confirms D132 gap=+40pp at extreme compression.\", \"metrics\": {\"SR\": 0.662}, \"parent\": \"eval_xvla_random_k03_object_seed42\", \"retry_count\": 0, \"spec\": {\"checkpoint_path\": \"N/A (eval experiment)\", \"checkpoint_source\": \"/root/autodl-tmp/X-VLA-Libero\", \"command\": \"CUDA_VISIBLE_DEVICES=1 python -u eval_xvla_pruning_libero.py --mode random --keep_ratio 0.3 --suite libero_object --seed 43 --gpu 0 --num_episodes 50 --model_path /root/autodl-tmp/X-VLA-Libero\", \"data_count\": 50, \"data_path\": \"libero_object\", \"eval_data\": \"libero_object\", \"gpu\": \"cuda:1\", \"log_path\": \"logs/eval_xvla_random_k03_object_seed43.log\", \"model_name\": \"X-VLA-Libero\", \"seed\": 43, \"server\": \"cqa1-33015\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-21T13:18:28.217Z\"}, \"eval_xvla_random_k07_object_seed44\": {\"completed_at\": \"2026-05-21T13:18:25.708Z\", \"conclusion\": \"success\", \"created_at\": \"2026-05-21T10:33:18.734Z\", \"hypothesis\": \"X-VLA random k=0.7 seed44 3rd seed. seed42=65.2%, seed43=65.0%. Expect ~64-66%.\", \"metrics\": {\"SR\": 0.65}, \"retry_count\": 0, \"spec\": {\"checkpoint_path\": \"N/A (eval experiment)\", \"command\": \"CUDA_VISIBLE_DEVICES=2 python -u eval_xvla_pruning_libero.py --mode random --keep_ratio 0.7 --suite libero_object --seed 44 --gpu 0 --num_episodes 50 --model_path /root/autodl-tmp/X-VLA-Libero\", \"data_count\": 500, \"data_path\": \"libero_object\", \"log_path\": \"eval_results/xvla_random_k0.7_libero_object_seed44.json\", \"model_name\": \"X-VLA\", \"seed\": 44, \"server\": \"cqa1-33015\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-21T13:18:25.708Z\"}, \"eval_xvla_l2norm_k07_object_seed43\": {\"completed_at\": \"2026-05-21T13:18:23.804Z\", \"conclusion\": \"success\", \"created_at\": \"2026-05-21T09:55:30.173Z\", \"hypothesis\": \"X-VLA L2norm k=0.7 seed43 multi-seed. seed42=58.2%, seed44=56.4%. Expect ~56-58%. vs random k=0.7 seed42=65.2%, seed43=65.0% → confirms D132 crossover at k=0.7.\", \"metrics\": {\"SR\": 0.59}, \"parent\": \"eval_xvla_l2norm_k07_object_seed42_v2\", \"retry_count\": 0, \"spec\": {\"checkpoint_path\": \"N/A (eval experiment)\", \"checkpoint_source\": \"/root/autodl-tmp/X-VLA-Libero\", \"command\": \"CUDA_VISIBLE_DEVICES=3 python -u eval_xvla_pruning_libero.py --mode l2_norm --keep_ratio 0.7 --suite libero_object --seed 43 --gpu 0 --num_episodes 50 --model_path /root/autodl-tmp/X-VLA-Libero\", \"data_count\": 50, \"data_path\": \"libero_object\", \"eval_data\": \"libero_object\", \"gpu\": \"cuda:3\", \"log_path\": \"logs/eval_xvla_l2norm_k07_object_seed43.log\", \"model_name\": \"X-VLA-Libero\", \"seed\": 43, \"server\": \"cqa1-33015\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-21T13:18:23.804Z\"}, \"eval_xvla_random_k03_object_seed44\": {\"completed_at\": \"2026-05-21T13:18:21.794Z\", \"conclusion\": \"success\", \"created_at\": \"2026-05-21T11:34:45.497Z\", \"hypothesis\": \"X-VLA random k=0.3 seed44 3rd seed for extreme compression. seed42=62.8%, seed43 running. Expect ~60-65%. vs L2norm k=0.3 ~21% → confirms D132 gap at extreme compression.\", \"metrics\": {\"SR\": 0.63, \"per_task\": [0.74, 0.42, 0.96, 0.8, 0.88, 0.84, 0, 0.74, 0, 0.92]}, \"parent\": \"eval_xvla_random_k03_object_seed42\", \"retry_count\": 0, \"spec\": {\"checkpoint_path\": \"N/A (eval experiment)\", \"checkpoint_source\": \"/root/autodl-tmp/X-VLA-Libero\", \"command\": \"CUDA_VISIBLE_DEVICES=1 python -u eval_xvla_pruning_libero.py --mode random --keep_ratio 0.3 --suite libero_object --seed 44 --gpu 0 --num_episodes 50 --model_path /root/autodl-tmp/X-VLA-Libero\", \"data_count\": 50, \"data_path\": \"libero_object\", \"eval_data\": \"libero_object\", \"gpu_id\": 1, \"log_path\": \"eval_results/xvla_random_k0.3_libero_object_seed44.json\", \"model_name\": \"X-VLA\", \"seed\": 44, \"server\": \"cqa1-33015\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-21T13:18:21.794Z\"}, \"eval_xvla_l2norm_k07_object_seed44\": {\"completed_at\": \"2026-05-21T13:18:19.891Z\", \"conclusion\": \"success\", \"created_at\": \"2026-05-21T11:34:48.607Z\", \"hypothesis\": \"X-VLA L2norm k=0.7 seed44 3rd seed for crossover validation. seed42=58.2%, seed43 running. vs random k=0.7 seed42=65.2% → confirms D132 crossover persists at k=0.7.\", \"metrics\": {\"SR\": 0.564, \"per_task\": [0.96, 0, 1, 0.8, 0.26, 0.9, 0.12, 0.7, 0.02, 0.88]}, \"parent\": \"eval_xvla_l2norm_k07_object_seed42\", \"retry_count\": 0, \"spec\": {\"checkpoint_path\": \"N/A (eval experiment)\", \"checkpoint_source\": \"/root/autodl-tmp/X-VLA-Libero\", \"command\": \"CUDA_VISIBLE_DEVICES=3 python -u eval_xvla_pruning_libero.py --mode l2_norm --keep_ratio 0.7 --suite libero_object --seed 44 --gpu 0 --num_episodes 50 --model_path /root/autodl-tmp/X-VLA-Libero\", \"data_count\": 50, \"data_path\": \"libero_object\", \"eval_data\": \"libero_object\", \"gpu_id\": 3, \"log_path\": \"eval_results/xvla_l2_norm_k0.7_libero_object_seed44.json\", \"model_name\": \"X-VLA\", \"seed\": 44, \"server\": \"cqa1-33015\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-21T13:18:19.891Z\"}, \"eval_pi05_l2norm_k07_object_seed43_v2\": {\"completed_at\": \"2026-05-21T13:03:12.189Z\", \"conclusion\": \"success\", \"created_at\": \"2026-05-21T13:01:13.097Z\", \"hypothesis\": \"π0.5 L2norm k=0.7 seed43 V-shape验证; seed42=55.0%, k=0.5 seed42=33.4%(valley), k=0.3 seed43=55.4%(recovery). 如果seed43 k=0.7也在50-60%范围，V-shape确认为系统性\", \"metrics\": {\"SR\": 0.578, \"elapsed_min\": 91.34, \"per_task\": {\"alphabet_soup\": 0.46, \"bbq_sauce\": 0.8, \"butter\": 0.3, \"chocolate_pudding\": 0.7, \"cream_cheese\": 0.96, \"ketchup\": 0.26, \"milk\": 0.04, \"orange_juice\": 0.46, \"salad_dressing\": 0.8, \"tomato_sauce\": 1}, \"total_episodes\": 500, \"total_successes\": 289}, \"parent\": \"eval_pi05_l2norm_k07_object_seed42\", \"retry_count\": 0, \"spec\": {\"checkpoint_path\": \"/root/autodl-tmp/pi05_libero_finetuned\", \"checkpoint_source\": \"/root/autodl-tmp/pi05_libero_finetuned\", \"command\": \"HF_HUB_OFFLINE=1 python -u eval_pi05_pruning_libero.py --prune_mode l2norm --keep_ratio 0.7 --suite object --n_episodes 50 --seed 43 --gpu 1\", \"data_count\": 500, \"data_path\": \"libero_object\", \"eval_data\": \"libero_object_10tasks_50eps\", \"gpu_id\": 1, \"log_path\": \"/root/autodl-tmp/importance_margin_vla_compress/eval_results/pi05_l2norm_k0.70_libero_object_seed43.json\", \"model_name\": \"pi05_libero_finetuned\", \"pid\": 339730, \"seed\": 43, \"server\": \"westd-41074\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-21T13:03:12.189Z\"}, \"eval_openvla_l2norm_k03_object_seed42_rerun\": {\"completed_at\": \"2026-05-21T12:55:52.232Z\", \"conclusion\": \"success\", \"created_at\": \"2026-05-21T07:54:46.646Z\", \"hypothesis\": \"OpenVLA L2norm k=0.3 rerun to verify prior 25.0% result. If consistent, confirms L2norm pruning curve datapoint for scaling law table.\", \"metrics\": {\"SR\": 0.25, \"elapsed_minutes\": 299.2, \"per_task\": {\"alphabet_soup\": 0.42, \"bbq_sauce\": 0.1, \"butter\": 0.08, \"chocolate_pudding\": 0.28, \"cream_cheese\": 0.06, \"ketchup\": 0.66, \"milk\": 0.36, \"orange_juice\": 0.26, \"salad_dressing\": 0.28, \"tomato_sauce\": 0}, \"total_episodes\": 500, \"total_successes\": 125, \"vision_tokens\": \"256->76\"}, \"retry_count\": 0, \"spec\": {\"checkpoint_path\": \"/root/autodl-tmp/openvla-libero-object\", \"checkpoint_source\": \"/root/autodl-tmp/openvla-libero-object\", \"command\": \"CUDA_VISIBLE_DEVICES=0 python -u eval_openvla_l2norm_libero.py --mode l2norm_prune --k_ratio 0.3 --suite libero_object --seed 42 --num_episodes 50\", \"data_count\": 500, \"data_path\": \"libero_object\", \"eval_data\": \"libero_object\", \"gpu_ids\": [\"cuda:0\"], \"log_path\": \"/root/autodl-tmp/importance_margin_vla_compress/eval_results/openvla_l2norm_prune_k0_3_object.log\", \"model_name\": \"OpenVLA L2norm prune k=0.3\", \"pid\": 193983, \"seed\": 42, \"server\": \"westd-27271\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-21T12:55:59.540Z\"}, \"eval_openvla_random_k03_object_seed42_v2\": {\"completed_at\": \"2026-05-21T12:33:43.536Z\", \"conclusion\": \"success\", \"created_at\": \"2026-05-21T07:24:56.943Z\", \"hypothesis\": \"OpenVLA random k=0.3 seed42: extreme random pruning on high-CV model. Expected poor performance, confirming random is suboptimal for high-CV models.\", \"metrics\": {\"elapsed_min\": 304.1, \"overall_SR\": 0.214, \"per_task\": {\"alphabet_soup\": 0.14, \"bbq_sauce\": 0.3, \"butter\": 0.02, \"chocolate_pudding\": 0.16, \"cream_cheese\": 0, \"ketchup\": 0.26, \"milk\": 0.14, \"orange_juice\": 0.56, \"salad_dressing\": 0.56, \"tomato_sauce\": 0}, \"seed\": 42}, \"retry_count\": 0, \"spec\": {\"checkpoint_path\": \"/root/autodl-tmp/importance_margin_vla_compress/eval_results/openvla_random_prune_k03_object.json\", \"command\": \"CUDA_VISIBLE_DEVICES=1 python -u eval_openvla_l2norm_libero.py --mode random_prune --k_ratio 0.3 --suite libero_object --seed 42\", \"data_count\": 500, \"data_path\": \"libero_object\", \"log_path\": \"/tmp/eval_random_k03_seed42.log\", \"model_name\": \"openvla-7b\", \"pid\": 2478, \"seed\": 42, \"server\": \"westd-38929\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-21T12:33:43.536Z\"}, \"eval_openvla_l2norm_k05_object_seed42_v3\": {\"completed_at\": \"2026-05-21T12:10:39.326Z\", \"conclusion\": \"killed\", \"created_at\": \"2026-05-21T07:31:58.321Z\", \"hypothesis\": \"OpenVLA L2norm k=0.5 seed42 v3: verify prior crash-recovered result of 39.2%. If consistent, confirms MLP connector retains ~40% SR at 50% pruning with importance-based method.\", \"retry_count\": 0, \"spec\": {\"checkpoint_path\": \"N/A - duplicate of v2\", \"command\": \"CUDA_VISIBLE_DEVICES=3 python -u eval_openvla_l2norm_libero.py --mode l2norm_prune --k_ratio 0.5 --suite libero_object --seed 42 --device cuda:0\", \"data_count\": 500, \"data_path\": \"libero_object\", \"log_path\": \"/tmp/eval_l2norm_k05_seed42.log\", \"model_name\": \"openvla-libero-object\", \"seed\": 42, \"server\": \"westd-38929\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-21T12:10:39.326Z\"}, \"eval_openvla_l2norm_k07_object_seed42_v2\": {\"completed_at\": \"2026-05-21T11:56:16.061Z\", \"conclusion\": \"success\", \"created_at\": \"2026-05-21T07:24:55.216Z\", \"extra\": {\"hook_events\": [{\"action\": \"agent\", \"event\": \"on_failed\", \"ts\": \"2026-05-21T11:56:24.911436+00:00\"}]}, \"failure_reason\": \"误判: cron 因缺少 W&B/sentinel 标记为 failed，实际 eval 正常完成 (249/500, 49.8%)\", \"hypothesis\": \"OpenVLA L2norm k=0.7 seed42: fills L2norm curve gap. MLP connector high CV should benefit from importance-based pruning.\", \"metrics\": {\"overall_sr\": 0.498, \"total_episodes\": 500, \"total_successes\": 249}, \"notes\": \"Cron 误判 failed。日志显示实验完成: Overall SR 49.8% (249/500)。结果文件: /root/autodl-tmp/importance_margin_vla_compress/eval_results/openvla_l2norm_prune_k07_object.json\", \"reproduce\": {\"finished_at\": \"2026-05-21T11:56:20.473Z\"}, \"retry_count\": 0, \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=0 python -u eval_openvla_l2norm_libero.py --mode l2norm_prune --k_ratio 0.7 --suite libero_object --seed 42\", \"data_count\": 500, \"data_path\": \"libero_object\", \"log_path\": \"/tmp/eval_l2norm_k07_seed42.log\", \"model_name\": \"openvla-7b\", \"pid\": 1945, \"seed\": 42, \"server\": \"westd-38929\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-21T11:58:44.252Z\"}, \"eval_pi05_random_k07_object_seed42\": {\"completed_at\": \"2026-05-21T10:49:40.934Z\", \"conclusion\": \"success\", \"created_at\": \"2026-05-21T09:11:18.283Z\", \"hypothesis\": \"π0.5 random k=0.7 fills scaling law curve. With random k=0.5=69.4% and baseline=98.2%, expect k=0.7 > 69.4%. D132 predicts random >> L2norm at this k.\", \"metrics\": {\"elapsed_min\": 83.1, \"overall_sr\": 0.772, \"total_episodes\": 500, \"total_successes\": 386}, \"parent\": \"eval_pi05_random_k05_object_seed42\", \"retry_count\": 0, \"spec\": {\"checkpoint_path\": \"/root/autodl-tmp/pi05_libero_finetuned\", \"checkpoint_source\": \"/root/autodl-tmp/pi05_libero_finetuned\", \"command\": \"HF_HUB_OFFLINE=1 python -u eval_pi05_pruning_libero.py --prune_mode random --keep_ratio 0.7 --suite libero_object --seed 42 --n_episodes 50 --gpu 3\", \"data_count\": 50, \"data_path\": \"/root/autodl-tmp/importance_margin_vla_compress\", \"eval_data\": \"libero_object\", \"gpu\": 3, \"log_path\": \"/root/autodl-tmp/importance_margin_vla_compress/eval_results/pi05_random_k0.70_libero_object.json\", \"model_name\": \"pi05_libero_finetuned\", \"pid\": 51513, \"seed\": 42, \"server\": \"westd-41074\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-21T10:49:40.934Z\"}, \"eval_xvla_l2norm_k03_object_seed42\": {\"completed_at\": \"2026-05-21T10:34:59.000Z\", \"conclusion\": \"success\", \"created_at\": \"2026-05-21T08:09:53.939Z\", \"hypothesis\": \"X-VLA L2norm k=0.3 seed42: completes seed42 L2norm curve. seed43=21%, seed44=22.8%. Expected ~20-23%. With random k=0.3=62.8%, this confirms D132 gap of ~40pp at extreme pruning.\", \"metrics\": {\"notes\": \"3 tasks at 0% SR (catastrophic). vs random k=0.3=62.8% → gap +40.6pp confirms D132.\", \"per_task\": [26, 0, 32, 40, 18, 46, 0, 24, 0, 36], \"success_rate\": 0.222, \"total_episodes\": 500, \"total_successes\": 111, \"wilson_ci_95\": [0.188, 0.26]}, \"parent\": \"eval_xvla_prune_k03_seed43\", \"retry_count\": 0, \"spec\": {\"checkpoint_source\": \"/root/autodl-tmp/X-VLA-Libero\", \"command\": \"CUDA_VISIBLE_DEVICES=2 python -u eval_xvla_pruning_libero.py --keep_ratio 0.30 --suite libero_object --seed 42 --num_episodes 50 --gpu 0 --mode l2_norm --model_path /root/autodl-tmp/X-VLA-Libero\", \"data_count\": 50, \"data_path\": \"libero_object\", \"eval_data\": \"libero_object\", \"model_name\": \"X-VLA\", \"seed\": 42, \"server\": \"cqa1-33015\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-21T10:34:59.000Z\"}, \"eval_pi05_l2norm_k03_object_seed42\": {\"completed_at\": \"2026-05-21T09:28:46.000Z\", \"conclusion\": \"success\", \"created_at\": \"2026-05-21T07:32:23.526Z\", \"extra\": {\"hook_events\": [{\"action\": \"agent\", \"event\": \"on_failed\", \"ts\": \"2026-05-21T09:22:55.524240+00:00\"}]}, \"failure_reason\": \"process dead 5× with no sentinel/W&B — auto-resolved as failed\", \"hypothesis\": \"π0.5 L2norm k=0.3 seed42: if L2norm k=0.5 = 33.4%, L2norm k=0.3 should be even worse (<20%). Establishes that L2norm pruning on near-uniform importance distributions (CV=0.055) is catastrophic at all aggressive ratios.\", \"metrics\": {\"notes\": \"D140: L2norm reversal at k=0.3 - L2norm > random for pi0.5\", \"success_rate\": 0.51, \"total_episodes\": 500, \"total_successes\": 255}, \"parent\": \"eval_pi05_l2norm_k05_object_seed42\", \"reproduce\": {\"finished_at\": \"2026-05-21T09:22:43.352Z\"}, \"retry_count\": 0, \"spec\": {\"checkpoint_source\": \"/root/autodl-tmp/pi05_libero_finetuned\", \"command\": \"python -u eval_pi05_pruning_libero.py --prune_mode l2norm --keep_ratio 0.3 --suite libero_object --seed 42 --n_episodes 50 --gpu 0\", \"data_count\": 50, \"data_path\": \"libero_object\", \"eval_data\": \"libero_object\", \"model_name\": \"pi05_libero_finetuned\", \"seed\": 42, \"server\": \"westd-41074\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-21T09:28:46.000Z\"}, \"eval_pi05_random_k03_object_seed42\": {\"completed_at\": \"2026-05-21T09:28:46.000Z\", \"conclusion\": \"success\", \"created_at\": \"2026-05-21T07:26:07.844Z\", \"extra\": {\"hook_events\": [{\"action\": \"agent\", \"event\": \"on_failed\", \"ts\": \"2026-05-21T09:22:06.697100+00:00\"}]}, \"failure_reason\": \"process dead 5× with no sentinel/W&B — auto-resolved as failed\", \"hypothesis\": \"π0.5 (CV=0.055, linear projection) random k=0.3: extreme pruning removing 70% of tokens. If SR remains >50%, confirms π0.5 is truly immune to random pruning even at extreme ratios, supporting Immune class designation.\", \"metrics\": {\"success_rate\": 0.364, \"total_episodes\": 500, \"total_successes\": 182}, \"parent\": \"eval_pi05_random_k05_object_seed42\", \"reproduce\": {\"finished_at\": \"2026-05-21T09:21:52.567Z\"}, \"retry_count\": 0, \"spec\": {\"checkpoint_source\": \"/root/autodl-tmp/pi05_libero_finetuned (official)\", \"command\": \"CUDA_VISIBLE_DEVICES=1 python -u eval_pi05_pruning_libero.py --prune_mode random --keep_ratio 0.3 --suite libero_object --seed 42 --n_episodes 50 --gpu 0\", \"data_count\": 500, \"data_path\": \"libero_object\", \"eval_data\": \"libero_object (10 tasks × 50 episodes)\", \"gpu_ids\": [\"cuda:1\"], \"log_path\": \"/root/autodl-tmp/importance_margin_vla_compress/logs/eval_pi05_random_k03_object_seed42.log\", \"model_name\": \"pi0.5 + random k=0.3\", \"pid\": 914714, \"seed\": 42, \"server\": \"westd-41074\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-21T09:28:46.000Z\"}, \"eval_xvla_random_k05_object_seed44\": {\"completed_at\": \"2026-05-21T09:28:46.000Z\", \"conclusion\": \"success\", \"created_at\": \"2026-05-21T07:59:36.900Z\", \"extra\": {\"hook_events\": [{\"action\": \"agent\", \"event\": \"on_failed\", \"ts\": \"2026-05-21T09:25:45.945326+00:00\"}]}, \"failure_reason\": \"process dead 5× with no sentinel/W&B — auto-resolved as failed\", \"hypothesis\": \"X-VLA random k=0.5 seed44: third seed for D132 verification. seed42=70.6%, seed43=71.0%. If seed44 ≈ 70%, confirms D132 gap (random >> L2norm at k=0.5) is robust across 3 seeds.\", \"metrics\": {\"notes\": \"3rd seed confirms D132: random k=0.5 seed42=70.6%, seed43=71.0%, seed44=69.2%\", \"success_rate\": 0.692, \"total_episodes\": 500, \"total_successes\": 346}, \"parent\": \"eval_xvla_random_k05_object_seed42\", \"reproduce\": {\"finished_at\": \"2026-05-21T09:25:37.135Z\"}, \"retry_count\": 0, \"spec\": {\"checkpoint_source\": \"/root/autodl-tmp/X-VLA-Libero\", \"command\": \"CUDA_VISIBLE_DEVICES=3 python -u eval_xvla_pruning_libero.py --keep_ratio 0.50 --suite libero_object --seed 44 --num_episodes 50 --gpu 0 --mode random --model_path /root/autodl-tmp/X-VLA-Libero\", \"data_count\": 50, \"data_path\": \"libero_object\", \"eval_data\": \"libero_object\", \"gpu\": \"cuda:3\", \"log_path\": \"/root/autodl-tmp/importance_margin_vla_compress/logs/eval_xvla_random_k05_object_seed44.log\", \"model_name\": \"X-VLA-Libero\", \"pid\": 660315, \"seed\": 44, \"server\": \"cqa1-33015\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-21T09:28:46.000Z\"}, \"eval_pi05_random_k05_object_seed42\": {\"completed_at\": \"2026-05-21T09:07:16.526Z\", \"conclusion\": \"success\", \"created_at\": \"2026-05-21T05:45:27.000Z\", \"hypothesis\": \"π0.5 (CV=0.055, linear projection) random k=0.5: D132 predicts random pruning effective for low-CV models. If SR remains high (>90%), confirms immune class even at 50% token removal. If SR drops, establishes pruning threshold for near-uniform importance distributions.\", \"metrics\": {\"comparison\": {\"baseline_sr\": 0.982, \"l2norm_k05_sr\": 0.334, \"random_vs_l2norm_gap\": \"+36.0pp\", \"retention_rate\": \"70.7%\"}, \"elapsed_min\": 94.9, \"overall_sr\": 0.694, \"per_task_sr\": {\"alphabet_soup\": 0.92, \"bbq_sauce\": 0.6, \"butter\": 0.88, \"chocolate_pudding\": 0.78, \"cream_cheese\": 0.78, \"ketchup\": 0.6, \"milk\": 0.54, \"orange_juice\": 0.58, \"salad_dressing\": 0.68, \"tomato_sauce\": 0.58}, \"total_episodes\": 500, \"total_successes\": 347}, \"notes\": \"Original PID 899206 crashed (Network unreachable, tokenizer download failed). Restarted as PID 912501→912506 on GPU 0 at 15:21 with HF_HUB_OFFLINE=1 and HF_HOME=/root/autodl-tmp/.hf_cache.\", \"parent\": \"eval_pi05_baseline_object_seed42\", \"spec\": {\"checkpoint_path\": \"/root/autodl-tmp/importance_margin_vla_compress/eval_results/pi05_random_k0.50_libero_object.json\", \"checkpoint_source\": \"/root/autodl-tmp/pi05_libero_finetuned\", \"command\": \"python eval_pi05_pruning_libero.py --prune_mode random --keep_ratio 0.5 --suite libero_object --seed 42\", \"data_count\": 500, \"data_path\": \"libero_object\", \"eval_data\": \"LIBERO-Object (10 tasks × 50 episodes)\", \"log_path\": \"/root/autodl-tmp/importance_margin_vla_compress/eval_results/pi05_random_k0.50_libero_object.json\", \"model_name\": \"pi0.5\", \"seed\": 42, \"server\": \"westd-41074\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-21T09:07:16.526Z\"}, \"eval_xvla_l2norm_k07_object_seed42_v2\": {\"checkpoint_path\": \"/root/autodl-tmp/importance_margin_vla_compress/eval_results/xvla_prune_k0.7_libero_object.json\", \"completed_at\": \"2026-05-21T08:08:03.496Z\", \"conclusion\": \"success\", \"created_at\": \"2026-05-21T06:36:31.607Z\", \"hypothesis\": \"X-VLA L2norm k=0.7 seed42 fills curve gap. With random k=0.7=65.2%, if L2norm k=0.7 < 65.2%, confirms D132 crossover extends to k=0.7 (not just k=0.5). Expected ~56% based on seed44=56.4%.\", \"log_path\": \"/root/autodl-tmp/importance_margin_vla_compress/logs/eval_xvla_l2norm_k07_object_seed42_v2.log\", \"metrics\": {\"notes\": \"Reviewer confirmed. westd-38929=56.2% vs cqa1=58.2%, 2pp diff acceptable.\", \"per_task\": [96, 2, 100, 78, 34, 90, 18, 0, 70, 94], \"success_rate\": 0.582, \"total_episodes\": 500, \"total_successes\": 291}, \"retry_count\": 0, \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=2 python -u eval_xvla_pruning_libero.py --model_path /root/autodl-tmp/X-VLA-Libero --keep_ratio 0.70 --suite libero_object --seed 42 --num_episodes 50 --gpu 0 --mode l2_norm\", \"data_count\": 500, \"data_path\": \"libero_object\", \"gpu_ids\": [2], \"model_name\": \"X-VLA\", \"seed\": 42, \"server\": \"cqa1-33015\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-21T08:42:43.884Z\"}, \"train_openvla_sc_m64_seed42_v4\": {\"completed_at\": \"2026-05-21T08:06:54.938Z\", \"conclusion\": \"failed\", \"created_at\": \"2026-05-21T02:48:11.429230+00:00\", \"extra\": {\"hook_events\": [{\"action\": \"agent\", \"event\": \"on_failed\", \"ts\": \"2026-05-21T08:07:00.398497+00:00\"}]}, \"failure_reason\": \"DISK_FULL: PytorchStreamWriter failed at step 10000 checkpoint save. Same root cause as v3.\", \"hypothesis\": \"Smart Compress M=64 retraining with save_every=10000 (v3 lost 50K steps due to disk full crash).\", \"metrics\": {\"note\": \"Previous run crashed at 50K. Current run restarted from 0.\", \"steps_completed\": \"from_step_0_restart\", \"steps_total\": 100000}, \"notes\": \"失败原因: 磁盘满 — torch.save checkpoint 时 PytorchStreamWriter failed writing file (与 v3 相同根因). 训练正常到 step 10000 (loss~3.0, 稳定下降), 在 save_checkpoint(step=10000) 时磁盘写满崩溃. | 已有成果: 10K steps 完成但无 checkpoint 保存. | 建议: 清理 westd-41074 磁盘后重启 v5\", \"parent\": \"train_openvla_sc_m64_seed42_v3\", \"reproduce\": {\"finished_at\": \"2026-05-21T08:06:51.764Z\"}, \"spec\": {\"checkpoint_source\": \"train_openvla_sc_m64_seed42_v3\", \"command\": \"bash -c 'source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && python train.py --m 64 --seed 42 --save_every 10000'\", \"data_count\": 273000, \"data_path\": \"/root/autodl-tmp/importance_margin_vla_compress/\", \"eval_data\": \"N/A - this is a training experiment, not eval\", \"gpu\": \"cuda:3\", \"gpu_ids\": [\"cuda:3\"], \"model_name\": \"OpenVLA VTC M=64\", \"note\": \"Restarted from step 0 (all previous checkpoints lost). Currently training from scratch. save_every=10000.\", \"pid\": 738642, \"seed\": 42, \"server\": \"westd-41074\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-21T08:09:24.294Z\"}, \"eval_xvla_random_k07_object_seed43_v2\": {\"completed_at\": \"2026-05-21T07:56:46.397Z\", \"conclusion\": \"success\", \"created_at\": \"2026-05-21T07:27:59.620Z\", \"hypothesis\": \"X-VLA random k=0.7 seed43 v2: re-run with correct --mode random. seed42=65.2%. Multi-seed verification of non-monotonicity (k=0.5=70.6% > k=0.7=65.2%). If seed43 also shows k=0.7 < k=0.5, confirms non-monotonicity is reproducible.\", \"metrics\": {\"success_rate\": 0.65, \"total_episodes\": 500, \"total_successes\": 325, \"wilson_ci_95\": [0.6072, 0.6905]}, \"parent\": \"eval_xvla_random_k07_object_seed42\", \"retry_count\": 0, \"spec\": {\"checkpoint_path\": \"/root/autodl-tmp/X-VLA-Libero\", \"checkpoint_source\": \"/root/autodl-tmp/X-VLA-Libero\", \"command\": \"CUDA_VISIBLE_DEVICES=0 python -u eval_xvla_pruning_libero.py --keep_ratio 0.70 --suite libero_object --seed 43 --num_episodes 50 --gpu 0 --mode random --model_path /root/autodl-tmp/X-VLA-Libero\", \"data_count\": 500, \"data_path\": \"libero_object\", \"eval_data\": \"libero_object (10 tasks x 50 episodes)\", \"log_path\": \"/root/autodl-tmp/importance_margin_vla_compress/eval_results/xvla_prune_k0.7_libero_object.json\", \"model_name\": \"X-VLA-Libero\", \"seed\": 43, \"server\": \"cqa1-33015\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-21T07:56:46.397Z\"}, \"eval_openvla_sc_m128_object_seed42_v2\": {\"checkpoint_path\": \"N/A\", \"completed_at\": \"2026-05-21T07:53:41.938Z\", \"conclusion\": \"failed\", \"created_at\": \"2026-05-21T06:34:48.000Z\", \"hypothesis\": \"OpenVLA SC M128 eval with properly merged LoRA checkpoint (v1 had 291 missing keys due to adapter format). PEFT merge_and_unload applied. Expected SR near baseline 74% if VTC M128 training was successful.\", \"log_path\": \"N/A\", \"metrics\": {\"failure_reason\": \"7/7 episodes FAIL (280-step timeout), model output invalid after LoRA merge. Killed by Director.\"}, \"parent\": \"eval_openvla_sc_m128_object_seed42\", \"retry_count\": 0, \"spec\": {\"checkpoint_source\": \"M128 LoRA adapter merged via PEFT merge_and_unload\", \"command\": \"CUDA_VISIBLE_DEVICES=0 python -u eval_openvla_sc_libero.py --n_queries 128 --checkpoint_path checkpoints/m128_merged --suite libero_object --num_episodes 50 --gpu 0 --seed 42\", \"data_count\": 500, \"data_path\": \"libero_object\", \"gpu_ids\": [\"cuda:0\"], \"model_name\": \"OpenVLA + VisionTokenCompressor(M=128)\", \"pid\": 188248, \"seed\": 42, \"server\": \"westd-27271\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-21T07:53:56.189Z\"}, \"eval_openvla_random_k07_object_seed42\": {\"conclusion\": \"failed\", \"created_at\": \"2026-05-21T07:24:58.705Z\", \"hypothesis\": \"OpenVLA random k=0.7 seed42: D132 crossover comparison. High-CV model → L2norm should beat random at this ratio.\", \"metrics\": {\"failure_reason\": \"Process never started — empty log, command failure on westd-38929\"}, \"retry_count\": 0, \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=2 python -u eval_openvla_l2norm_libero.py --mode random_prune --k_ratio 0.7 --suite libero_object --seed 42\", \"data_count\": 500, \"data_path\": \"libero_object\", \"log_path\": \"/tmp/eval_random_k07_seed42.log\", \"model_name\": \"openvla-7b\", \"pid\": 3110, \"seed\": 42, \"server\": \"westd-38929\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-21T07:30:01.000Z\"}, \"eval_pi05_l2norm_k05_object_seed42\": {\"completed_at\": \"2026-05-21T07:26:04.777Z\", \"conclusion\": \"negative\", \"created_at\": \"2026-05-21T05:45:27.000Z\", \"hypothesis\": \"π0.5 L2norm pruning k=0.5 on Object. CV=0.055 predicts immunity: if SR stays ~96% at 50% token removal, confirms linear projection → uniform importance → pruning immune.\", \"metrics\": {\"elapsed_minutes\": 95.6, \"keep_ratio\": 0.5, \"num_episodes\": 500, \"per_task\": {\"alphabet_soup\": 0.5, \"bbq_sauce\": 0.0, \"butter\": 0.28, \"chocolate_pudding\": 0.38, \"cream_cheese\": 0.14, \"ketchup\": 0.54, \"milk\": 0.64, \"orange_juice\": 0.48, \"salad_dressing\": 0.0, \"tomato_sauce\": 0.38}, \"seed\": 42, \"success_rate\": 33.4, \"total_successes\": 167}, \"parent\": \"eval_pi05_baseline_object_seed42\", \"spec\": {\"checkpoint_path\": \"/root/autodl-tmp/pi05_libero_finetuned\", \"checkpoint_source\": \"/root/autodl-tmp/pi05_libero_finetuned (official)\", \"command\": \"CUDA_VISIBLE_DEVICES=0 python eval_pi05_pruning_libero.py --suite libero_object --prune_mode l2norm --keep_ratio 0.5 --seed 42 --n_episodes 50 --gpu 0\", \"data_count\": 500, \"data_path\": \"libero_object\", \"gpu_ids\": [\"cuda:0\"], \"log_path\": \"/root/autodl-tmp/importance_margin_vla_compress/logs/eval_pi05_l2norm_k05_object_seed42.log\", \"model_name\": \"pi0.5 + L2norm k=0.5\", \"pid\": 838823, \"seed\": 42, \"server\": \"westd-41074\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-21T07:28:33.000Z\"}, \"eval_xvla_random_k07_object_seed43\": {\"completed_at\": \"2026-05-21T07:22:05.150Z\", \"conclusion\": \"failed\", \"created_at\": \"2026-05-21T06:15:13.000Z\", \"extra\": {\"hook_events\": [{\"action\": \"agent\", \"event\": \"on_failed\", \"ts\": \"2026-05-21T07:22:10.331919+00:00\"}]}, \"failure_reason\": \"process dead 5× with no sentinel/W&B — auto-resolved as failed\", \"hypothesis\": \"X-VLA random pruning k=0.7 seed43 verifies D132 non-monotonicity (seed42: k=0.7=65.2% < k=0.5=70.6%). If seed43 also shows k=0.5 > k=0.7, the non-monotonicity is reproducible and points to architectural property, not noise.\", \"metrics\": {}, \"notes\": \"Confirmed failed: no random k=0.7 seed43 result on disk. The file xvla_prune_k0.7_libero_object_seed43.json is actually l2_norm_prune mode (SR=59.0%), not random. Experiment was likely launched with wrong --mode or never ran. GPU freed.\", \"parent\": \"eval_xvla_random_k07_object_seed42\", \"reproduce\": {\"finished_at\": \"2026-05-21T07:22:02.198Z\"}, \"retry_count\": 0, \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=1 python eval_xvla_pruning_libero.py --keep_ratio 0.70 --suite libero_object --seed 43 --n_episodes 50 --gpu 0 --mode random\", \"data_count\": 500, \"data_path\": \"libero_object\", \"gpu_ids\": [\"cuda:1\"], \"model_name\": \"X-VLA\", \"pid\": 223594, \"seed\": 43, \"server\": \"cqa1-33015\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-21T07:24:45.003Z\"}, \"eval_openvla_l2norm_k03_object_seed42\": {\"completed_at\": \"2026-05-21T07:03:04.168Z\", \"conclusion\": \"success\", \"created_at\": \"2026-05-21T05:46:57.000Z\", \"extra\": {\"hook_events\": [{\"action\": \"agent\", \"event\": \"on_failed\", \"ts\": \"2026-05-21T07:03:32.287541+00:00\"}]}, \"failure_reason\": \"process dead 5× with no sentinel/W&B — auto-resolved as failed\", \"hypothesis\": \"OpenVLA L2norm pruning k=0.3 on Object. Most aggressive L2norm point.\", \"metrics\": {\"failure_reason\": \"AutoDL container restart at 14:50:19 UTC killed process. Was at Task 4/10 (~40%). GPU count dropped from 4 to 1 after restart.\", \"k_ratio\": 0.3, \"note\": \"Prior complete result found on disk after container crash. Current run crashed at Task 4/10.\", \"success_rate\": 25.0}, \"reproduce\": {\"finished_at\": \"2026-05-21T07:03:06.013Z\"}, \"spec\": {\"command\": \"eval_openvla_l2norm_libero.py --mode l2norm --k_ratio 0.3 --suite libero_object --seed 42\", \"data_count\": 500, \"data_path\": \"libero_object\", \"gpu_ids\": [\"cuda:3\"], \"model_name\": \"OpenVLA + L2norm k=0.3\", \"pid\": 570309, \"seed\": 42, \"server\": \"westd-38929\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-21T07:20:13.000Z\"}, \"eval_openvla_l2norm_k05_object_seed42\": {\"completed_at\": \"2026-05-21T07:01:56.552Z\", \"conclusion\": \"success\", \"created_at\": \"2026-05-21T05:46:57.000Z\", \"failure_reason\": \"process dead 5× with no sentinel/W&B — auto-resolved as failed\", \"hypothesis\": \"OpenVLA L2norm pruning k=0.5 on Object. Complement random k=0.5 (35.8%) data point.\", \"metrics\": {\"failure_reason\": \"AutoDL container restart at 14:50:19 UTC killed process. Was at Task 4/10 (~40%). GPU count dropped from 4 to 1 after restart.\", \"k_ratio\": 0.5, \"note\": \"Prior complete result found on disk after container crash. Current run crashed at Task 4/10.\", \"success_rate\": 39.2}, \"notes\": \"失败原因: process dead 5× with no sentinel/W&B — 与 westd-38929 上其他 3 个 OpenVLA eval 同批次失败。诊断 Worker 已在运行中（worker_diagnose_openvla_batch_fail_westd38929_20260521T070441 等）。待诊断结果后重试。\", \"reproduce\": {\"finished_at\": \"2026-05-21T07:01:53.729Z\"}, \"spec\": {\"command\": \"eval_openvla_l2norm_libero.py --mode l2norm --k_ratio 0.5 --suite libero_object --seed 42\", \"data_count\": 500, \"data_path\": \"libero_object\", \"gpu_ids\": [\"cuda:0\"], \"model_name\": \"OpenVLA + L2norm k=0.5\", \"pid\": 568225, \"seed\": 42, \"server\": \"westd-38929\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-21T07:20:13.000Z\"}, \"eval_openvla_random_k03_object_seed42\": {\"completed_at\": \"2026-05-21T07:02:11.760Z\", \"conclusion\": \"failed\", \"created_at\": \"2026-05-21T05:46:57.000Z\", \"extra\": {\"hook_events\": [{\"action\": \"agent\", \"event\": \"on_failed\", \"ts\": \"2026-05-21T07:02:20.729363+00:00\"}]}, \"failure_reason\": \"process dead 5× with no sentinel/W&B — auto-resolved as failed\", \"hypothesis\": \"OpenVLA random pruning k=0.3 on Object. Most aggressive random pruning point for OpenVLA.\", \"metrics\": {\"failure_reason\": \"AutoDL container restart at 14:50:19 UTC killed process. Was at Task 4/10 (~40%). GPU count dropped from 4 to 1 after restart.\"}, \"reproduce\": {\"finished_at\": \"2026-05-21T07:02:13.597Z\"}, \"spec\": {\"command\": \"eval_openvla_l2norm_libero.py --mode random --k_ratio 0.3 --suite libero_object --seed 42\", \"data_count\": 500, \"data_path\": \"libero_object\", \"gpu_ids\": [\"cuda:1\"], \"model_name\": \"OpenVLA + random k=0.3\", \"pid\": 568905, \"seed\": 42, \"server\": \"westd-38929\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-21T07:17:46.000Z\"}, \"eval_xvla_random_k03_object_seed42\": {\"conclusion\": \"success\", \"created_at\": \"2026-05-21T06:57:43.000Z\", \"hypothesis\": \"X-VLA random k=0.3 seed42: extreme random pruning (70% tokens removed). Extends random pruning curve below k=0.5. Expected low SR given k=0.5=70.6%.\", \"metrics\": {\"keep_ratio\": 0.3, \"success_rate\": 62.8}, \"parent\": \"eval_xvla_random_k05_object_seed42\", \"retry_count\": 0, \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=? python eval_xvla_pruning_libero.py --keep_ratio 0.30 --suite libero_object --seed 42 --n_episodes 50 --gpu 0 --mode random\", \"data_count\": 500, \"data_path\": \"libero_object\", \"model_name\": \"X-VLA\", \"seed\": 42, \"server\": \"cqa1-33015\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-21T06:57:43.000Z\"}, \"eval_xvla_random_k07_object_seed42\": {\"completed_at\": \"2026-05-21T05:45:07.000Z\", \"conclusion\": \"success\", \"created_at\": \"2026-05-21T05:24:53.000Z\", \"hypothesis\": \"X-VLA random pruning k=0.7 on Object suite. Compare with L2norm k=0.7 to extend random vs L2norm equivalence analysis at more aggressive compression.\", \"metrics\": {\"duration_min\": 77.3, \"num_episodes\": 500, \"per_task\": [0.98, 0.0, 1.0, 0.94, 0.62, 0.96, 0.1, 0.92, 0.0, 1.0], \"success_rate\": 65.2, \"wilson_ci_95\": [0.609, 0.692]}, \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=1 python eval_xvla_pruning_libero.py --keep_ratio 0.7 --mode random --suite libero_object --seed 42 --gpu 0\", \"data_count\": 500, \"data_path\": \"libero_object\", \"gpu_ids\": [\"cuda:1\"], \"log_path\": \"/root/runs/importance_margin_vla_compress/eval_xvla_random_k07_object_seed42.log\", \"model_name\": \"X-VLA + random pruning k=0.7\", \"pid\": 906389, \"seed\": 42, \"server\": \"cqa1-33015\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-21T05:45:07.000Z\"}, \"eval_openvla_sc_m128_object_seed42\": {\"completed_at\": \"2026-05-21T05:44:30.000Z\", \"conclusion\": \"failed\", \"created_at\": \"2026-05-21T03:03:54.000Z\", \"failure_reason\": \"LoRA adapter checkpoint loaded without merge: 291 missing keys + 419 unexpected keys. Model weights effectively random. 0/16 episodes = 0% SR. Need to fix eval script to merge LoRA weights before inference.\", \"hypothesis\": \"OpenVLA VTC M=128 (256→128 tokens, 50% compression) eval on LIBERO-Object. M-sweep data point: if M=128 SR is close to baseline (74%), confirms minimal degradation at 50% compression for MLP-projector VTC.\", \"metrics\": {\"all_fail\": true, \"num_episodes_completed\": 16, \"success_rate\": 0.0}, \"parent\": \"train_openvla_sc_m128_seed42\", \"retry_count\": 0, \"spec\": {\"checkpoint_path\": \"N/A (eval only)\", \"checkpoint_source\": \"checkpoints/openvla_sc_m128_seed42/checkpoint.pt (full training, 20GB)\", \"command\": \"CUDA_VISIBLE_DEVICES=0 python -u eval_openvla_smart_compress.py --n_queries 128 --checkpoint_path checkpoints/openvla_sc_m128_seed42/checkpoint.pt --suite libero_object --num_episodes 50 --gpu 0 --seed 42\", \"data_count\": 500, \"data_path\": \"libero_object\", \"eval_data\": \"LIBERO-Object (10 tasks x 50 episodes)\", \"gpu_ids\": [\"cuda:0\"], \"log_path\": \"/root/autodl-tmp/importance_margin_vla_compress/logs/eval_openvla_sc_m128_object_seed42.log\", \"model_name\": \"OpenVLA + VisionTokenCompressor(M=128)\", \"note\": \"train_openvla_sc_m128_seed42 marked failed/killed but checkpoint is loadable (20GB, 6 keys). compressor params=403M.\", \"pid\": 176320, \"seed\": 42, \"server\": \"westd-27271\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-21T05:44:30.000Z\"}, \"eval_openvla_prune_random_k05_seed42\": {\"completed_at\": \"2026-05-21T05:43:50.000Z\", \"conclusion\": \"success\", \"created_at\": \"2026-05-20T19:33:00.857Z\", \"hypothesis\": \"OpenVLA random k=0.5 seed42 第3个seed验证MF-3。已有seed7=37.4%, seed43=35.6%，预期seed42在此范围内\", \"metrics\": {\"duration_min\": 291, \"num_episodes\": 500, \"per_task\": [0.56, 0.02, 0.4, 0.58, 0.6, 0.26, 0.0, 0.12, 0.3, 0.74], \"seed\": 42, \"success_rate\": 35.8, \"wilson_ci_95\": [0.317, 0.401]}, \"notes\": \"Confirmed running on westd-41074:cuda:0, PID 659206\", \"retry_count\": 0, \"spec\": {\"command\": \"cd /root/autodl-tmp/importance_margin_vla_compress && CUDA_VISIBLE_DEVICES=0 MUJOCO_GL=egl python -u eval_openvla_libero.py --mode random_prune --k_ratio 0.5 --suite libero_object --num_episodes 50 --seed 42 --output eval_results/openvla_random_k05_seed42.json\", \"data_count\": 50, \"data_path\": \"libero_object\", \"gpu\": \"cuda:0\", \"model_name\": \"OpenVLA-OFT\", \"pid\": 659206, \"seed\": 42, \"server\": \"westd-41074\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-21T05:43:50.000Z\"}, \"eval_openvla_prune_random_k07_seed42_v2\": {\"completed_at\": \"2026-05-21T04:41:20.000Z\", \"conclusion\": \"success\", \"hypothesis\": \"OpenVLA random pruning k=0.7 Object seed42 v2 (M043 restart).\", \"metrics\": {\"num_episodes\": 500, \"seed\": 42, \"success_rate\": 44.4}, \"notes\": \"[D125] env.seed(0) bug — results use seed 0 regardless of --seed. Still valid for single-seed comparison.\", \"spec\": {\"gpu\": \"cuda:1\", \"model_name\": \"openvla-7b-finetuned-libero-object\", \"seed\": 42, \"server\": \"westd-38929\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-21T04:41:20.000Z\"}, \"eval_openvla_prune_random_k095_seed42_v2\": {\"completed_at\": \"2026-05-21T04:01:10.000Z\", \"conclusion\": \"success\", \"hypothesis\": \"OpenVLA random pruning k=0.95 Object seed42 v2 (M043 restart).\", \"metrics\": {\"num_episodes\": 500, \"per_task\": [0.8, 0.42, 0.7, 0.42, 0.88, 0.84, 0.6, 0.68, 0.66, 0.92], \"seed\": 42, \"success_rate\": 69.2, \"wilson_ci_95\": [0.65, 0.731]}, \"notes\": \"[D125] env.seed(0) bug — results use seed 0 regardless of --seed. Still valid for single-seed comparison.\", \"spec\": {\"gpu\": \"cuda:0\", \"model_name\": \"openvla-7b-finetuned-libero-object\", \"seed\": 42, \"server\": \"westd-38929\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-21T04:01:10.000Z\"}, \"eval_smolvla_baseline_spatial_westd38929_seed42\": {\"completed_at\": \"2026-05-21T02:55:52.000Z\", \"conclusion\": \"success\", \"hypothesis\": \"SmolVLA unpruned baseline on LIBERO-Spatial (westd-38929, OffScreenRenderEnv).\", \"metrics\": {\"note\": \"OffScreenRenderEnv - not comparable with LiberoEnv results\", \"num_episodes\": 500, \"per_task\": [0.24, 0.08, 0.04, 0.24, 0.0, 0.02, 0.02, 0.02, 0.14, 0.0], \"success_rate\": 8.0, \"wilson_ci_95\": [0.059, 0.107]}, \"notes\": \"[D125] OffScreenRenderEnv — NOT comparable with cqa1 results (LiberoEnv baseline=43.8%). For reference only.\", \"spec\": {\"gpu\": \"cuda:2\", \"model_name\": \"SmolVLA-official\", \"server\": \"westd-38929\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-21T03:41:17.000Z\"}, \"eval_xvla_random_k08_object_seed42\": {\"completed_at\": \"2026-05-21T03:35:27.000Z\", \"conclusion\": \"success\", \"created_at\": \"2026-05-21T02:31:58.311851+00:00\", \"hypothesis\": \"X-VLA random pruning k=0.8 on Object suite (seed42). Compare with L2 norm pruning at same k to quantify importance-aware vs random token selection.\", \"metrics\": {\"num_episodes\": 500, \"per_task\": [0.96, 0.88, 1.0, 0.92, 0.94, 0.96, 0.5, 0.94, 0.84, 1.0], \"success_rate\": 89.4, \"wilson_ci_95\": [0.864, 0.918]}, \"notes\": \"[D124] X-VLA random pruning experiment (M046 fix: script now supports --mode random).\", \"parent\": \"eval_xvla_prune_k08_seed42\", \"spec\": {\"command\": \"python eval_xvla_pruning_libero.py --model_path /root/autodl-tmp/X-VLA-Libero --suite libero_object --keep_ratio 0.8 --mode random --num_episodes 50 --seed 42 --domain_id 3 --gpu 0\", \"data_count\": 500, \"data_path\": \"libero_object\", \"gpu\": \"cuda:1\", \"model_name\": \"X-VLA-Libero\", \"seed\": 42, \"server\": \"cqa1-33015\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-21T03:35:27.000Z\"}, \"eval_xvla_random_k09_object_seed42\": {\"completed_at\": \"2026-05-21T03:25:33.000Z\", \"conclusion\": \"success\", \"created_at\": \"2026-05-21T02:31:58.311851+00:00\", \"hypothesis\": \"X-VLA random pruning k=0.9 on Object suite (seed42). Compare with L2 norm pruning at same k to quantify importance-aware vs random token selection.\", \"metrics\": {\"duration_min\": 50.4, \"num_episodes\": 500, \"per_task\": [0.96, 1.0, 1.0, 0.94, 1.0, 0.94, 1.0, 0.98, 0.96, 1.0], \"success_rate\": 97.8, \"wilson_ci_95\": [0.961, 0.988]}, \"notes\": \"[D124] X-VLA random pruning experiment (M046 fix: script now supports --mode random).\", \"parent\": \"eval_xvla_prune_k09_seed42\", \"spec\": {\"command\": \"python eval_xvla_pruning_libero.py --model_path /root/autodl-tmp/X-VLA-Libero --suite libero_object --keep_ratio 0.9 --mode random --num_episodes 50 --seed 42 --domain_id 3 --gpu 0\", \"data_count\": 500, \"data_path\": \"libero_object\", \"gpu\": \"cuda:0\", \"model_name\": \"X-VLA-Libero\", \"seed\": 42, \"server\": \"cqa1-33015\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-21T03:25:33.000Z\"}, \"eval_xvla_spatial_k085_seed42\": {\"completed_at\": \"2026-05-21T03:08:20.000Z\", \"conclusion\": \"success\", \"created_at\": \"2026-05-21T01:18:20.885504Z\", \"hypothesis\": \"X-VLA shows non-monotonic cliff at k=0.85 on Object (67.9% vs k=0.8=89.0%). If same cliff appears on Spatial (baseline=91.6%, k=0.9=79.0%), it confirms the cliff is a general property of X-VLA linear connector, not suite-specific.\", \"metrics\": {\"num_episodes\": 500, \"success_rate\": 66.6}, \"notes\": \"[M046] Pruning method: L2 norm topk (same as all X-VLA pruning experiments).\", \"parent\": \"eval_xvla_prune_k085_seed42\", \"spec\": {\"account\": \"root\", \"backend\": \"tmux\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/importance_margin_vla_compress && python eval_xvla_pruning_libero.py --model_path /root/autodl-tmp/X-VLA-Libero --suite libero_spatial --keep_ratio 0.85 --num_episodes 50 --seed 42 --domain_id 3 --gpu 0\\\"\", \"gpu\": [\"cuda:2\"], \"log_path\": \"~/runs/importance_margin_vla_compress/eval_xvla_spatial_k085_seed42.log\", \"pid\": 279327, \"server\": \"cqa1-33015\", \"submitted_at\": \"2026-05-21T01:18:30.383Z\", \"submitted_via\": \"submit_training_job\"}, \"started_at\": \"2026-05-21T01:19:17.534020+00:00\", \"status\": \"DONE\", \"updated_at\": \"2026-05-21T03:08:20.000Z\"}, \"eval_openvla_prune_l2norm_k07_seed43_v2\": {\"completed_at\": \"2026-05-21T02:55:52.000Z\", \"conclusion\": \"success\", \"created_at\": \"2026-05-20T22:21:37.716Z\", \"hypothesis\": \"重跑 L2 norm k=0.7 seed43（修正参数 bug）。预期 SR ≈ 49.8%（与 seed42 random k=0.7 对齐，D108 结论 L2≈random at k≤0.7）\", \"metrics\": {\"num_episodes\": 500, \"success_rate\": 49.8, \"wilson_ci_95\": [0.455, 0.541]}, \"parent\": \"eval_openvla_prune_l2norm_k07_seed43\", \"retry_count\": 0, \"spec\": {\"checkpoint_source\": \"/root/autodl-tmp/openvla-libero-object\", \"command\": \"cd /root/autodl-tmp/importance_margin_vla_compress && CUDA_VISIBLE_DEVICES=0 MUJOCO_GL=egl python -u eval_openvla_l2norm_libero.py --mode l2norm_prune --k_ratio 0.7 --suite libero_object --num_episodes 50 --seed 43 --output eval_results/openvla_l2norm_k07_seed43_v2.json\", \"data_count\": 500, \"data_path\": \"libero_object\", \"eval_data\": \"libero_object (10 tasks x 50 episodes)\", \"gpu\": \"cuda:0\", \"log_path\": \"/tmp/eval_l2norm_k07_s43_v2.log\", \"model_name\": \"openvla-7b-libero-object\", \"output_file\": \"eval_results/openvla_l2norm_k07_seed43_v2.json\", \"seed\": 43, \"server\": \"westd-27271\", \"tmux_session\": \"eval_l2norm_k07_s43_v2\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-21T02:55:52.000Z\"}, \"eval_oft_baseline_object_seed42\": {\"conclusion\": \"killed\", \"created_at\": \"2026-05-21T02:23:43.052531+00:00\", \"hypothesis\": \"OFT Object baseline (no pruning, k=1.0). OFT uses 3-layer MLP connector (same family as OpenVLA) with 512 vision tokens (DINOv2+SigLIP). Expected SR ≈ 97% (SOTA). Validates eval adapter correctness.\", \"notes\": \"Killed on westd-41074:cuda:1 per Director instruction (D124). OFT baseline reassigned to westd-38929:cuda:0.\", \"retry_count\": 0, \"spec\": {\"account\": \"root\", \"backend\": \"tmux\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/importance_margin_vla_compress && CUDA_VISIBLE_DEVICES=2 python -u eval_oft_libero.py --checkpoint /root/autodl-tmp/openvla-oft-libero-object/ --suite libero_object --prune_mode none --keep_ratio 1.0 --seed 42\\\"\", \"gpu\": [\"cuda:2\"], \"log_path\": \"~/runs/importance_margin_vla_compress/eval_oft_baseline_object_seed42.log\", \"pid\": \"398822\", \"server\": \"westd-38929\", \"submitted_at\": \"2026-05-21T02:51:12.406Z\", \"submitted_via\": \"submit_training_job\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-21T02:51:13.099Z\"}, \"train_openvla_sc_m64_seed42_v3\": {\"completed_at\": \"2026-05-21T02:41:41.925Z\", \"conclusion\": \"failed\", \"created_at\": \"2026-05-20T06:16:27.251Z\", \"failure_reason\": \"磁盘写满导致 checkpoint 保存失败 — step 50000/100000 eval 后 torch.save 报 RuntimeError: PytorchStreamWriter failed writing file data/981 (磁盘 250G 100% 占满). checkpoint_step50000.pt (14G) 存在但损坏. 训练本身正常 (loss ~2.5-2.9, eval_loss=2.9016@50K).\", \"hypothesis\": \"OpenVLA VTC-only M=64 (256→64 tokens, 75% compression). M-sweep data point. Retracked from orphan PID 68852 after config-missing failure. Training from step 0, currently at ~2450+. If M=64 SR > M=32 SR, confirms monotonic degradation for MLP-projector VTC re-encoding at higher compression ratios on OpenVLA.\", \"parent\": \"train_openvla_sc_m128_vtconly_seed42\", \"retry_count\": 0, \"spec\": {\"checkpoint_source\": \"openvla/openvla-7b\", \"command\": \"python train_openvla_smart_compress.py --config configs/openvla_smart_compress_m64.yaml\", \"data_count\": 50000, \"data_path\": \"LIBERO\", \"eval_data\": \"N/A - training experiment\", \"gpu\": \"cuda:3\", \"model_name\": \"openvla-7b\", \"pid\": 68852, \"seed\": 42, \"server\": \"westd-41074\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-21T02:41:41.924Z\"}, \"eval_openvla_baseline_spatial_seed42_v2\": {\"conclusion\": \"failed\", \"created_at\": \"2026-05-21T00:52:09.639Z\", \"hypothesis\": \"OpenVLA baseline on LIBERO-Spatial (v2, after checkpoint integrity verification). M044 lesson: v1 used partial checkpoint leading to 0% SR.\", \"notes\": \"No process found on westd-41074:cuda:1. Experiment died without trace. [D122] 0% SR confirmed not max_steps issue. Killed to free GPU.\", \"parent\": \"eval_openvla_baseline_spatial_seed42\", \"retry_count\": 0, \"spec\": {\"checkpoint_source\": \"/root/autodl-tmp/openvla-7b-finetuned-libero-spatial\", \"command\": \"CUDA_VISIBLE_DEVICES=1 MUJOCO_GL=egl python -u eval_openvla_libero.py --model_path /root/autodl-tmp/openvla-7b-finetuned-libero-spatial --mode random_prune --k_ratio 1.0 --suite libero_spatial --num_episodes 50 --seed 42 --output eval_results/openvla_baseline_spatial_seed42.json\", \"data_count\": 500, \"data_path\": \"libero_spatial\", \"eval_data\": \"libero_spatial\", \"gpu_id\": 1, \"model_name\": \"openvla-7b-finetuned-libero-spatial\", \"seed\": 42, \"server\": \"westd-41074\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-21T00:52:30.601Z\"}, \"eval_xvla_goal_k05_seed42\": {\"completed_at\": \"2026-05-21T02:34:03.005612+00:00\", \"conclusion\": \"success\", \"created_at\": \"2026-05-21T00:49:10.505Z\", \"hypothesis\": \"X-VLA k=0.5 on LIBERO-Goal. Object k=0.5=43.7%, Spatial k=0.5 running. Cross-suite comparison at aggressive pruning level (C1)\", \"metrics\": {\"num_episodes\": 500, \"per_task\": [0.82, 0.98, 1.0, 0.4, 1.0, 0.0, 0.24, 0.74, 0.92, 0.0], \"seed\": 42, \"success_rate\": 0.61, \"suite\": \"libero_goal\", \"wilson_ci_95\": [0.567, 0.652]}, \"notes\": \"[M046] L2 norm pruning (not random). Result from Director.\", \"retry_count\": 0, \"spec\": {\"checkpoint_source\": \"/root/autodl-tmp/X-VLA-Libero\", \"command\": \"CUDA_VISIBLE_DEVICES=3 MUJOCO_GL=egl python -u eval_xvla_pruning_libero.py --model_path /root/autodl-tmp/X-VLA-Libero --suite libero_goal --keep_ratio 0.5 --num_episodes 50 --seed 42 --domain_id 3 --gpu 0 --output eval_results/xvla_goal_k05_seed42.json\", \"data_count\": 500, \"data_path\": \"libero_goal\", \"eval_data\": \"libero_goal (10 tasks x 50 episodes)\", \"gpu\": \"cuda:3\", \"log_path\": \"/root/autodl-tmp/importance_margin_vla_compress/logs/eval_xvla_goal_k05_seed42.log\", \"model_name\": \"X-VLA-Libero\", \"seed\": 42, \"server\": \"cqa1-33015\", \"tmux_session\": \"eval_xvla_goal_k05\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-21T00:50:28.802Z\"}, \"eval_xvla_goal_k09_seed42\": {\"completed_at\": \"2026-05-21T02:35:47.190358+00:00\", \"conclusion\": \"success\", \"created_at\": \"2026-05-21T00:49:06.867Z\", \"hypothesis\": \"X-VLA k=0.9 on LIBERO-Goal. Object k=0.9=97.8%, Spatial k=0.9=79.0%. If Goal also high, confirms cross-suite pruning tolerance. If lower, reveals suite-dependent sensitivity (C1)\", \"metrics\": {\"num_episodes\": 500, \"per_task\": [1.0, 0.82, 0.96, 0.06, 0.96, 0.0, 0.78, 1.0, 0.46, 0.98], \"seed\": 42, \"success_rate\": 0.702, \"suite\": \"libero_goal\", \"wilson_ci_95\": [0.66, 0.74]}, \"notes\": \"[M046] L2 norm pruning. Goal suite much more sensitive than Object (-27.8pp vs -1.4pp at k=0.9).\", \"retry_count\": 0, \"spec\": {\"checkpoint_source\": \"/root/autodl-tmp/X-VLA-Libero\", \"command\": \"CUDA_VISIBLE_DEVICES=0 MUJOCO_GL=egl python -u eval_xvla_pruning_libero.py --model_path /root/autodl-tmp/X-VLA-Libero --suite libero_goal --keep_ratio 0.9 --num_episodes 50 --seed 42 --domain_id 3 --gpu 0 --output eval_results/xvla_goal_k09_seed42.json\", \"data_count\": 500, \"data_path\": \"libero_goal\", \"eval_data\": \"libero_goal (10 tasks x 50 episodes)\", \"gpu\": \"cuda:0\", \"log_path\": \"/root/autodl-tmp/importance_margin_vla_compress/logs/eval_xvla_goal_k09_seed42.log\", \"model_name\": \"X-VLA-Libero\", \"seed\": 42, \"server\": \"cqa1-33015\", \"tmux_session\": \"eval_xvla_goal_k09\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-21T00:50:23.115Z\"}, \"eval_xvla_spatial_k09_seed42\": {\"completed_at\": \"2026-05-21T00:48:54.159Z\", \"conclusion\": \"success\", \"created_at\": \"2026-05-20T23:19:31.674Z\", \"hypothesis\": \"X-VLA k=0.9 pruning on LIBERO-Spatial. Object suite k=0.9=97.8%, Spatial baseline=98%+. If Spatial also robust at k=0.9, confirms cross-suite pruning tolerance at high keep ratios\", \"metrics\": {\"num_episodes\": 500, \"success_rate\": 0.79, \"wilson_ci_95\": [0.752, 0.823]}, \"notes\": \"[M046] Pruning method: L2 norm topk (same as all X-VLA pruning experiments).\", \"retry_count\": 0, \"spec\": {\"checkpoint_path\": \"/root/autodl-tmp/X-VLA-Libero\", \"command\": \"CUDA_VISIBLE_DEVICES=1 MUJOCO_GL=egl python -u eval_xvla_pruning_libero.py --model_path /root/autodl-tmp/X-VLA-Libero --suite libero_spatial --keep_ratio 0.9 --num_episodes 50 --seed 42 --domain_id 3 --gpu 0 --output eval_results/xvla_spatial_k09_seed42.json\", \"data_count\": 50, \"data_path\": \"libero_spatial\", \"log_path\": \"/root/autodl-tmp/importance_margin_vla_compress/eval_results/xvla_spatial_k09_seed42.json\", \"model_name\": \"X-VLA-Libero\", \"seed\": 42, \"server\": \"cqa1-33015\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-21T00:48:54.159Z\"}, \"eval_openvla_sc_m128_spatial_seed42\": {\"conclusion\": \"failed\", \"created_at\": \"2026-05-20T23:47:52.524Z\", \"hypothesis\": \"OpenVLA SmartCompress M=128 on LIBERO-Spatial. Object suite SR=59.8% (vs random k=0.5 ~36%). If Spatial maintains similar relative advantage over random pruning, confirms learned VTC re-encoding generalizes across suites (C3 graceful degradation)\", \"notes\": \"No process found on westd-41074:cuda:1. Experiment died without trace.\", \"retry_count\": 0, \"spec\": {\"checkpoint_source\": \"checkpoints/openvla_sc_m128/checkpoint.pt\", \"command\": \"CUDA_VISIBLE_DEVICES=1 MUJOCO_GL=egl python -u eval_openvla_smart_compress.py --n_queries 128 --checkpoint_path checkpoints/openvla_sc_m128/checkpoint.pt --suite libero_spatial --num_episodes 50 --seed 42 --gpu 0 --output eval_results/openvla_sc_m128_spatial_seed42.json\", \"data_count\": 500, \"data_path\": \"LIBERO-Spatial (10 tasks x 50 episodes)\", \"eval_data\": \"libero_spatial\", \"model_name\": \"OpenVLA SmartCompress M=128\", \"seed\": 42, \"server\": \"westd-41074\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-20T23:48:20.930Z\"}, \"eval_openvla_prune_random_k03_seed43\": {\"completed_at\": \"2026-05-20T23:24:24.497Z\", \"conclusion\": \"killed\", \"created_at\": \"2026-05-20T19:30:53.798Z\", \"failure_reason\": \"M043: LIBERO-Plus pip install overwrote running LIBERO package\", \"hypothesis\": \"OpenVLA random pruning k=0.3 seed43 provides 2nd seed for MF-3 validation at 70% pruning. seed7=20.6%. Tests whether severe degradation pattern is consistent across seeds.\", \"log_path\": \"/root/autodl-tmp/importance_margin_vla_compress/logs/eval_random_k03_seed43.log\", \"notes\": \"Process died silently during Task 3 (salad dressing, Ep 30/50) — no traceback in log, log stopped updating at 07:18 CST. GPU 2 shows 15.6GB memory but 0% utilization (zombie memory). Same LIBERO init_files issue as other 3 experiments. Partial results: T1=18%, T2=2%, T3=partial(16/30). Metadata verified: Random pruning k=0.3, 256→76 tokens.\", \"parent\": \"eval_openvla_prune_seed43_sweep\", \"retry_count\": 0, \"spec\": {\"checkpoint_source\": \"/root/autodl-tmp/openvla-libero-object\", \"command\": \"CUDA_VISIBLE_DEVICES=2 MUJOCO_GL=egl python -u eval_openvla_libero.py --mode random_prune --k_ratio 0.3 --suite libero_object --seed 43 --output eval_results/openvla_random_k03_seed43.json\", \"data_count\": 500, \"data_path\": \"/root/autodl-tmp/openvla-libero-object\", \"eval_data\": \"libero_object (10 tasks x 50 eps)\", \"gpu\": \"cuda:2\", \"model_name\": \"openvla-7b-libero-object\", \"seed\": 43, \"server\": \"westd-38929\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-20T23:24:24.497Z\"}, \"eval_openvla_prune_random_k07_seed42\": {\"completed_at\": \"2026-05-20T23:24:23.000Z\", \"conclusion\": \"killed\", \"created_at\": \"2026-05-20T19:28:27.340Z\", \"failure_reason\": \"M043: LIBERO-Plus pip install overwrote running LIBERO package\", \"hypothesis\": \"OpenVLA random pruning k=0.7 seed42 provides 3rd seed for MF-3 validation. seed7=49%, seed43=52.6%. If seed42 ≈ 50%, confirms graded degradation at 30% pruning is robust across seeds.\", \"log_path\": \"/root/autodl-tmp/importance_margin_vla_compress/logs/eval_random_k07_seed42.log\", \"notes\": \"CRASHED mid-Task 3 (salad dressing, Ep 40/50) — FileNotFoundError for .pruned_init file. Same LIBERO init_files path issue as all 4 westd-38929 experiments. Partial results: T1=72%, T2=20%, T3=partial(21/40). Metadata verified: Random pruning k=0.7, 256→179 tokens. Needs LIBERO reinstall before rerun.\", \"parent\": \"eval_openvla_random_pruning_sweep\", \"retry_count\": 0, \"spec\": {\"checkpoint_source\": \"/root/autodl-tmp/openvla-libero-object\", \"command\": \"CUDA_VISIBLE_DEVICES=1 MUJOCO_GL=egl python -u eval_openvla_libero.py --mode random_prune --k_ratio 0.7 --suite libero_object --seed 42 --output eval_results/openvla_random_k07_seed42.json\", \"data_count\": 500, \"data_path\": \"/root/autodl-tmp/openvla-libero-object\", \"eval_data\": \"libero_object (10 tasks x 50 eps)\", \"gpu\": \"cuda:1\", \"model_name\": \"openvla-7b-libero-object\", \"seed\": 42, \"server\": \"westd-38929\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-20T23:24:23.000Z\"}, \"eval_openvla_prune_random_k095_seed42\": {\"completed_at\": \"2026-05-20T23:24:21.317Z\", \"conclusion\": \"killed\", \"created_at\": \"2026-05-20T19:28:25.854Z\", \"failure_reason\": \"M043: LIBERO-Plus pip install overwrote running LIBERO package\", \"hypothesis\": \"OpenVLA random pruning k=0.95 seed42 provides 3rd seed for MF-3 validation. seed7=69.4%. If seed42 ≈ 69%, confirms minimal pruning (5%) causes only marginal degradation in MLP-connector architecture, robust across seeds.\", \"log_path\": \"/root/autodl-tmp/importance_margin_vla_compress/logs/eval_random_k095_seed42.log\", \"notes\": \"CRASHED at Task 4/10 (bbq sauce) — FileNotFoundError for .pruned_init file. LIBERO init_files at /root/miniconda3/.../site-packages/libero/ wiped after M040 restart. Partial results (3/10 tasks): T1=80%, T2=42%, T3=70%. Metadata verified: Random pruning k=0.95, 256→243 tokens. Needs LIBERO reinstall or symlink to /root/autodl-tmp/LIBERO-plus/ before rerun.\", \"parent\": \"eval_openvla_random_pruning_sweep\", \"retry_count\": 0, \"spec\": {\"checkpoint_source\": \"/root/autodl-tmp/openvla-libero-object\", \"command\": \"CUDA_VISIBLE_DEVICES=0 MUJOCO_GL=egl python -u eval_openvla_libero.py --mode random_prune --k_ratio 0.95 --suite libero_object --seed 42 --output eval_results/openvla_random_k095_seed42.json\", \"data_count\": 500, \"data_path\": \"/root/autodl-tmp/openvla-libero-object\", \"eval_data\": \"libero_object (10 tasks x 50 eps)\", \"gpu\": \"cuda:0\", \"model_name\": \"openvla-7b-libero-object\", \"seed\": 42, \"server\": \"westd-38929\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-20T23:24:21.317Z\"}, \"eval_openvla_prune_l2norm_k09_seed43\": {\"completed_at\": \"2026-05-20T23:21:58.931Z\", \"conclusion\": \"killed\", \"created_at\": \"2026-05-20T19:30:56.421Z\", \"failure_reason\": \"M043: LIBERO-Plus pip install overwrote running LIBERO package\", \"hypothesis\": \"OpenVLA L2 norm pruning k=0.9 seed43 provides 2nd seed for D108 L2 norm multi-seed validation. seed7 L2 norm k=0.9=70.6% vs random=62%. If seed43 confirms +8pp advantage, strengthens L2 norm's selective benefit at high retention.\", \"log_path\": \"/root/autodl-tmp/importance_margin_vla_compress/logs/eval_l2norm_k09_seed43.log\", \"notes\": \"CRASHED at Task 4/10 (bbq sauce) — FileNotFoundError for .pruned_init file. Root cause: LIBERO init_files path mismatch. Code resolves to /root/miniconda3/.../site-packages/libero/libero/init_files/ (non-existent) but actual files are at /root/autodl-tmp/LIBERO-plus/libero/libero/init_files/. Same bug hits eval_random_k095_seed42 and eval_random_k07_seed42. Only 3/10 tasks completed (T1=66%, T2=58%, T3=66%). Needs LIBERO reinstall or symlink fix before rerun.\", \"parent\": \"eval_openvla_prune_l2norm_sweep\", \"retry_count\": 0, \"spec\": {\"checkpoint_source\": \"/root/autodl-tmp/openvla-libero-object\", \"command\": \"CUDA_VISIBLE_DEVICES=3 MUJOCO_GL=egl python -u eval_openvla_l2norm_libero.py --mode l2norm_prune --k_ratio 0.9 --suite libero_object --seed 43 --output eval_results/openvla_l2norm_k09_seed43.json\", \"data_count\": 500, \"data_path\": \"/root/autodl-tmp/openvla-libero-object\", \"eval_data\": \"libero_object (10 tasks x 50 eps)\", \"gpu\": \"cuda:3\", \"model_name\": \"openvla-7b-libero-object\", \"seed\": 43, \"server\": \"westd-38929\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-20T23:21:58.931Z\"}, \"eval_xvla_spatial_k05_seed42\": {\"checkpoint_path\": \"/root/autodl-tmp/importance_margin_vla_compress/eval_results/xvla_spatial_k05_seed42.json\", \"conclusion\": \"success\", \"created_at\": \"2026-05-20T23:19:33.364Z\", \"hypothesis\": \"X-VLA k=0.5 pruning on LIBERO-Spatial. Object suite k=0.5=43.7%. If Spatial shows similar degradation pattern, confirms cross-suite consistency. If different, reveals suite-dependent pruning sensitivity\", \"log_path\": \"/root/autodl-tmp/importance_margin_vla_compress/logs/eval_xvla_spatial_k05_seed42.log\", \"metrics\": {\"num_episodes\": 500, \"per_task\": [0.94, 0.22, 0.9, 0.74, 0.88, 0.0, 0.78, 0.3, 0.74, 0.38], \"success_rate\": 0.588, \"wilson_ci_95\": [0.544, 0.63]}, \"notes\": \"[M046] Pruning method: L2 norm topk (same as all X-VLA pruning experiments).\", \"retry_count\": 0, \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=2 MUJOCO_GL=egl python -u eval_xvla_pruning_libero.py --model_path /root/autodl-tmp/X-VLA-Libero --suite libero_spatial --keep_ratio 0.5 --num_episodes 50 --seed 42 --domain_id 3 --gpu 0 --output eval_results/xvla_spatial_k05_seed42.json\", \"data_count\": 50, \"data_path\": \"libero_spatial\", \"model_name\": \"X-VLA-Libero\", \"seed\": 42, \"server\": \"cqa1-33015\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-20T23:21:26.353Z\"}, \"eval_xvla_prune_k085_seed44\": {\"completed_at\": \"2026-05-20T23:15:00.000Z\", \"conclusion\": \"success\", \"created_at\": \"2026-05-20T21:56:57.648Z\", \"hypothesis\": \"X-VLA L2 norm pruning k=0.85 seed44 provides 3rd seed for cliff region. seed42=68.0% shows massive task-specific variance (T6=0%, T4=26%). 3rd seed validates variance pattern.\", \"metrics\": {\"num_episodes\": 500, \"success_rate\": 0.682, \"wilson_ci_95\": [0.64, 0.721]}, \"notes\": \"[M046] Pruning method corrected: was labeled random but actually uses L2 norm topk selection.\", \"retry_count\": 0, \"spec\": {\"checkpoint_path\": \"/root/autodl-tmp/X-VLA-Libero\", \"command\": \"python -u eval_xvla_pruning_libero.py --model_path /root/autodl-tmp/X-VLA-Libero --suite libero_object --keep_ratio 0.85 --num_episodes 50 --seed 44 --domain_id 3 --gpu 0 --output eval_results/xvla_prune_k085_libero_object_seed44.json\", \"data_count\": 50, \"data_path\": \"libero_object\", \"gpu\": \"cuda:2\", \"log_path\": \"/root/autodl-tmp/importance_margin_vla_compress/eval_results/xvla_prune_k085_libero_object_seed44.json\", \"metrics\": {\"num_episodes\": 500, \"success_rate\": 0.682, \"total_successes\": 341, \"wilson_ci_95\": [0.64, 0.721]}, \"model_name\": \"X-VLA-Libero\", \"seed\": 44, \"server\": \"cqa1-33015\", \"tmux_session\": \"eval_xvla_k085_s44\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-20T23:16:00.643Z\"}, \"eval_xvla_prune_k08_seed44\": {\"checkpoint_path\": \"/root/autodl-tmp/X-VLA-Libero\", \"completed_at\": \"2026-05-20T22:51:44.737Z\", \"conclusion\": \"success\", \"created_at\": \"2026-05-20T21:47:40.340Z\", \"hypothesis\": \"X-VLA L2 norm pruning k=0.8 seed44 provides 3rd seed for cliff threshold localization at MF-3 statistical validation. seed43=88.4%. Expecting similar range to confirm cliff position.\", \"log_path\": \"/root/autodl-tmp/importance_margin_vla_compress/logs/eval_xvla_k08_seed44.log\", \"metrics\": {\"num_episodes\": 500, \"success_rate\": 0.898, \"total_successes\": 449, \"wilson_ci_95\": [0.868, 0.922]}, \"notes\": \"k=0.8 seed44 SR=89.8% [86.8%, 92.2%]. JSON file missing (log data intact). 3-seed mean for k=0.8: (88.8+88.4+89.8)/3=89.0%. Confirms k=0.8 is above the cliff — performance nearly matches baseline. Cliff localized to 0.80→0.85 (keep_ratio) region where SR drops from ~89% to ~68%. [M046] Pruning method corrected: was labeled random but actually uses L2 norm topk selection.\", \"retry_count\": 0, \"spec\": {\"command\": \"python -u eval_xvla_pruning_libero.py --model_path /root/autodl-tmp/X-VLA-Libero --suite libero_object --keep_ratio 0.8 --num_episodes 50 --seed 44 --domain_id 3 --gpu 0 --output eval_results/xvla_prune_k08_libero_object_seed44.json\", \"data_count\": 50, \"data_path\": \"libero_object\", \"gpu\": \"cuda:1\", \"model_name\": \"X-VLA-Libero\", \"pid\": 563249, \"seed\": 44, \"server\": \"cqa1-33015\", \"tmux_session\": \"eval_xvla_k08_s44\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-20T22:51:44.737Z\"}, \"eval_openvla_prune_random_k095_seed43\": {\"checkpoint_path\": \"eval_results/openvla_random_prune_k095_seed43.json\", \"completed_at\": \"2026-05-20T22:33:00.000Z\", \"conclusion\": \"success\", \"created_at\": \"2026-05-20T19:11:40.332Z\", \"hypothesis\": \"OpenVLA random pruning at k=0.95 with seed=43 verifies reproducibility of seed=7 result (69.4% SR). If consistent, confirms that minimal pruning (5%) causes marginal degradation in MLP-connector architecture.\", \"log_path\": \"eval_results/openvla_random_prune_k095_seed43.json\", \"metrics\": {\"elapsed_minutes\": 249.43, \"k_ratio\": 0.95, \"mode\": \"random_prune\", \"num_episodes\": 500, \"seed\": 43, \"success_rate\": 0.668, \"total_successes\": 334, \"wilson_ci_95\": [0.626, 0.708]}, \"parent\": \"eval_openvla_prune_seed43_sweep\", \"retry_count\": 0, \"spec\": {\"checkpoint_source\": \"/root/autodl-tmp/openvla-libero-object\", \"command\": \"CUDA_VISIBLE_DEVICES=0 MUJOCO_GL=egl python eval_openvla_libero.py --mode random_prune --k_ratio 0.95 --suite libero_object --seed 43 --output eval_results/openvla_random_k095_seed43.json\", \"data_count\": 500, \"data_path\": \"/root/autodl-tmp/openvla-libero-object\", \"eval_data\": \"libero_object (10 tasks x 50 eps)\", \"gpu\": \"cuda:0\", \"model_name\": \"openvla-7b-libero-object\", \"pid\": 564811, \"seed\": 43, \"server\": \"westd-41074\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-20T22:34:31.530Z\"}, \"eval_openvla_prune_l2norm_k07_seed43\": {\"completed_at\": \"2026-05-20T22:16:27.831Z\", \"conclusion\": \"failed\", \"created_at\": \"2026-05-20T18:15:31.381Z\", \"failure_reason\": \"pruning not applied, mode=baseline in metadata, SR=74.0% matches unpruned baseline\", \"hypothesis\": \"OpenVLA L2 norm pruning at k=0.7 with seed=43. Seed42 L2 norm k=0.7 = 49.8%. If seed43 ≈ 50%, confirms L2 norm pruning curve is reproducible across seeds for MLP projector.\", \"metrics\": {\"elapsed_minutes\": 237.8, \"num_episodes\": 500, \"per_task\": {\"alphabet_soup\": 0.78, \"bbq_sauce\": 0.46, \"butter\": 0.58, \"chocolate_pudding\": 0.68, \"cream_cheese\": 0.8, \"ketchup\": 0.96, \"milk\": 0.72, \"orange_juice\": 0.82, \"salad_dressing\": 0.82, \"tomato_sauce\": 0.78}, \"seed\": 43, \"success_rate\": 0.74, \"total_successes\": 370, \"wilson_ci_95\": [0.7, 0.777]}, \"retry_count\": 0, \"spec\": {\"checkpoint_path\": \"N/A (eval only)\", \"checkpoint_source\": \"openvla-oft checkpoint\", \"command\": \"python -u eval_openvla_l2norm_libero.py --keep_ratio 0.7 --seed 43 --suite libero_object --num_episodes 50 --output eval_results/openvla_l2norm_prune_k0_7_seed43_object.json\", \"data_count\": 500, \"data_path\": \"libero_object\", \"eval_data\": \"LIBERO-Object (10 tasks x 50 episodes)\", \"gpu\": \"cuda:0\", \"log_path\": \"/root/autodl-tmp/importance_margin_vla_compress/logs/eval_openvla_l2norm_k07_seed43.log\", \"model_name\": \"OpenVLA-OFT\", \"pid\": 67609, \"seed\": 43, \"server\": \"westd-27271\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-20T22:16:27.831Z\"}, \"eval_xvla_prune_k08_seed42\": {\"checkpoint_path\": \"eval_results/xvla_prune_k08_libero_object_seed42.json\", \"completed_at\": \"2026-05-20T22:05:49.364Z\", \"conclusion\": \"success\", \"created_at\": \"2026-05-20T20:27:56.367Z\", \"extra\": {\"hook_events\": [{\"action\": \"agent\", \"event\": \"on_failed\", \"ts\": \"2026-05-20T22:05:57.629598+00:00\"}]}, \"failure_reason\": null, \"hypothesis\": \"X-VLA L2 norm pruning k=0.8 seed42 locates the cliff threshold between k=0.9 (97.8%) and k=0.7 (57.2%). If k=0.8 ≈ 90%+, cliff is between 0.7-0.8; if k=0.8 ≈ 60%, cliff starts at 0.8.\", \"log_path\": \"eval_results/xvla_prune_k08_libero_object_seed42.json\", \"metrics\": {\"keep_ratio\": 0.8, \"n_vision_tokens_kept\": 40, \"n_vision_tokens_original\": 50, \"num_episodes\": 500, \"success_rate\": 0.888, \"wilson_ci_95\": [0.8573, 0.9127]}, \"notes\": \"[M046] Pruning method corrected: was labeled random but actually uses L2 norm topk selection.\", \"reproduce\": {\"finished_at\": \"2026-05-20T22:05:46.313Z\"}, \"retry_count\": 0, \"spec\": {\"command\": \"python -u eval_xvla_pruning_libero.py --model_path /root/autodl-tmp/X-VLA-Libero --suite libero_object --keep_ratio 0.8 --num_episodes 50 --seed 42 --domain_id 3 --gpu 0 --output eval_results/xvla_prune_k08_libero_object_seed42.json\", \"data_count\": 50, \"data_path\": \"libero_object\", \"gpu\": \"cuda:0\", \"model_name\": \"X-VLA-Libero\", \"pid\": 335130, \"seed\": 42, \"server\": \"cqa1-33015\", \"tmux_session\": \"eval_xvla_k08_s42\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-20T22:12:20.485Z\"}, \"eval_xvla_prune_k085_seed43\": {\"checkpoint_path\": \"eval_results/xvla_prune_k0.85_libero_object_seed43.json\", \"completed_at\": \"2026-05-20T22:12:00.000Z\", \"conclusion\": \"success\", \"created_at\": \"2026-05-20T20:28:01.206Z\", \"hypothesis\": \"X-VLA L2 norm pruning k=0.85 seed43 provides 2nd seed for k=0.85 data point. Combined with seed42, validates whether the cliff shape is consistent across seeds.\", \"log_path\": \"eval_results/xvla_prune_k0.85_libero_object_seed43.json\", \"metrics\": {\"keep_ratio\": 0.85, \"n_vision_tokens_kept\": 42, \"n_vision_tokens_original\": 50, \"num_episodes\": 500, \"success_rate\": 0.676, \"wilson_ci_95\": [0.6338, 0.7155]}, \"notes\": \"[M046] Pruning method corrected: was labeled random but actually uses L2 norm topk selection.\", \"retry_count\": 0, \"spec\": {\"command\": \"python -u eval_xvla_pruning_libero.py --model_path /root/autodl-tmp/X-VLA-Libero --suite libero_object --keep_ratio 0.85 --num_episodes 50 --seed 43 --domain_id 3 --gpu 0 --output eval_results/xvla_prune_k085_libero_object_seed43.json\", \"data_count\": 50, \"data_path\": \"libero_object\", \"gpu\": \"cuda:3\", \"model_name\": \"X-VLA-Libero\", \"pid\": 264237, \"seed\": 43, \"server\": \"cqa1-33015\", \"tmux_session\": \"eval_xvla_k085_s43\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-20T22:12:19.023Z\"}, \"eval_xvla_prune_k085_seed42\": {\"completed_at\": \"2026-05-20T21:57:02.351Z\", \"conclusion\": \"success\", \"created_at\": \"2026-05-20T20:28:00.150Z\", \"hypothesis\": \"X-VLA L2 norm pruning k=0.85 seed42 further narrows the cliff between k=0.9 (97.8%) and k=0.8. If k=0.85 ≈ 97%, cliff is sharp at k=0.8; if k=0.85 ≈ 80%, degradation is more gradual.\", \"metrics\": {\"num_episodes\": 500, \"success_rate\": 0.68, \"wilson_ci_95\": [0.638, 0.719]}, \"notes\": \"[M046] Pruning method corrected: was labeled random but actually uses L2 norm topk selection.\", \"retry_count\": 0, \"spec\": {\"checkpoint_path\": \"N/A\", \"command\": \"python -u eval_xvla_pruning_libero.py --model_path /root/autodl-tmp/X-VLA-Libero --suite libero_object --keep_ratio 0.85 --num_episodes 50 --seed 42 --domain_id 3 --gpu 0 --output eval_results/xvla_prune_k085_libero_object_seed42.json\", \"data_count\": 50, \"data_path\": \"libero_object\", \"gpu\": \"cuda:2\", \"log_path\": \"cqa1-33015:/root/autodl-tmp/X-VLA-Libero/eval_results/xvla_prune_k085_libero_object_seed42.json\", \"model_name\": \"X-VLA-Libero\", \"pid\": 244489, \"seed\": 42, \"server\": \"cqa1-33015\", \"tmux_session\": \"eval_xvla_k085_s42\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-20T21:57:02.351Z\"}, \"eval_xvla_prune_k08_seed43\": {\"completed_at\": \"2026-05-20T21:44:22.944Z\", \"conclusion\": \"success\", \"created_at\": \"2026-05-20T20:27:57.915Z\", \"hypothesis\": \"X-VLA L2 norm pruning k=0.8 seed43 provides 2nd seed for cliff threshold localization. Combined with seed42, narrows the cliff to a 5pp interval.\", \"metrics\": {\"num_episodes\": 500, \"success_rate\": 0.884, \"wilson_ci_95\": [0.853, 0.909]}, \"notes\": \"[M046] Pruning method corrected: was labeled random but actually uses L2 norm topk selection.\", \"retry_count\": 0, \"spec\": {\"checkpoint_path\": \"N/A\", \"command\": \"python -u eval_xvla_pruning_libero.py --model_path /root/autodl-tmp/X-VLA-Libero --suite libero_object --keep_ratio 0.8 --num_episodes 50 --seed 43 --domain_id 3 --gpu 0 --output eval_results/xvla_prune_k08_libero_object_seed43.json\", \"data_count\": 50, \"data_path\": \"libero_object\", \"gpu\": \"cuda:1\", \"log_path\": \"cqa1-33015:/root/autodl-tmp/X-VLA-Libero/eval_results/xvla_prune_k08_libero_object_seed43.json\", \"model_name\": \"X-VLA-Libero\", \"pid\": 262573, \"seed\": 43, \"server\": \"cqa1-33015\", \"tmux_session\": \"eval_xvla_k08_s43\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-20T21:44:22.944Z\"}, \"eval_xvla_prune_k01_seed42\": {\"completed_at\": \"2026-05-20T20:57:58.079Z\", \"conclusion\": \"success\", \"created_at\": \"2026-05-20T18:58:45.681Z\", \"hypothesis\": \"X-VLA L2 norm pruning at k=0.1 with seed=42. Extends curve to 90% token removal. Seed42 k=0.2=5.2%. If k=0.1 ≈ 0-5%, confirms near-total collapse at extreme compression for linear projection connector.\", \"metrics\": {\"num_episodes\": 500, \"success_rate\": 0, \"wilson_ci_95\": [0, 0.008]}, \"retry_count\": 0, \"spec\": {\"checkpoint_path\": \"N/A (eval only)\", \"checkpoint_source\": \"/root/autodl-tmp/X-VLA-Libero\", \"command\": \"python -u eval_xvla_pruning_libero.py --model_path /root/autodl-tmp/X-VLA-Libero --suite libero_object --keep_ratio 0.1 --num_episodes 50 --seed 42 --domain_id 3 --gpu 0 --output eval_results/xvla_prune_k01_libero_object_seed42.json\", \"data_count\": 500, \"data_path\": \"libero_object\", \"eval_data\": \"LIBERO-Object (10 tasks x 50 episodes)\", \"gpu\": \"cuda:0\", \"log_path\": \"/root/autodl-tmp/importance_margin_vla_compress/logs/eval_xvla_prune_k01_seed42.log\", \"model_name\": \"X-VLA-Libero\", \"pid\": 854755, \"seed\": 42, \"server\": \"cqa1-33015\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-20T20:57:58.079Z\"}, \"eval_xvla_prune_k095_seed43\": {\"completed_at\": \"2026-05-20T20:43:19.590Z\", \"conclusion\": \"success\", \"created_at\": \"2026-05-20T19:57:33.756Z\", \"hypothesis\": \"X-VLA L2 norm pruning k=0.95 seed43 provides 2nd seed for high-retention curve extension. X-VLA baseline=99.2%, k=0.9 seed43=? Expected near-baseline SR, confirming minimal impact of 5% token removal on linear projection connector.\", \"metrics\": {\"num_episodes\": 500, \"success_rate\": 0.99, \"wilson_ci_95\": [0.9768, 0.9957]}, \"notes\": \"[M046] Pruning method corrected: was labeled random but actually uses L2 norm topk selection.\", \"retry_count\": 0, \"spec\": {\"checkpoint_path\": \"N/A\", \"checkpoint_source\": \"/root/autodl-tmp/X-VLA-Libero\", \"command\": \"CUDA_VISIBLE_DEVICES=1 python -u eval_xvla_pruning_libero.py --model_path /root/autodl-tmp/X-VLA-Libero --suite libero_object --keep_ratio 0.95 --num_episodes 50 --seed 43 --domain_id 3 --gpu 0 --output eval_results/xvla_prune_k095_libero_object_seed43.json\", \"data_count\": 500, \"data_path\": \"libero_object\", \"eval_data\": \"LIBERO-Object (10 tasks x 50 episodes)\", \"gpu\": \"cuda:1\", \"log_path\": \"cqa1-33015:/root/autodl-tmp/X-VLA-Libero/eval_results/xvla_prune_k095_libero_object_seed43.json\", \"model_name\": \"X-VLA-Libero\", \"pid\": 961641, \"seed\": 43, \"server\": \"cqa1-33015\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-20T20:44:35.339Z\"}, \"eval_xvla_prune_k095_seed44\": {\"completed_at\": \"2026-05-20T20:43:20.938Z\", \"conclusion\": \"success\", \"created_at\": \"2026-05-20T19:57:35.290Z\", \"hypothesis\": \"X-VLA L2 norm pruning k=0.95 seed44 provides 3rd seed for high-retention curve extension. X-VLA baseline=99.2%, k=0.9 seed44=98.2%. Expected near-baseline SR, completing 3-seed k=0.95 data point.\", \"metrics\": {\"num_episodes\": 500, \"success_rate\": 0.994, \"wilson_ci_95\": [0.983, 0.998]}, \"notes\": \"[M046] Pruning method corrected: was labeled random but actually uses L2 norm topk selection.\", \"retry_count\": 0, \"spec\": {\"checkpoint_path\": \"N/A\", \"checkpoint_source\": \"/root/autodl-tmp/X-VLA-Libero\", \"command\": \"CUDA_VISIBLE_DEVICES=3 python -u eval_xvla_pruning_libero.py --model_path /root/autodl-tmp/X-VLA-Libero --suite libero_object --keep_ratio 0.95 --num_episodes 50 --seed 44 --domain_id 3 --gpu 0 --output eval_results/xvla_prune_k095_libero_object_seed44.json\", \"data_count\": 500, \"data_path\": \"libero_object\", \"eval_data\": \"LIBERO-Object (10 tasks x 50 episodes)\", \"gpu\": \"cuda:3\", \"log_path\": \"cqa1-33015:/root/autodl-tmp/X-VLA-Libero/eval_results/xvla_prune_k095_libero_object_seed44.json\", \"model_name\": \"X-VLA-Libero\", \"pid\": 961802, \"seed\": 44, \"server\": \"cqa1-33015\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-20T20:43:20.938Z\"}, \"eval_xvla_prune_k095_seed42\": {\"completed_at\": \"2026-05-20T20:30:43.657Z\", \"conclusion\": \"success\", \"created_at\": \"2026-05-20T19:32:58.096Z\", \"hypothesis\": \"X-VLA L2 norm pruning k=0.95 seed42 extends the curve to the high-retention end. X-VLA baseline=99.2%, k=0.9=97.8%. k=0.95 should be near-baseline, completing the 7-point curve (k=0.95→0.1).\", \"metrics\": {\"num_episodes\": 500, \"success_rate\": 0.99, \"wilson_ci_95\": [0.977, 0.996]}, \"notes\": \"[M046] Pruning method corrected: was labeled random but actually uses L2 norm topk selection.\", \"retry_count\": 0, \"spec\": {\"checkpoint_path\": \"N/A (eval only)\", \"checkpoint_source\": \"/root/autodl-tmp/X-VLA-Libero\", \"command\": \"CUDA_VISIBLE_DEVICES=2 python -u eval_xvla_pruning_libero.py --model_path /root/autodl-tmp/X-VLA-Libero --suite libero_object --keep_ratio 0.95 --num_episodes 50 --seed 42 --domain_id 3 --gpu 0\", \"data_count\": 500, \"data_path\": \"libero_object\", \"eval_data\": \"LIBERO-Object (10 tasks x 50 episodes)\", \"gpu\": \"cuda:2\", \"log_path\": \"/root/autodl-tmp/importance_margin_vla_compress/logs/eval_xvla_k095_seed42.log\", \"model_name\": \"X-VLA-Libero\", \"pid\": 948547, \"seed\": 42, \"server\": \"cqa1-33015\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-20T20:30:43.657Z\"}, \"eval_xvla_prune_k01_seed44\": {\"completed_at\": \"2026-05-20T19:37:48.239Z\", \"conclusion\": \"success\", \"created_at\": \"2026-05-20T17:29:15.831Z\", \"hypothesis\": \"X-VLA L2 norm pruning at k=0.1 with seed=44. Extends curve to 90% token removal. Seed42 k=0.2=5.2%. If k=0.1 ≈ 0-5%, confirms near-total collapse at extreme compression for linear projection connector.\", \"metrics\": {\"num_episodes\": 500, \"success_rate\": 0, \"wilson_ci_95\": [0, 0.008]}, \"retry_count\": 0, \"spec\": {\"checkpoint_path\": \"N/A (eval only)\", \"checkpoint_source\": \"/root/autodl-tmp/X-VLA-Libero\", \"command\": \"python -u eval_xvla_pruning_libero.py --model_path /root/autodl-tmp/X-VLA-Libero --suite libero_object --keep_ratio 0.1 --num_episodes 50 --seed 44 --domain_id 3 --gpu 0 --output eval_results/xvla_prune_k01_libero_object_seed44.json\", \"data_count\": 500, \"data_path\": \"libero_object\", \"eval_data\": \"LIBERO-Object (10 tasks x 50 episodes)\", \"gpu\": \"cuda:3\", \"log_path\": \"/root/autodl-tmp/importance_margin_vla_compress/logs/eval_xvla_prune_k01_seed44.log\", \"model_name\": \"X-VLA-Libero\", \"pid\": 696123, \"seed\": 44, \"server\": \"cqa1-33015\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-20T19:37:48.239Z\"}, \"eval_xvla_prune_k01_seed43\": {\"completed_at\": \"2026-05-20T19:37:06.762Z\", \"conclusion\": \"success\", \"created_at\": \"2026-05-20T17:29:14.767Z\", \"hypothesis\": \"X-VLA L2 norm pruning at k=0.1 with seed=43. Extends curve to 90% token removal. Seed42 k=0.2=5.2%. If k=0.1 ≈ 0-5%, confirms near-total collapse at extreme compression for linear projection connector.\", \"metrics\": {\"num_episodes\": 500, \"success_rate\": 0, \"wilson_ci_95\": [0, 0.0076]}, \"retry_count\": 0, \"spec\": {\"checkpoint_path\": \"N/A (eval only)\", \"checkpoint_source\": \"/root/autodl-tmp/X-VLA-Libero\", \"command\": \"python -u eval_xvla_pruning_libero.py --model_path /root/autodl-tmp/X-VLA-Libero --suite libero_object --keep_ratio 0.1 --num_episodes 50 --seed 43 --domain_id 3 --gpu 0 --output eval_results/xvla_prune_k01_libero_object_seed43.json\", \"data_count\": 500, \"data_path\": \"libero_object\", \"eval_data\": \"LIBERO-Object (10 tasks x 50 episodes)\", \"gpu\": \"cuda:1\", \"log_path\": \"/root/autodl-tmp/importance_margin_vla_compress/logs/eval_xvla_prune_k01_seed43.log\", \"model_name\": \"X-VLA-Libero\", \"pid\": 694944, \"seed\": 43, \"server\": \"cqa1-33015\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-20T19:37:06.762Z\"}, \"eval_openvla_prune_random_k09_seed42\": {\"completed_at\": \"2026-05-20T23:30:00.000Z\", \"conclusion\": \"success\", \"created_at\": \"2026-05-20T19:13:37.199Z\", \"hypothesis\": \"OpenVLA random pruning at k=0.9 with seed=42 provides the 3rd seed for MF-3 statistical validation. seed7=62%, seed43=62.2%. If seed42 ≈ 62%, confirms robust graded degradation at the critical 10% pruning point.\", \"metrics\": {\"num_episodes\": 500, \"success_rate\": 0.646, \"total_successes\": 323, \"wilson_ci_95\": [0.604, 0.686]}, \"parent\": \"eval_openvla_random_pruning_sweep\", \"retry_count\": 0, \"spec\": {\"checkpoint_path\": \"/root/autodl-tmp/openvla-libero-object\", \"checkpoint_source\": \"/root/autodl-tmp/openvla-libero-object\", \"command\": \"CUDA_VISIBLE_DEVICES=1 MUJOCO_GL=egl python -u eval_openvla_libero.py --mode random_prune --k_ratio 0.9 --suite libero_object --seed 42 --output eval_results/openvla_random_k09_seed42.json\", \"data_count\": 500, \"data_path\": \"/root/autodl-tmp/openvla-libero-object\", \"eval_data\": \"libero_object (10 tasks x 50 eps)\", \"gpu\": \"cuda:1\", \"log_path\": \"/root/autodl-tmp/importance_margin_vla_compress/logs/eval_random_k09_seed42.log\", \"model_name\": \"openvla-7b-libero-object\", \"pid\": 579915, \"seed\": 42, \"server\": \"westd-41074\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-20T19:30:12.381Z\"}, \"eval_openvla_prune_random_k09_seed43\": {\"completed_at\": \"2026-05-20T19:12:42.943Z\", \"conclusion\": \"success\", \"created_at\": \"2026-05-20T19:11:41.824Z\", \"hypothesis\": \"OpenVLA random pruning at k=0.9 with seed=43 verifies reproducibility of seed=7 result (62% SR). The k=0.9 point is critical for demonstrating graded degradation in MLP-connector architecture.\", \"metrics\": {\"num_episodes\": 500, \"success_rate\": 0.622}, \"parent\": \"eval_openvla_prune_seed43_sweep\", \"retry_count\": 0, \"spec\": {\"checkpoint_path\": \"/root/autodl-tmp/openvla-libero-object\", \"checkpoint_source\": \"/root/autodl-tmp/openvla-libero-object\", \"command\": \"CUDA_VISIBLE_DEVICES=0 MUJOCO_GL=egl python eval_openvla_libero.py --mode random_prune --k_ratio 0.9 --suite libero_object --seed 43\", \"data_count\": 500, \"data_path\": \"/root/autodl-tmp/openvla-libero-object\", \"eval_data\": \"libero_object (10 tasks x 50 eps)\", \"gpu\": \"cuda:0\", \"log_path\": \"/root/autodl-tmp/importance_margin_vla_compress/logs/eval_random_k09_seed43.log\", \"model_name\": \"openvla-7b-libero-object\", \"note\": \"Salvaged from duplicate process on westd-27271 before kill\", \"seed\": 43, \"server\": \"westd-27271\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-20T19:12:42.943Z\"}, \"eval_openvla_prune_random_k05_seed43_v2\": {\"completed_at\": \"2026-05-20T19:09:26.267Z\", \"conclusion\": \"success\", \"created_at\": \"2026-05-20T13:37:11.254Z\", \"hypothesis\": \"OpenVLA random pruning at k=0.5 with seed=43 verifies reproducibility of seed=7 result (37.4% SR). Retry with correct script (eval_openvla_libero.py). If seed43 ≈ 37.4%, confirms graded degradation pattern is robust across seeds.\", \"metrics\": {\"num_episodes\": 500, \"success_rate\": 0.356}, \"parent\": \"eval_openvla_prune_seed43_sweep\", \"retry_count\": 0, \"spec\": {\"account\": \"root\", \"checkpoint_path\": \"/root/autodl-tmp/openvla-libero-object\", \"checkpoint_source\": \"/root/autodl-tmp/openvla-libero-object\", \"command\": \"CUDA_VISIBLE_DEVICES=1 MUJOCO_GL=egl python eval_openvla_libero.py --mode random_prune --k_ratio 0.5 --suite libero_object --seed 43 --output eval_results/openvla_random_k05_seed43_v2.json\", \"data_count\": 500, \"data_path\": \"/root/autodl-tmp/openvla-libero-object\", \"eval_data\": \"libero_object (10 tasks x 50 eps)\", \"gpu\": \"cuda:1\", \"log_path\": \"/root/autodl-tmp/importance_margin_vla_compress/eval_openvla_random_k05_seed43_v2.log\", \"model_name\": \"openvla-7b-libero-object\", \"pid\": 468858, \"seed\": 43, \"server\": \"westd-41074\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-20T19:09:26.267Z\"}, \"eval_xvla_prune_k02_seed44\": {\"completed_at\": \"2026-05-20T18:58:30.945Z\", \"conclusion\": \"success\", \"created_at\": \"2026-05-20T16:50:07.505Z\", \"hypothesis\": \"X-VLA L2 norm pruning at k=0.2 with seed=44 (3rd seed). Seed42 k=0.2=5.2%, seed43 k=0.2 running. If seed44 ≈ 5%, confirms near-total collapse at 80% token removal across 3 seeds.\", \"metrics\": {\"num_episodes\": 500, \"success_rate\": 0.04}, \"retry_count\": 0, \"spec\": {\"checkpoint_path\": \"N/A (eval only)\", \"checkpoint_source\": \"/root/autodl-tmp/X-VLA-Libero\", \"command\": \"python -u eval_xvla_pruning_libero.py --keep_ratio 0.2 --seed 44 --suite libero_object --num_episodes 50\", \"data_count\": 500, \"data_path\": \"libero_object\", \"eval_data\": \"libero_object\", \"gpu\": \"cuda:2\", \"log_path\": \"/root/autodl-tmp/importance_margin_vla_compress/eval_results/xvla_prune_k02_libero_object_seed44.json\", \"model_name\": \"X-VLA-Libero\", \"pid\": 518362, \"seed\": 44, \"server\": \"cqa1-33015\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-20T18:58:39.891Z\"}, \"eval_xvla_prune_k02_seed43\": {\"completed_at\": \"2026-05-20T18:58:29.628Z\", \"conclusion\": \"success\", \"created_at\": \"2026-05-20T16:50:05.876Z\", \"hypothesis\": \"X-VLA L2 norm pruning at k=0.2 with seed=43. Seed42 k=0.2=5.2%. Extends seed43 curve to extreme compression. If seed43 ≈ 5%, confirms near-total collapse at 80% token removal is consistent.\", \"metrics\": {\"num_episodes\": 500, \"success_rate\": 0.048}, \"retry_count\": 0, \"spec\": {\"checkpoint_path\": \"N/A (eval only)\", \"checkpoint_source\": \"/root/autodl-tmp/X-VLA-Libero\", \"command\": \"python -u eval_xvla_pruning_libero.py --keep_ratio 0.2 --seed 43 --suite libero_object --num_episodes 50\", \"data_count\": 500, \"data_path\": \"libero_object\", \"eval_data\": \"libero_object\", \"gpu\": \"cuda:0\", \"log_path\": \"/root/autodl-tmp/importance_margin_vla_compress/eval_results/xvla_prune_k02_libero_object_seed43.json\", \"model_name\": \"X-VLA-Libero\", \"pid\": 443004, \"seed\": 43, \"server\": \"cqa1-33015\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-20T18:58:39.148Z\"}, \"eval_openvla_prune_l2norm_k09\": {\"completed_at\": \"2026-05-20T18:13:32.213Z\", \"conclusion\": \"success\", \"created_at\": \"2026-05-20T13:17:18.346Z\", \"hypothesis\": \"OpenVLA L2 norm pruning at k=0.9 (retain 230/256 tokens). If L2 norm SR ≈ random pruning SR (62%), confirms L2 norm ≈ random for MLP projector, supporting architecture-determines-compressibility thesis.\", \"metrics\": {\"num_episodes\": 500, \"success_rate\": 0.706}, \"retry_count\": 0, \"spec\": {\"checkpoint_path\": \"N/A (eval only)\", \"checkpoint_source\": \"openvla-oft checkpoint\", \"command\": \"python -u eval_openvla_l2norm_libero.py --keep_ratio 0.9 --seed 42 --suite libero_object --num_episodes 50\", \"data_count\": 500, \"data_path\": \"libero_object\", \"eval_data\": \"LIBERO-Object (10 tasks x 50 episodes)\", \"gpu\": \"cuda:2\", \"log_path\": \"/root/autodl-tmp/importance_margin_vla_compress/eval_results/openvla_l2norm_prune_k0_9_object.json\", \"model_name\": \"OpenVLA-OFT\", \"pid\": 796062, \"seed\": 42, \"server\": \"westd-38929\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-20T18:16:12.843Z\"}, \"eval_openvla_prune_random_k07_seed43_v2\": {\"completed_at\": \"2026-05-20T18:14:52.642Z\", \"conclusion\": \"success\", \"created_at\": \"2026-05-20T13:37:10.166Z\", \"hypothesis\": \"OpenVLA random pruning at k=0.7 with seed=43 verifies reproducibility of seed=7 result (49% SR). Retry with correct script (eval_openvla_libero.py). If seed43 ≈ 49%, confirms graded degradation pattern is robust across seeds.\", \"metrics\": {\"num_episodes\": 500, \"success_rate\": 0.526}, \"parent\": \"eval_openvla_prune_seed43_sweep\", \"retry_count\": 0, \"spec\": {\"account\": \"root\", \"checkpoint_path\": \"/root/autodl-tmp/openvla-libero-object\", \"checkpoint_source\": \"/root/autodl-tmp/openvla-libero-object\", \"command\": \"CUDA_VISIBLE_DEVICES=0 MUJOCO_GL=egl python eval_openvla_libero.py --mode random_prune --k_ratio 0.7 --suite libero_object --seed 43 --output eval_results/openvla_random_k07_seed43_v2.json\", \"data_count\": 500, \"data_path\": \"/root/autodl-tmp/openvla-libero-object\", \"eval_data\": \"libero_object (10 tasks x 50 eps)\", \"gpu\": \"cuda:0\", \"log_path\": \"/root/autodl-tmp/importance_margin_vla_compress/eval_openvla_random_k07_seed43_v2.log\", \"model_name\": \"openvla-7b-libero-object\", \"pid\": 468324, \"seed\": 43, \"server\": \"westd-41074\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-20T18:14:57.205Z\"}, \"eval_openvla_prune_l2norm_k095\": {\"completed_at\": \"2026-05-20T18:13:33.759Z\", \"conclusion\": \"success\", \"created_at\": \"2026-05-20T13:17:20.150Z\", \"hypothesis\": \"OpenVLA L2 norm pruning at k=0.95 (retain 243/256 tokens). Near-lossless point. If SR ≈ baseline (74%), minimal tokens carry most information regardless of selection method.\", \"metrics\": {\"num_episodes\": 500, \"success_rate\": 0.706}, \"retry_count\": 0, \"spec\": {\"checkpoint_path\": \"N/A (eval only)\", \"checkpoint_source\": \"openvla-oft checkpoint\", \"command\": \"python -u eval_openvla_l2norm_libero.py --keep_ratio 0.95 --seed 42 --suite libero_object --num_episodes 50\", \"data_count\": 500, \"data_path\": \"libero_object\", \"eval_data\": \"LIBERO-Object (10 tasks x 50 episodes)\", \"gpu\": \"cuda:3\", \"log_path\": \"/root/autodl-tmp/importance_margin_vla_compress/eval_results/openvla_l2norm_prune_k0_95_object.json\", \"model_name\": \"OpenVLA-OFT\", \"pid\": 796839, \"seed\": 42, \"server\": \"westd-38929\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-20T18:13:41.918Z\"}, \"eval_openvla_prune_l2norm_k03\": {\"completed_at\": \"2026-05-20T18:13:29.969Z\", \"conclusion\": \"success\", \"created_at\": \"2026-05-20T17:49:04.494Z\", \"hypothesis\": \"OpenVLA L2 norm pruning at k=0.3 (keep 30% vision tokens by L2 norm). D108 unifies pruning method across models. If L2 norm k=0.3 ≈ random k=0.3 (20.6%), confirms architecture determines compressibility, not pruning strategy.\", \"metrics\": {\"num_episodes\": 500, \"success_rate\": 0.25}, \"retry_count\": 0, \"spec\": {\"checkpoint_path\": \"N/A (eval only)\", \"checkpoint_source\": \"openvla-oft checkpoint\", \"command\": \"python -u eval_openvla_l2norm_libero.py --keep_ratio 0.3 --seed 42 --suite libero_object --num_episodes 50\", \"data_count\": 500, \"data_path\": \"libero_object\", \"eval_data\": \"LIBERO-Object (10 tasks x 50 episodes)\", \"gpu\": \"cuda:1\", \"log_path\": \"/root/autodl-tmp/importance_margin_vla_compress/eval_results/openvla_l2norm_prune_k0_3_object.json\", \"model_name\": \"OpenVLA-OFT\", \"pid\": 788043, \"seed\": 42, \"server\": \"westd-38929\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-20T18:13:40.284Z\"}, \"eval_openvla_prune_l2norm_k05\": {\"completed_at\": \"2026-05-20T18:13:26.599Z\", \"conclusion\": \"success\", \"created_at\": \"2026-05-20T17:49:03.193Z\", \"hypothesis\": \"OpenVLA L2 norm pruning at k=0.5 (keep 50% vision tokens by L2 norm). D108 unifies pruning method across models. If L2 norm k=0.5 ≈ random k=0.5 (37.4%), confirms architecture determines compressibility, not pruning strategy.\", \"metrics\": {\"num_episodes\": 500, \"success_rate\": 0.392}, \"retry_count\": 0, \"spec\": {\"checkpoint_path\": \"N/A (eval only)\", \"checkpoint_source\": \"openvla-oft checkpoint\", \"command\": \"python -u eval_openvla_l2norm_libero.py --keep_ratio 0.5 --seed 42 --suite libero_object --num_episodes 50\", \"data_count\": 500, \"data_path\": \"libero_object\", \"eval_data\": \"LIBERO-Object (10 tasks x 50 episodes)\", \"gpu\": \"cuda:0\", \"log_path\": \"/root/autodl-tmp/importance_margin_vla_compress/eval_results/openvla_l2norm_prune_k0_5_object.json\", \"model_name\": \"OpenVLA-OFT\", \"pid\": 787425, \"seed\": 42, \"server\": \"westd-38929\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-20T18:13:38.867Z\"}, \"eval_xvla_prune_k03_seed43\": {\"completed_at\": \"2026-05-20T17:11:27.523Z\", \"conclusion\": \"success\", \"created_at\": \"2026-05-20T16:50:01.675Z\", \"hypothesis\": \"X-VLA L2 norm pruning at k=0.3 with seed=43. Seed42=23.0%. If seed43 ≈ 23%, confirms severe degradation at extreme compression is consistent across seeds.\", \"metrics\": {\"num_episodes\": 500, \"success_rate\": 0.21}, \"retry_count\": 0, \"spec\": {\"checkpoint_path\": \"N/A (eval only)\", \"checkpoint_source\": \"/root/autodl-tmp/X-VLA-Libero\", \"command\": \"python -u eval_xvla_pruning_libero.py --keep_ratio 0.3 --seed 43 --suite libero_object --num_episodes 50\", \"data_count\": 500, \"data_path\": \"libero_object\", \"eval_data\": \"libero_object\", \"gpu\": \"cuda:3\", \"log_path\": \"/root/autodl-tmp/importance_margin_vla_compress/eval_results/xvla_prune_k03_libero_object_seed43.json\", \"model_name\": \"X-VLA-Libero\", \"pid\": 344867, \"seed\": 43, \"server\": \"cqa1-33015\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-20T17:29:01.183Z\"}, \"eval_xvla_prune_k03_seed44\": {\"completed_at\": \"2026-05-20T17:11:28.861Z\", \"conclusion\": \"success\", \"created_at\": \"2026-05-20T16:50:03.822Z\", \"hypothesis\": \"X-VLA L2 norm pruning at k=0.3 with seed=44 (3rd seed). Seed42=23.0%. Third seed for extreme compression point, completes 3-seed coverage for all k values.\", \"metrics\": {\"num_episodes\": 500, \"success_rate\": 0.228}, \"retry_count\": 0, \"spec\": {\"checkpoint_path\": \"N/A (eval only)\", \"checkpoint_source\": \"/root/autodl-tmp/X-VLA-Libero\", \"command\": \"python -u eval_xvla_pruning_libero.py --keep_ratio 0.3 --seed 44 --suite libero_object --num_episodes 50\", \"data_count\": 500, \"data_path\": \"libero_object\", \"eval_data\": \"libero_object\", \"gpu\": \"cuda:1\", \"log_path\": \"/root/autodl-tmp/importance_margin_vla_compress/eval_results/xvla_prune_k03_libero_object_seed44.json\", \"model_name\": \"X-VLA-Libero\", \"pid\": 346216, \"seed\": 44, \"server\": \"cqa1-33015\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-20T17:11:39.783Z\"}, \"eval_xvla_prune_k05_seed44\": {\"completed_at\": \"2026-05-20T17:10:17.795Z\", \"conclusion\": \"success\", \"created_at\": \"2026-05-20T16:49:59.697Z\", \"hypothesis\": \"X-VLA L2 norm pruning at k=0.5 with seed=44 (3rd seed). Seed42=42.6%, seed43=44.2%. If seed44 also ~43%, confirms steep degradation below cliff onset is consistent across seeds.\", \"metrics\": {\"num_episodes\": 500, \"success_rate\": 0.444}, \"retry_count\": 0, \"spec\": {\"checkpoint_path\": \"N/A (eval only)\", \"checkpoint_source\": \"/root/autodl-tmp/X-VLA-Libero\", \"command\": \"python -u eval_xvla_pruning_libero.py --model_path /root/autodl-tmp/X-VLA-Libero --suite libero_object --keep_ratio 0.5 --num_episodes 50 --seed 44 --domain_id 3 --gpu 0 --output eval_results/xvla_prune_k05_libero_object_seed44.json\", \"data_count\": 500, \"data_path\": \"libero_object\", \"eval_data\": \"LIBERO-Object (10 tasks x 50 episodes)\", \"log_path\": \"N/A (already completed)\", \"model_name\": \"X-VLA-Libero\", \"seed\": 44, \"server\": \"cqa1-33015\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-20T17:10:23.370Z\"}, \"eval_xvla_prune_k07_seed44\": {\"completed_at\": \"2026-05-20T16:50:17.608Z\", \"conclusion\": \"success\", \"created_at\": \"2026-05-20T13:26:03.840Z\", \"hypothesis\": \"X-VLA L2 norm pruning at k=0.7 with seed=44 (3rd seed). Seed42=56.2%, seed43=59.0%. If seed44 also ~56-59%, confirms cliff onset at k=0.7 is robust across 3 seeds.\", \"metrics\": {\"episodes\": 500, \"success_rate\": 0.564}, \"retry_count\": 0, \"spec\": {\"checkpoint_path\": \"/root/autodl-tmp/X-VLA-Libero\", \"checkpoint_source\": \"/root/autodl-tmp/X-VLA-Libero\", \"command\": \"CUDA_VISIBLE_DEVICES=0 MUJOCO_GL=egl python -u eval_xvla_pruning_libero.py --model_path /root/autodl-tmp/X-VLA-Libero --suite libero_object --keep_ratio 0.7 --num_episodes 50 --seed 44 --domain_id 3 --gpu 0 --output eval_results/xvla_prune_k0.7_libero_object_seed44.json\", \"data_count\": 500, \"data_path\": \"libero_object\", \"eval_data\": \"libero_object\", \"log_path\": \"/tmp/eval_xvla_k07_seed44.log\", \"model_name\": \"X-VLA-Libero\", \"seed\": 44, \"server\": \"cqa1-33015\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-20T16:50:17.607Z\"}, \"eval_xvla_prune_k09_seed44\": {\"completed_at\": \"2026-05-20T16:50:16.026Z\", \"conclusion\": \"success\", \"created_at\": \"2026-05-20T13:26:04.825Z\", \"hypothesis\": \"X-VLA L2 norm pruning at k=0.9 with seed=44 (3rd seed). Seed42=99.2%, seed43=97.6%. If seed44 also >=97%, confirms near-lossless region is robust across 3 seeds.\", \"metrics\": {\"episodes\": 500, \"success_rate\": 0.982}, \"retry_count\": 0, \"spec\": {\"checkpoint_path\": \"/root/autodl-tmp/X-VLA-Libero\", \"checkpoint_source\": \"/root/autodl-tmp/X-VLA-Libero\", \"command\": \"CUDA_VISIBLE_DEVICES=1 MUJOCO_GL=egl python -u eval_xvla_pruning_libero.py --model_path /root/autodl-tmp/X-VLA-Libero --suite libero_object --keep_ratio 0.9 --num_episodes 50 --seed 44 --domain_id 3 --gpu 0 --output eval_results/xvla_prune_k0.9_libero_object_seed44.json\", \"data_count\": 500, \"data_path\": \"libero_object\", \"eval_data\": \"libero_object\", \"log_path\": \"/tmp/eval_xvla_k09_seed44.log\", \"model_name\": \"X-VLA-Libero\", \"seed\": 44, \"server\": \"cqa1-33015\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-20T16:50:16.026Z\"}, \"eval_openvla_prune_random_k05_seed43\": {\"completed_at\": \"2026-05-20T16:49:44.800Z\", \"conclusion\": \"failed\", \"created_at\": \"2026-05-20T13:18:44.772Z\", \"hypothesis\": \"OpenVLA random pruning at k=0.5 with seed=43 verifies reproducibility of seed=7 result (37.4% SR). If seed43 ≈ 37.4%, confirms graded degradation pattern is robust across seeds.\", \"notes\": \"Wrong script: used eval_oft_prune_libero.py which loads OFT model instead of OpenVLA. Data invalid. Replaced by eval_openvla_prune_random_k05_seed43_v2.\", \"parent\": \"eval_openvla_prune_seed43_sweep\", \"retry_count\": 0, \"spec\": {\"account\": \"root\", \"checkpoint_path\": \"/root/autodl-tmp/openvla-oft-libero-object\", \"checkpoint_source\": \"/root/autodl-tmp/openvla-oft-libero-object\", \"command\": \"CUDA_VISIBLE_DEVICES=1 MUJOCO_GL=egl python -u eval_oft_prune_libero.py --k_ratio 0.5 --suite libero_object --num_episodes 50 --seed 43 --output eval_results/eval_openvla_random_k05_seed43.json\", \"data_count\": 500, \"data_path\": \"/root/autodl-tmp/openvla-oft-libero-object\", \"eval_data\": \"libero_object (10 tasks x 50 eps)\", \"gpu\": \"cuda:1\", \"log_path\": \"/root/autodl-tmp/importance_margin_vla_compress/logs/eval_openvla_random_k05_seed43.log\", \"model_name\": \"openvla-7b-oft-libero-object\", \"pid\": 461577, \"seed\": 43, \"server\": \"westd-41074\", \"tmux_session\": \"eval_random_k05_seed43\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-20T16:49:44.800Z\"}, \"eval_openvla_prune_random_k07_seed43\": {\"completed_at\": \"2026-05-20T16:49:43.237Z\", \"conclusion\": \"failed\", \"created_at\": \"2026-05-20T13:18:43.718Z\", \"hypothesis\": \"OpenVLA random pruning at k=0.7 with seed=43 verifies reproducibility of seed=7 result (49% SR). If seed43 ≈ 49%, confirms graded degradation pattern is robust across seeds.\", \"notes\": \"Wrong script: used eval_oft_prune_libero.py which loads OFT model instead of OpenVLA. Data invalid. Replaced by eval_openvla_prune_random_k07_seed43_v2.\", \"parent\": \"eval_openvla_prune_seed43_sweep\", \"retry_count\": 0, \"spec\": {\"account\": \"root\", \"checkpoint_path\": \"/root/autodl-tmp/openvla-oft-libero-object\", \"checkpoint_source\": \"/root/autodl-tmp/openvla-oft-libero-object\", \"command\": \"CUDA_VISIBLE_DEVICES=0 MUJOCO_GL=egl python -u eval_oft_prune_libero.py --k_ratio 0.7 --suite libero_object --num_episodes 50 --seed 43 --output eval_results/eval_openvla_random_k07_seed43.json\", \"data_count\": 500, \"data_path\": \"/root/autodl-tmp/openvla-oft-libero-object\", \"eval_data\": \"libero_object (10 tasks x 50 eps)\", \"gpu\": \"cuda:0\", \"log_path\": \"/root/autodl-tmp/importance_margin_vla_compress/logs/eval_openvla_random_k07_seed43.log\", \"model_name\": \"openvla-7b-oft-libero-object\", \"pid\": 461502, \"seed\": 43, \"server\": \"westd-41074\", \"tmux_session\": \"eval_random_k07_seed43\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-20T16:49:43.237Z\"}, \"eval_oft_baseline_k10\": {\"completed_at\": \"2026-05-20T13:10:53.920Z\", \"conclusion\": \"failed\", \"created_at\": \"2026-05-20T12:55:13.356Z\", \"hypothesis\": \"OFT model without pruning (k=1.0) should achieve ~74% SR on libero_object if the eval pipeline is correct; if SR=0% then the OFT pruning sweep results (k=0.95=0%, k=0.9=0%) are due to a model loading/inference bug, not catastrophic pruning sensitivity.\", \"notes\": \"OFT k=1.0 baseline (no pruning) = 0% SR on Task 1, confirming eval script bug (action normalization / image preprocessing / prompt format inconsistency with OFT original code). All OFT pruning data invalid. OFT relegated to entropy-only analysis in paper (Table 1 footnote §). Director decision: do not fix OFT eval, not worth the time investment.\", \"retry_count\": 0, \"spec\": {\"checkpoint_path\": \"/root/autodl-tmp/openvla-oft-libero-object\", \"checkpoint_source\": \"/root/autodl-tmp/openvla-oft-libero-object\", \"command\": \"CUDA_VISIBLE_DEVICES=0 MUJOCO_GL=egl python -u eval_oft_prune_libero.py --k_ratio 1.0 --suite libero_object --num_episodes 50 --seed 7 --output eval_results/eval_oft_prune_k10_baseline.json\", \"data_count\": 500, \"data_path\": \"/root/autodl-tmp/openvla-oft-libero-object\", \"eval_data\": \"libero_object (10 tasks x 50 eps)\", \"gpu\": \"cuda:0\", \"log_path\": \"/tmp/oft_k10_full.log\", \"model_name\": \"openvla-7b-oft-libero-object\", \"pid\": 434280, \"seed\": 7, \"server\": \"westd-41074\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-20T13:12:00.402Z\"}, \"eval_openvla_sc_m128_20k_seed42\": {\"completed_at\": \"2026-05-20T09:24:29.766Z\", \"conclusion\": \"negative\", \"created_at\": \"2026-05-20T08:33:32.863Z\", \"failure_reason\": \"startup recovery: process dead, no active cron monitor\", \"hypothesis\": \"OpenVLA with Smart Compress M=128 at 20K steps achieves competitive success rate on LIBERO-Object (C4-ext checkpoint), validating that VTC-only compression preserves action prediction quality\", \"metrics\": {\"episodes_completed\": 44, \"episodes_total\": 50, \"note\": \"0/44 episodes succeeded on Task 0. All episodes timeout at 280 steps. Overfitting confirmed.\", \"seed\": 42, \"suite\": \"libero_object\", \"task_0_sr\": 0}, \"retry_count\": 0, \"spec\": {\"checkpoint_path\": \"checkpoints/openvla_sc_m128/checkpoint_step20000.pt\", \"checkpoint_source\": \"westd-41074:/root/autodl-tmp/importance_margin_vla_compress/checkpoints/openvla_sc_m128/checkpoint_step20000.pt\", \"command\": \"CUDA_VISIBLE_DEVICES=0 MUJOCO_GL=egl python -u eval_openvla_smart_compress.py --n_queries 128 --checkpoint_path checkpoints/openvla_sc_m128/checkpoint_step20000.pt --suite libero_object --num_episodes 50 --gpu 0 --seed 42 --model_path /root/autodl-tmp/openvla-libero-object --output eval_results/eval_openvla_sc_m128_vtconly_20k_seed42.json\", \"data_count\": 500, \"data_path\": \"/root/autodl-tmp/importance_margin_vla_compress/checkpoints/openvla_sc_m128/checkpoint_step20000.pt\", \"estimated_hours\": 50, \"eval_data\": \"libero_object (10 tasks x 50 episodes, seed 42)\", \"log_path\": \"logs/eval_openvla_sc_m128_vtconly_20k_seed42.log\", \"model_name\": \"openvla_sc_m128\", \"pid\": 89467, \"seed\": 42, \"server\": \"westd-38929\", \"started_at\": \"2026-05-20T17:00:22+08:00\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-20T11:56:03.798Z\"}, \"eval_smart_compress_m16_seed44\": {\"completed_at\": \"2026-05-20T09:24:56.802Z\", \"conclusion\": \"success\", \"created_at\": \"2026-05-20T01:13:02.246Z\", \"extra\": {\"hook_events\": [{\"action\": \"agent\", \"event\": \"on_failed\", \"ts\": \"2026-05-20T09:25:05.286695+00:00\"}]}, \"failure_reason\": \"process dead 5× with no sentinel/W&B — auto-resolved as failed\", \"hypothesis\": \"Eval of M=16 seed44 (v3 training) checkpoint on LIBERO-Object (50 eps/task). Third seed for extreme compression point (87.5%). Prior: seed42=55.8%. Completes 3-seed data for M=16 on M-curve.\", \"metrics\": {\"n_episodes\": 500, \"n_queries\": 16, \"overall_sr\": 0.565, \"per_task_sr\": {\"task_0_alphabet_soup\": 0.38, \"task_1_cream_cheese\": 0.7, \"task_2_salad_dressing\": 0.55, \"task_3_bbq_sauce\": 0.42, \"task_4_ketchup\": 0.65, \"task_5_tomato_sauce\": 0.33, \"task_6_butter\": 0.73, \"task_7_milk\": 0.64, \"task_8_chocolate_pudding\": 0.87, \"task_9_orange_juice\": 0.38}, \"seed\": 44, \"suite\": \"libero_object\"}, \"parent\": \"train_smart_compress_m16_seed44_v3\", \"reproduce\": {\"finished_at\": \"2026-05-20T09:24:54.724Z\"}, \"retry_count\": 0, \"spec\": {\"checkpoint_source\": \"train_smart_compress_m16_seed44_v3\", \"command\": \"python -u eval_smart_compress.py --checkpoint checkpoints/smart_compress_m16_seed44/checkpoint.pt --suite libero_object --n_episodes 50 --seed 44\", \"data_count\": \"500\", \"data_path\": \"LIBERO-Object\", \"eval_data\": \"LIBERO-Object (50 eps × 10 tasks)\", \"gpu\": \"cuda:0\", \"model_name\": \"smolvla_base + VisionTokenCompressor(M=16)\", \"pid\": \"994858\", \"seed\": 44, \"server\": \"cqa1-33015\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-20T10:27:29.577Z\"}, \"eval_smart_compress_m16_seed43\": {\"checkpoint_path\": \"/root/autodl-tmp/importance_margin_vla_compress/eval_results/eval_smart_compress_m16_seed43.json\", \"completed_at\": \"2026-05-20T08:32:03.528Z\", \"conclusion\": \"success\", \"created_at\": \"2026-05-19T23:16:37.338Z\", \"hypothesis\": \"Eval Smart Compress M=16 seed43 on LIBERO-Object (500 eps). Third seed for extreme compression point (87.5%). Prior: seed42=55.8%.\", \"log_path\": \"/root/autodl-tmp/importance_margin_vla_compress/logs/eval_smart_compress_m16_seed43.log\", \"metrics\": {\"n_queries\": 16, \"overall_sr\": 0.584, \"per_task_sr\": {\"task_0_alphabet_soup\": 0.428, \"task_1_cream_cheese\": 0.474, \"task_2_salad_dressing\": 0.662, \"task_3_bbq_sauce\": 0.484, \"task_4_ketchup\": 0.742, \"task_5_tomato_sauce\": 0.4, \"task_6_butter\": 0.792, \"task_7_milk\": 0.698, \"task_8_chocolate_pudding\": 0.766, \"task_9_orange_juice\": 0.394}, \"seed\": 43, \"suite\": \"libero_object\", \"wilson_ci_95\": [0.5703, 0.5976]}, \"retry_count\": 0, \"spec\": {\"checkpoint_source\": \"smart_compress_m16\", \"command\": \"python eval_smart_compress.py --M 16 --seed 43\", \"data_count\": 5000, \"data_path\": \"/root/autodl-tmp/importance_margin_vla_compress/data\", \"eval_data\": \"libero_object\", \"model_name\": \"smart_compress_m16\", \"seed\": 43, \"server\": \"cqa1-33015\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-20T08:34:14.695Z\"}, \"eval_smart_compress_m128_seed43\": {\"checkpoint_path\": \"/root/autodl-tmp/importance_margin_vla_compress/checkpoints/smart_compress_m128_seed43/checkpoint.pt\", \"completed_at\": \"2026-05-20T08:31:23.821Z\", \"conclusion\": \"success\", \"created_at\": \"2026-05-19T23:16:35.879Z\", \"hypothesis\": \"Eval Smart Compress M=128 seed43 on LIBERO-Object (500 eps). Third seed for M=128 passthrough point. Prior: seed42=59.8%.\", \"log_path\": \"/root/autodl-tmp/importance_margin_vla_compress/logs/eval_smart_compress_m128_seed43.log\", \"metrics\": {\"n_queries\": 128, \"overall_sr\": 0.54, \"per_task_sr\": {\"task_0_alphabet_soup\": 0.646, \"task_1_cream_cheese\": 0.322, \"task_2_salad_dressing\": 0.614, \"task_3_bbq_sauce\": 0.432, \"task_4_ketchup\": 0.348, \"task_5_tomato_sauce\": 0.442, \"task_6_butter\": 0.716, \"task_7_milk\": 0.604, \"task_8_chocolate_pudding\": 0.818, \"task_9_orange_juice\": 0.458}, \"seed\": 43, \"suite\": \"libero_object\", \"wilson_ci_95\": [0.5262, 0.5538]}, \"retry_count\": 0, \"spec\": {\"checkpoint_source\": \"checkpoints/smart_compress_m128_seed43/checkpoint.pt\", \"command\": \"python eval.py --config configs/smart_compress_m128_seed43.yaml\", \"data_count\": 5000, \"data_path\": \"libero_object\", \"eval_data\": \"libero_object\", \"model_name\": \"smart_compress_m128\", \"seed\": 43, \"server\": \"cqa1-33015\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-20T08:34:05.580Z\"}, \"train_openvla_sc_m128_vtconly_seed42\": {\"completed_at\": \"2026-05-20T08:33:04.639Z\", \"conclusion\": \"killed\", \"created_at\": \"2026-05-19T18:45:06.745Z\", \"hypothesis\": \"VTC-only (no LoRA) on OpenVLA M=128 (256→128 tokens, 50% compression). This is the C4-ext go/no-go gate experiment. If VTC re-encoding significantly outperforms k=0.5 random pruning (37.4% SR), demonstrates learned re-encoding generalizes from pixel-shuffle (SmolVLA) to MLP-projector architecture.\", \"retry_count\": 0, \"spec\": {\"command\": \"python train_openvla_smart_compress.py --config configs/openvla_smart_compress_m128.yaml --output_dir checkpoints/openvla_vtc_m128_only_seed42 --seed 42\", \"data_count\": 273465, \"data_path\": \"HuggingFaceVLA/libero\", \"gpu\": \"cuda:0\", \"model_name\": \"openvla+VTC(M=128)\", \"pid\": 26118, \"seed\": 42, \"server\": \"westd-41074\", \"tmux_session\": \"train_openvla_sc_m128_seed42\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-20T08:33:04.639Z\"}, \"eval_openvla_sc_m128_vtconly_20k_seed42\": {\"completed_at\": \"2026-05-20T07:48:57.478Z\", \"conclusion\": \"killed\", \"created_at\": \"2026-05-20T07:19:29.095Z\", \"extra\": {\"hook_events\": [{\"action\": \"agent\", \"event\": \"on_failed\", \"ts\": \"2026-05-20T07:49:02.307982+00:00\"}]}, \"failure_reason\": \"SSH check failed 5x — last error: Invalid pid/session_name: 'tmux:eval_openvla_sc_m128_20k'. Must match [a-zA-Z0-9_-]+\", \"hypothesis\": \"OpenVLA VTC-only M=128 best checkpoint (20K step, eval loss 2.7768) LIBERO-Object eval. Go/no-go gate: if SR > 37.4% (random pruning k=0.5 baseline), confirms VTC cross-attention re-encoding generalizes from pixel-shuffle (SmolVLA) to MLP-projector architecture (OpenVLA), establishing C4-ext method universality.\", \"parent\": \"train_openvla_sc_m128_vtconly_seed42\", \"retry_count\": 0, \"spec\": {\"checkpoint_path\": \"checkpoints/openvla_sc_m128/checkpoint_step20000.pt\", \"checkpoint_source\": \"checkpoints/openvla_sc_m128/checkpoint_step20000.pt (20K step, eval loss 2.7768)\", \"command\": \"CUDA_VISIBLE_DEVICES=0 MUJOCO_GL=egl python -u eval_openvla_smart_compress.py --n_queries 128 --checkpoint_path checkpoints/openvla_sc_m128/checkpoint_step20000.pt --suite libero_object --num_episodes 50 --gpu 0 --seed 42 --model_path /root/autodl-tmp/openvla-libero-object --output eval_results/eval_openvla_sc_m128_vtconly_20k_seed42.json\", \"data_count\": \"500\", \"data_path\": \"LIBERO-Object\", \"eval_data\": \"LIBERO-Object (10 tasks x 50 episodes)\", \"gpu\": \"cuda:0\", \"log_path\": \"/root/autodl-tmp/importance_margin_vla_compress/logs/eval_openvla_sc_m128_vtconly_20k_seed42.log\", \"model_name\": \"openvla-7b + VTC(M=128)\", \"pid\": \"tmux:eval_openvla_sc_m128_20k\", \"seed\": 42, \"server\": \"westd-27271\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-20T08:10:48.268Z\"}, \"train_openvla_sc_m128_seed42_v2\": {\"completed_at\": \"2026-05-20T07:36:57.910Z\", \"conclusion\": \"killed\", \"created_at\": \"2026-05-19T18:26:58.293Z\", \"hypothesis\": \"VTC+LoRA variant: OpenVLA VTC re-encoding (M=128, 256→128 tokens) + LoRA (r=16, q_proj/v_proj) on westd-27271. Config had lora.enabled=true. If VTC+LoRA > VTC-only, backbone adaptation is complementary to re-encoding for MLP-projector architectures.\", \"parent\": \"train_openvla_sc_m128_seed42\", \"retry_count\": 0, \"spec\": {\"account\": \"root\", \"backend\": \"tmux\", \"checkpoint_path\": \"checkpoints/openvla_sc_m128_seed42/\", \"checkpoint_source\": \"openvla/openvla-7b (libero finetuned)\", \"command\": \"bash -c 'source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/importance_margin_vla_compress && HF_HOME=/root/autodl-tmp/.hf_cache TRANSFORMERS_OFFLINE=1 WANDB_MODE=offline python -u train_openvla_smart_compress.py --config configs/openvla_smart_compress_m128.yaml'\", \"data_count\": \"273465\", \"data_path\": \"HuggingFaceVLA/libero\", \"gpu\": \"cuda:0\", \"log_path\": \"~/runs/importance_margin_vla_compress/train_openvla_sc_m128_seed42_v2.log\", \"model_name\": \"openvla + VTC(M=128) + LoRA(r=16, q/v_proj)\", \"pid\": \"841334\", \"seed\": 42, \"server\": \"westd-27271\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-20T07:36:57.910Z\"}, \"analysis_xvla_token_importance\": {\"completed_at\": \"2026-05-20T04:37:07.968Z\", \"conclusion\": \"success\", \"created_at\": \"2026-05-20T04:33:25.537Z\", \"hypothesis\": \"X-VLA uses a linear projection connector (simpler than OpenVLA's 2-layer MLP), so its vision tokens may exhibit different compressibility patterns — potentially more uniform attention distribution and higher tolerance to pruning due to less non-linear feature mixing in the connector.\", \"retry_count\": 0, \"spec\": {\"account\": \"root\", \"backend\": \"tmux\", \"checkpoint_path\": \"N/A (analysis only)\", \"command\": \"python analyze_xvla_token_importance.py\", \"data_count\": 100, \"data_path\": \"LIBERO-Object (task_index 20-29)\", \"gpu\": [\"cuda:1\"], \"gpu_hours\": 0.04, \"log_path\": \"~/runs/importance_margin_vla_compress/analysis_xvla_token_importance.log\", \"model_name\": \"X-VLA-0.9B (lerobot/xvla-libero)\", \"pid\": \"74729\", \"seed\": 42, \"server\": \"westd-41074\", \"submitted_at\": \"2026-05-20T04:34:35.248Z\", \"submitted_via\": \"submit_training_job\", \"wall_clock_seconds\": 152.7}, \"status\": \"DONE\", \"updated_at\": \"2026-05-20T04:37:07.968Z\"}, \"train_openvla_sc_m96_vtconly_seed42\": {\"completed_at\": \"2026-05-20T03:22:41.682Z\", \"conclusion\": \"failed\", \"created_at\": \"2026-05-20T03:08:23.577Z\", \"extra\": {\"hook_events\": [{\"action\": \"agent\", \"event\": \"on_failed\", \"ts\": \"2026-05-20T03:22:49.214534+00:00\"}]}, \"failure_reason\": \"process dead 5× with no sentinel/W&B — auto-resolved as failed\", \"hypothesis\": \"OpenVLA VTC-only M=96 (256→96 tokens, 62.5% compression). M-sweep data point between M=128 and M=64. If M=96 SR falls between M=128 and M=64 SR, confirms graded degradation pattern for MLP-projector VTC re-encoding on OpenVLA.\", \"parent\": \"train_openvla_sc_m128_vtconly_seed42\", \"reproduce\": {\"finished_at\": \"2026-05-20T03:22:39.813Z\"}, \"retry_count\": 0, \"spec\": {\"checkpoint_source\": \"openvla/openvla-7b (HF pretrained)\", \"command\": \"python train_openvla_vtc.py --M 96 --seed 42\", \"data_count\": 500, \"data_path\": \"LIBERO-Object\", \"eval_data\": \"N/A (training experiment)\", \"gpu\": \"cuda:2\", \"model_name\": \"OpenVLA-7B\", \"pid\": 63701, \"seed\": 42, \"server\": \"westd-41074\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-20T03:23:31.112Z\"}, \"train_openvla_sc_m64_vtconly_seed42\": {\"completed_at\": \"2026-05-20T03:22:08.304Z\", \"conclusion\": \"failed\", \"created_at\": \"2026-05-20T03:08:25.152Z\", \"extra\": {\"hook_events\": [{\"action\": \"agent\", \"event\": \"on_failed\", \"ts\": \"2026-05-20T03:22:12.675001+00:00\"}]}, \"failure_reason\": \"process dead 5× with no sentinel/W&B — auto-resolved as failed\", \"hypothesis\": \"OpenVLA VTC-only M=64 (256→64 tokens, 75% compression). M-sweep data point between M=96 and M=32. If M=64 SR > M=32 SR, confirms monotonic degradation for MLP-projector VTC re-encoding at higher compression ratios on OpenVLA.\", \"parent\": \"train_openvla_sc_m128_vtconly_seed42\", \"reproduce\": {\"finished_at\": \"2026-05-20T03:22:06.323Z\"}, \"retry_count\": 0, \"spec\": {\"checkpoint_source\": \"openvla/openvla-7b (HF pretrained)\", \"command\": \"python train_openvla_vtc.py --M 64 --seed 42\", \"data_count\": 500, \"data_path\": \"LIBERO-Object\", \"eval_data\": \"N/A (training experiment)\", \"gpu\": \"cuda:3\", \"model_name\": \"OpenVLA-7B\", \"pid\": 63780, \"seed\": 42, \"server\": \"westd-41074\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-20T03:22:08.304Z\"}, \"train_c5_roboflamingo_v2\": {\"completed_at\": \"2026-05-20T00:54:21.836Z\", \"conclusion\": \"killed\", \"created_at\": \"2026-05-19T22:24:24.260Z\", \"hypothesis\": \"RoboFlamingo (Perceiver Resampler) fine-tuned on LIBERO-Object with fixed gripper loss (BCE instead of BCE_with_logits, weight 0.1). Establishes 3rd connector architecture baseline for compression analysis (C5). Bug M029 fix: previous version had double sigmoid causing gripper to not learn.\", \"parent\": \"train_c5_roboflamingo_libero_object\", \"retry_count\": 0, \"spec\": {\"checkpoint_path\": \"/root/autodl-tmp/checkpoints/roboflamingo_libero_c5_v2\", \"checkpoint_source\": \"OpenFlamingo-3B-vitl-mpt1b-langinstruct (from scratch, no resume)\", \"command\": \"CUDA_VISIBLE_DEVICES=1 MUJOCO_GL=egl python -u train_libero.py --suite libero_object --data_dir /root/autodl-tmp/libero_data/datasets/libero_object --num_epochs 50 --batch_size 8 --lr 1e-4 --window_size 12 --gpu 0 --save_dir /root/autodl-tmp/checkpoints/roboflamingo_libero_c5_v2\", \"data_count\": 500, \"data_path\": \"/root/autodl-tmp/libero_data/datasets/libero_object\", \"eval_data\": \"N/A (training)\", \"log_path\": \"/root/autodl-tmp/importance_margin_vla_compress/logs/train_c5_roboflamingo_v2.log\", \"model_name\": \"RoboFlamingo (OpenFlamingo-3B-vitl-mpt1b) + BCE fix\", \"seed\": 42, \"server\": \"westd-41074\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-20T00:54:21.836Z\"}, \"train_c5_roboflamingo_libero_object\": {\"completed_at\": \"2026-05-19T22:20:17.389Z\", \"conclusion\": \"killed\", \"created_at\": \"2026-05-19T21:33:38.468Z\", \"hypothesis\": \"RoboFlamingo (Perceiver Resampler, 64 queries) fine-tuned on LIBERO-Object (500 eps, 10 tasks) will achieve competitive baseline SR, establishing the 3rd connector architecture for compression analysis (C5). Perceiver's global cross-attention summary tokens should show a different degradation pattern than pixel-shuffle (cliff-edge) and MLP (graded).\", \"retry_count\": 0, \"spec\": {\"checkpoint_path\": \"/root/autodl-tmp/checkpoints/roboflamingo_libero_c5\", \"command\": \"CUDA_VISIBLE_DEVICES=1 MUJOCO_GL=egl python -u train_libero.py --suite libero_object --data_dir /root/autodl-tmp/libero_data/datasets/libero_object --num_epochs 50 --batch_size 8 --lr 1e-4 --window_size 12 --gpu 0 --save_dir /root/autodl-tmp/checkpoints/roboflamingo_libero_c5\", \"data_count\": 500, \"data_path\": \"/root/autodl-tmp/libero_data/datasets/libero_object\", \"log_path\": \"/root/autodl-tmp/importance_margin_vla_compress/logs/train_c5_roboflamingo_gpu1.log\", \"model_name\": \"RoboFlamingo (OpenFlamingo-3B-vitl-mpt1b)\", \"seed\": 42, \"server\": \"westd-41074\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-19T22:20:17.389Z\"}, \"train_openvla_sc_m128_lora_seed42\": {\"completed_at\": \"2026-05-19T18:45:56.133Z\", \"conclusion\": \"killed\", \"created_at\": \"2026-05-19T18:02:50.161Z\", \"extra\": {\"previous_failure\": {\"conclusion\": \"killed\"}}, \"hypothesis\": \"OpenVLA VTC re-encoding (M=128) + LoRA fine-tuning (r=16, q_proj/v_proj) allows LLM backbone to adapt to compressed token representations. If VTC+LoRA > VTC-only on OpenVLA, backbone adaptation is complementary to re-encoding for MLP-projector architectures, maximizing compression recovery.\", \"retry_count\": 1, \"spec\": {\"checkpoint_path\": \"/root/autodl-tmp/importance_margin_vla_compress/checkpoints/openvla_sc_m128_lora/\", \"command\": \"CUDA_VISIBLE_DEVICES=1 python train_openvla_smart_compress_lora.py --config configs/openvla_smart_compress_m128_lora.yaml\", \"data_count\": 273465, \"data_path\": \"HuggingFaceVLA/libero\", \"log_path\": \"/root/autodl-tmp/importance_margin_vla_compress/logs/train_openvla_sc_m128_lora_seed42.log\", \"model_name\": \"openvla + VTC(M=128) + LoRA(r=16)\", \"seed\": 42, \"server\": \"westd-41074\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-19T22:13:57.055Z\"}, \"eval_smart_compress_m32_seed44\": {\"completed_at\": \"2026-05-19T10:06:32.856Z\", \"conclusion\": \"success\", \"created_at\": \"2026-05-19T08:15:54.669Z\", \"hypothesis\": \"Third seed (seed=44) for Smart Compress M=32 (87.5% compression). Completes 3-seed data for M=32 point on M-curve.\", \"metrics\": {\"ci_95_lower\": 55.2, \"ci_95_upper\": 63.8, \"n_episodes\": 500, \"seed\": 44, \"success_rate\": 59.6}, \"parent\": \"train_smart_compress_m32_seed44\", \"retry_count\": 0, \"spec\": {\"account\": \"root\", \"backend\": \"tmux\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/importance_margin_vla_compress && python eval_smart_compress_libero.py --n_queries 32 --checkpoint_path checkpoints/smart_compress_m32_seed44/checkpoint.pt --suite libero_object --num_episodes 500 --gpu 0 --seed 44\\\"\", \"gpu\": [\"cuda:3\"], \"log_path\": \"~/runs/importance_margin_vla_compress/eval_smart_compress_m32_seed44.log\", \"pid\": \"685410\", \"server\": \"cqa1-33015\", \"submitted_at\": \"2026-05-19T20:05:46.665Z\", \"submitted_via\": \"submit_training_job\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-19T22:12:01.611Z\"}, \"eval_smart_compress_m96_seed44\": {\"completed_at\": \"2026-05-19T10:06:35.586Z\", \"conclusion\": \"success\", \"created_at\": \"2026-05-19T08:15:57.478Z\", \"hypothesis\": \"Third seed (seed=44) for Smart Compress M=96 (62.5% compression). Completes 3-seed data for M=96 point on M-curve. Prior seeds showed M=96 dip (p=0.034 vs M=64).\", \"metrics\": {\"ci_95_lower\": 48.4, \"ci_95_upper\": 57.1, \"n_episodes\": 500, \"seed\": 44, \"success_rate\": 52.8}, \"parent\": \"train_smart_compress_m96_seed44\", \"retry_count\": 0, \"spec\": {\"checkpoint_path\": \"checkpoints/smart_compress_m96_seed44/checkpoint.pt\", \"checkpoint_source\": \"/root/autodl-tmp/importance_margin_vla_compress/checkpoints/smart_compress_m96_seed44/checkpoint.pt\", \"command\": \"CUDA_VISIBLE_DEVICES=2 python eval_smart_compress_libero.py --n_queries 96 --checkpoint_path checkpoints/smart_compress_m96_seed44/checkpoint.pt --suite libero_object --num_episodes 500 --gpu 0 --seed 44\", \"data_count\": 500, \"data_path\": \"libero_object\", \"eval_data\": \"libero_object (500 episodes)\", \"gpu_ids\": [\"cuda:2\"], \"log_path\": \"/root/autodl-tmp/importance_margin_vla_compress/logs/eval_smart_compress_m96_seed44.log\", \"model_name\": \"smolvla_base + VisionTokenCompressor(M=96)\", \"pid\": 764777, \"seed\": 44, \"server\": \"cqa1-33015\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-19T22:11:59.550Z\"}, \"eval_smart_compress_m64_seed44\": {\"completed_at\": \"2026-05-19T10:06:34.336Z\", \"conclusion\": \"success\", \"created_at\": \"2026-05-19T08:15:56.060Z\", \"hypothesis\": \"Third seed (seed=44) for Smart Compress M=64 (75% compression). Completes 3-seed data for M=64 point on M-curve.\", \"metrics\": {\"ci_95_lower\": 60.1, \"ci_95_upper\": 68.5, \"n_episodes\": 500, \"seed\": 44, \"success_rate\": 64.4}, \"parent\": \"train_smart_compress_m64_seed44\", \"retry_count\": 0, \"spec\": {\"checkpoint_path\": \"checkpoints/smart_compress_m64_seed44/checkpoint.pt\", \"checkpoint_source\": \"/root/autodl-tmp/importance_margin_vla_compress/checkpoints/smart_compress_m64_seed44/checkpoint.pt\", \"command\": \"CUDA_VISIBLE_DEVICES=1 python eval_smart_compress_libero.py --n_queries 64 --checkpoint_path checkpoints/smart_compress_m64_seed44/checkpoint.pt --suite libero_object --num_episodes 500 --gpu 0 --seed 44\", \"data_count\": 500, \"data_path\": \"libero_object\", \"eval_data\": \"libero_object (500 episodes)\", \"gpu_ids\": [\"cuda:1\"], \"log_path\": \"/root/autodl-tmp/importance_margin_vla_compress/logs/eval_smart_compress_m64_seed44.log\", \"model_name\": \"smolvla_base + VisionTokenCompressor(M=64)\", \"pid\": 763351, \"seed\": 44, \"server\": \"cqa1-33015\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-19T22:11:57.673Z\"}, \"eval_openvla_random_pruning_sweep\": {\"completed_at\": \"2026-05-19T21:31:54.881Z\", \"conclusion\": \"success\", \"created_at\": \"2026-05-19T21:31:36.150Z\", \"hypothesis\": \"OpenVLA (MLP projector) shows graded degradation under random pruning across k=0.30-0.95, confirming C3 claim that MLP projector architecture allows graceful compression unlike pixel-shuffle's cliff-edge.\", \"metrics\": {\"k0.30_sr\": 20.6, \"k0.50_sr\": 37.4, \"k0.70_sr\": 49, \"k0.90_sr\": 62, \"k0.95_sr\": 69.4, \"k1.0_sr\": 74, \"n_episodes\": 500, \"seed\": 7, \"suite\": \"libero_object\"}, \"retry_count\": 0, \"spec\": {\"checkpoint_path\": \"N/A (eval only)\", \"command\": \"python eval_success_rate_libero.py --mode random --keep_ratio {k} --suite libero_object --num_episodes 500 --seed 7\", \"data_count\": 500, \"data_path\": \"libero_object\", \"log_path\": \"/root/autodl-tmp/importance_margin_vla_compress/eval_results/openvla_random_prune_k*_object.json\", \"model_name\": \"openvla-7b\", \"seed\": 7, \"server\": \"westd-27271\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-19T21:31:54.881Z\"}, \"train_openvla_sc_m128_seed42\": {\"completed_at\": \"2026-05-19T18:26:21.388Z\", \"conclusion\": \"failed\", \"created_at\": \"2026-05-19T17:05:34.873Z\", \"failure_reason\": \"httpx.ConnectError: Network is unreachable on westd-41074\", \"hypothesis\": \"OpenVLA (MLP-projector, baseline 74% SR) + VTC cross-attention re-encoding (256→128 tokens, 50% compression). If VTC re-encoding significantly outperforms k=0.5 random pruning (37.4% SR) on OpenVLA, demonstrates learned re-encoding generalizes from pixel-shuffle (SmolVLA) to MLP-projector architecture, establishing C4-ext method universality.\", \"retry_count\": 0, \"spec\": {\"account\": \"root\", \"backend\": \"tmux\", \"command\": \"bash -c \\\"source /etc/network_turbo; export REQUESTS_CA_BUNDLE=/etc/ssl/certs/ca-certificates.crt; export SSL_CERT_FILE=/etc/ssl/certs/ca-certificates.crt; export HF_HOME=/root/autodl-tmp/.hf_cache; export HF_HUB_DISABLE_XET=1; export WANDB_MODE=disabled; export CUDA_VISIBLE_DEVICES=0; source /root/miniconda3/etc/profile.d/conda.sh && conda activate base; cd /root/autodl-tmp/importance_margin_vla_compress; python train_openvla_smart_compress.py --config configs/openvla_smart_compress_m128.yaml\\\"\", \"gpu\": [\"cuda:0\"], \"log_path\": \"~/runs/importance_margin_vla_compress/train_openvla_sc_m128_seed42.log\", \"pid\": \"26109\", \"server\": \"westd-41074\", \"submitted_at\": \"2026-05-19T18:33:25.872Z\", \"submitted_via\": \"submit_training_job\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-19T18:33:26.246Z\"}, \"train_smart_compress_m16_seed44_v2\": {\"completed_at\": \"2026-05-19T16:18:02.986Z\", \"conclusion\": \"failed\", \"created_at\": \"2026-05-19T15:22:09.291Z\", \"hypothesis\": \"Retry of train_smart_compress_m16_seed44 (failed due to server restart, not OOM). Third seed (seed=44) for Smart Compress M=16 (87.5% compression). Prior: seed42=55.8%. Completes 3-seed data for extreme compression point on M-curve.\", \"metrics\": {\"failure_reason\": \"Disk full on /root/autodl-tmp/ (250G/250G, 100% used, 4MB free). Training ran normally to step=1000 (loss 5.0→0.2), but torch.save() failed at first checkpoint save with PytorchStreamWriter write error. Checkpoints dir already 112GB from prior experiments — needs cleanup before retry. Partial checkpoint.pt (228MB) likely corrupted.\", \"last_loss\": 0.207, \"last_step\": 1000, \"steps_per_second\": 3.8}, \"retry_count\": 0, \"spec\": {\"account\": \"root\", \"backend\": \"tmux\", \"checkpoint_path\": \"checkpoints/smart_compress_m16_seed44/checkpoint.pt\", \"checkpoint_source\": \"smolvla_base\", \"command\": \"python -u train_smart_compress.py --config configs/smart_compress_m16_seed44.yaml --wandb_run smart_compress_m16_seed44_v2 --seed 44 --gpu 0\", \"data_count\": \"all\", \"data_path\": \"HuggingFaceVLA/libero\", \"gpu\": \"cuda:3\", \"gpu_hours\": 0.9, \"log_path\": \"~/runs/importance_margin_vla_compress/train_smart_compress_m16_seed44_v2.log\", \"model_name\": \"smolvla_base + VisionTokenCompressor(M=16)\", \"pid\": \"650986\", \"seed\": 44, \"server\": \"cqa1-33015\", \"submitted_at\": \"2026-05-19T15:23:45.676Z\", \"submitted_via\": \"submit_training_job\", \"wall_clock_seconds\": 3257.3}, \"status\": \"DONE\", \"updated_at\": \"2026-05-19T16:21:36.107Z\"}, \"eval_official_smolvla_prune_k05_spatial_v2\": {\"completed_at\": \"2026-05-19T16:17:38.764Z\", \"conclusion\": \"success\", \"created_at\": \"2026-05-19T14:36:27.695Z\", \"hypothesis\": \"Official SmolVLA checkpoint (SR=43.8% on Spatial baseline) with k=0.5 random token pruning on LIBERO-Spatial. Retry of eval_official_smolvla_prune_k05_spatial (failed due to missing HF env vars). If 0% SR (matching LoRA-FT k=0.5 spatial=0% and official k=0.5 Object=0%), confirms pixel-shuffle cliff-edge is universal across all checkpoint variants and task suites (C2).\", \"metrics\": {\"note\": \"cliff-edge confirmed on Spatial suite, 0.6% SR with k=0.5 random pruning\", \"overall_success_rate\": 0.006, \"total_episodes\": 500, \"total_successes\": 3}, \"parent\": \"eval_smolvla_prune_k05_spatial_v2\", \"retry_count\": 0, \"spec\": {\"account\": \"root\", \"backend\": \"tmux\", \"checkpoint_path\": \"/root/autodl-tmp/.hf_cache/smolvla_libero_official\", \"checkpoint_source\": \"/root/autodl-tmp/.hf_cache/smolvla_libero_official\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/importance_margin_vla_compress && CUDA_VISIBLE_DEVICES=0 HF_HOME=/root/autodl-tmp/.hf_cache HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 MUJOCO_GL=egl python -u eval_official_libero.py --pretrained_dir /root/autodl-tmp/.hf_cache/smolvla_libero_official --suite libero_spatial --num_episodes 50 --gpu 0 --mode random_prune --k_ratio 0.5 --seed 42\\\"\", \"data_count\": 500, \"data_path\": \"libero_spatial\", \"eval_data\": \"LIBERO-Spatial (10 tasks x 50 episodes)\", \"gpu\": \"cuda:0\", \"gpu_hours\": 1.68, \"log_path\": \"~/runs/importance_margin_vla_compress/eval_official_smolvla_prune_k05_spatial_v2.log\", \"model_name\": \"SmolVLA official + k=0.5 random pruning\", \"pid\": 620540, \"seed\": 42, \"server\": \"cqa1-33015\", \"submitted_at\": \"2026-05-19T14:36:39.750Z\", \"submitted_via\": \"submit_training_job\", \"wall_clock_seconds\": 6059.0}, \"status\": \"DONE\", \"updated_at\": \"2026-05-19T16:21:18.728Z\"}, \"eval_smart_compress_m96_seed44_v2\": {\"completed_at\": \"2026-05-19T11:05:25.610Z\", \"conclusion\": \"success\", \"created_at\": \"2026-05-19T10:06:47.264Z\", \"hypothesis\": \"Eval of M=96 seed44 checkpoint on LIBERO-Object (50 eps/task). Prior M=96 seeds: seed42=52.6%, seed43=58.2%. High variance (5.6pp) makes third seed critical for M=96 stability. Parent: train_smart_compress_m96_seed44 (ANALYZING, training complete).\", \"metrics\": {\"overall_success_rate\": 0.528, \"total_episodes\": 500, \"total_successes\": 264, \"wilson_ci_95\": [0.4842, 0.5714]}, \"parent\": \"train_smart_compress_m96_seed44\", \"retry_count\": 0, \"spec\": {\"checkpoint_path\": \"checkpoints/smart_compress_m96_seed44/checkpoint.pt\", \"checkpoint_source\": \"checkpoints/smart_compress_m96_seed44/checkpoint.pt\", \"command\": \"CUDA_VISIBLE_DEVICES=2 python eval_smart_compress_libero.py --n_queries 96 --checkpoint_path checkpoints/smart_compress_m96_seed44/checkpoint.pt --suite libero_object --num_episodes 50 --gpu 0 --seed 44\", \"data_count\": 50, \"data_path\": \"libero_object\", \"eval_data\": \"libero_object (50 episodes/task)\", \"gpu_ids\": [\"cuda:2\"], \"log_path\": \"/root/autodl-tmp/importance_margin_vla_compress/logs/eval_smart_compress_m96_seed44.log\", \"model_name\": \"smolvla_base + VisionTokenCompressor(M=96)\", \"pid\": 164042, \"seed\": 44, \"server\": \"cqa1-33015\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-19T16:19:52.674Z\"}, \"eval_smart_compress_m64_seed44_v2\": {\"completed_at\": \"2026-05-19T11:05:24.691Z\", \"conclusion\": \"success\", \"created_at\": \"2026-05-19T10:06:46.094Z\", \"hypothesis\": \"Eval of M=64 seed44 checkpoint on LIBERO-Object (50 eps/task). Prior M=64 seeds: seed42=61.6%, seed43=60.0%. Third seed completes 3-seed mean±std for M=64 point on M-curve. Parent: train_smart_compress_m64_seed44 (ANALYZING, training complete).\", \"metrics\": {\"overall_success_rate\": 0.644, \"total_episodes\": 500, \"total_successes\": 322, \"wilson_ci_95\": [0.6011, 0.6847]}, \"parent\": \"train_smart_compress_m64_seed44\", \"retry_count\": 0, \"spec\": {\"checkpoint_path\": \"checkpoints/smart_compress_m64_seed44/checkpoint.pt\", \"checkpoint_source\": \"checkpoints/smart_compress_m64_seed44/checkpoint.pt\", \"command\": \"CUDA_VISIBLE_DEVICES=1 python eval_smart_compress_libero.py --n_queries 64 --checkpoint_path checkpoints/smart_compress_m64_seed44/checkpoint.pt --suite libero_object --num_episodes 50 --gpu 0 --seed 44\", \"data_count\": 50, \"data_path\": \"libero_object\", \"eval_data\": \"libero_object (50 episodes/task)\", \"gpu_ids\": [\"cuda:1\"], \"log_path\": \"/root/autodl-tmp/importance_margin_vla_compress/logs/eval_smart_compress_m64_seed44.log\", \"model_name\": \"smolvla_base + VisionTokenCompressor(M=64)\", \"pid\": 162254, \"seed\": 44, \"server\": \"cqa1-33015\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-19T16:19:50.885Z\"}, \"eval_smart_compress_m32_seed44_v2\": {\"completed_at\": \"2026-05-19T11:05:23.746Z\", \"conclusion\": \"success\", \"created_at\": \"2026-05-19T10:06:45.543Z\", \"hypothesis\": \"Eval of M=32 seed44 checkpoint on LIBERO-Object (50 eps/task). Prior M=32 seeds: seed42=61.6%, seed43=59.2%. Third seed completes 3-seed mean±std for core compression point on M-curve. Parent: train_smart_compress_m32_seed44 (ANALYZING, training complete).\", \"metrics\": {\"overall_success_rate\": 0.596, \"total_episodes\": 500, \"total_successes\": 298, \"wilson_ci_95\": [0.5524, 0.6381]}, \"parent\": \"train_smart_compress_m32_seed44\", \"retry_count\": 0, \"spec\": {\"checkpoint_path\": \"checkpoints/smart_compress_m32_seed44/checkpoint.pt\", \"checkpoint_source\": \"checkpoints/smart_compress_m32_seed44/checkpoint.pt\", \"command\": \"CUDA_VISIBLE_DEVICES=0 python eval_smart_compress_libero.py --n_queries 32 --checkpoint_path checkpoints/smart_compress_m32_seed44/checkpoint.pt --suite libero_object --num_episodes 50 --gpu 0 --seed 44\", \"data_count\": 50, \"data_path\": \"libero_object\", \"eval_data\": \"libero_object (50 episodes/task)\", \"gpu_ids\": [\"cuda:0\"], \"log_path\": \"/root/autodl-tmp/importance_margin_vla_compress/logs/eval_smart_compress_m32_seed44.log\", \"model_name\": \"smolvla_base + VisionTokenCompressor(M=32)\", \"pid\": 160877, \"seed\": 44, \"server\": \"cqa1-33015\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-19T16:19:49.468Z\"}, \"eval_mlp_adapter_seed44\": {\"completed_at\": \"2026-05-19T14:35:44.713Z\", \"conclusion\": \"negative\", \"created_at\": \"2026-05-19T13:06:52.554Z\", \"hypothesis\": \"MLP adapter control seed=44 eval on LIBERO-Object (50 eps/task). Prior seed42=65.2%. Multi-seed parity with cross-attention 3-seed (61.2±1.4%) required by Reviewer. Third seed completes 3-seed mean±std for MLP adapter.\", \"metrics\": {\"overall_success_rate\": 0.604, \"per_task_sr\": {\"0_alphabet_soup\": 0.54, \"1_cream_cheese\": 0.68, \"2_salad_dressing\": 0.58, \"3_bbq_sauce\": 0.5, \"4_ketchup\": 0.8, \"5_tomato_sauce\": 0.58, \"6_butter\": 0.82, \"7_milk\": 0.58, \"8_chocolate_pudding\": 0.54, \"9_orange_juice\": 0.42}, \"suite\": \"libero_object\", \"total_episodes\": 500, \"total_successes\": 302, \"wilson_ci_95\": [0.5605, 0.6459]}, \"parent\": \"eval_mlp_adapter_control\", \"reproduce\": {\"finished_at\": \"2026-05-19T14:33:42.430Z\"}, \"retry_count\": 0, \"spec\": {\"checkpoint_path\": \"checkpoints/mlp_adapter_control/checkpoint.pt\", \"checkpoint_source\": \"checkpoints/mlp_adapter_control/checkpoint.pt\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/importance_margin_vla_compress && CUDA_VISIBLE_DEVICES=0 MUJOCO_GL=egl HF_HOME=/root/autodl-tmp/.hf_cache HF_HUB_OFFLINE=1 python -u eval_smart_compress_libero.py --n_queries 32 --checkpoint_path checkpoints/mlp_adapter_control/checkpoint.pt --suite libero_object --num_episodes 50 --gpu 0 --seed 44 --output eval_results/eval_mlp_adapter_seed44.json\\\"\", \"data_count\": 500, \"data_path\": \"libero_object\", \"eval_data\": \"libero_object (10 tasks x 50 episodes)\", \"gpu\": \"cuda:0\", \"log_path\": \"eval_results/eval_mlp_adapter_seed44.json\", \"model_name\": \"SmolVLA + MLP adapter control (avg-pool, ~22M params)\", \"pid\": 731452, \"seed\": 44, \"server\": \"westd-27271\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-19T14:35:44.713Z\"}, \"eval_official_smolvla_prune_k05_spatial\": {\"completed_at\": \"2026-05-19T14:33:46.893Z\", \"conclusion\": \"failed\", \"created_at\": \"2026-05-19T14:21:42.301Z\", \"failure_reason\": \"EXIT_CODE=1 (generic error — check log tail)\", \"hypothesis\": \"Official SmolVLA checkpoint (SR=43.8% on Spatial baseline) with k=0.5 random token pruning on LIBERO-Spatial. If 0% SR (matching LoRA-FT k=0.5 spatial=0% and official k=0.5 Object=0%), confirms pixel-shuffle cliff-edge is universal across checkpoint variants AND task suites — completing the \\\"all SmolVLA variants × all suites = cliff-edge\\\" claim (C2).\", \"parent\": \"eval_smolvla_prune_k05_spatial_v2\", \"retry_count\": 0, \"spec\": {\"account\": \"root\", \"backend\": \"tmux\", \"checkpoint_path\": \"N/A (eval only)\", \"checkpoint_source\": \"/root/autodl-tmp/.hf_cache/smolvla_libero_official\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/importance_margin_vla_compress && CUDA_VISIBLE_DEVICES=0 python -u eval_official_libero.py --pretrained_dir /root/autodl-tmp/.hf_cache/smolvla_libero_official --suite libero_spatial --num_episodes 50 --gpu 0 --mode random_prune --k_ratio 0.5 --seed 42\\\"\", \"data_count\": 500, \"data_path\": \"libero_spatial\", \"eval_data\": \"LIBERO-Spatial (10 tasks x 50 episodes)\", \"gpu\": \"cuda:0\", \"gpu_hours\": 0.19, \"log_path\": \"~/runs/importance_margin_vla_compress/eval_official_smolvla_prune_k05_spatial.log\", \"model_name\": \"SmolVLA official + k=0.5 random pruning\", \"pid\": 619830, \"seed\": 42, \"server\": \"cqa1-33015\", \"submitted_at\": \"2026-05-19T14:22:23.073Z\", \"submitted_via\": \"submit_training_job\", \"wall_clock_seconds\": 683.8}, \"status\": \"DONE\", \"updated_at\": \"2026-05-19T14:33:46.893Z\"}, \"eval_smolvla_official_baseline_spatial_v2\": {\"completed_at\": \"2026-05-19T14:15:25.202Z\", \"conclusion\": \"success\", \"created_at\": \"2026-05-19T13:05:32.615Z\", \"hypothesis\": \"Official SmolVLA checkpoint (LIBERO-Object baseline SR=59.2%) eval on LIBERO-Spatial. Continuation of eval_smolvla_official_baseline_spatial (mistakenly marked failed during server restart). PID 537882 on cqa1 cuda:1, Task 0 ep 35/50 at time of recovery.\", \"metrics\": {\"overall_success_rate\": 0.438, \"per_task_sr\": {\"task_0\": 0.54, \"task_1\": 0.48, \"task_2\": 0.08, \"task_3\": 0.76, \"task_4\": 0.38, \"task_5\": 0.2, \"task_6\": 0.34, \"task_7\": 0.78, \"task_8\": 0.48, \"task_9\": 0.34}, \"total_episodes\": 500, \"total_successes\": 219, \"wilson_ci_95\": [0.3951, 0.4818]}, \"retry_count\": 0, \"spec\": {\"checkpoint_path\": \"/root/autodl-tmp/.hf_cache/smolvla_libero_official\", \"checkpoint_source\": \"/root/autodl-tmp/.hf_cache/smolvla_libero_official\", \"command\": \"CUDA_VISIBLE_DEVICES=1 python -u eval_official_libero.py --pretrained_dir /root/autodl-tmp/.hf_cache/smolvla_libero_official --suite libero_spatial --num_episodes 50 --gpu 0 --mode baseline --seed 42\", \"data_count\": 500, \"data_path\": \"libero_spatial\", \"eval_data\": \"LIBERO-Spatial (10 tasks x 50 episodes)\", \"gpu_ids\": [\"cuda:1\"], \"log_path\": \"~/runs/importance_margin_vla_compress/eval_smolvla_official_baseline_spatial.log\", \"model_name\": \"SmolVLA official\", \"pid\": 537882, \"seed\": 42, \"server\": \"cqa1-33015\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-19T14:15:31.519Z\"}, \"eval_mlp_adapter_seed43\": {\"completed_at\": \"2026-05-19T13:47:59.209Z\", \"conclusion\": \"negative\", \"created_at\": \"2026-05-19T13:06:49.591Z\", \"hypothesis\": \"MLP adapter control seed=43 eval on LIBERO-Object (50 eps/task). Prior seed42=65.2%. Multi-seed parity with cross-attention 3-seed (61.2±1.4%) required by Reviewer. If seed43 yields ~60-65%, confirms MLP adapter result is robust.\", \"metrics\": {\"overall_success_rate\": 0.646, \"per_task_sr\": {\"task0_alphabet_soup\": 0.74, \"task1_cream_cheese\": 0.74, \"task2_salad_dressing\": 0.66, \"task3_bbq_sauce\": 0.44, \"task4_ketchup\": 0.56, \"task5_tomato_sauce\": 0.64, \"task6_butter\": 0.86, \"task7_milk\": 0.58, \"task8_chocolate_pudding\": 0.72, \"task9_orange_juice\": 0.52}, \"suite\": \"libero_object\", \"total_episodes\": 500, \"total_successes\": 323, \"wilson_ci_95\": [0.603, 0.687]}, \"parent\": \"eval_mlp_adapter_control\", \"retry_count\": 0, \"spec\": {\"checkpoint_path\": \"checkpoints/mlp_adapter_control/checkpoint.pt\", \"checkpoint_source\": \"checkpoints/mlp_adapter_control/checkpoint.pt\", \"command\": \"CUDA_VISIBLE_DEVICES=0 MUJOCO_GL=egl HF_HOME=/root/autodl-tmp/.hf_cache HF_HUB_OFFLINE=1 python -u eval_smart_compress_libero.py --n_queries 32 --checkpoint_path checkpoints/mlp_adapter_control/checkpoint.pt --suite libero_object --num_episodes 50 --gpu 0 --seed 43 --output eval_results/eval_mlp_adapter_seed43.json\", \"data_count\": 500, \"data_path\": \"libero_object\", \"eval_data\": \"libero_object (10 tasks x 50 episodes)\", \"gpu\": \"cuda:0\", \"log_path\": \"eval_results/eval_mlp_adapter_seed43.log\", \"model_name\": \"SmolVLA + MLP adapter control (avg-pool, ~22M params)\", \"pid\": 651149, \"seed\": 43, \"server\": \"westd-27271\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-19T13:47:59.209Z\"}, \"eval_mlp_adapter_control\": {\"completed_at\": \"2026-05-19T12:44:36.770Z\", \"conclusion\": \"negative\", \"created_at\": \"2026-05-19T12:00:15.803Z\", \"failure_reason\": \"startup recovery: RUNNING with no cron and no server/pid info\", \"hypothesis\": \"MLP+average-pooling compressor (no cross-attention, matched ~22M params) will achieve significantly lower success rate than VisionTokenCompressor (cross-attention) at M=32 on LIBERO-Object, proving that cross-attention re-encoding mechanism is critical for effective vision token compression, not merely parameter capacity.\", \"metrics\": {\"overall_success_rate\": 0.652, \"per_task_sr\": {\"task0_alphabet_soup\": 0.58, \"task1_cream_cheese\": 0.74, \"task2_salad_dressing\": 0.72, \"task3_bbq_sauce\": 0.56, \"task4_ketchup\": 0.76, \"task5_tomato_sauce\": 0.68, \"task6_butter\": 0.8, \"task7_milk\": 0.62, \"task8_chocolate_pudding\": 0.52, \"task9_orange_juice\": 0.54}, \"suite\": \"libero_object\", \"total_episodes\": 500, \"total_successes\": 326, \"wilson_ci_95\": [0.6092, 0.6925]}, \"parent\": \"train_mlp_adapter_control\", \"retry_count\": 0, \"spec\": {\"checkpoint_path\": \"checkpoints/mlp_adapter_control/checkpoint.pt\", \"checkpoint_source\": \"checkpoints/mlp_adapter_control/checkpoint.pt\", \"command\": \"CUDA_VISIBLE_DEVICES=0 MUJOCO_GL=egl HF_HOME=/root/autodl-tmp/.hf_cache HF_HUB_OFFLINE=1 python -u eval_smart_compress_libero.py --n_queries 32 --checkpoint_path checkpoints/mlp_adapter_control/checkpoint.pt --suite libero_object --num_episodes 50 --gpu 0 --seed 42 --output eval_results/eval_mlp_adapter_control.json\", \"data_count\": 500, \"data_path\": \"LIBERO-Object (10 tasks x 50 episodes)\", \"eval_data\": \"libero_object\", \"log_path\": \"logs/eval_mlp_adapter_control.log\", \"model_name\": \"smolvla_base + MLPCompressor(22.14M params, M=32)\", \"seed\": 42, \"server\": \"westd-27271\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-19T13:36:50.011Z\"}, \"eval_smolvla_prune_k05_spatial_v2\": {\"completed_at\": \"2026-05-19T13:19:02.593Z\", \"conclusion\": \"success\", \"created_at\": \"2026-05-19T13:05:34.351Z\", \"hypothesis\": \"SmolVLA k=0.5 random token pruning on LIBERO-Spatial. Continuation of eval_smolvla_prune_k05_spatial (mistakenly marked failed during server restart). PID 458637 on cqa1 cuda:2, Task 8-9 in progress at time of recovery. Expected 0% SR.\", \"metrics\": {\"episodes_per_task\": 50, \"k_ratio\": 0.5, \"num_tasks\": 10, \"overall_success_rate\": 0, \"per_task_sr\": {\"T0\": 0, \"T1\": 0, \"T2\": 0, \"T3\": 0, \"T4\": 0, \"T5\": 0, \"T6\": 0, \"T7\": 0, \"T8\": 0, \"T9\": 0}, \"pruning_method\": \"true_removal\", \"tokens_kept\": 64, \"tokens_removed\": 64, \"total_episodes\": 500, \"total_successes\": 0, \"wilson_ci_95\": [0, 0.0076]}, \"retry_count\": 0, \"spec\": {\"checkpoint_path\": \"/root/autodl-tmp/importance_margin_vla_compress/checkpoints/libero_full_ft/step_099999/checkpoint.pt\", \"command\": \"CUDA_VISIBLE_DEVICES=2 python -u eval_random_prune_smolvla_spatial.py --k_ratio 0.5 --episodes_per_task 50 --seed 42\", \"data_count\": 500, \"data_path\": \"libero_spatial\", \"eval_data\": \"LIBERO-Spatial (10 tasks x 50 episodes)\", \"gpu_ids\": [\"cuda:2\"], \"log_path\": \"/root/autodl-tmp/importance_margin_vla_compress/eval_results/eval_prune_k05_spatial.log\", \"model_name\": \"SmolVLA + k=0.5 random pruning\", \"pid\": 458637, \"seed\": 42, \"server\": \"cqa1-33015\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-19T13:19:09.320Z\"}, \"eval_smolvla_baseline_spatial\": {\"completed_at\": \"2026-05-19T13:05:29.450Z\", \"conclusion\": \"success\", \"created_at\": \"2026-05-19T11:11:07.968Z\", \"hypothesis\": \"SmolVLA baseline (no compression, no Smart Compress) eval on LIBERO-Spatial. SmolVLA uses pixel-shuffle connector which creates entangled tokens. Cross-suite eval provides reference point for compression impact on spatial reasoning tasks. Combined with OpenVLA Spatial baseline, tests MF-3 (architecture-dependent compressibility across task suites).\", \"metrics\": {\"overall_success_rate\": 0.062, \"total_episodes\": 500, \"total_successes\": 31}, \"retry_count\": 0, \"spec\": {\"account\": \"root\", \"backend\": \"tmux\", \"checkpoint_path\": \"N/A (eval only)\", \"checkpoint_source\": \"checkpoints/libero_baseline/latest/checkpoint.pt\", \"command\": \"CUDA_VISIBLE_DEVICES=0 MUJOCO_GL=egl HF_HOME=/root/autodl-tmp/.hf_cache HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 python -u eval_success_rate_libero.py --checkpoint checkpoints/libero_baseline/latest/checkpoint.pt --config configs/libero_baseline.yaml --suite libero_spatial --num_episodes 50 --gpu 0 --seed 42 --mode baseline --output eval_results/eval_smolvla_baseline_spatial.json\", \"data_count\": 500, \"data_path\": \"liber
```

---

### Large event (continued)

````text
o_spatial\", \"eval_data\": \"LIBERO-Spatial (10 tasks x 50 episodes)\", \"gpu\": \"cuda:0\", \"log_path\": \"~/runs/importance_margin_vla_compress/eval_smolvla_baseline_spatial.log\", \"model_name\": \"smolvla_baseline (LoRA fine-tuned, no compression)\", \"pid\": 439389, \"seed\": 42, \"server\": \"cqa1-33015\", \"submitted_at\": \"2026-05-19T19:13:09Z\", \"submitted_via\": \"tmux\", \"tmux_session\": \"eval_smolvla_baseline_spatial\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-19T13:05:29.450Z\"}, \"eval_smolvla_official_baseline_spatial\": {\"completed_at\": \"2026-05-19T12:44:38.701Z\", \"conclusion\": \"failed\", \"created_at\": \"2026-05-19T12:34:16.522Z\", \"failure_reason\": \"startup recovery: RUNNING with no cron and no server/pid info\", \"hypothesis\": \"Official SmolVLA checkpoint (HuggingFaceVLA/smolvla_libero, LIBERO-Object baseline SR=59.2%) eval on LIBERO-Spatial. Provides cross-suite baseline data for the official checkpoint. Combined with existing LIBERO-Object official baseline, enables cross-suite comparison of official vs fine-tuned models and compression impact across task suites.\", \"parent\": \"eval_official_smolvla_baseline\", \"retry_count\": 0, \"spec\": {\"account\": \"root\", \"backend\": \"tmux\", \"checkpoint_path\": \"N/A (eval only)\", \"checkpoint_source\": \"/root/autodl-tmp/.hf_cache/smolvla_libero_official\", \"command\": \"CUDA_VISIBLE_DEVICES=1 MUJOCO_GL=egl HF_HOME=/root/autodl-tmp/.hf_cache HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 python -u eval_official_libero.py --pretrained_dir /root/autodl-tmp/.hf_cache/smolvla_libero_official --suite libero_spatial --num_episodes 50 --gpu 0 --mode baseline --seed 42 --output eval_results/eval_smolvla_official_baseline_spatial.json\", \"data_count\": 500, \"data_path\": \"libero_spatial\", \"eval_data\": \"LIBERO-Spatial (10 tasks x 50 episodes)\", \"gpu\": \"cuda:1\", \"log_path\": \"~/runs/importance_margin_vla_compress/eval_smolvla_official_baseline_spatial.log\", \"model_name\": \"SmolVLA official (HuggingFaceVLA/smolvla_libero)\", \"seed\": 42, \"server\": \"cqa1-33015\", \"submitted_at\": \"2026-05-19T20:40:24Z\", \"submitted_via\": \"tmux\", \"tmux_session\": \"eval_official_spatial\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-19T12:44:38.701Z\"}, \"eval_smolvla_prune_k05_spatial\": {\"completed_at\": \"2026-05-19T12:44:34.803Z\", \"conclusion\": \"failed\", \"created_at\": \"2026-05-19T11:35:08.730Z\", \"failure_reason\": \"startup recovery: RUNNING with no cron and no server/pid info\", \"hypothesis\": \"SmolVLA with random k=0.5 token pruning will achieve 0% SR on LIBERO-Spatial, consistent with LIBERO-Object results, because pixel-shuffle connector creates entangled tokens where any deletion causes catastrophic failure regardless of task suite.\", \"retry_count\": 0, \"spec\": {\"checkpoint_path\": \"checkpoints/libero_full_ft/step_099999/checkpoint.pt\", \"checkpoint_source\": \"checkpoints/libero_full_ft/step_099999/checkpoint.pt\", \"command\": \"CUDA_VISIBLE_DEVICES=2 python -u eval_random_prune_smolvla_spatial.py --k_ratio 0.5 --episodes_per_task 50 --output_name smolvla_random_prune_k05_spatial.json --seed 42\", \"data_count\": 500, \"data_path\": \"/root/autodl-tmp/importance_margin_vla_compress/\", \"eval_data\": \"libero_spatial (10 tasks x 50 episodes = 500 episodes)\", \"gpu\": \"cuda:2\", \"log_path\": \"eval_results/eval_prune_k05_spatial.log\", \"model_name\": \"SmolVLA full_ft baseline (libero_full_ft step_099999)\", \"seed\": 42, \"server\": \"cqa1-33015\", \"tmux_session\": \"eval_prune_spatial\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-19T12:44:34.803Z\"}, \"train_smart_compress_m16_seed44\": {\"completed_at\": \"2026-05-19T04:37:16.668Z\", \"conclusion\": \"failed\", \"created_at\": \"2026-05-19T03:03:15.846Z\", \"extra\": {\"hook_events\": [{\"action\": \"agent\", \"event\": \"on_failed\", \"ts\": \"2026-05-19T04:37:21.512792+00:00\"}], \"previous_failure\": {\"conclusion\": \"failed\"}}, \"failure_reason\": \"startup recovery: process dead, no active cron monitor\", \"hypothesis\": \"Third seed (seed=44) for Smart Compress M=16 (87.5% compression). Prior: seed42=55.8%. M=16 showed lowest SR among tested M values, confirming information bottleneck at extreme compression. Third seed establishes variance at this extreme point.\", \"notes\": \"Killed at step 35075 to free westd:cuda:0 for MLP adapter control experiment (D078 confirmed non-critical bonus).\", \"parent\": \"eval_smart_compress_m16\", \"reproduce\": {\"finished_at\": \"2026-05-19T04:37:14.278Z\"}, \"retry_count\": 1, \"spec\": {\"checkpoint_path\": \"checkpoints/smart_compress_m16_seed44/\", \"checkpoint_source\": \"smolvla_base (from scratch)\", \"command\": \"CUDA_VISIBLE_DEVICES=0 HF_HOME=/root/autodl-tmp/.hf_cache HF_HUB_OFFLINE=1 WANDB_MODE=offline python -u train_smart_compress.py --config configs/smart_compress_m16_seed44.yaml --wandb_run smart_compress_m16_seed44 --seed 44 --gpu 0\", \"data_count\": \"all\", \"data_path\": \"HuggingFaceVLA/libero\", \"eval_data\": \"HuggingFaceVLA/libero (training, not eval)\", \"log_path\": \"/root/autodl-tmp/importance_margin_vla_compress/logs/train_smart_compress_m16_seed44.log\", \"model_name\": \"smolvla_base + VisionTokenCompressor(M=16)\", \"pid\": 462076, \"seed\": 44, \"server\": \"westd-27271\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-19T12:44:31.046Z\"}, \"train_mlp_adapter_control\": {\"completed_at\": \"2026-05-19T12:00:10.299Z\", \"conclusion\": \"success\", \"created_at\": \"2026-05-19T06:06:23.543Z\", \"hypothesis\": \"An MLP+average-pooling compressor (no cross-attention, no learnable queries) with matched parameter count (~22M) will underperform the cross-attention VisionTokenCompressor at M=32, demonstrating that cross-attention's ability to selectively attend to informative tokens is critical for effective vision token compression.\", \"parent\": \"\", \"retry_count\": 0, \"spec\": {\"checkpoint_path\": \"/root/autodl-tmp/importance_margin_vla_compress/checkpoints/mlp_adapter_control/checkpoint.pt\", \"checkpoint_source\": \"/root/autodl-tmp/.hf_cache/lerobot/smolvla_base\", \"command\": \"CUDA_VISIBLE_DEVICES=0 HF_HOME=/root/autodl-tmp/.hf_cache HF_HUB_OFFLINE=1 WANDB_MODE=offline python -u train_smart_compress.py --config configs/mlp_adapter_control.yaml --wandb_run mlp_adapter_control --seed 42 --gpu 0\", \"data_count\": -1, \"data_path\": \"HuggingFaceVLA/libero\", \"log_path\": \"N/A\", \"model_name\": \"smolvla_base + MLPCompressor(3-layer MLP, 22.14M params)\", \"notes\": \"Control experiment: MLP+avg-pool compressor (no cross-attention) with matched params (~22.14M) vs VisionTokenCompressor M=32. 3x MLP blocks (Linear 960->3840 + GELU + Linear 3840->960 + LN). 128 tokens -> avg pool -> 32 tokens. tmux session: mlp_adapter_control\", \"seed\": 42, \"server\": \"westd-27271\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-19T12:00:10.299Z\"}, \"eval_smart_compress_m32_spatial\": {\"completed_at\": \"2026-05-19T11:33:06.973Z\", \"conclusion\": \"success\", \"created_at\": \"2026-05-19T11:11:10.734Z\", \"hypothesis\": \"Smart Compress M=32 (75% compression) eval on LIBERO-Spatial, seed=42. If M=32 maintains similar relative performance on Spatial as on Object (61.2% vs 44.8% baseline = +16.4pp), cross-attention compression generalizes across task suites. Combined with SmolVLA baseline Spatial and OpenVLA Spatial, completes cross-suite evidence for MF-3.\", \"retry_count\": 0, \"spec\": {\"checkpoint_path\": \"checkpoints/smart_compress_m32/checkpoint.pt\", \"checkpoint_source\": \"checkpoints/smart_compress_m32/checkpoint.pt\", \"command\": \"CUDA_VISIBLE_DEVICES=1 python eval_smart_compress_libero.py --n_queries 32 --checkpoint_path checkpoints/smart_compress_m32/checkpoint.pt --suite libero_spatial --num_episodes 50 --gpu 0 --seed 42\", \"data_count\": 500, \"data_path\": \"/root/autodl-tmp/importance_margin_vla_compress/\", \"eval_data\": \"libero_spatial\", \"gpu_ids\": [1], \"log_path\": \"eval_results/eval_smart_compress_m32_libero_spatial.json\", \"model_name\": \"smart_compress_m32\", \"seed\": 42, \"server\": \"cqa1-33015\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-19T11:33:06.973Z\"}, \"eval_smart_compress_m128_seed44\": {\"completed_at\": \"2026-05-19T11:05:26.519Z\", \"conclusion\": \"success\", \"created_at\": \"2026-05-19T10:08:22.906Z\", \"hypothesis\": \"Smart Compress M=128 (passthrough, no compression) seed=44 eval. Prior: seed42=59.8%. M=128 retains all tokens through cross-attention re-encoding. Third seed validates re-encoding gain robustness for appendix 3-seed mean±std.\", \"metrics\": {\"overall_success_rate\": 0.602, \"per_task_sr\": {\"alphabet_soup\": 0.54, \"bbq_sauce\": 0.5, \"butter\": 0.66, \"chocolate_pudding\": 0.88, \"cream_cheese\": 0.3, \"ketchup\": 0.86, \"milk\": 0.72, \"orange_juice\": 0.54, \"salad_dressing\": 0.62, \"tomato_sauce\": 0.4}, \"total_episodes\": 500, \"total_successes\": 301, \"wilson_ci_95\": [0.5585, 0.644]}, \"parent\": \"train_smart_compress_m128_seed44\", \"retry_count\": 0, \"spec\": {\"account\": \"root\", \"backend\": \"tmux\", \"checkpoint_path\": \"N/A (eval only)\", \"checkpoint_source\": \"checkpoints/smart_compress_m128_seed44/checkpoint.pt\", \"command\": \"CUDA_VISIBLE_DEVICES=1 MUJOCO_GL=egl HF_HOME=/root/autodl-tmp/.hf_cache HF_HUB_OFFLINE=1 python -u eval_smart_compress_libero.py --n_queries 128 --checkpoint_path checkpoints/smart_compress_m128_seed44/checkpoint.pt --suite libero_object --num_episodes 50 --gpu 0 --seed 44 --output eval_results/eval_smart_compress_m128_seed44.json\", \"data_count\": 500, \"data_path\": \"libero_object\", \"eval_data\": \"LIBERO-Object (10 tasks x 50 episodes)\", \"gpu_ids\": [\"cuda:1\"], \"log_path\": \"~/runs/importance_margin_vla_compress/eval_smart_compress_m128_seed44.log\", \"model_name\": \"smart_compress_m128_seed44\", \"pid\": 480299, \"seed\": 44, \"server\": \"westd-27271\", \"tmux_session\": \"eval_m128_s44\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-19T11:05:26.519Z\"}, \"train_smart_compress_m32_official\": {\"completed_at\": \"2026-05-19T10:23:38.436Z\", \"conclusion\": \"success\", \"created_at\": \"2026-05-19T01:37:54.191Z\", \"hypothesis\": \"Training Smart Compress (M=32) from the official SmolVLA checkpoint (HuggingFaceVLA/smolvla_libero, baseline SR=59.2%) will yield higher success rate than training from smolvla_base (baseline SR=44.8%), because the official checkpoint has stronger pretrained features for LIBERO tasks.\", \"notes\": \"CWD issue: nohup启动时未cd到项目目录，CWD=/root，checkpoint实际保存在/root/checkpoints/smart_compress_m32_official/checkpoint.pt（非项目目录下）。训练结束后需移动到/root/autodl-tmp/importance_margin_vla_compress/checkpoints/smart_compress_m32_official/。当前进度: step 23900/100000, loss~0.05-0.19, ETA~5.2h (截至2026-05-19 11:52)\", \"parent\": \"\", \"retry_count\": 0, \"spec\": {\"checkpoint_path\": \"/root/autodl-tmp/importance_margin_vla_compress/checkpoints/smart_compress_m32_official/checkpoint.pt\", \"checkpoint_source\": \"/root/checkpoints/smart_compress_m32_official/checkpoint.pt\", \"command\": \"CUDA_VISIBLE_DEVICES=3 HF_HOME=/root/autodl-tmp/.hf_cache HF_HUB_OFFLINE=1 WANDB_MODE=offline python -u train_smart_compress.py --config configs/smart_compress_m32_official.yaml --wandb_run smart_compress_m32_official --seed 42 --gpu 0\", \"data_count\": \"full LIBERO dataset\", \"data_path\": \"/root/autodl-tmp/importance_margin_vla_compress\", \"log_path\": \"/root/autodl-tmp/importance_margin_vla_compress/logs/train_smart_compress_m32_official.log\", \"model_name\": \"smart_compress_m32\", \"seed\": 42, \"server\": \"cqa1-33015\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-19T10:23:38.436Z\"}, \"train_smart_compress_m128_seed44\": {\"completed_at\": \"2026-05-19T10:03:52.885Z\", \"conclusion\": \"success\", \"created_at\": \"2026-05-19T03:03:16.770Z\", \"hypothesis\": \"Third seed (seed=44) for Smart Compress M=128 passthrough control. Prior: seed42=59.8%. M=128 retains all tokens through cross-attention re-encoding, isolating the architecture effect from compression. Third seed validates re-encoding gain robustness.\", \"parent\": null, \"retry_count\": 0, \"spec\": {\"checkpoint_path\": \"/root/autodl-tmp/importance_margin_vla_compress/checkpoints/smart_compress_m128_seed44/checkpoint.pt\", \"command\": \"CUDA_VISIBLE_DEVICES=1 HF_HOME=/root/autodl-tmp/.hf_cache HF_HUB_OFFLINE=1 WANDB_MODE=offline python -u train_smart_compress.py --config configs/smart_compress_m128_seed44.yaml --wandb_run smart_compress_m128_seed44 --seed 44 --gpu 0\", \"data_count\": 0, \"data_path\": \"/root/autodl-tmp/importance_margin_vla_compress/data\", \"gpu_ids\": [\"cuda:1\"], \"log_path\": \"/root/autodl-tmp/importance_margin_vla_compress/logs/smart_compress_m128_seed44.log\", \"model_name\": \"SmolVLA+VisionTokenCompressor_M128\", \"seed\": 44, \"server\": \"westd-27271\", \"tmux_session\": \"train_m128_s44\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-19T10:03:52.885Z\"}, \"eval_openvla_prune_k095\": {\"completed_at\": \"2026-05-19T00:56:35.365Z\", \"conclusion\": \"success\", \"created_at\": \"2026-05-18T20:32:24.616Z\", \"hypothesis\": \"OpenVLA (MLP projection, 7B) with k=0.95 random pruning (remove only 5% = 13/256 tokens). Expected minimal degradation (~68-72% SR vs 74% baseline). Direct comparison: at k=0.95 SmolVLA drops from 59.2% to 0% while OpenVLA should retain most performance, proving architecture-dependent token compressibility.\", \"metrics\": {\"num_episodes\": 500, \"per_task_sr\": [76, 38, 84, 54, 84, 82, 46, 74, 64, 92], \"success_rate\": 69.4, \"suite\": \"libero_object\"}, \"parent\": \"eval_openvla_pruning_k07\", \"retry_count\": 0, \"spec\": {\"checkpoint_path\": \"N/A (eval only)\", \"checkpoint_source\": \"/root/autodl-tmp/openvla-libero-object\", \"command\": \"python -u /tmp/eval_openvla_libero_gpu1.py --mode random_prune --k_ratio 0.95 --suite libero_object --num_episodes 50 --seed 7\", \"data_count\": 500, \"data_path\": \"/root/autodl-tmp/openvla-libero-object\", \"eval_data\": \"LIBERO-Object (10 tasks x 50 episodes)\", \"gpu\": \"cuda:1\", \"k_ratio\": 0.95, \"log_path\": \"/root/autodl-tmp/importance_margin_vla_compress/eval_results/openvla_random_prune_k095_object.log\", \"model_name\": \"OpenVLA-7B-libero-object\", \"pid\": 355272, \"pruning_method\": \"random + true_removal\", \"seed\": 7, \"server\": \"westd-27271\", \"tmux_session\": \"eval_openvla_k095\", \"vision_tokens\": \"256 -> 243 (remove 13)\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-19T00:56:35.365Z\"}, \"eval_openvla_prune_k09\": {\"completed_at\": \"2026-05-19T00:56:32.961Z\", \"conclusion\": \"success\", \"created_at\": \"2026-05-18T20:32:18.048Z\", \"hypothesis\": \"OpenVLA (MLP projection, 7B) with k=0.9 random pruning (true removal). Expected graceful degradation (~65-70% SR vs 74% baseline). At the same pruning ratio, SmolVLA shows 0% SR, demonstrating architecture-dependent compressibility difference between MLP projection and cross-attention.\", \"metrics\": {\"num_episodes\": 500, \"per_task_sr\": [70, 28, 76, 56, 78, 70, 42, 60, 54, 86], \"success_rate\": 62, \"suite\": \"libero_object\"}, \"retry_count\": 0, \"spec\": {\"checkpoint_path\": \"/root/autodl-tmp/openvla-libero-object\", \"checkpoint_source\": \"/root/autodl-tmp/openvla-libero-object\", \"command\": \"CUDA_VISIBLE_DEVICES=0 python -u eval_openvla_libero.py --mode random_prune --k_ratio 0.9 --suite libero_object --num_episodes 50 --seed 7\", \"data_count\": 500, \"data_path\": \"/root/autodl-tmp/importance_margin_vla_compress/eval_openvla_libero.py\", \"eval_data\": \"libero_object (10 tasks x 50 episodes)\", \"gpu\": \"cuda:0\", \"log_path\": \"/root/autodl-tmp/importance_margin_vla_compress/eval_results/openvla_random_prune_k09_object_nohup.log\", \"model_name\": \"openvla-7b-finetuned-libero-object\", \"pid\": 354653, \"pruning\": \"random, true_removal, k=0.9\", \"seed\": 7, \"server\": \"westd-27271\", \"vision_tokens\": \"256 -> 230\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-19T00:56:32.960Z\"}, \"eval_smart_compress_m32_seed43\": {\"completed_at\": \"2026-05-19T00:56:00.177Z\", \"conclusion\": \"success\", \"created_at\": \"2026-05-18T23:23:07.824Z\", \"hypothesis\": \"Smart Compress M=32 seed=43 repeat eval. M=32 is the headline result (61.6% SR at 75% compression with seed=42). If seed=43 yields similar SR (~60%), confirms robustness of the compression-performance sweet spot.\", \"metrics\": {\"num_episodes\": 500, \"per_task_sr\": [72, 38, 68, 36, 68, 48, 86, 44, 96, 36], \"success_rate\": 59.2, \"suite\": \"libero_object\"}, \"parent\": \"train_smart_compress_m32_seed43\", \"retry_count\": 0, \"spec\": {\"account\": \"root\", \"backend\": \"tmux\", \"checkpoint_path\": \"N/A (eval only)\", \"checkpoint_source\": \"checkpoints/smart_compress_m32_seed43/checkpoint.pt\", \"command\": \"CUDA_VISIBLE_DEVICES=3 python -u eval_smart_compress_libero.py --n_queries 32 --checkpoint_path checkpoints/smart_compress_m32_seed43/checkpoint.pt --suite libero_object --num_episodes 50 --gpu 0 --seed 42 --output eval_results/eval_smart_compress_m32_seed43.json\", \"data_count\": 500, \"data_path\": \"libero_object\", \"eval_data\": \"LIBERO-Object (10 tasks x 50 episodes)\", \"gpu\": \"cuda:3\", \"gpu_hours\": 1.55, \"log_path\": \"~/runs/importance_margin_vla_compress/eval_smart_compress_m32_seed43.log\", \"model_name\": \"smart_compress_m32_seed43\", \"pid\": 470232, \"seed\": 42, \"server\": \"cqa1-33015\", \"submitted_at\": \"2026-05-18T23:23:07.575Z\", \"submitted_via\": \"submit_training_job\", \"tmux_session\": \"eval_smart_compress_m32_seed43\", \"wall_clock_seconds\": 5572.6}, \"status\": \"DONE\", \"updated_at\": \"2026-05-19T00:56:00.177Z\"}, \"eval_smart_compress_m32_libero_spatial\": {\"completed_at\": \"2026-05-19T00:55:59.282Z\", \"conclusion\": \"success\", \"created_at\": \"2026-05-18T23:01:15.309Z\", \"hypothesis\": \"Smart Compress M=32 (trained on LIBERO-Object) evaluated on LIBERO-Spatial to test cross-suite generalization. If SR > 0% (hard pruning gives 0% on all suites), proves compression via cross-attention re-encoding generalizes beyond training suite.\", \"metrics\": {\"num_episodes\": 500, \"per_task_sr\": [58, 62, 52, 82, 28, 18, 82, 70, 56, 24], \"success_rate\": 53.2, \"suite\": \"libero_spatial\"}, \"parent\": \"train_smart_compress_m32\", \"retry_count\": 0, \"spec\": {\"account\": \"root\", \"backend\": \"tmux\", \"checkpoint_path\": \"N/A (eval only)\", \"checkpoint_source\": \"checkpoints/smart_compress_m32/checkpoint.pt\", \"command\": \"CUDA_VISIBLE_DEVICES=2 python -u eval_smart_compress_libero.py --n_queries 32 --checkpoint_path checkpoints/smart_compress_m32/checkpoint.pt --suite libero_spatial --num_episodes 50 --gpu 0 --seed 42 --output eval_results/eval_smart_compress_m32_libero_spatial.json\", \"data_count\": 500, \"data_path\": \"libero_spatial\", \"eval_data\": \"LIBERO-Spatial (10 tasks x 50 episodes)\", \"gpu\": \"cuda:2\", \"gpu_hours\": 1.91, \"log_path\": \"~/runs/importance_margin_vla_compress/eval_smart_compress_m32_libero_spatial.log\", \"model_name\": \"smart_compress_m32 (seed=42)\", \"pid\": 424163, \"seed\": 42, \"server\": \"cqa1-33015\", \"submitted_at\": \"2026-05-18T23:01:14.874Z\", \"submitted_via\": \"submit_training_job\", \"tmux_session\": \"eval_smart_compress_m32_libero_spatial\", \"wall_clock_seconds\": 6884.4}, \"status\": \"DONE\", \"updated_at\": \"2026-05-19T00:55:59.282Z\"}, \"eval_smart_compress_m64_seed43\": {\"completed_at\": \"2026-05-19T00:55:57.834Z\", \"conclusion\": \"success\", \"created_at\": \"2026-05-18T23:58:31.679Z\", \"hypothesis\": \"Smart Compress M=64 seed=43 repeat eval. M=64 seed=42 achieved 61.6% SR at 50% compression. If seed=43 yields similar SR (~60%), confirms robustness at this compression level.\", \"metrics\": {\"num_episodes\": 500, \"per_task_sr\": [58, 56, 46, 50, 48, 58, 80, 60, 86, 58], \"success_rate\": 60, \"suite\": \"libero_object\"}, \"parent\": \"train_smart_compress_m64_seed43\", \"retry_count\": 0, \"spec\": {\"account\": \"root\", \"backend\": \"tmux\", \"checkpoint_path\": \"N/A (eval only)\", \"checkpoint_source\": \"checkpoints/smart_compress_m64_seed43/checkpoint.pt\", \"command\": \"CUDA_VISIBLE_DEVICES=1 python -u eval_smart_compress_libero.py --n_queries 64 --checkpoint_path checkpoints/smart_compress_m64_seed43/checkpoint.pt --suite libero_object --num_episodes 50 --gpu 0 --seed 42 --output eval_results/eval_smart_compress_m64_seed43.json\", \"data_count\": 500, \"data_path\": \"libero_object\", \"eval_data\": \"LIBERO-Object (10 tasks x 50 episodes)\", \"gpu\": \"cuda:1\", \"gpu_hours\": 0.96, \"log_path\": \"~/runs/importance_margin_vla_compress/eval_smart_compress_m64_seed43.log\", \"model_name\": \"smart_compress_m64_seed43\", \"pid\": 560607, \"seed\": 42, \"server\": \"cqa1-33015\", \"submitted_at\": \"2026-05-18T23:58:31.377Z\", \"submitted_via\": \"submit_training_job\", \"tmux_session\": \"eval_smart_compress_m64_seed43\", \"wall_clock_seconds\": 3446.5}, \"status\": \"DONE\", \"updated_at\": \"2026-05-19T00:55:57.834Z\"}, \"eval_smart_compress_m32_libero_goal\": {\"completed_at\": \"2026-05-19T00:55:56.421Z\", \"conclusion\": \"success\", \"created_at\": \"2026-05-19T00:01:35.491Z\", \"hypothesis\": \"Smart Compress M=32 (trained on LIBERO-Object) evaluated on LIBERO-Goal to test cross-suite generalization. Combined with LIBERO-Spatial (~56% partial), if LIBERO-Goal SR > 0%, establishes robust cross-suite generalization claim for the paper.\", \"metrics\": {\"num_episodes\": 500, \"per_task_sr\": [60, 94, 62, 52, 32, 28, 28, 100, 78, 30], \"success_rate\": 56.4, \"suite\": \"libero_goal\"}, \"parent\": \"train_smart_compress_m32\", \"retry_count\": 0, \"spec\": {\"account\": \"root\", \"backend\": \"tmux\", \"checkpoint_path\": \"N/A (eval only)\", \"checkpoint_source\": \"checkpoints/smart_compress_m32/checkpoint.pt\", \"command\": \"CUDA_VISIBLE_DEVICES=0 python -u eval_smart_compress_libero.py --n_queries 32 --checkpoint_path checkpoints/smart_compress_m32/checkpoint.pt --suite libero_goal --num_episodes 50 --gpu 0 --seed 42 --output eval_results/eval_smart_compress_m32_libero_goal.json\", \"data_count\": 500, \"data_path\": \"libero_goal\", \"eval_data\": \"LIBERO-Goal (10 tasks x 50 episodes)\", \"gpu\": \"cuda:0\", \"gpu_hours\": 0.91, \"log_path\": \"~/runs/importance_margin_vla_compress/eval_smart_compress_m32_libero_goal.log\", \"model_name\": \"smart_compress_m32 (seed=42)\", \"pid\": 571598, \"seed\": 42, \"server\": \"cqa1-33015\", \"submitted_at\": \"2026-05-19T00:01:35.221Z\", \"submitted_via\": \"submit_training_job\", \"tmux_session\": \"eval_smart_compress_m32_libero_goal\", \"wall_clock_seconds\": 3261.2}, \"status\": \"DONE\", \"updated_at\": \"2026-05-19T00:55:56.421Z\"}, \"eval_baseline_control_prune_k05\": {\"completed_at\": \"2026-05-18T23:59:46.141Z\", \"conclusion\": \"success\", \"created_at\": \"2026-05-18T22:23:01.248Z\", \"hypothesis\": \"Baseline control 100K v2 (45.0% SR) with random pruning k=0.5. Expected 0% SR, confirming cliff-edge is inherent to pixel-shuffle architecture regardless of training duration. Strengthens narrative: extra training cannot fix the architectural fragility.\", \"metrics\": {\"num_episodes\": 500, \"per_task_sr\": [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], \"success_rate\": 0, \"suite\": \"libero_object\"}, \"parent\": \"eval_baseline_control_100k_v2\", \"retry_count\": 0, \"spec\": {\"account\": \"root\", \"backend\": \"tmux\", \"checkpoint_path\": \"N/A (eval only)\", \"checkpoint_source\": \"checkpoints/baseline_control/latest/checkpoint.pt\", \"command\": \"CUDA_VISIBLE_DEVICES=0 python -u eval_success_rate_libero.py --checkpoint checkpoints/baseline_control/latest/checkpoint.pt --config configs/baseline_control.yaml --suite libero_object --num_episodes 50 --gpu 0 --seed 42 --mode random_prune --k_ratio 0.5 --output eval_results/eval_baseline_control_prune_k05.json\", \"data_count\": 500, \"data_path\": \"libero_object\", \"eval_data\": \"LIBERO-Object (10 tasks x 50 episodes)\", \"gpu\": \"cuda:0\", \"gpu_hours\": 1.55, \"k_ratio\": 0.5, \"log_path\": \"~/runs/importance_margin_vla_compress/eval_baseline_control_prune_k05.log\", \"model_name\": \"baseline_control_100k_v2\", \"pid\": 394430, \"pruning_method\": \"random + zero_mask\", \"seed\": 42, \"server\": \"cqa1-33015\", \"submitted_at\": \"2026-05-18T22:26:42.237Z\", \"submitted_via\": \"submit_training_job\", \"tmux_session\": \"eval_baseline_control_prune_k05\", \"wall_clock_seconds\": 5583.9}, \"status\": \"DONE\", \"updated_at\": \"2026-05-18T23:59:46.141Z\"}, \"train_smart_compress_m64_seed43\": {\"completed_at\": \"2026-05-18T23:59:39.177Z\", \"conclusion\": \"success\", \"created_at\": \"2026-05-18T16:51:27.728Z\", \"hypothesis\": \"Repeat of Smart Compress M=64 training with seed=43. M=64 is a headline result (61.6% SR at 50% compression, same as M=32). If seed=43 yields similar SR (~60%), confirms robustness. If significantly different, indicates high variance.\", \"retry_count\": 0, \"spec\": {\"checkpoint_path\": \"checkpoints/smart_compress_m64_seed43/checkpoint.pt\", \"checkpoint_source\": null, \"command\": \"source /root/miniconda3/bin/activate && cd /root/autodl-tmp/importance_margin_vla_compress && HF_HOME=/root/autodl-tmp/.hf_cache HF_HUB_OFFLINE=1 WANDB_MODE=offline CUDA_VISIBLE_DEVICES=1 python -u train_smart_compress.py --config configs/smart_compress_m64_seed43.yaml --wandb_run smart_compress_m64_seed43 --seed 43 --gpu 0\", \"config\": \"configs/smart_compress_m64_seed43.yaml\", \"data_count\": null, \"data_path\": \"HuggingFaceVLA/libero\", \"eval_data\": null, \"gpu\": \"cuda:1\", \"log_path\": \"/root/runs/importance_margin_vla_compress/train_smart_compress_m64_seed43.log\", \"model_name\": \"smolvla_base + VisionTokenCompressor(M=64)\", \"pid\": 202271, \"seed\": 43, \"server\": \"cqa1-33015\", \"total_steps\": 100000}, \"status\": \"DONE\", \"updated_at\": \"2026-05-18T23:59:39.177Z\"}, \"train_smart_compress_m32_seed43\": {\"completed_at\": \"2026-05-18T23:24:25.273Z\", \"conclusion\": \"success\", \"created_at\": \"2026-05-18T16:21:33.106Z\", \"hypothesis\": \"Repeat of Smart Compress M=32 training with seed=43. M=32 is the headline result (61.6% SR at 75% compression). If seed=43 yields similar SR (~60%), confirms robustness. If significantly different, indicates high variance requiring more seeds.\", \"parent\": \"train_smart_compress_m32\", \"retry_count\": 0, \"spec\": {\"account\": \"root\", \"backend\": \"tmux\", \"checkpoint_path\": \"checkpoints/smart_compress_m32_seed43/checkpoint.pt\", \"checkpoint_source\": \"smolvla_base (from scratch)\", \"command\": \"bash -c \\\"source /root/miniconda3/bin/activate && cd /root/autodl-tmp/importance_margin_vla_compress && HF_HOME=/root/autodl-tmp/.hf_cache HF_HUB_OFFLINE=1 WANDB_MODE=offline CUDA_VISIBLE_DEVICES=3 python -u train_smart_compress.py --config configs/smart_compress_m32_seed43.yaml --wandb_run smart_compress_m32_seed43 --seed 43 --gpu 0\\\"\", \"data_count\": 0, \"data_path\": \"HuggingFaceVLA/libero\", \"eval_data\": \"HuggingFaceVLA/libero\", \"gpu\": [\"cuda:3\"], \"log_path\": \"~/runs/importance_margin_vla_compress/train_smart_compress_m32_seed43.log\", \"model_name\": \"smolvla_base + VisionTokenCompressor(M=32)\", \"pid\": \"200291\", \"seed\": 43, \"server\": \"cqa1-33015\", \"submitted_via\": \"tmux\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-18T23:24:25.273Z\"}, \"eval_smart_compress_m96_seed43_v2\": {\"completed_at\": \"2026-05-18T23:00:50.722Z\", \"conclusion\": \"success\", \"created_at\": \"2026-05-18T21:31:55.821Z\", \"hypothesis\": \"Re-eval of M=96 seed=43 with correct script (eval_smart_compress_libero.py, loads SmartCompressWrapper). Previous eval used wrong script (eval_success_rate_libero.py --mode baseline, no compressor) giving invalid 0%. Expected SR ≈ 52.6% (seed=42 result) if M-curve robust.\", \"metrics\": {\"num_episodes\": 500, \"per_task_sr\": [72, 66, 54, 48, 52, 40, 88, 60, 86, 16], \"success_rate\": 58.2, \"suite\": \"libero_object\", \"wilson_ci_95\": [53.8, 62.4]}, \"parent\": \"train_smart_compress_m96_seed43\", \"retry_count\": 0, \"spec\": {\"account\": \"root\", \"backend\": \"tmux\", \"checkpoint_path\": \"N/A (eval only)\", \"checkpoint_source\": \"checkpoints/smart_compress_m96_seed43/checkpoint.pt\", \"command\": \"CUDA_VISIBLE_DEVICES=2 python -u eval_smart_compress_libero.py --n_queries 96 --checkpoint_path checkpoints/smart_compress_m96_seed43/checkpoint.pt --suite libero_object --num_episodes 50 --gpu 0 --seed 42 --output eval_results/eval_smart_compress_m96_seed43_v2.json\", \"data_count\": 500, \"data_path\": \"libero_object\", \"eval_data\": \"LIBERO-Object (10 tasks x 50 episodes)\", \"gpu\": \"cuda:2\", \"gpu_hours\": 1.48, \"log_path\": \"/root/autodl-tmp/importance_margin_vla_compress/eval_results/eval_smart_compress_m96_seed43_v2.json\", \"model_name\": \"smart_compress_m96_seed43\", \"pid\": 322232, \"seed\": 42, \"server\": \"cqa1-33015\", \"submitted_at\": \"2026-05-18T21:31:55.572Z\", \"submitted_via\": \"submit_training_job\", \"tmux_session\": \"eval_smart_compress_m96_seed43_v2\", \"wall_clock_seconds\": 5335.1}, \"status\": \"DONE\", \"updated_at\": \"2026-05-18T23:00:50.722Z\"}, \"eval_smart_compress_m96_seed43\": {\"completed_at\": \"2026-05-18T21:26:00.573Z\", \"conclusion\": \"failed\", \"created_at\": \"2026-05-18T19:47:29.710Z\", \"hypothesis\": \"Smart Compress M=96 seed=43 repeat. If SR ≈ 52.6% (seed=42 result), confirms non-monotonic M-curve is robust. If significantly different, indicates high variance at M=96.\", \"metrics\": {\"note\": \"INVALID — used wrong eval script (eval_success_rate_libero.py --mode baseline, no compressor loaded). Re-eval as eval_smart_compress_m96_seed43_v2.\", \"num_episodes\": 500, \"per_task_sr\": [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], \"success_rate\": 0, \"suite\": \"libero_object\"}, \"parent\": \"train_smart_compress_m96_seed43\", \"retry_count\": 0, \"spec\": {\"checkpoint_path\": \"N/A (eval only)\", \"checkpoint_source\": \"checkpoints/smart_compress_m96_seed43/checkpoint.pt\", \"command\": \"CUDA_VISIBLE_DEVICES=2 python eval_success_rate_libero.py --checkpoint checkpoints/smart_compress_m96_seed43/checkpoint.pt --config configs/smart_compress_m96_seed43.yaml --suite libero_object --num_episodes 50 --gpu 0 --seed 42 --mode baseline --output eval_results/eval_smart_compress_m96_seed43.json\", \"data_count\": 50, \"data_path\": \"libero_object\", \"eval_data\": \"libero_object\", \"log_path\": \"/root/autodl-tmp/importance_margin_vla_compress/eval_results/eval_smart_compress_m96_seed43.json\", \"model_name\": \"smart_compress_m96_seed43\", \"seed\": 42, \"server\": \"cqa1-33015\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-18T21:30:12.345Z\"}, \"train_smart_compress_m96_seed43\": {\"completed_at\": \"2026-05-18T21:26:15.795Z\", \"conclusion\": \"success\", \"created_at\": \"2026-05-18T12:38:32.719Z\", \"hypothesis\": \"Repeat of Smart Compress M=96 training with seed=43. If SR is similar to seed=42 (52.6%), confirms the non-monotonic M-curve is robust. If SR differs significantly, indicates high variance at M=96 compression level.\", \"parent\": \"train_smart_compress_m96\", \"retry_count\": 0, \"spec\": {\"account\": \"root\", \"backend\": \"tmux\", \"checkpoint_path\": \"checkpoints/smart_compress_m96_seed43/checkpoint.pt\", \"checkpoint_source\": \"smolvla_base (from scratch)\", \"command\": \"bash -c \\\"source /root/miniconda3/bin/activate && cd /root/autodl-tmp/importance_margin_vla_compress && HF_HOME=/root/autodl-tmp/.hf_cache HF_HUB_OFFLINE=1 WANDB_MODE=offline CUDA_VISIBLE_DEVICES=2 python -u train_smart_compress.py --config configs/smart_compress_m96_seed43.yaml --wandb_run smart_compress_m96_seed43 --seed 43 --gpu 0\\\"\", \"data_count\": 0, \"data_path\": \"HuggingFaceVLA/libero\", \"eval_data\": \"HuggingFaceVLA/libero\", \"gpu\": [\"cuda:2\"], \"gpu_hours\": 8.8, \"log_path\": \"~/runs/importance_margin_vla_compress/train_smart_compress_m96_seed43.log\", \"model_name\": \"smolvla_base + VisionTokenCompressor(M=96)\", \"pid\": \"111876\", \"seed\": 43, \"server\": \"cqa1-33015\", \"submitted_at\": \"2026-05-18T12:38:32.454Z\", \"submitted_via\": \"submit_training_job\", \"wall_clock_seconds\": 31663.3}, \"status\": \"DONE\", \"updated_at\": \"2026-05-18T21:26:15.795Z\"}, \"train_baseline_control_100k_v2\": {\"completed_at\": \"2026-05-18T21:26:14.600Z\", \"conclusion\": \"success\", \"created_at\": \"2026-05-18T12:37:08.905Z\", \"hypothesis\": \"If Smart Compress's 15pp gain over baseline (59.8% vs 44.8%) comes from cross-attention re-encoding rather than extra training, then continuing baseline training for another 100K steps (expert-only, no compressor, fresh lr schedule) should NOT close the gap. If baseline+100K reaches ~60%, the gain was from training; if it stays near 44.8%, cross-attention architecture is the cause.\", \"parent\": \"eval_smart_compress_m128\", \"retry_count\": 0, \"spec\": {\"account\": \"root\", \"backend\": \"tmux\", \"checkpoint_path\": \"checkpoints/baseline_control/latest/checkpoint.pt\", \"checkpoint_source\": \"checkpoints/libero_full_ft/step_099999/checkpoint.pt\", \"command\": \"bash -c \\\"cd /root/autodl-tmp/importance_margin_vla_compress && source /root/miniconda3/bin/activate && HF_HOME=/root/autodl-tmp/.hf_cache HF_HUB_OFFLINE=1 WANDB_MODE=offline python train_baseline_control.py --config configs/baseline_control.yaml --wandb_project smart-compress-vla --wandb_run baseline_control_fresh_lr_v2\\\"\", \"data_count\": \"same as full_ft baseline\", \"data_path\": \"LIBERO-Object (same as full_ft baseline)\", \"eval_data\": \"N/A (training experiment, not eval)\", \"gpu\": [\"cuda:0\"], \"gpu_hours\": 8.82, \"log_path\": \"~/runs/importance_margin_vla_compress/train_baseline_control_100k_v2.log\", \"model_name\": \"SmolVLA (from step 99999 checkpoint, fresh lr)\", \"pid\": \"109885\", \"seed\": \"default\", \"server\": \"cqa1-33015\", \"submitted_at\": \"2026-05-18T12:37:08.670Z\", \"submitted_via\": \"submit_training_job\", \"wall_clock_seconds\": 31745.9}, \"status\": \"DONE\", \"updated_at\": \"2026-05-18T21:26:14.600Z\"}, \"eval_baseline_control_100k_v2\": {\"completed_at\": \"2026-05-18T21:25:59.497Z\", \"conclusion\": \"success\", \"created_at\": \"2026-05-18T19:53:48.996Z\", \"hypothesis\": \"Baseline control trained for additional 100K steps with fresh lr schedule. If SR stays near 44.8% (original baseline), confirms Smart Compress gain comes from cross-attention re-encoding, not extra training. If SR reaches ~60%, gain was from training.\", \"metrics\": {\"num_episodes\": 500, \"per_task_sr\": [0, 50, 74, 64, 68, 8, 58, 38, 52, 38], \"success_rate\": 45, \"suite\": \"libero_object\"}, \"parent\": \"train_baseline_control_100k_v2\", \"retry_count\": 0, \"spec\": {\"checkpoint_path\": \"N/A (eval only)\", \"checkpoint_source\": \"checkpoints/baseline_control/latest/checkpoint.pt\", \"command\": \"CUDA_VISIBLE_DEVICES=0 python eval_success_rate_libero.py --checkpoint checkpoints/baseline_control/latest/checkpoint.pt --config configs/baseline_control.yaml --suite libero_object --num_episodes 50 --gpu 0 --seed 42 --mode baseline --output eval_results/eval_baseline_control_100k_v2.json\", \"data_count\": 50, \"data_path\": \"libero_object\", \"eval_data\": \"libero_object\", \"log_path\": \"/root/autodl-tmp/importance_margin_vla_compress/eval_results/eval_baseline_control_100k_v2.json\", \"model_name\": \"baseline_control_100k_v2\", \"seed\": 42, \"server\": \"cqa1-33015\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-18T21:25:59.497Z\"}, \"eval_official_smolvla_prune_k095\": {\"completed_at\": \"2026-05-18T16:26:06.078Z\", \"conclusion\": \"success\", \"created_at\": \"2026-05-18T16:01:21.015Z\", \"failure_reason\": \"startup recovery: RUNNING with no cron and no server/pid info\", \"hypothesis\": \"Official SmolVLA checkpoint with k=0.95 random pruning (remove only 5% = 7/128 tokens). If 0% SR, confirms that even the slightest random token removal destroys the official model, matching our fine-tuned model's cliff-edge behavior exactly.\", \"metrics\": {\"note\": \"Official SmolVLA checkpoint k=0.95 random pruning (true_removal, remove 5% = 7 tokens) = 0% SR. All 500 episodes timeout at 280 steps.\", \"overall_sr\": 0, \"per_task_sr\": {\"all_10_tasks\": \"0%\"}, \"total_episodes\": 500, \"total_successes\": 0}, \"parent\": \"eval_official_smolvla_baseline\", \"retry_count\": 0, \"spec\": {\"checkpoint_path\": \"N/A (eval only)\", \"checkpoint_source\": \"/root/autodl-tmp/.hf_cache/smolvla_libero_official\", \"command\": \"MUJOCO_GL=egl PYTHONUNBUFFERED=1 HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 CUDA_VISIBLE_DEVICES=1 python eval_official_libero.py --pretrained_dir /root/autodl-tmp/.hf_cache/smolvla_libero_official --suite libero_object --num_episodes 50 --gpu 0 --mode random_prune --k_ratio 0.95 --output eval_results/official_libero_object_random_prune_k095.json --seed 42\", \"data_count\": \"500 episodes (10 tasks x 50 eps)\", \"data_path\": \"/root/autodl-tmp/.hf_cache/smolvla_libero_official\", \"eval_data\": \"LIBERO-Object (10 tasks, 50 episodes each)\", \"gpu\": \"cuda:1\", \"log_path\": \"/root/autodl-tmp/importance_margin_vla_compress/eval_results/official_prune_k095.log\", \"model_name\": \"SmolVLA-LIBERO official checkpoint\", \"seed\": 42, \"server\": \"westd-27271\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-18T17:27:37.072Z\"}, \"eval_official_smolvla_prune_k09\": {\"completed_at\": \"2026-05-18T16:26:04.562Z\", \"conclusion\": \"success\", \"created_at\": \"2026-05-18T16:00:44.235Z\", \"failure_reason\": \"startup recovery: RUNNING with no cron and no server/pid info\", \"hypothesis\": \"Official SmolVLA checkpoint with k=0.9 random pruning (remove only 10% visual tokens). If 0% SR like k=0.5, confirms extreme cliff-edge sensitivity where even minimal token removal destroys performance on the official checkpoint.\", \"metrics\": {\"note\": \"Official SmolVLA checkpoint k=0.9 random pruning (true_removal, remove 10% tokens) = 0% SR. All 500 episodes timeout at 280 steps.\", \"overall_sr\": 0, \"per_task_sr\": {\"all_10_tasks\": \"0%\"}, \"total_episodes\": 500, \"total_successes\": 0}, \"parent\": \"eval_official_smolvla_baseline\", \"retry_count\": 0, \"spec\": {\"checkpoint_path\": \"/root/autodl-tmp/.hf_cache/smolvla_libero_official\", \"checkpoint_source\": \"/root/autodl-tmp/.hf_cache/smolvla_libero_official\", \"command\": \"python eval_official_libero.py --pretrained_dir /root/autodl-tmp/.hf_cache/smolvla_libero_official --suite libero_object --num_episodes 50 --gpu 0 --mode random_prune --k_ratio 0.9 --output eval_results/official_libero_object_random_prune_k09.json --seed 42\", \"data_count\": 500, \"data_path\": \"libero_object (10 tasks x 50 episodes)\", \"eval_data\": \"libero_object\", \"gpu\": \"cuda:0\", \"k_ratio\": 0.9, \"log_path\": \"eval_results/official_libero_object_random_prune_k09.log\", \"model_name\": \"SmolVLA-LIBERO-official\", \"pruning_method\": \"true_removal\", \"seed\": 42, \"server\": \"westd-27271\", \"tmux_session\": \"eval_k09\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-18T17:27:34.761Z\"}, \"eval_acis_k05_supplement_v2\": {\"checkpoint_path\": \"eval_results/eval_acis_k05_supplement_v2.json\", \"completed_at\": \"2026-05-18T16:11:55.262Z\", \"conclusion\": \"success\", \"created_at\": \"2026-05-18T15:29:31.546Z\", \"hypothesis\": \"Re-run ACIS k=0.5 eval on tasks 6-9 with fixed eval script (offset-based hook). Expected 0% SR consistent with tasks 0-5. Previous run (47.5%) was invalid due to pruning hook bug.\", \"log_path\": \"logs/eval_acis_k05_v2.log\", \"metrics\": {\"note\": \"Fixed eval script with offset-based ACIS hook confirms 0% SR. Previous 47.5% was due to pruning hook bug (never applied pruning).\", \"overall_SR\": \"0.0% (0/200)\", \"task6_SR\": \"0% (0/50)\", \"task7_SR\": \"0% (0/50)\", \"task8_SR\": \"0% (0/50)\", \"task9_SR\": \"0% (0/50)\", \"wilson_ci_95\": \"[0.0%, 1.9%]\"}, \"parent\": \"eval_acis_k05_supplement_200eps\", \"retry_count\": 0, \"spec\": {\"account\": \"root\", \"backend\": \"tmux\", \"checkpoint_source\": \"checkpoints/libero_imm_twostage_fullft/stage1_done/checkpoint.pt\", \"command\": \"CUDA_VISIBLE_DEVICES=1 python -u eval_success_rate_libero.py --checkpoint checkpoints/libero_imm_twostage_fullft/stage1_done/checkpoint.pt --config configs/libero_imm_twostage_fullft.yaml --suite libero_object --mode acis_prune --pruning-method zero_mask --k_ratio 0.5 --num_episodes 50 --gpu 0 --seed 42 --task_ids 6,7,8,9 --output eval_results/eval_acis_k05_supplement_v2.json\", \"data_count\": 200, \"data_path\": \"libero_object\", \"eval_data\": \"libero_object tasks 6-9 x 50 episodes\", \"gpu\": [\"cuda:1\"], \"log_path\": \"~/runs/importance_margin_vla_compress/eval_acis_k05_supplement_v2.log\", \"model_name\": \"SmolVLA IMM twostage fullft (stage1_done)\", \"seed\": 42, \"server\": \"cqa1-33015\", \"submitted_via\": \"tmux\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-18T16:11:55.262Z\"}, \"eval_acis_k05_supplement_200eps\": {\"completed_at\": \"2026-05-18T15:04:26.839Z\", \"conclusion\": \"failed\", \"created_at\": \"2026-05-18T13:44:59.461Z\", \"hypothesis\": \"ACIS k=0.5 zero_mask pruning on tasks 6-9 should yield 0% SR, confirming that the pruned weights are critical for task performance\", \"metrics\": {\"overall_SR\": \"47.5% (95/200)\", \"task6_SR\": \"48% (24/50)\", \"task7_SR\": \"40% (20/50)\", \"task8_SR\": \"64% (32/50)\", \"task9_SR\": \"38% (19/50)\", \"wilson_ci_95\": \"[40.7%, 54.4%]\"}, \"parent\": \"eval_stage1only_object_v2_fixed\", \"retry_count\": 0, \"spec\": {\"failure_reason\": \"cqa1 eval_success_rate_libero.py is OLD version with ACIS hook bug: compares single-camera token shape vs full mask shape, always mismatches, hook returns output unchanged = NO pruning executed. 47.5% SR is unpruned baseline, not ACIS pruning result.\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-18T15:08:57.342Z\"}, \"eval_official_smolvla_prune_k05_v2\": {\"checkpoint_path\": \"N/A (eval only)\", \"completed_at\": \"2026-05-18T14:11:21.198Z\", \"conclusion\": \"success\", \"created_at\": \"2026-05-18T13:24:02.097Z\", \"extra\": {\"hook_events\": [{\"action\": \"agent\", \"event\": \"on_complete\", \"ts\": \"2026-05-18T14:09:27.250914+00:00\"}]}, \"hypothesis\": \"Official SmolVLA LIBERO checkpoint with k=0.5 random pruning (keep 50% = 64/128 tokens) on LIBERO-Object. If 0% SR (same as our fine-tuned model), confirms cliff-edge is inherent to pixel-shuffle architecture, not fine-tuning-specific. If >0%, suggests official training creates different token dependencies.\", \"log_path\": \"~/runs/importance_margin_vla_compress/eval_official_smolvla_prune_k05_v2.log\", \"metrics\": {\"note\": \"Official SmolVLA checkpoint with k=0.5 random pruning = 0% SR, confirming cliff-edge on official checkpoint (59.2% baseline → 0%)\", \"overall_sr\": 0, \"per_task_sr\": {\"all_tasks\": \"0%\"}, \"total_episodes\": 500, \"total_successes\": 0}, \"parent\": \"eval_official_smolvla_baseline\", \"reproduce\": {\"finished_at\": \"2026-05-18T14:09:22.717Z\"}, \"retry_count\": 0, \"spec\": {\"account\": \"root\", \"backend\": \"tmux\", \"checkpoint_source\": \"/root/autodl-tmp/.hf_cache/smolvla_libero_official\", \"command\": \"python -u eval_official_libero.py --mode random_prune --k_ratio 0.5 --num_episodes 50 --suite libero_object --seed 42\", \"data_count\": 500, \"data_path\": \"libero_object\", \"eval_data\": \"libero_object (10 tasks x 50 episodes)\", \"gpu\": [\"cuda:1\"], \"gpu_hours\": 0.78, \"log_path\": \"~/runs/importance_margin_vla_compress/eval_official_smolvla_prune_k05_v2.log\", \"model_name\": \"smolvla_libero_official\", \"pid\": \"136801\", \"seed\": 42, \"server\": \"westd-27271\", \"submitted_at\": \"2026-05-18T13:24:15.257Z\", \"submitted_via\": \"submit_training_job\", \"wall_clock_seconds\": 2825.9}, \"status\": \"DONE\", \"updated_at\": \"2026-05-18T14:11:29.005Z\"}, \"eval_official_smolvla_baseline\": {\"checkpoint_path\": \"N/A (eval-only)\", \"completed_at\": \"2026-05-18T13:58:17.855Z\", \"conclusion\": \"success\", \"created_at\": \"2026-05-18T12:43:13.148Z\", \"extra\": {\"hook_events\": [{\"action\": \"agent\", \"event\": \"on_complete\", \"ts\": \"2026-05-18T13:56:28.169877+00:00\"}]}, \"hypothesis\": \"Official SmolVLA LIBERO checkpoint unpruned baseline on LIBERO-Object. Establishes baseline SR for official checkpoint to compare against pruning experiments. If ~44.8% (similar to our fine-tuned), confirms consistent baseline. If different, indicates training-specific effects.\", \"log_path\": \"~/runs/importance_margin_vla_compress/eval_official_smolvla_baseline.log\", \"metrics\": {\"overall_sr\": 59.2, \"per_task_sr\": {\"task_0_alphabet_soup\": 64, \"task_1_cream_cheese\": 40, \"task_2_salad_dressing\": 44, \"task_3_bbq_sauce\": 38, \"task_4_ketchup\": 60, \"task_5_tomato_sauce\": 46, \"task_6_butter\": 78, \"task_7_milk\": 52, \"task_8_chocolate_pudding\": 90, \"task_9_orange_juice\": 80}, \"total_episodes\": 500, \"total_successes\": 296, \"wilson_ci_95\": [54.8, 63.4]}, \"parent\": \"eval_smolvla_random_prune_k095\", \"reproduce\": {\"finished_at\": \"2026-05-18T13:56:17.750Z\"}, \"retry_count\": 0, \"spec\": {\"account\": \"root\", \"backend\": \"tmux\", \"checkpoint_source\": \"smolvla_libero_official\", \"command\": \"python eval_official_libero.py --pretrained_dir /root/autodl-tmp/.hf_cache/smolvla_libero_official --suite libero_object --num_episodes 50 --gpu 0 --mode baseline --seed 42\", \"data_count\": 500, \"data_path\": \"LIBERO-Object\", \"eval_data\": \"LIBERO-Object 10 tasks x 50 episodes\", \"gpu\": [\"cuda:0\"], \"gpu_hours\": 0.67, \"gpu_id\": \"cuda:0\", \"log_path\": \"~/runs/importance_margin_vla_compress/eval_official_smolvla_baseline.log\", \"model_name\": \"SmolVLA official checkpoint (HuggingFace)\", \"pid\": \"117439\", \"seed\": 42, \"server\": \"westd-27271\", \"submitted_at\": \"2026-05-18T13:17:58.352Z\", \"submitted_via\": \"submit_training_job\", \"wall_clock_seconds\": 2419.5}, \"status\": \"DONE\", \"updated_at\": \"2026-05-18T13:58:17.855Z\"}, \"eval_smolvla_random_prune_k095\": {\"checkpoint_path\": \"/root/autodl-tmp/importance_margin_vla_compress/eval_results/smolvla_random_prune_k095.json\", \"completed_at\": \"2026-05-18T13:20:17.960Z\", \"conclusion\": \"success\", \"created_at\": \"2026-05-18T12:16:53.132Z\", \"hypothesis\": \"Random pruning at k=0.95 (removing only 7/128 tokens) will still cause complete failure (0% SR), demonstrating extreme cliff-edge sensitivity where even minimal random token removal destroys VLA action generation\", \"log_path\": \"~/runs/importance_margin_vla_compress/eval_smolvla_random_prune_k095.log\", \"metrics\": {\"k_ratio\": 0.95, \"overall_SR\": 0, \"per_task_SR\": {\"T0_alphabet_soup\": 0, \"T1_cream_cheese\": 0, \"T2_salad_dressing\": 0, \"T3_bbq_sauce\": 0, \"T4_ketchup\": 0, \"T5_tomato_sauce\": 0, \"T6_butter\": 0, \"T7_milk\": 0, \"T8_chocolate_pudding\": 0, \"T9_orange_juice\": 0}, \"tokens_kept\": 121, \"tokens_removed\": 7, \"total_episodes\": 500, \"total_successes\": 0, \"wilson_ci_95\": [0, 0.0076]}, \"parent\": \"eval_smolvla_random_prune\", \"retry_count\": 0, \"spec\": {\"account\": \"root\", \"backend\": \"tmux\", \"checkpoint_path\": \"checkpoints/libero_full_ft/step_099999/checkpoint.pt\", \"checkpoint_source\": \"checkpoints/libero_full_ft/step_099999/checkpoint.pt\", \"command\": \"CUDA_VISIBLE_DEVICES=1 python -u eval_random_prune_smolvla.py --k_ratio 0.95 --episodes_per_task 50 --output_name smolvla_random_prune_k095.json --seed 42\", \"data_count\": 500, \"data_path\": \"LIBERO-Object (10 tasks x 50 eps)\", \"eval_data\": \"LIBERO-Object\", \"gpu\": [\"cuda:1\"], \"gpu_hours\": 1.05, \"log_path\": \"~/runs/importance_margin_vla_compress/eval_smolvla_random_prune_k095.log\", \"model_name\": \"SmolVLA full_ft (baseline)\", \"pid\": \"92881\", \"seed\": 42, \"server\": \"cqa1-33015\", \"submitted_at\": \"2026-05-18T12:17:00Z\", \"submitted_via\": \"tmux\", \"wall_clock_seconds\": 3798.0}, \"status\": \"DONE\", \"updated_at\": \"2026-05-18T13:20:17.960Z\"}, \"eval_official_smolvla_pruning\": {\"completed_at\": \"2026-05-18T12:57:46.413Z\", \"conclusion\": \"failed\", \"created_at\": \"2026-05-18T12:43:31.516Z\", \"failure_reason\": \"startup recovery: RUNNING with no cron and no server/pid info\", \"hypothesis\": \"Official SmolVLA LIBERO checkpoint with random pruning k=0.5 should also show 0% SR cliff-edge, confirming the phenomenon is not specific to our fine-tuning setup but inherent to the pixel-shuffle architecture.\", \"parent\": \"eval_smolvla_random_prune_k095\", \"retry_count\": 0, \"spec\": {\"checkpoint_source\": \"/root/autodl-tmp/.hf_cache/smolvla_libero_official\", \"command\": \"python eval_official_libero.py --pretrained_dir /root/autodl-tmp/.hf_cache/smolvla_libero_official --suite libero_object --num_episodes 50 --mode baseline/random_prune --k_ratio 0.5\", \"data_count\": 500, \"data_path\": \"LIBERO libero_object (sim)\", \"eval_data\": \"libero_object 10 tasks x 50 episodes\", \"model_name\": \"SmolVLA-500M-official-LIBERO\", \"seed\": 42, \"server\": \"westd-27271\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-18T12:57:46.413Z\"}, \"train_baseline_control_100k\": {\"completed_at\": \"2026-05-18T12:33:39.888Z\", \"conclusion\": \"failed\", \"created_at\": \"2026-05-18T12:25:07.235Z\", \"failure_reason\": \"EXIT_CODE=1 (generic error — check log tail)\", \"hypothesis\": \"If Smart Compress's 15pp gain over baseline (59.8% vs 44.8%) comes from cross-attention re-encoding rather than extra training, then continuing baseline training for another 100K steps (expert-only, no compressor) should NOT close the gap. If baseline+100K reaches ~60%, the gain was from training; if it stays near 44.8%, cross-attention architecture is the cause.\", \"notes\": \"wandb.init() failed — no WANDB_API_KEY on cqa1-33015. Restarted as train_baseline_control_100k_v2 with WANDB_MODE=offline.\", \"parent\": \"eval_smart_compress_m128\", \"retry_count\": 0, \"spec\": {\"account\": \"root\", \"backend\": \"tmux\", \"checkpoint_source\": \"checkpoints/libero_full_ft/step_099999/checkpoint.pt\", \"command\": \"python train_baseline_control.py --config configs/baseline_control.yaml --wandb_project smart-compress-vla --wandb_run baseline_control_fresh_lr\", \"data_count\": \"same as full_ft baseline\", \"data_path\": \"LIBERO-Object (same as full_ft baseline)\", \"eval_data\": \"N/A (training experiment, not eval)\", \"gpu\": \"cuda:0\", \"gpu_hours\": 0.14, \"log_path\": \"~/runs/importance_margin_vla_compress/train_baseline_control_100k.log\", \"model_name\": \"SmolVLA (from step 99999 checkpoint)\", \"pid\": \"100236\", \"seed\": \"default\", \"server\": \"cqa1-33015\", \"submitted_at\": \"2026-05-18T12:25:14.994Z\", \"submitted_via\": \"submit_training_job\", \"trainable_params\": \"99.9M (action expert + projections only)\", \"wall_clock_seconds\": 504.9}, \"status\": \"DONE\", \"updated_at\": \"2026-05-18T12:39:31.964Z\"}, \"eval_smart_compress_m128\": {\"checkpoint_path\": \"N/A (eval only)\", \"completed_at\": \"2026-05-18T11:20:33.418Z\", \"conclusion\": \"success\", \"created_at\": \"2026-05-18T10:08:14.626Z\", \"hypothesis\": \"Cross-attention pooling with M=128 queries (no compression, passthrough control) on LIBERO-Object. If SR similar to M=32/M=64 (61.6%), improvement comes from cross-attention architecture itself. If lower/equal to baseline (44.8%), compression bottleneck provides the benefit. Critical control experiment for paper framing.\", \"metrics\": {\"libero_object_sr\": 0.598, \"libero_object_sr_ci95\": [0.554, 0.64], \"per_task_sr\": {\"alphabet_soup\": 0.62, \"bbq_sauce\": 0.34, \"butter\": 0.82, \"chocolate_pudding\": 0.82, \"cream_cheese\": 0.58, \"ketchup\": 0.62, \"milk\": 0.56, \"orange_juice\": 0.58, \"salad_dressing\": 0.54, \"tomato_sauce\": 0.5}, \"total_episodes\": 500, \"total_successes\": 299}, \"parent\": \"train_smart_compress_m128_resume\", \"retry_count\": 0, \"spec\": {\"account\": \"root\", \"backend\": \"tmux\", \"checkpoint_source\": \"checkpoints/smart_compress_m128/checkpoint.pt\", \"command\": \"eval_smart_compress_libero.py --n_queries 128\", \"data_count\": 500, \"data_path\": \"libero_object\", \"eval_data\": \"libero_object\", \"gpu\": [\"cuda:0\"], \"gpu_hours\": 1.2, \"log_path\": \"~/runs/importance_margin_vla_compress/eval_smart_compress_m128.log\", \"model_name\": \"smart_compress_m128\", \"pid\": \"18074\", \"seed\": 42, \"server\": \"cqa1-33015\", \"submitted_at\": \"2026-05-18T10:08:26.674Z\", \"submitted_via\": \"submit_training_job\", \"wall_clock_seconds\": 4326.7}, \"status\": \"DONE\", \"updated_at\": \"2026-05-18T11:20:33.418Z\"}, \"eval_openvla_pruning_k03_restart\": {\"checkpoint_path\": \"/root/autodl-tmp/importance_margin_vla_compress/eval_results/openvla_random_prune_k03_object.json\", \"completed_at\": \"2026-05-18T10:23:22.693Z\", \"conclusion\": \"success\", \"created_at\": \"2026-05-18T05:29:54.046Z\", \"hypothesis\": \"Restart of eval_openvla_pruning_k03 after server reboot. OpenVLA k=0.3 random pruning (keep 30% = 76 tokens). Completing degradation curve.\", \"log_path\": \"/root/autodl-tmp/importance_margin_vla_compress/eval_results/openvla_random_prune_k03_restart.log\", \"metrics\": {\"elapsed_minutes\": 288.6, \"overall_sr\": 0.206, \"per_task_sr\": {\"alphabet_soup\": 0.14, \"bbq_sauce\": 0.3, \"butter\": 0, \"chocolate_pudding\": 0.1, \"cream_cheese\": 0, \"ketchup\": 0.3, \"milk\": 0.08, \"orange_juice\": 0.42, \"salad_dressing\": 0.64, \"tomato_sauce\": 0.08}, \"total_episodes\": 500, \"total_successes\": 103, \"wilson_ci_95\": [0.173, 0.244]}, \"parent\": \"eval_openvla_pruning_k03\", \"retry_count\": 0, \"spec\": {\"checkpoint_source\": \"/root/autodl-tmp/openvla-libero-object\", \"command\": \"python -u /tmp/eval_openvla_libero_gpu1.py --mode random_prune --k_ratio 0.3 --suite libero_object --num_episodes 50 --seed 7\", \"data_count\": 500, \"data_path\": \"/root/autodl-tmp/openvla-libero-object\", \"eval_data\": \"libero_object\", \"model_name\": \"openvla-libero-object\", \"seed\": 7, \"server\": \"westd-27271\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-18T10:23:22.693Z\"}, \"smolvla_entropy_perlayer\": {\"completed_at\": \"2026-05-18T07:03:49.995Z\", \"conclusion\": \"success\", \"created_at\": \"2026-05-18T07:01:32.515Z\", \"hypothesis\": \"SmolVLA per-layer attention entropy will be uniformly high (~0.98) across all 16 layers, in contrast to OpenVLA's progressive sharpening (0.98→0.48). This flat profile would confirm that pixel-shuffle creates uniform token dependence at every depth.\", \"metrics\": {\"dataset\": \"LIBERO-Object (task 20-29)\", \"entropy_range\": [0.9311, 0.9826], \"entropy_range_width\": 0.05, \"n_images\": 260, \"n_layers\": 16, \"n_tasks\": 10, \"note\": \"Fixed: previous run sampled task 0-8 (LIBERO-90), not LIBERO-Object. Difference: 0.952 vs 0.944, conclusion unchanged.\", \"openvla_comparison\": {\"overall\": 0.639, \"range_width\": 0.5}, \"overall_entropy_ratio\": 0.9521, \"overall_entropy_std\": 0.02, \"per_layer\": {\"L0\": 0.9826, \"L1\": 0.9561, \"L10\": 0.9455, \"L11\": 0.951, \"L12\": 0.9485, \"L13\": 0.9311, \"L14\": 0.9482, \"L15\": 0.9566, \"L2\": 0.9597, \"L3\": 0.9434, \"L4\": 0.9408, \"L5\": 0.9406, \"L6\": 0.9474, \"L7\": 0.9628, \"L8\": 0.9614, \"L9\": 0.9572}}, \"retry_count\": 0, \"spec\": {\"checkpoint_path\": \"N/A (analysis)\", \"checkpoint_source\": \"/root/autodl-tmp/.hf_cache/lerobot/smolvla_base\", \"command\": \"python measure_smolvla_entropy_perlayer.py\", \"data_count\": 256, \"data_path\": \"HuggingFaceVLA/libero (cached)\", \"eval_data\": \"LIBERO mixed tasks\", \"log_path\": \"/root/autodl-tmp/importance_margin_vla_compress/eval_results/smolvla_entropy_perlayer.log\", \"model_name\": \"smolvla_base\", \"seed\": 42, \"server\": \"cqa1-33015\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-18T07:19:52.802Z\"}, \"inference_latency_comparison\": {\"checkpoint_path\": \"eval_results/inference_latency_comparison.json\", \"completed_at\": \"2026-05-18T07:01:05.147Z\", \"conclusion\": \"success\", \"created_at\": \"2026-05-18T06:59:04.973Z\", \"hypothesis\": \"Smart Compress with M=32 (75% fewer vision tokens) will show measurable inference speedup over baseline 128 tokens, quantifying the practical benefit of learned compression.\", \"log_path\": \"logs/inference_latency_comparison.log\", \"metrics\": {\"baseline_128_mean_ms\": 164.33, \"baseline_params\": 450046176, \"compressor_m32_params\": 22179840, \"m32_mean_ms\": 154.78, \"m64_mean_ms\": 156.16, \"speedup_m32\": 1.0617, \"speedup_m64\": 1.0523}, \"retry_count\": 0, \"spec\": {\"command\": \"cd /root/autodl-tmp/importance_margin_vla_compress && CUDA_VISIBLE_DEVICES=2 python measure_inference_latency.py\", \"data_count\": 0, \"data_path\": \"N/A\", \"model_name\": \"smolvla_base + SmartCompressWrapper\", \"seed\": 42, \"server\": \"cqa1-33015\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-18T07:01:05.146Z\"}, \"eval_openvla_pruning_k03\": {\"completed_at\": \"2026-05-18T06:15:16.402Z\", \"conclusion\": \"killed\", \"created_at\": \"2026-05-18T01:01:28.122Z\", \"hypothesis\": \"OpenVLA (7B) with k=0.3 random pruning (keep 30% = 76 tokens) on LIBERO-Object will show severe but non-zero degradation, completing the 4-point degradation curve (k=1.0 74% → k=0.7 ? → k=0.5 37.4% → k=0.3 ?). Expected SR significantly below k=0.5 but possibly above 0% due to OpenVLA architecture tolerance.\", \"parent\": \"eval_openvla_pruning_k05\", \"retry_count\": 0, \"spec\": {\"checkpoint_path\": \"N/A (eval only)\", \"checkpoint_source\": \"openvla-libero-object\", \"command\": \"python -u /tmp/eval_openvla_libero_gpu1.py --mode random_prune --k_ratio 0.3 --suite libero_object --num_episodes 50 --seed 7\", \"data_count\": 500, \"data_path\": \"LIBERO-Object (10 tasks x 50 eps)\", \"eval_data\": \"LIBERO-Object\", \"gpu\": \"cuda:1\", \"log_path\": \"/root/autodl-tmp/importance_margin_vla_compress/eval_results/openvla_random_prune_k03_object.log\", \"model_name\": \"OpenVLA (7B)\", \"pid\": 768729, \"seed\": 7, \"server\": \"westd-27271\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-18T06:15:16.402Z\"}, \"openvla_entropy_real\": {\"checkpoint_path\": \"N/A (analysis only)\", \"completed_at\": \"2026-05-18T05:39:26.750Z\", \"conclusion\": \"success\", \"created_at\": \"2026-05-18T05:35:28.266Z\", \"hypothesis\": \"Measure OpenVLA attention entropy on real LIBERO-Object images (250 frames, 10 tasks) to replace previous measurement on 20 random images. Expected similar directional finding (entropy << 1.0) but more defensible to reviewers.\", \"log_path\": \"/root/autodl-tmp/importance_margin_vla_compress/eval_results/openvla_entropy_real.log\", \"metrics\": {\"deep_layers_27_30\": [0.542, 0.53, 0.477, 0.524], \"max_entropy_layer\": {\"layer\": 0, \"ratio\": 0.979}, \"min_entropy_layer\": {\"layer\": 29, \"ratio\": 0.4774}, \"n_images\": 250, \"n_tasks\": 10, \"overall_entropy_ratio\": 0.6393, \"overall_entropy_std\": 0.1334, \"overall_vision_attn_frac\": 0.1211, \"previous_random_N20\": 0.617, \"shallow_layers_0_1\": [0.979, 0.952], \"smolvla_reference\": 0.98}, \"retry_count\": 0, \"spec\": {\"command\": \"MUJOCO_GL=egl HF_HOME=/root/autodl-tmp/.hf_cache CUDA_VISIBLE_DEVICES=0 python measure_openvla_entropy_real.py\", \"data_count\": 250, \"data_path\": \"LIBERO-Object simulation (10 tasks, 250 rendered frames)\", \"model_name\": \"OpenVLA-7B-libero-object\", \"seed\": 42, \"server\": \"westd-27271\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-18T05:39:26.750Z\"}, \"train_smart_compress_m128\": {\"completed_at\": \"2026-05-18T05:24:55.028Z\", \"conclusion\": \"failed\", \"created_at\": \"2026-05-18T02:57:30.022Z\", \"hypothesis\": \"Cross-attention pooling with M=128 queries attending to 128 source tokens (no compression, passthrough control). If SR is similar to M=32/M=64 (61.6%), the improvement over baseline comes from cross-attention architecture itself, not compression. If SR is higher, compression may be slightly hurting. If SR is lower or equal to baseline (44.8%), compression itself provides the benefit.\", \"parent\": \"eval_smart_compress_m32\", \"retry_count\": 0, \"spec\": {\"account\": \"root\", \"backend\": \"tmux\", \"checkpoint_path\": \"/root/autodl-tmp/importance_margin_vla_compress/checkpoints/smart_compress_m128/checkpoint.pt\", \"checkpoint_source\": \"/root/autodl-tmp/libero_full_ft/step_099999/checkpoint.pt\", \"command\": \"bash -c \\\"cd /root/autodl-tmp/importance_margin_vla_compress && source /root/miniconda3/bin/activate && HF_HOME=/root/autodl-tmp/.hf_cache HF_HUB_OFFLINE=1 WANDB_MODE=offline python train_smart_compress.py --config configs/smart_compress_m128.yaml --wandb_run smart_compress_m128\\\"\", \"data_count\": 100000, \"data_path\": \"LIBERO dataset\", \"eval_data\": \"N/A (training)\", \"failure_reason\": \"Server rebooted at ~13:22 UTC, training interrupted at step 32500/100000 (32.5%). Last checkpoint at step 32000.\", \"gpu\": \"cuda:0\", \"gpu_hours\": 2.45, \"last_loss\": 0.0476, \"last_step\": 32500, \"log_path\": \"~/runs/importance_margin_vla_compress/train_smart_compress_m128.log\", \"model_name\": \"SmolVLA-SmartCompress-M128\", \"pid\": 685989, \"seed\": 42, \"server\": \"cqa1-33015\", \"submitted_at\": \"2026-05-18T02:57:46.749Z\", \"submitted_via\": \"submit_training_job\", \"wall_clock_seconds\": 8828.3}, \"status\": \"DONE\", \"updated_at\": \"2026-05-18T05:24:55.028Z\"}, \"eval_smart_compress_m96\": {\"completed_at\": \"2026-05-18T05:09:45.271Z\", \"conclusion\": \"success\", \"created_at\": \"2026-05-18T04:10:41.873Z\", \"extra\": {\"hook_events\": [{\"action\": \"agent\", \"event\": \"on_complete\", \"ts\": \"2026-05-18T05:08:08.217286+00:00\"}]}, \"hypothesis\": \"Cross-attention pooling compression (128→96 tokens, 25% reduction) is the mildest compression. Expected to retain near-full SR, establishing the upper bound of the compression-performance curve alongside M=32 (61.6%) and M=64 (61.6%).\", \"metrics\": {\"overall_sr\": 52.6, \"per_task_sr\": {\"task_0_alphabet_soup\": 40, \"task_1_cream_cheese\": 52, \"task_2_salad_dressing\": 56, \"task_3_bbq_sauce\": 40, \"task_4_ketchup\": 26, \"task_5_tomato_sauce\": 50, \"task_6_butter\": 72, \"task_7_milk\": 62, \"task_8_chocolate_pudding\": 86, \"task_9_orange_juice\": 42}, \"total_episodes\": 500, \"total_successes\": 263, \"wilson_ci_95\": [48.2, 56.9]}, \"parent\": \"train_smart_compress_m96\", \"reproduce\": {\"finished_at\": \"2026-05-18T05:08:01.938Z\"}, \"retry_count\": 0, \"spec\": {\"account\": \"root\", \"backend\": \"tmux\", \"checkpoint_path\": \"checkpoints/smart_compress_m96/checkpoint.pt\", \"checkpoint_source\": \"checkpoints/smart_compress_m96/checkpoint.pt\", \"command\": \"bash -c \\\"cd /root/autodl-tmp/importance_margin_vla_compress && source /root/miniconda3/bin/activate && HF_HOME=/root/autodl-tmp/.hf_cache python eval_smart_compress_libero.py --checkpoint_path checkpoints/smart_compress_m96/checkpoint.pt --n_queries 96 --num_episodes 50 --suite libero_object --seed 42\\\"\", \"data_count\": 500, \"data_path\": \"LIBERO-Object (10 tasks x 50 eps)\", \"eval_data\": \"LIBERO-Object\", \"gpu\": \"cuda:1\", \"gpu_hours\": 0.98, \"log_path\": \"~/runs/importance_margin_vla_compress/eval_smart_compress_m96.log\", \"model_name\": \"SmolVLA-SmartCompress-M96\", \"pid\": 689457, \"seed\": 42, \"server\": \"cqa1-33015\", \"submitted_at\": \"2026-05-18T04:10:59.380Z\", \"submitted_via\": \"submit_training_job\", \"wall_clock_seconds\": 3525.9}, \"status\": \"DONE\", \"updated_at\": \"2026-05-18T05:10:12.875Z\"}, \"eval_smart_compress_m16\": {\"completed_at\": \"2026-05-18T05:09:46.379Z\", \"conclusion\": \"success\", \"created_at\": \"2026-05-18T04:10:44.382Z\", \"extra\": {\"hook_events\": [{\"action\": \"agent\", \"event\": \"on_complete\", \"ts\": \"2026-05-18T05:08:13.758917+00:00\"}]}, \"hypothesis\": \"Cross-attention pooling compression (128→16 tokens, 87.5% compression) is the most extreme reduction. Expected to show degradation vs M=32/M=64, establishing the lower bound of the compression curve and testing where soft compression begins to fail.\", \"metrics\": {\"overall_sr\": 55.8, \"overall_sr_ci95\": [51.4, 60.1], \"per_task_sr\": {\"task_0_alphabet_soup\": 56, \"task_1_cream_cheese\": 44, \"task_2_salad_dressing\": 72, \"task_3_bbq_sauce\": 56, \"task_4_ketchup\": 62, \"task_5_tomato_sauce\": 40, \"task_6_butter\": 78, \"task_7_milk\": 54, \"task_8_chocolate_pudding\": 76, \"task_9_orange_juice\": 20}, \"runtime_minutes\": 55, \"total_episodes\": 500, \"total_successes\": 279}, \"parent\": \"smart_compress_m16\", \"reproduce\": {\"finished_at\": \"2026-05-18T05:08:08.647Z\"}, \"retry_count\": 0, \"spec\": {\"account\": \"root\", \"backend\": \"tmux\", \"checkpoint_path\": \"checkpoints/smart_compress_m16/checkpoint.pt\", \"checkpoint_source\": \"checkpoints/smart_compress_m16/checkpoint.pt\", \"command\": \"bash -c \\\"cd /root/autodl-tmp/importance_margin_vla_compress && source /root/miniconda3/bin/activate && HF_HOME=/root/autodl-tmp/.hf_cache python eval_smart_compress_libero.py --checkpoint_path checkpoints/smart_compress_m16/checkpoint.pt --n_queries 16 --num_episodes 50 --suite libero_object --seed 42\\\"\", \"data_count\": 500, \"data_path\": \"LIBERO-Object (10 tasks x 50 eps)\", \"eval_data\": \"LIBERO-Object\", \"gpu\": \"cuda:2\", \"gpu_hours\": 0.98, \"log_path\": \"~/runs/importance_margin_vla_compress/eval_smart_compress_m16.log\", \"model_name\": \"SmolVLA-SmartCompress-M16\", \"pid\": 689536, \"seed\": 42, \"server\": \"cqa1-33015\", \"submitted_at\": \"2026-05-18T04:11:00.528Z\", \"submitted_via\": \"submit_training_job\", \"wall_clock_seconds\": 3525.9}, \"status\": \"DONE\", \"updated_at\": \"2026-05-18T05:10:04.657Z\"}, \"eval_openvla_pruning_k07\": {\"checkpoint_path\": \"N/A (eval only)\", \"completed_at\": \"2026-05-18T04:58:42.562Z\", \"conclusion\": \"success\", \"created_at\": \"2026-05-18T00:07:29.205Z\", \"hypothesis\": \"OpenVLA (7B) with random k=0.7 true_removal (keep 70% tokens) on LIBERO-Object. k=0.5 showed 74%→37.4% (graceful). k=0.7 retains more tokens so should degrade less — establishing the degradation curve slope for OpenVLA.\", \"log_path\": \"/root/autodl-tmp/importance_margin_vla_compress/eval_results/openvla_random_prune_k07_object.log\", \"metrics\": {\"elapsed_minutes\": 260.7, \"overall_sr\": 0.49, \"per_task_sr\": {\"alphabet_soup\": 0.74, \"bbq_sauce\": 0.46, \"butter\": 0.1, \"chocolate_pudding\": 0.32, \"cream_cheese\": 0.18, \"ketchup\": 0.68, \"milk\": 0.4, \"orange_juice\": 0.76, \"salad_dressing\": 0.64, \"tomato_sauce\": 0.62}, \"total_episodes\": 500, \"total_successes\": 245}, \"parent\": \"eval_openvla_pruning_k05\", \"retry_count\": 0, \"spec\": {\"checkpoint_source\": \"/root/autodl-tmp/openvla-libero-object\", \"command\": \"nohup python -u eval_openvla_libero.py --mode random_prune --k_ratio 0.7 --suite libero_object --num_episodes 50 --seed 7 > eval_results/openvla_random_prune_k07_object.log 2>&1 &\", \"data_count\": 500, \"data_path\": \"/root/autodl-tmp/libero/libero_object\", \"eval_data\": \"libero_object_10tasks_50eps\", \"model_name\": \"openvla-7b-libero-object\", \"seed\": 7, \"server\": \"westd-27271\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-18T04:58:42.562Z\"}, \"train_smart_compress_m96\": {\"completed_at\": \"2026-05-18T04:14:54.665Z\", \"conclusion\": \"success\", \"created_at\": \"2026-05-17T21:26:45.277Z\", \"extra\": {\"hook_events\": [{\"action\": \"agent\", \"event\": \"on_failed\", \"ts\": \"2026-05-18T04:14:57.122112+00:00\"}]}, \"failure_reason\": \"process dead 5× with no sentinel/W&B — auto-resolved as failed\", \"hypothesis\": \"Cross-attention pooling compression (128→96 tokens, 25% reduction) — the mildest compression point. Expected to retain near-full SR, establishing the upper bound of the compression-performance curve.\", \"metrics\": {\"eval_action_loss\": 0.064, \"total_steps\": 100000, \"train_action_loss\": 0.055}, \"parent\": \"train_smart_compress_m64\", \"reproduce\": {\"finished_at\": \"2026-05-18T04:14:53.512Z\"}, \"retry_count\": 0, \"spec\": {\"checkpoint_source\": \"/root/autodl-tmp/libero_full_ft/step_099999/checkpoint.pt\", \"command\": \"nohup python -u train_smart_compress.py --n_queries 96 > train_M96.log 2>&1 &\", \"data_count\": 130, \"data_path\": \"HuggingFaceVLA/libero (130 task demos)\", \"eval_data\": \"N/A (training)\", \"model_name\": \"smolvla-smart-compress-m96\", \"seed\": 42, \"server\": \"cqa1-33015\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-18T04:36:32.132Z\"}, \"smart_compress_m16\": {\"completed_at\": \"2026-05-18T04:16:02.545Z\", \"conclusion\": \"success\", \"created_at\": \"2026-05-17T21:08:36.215Z\", \"hypothesis\": \"Compressing 128 vision tokens to 16 (87.5% compression) via learned queries will retain sufficient visual information for action prediction, though with expected performance degradation compared to higher token counts (M=32/64/96)\", \"metrics\": {\"eval_action_loss\": 0.069, \"total_steps\": 100000, \"train_action_loss\": 0.058}, \"retry_count\": 0, \"spec\": {\"checkpoint_path\": \"checkpoints/smart_compress_m16/checkpoint.pt\", \"command\": \"CUDA_VISIBLE_DEVICES=3 HF_HOME=/root/autodl-tmp/.hf_cache HF_HUB_OFFLINE=1 WANDB_MODE=offline python -u train_smart_compress.py --config configs/smart_compress_m16.yaml --wandb_run smart_compress_m16\", \"data_count\": null, \"data_path\": \"/root/autodl-tmp/importance_margin_vla_compress/\", \"gpu\": 3, \"log_path\": \"train_M16.log\", \"model_name\": \"SmolVLM2-500M-Video-Instruct\", \"pid\": 352025, \"seed\": null, \"server\": \"cqa1-33015\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-18T04:16:03.747Z\"}, \"eval_smart_compress_m64\": {\"completed_at\": \"2026-05-18T02:55:42.732Z\", \"conclusion\": \"success\", \"created_at\": \"2026-05-18T01:30:45.305Z\", \"hypothesis\": \"Cross-attention pooling compression (128→64 tokens, 50% reduction) with learned queries will retain higher SR than M=32 on LIBERO-Object, establishing the compression-performance curve for soft compression. Expected SR higher than M=32 since more tokens are retained.\", \"metrics\": {\"overall_sr\": 0.616, \"per_task_sr\": {\"alphabet_soup\": 0.74, \"bbq_sauce\": 0.56, \"butter\": 0.84, \"chocolate_pudding\": 0.74, \"cream_cheese\": 0.38, \"ketchup\": 0.64, \"milk\": 0.62, \"orange_juice\": 0.46, \"salad_dressing\": 0.64, \"tomato_sauce\": 0.54}, \"total_episodes\": 500, \"total_successes\": 308, \"wilson_ci_95\": [0.573, 0.658]}, \"parent\": \"train_smart_compress_m64\", \"retry_count\": 0, \"spec\": {\"checkpoint_path\": \"checkpoints/smart_compress_m64/checkpoint.pt\", \"checkpoint_source\": \"train_smart_compress_m64\", \"command\": \"CUDA_VISIBLE_DEVICES=1 HF_HOME=/root/autodl-tmp/.hf_cache python eval_smart_compress_libero.py --checkpoint_path checkpoints/smart_compress_m64/checkpoint.pt --n_queries 64 --num_episodes 50 --suite libero_object --seed 42\", \"data_count\": 500, \"data_path\": \"LIBERO-Object (10 tasks x 50 eps)\", \"eval_data\": \"LIBERO-Object\", \"gpu\": \"cuda:1\", \"log_path\": \"eval_m64_50ep.log\", \"model_name\": \"SmolVLA + SmartCompressWrapper (M=64)\", \"pid\": 542036, \"seed\": 42, \"server\": \"cqa1-33015\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-18T02:55:42.732Z\"}, \"eval_smart_compress_m32\": {\"completed_at\": \"2026-05-18T02:55:41.591Z\", \"conclusion\": \"success\", \"created_at\": \"2026-05-18T01:30:43.772Z\", \"hypothesis\": \"Cross-attention pooling compression (128→32 tokens, 75% reduction) with learned queries will retain non-zero SR on LIBERO-Object, proving soft compression bypasses the cliff-edge that all hard pruning methods hit. SR > 0% at 75% compression = fundamental difference vs hard pruning.\", \"metrics\": {\"overall_sr\": 0.616, \"per_task_sr\": {\"alphabet_soup\": 0.68, \"bbq_sauce\": 0.46, \"butter\": 0.82, \"chocolate_pudding\": 0.9, \"cream_cheese\": 0.64, \"ketchup\": 0.66, \"milk\": 0.76, \"orange_juice\": 0.28, \"salad_dressing\": 0.6, \"tomato_sauce\": 0.36}, \"total_episodes\": 500, \"total_successes\": 308, \"wilson_ci_95\": [0.573, 0.658]}, \"parent\": \"train_smart_compress_m32\", \"retry_count\": 0, \"spec\": {\"checkpoint_path\": \"checkpoints/smart_compress_m32/checkpoint.pt\", \"checkpoint_source\": \"train_smart_compress_m32\", \"command\": \"CUDA_VISIBLE_DEVICES=0 HF_HOME=/root/autodl-tmp/.hf_cache python eval_smart_compress_libero.py --checkpoint_path checkpoints/smart_compress_m32/checkpoint.pt --n_queries 32 --num_episodes 50 --suite libero_object --seed 42\", \"data_count\": 500, \"data_path\": \"LIBERO-Object (10 tasks x 50 eps)\", \"eval_data\": \"LIBERO-Object\", \"gpu\": \"cuda:0\", \"log_path\": \"eval_m32_50ep.log\", \"model_name\": \"SmolVLA + SmartCompressWrapper (M=32)\", \"pid\": 541184, \"seed\": 42, \"server\": \"cqa1-33015\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-18T02:55:41.591Z\"}, \"train_smart_compress_m32\": {\"completed_at\": \"2026-05-18T00:47:34.304Z\", \"conclusion\": \"success\", \"created_at\": \"2026-05-17T17:40:16.346Z\", \"extra\": {\"hook_events\": [{\"action\": \"agent\", \"event\": \"on_failed\", \"ts\": \"2026-05-18T00:47:40.279707+00:00\"}]}, \"failure_reason\": \"process dead 5× with no sentinel/W&B — auto-resolved as failed\", \"hypothesis\": \"Cross-attention pooling compression (128→32 tokens, 75% reduction) with learned queries preserves action prediction quality by soft-fusing all token information rather than hard-deleting. This is the most aggressive compression ratio — if SR remains non-zero at 75% token reduction, it proves soft compression fundamentally differs from hard pruning.\", \"metrics\": {\"checkpoint\": \"checkpoints/smart_compress_m32/checkpoint.pt\", \"checkpoint_size_gb\": 1.5, \"eval_action_loss\": 0.052, \"speed_sps\": 4.1, \"total_steps\": 100000, \"train_action_loss\": 0.11, \"training_duration_h\": 6.5}, \"notes\": \"Training completed successfully (100K steps, 99999/100000). Cron 误判为 failed（nohup 启动无 sentinel）。实际正常完成，checkpoint 已保存。首次 eval (PID 363256, eval_success_rate_libero.py) 使用错误脚本，Task 0 全 FAIL，已 kill。需要用 eval_smart_compress.py 重新 eval。\", \"parent\": \"eval_geometric_prior_k05\", \"reproduce\": {\"finished_at\": \"2026-05-18T00:47:33.287Z\"}, \"retry_count\": 0, \"spec\": {\"checkpoint_source\": \"/root/autodl-tmp/libero_full_ft/step_099999/checkpoint.pt\", \"command\": \"nohup python -u train_smart_compress.py --config configs/smart_compress.yaml > train_M32.log 2>&1 &\", \"data_count\": 130, \"data_path\": \"HuggingFaceVLA/libero (130 task demos)\", \"eval_data\": \"N/A (training experiment)\", \"model_name\": \"smolvla-smart-compress-m32\", \"seed\": 42, \"server\": \"cqa1-33015\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-18T01:16:42.593Z\"}, \"train_smart_compress_m64\": {\"completed_at\": \"2026-05-18T00:47:11.864Z\", \"conclusion\": \"success\", \"created_at\": \"2026-05-17T17:38:49.443Z\", \"extra\": {\"hook_events\": [{\"action\": \"agent\", \"event\": \"on_failed\", \"ts\": \"2026-05-18T00:47:15.252424+00:00\"}]}, \"failure_reason\": \"process dead 5× with no sentinel/W&B — auto-resolved as failed\", \"hypothesis\": \"Cross-attention pooling compression (128→64 tokens, 50% reduction) with learned queries preserves action prediction quality by soft-fusing all token information rather than hard-deleting. If SR remains non-zero, it proves soft compression can bypass the cliff-edge that all hard pruning methods hit at any ratio.\", \"metrics\": {\"checkpoint\": \"checkpoints/smart_compress_m64/checkpoint.pt\", \"checkpoint_size_gb\": 1.5, \"eval_action_loss\": 0.062, \"speed_sps\": 4.1, \"total_steps\": 100000, \"train_action_loss\": 0.045, \"training_duration_h\": 6.5}, \"notes\": \"Training completed successfully (100K steps, 99999/100000). Cron 误判为 failed（nohup 启动无 sentinel）。实际正常完成，checkpoint 已保存。首次 eval (PID 364255, eval_success_rate_libero.py) 使用错误脚本，Task 0 全 FAIL，已 kill。需要用 eval_smart_compress.py 重新 eval。\", \"parent\": \"eval_geometric_prior_k05\", \"reproduce\": {\"finished_at\": \"2026-05-18T00:47:10.396Z\"}, \"retry_count\": 0, \"spec\": {\"checkpoint_source\": \"/root/autodl-tmp/libero_full_ft/step_099999/checkpoint.pt\", \"command\": \"nohup python -u train_smart_compress.py --config configs/smart_compress_m64.yaml > train_M64.log 2>&1 &\", \"data_count\": 130, \"data_path\": \"HuggingFaceVLA/libero (130 task demos)\", \"eval_data\": \"N/A (training experiment)\", \"model_name\": \"smolvla-smart-compress-m64\", \"seed\": 42, \"server\": \"cqa1-33015\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-18T01:16:41.169Z\"}, \"libero_full_ft_baseline\": {\"checkpoint_path\": \"checkpoints/libero_full_ft/step_099999/checkpoint.pt\", \"completed_at\": \"2026-05-18T00:59:00.156Z\", \"conclusion\": \"success\", \"created_at\": \"2026-05-16T14:20:17.482Z\", \"extra\": {\"hook_events\": [{\"action\": \"agent\", \"event\": \"on_complete\", \"ts\": \"2026-05-16T21:26:39.366417+00:00\"}]}, \"hypothesis\": \"Full expert fine-tuning of SmolVLA (22.2% params trainable, 99.9M/450M) on LIBERO data for 100K steps with cosine LR decay should achieve reasonable manipulation SR as a baseline for compression experiments\", \"log_path\": \"~/runs/importance_margin_vla_compress/libero_full_ft_baseline.log\", \"metrics\": {\"diversity_10k\": {\"noise_diversity_std\": 0.1987, \"pass\": true, \"per_obs\": [0.193, 0.192, 0.203, 0.193, 0.213], \"threshold\": 0.05}, \"sr_100k_goal\": {\"n_episodes\": 100, \"overall\": 0.63, \"per_task\": [0.5, 0.9, 0.7, 0.3, 1, 0.4, 0.4, 1, 0.8, 0.3], \"suite\": \"libero_goal\"}, \"sr_100k_object\": {\"n_episodes\": 100, \"overall\": 0.36, \"per_task\": [0, 0.3, 0.4, 0.6, 0.5, 0.1, 0.3, 0.5, 0.4, 0.5], \"suite\": \"libero_object\"}, \"sr_100k_overall\": 0.49, \"sr_100k_spatial\": {\"n_episodes\": 100, \"overall\": 0.48, \"per_task\": [0.8, 0.5, 0.4, 0.4, 0.3, 0.3, 0.6, 0.2, 0.9, 0.4], \"suite\": \"libero_spatial\"}, \"sr_50k\": {\"n_episodes\": 100, \"overall\": 0.33, \"per_task\": [0.1, 0.7, 0.5, 0.1, 0.3, 0.1, 0.5, 0.1, 0.4, 0.5], \"suite\": \"libero_object\", \"wilson_ci_95\": [0.246, 0.427]}, \"sr_50k_goal\": {\"n_episodes\": 100, \"overall\": 0.42, \"per_task\": [0.2, 0.7, 0.5, 0.1, 0.6, 0.5, 0.2, 0.8, 0.5, 0.1], \"suite\": \"libero_goal\", \"wilson_ci_95\": [0.328, 0.518]}, \"sr_50k_spatial\": {\"n_episodes\": 100, \"overall\": 0.34, \"per_task\": [0.8, 0.1, 0.3, 0.2, 0.2, 0.4, 0.3, 0.2, 0.6, 0.3], \"suite\": \"libero_spatial\", \"wilson_ci_95\": [0.255, 0.437]}}, \"notes\": \"100K training completed. Final: loss=0.04082, eval_loss=0.07811, lr=2.50e-06. Eval SR@100K: object=36%, spatial=48%, goal=63%, overall=49.0%. Improved from 50K (36.3%) by +12.7pp. Below 50% threshold but strong upward trend. Seed0 training in progress on cuda:3.\", \"parent\": \"libero_lora_baseline\", \"reproduce\": {\"finished_at\": \"2026-05-16T21:26:33.907Z\"}, \"retry_count\": 0, \"spec\": {\"account\": \"root\", \"backend\": \"tmux\", \"command\": \"python train.py --config configs/libero_full_ft.yaml\", \"data_count\": 273465, \"data_path\": \"HuggingFaceVLA/libero\", \"gpu\": [\"cuda:0\"], \"gpu_hours\": 34.65, \"log_path\": \"~/runs/importance_margin_vla_compress/libero_full_ft_baseline.log\", \"model_name\": \"smolvla_base_full_ft\", \"pid\": \"8985\", \"seed\": 42, \"server\": \"cqa1-33015\", \"submitted_at\": \"2026-05-16T14:20:17.428Z\", \"submitted_via\": \"submit_training_job\", \"wall_clock_seconds\": 124722.7}, \"status\": \"DONE\", \"updated_at\": \"2026-05-18T00:59:00.156Z\"}, \"train_acis_stage1only_k03\": {\"completed_at\": \"2026-05-17T07:40:00.078Z\", \"conclusion\": \"failed\", \"created_at\": \"2026-05-17T07:12:38.108Z\", \"extra\": {\"hook_events\": [{\"action\": \"agent\", \"event\": \"on_failed\", \"ts\": \"2026-05-17T07:40:03.011796+00:00\"}], \"previous_failure\": {\"conclusion\": \"failed\", \"notes\": \"Cron误报退出。进程实际仍在运行(PID 11343, GPU 3)。当前实例启动于15:16 UTC(可能是重启的)，step 2000/10000, margin_loss~0.18, sps=4.3。预计~15:56 UTC完成。\"}}, \"failure_reason\": \"process dead 5× with no sentinel/W&B — auto-resolved as failed\", \"hypothesis\": \"Stage1-only ACIS (k=0.3, 保留 30% tokens) 训练。验证激进压缩的性能下界——如果 SR > 20% 则证明 ACIS 即使在 70% pruning 下仍有价值。\", \"notes\": \"⚠️ INVALIDATED: 下游 eval (libero_object_acis_k03_prune.json) 的 45% SR 是 bug — hook 维度 guard (64≠128) 未触发，pruning 从未执行。与 eval_stage1_only (k=0.5, 44.8% SR) 同一 bug。实际 pruning 后预期 0% SR（所有其他 k ratio 修复后均为 0%）。此实验结果不可引用。\", \"reproduce\": {\"finished_at\": \"2026-05-17T07:39:58.151Z\"}, \"retry_count\": 1, \"spec\": {\"checkpoint_path\": \"/root/autodl-tmp/importance_margin_vla_compress/checkpoints/libero_acis_stage1only_k03/stage1_done/checkpoint.pt\", \"command\": \"python train_twostage.py --config configs/libero_acis_stage1only_k03.yaml --gpu 0\", \"data_count\": \"10K steps\", \"data_path\": \"HuggingFaceVLA/libero\", \"log_path\": \"/root/autodl-tmp/importance_margin_vla_compress/wandb/offline-run-20260517_151658-eqy9eh8c/\", \"model_name\": \"SmolVLA ACIS Stage1-only k=0.3\", \"seed\": 42, \"server\": \"cqa1-33015\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-18T00:33:33.269Z\"}, \"eval_openvla_pruning_k05\": {\"completed_at\": \"2026-05-18T00:07:22.914Z\", \"conclusion\": \"success\", \"created_at\": \"2026-05-17T19:49:18.253Z\", \"hypothesis\": \"OpenVLA (7B) with random k=0.5 true_removal pruning on LIBERO-Object. Baseline=74%. Early signal Task 1: 7/10=70% (vs baseline 78%), suggesting graceful degradation rather than cliff-edge. If confirmed across all 10 tasks, proves model scale provides pruning robustness absent in SmolVLA (0.5B).\", \"parent\": \"eval_openvla_crossmodel_pruning\", \"retry_count\": 0, \"spec\": {\"checkpoint_path\": \"N/A (eval only)\", \"checkpoint_source\": \"/root/autodl-tmp/openvla-libero-object\", \"command\": \"python -u eval_openvla_libero.py --mode random_prune --k_ratio 0.5 --suite libero_object --num_episodes 50 --seed 7\", \"data_count\": 500, \"data_path\": \"/root/autodl-tmp/libero/libero_object\", \"eval_data\": \"libero_object_10tasks_50eps\", \"log_path\": \"/root/autodl-tmp/importance_margin_vla_compress/eval_results/openvla_random_prune_k05_object.log\", \"metrics\": {\"baseline_sr\": 0.74, \"k_ratio\": 0.5, \"overall_sr\": 0.374, \"per_task_sr\": {\"alphabet_soup\": 0.6, \"bbq_sauce\": 0.44, \"butter\": 0.02, \"chocolate_pudding\": 0.4, \"cream_cheese\": 0.08, \"ketchup\": 0.5, \"milk\": 0.24, \"orange_juice\": 0.72, \"salad_dressing\": 0.36, \"tomato_sauce\": 0.38}, \"pruning_method\": \"random_true_removal\", \"relative_drop_pct\": 49.5, \"total_episodes\": 500, \"total_successes\": 187}, \"model_name\": \"openvla-7b-libero-object\", \"seed\": 7, \"server\": \"westd-27271\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-18T00:07:22.914Z\"}, \"geometric_prior_k05_eval\": {\"completed_at\": \"2026-05-17T20:45:53.973Z\", \"conclusion\": \"negative\", \"created_at\": \"2026-05-17T16:26:30.314Z\", \"hypothesis\": \"Geometric prior pruning (Sobel edge scoring) at k=0.5 will fail catastrophically on SmolVLA LIBERO-Object, demonstrating that naive heuristic-based token removal causes cliff-edge degradation even though ACIS-based learned pruning maintains performance at the same ratio.\", \"retry_count\": 0, \"spec\": {\"checkpoint_path\": \"N/A (eval only)\", \"checkpoint_source\": \"checkpoints/libero_full_ft/step_099999/checkpoint.pt\", \"command\": \"CUDA_VISIBLE_DEVICES=1 PYTHONUNBUFFERED=1 python eval_geometric_prior_k05.py\", \"data_count\": 500, \"data_path\": \"/root/autodl-tmp/importance_margin_vla_compress/checkpoints/libero_full_ft/step_099999/checkpoint.pt\", \"eval_data\": \"libero_object 10 tasks x 50 eps\", \"log_path\": \"/root/autodl-tmp/importance_margin_vla_compress/eval_geometric_prior_k05.log\", \"metrics\": {\"early_stopped\": true, \"k_ratio\": 0.5, \"overall_sr\": 0, \"pruning_method\": \"geometric_prior_sobel\", \"total_episodes\": 181}, \"model_name\": \"SmolVLA full_ft\", \"seed\": 42, \"server\": \"cqa1-33015\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-17T20:45:53.973Z\"}, \"eval_openvla_crossmodel_pruning\": {\"completed_at\": \"2026-05-17T19:48:47.840Z\", \"conclusion\": \"success\", \"created_at\": \"2026-05-17T16:02:43.205Z\", \"extra\": {\"hook_events\": [{\"action\": \"agent\", \"event\": \"on_failed\", \"ts\": \"2026-05-17T19:48:53.562662+00:00\"}]}, \"failure_reason\": \"process dead 5× with no sentinel/W&B — auto-resolved as failed\", \"hypothesis\": \"OpenVLA (7B params) with random k=0.5 true_removal pruning on LIBERO-Object will also show cliff-edge collapse (0% SR), confirming the phenomenon is universal across VLA architectures and not SmolVLA-specific. If OpenVLA degrades gracefully, it suggests model scale or architecture differences provide robustness to token pruning.\", \"notes\": \"Cron 误判为 failed（监控旧 PID 643978 而非实际 pruning PID 697608）。Baseline 已完成: 74.0% SR (370/500)。Pruning 条件在新实验 eval_openvla_pruning_k05 中跟踪。\", \"parent\": \"baseline_bypass_object\", \"reproduce\": {\"finished_at\": \"2026-05-17T19:48:46.829Z\"}, \"retry_count\": 0, \"spec\": {\"checkpoint_source\": \"/root/autodl-tmp/openvla-libero-object\", \"command\": \"python eval_openvla_libero.py --model_path /root/autodl-tmp/openvla-libero-object --suite libero_object --episodes 50 --conditions baseline,random_prune_k05\", \"data_count\": 500, \"data_path\": \"/root/autodl-tmp/libero/libero_object\", \"eval_data\": \"libero_object_10tasks_50eps\", \"model_name\": \"openvla-7b-libero-object\", \"seed\": 42, \"server\": \"westd-27271\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-17T19:49:13.985Z\"}, \"eval_geometric_prior_k09\": {\"completed_at\": \"2026-05-17T16:49:34.037Z\", \"conclusion\": \"negative\", \"created_at\": \"2026-05-17T16:48:51.853Z\", \"hypothesis\": \"Geometric prior pruning (Sobel edge) with k=0.9 (keep 90% tokens, remove only ~13/128) on SmolVLA LIBERO-Object. Most conservative pruning ratio. If 0%, definitively proves pixel_shuffle pre-compression makes inference-time token pruning infeasible regardless of selection strategy.\", \"parent\": \"eval_geometric_prior_k07\", \"retry_count\": 0, \"spec\": {\"checkpoint_path\": \"N/A (eval only)\", \"checkpoint_source\": \"/root/autodl-tmp/libero_full_ft/step_099999/checkpoint.pt\", \"command\": \"python eval_geometric_prior.py --k_ratio 0.9 --suite libero_object --episodes 50\", \"data_count\": 500, \"data_path\": \"/root/autodl-tmp/libero/libero_object\", \"eval_data\": \"libero_object_10tasks_50eps\", \"log_path\": \"/root/autodl-tmp/eval_results/eval_geometric_prior_k09.log\", \"metrics\": {\"early_stopped\": true, \"k_ratio\": 0.9, \"overall_sr\": 0, \"pruning_method\": \"geometric_prior_sobel\", \"total_episodes\": 239, \"wilson_ci_95_upper\": 0.016}, \"model_name\": \"smolvla-full-ft-step099999\", \"seed\": 42, \"server\": \"cqa1-33015\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-17T16:49:34.037Z\"}, \"eval_geometric_prior_k07\": {\"completed_at\": \"2026-05-17T16:49:01.514Z\", \"conclusion\": \"negative\", \"created_at\": \"2026-05-17T16:28:43.832Z\", \"hypothesis\": \"Geometric prior pruning (Sobel edge) with k=0.7 (keep 70% tokens) on SmolVLA LIBERO-Object. Higher retention ratio than k=0.5 might allow partial performance recovery if the cliff-edge has a threshold. If still 0%, narrows the feasibility window further.\", \"parent\": \"eval_geometric_prior_k05\", \"retry_count\": 0, \"spec\": {\"checkpoint_path\": \"N/A (eval only)\", \"checkpoint_source\": \"/root/autodl-tmp/libero_full_ft/step_099999/checkpoint.pt\", \"command\": \"python eval_geometric_prior.py --k_ratio 0.7 --suite libero_object --episodes 50\", \"data_count\": 500, \"data_path\": \"/root/autodl-tmp/libero/libero_object\", \"eval_data\": \"libero_object_10tasks_50eps\", \"log_path\": \"/root/autodl-tmp/eval_results/eval_geometric_prior_k07.log\", \"metrics\": {\"early_stopped\": true, \"k_ratio\": 0.7, \"overall_sr\": 0, \"pruning_method\": \"geometric_prior_sobel\", \"total_episodes\": 240, \"wilson_ci_95_upper\": 0.016}, \"model_name\": \"smolvla-full-ft-step099999\", \"seed\": 42, \"server\": \"cqa1-33015\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-17T16:49:01.514Z\"}, \"eval_geometric_prior_k05\": {\"completed_at\": \"2026-05-17T16:49:00.282Z\", \"conclusion\": \"negative\", \"created_at\": \"2026-05-17T16:27:59.058Z\", \"hypothesis\": \"Geometric prior pruning (Sobel edge detection → keep tokens at object boundaries) with k=0.5 on SmolVLA LIBERO-Object. If spatially-aware token selection outperforms random/ACIS pruning, it demonstrates that informed pruning can bypass the cliff-edge. If still 0%, confirms pixel_shuffle pre-compression makes any inference-time pruning infeasible.\", \"parent\": \"baseline_bypass_object\", \"retry_count\": 0, \"spec\": {\"checkpoint_path\": \"N/A (eval only)\", \"checkpoint_source\": \"/root/autodl-tmp/libero_full_ft/step_099999/checkpoint.pt\", \"command\": \"python eval_geometric_prior_k05.py --k_ratio 0.5 --suite libero_object --episodes 50\", \"data_count\": 500, \"data_path\": \"/root/autodl-tmp/libero/libero_object\", \"eval_data\": \"libero_object_10tasks_50eps\", \"log_path\": \"/root/autodl-tmp/eval_results/eval_geometric_prior_k05.log\", \"metrics\": {\"early_stopped\": true, \"k_ratio\": 0.5, \"overall_sr\": 0, \"pruning_method\": \"geometric_prior_sobel\", \"total_episodes\": 181, \"wilson_ci_95_upper\": 0.021}, \"model_name\": \"smolvla-full-ft-step099999\", \"seed\": 42, \"server\": \"cqa1-33015\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-17T16:49:00.281Z\"}, \"libero_fullft_batch64_v2\": {\"completed_at\": \"2026-05-17T14:36:51.484Z\", \"conclusion\": \"killed\", \"created_at\": \"2026-05-17T06:52:36.433Z\", \"extra\": {\"hook_events\": [{\"action\": \"agent\", \"event\": \"on_failed\", \"ts\": \"2026-05-17T08:10:34.525154+00:00\"}, {\"action\": \"agent\", \"event\": \"on_failed\", \"ts\": \"2026-05-17T14:35:15.988773+00:00\"}]}, \"failure_reason\": \"EXIT_CODE=137 (SIGKILL — OOM killer or manual kill)\", \"hypothesis\": \"Increasing effective batch size from 4 to 64 (via gradient accumulation 16x) improves training stability and final performance for SmolVLA full expert fine-tuning on LIBERO, as larger batches provide more stable gradient estimates for the action expert parameters.\", \"notes\": \"D066: Director 指令 kill。ETA 23天远超 CoRL DDL (12天)，0.1 sps 无价值。释放 cqa1:0 给 Pi0.5 cross-model validation。Step ~2000/100K at kill time. EXIT_CODE=137 (SIGKILL). Cron confirmed process exit 2026-05-17T14:35Z.\", \"parent\": \"\", \"reproduce\": {\"finished_at\": \"2026-05-17T14:35:04.309Z\"}, \"retry_count\": 0, \"spec\": {\"checkpoint_path\": \"none\", \"command\": \"killed before meaningful progress\", \"log_path\": \"~/runs/importance_margin_vla_compress/train_fullft_batch64_v2.log\", \"server\": \"cqa1-33015\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-17T14:36:51.484Z\"}, \"baseline_bypass_object\": {\"completed_at\": \"2026-05-17T14:25:15.378Z\", \"conclusion\": \"success\", \"created_at\": \"2026-05-17T14:24:41.442Z\", \"hypothesis\": \"Stage1-only checkpoint in bypass mode (k=1.0, no pruning) should reproduce the baseline SR of 44.8% on libero_object, establishing the clean unpruned reference for Table 1 cliff-edge comparison.\", \"metrics\": {\"checkpoint_matches_object_eval\": true, \"k_ratio\": 1, \"mode\": \"bypass\", \"overall_sr\": 0.448, \"per_task_sr\": [0.22, 0.6, 0.42, 0.38, 0.58, 0.26, 0.62, 0.38, 0.5, 0.52], \"total_episodes\": 500, \"total_successes\": 224, \"wilson_ci_95\": [0.405, 0.492]}, \"parent\": \"eval_stage1only_object_v2_fixed\", \"retry_count\": 0, \"spec\": {\"checkpoint_path\": \"checkpoints/libero_imm_twostage_fullft/stage1_done/checkpoint.pt\", \"checkpoint_source\": \"checkpoints/libero_imm_twostage_fullft/stage1_done/checkpoint.pt\", \"command\": \"python eval_libero.py --suite libero_object --mode bypass --checkpoint checkpoints/libero_imm_twostage_fullft/stage1_done/checkpoint.pt --episodes 50\", \"data_count\": 500, \"data_path\": \"libero_object\", \"eval_data\": \"libero_object\", \"log_path\": \"eval_results/baseline_bypass_object.json\", \"model_name\": \"SmolVLA+ACIS_stage1_bypass\", \"seed\": 42, \"server\": \"westd-27271\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-17T14:25:17.585Z\"}, \"action_divergence_v2_clean\": {\"completed_at\": \"2026-05-17T13:13:46.694Z\", \"conclusion\": \"success\", \"created_at\": \"2026-05-17T12:04:33.765Z\", \"hypothesis\": \"Closed-loop action divergence: bypass vs ACIS k=0.5 true-removal 在 sim rollout 中的逐步轨迹偏离。与 offline single-step error (111.5% relative) 互为补充——offline 证明每步误差大，closed-loop 展示实际轨迹如何快速分叉。\", \"metrics\": {\"action_l2_mean\": 1.117, \"action_l2_median\": 0.85, \"bypass_early_terminations\": \"multiple\", \"divergence_onset_step\": 0, \"eef_position_l2_mean_m\": 0.214, \"eef_position_l2_median_m\": 0.214, \"first_10_steps_action_l2\": 1.262, \"first_10_steps_eef_l2_m\": 0.041, \"last_10_steps_action_l2\": 0.759, \"last_10_steps_eef_l2_m\": 0.198, \"max_steps\": 300, \"n_episodes_per_task\": 10, \"n_tasks\": 3, \"pattern\": \"immediate_onset_monotonic_growth\", \"pruned_early_terminations\": 0}, \"retry_count\": 0, \"spec\": {\"checkpoint_path\": \"checkpoints/acis_stage1only_k05/stage1_done/checkpoint.pt\", \"checkpoint_source\": \"checkpoints/acis_stage1only_k05/stage1_done/checkpoint.pt\", \"command\": \"python closedloop_action_divergence.py --num_tasks 3 --episodes_per_task 10 --max_steps 300\", \"data_count\": 30, \"data_path\": \"libero_object\", \"eval_data\": \"libero_object\", \"log_path\": \"eval_results/action_divergence_closedloop.json\", \"model_name\": \"SmolVLA+ACIS_stage1only_k05\", \"seed\": 42, \"server\": \"westd-27271\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-17T13:13:50.571Z\"}, \"eval_goal_prune_k05\": {\"completed_at\": \"2026-05-17T12:54:41.532Z\", \"conclusion\": \"success\", \"created_at\": \"2026-05-17T12:04:37.802Z\", \"hypothesis\": \"ACIS k=0.5 true_removal 在 libero_goal suite 上的 SR。验证 cliff-edge 效应是否跨全部 3 个 LIBERO suite (Object/Spatial/Goal) 一致。Goal baseline=63%, Object/Spatial 已确认 0%。\", \"metrics\": {\"all_tasks_zero\": true, \"baseline_sr\": 0.63, \"k_ratio\": 0.5, \"mode\": \"acis_prune\", \"overall_sr\": 0, \"pruning_method\": \"true_removal\", \"sr_drop\": -0.63, \"suite\": \"libero_goal\", \"total_episodes\": 500, \"total_successes\": 0, \"wilson_ci_95\": [0, 0.0076]}, \"notes\": \"0% SR across all 10 goal tasks (0/500 episodes). Confirms cliff-edge across all 3 LIBERO suites (Object=0%, Spatial=0%, Goal=0%). Baseline goal SR=63%. Results: eval_results/eval_goal_prune_k05.json\", \"parent\": \"eval_spatial_prune_k05\", \"retry_count\": 0, \"spec\": {\"checkpoint_path\": \"checkpoints/acis_stage1only_k05/stage1_done/checkpoint.pt\", \"checkpoint_source\": \"checkpoints/acis_stage1only_k05/stage1_done/checkpoint.pt\", \"command\": \"python eval_libero.py --suite libero_goal --mode acis_prune --k_ratio 0.5 --pruning_method true_removal --checkpoint checkpoints/acis_stage1only_k05/stage1_done/checkpoint.pt --episodes 50\", \"data_count\": 500, \"data_path\": \"libero_goal\", \"eval_data\": \"libero_goal\", \"log_path\": \"eval_results/eval_goal_prune_k05.json\", \"model_name\": \"SmolVLA+ACIS_stage1only_k05\", \"seed\": 42, \"server\": \"westd-27271\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-17T12:54:41.532Z\"}, \"offline_singlestep_action_error\": {\"completed_at\": \"2026-05-17T12:02:11.341Z\", \"conclusion\": \"success\", \"created_at\": \"2026-05-17T11:36:40.871Z\", \"hypothesis\": \"Offline single-step action error analysis: 区分 pruning 导致的 per-step error 是小误差通过 compounding 放大（per-step L2 < 10% action norm → compounding 叙事），还是 pruning 直接摧毁 action prediction（per-step L2 很大 → pruning 本身就 catastrophic）。这是论文 mechanistic explanation 的关键证据。\", \"metrics\": {\"bypass_vs_gt_l2_mean\": 0.414, \"bypass_vs_pruned_l2_mean\": 1.284, \"conclusion_type\": \"large_per_step_error\", \"interpretation\": \"Pruning directly destroys action prediction at each step. Not a compounding issue.\", \"n_steps\": 200, \"per_dim_gripper\": 1.02, \"per_dim_position_xyz\": [0.2, 0.25, 0.3], \"per_dim_rotation_xyz\": [0.01, 0.02, 0.01], \"pruned_vs_gt_l2_mean\": 1.391, \"relative_error_pct\": 111.5}, \"parent\": \"eval_true_removal_k05\", \"retry_count\": 0, \"spec\": {\"checkpoint_path\": \"checkpoints/libero_full_ft_100k/checkpoint.pt\", \"checkpoint_source\": \"libero_full_ft_baseline (100K)\", \"command\": \"python offline_singlestep_error.py\", \"data_count\": 200, \"data_path\": \"LIBERO demo dataset (libero_object)\", \"eval_data\": \"LIBERO demo observations (200 steps from libero_object)\", \"log_path\": \"eval_results/offline_singlestep_error.json\", \"model_name\": \"SmolVLA Stage1-only (Full FT + ACIS k=0.5)\", \"seed\": 42, \"server\": \"westd-27271\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-17T12:02:11.341Z\"}, \"offline_singlestep_error_k05\": {\"checkpoint_path\": \"checkpoints/libero_imm_twostage_fullft/stage1_done/checkpoint.pt\", \"completed_at\": \"2026-05-17T11:56:46.173Z\", \"conclusion\": \"success\", \"created_at\": \"2026-05-17T11:55:59.152Z\", \"hypothesis\": \"ACIS k=0.5 true_removal pruning causes large per-step action errors (not small compounding errors) because removing 50% of visual tokens fundamentally disrupts the attention pattern the expert relies on for action prediction, especially for discrete actions like gripper.\", \"log_path\": \"eval_results/offline_singlestep_error.json\", \"retry_count\": 0, \"spec\": {\"checkpoint_source\": \"checkpoints/libero_imm_twostage_fullft/stage1_done/checkpoint.pt\", \"command\": \"python offline_singlestep_error.py\", \"data_count\": 200, \"data_path\": \"HuggingFaceVLA/libero\", \"eval_data\": \"libero episodes 0,1\", \"model_name\": \"smolvla_imm_twostage_fullft_k05\", \"seed\": 42, \"server\": \"westd-27271\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-17T11:56:46.173Z\"}, \"eval_spatial_prune_k05\": {\"checkpoint_path\": \"checkpoints/libero_acis_stage1only_k03/stage1_done/checkpoint.pt\", \"completed_at\": \"2026-05-17T11:39:31.186Z\", \"conclusion\": \"success\", \"created_at\": \"2026-05-17T10:43:21.844Z\", \"hypothesis\": \"ACIS k=0.5 true_removal pruning on libero_spatial will show the same cliff-edge collapse (0% SR) as observed on libero_object, confirming that removing ACIS-identified important tokens destroys policy capability across different task suites.\", \"log_path\": \"eval_results/eval_spatial_prune_k05.log\", \"metrics\": {\"all_tasks_zero\": true, \"baseline_sr\": 0.518, \"mode\": \"acis_prune\", \"overall_sr\": 0, \"pruning_method\": \"true_removal\", \"sr_drop\": -0.518, \"suite\": \"libero_spatial\", \"total_episodes\": 500, \"total_successes\": 0, \"wilson_ci_95\": [0, 0.0076]}, \"notes\": \"Completed normally at 2026-05-17 19:35. 0% SR across all 10 spatial tasks (0/500 episodes). Confirms cliff-edge generalizes from object to spatial suite. Log: eval_results/eval_spatial_prune_k05.log, Results: eval_results/eval_spatial_prune_k05.json\", \"parent\": \"eval_true_removal_k05\", \"retry_count\": 0, \"spec\": {\"checkpoint_source\": \"libero_acis_stage1only_k03\", \"command\": \"python eval_success_rate_libero.py --checkpoint checkpoints/libero_acis_stage1only_k03/stage1_done/checkpoint.pt --suite spatial --k_ratio 0.5 --pruning_method true_removal --num_episodes 50 --gpu 0\", \"data_count\": 500, \"data_path\": \"libero_spatial\", \"eval_data\": \"LIBERO-Spatial (10 tasks x 50 episodes)\", \"gpu\": \"1\", \"model_name\": \"SmolVLA-ACIS-Stage1Only-k03\", \"seed\": 0, \"server\": \"westd-27271\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-17T11:39:31.186Z\"}, \"eval_merge_k05\": {\"checkpoint_path\": \"checkpoints/libero_acis_stage1only_k07/stage1_done/checkpoint.pt\", \"completed_at\": \"2026-05-17T10:34:55.451Z\", \"conclusion\": \"negative\", \"created_at\": \"2026-05-17T10:03:09.100Z\", \"hypothesis\": \"Token merging（将 pruned token 信息加权合并到保留 token）比 zero-masking 和 true-removal 更好地保留信息，可能恢复部分推理能力。如果 merge SR > 0%，说明信息丢失（而非序列长度变化）是 pruning 崩溃的主因\", \"log_path\": \"eval_results/eval_merge_k05.log\", \"metrics\": {\"episodes\": 500, \"k_ratio\": 0.5, \"libero_object_sr\": 0, \"merge_alpha\": 1, \"pruning_method\": \"merge\", \"pruning_type\": \"acis\", \"wilson_ci_95\": \"[0.0%, 0.76%]\"}, \"parent\": \"eval_true_removal_k05\", \"retry_count\": 0, \"spec\": {\"checkpoint_source\": \"libero_acis_stage1only_k07\", \"command\": \"python eval_success_rate_libero.py --checkpoint checkpoints/libero_acis_stage1only_k07/stage1_done/checkpoint.pt --suite object --k_ratio 0.5 --pruning_method merge --merge_alpha 1.0 --num_episodes 50 --gpu 0\", \"data_count\": 500, \"data_path\": \"libero_object\", \"eval_data\": \"LIBERO-Object (10 tasks x 50 episodes)\", \"gpu\": \"0\", \"model_name\": \"SmolVLA-ACIS-Stage1Only-k07\", \"seed\": 0, \"server\": \"westd-27271\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-17T10:34:55.451Z\"}, \"eval_k07_zero_mask\": {\"checkpoint_path\": \"checkpoints/libero_acis_stage1only_k07/stage1_done/checkpoint.pt\", \"completed_at\": \"2026-05-17T10:26:56.534Z\", \"conclusion\": \"negative\", \"created_at\": \"2026-05-17T10:03:12.588Z\", \"hypothesis\": \"Stage1-only ACIS k=0.7（保留 70% tokens）zero-mask pruning 的 SR。k=0.9 已确认 0%，k=0.7 预期也是 0%。作为完整 pruning ratio ablation 数据用于论文\", \"log_path\": \"eval_results/eval_k07_zero_mask.log\", \"metrics\": {\"episodes\": 500, \"k_ratio\": 0.7, \"libero_object_sr\": 0, \"pruning_method\": \"zero_mask\", \"pruning_type\": \"acis\", \"wilson_ci_95\": \"[0.0%, 0.76%]\"}, \"parent\": \"eval_stage1only_k09\", \"retry_count\": 0, \"spec\": {\"checkpoint_source\": \"libero_acis_stage1only_k07\", \"command\": \"python eval_success_rate_libero.py --checkpoint checkpoints/libero_acis_stage1only_k07/stage1_done/checkpoint.pt --suite libero_object --mode acis_prune --pruning-method zero_mask --num_episodes 50 --gpu 0\", \"data_count\": 500, \"data_path\": \"libero_object\", \"eval_data\": \"LIBERO-Object (10 tasks x 50 episodes)\", \"gpu\": \"1\", \"model_name\": \"SmolVLA-ACIS-Stage1Only-k07\", \"seed\": 0, \"server\": \"westd-27271\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-17T10:26:56.534Z\"}, \"eval_true_removal_k05\": {\"checkpoint_path\": \"checkpoints/libero_acis_stage1only/stage1_done/checkpoint.pt\", \"completed_at\": \"2026-05-17T09:41:16.170Z\", \"conclusion\": \"negative\", \"created_at\": \"2026-05-17T08:59:33.996Z\", \"hypothesis\": \"Zero-masking（将 pruned token 置零）产生 OOD 输入导致 0% SR；true token removal（真正移除 pruned token，缩短序列）应恢复正常推理能力，因为 SmolVLA 用 RoPE 位置编码且 embed_prefix 动态适配序列长度\", \"log_path\": \"eval_results/eval_true_removal_k05.log\", \"metrics\": {\"episodes\": 500, \"k_ratio\": 0.5, \"libero_object_sr\": 0, \"pruning_method\": \"true_removal\", \"pruning_type\": \"acis\", \"wilson_ci_95\": \"[0.0%, 0.8%]\"}, \"parent\": \"eval_stage1only_k09\", \"retry_count\": 0, \"spec\": {\"checkpoint_source\": \"libero_acis_stage1only\", \"command\": \"python eval_success_rate_libero.py --checkpoint checkpoints/libero_acis_stage1only/stage1_done/checkpoint.pt --suite object --k-ratio 0.5 --pruning-method true_removal\", \"data_count\": 500, \"data_path\": \"/root/autodl-tmp/importance_margin_vla_compress/data/libero/object\", \"eval_data\": \"LIBERO-Object\", \"gpu\": \"1\", \"model_name\": \"SmolVLA-ACIS-Stage1Only\", \"seed\": 0, \"server\": \"westd-27271\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-17T09:41:16.170Z\"}, \"eval_stage1only_k09\": {\"completed_at\": \"2026-05-17T09:09:19.832Z\", \"conclusion\": \"negative\", \"created_at\": \"2026-05-17T08:32:20.053Z\", \"extra\": {\"hook_events\": [{\"action\": \"agent\", \"event\": \"on_failed\", \"ts\": \"2026-05-17T09:09:24.300632+00:00\"}]}, \"failure_reason\": \"process dead 5× with no sentinel/W&B — auto-resolved as failed\", \"hypothesis\": \"Stage1-only ACIS k=0.9（只移除 10% tokens）的 closed-loop SR。k=0.5 已确认 0% SR。如果 k=0.9 也 0% → 模型对任何 token 移除完全零容忍（极强 negative evidence，或 pruning hook 实现有根本问题）；如果 > 0% → 存在可接受的 pruning threshold。\", \"metrics\": {\"episodes\": 500, \"k_ratio\": 0.9, \"libero_object_sr\": 0, \"pruning_method\": \"zero_mask\", \"pruning_type\": \"acis\"}, \"parent\": \"eval_stage1only_object_v2_fixed\", \"reproduce\": {\"finished_at\": \"2026-05-17T09:09:23.064Z\"}, \"retry_count\": 0, \"spec\": {\"checkpoint_source\": \"checkpoints/libero_imm_twostage_fullft/stage1_done/checkpoint.pt\", \"command\": \"python eval_success_rate_libero.py --checkpoint checkpoints/libero_imm_twostage_fullft/stage1_done/checkpoint.pt --config configs/libero_acis_stage1only_k09.yaml --suite libero_object --mode acis_prune --num_episodes 50 --gpu 0 --output eval_results/eval_stage1only_k09_object.json\", \"data_count\": 500, \"data_path\": \"libero_object\", \"eval_data\": \"libero_object (10 tasks x 50 episodes)\", \"model_name\": \"smolvla_imm_stage1_only_k09\", \"seed\": 42, \"server\": \"westd-27271\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-17T09:16:38.225Z\"}, \"eval_random_prune_k05\": {\"completed_at\": \"2026-05-17T09:09:04.733Z\", \"conclusion\": \"negative\", \"created_at\": \"2026-05-17T08:30:40.635Z\", \"extra\": {\"hook_events\": [{\"action\": \"agent\", \"event\": \"on_failed\", \"ts\": \"2026-05-17T09:09:09.150955+00:00\"}]}, \"failure_reason\": \"process dead 5× with no sentinel/W&B — auto-resolved as failed\", \"hypothesis\": \"Random pruning 50% tokens（torch.rand 替代 ACIS scores）的 closed-loop SR。对照 ACIS pruning 0% SR：如果 random_prune 也 0% → 模型结构性不容忍 50% pruning（问题在 pruning ratio 不在 ACIS）；如果 random_prune > 0% → ACIS importance ranking 比随机更差（ACIS 学到了错误的 ranking）。\", \"metrics\": {\"episodes\": 500, \"k_ratio\": 0.5, \"libero_object_sr\": 0, \"pruning_method\": \"zero_mask\", \"pruning_type\": \"random\"}, \"parent\": \"eval_stage1only_object_v2_fixed\", \"reproduce\": {\"finished_at\": \"2026-05-17T09:09:04.097Z\"}, \"retry_count\": 0, \"spec\": {\"checkpoint_source\": \"checkpoints/libero_imm_twostage_fullft/stage1_done/checkpoint.pt\", \"command\": \"python eval_success_rate_libero.py --checkpoint checkpoints/libero_imm_twostage_fullft/stage1_done/checkpoint.pt --config configs/libero_imm_twostage_fullft.yaml --suite libero_object --mode random_prune --num_episodes 50 --gpu 0 --output eval_results/eval_random_prune_k05_object.json\", \"data_count\": 500, \"data_path\": \"libero_object\", \"eval_data\": \"libero_object (10 tasks x 50 episodes)\", \"model_name\": \"smolvla_imm_stage1_only\", \"seed\": 42, \"server\": \"westd-27271\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-17T09:16:36.387Z\"}, \"train_acis_stage1only_k07\": {\"completed_at\": \"2026-05-17T07:39:53.628Z\", \"conclusion\": \"success\", \"created_at\": \"2026-05-17T07:12:36.355Z\", \"extra\": {\"hook_events\": [{\"action\": \"agent\", \"event\": \"on_failed\", \"ts\": \"2026-05-17T07:39:56.009064+00:00\"}], \"previous_failure\": {\"conclusion\": \"failed\", \"notes\": \"2026-05-17T07:26Z diagnostic: cron false alarm. Process PID 11257 still alive on cqa1-33015 GPU 2. Currently at step 2300/10000, 4.3 sps, margin_loss ~0.19 (converging). ETA ~07:55 UTC. wandb run: offline-run-20260517_151656-8r6bfv8x. Log: ~/runs/importance_margin_vla_compress/train_acis_stage1only_k07.log\"}}, \"failure_reason\": \"process dead 5× with no sentinel/W&B — auto-resolved as failed\", \"hypothesis\": \"Stage1-only ACIS (k=0.7, 保留 70% tokens) 训练。与 k=0.5 (44.8% SR) 对比，预期 k=0.7 prune 后 SR >= 44.8% 因为保留更多信息。\", \"notes\": \"2026-05-17T07:26Z diagnostic: cron false alarm. Process PID 11257 still alive on cqa1-33015 GPU 2. Currently at step 2300/10000, 4.3 sps, margin_loss ~0.19 (converging). ETA ~07:55 UTC. wandb run: offline-run-20260517_151656-8r6bfv8x. Log: ~/runs/importance_margin_vla_compress/train_acis_stage1only_k07.log\", \"reproduce\": {\"finished_at\": \"2026-05-17T07:39:53.025Z\"}, \"retry_count\": 1, \"spec\": {\"checkpoint_path\": \"/root/autodl-tmp/importance_margin_vla_compress/checkpoints/libero_acis_stage1only_k07/stage1_done/checkpoint.pt\", \"command\": \"python train_twostage.py --config configs/libero_acis_stage1only_k07.yaml --gpu 0\", \"data_count\": \"10K steps\", \"data_path\": \"HuggingFaceVLA/libero\", \"log_path\": \"/root/autodl-tmp/importance_margin_vla_compress/wandb/offline-run-20260517_151656-8r6bfv8x/\", \"model_name\": \"SmolVLA ACIS Stage1-only k=0.7\", \"seed\": 42, \"server\": \"cqa1-33015\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-17T08:08:21.508Z\"}, \"eval_stage1only_object_v2_fixed\": {\"checkpoint_path\": \"checkpoints/libero_imm_twostage_fullft/stage1_done/checkpoint.pt\", \"completed_at\": \"2026-05-17T07:47:20.723Z\", \"conclusion\": \"negative\", \"created_at\": \"2026-05-17T07:22:09.502Z\", \"hypothesis\": \"Stage1-only ACIS (k=0.5) 在修复 pruning bug 后的真实 closed-loop 性能。bugfix 前 44.8% SR 是假阳性（pruning 未执行）。本实验验证实际 50% token pruning 下的 SR。若 SR >= 30% 证明 ACIS learned effective importance ranking；若 SR < 10% 则 ACIS scoring 无效。\", \"metrics\": {\"k_ratio\": 0.5, \"mode\": \"acis_prune\", \"note\": \"Fixed pruning (offset-tracking). Pruning actually executed this time. 0% SR confirms ACIS importance scoring is ineffective for closed-loop control after Stage1-only training.\", \"overall_success_rate\": 0, \"per_task_sr\": [0, 0, 0, 0, 0, 0], \"total_episodes\": 300, \"total_successes\": 0}, \"notes\": \"修复 pruning bug 后重跑。hook offset-tracking 方法确认 pruning 实际执行（保留 64/128 tokens）。结果：0% SR across 6+ tasks (300+ episodes)。之前 44.8% SR 是假阳性（pruning 未执行 = baseline forward）。Stage1-only ACIS pruning 50% tokens 导致完全失败——ACIS 学到的 importance ranking 在 closed-loop control 中无效。\", \"parent\": \"eval_stage1_only\", \"retry_count\": 0, \"spec\": {\"account\": \"root\", \"backend\": \"tmux\", \"checkpoint_source\": \"checkpoints/libero_imm_twostage_fullft/stage1_done/checkpoint.pt\", \"command\": \"python eval_success_rate_libero.py --checkpoint checkpoints/libero_imm_twostage_fullft/stage1_done/checkpoint.pt --config configs/libero_imm_twostage_fullft.yaml --suite libero_object --mode acis_prune --num_episodes 50 --gpu 0 --output eval_results/eval_stage1only_object_v2_fixed.json\", \"data_count\": 500, \"data_path\": \"libero_object\", \"eval_data\": \"libero_object (10 tasks x 50 episodes)\", \"gpu\": [\"cuda:0\"], \"gpu_hours\": 0.42, \"log_path\": \"~/runs/importance_margin_vla_compress/eval_stage1only_object_v2_fixed.log\", \"model_name\": \"smolvla_imm_stage1_only\", \"pid\": \"140050\", \"seed\": 42, \"server\": \"westd-27271\", \"submitted_at\": \"2026-05-17T07:22:09.342Z\", \"submitted_via\": \"submit_training_job\", \"wall_clock_seconds\": 1511.4}, \"status\": \"DONE\", \"updated_at\": \"2026-05-17T08:06:54.565Z\"}, \"eval_stage1only_spatial\": {\"completed_at\": \"2026-05-17T07:47:09.289Z\", \"conclusion\": \"killed\", \"created_at\": \"2026-05-17T06:52:30.933Z\", \"hypothesis\": \"Stage1-only ACIS pruning generalizes across suites: the same checkpoint that achieves 44.8% SR on Object suite should achieve comparable performance on Spatial suite (baseline 48% full FT)\", \"notes\": \"Killed: buggy eval code, pruning never executed due to dimension guard bug (64≠128). Results invalid.\", \"retry_count\": 0, \"spec\": {\"account\": \"root\", \"backend\": \"tmux\", \"checkpoint_source\": \"checkpoints/libero_imm_twostage_fullft/stage1_done/checkpoint.pt\", \"command\": \"CUDA_VISIBLE_DEVICES=1 python eval_success_rate_libero.py --checkpoint checkpoints/libero_imm_twostage_fullft/stage1_done/checkpoint.pt --config configs/libero_imm_twostage_fullft.yaml --suite libero_spatial --mode acis_prune --num_episodes 50 --gpu 0 --output eval_results/eval_stage1only_spatial.json\", \"data_count\": 500, \"data_path\": \"libero_spatial\", \"eval_data\": \"libero_spatial_10tasks_50ep\", \"gpu\": [\"cuda:1\"], \"gpu_hours\": 0.9, \"log_path\": \"~/runs/importance_margin_vla_compress/eval_stage1only_spatial.log\", \"model_name\": \"stage1_only_acis_prune\", \"pid\": \"65128\", \"seed\": 42, \"server\": \"westd-27271\", \"submitted_at\": \"2026-05-17T06:53:07.718Z\", \"submitted_via\": \"submit_training_job\", \"wall_clock_seconds\": 3241.6}, \"status\": \"DONE\", \"updated_at\": \"2026-05-17T07:47:16.934Z\"}, \"eval_stage1_only\": {\"completed_at\": \"2026-05-17T06:10:34.650Z\", \"conclusion\": \"success\", \"created_at\": \"2026-05-17T04:27:01.664Z\", \"hypothesis\": \"Stage1 ACIS learned effective token importance ranking. Using stage1_done checkpoint (original expert + trained ACIS, k_ratio=0.5) for acis_prune eval should retain significant performance (SR >= 30%) if ACIS quality is good. SR < 10% indicates ACIS importance scoring is ineffective.\", \"metrics\": {\"k_ratio\": 0.5, \"mode\": \"acis_prune\", \"overall_success_rate\": 0.448, \"per_task_sr\": [0.22, 0.6, 0.42, 0.38, 0.58, 0.26, 0.62, 0.38, 0.5, 0.52], \"total_episodes\": 500, \"total_successes\": 224, \"wilson_ci_95\": [0.405, 0.4918]}, \"notes\": \"⚠️ 结果已撤回。2026-05-17 pruning bug 确认：eval 脚本 dimension guard (64≠128) 导致 acis_prune 模式从未实际执行 pruning，所有 token 原样通过。44.8% SR 是未 pruning 的结果，不能证明 \\\"lossless 2x compression\\\"。已修复并启动 eval_stage1only_object_v2_fixed 重跑。\", \"parent\": \"eval_imm100k_bypass\", \"retry_count\": 0, \"spec\": {\"account\": \"root\", \"backend\": \"tmux\", \"checkpoint_path\": \"checkpoints/libero_imm_twostage_fullft/stage1_done/checkpoint.pt\", \"checkpoint_source\": \"checkpoints/libero_imm_twostage_fullft/stage1_done/checkpoint.pt\", \"command\": \"python eval_success_rate_libero.py --checkpoint checkpoints/libero_imm_twostage_fullft/stage1_done/checkpoint.pt --config configs/libero_imm_twostage_fullft.yaml --suite libero_object --mode acis_prune --num_episodes 50 --gpu 0\", \"data_count\": 500, \"data_path\": \"libero_object\", \"eval_data\": \"libero_object (10 tasks x 50 episodes)\", \"gpu\": [\"cuda:0\"], \"gpu_hours\": 1.72, \"log_path\": \"eval_results/eval_stage1only_object.json\", \"model_name\": \"smolvla_imm_stage1_only\", \"pid\": \"961179\", \"seed\": 42, \"server\": \"westd-27271\", \"submitted_at\": \"2026-05-17T04:27:18.785Z\", \"submitted_via\": \"submit_training_job\", \"wall_clock_seconds\": 6195.9}, \"status\": \"DONE\", \"updated_at\": \"2026-05-17T07:24:44.994Z\"}, \"libero_fullft_seed1\": {\"completed_at\": \"2026-05-17T01:27:49.728Z\", \"conclusion\": \"success\", \"created_at\": \"2026-05-16T21:52:18.096Z\", \"extra\": {\"hook_events\": [{\"action\": \"agent\", \"event\": \"on_failed\", \"ts\": \"2026-05-17T01:51:30.586420+00:00\"}], \"previous_failure\": {\"conclusion\": \"failed\", \"notes\": \"正常运行中 64,300/100K (64.3%), sps=4.2。之前 cron 误报进程退出，Reviewer 和诊断 Worker 均确认进程存活。预计 ~2h 完成。Log: /root/runs/importance_margin_vla_compress/libero_fullft_seed1.log\"}}, \"failure_reason\": \"process dead 5× with no sentinel/W&B — auto-resolved as failed\", \"hypothesis\": \"Full FT seed=1 应复现 seed=42 (49% SR) 和 seed=0 的性能水平，验证 Full FT 方法对 LIBERO 的泛化性不依赖于特定随机种子。预期 SR 在 40-55% 范围内。\", \"metrics\": {\"eval_action_loss\": 0.05404, \"total_steps\": 100000, \"train_action_loss\": 0.04282, \"train_grad_norm\": 1.17539}, \"notes\": \"100K steps 完成 (2026-05-17 12:30 UTC+8). Final train_loss=0.0428, eval_loss=0.0540. Checkpoint 1.3GB saved at step_099999. GPU 0 已释放。需要 SR eval 确认性能。\", \"parent\": \"libero_full_ft_baseline\", \"reproduce\": {\"finished_at\": \"2026-05-17T01:51:28.197Z\"}, \"retry_count\": 2, \"spec\": {\"checkpoint_path\": \"/root/autodl-tmp/importance_margin_vla_compress/checkpoints/libero_full_ft_seed1/step_099999/checkpoint.pt\", \"command\": \"python train.py --config configs/libero_full_ft_seed1.yaml --gpu 0 --seed 1\", \"data_count\": 273465, \"data_path\": \"HuggingFaceVLA/libero\", \"gpu\": [\"cuda:0\"], \"log_path\": \"/root/runs/importance_margin_vla_compress/libero_fullft_seed1.log\", \"model_name\": \"smolvla_base_full_ft\", \"seed\": 1, \"server\": \"cqa1-33015\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-17T06:50:58.697Z\"}, \"libero_fullft_batch64\": {\"completed_at\": \"2026-05-17T05:34:58.137Z\", \"conclusion\": \"failed\", \"created_at\": \"2026-05-17T01:29:36.383Z\", \"extra\": {\"hook_events\": [{\"action\": \"agent\", \"event\": \"on_failed\", \"ts\": \"2026-05-17T05:35:00.242982+00:00\"}]}, \"failure_reason\": \"SSH check failed 5x — last error: [Errno None] Unable to connect to port 33015 on 58.144.141.28\", \"hypothesis\": \"Batch size 4→64 (grad_accum=16) 是 87.3% SR gap 根因 (D055)。使用与 SmolVLA 官方相同 effective batch=64 训练 100K steps，预期 SR 从 49% 提升至接近官方水平 (~80%+)，为 IMM 实验提供强 baseline。\", \"notes\": \"进程死亡 at step 3550/100K，无 checkpoint（save_every=10000 导致 3.3h 训练全丢）。需要从头重启，改 save_every=5000。\", \"parent\": \"libero_full_ft_baseline\", \"retry_count\": 0, \"spec\": {\"checkpoint_source\": \"N/A (training from scratch, same architecture as libero_full_ft_baseline)\", \"command\": \"python train.py --config configs/libero_full_ft_batch64.yaml --gpu 0\", \"data_count\": 273465, \"data_path\": \"HuggingFaceVLA/libero\", \"effective_batch_size\": 64, \"eval_data\": \"N/A (training experiment, will eval post-training)\", \"gpu\": [\"cuda:1\"], \"gradient_accumulation_steps\": 16, \"log_path\": \"logs/fullft_batch64.log\", \"model_name\": \"smolvla_base_full_ft_batch64\", \"pid\": \"124908\", \"seed\": 42, \"server\": \"cqa1-33015\", \"tmux_session\": \"fullft_batch64\", \"total_steps\": 100000, \"trainable_params\": \"99.9M (22.2%)\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-17T06:50:58.195Z\"}, \"eval_imm100k_bypass\": {\"completed_at\": \"2026-05-17T06:10:36.056Z\", \"conclusion\": \"negative\", \"created_at\": \"2026-05-17T03:35:41.235Z\", \"hypothesis\": \"IMM Stage2 full-FT training preserves expert weight quality: bypass eval (baseline mode, no pruning) of the IMM 100K checkpoint should recover baseline SR ~44% if weights are intact, or show SR < 20% if Stage2 damaged expert weights.\", \"metrics\": {\"mode\": \"baseline_bypass\", \"note\": \"Stage2 completely destroyed expert weights\", \"overall_success_rate\": 0, \"per_task_sr\": [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], \"total_episodes\": 500, \"total_successes\": 0, \"wilson_ci_95\": [0, 0.0076]}, \"notes\": \"2026-05-17 ~12:00 UTC: westd-27271 不可达。已知部分结果：6/10 tasks 完成时全部 0% SR。服务器断联前可能已完成全部 10 tasks。需重启后检查 eval_results/imm_100k_bypass_object.json。\", \"retry_count\": 0, \"spec\": {\"account\": \"root\", \"backend\": \"tmux\", \"checkpoint_path\": \"checkpoints/libero_imm_twostage_fullft/final/checkpoint.pt\", \"checkpoint_source\": \"checkpoints/libero_imm_twostage_fullft/final/checkpoint.pt\", \"command\": \"CUDA_VISIBLE_DEVICES=0 python eval_success_rate_libero.py --checkpoint checkpoints/libero_imm_twostage_fullft/final/checkpoint.pt --config configs/libero_imm_twostage_fullft.yaml --suite libero_object --mode baseline --num_episodes 50 --gpu 0 --output eval_results/imm_100k_bypass_object.json\", \"data_count\": 50, \"data_path\": \"libero_object\", \"eval_data\": \"libero_object\", \"gpu\": [\"cuda:0\"], \"gpu_hours\": 2.5, \"log_path\": \"eval_results/imm_100k_bypass_object.json\", \"model_name\": \"libero_imm_twostage_fullft\", \"pid\": \"882658\", \"seed\": 0, \"server\": \"westd-27271\", \"submitted_at\": \"2026-05-17T03:40:48.744Z\", \"submitted_via\": \"submit_training_job\", \"wall_clock_seconds\": 8987.3}, \"status\": \"DONE\", \"updated_at\": \"2026-05-17T06:29:09.923Z\"}, \"eval_k07_bypass_v3\": {\"completed_at\": \"2026-05-17T06:10:37.113Z\", \"conclusion\": \"negative\", \"created_at\": \"2026-05-17T04:00:06.238Z\", \"hypothesis\": \"k=0.7 two-stage full-FT model with baseline (bypass/no-pruning) forward should achieve competitive success rate on libero_object, establishing upper-bound performance before ACIS pruning is applied.\", \"metrics\": {\"mode\": \"baseline_bypass\", \"note\": \"Stage2 k=0.7 also completely destroyed expert weights\", \"overall_success_rate\": 0, \"per_task_sr\": [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], \"total_episodes\": 500, \"total_successes\": 0, \"wilson_ci_95\": [0, 0.0076]}, \"notes\": \"2026-05-17 ~12:00 UTC: westd-27271 不可达。eval 提交于 04:00 UTC，距今 ~8h，预计已完成或接近完成。需重启后检查 eval_results/imm_k07_bypass_object.json。\", \"retry_count\": 0, \"spec\": {\"account\": \"root\", \"backend\": \"tmux\", \"checkpoint_path\": \"checkpoints/libero_imm_twostage_fullft_k07/final/checkpoint.pt\", \"checkpoint_source\": \"checkpoints/libero_imm_twostage_fullft_k07/final/checkpoint.pt\", \"command\": \"bash -c \\\"cd /root/autodl-tmp/importance_margin_vla_compress && source /root/miniconda3/bin/activate && CUDA_VISIBLE_DEVICES=1 python eval_success_rate_libero.py --checkpoint checkpoints/libero_imm_twostage_fullft_k07/final/checkpoint.pt --config configs/libero_imm_twostage_fullft_k07.yaml --suite libero_object --mode baseline --num_episodes 50 --gpu 0 --output eval_results/imm_k07_bypass_object.json\\\"\", \"data_count\": 500, \"data_path\": \"libero_object\", \"eval_data\": \"libero_object (10 tasks x 50 episodes)\", \"gpu\": [\"cuda:1\"], \"gpu_hours\": 2.18, \"log_path\": \"eval_results/imm_k07_bypass_object.json\", \"model_name\": \"libero_imm_twostage_fullft_k07\", \"pid\": \"905921\", \"seed\": 0, \"server\": \"westd-27271\", \"submitted_at\": \"2026-05-17T04:00:06.138Z\", \"submitted_via\": \"submit_training_job\", \"wall_clock_seconds\": 7831.0}, \"status\": \"DONE\", \"updated_at\": \"2026-05-17T06:10:37.113Z\"}, \"eval_k07_bypass_v2\": {\"completed_at\": \"2026-05-17T03:59:51.984Z\", \"conclusion\": \"failed\", \"created_at\": \"2026-05-17T03:36:19.130Z\", \"hypothesis\": \"k=0.7 bypass eval will show less expert degradation than k=0.5 bypass because retaining more tokens during training causes less damage to the expert backbone representations\", \"notes\": \"CUDA error: invalid device ordinal. Script specified cuda:1 but CUDA_VISIBLE_DEVICES likely restricted visibility to 1 GPU. Fix: use --device cuda:0 with CUDA_VISIBLE_DEVICES=1, or remove CUDA_VISIBLE_DEVICES and use --device cuda:1.\", \"retry_count\": 0, \"spec\": {\"account\": \"root\", \"backend\": \"tmux\", \"checkpoint_source\": \"checkpoints/libero_imm_twostage_fullft_k07/final/checkpoint.pt\", \"command\": \"python eval_success_rate_libero.py --mode baseline --suite libero_object --num_episodes 50\", \"data_count\": 50, \"data_path\": \"libero_object\", \"eval_data\": \"libero_object\", \"gpu\": [\"cuda:1\"], \"gpu_hours\": 0.39, \"log_path\": \"~/runs/importance_margin_vla_compress/eval_k07_bypass_v2.log\", \"model_name\": \"smolvla_imm_k07_twostage_fullft\", \"pid\": \"876957\", \"seed\": 0, \"server\": \"westd-27271\", \"submitted_at\": \"2026-05-17T03:36:19.036Z\", \"submitted_via\": \"submit_training_job\", \"wall_clock_seconds\": 1412.9}, \"status\": \"DONE\", \"updated_at\": \"2026-05-17T04:00:12.288Z\"}, \"eval_imm_k07_object\": {\"checkpoint_path\": \"eval_results/eval_imm_k07_object_acis_prune.json\", \"completed_at\": \"2026-05-17T03:30:14.633Z\", \"conclusion\": \"negative\", \"created_at\": \"2026-05-17T01:58:25.483Z\", \"hypothesis\": \"k=0.7 (retain 70% tokens) should recover most task performance compared to k=0.5 catastrophic failure (3.5-15.4% SR), because 70% retention preserves critical spatial/manipulation information that 50% discards. Expect SR >= 30-40% if the performance cliff is between k=0.5 and k=0.7.\", \"metrics\": {\"overall_success_rate\": 0.048, \"per_task_sr\": [0, 0, 0.06, 0.02, 0.32, 0.06, 0.02, 0, 0, 0], \"total_episodes\": 500, \"total_successes\": 24, \"wilson_ci_95\": [0.0325, 0.0704]}, \"parent\": \"libero_imm_fullft_k07\", \"retry_count\": 0, \"spec\": {\"account\": \"root\", \"backend\": \"tmux\", \"checkpoint_source\": \"cqa1-33015\", \"command\": \"python eval_success_rate_libero.py --checkpoint checkpoints/libero_imm_twostage_fullft_k07/final/checkpoint.pt --config configs/libero_imm_twostage_fullft_k07.yaml --suite libero_object --num_episodes 50 --gpu 0 --mode acis_prune --output eval_results/eval_imm_k07_object_acis_prune.json\", \"data_count\": 500, \"data_path\": \"libero_object\", \"eval_data\": \"libero_object (10 tasks x 50 episodes)\", \"gpu\": [\"cuda:0\"], \"gpu_hours\": 1.53, \"log_path\": \"~/runs/importance_margin_vla_compress/eval_imm_k07_object.log\", \"model_name\": \"smolvla_imm_twostage_fullft_k07\", \"pid\": \"823162\", \"seed\": 42, \"server\": \"westd-27271\", \"submitted_at\": \"2026-05-17T01:58:25.393Z\", \"submitted_via\": \"submit_training_job\", \"wall_clock_seconds\": 5509.2}, \"status\": \"DONE\", \"updated_at\": \"2026-05-17T03:31:16.482Z\"}, \"mvp_imm_anchor_v7_2\": {\"completed_at\": \"2026-05-15T23:05:32.357Z\", \"conclusion\": \"negative\", \"created_at\": \"2026-05-15T19:18:02.766Z\", \"hypothesis\": \"v7 的 G3 failure (3.28x) 中有部分归因于 eval mode leak (metrics.py bug)。修复后重跑 (lambda=0.2, grad_clip=30.0) 预期 G3 显著改善至 ≤2.0x，若仍 >2.0x 则证明 G3 问题是训练机制本身而非评估 bug。\", \"metrics\": {\"bypass_acis\": {\"clean_action_loss\": 0.0078, \"conclusion\": \"weights_damaged\", \"g3_ratio\": 1.91}, \"eval_500batch_soft\": {\"clean_action_loss\": 0.013, \"clean_margin_median\": 0.6627, \"clean_preservation\": 1, \"eps001_led_median\": 0.162, \"eps001_preservation\": 0.9253, \"eps002_led_median\": 0.3232, \"eps002_preservation\": 0.8482, \"eps005_led_median\": 0.7656, \"eps005_preservation\": 0.6597, \"lipschitz_empirical\": 0.3393, \"lipschitz_spectral\": 1.0672}, \"gate_v7_2\": {\"G1_margin_ratio\": 64.25, \"G1_pass\": true, \"G2_pass\": true, \"G2_preservation_diff_pp\": 47.46, \"G3_action_loss_ratio\": 3.19, \"G3_pass\": false, \"G4_led_median\": 0.323, \"G4_pass\": true, \"overall\": \"FAIL\"}, \"source\": \"eval_results/eval_imm_v7_2_final.json + eval_results/eval_imm_v7_2_bypass_acis.json\"}, \"notes\": \"v7.2 final eval (fixed soft forward + temperature): G1 PASS 64.25x, G2 PASS +47.46pp, G3 FAIL 3.19x (vs v7's 3.28x — barely better despite lambda 0.5→0.2), G4 PASS 0.323. Bypass-ACIS diagnostic: G3=1.91x >> 1.10 → 权重受损确认，不是 selection mechanism overhead。IMM 梯度回传通过 LoRA 污染了 VLM backbone。附注: pruneTrue 条件下 v7.2 远优于 baseline (0.24x ratio)，说明 IMM 训练确实提升了 token importance 鲁棒性，但代价是 clean performance。\", \"parent\": \"mvp_imm_anchor_v7\", \"retry_count\": 0, \"spec\": {\"checkpoint_path\": \"checkpoints/imm_anchor_v7_1/step_029999\", \"log_path\": \"/tmp/imm_anchor_v7_2.log\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-17T02:56:02.730Z\"}, \"mvp_imm_anchor_v7\": {\"completed_at\": \"2026-05-15T21:30:03.885Z\", \"conclusion\": \"failed\", \"created_at\": \"2026-05-15T17:07:33.984Z\", \"extra\": {\"hook_events\": [{\"action\": \"agent\", \"event\": \"on_complete\", \"ts\": \"2026-05-15T20:20:19.132930+00:00\"}]}, \"hypothesis\": \"IMM training (delta=0.3, lambda=0.5) with eval disabled (D008) - same config as v6, skip in-training eval to avoid RoPE crash\", \"metrics\": {\"eval_500batch\": {\"clean_action_loss\": 0.0134, \"clean_margin_median\": 0.5743, \"clean_preservation\": 1, \"eps001_led_median\": 0.1341, \"eps001_preservation\": 0.9124, \"eps002_led_median\": 0.2726, \"eps002_preservation\": 0.8172, \"eps005_led_median\": 0.69, \"eps005_preservation\": 0.6079, \"lipschitz_empirical\": 0.2493, \"lipschitz_spectral\": 1.0672}, \"source\": \"eval_results/eval_imm_v7_final.json\"}, \"notes\": \"G3 FAIL: clean action_loss 3.28x baseline (需≤1.10)。G1/G2/G4 PASS (margin 55x, preservation +44pp, LED 0.27<1.0)。lambda=0.5 过于激进。Source: eval_imm_v7_final.json, eval_baseline_v5_final.json, gate_report.json.\", \"parent\": \"mvp_imm_anchor_v6\", \"reproduce\": {\"finished_at\": \"2026-05-15T20:20:18.377Z\"}, \"retry_count\": 0, \"spec\": {\"checkpoint_path\": \"checkpoints/imm_anchor/step_029999\", \"log_path\": \"/tmp/imm_anchor_v7.log\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-17T02:56:02.358Z\"}, \"libero_fullft_seed0\": {\"completed_at\": \"2026-05-16T21:01:45.291Z\", \"conclusion\": \"success\", \"created_at\": \"2026-05-16T15:59:20.198Z\", \"extra\": {\"previous_failure\": {\"conclusion\": \"failed\", \"notes\": \"step 42450/100000 (42.5%), loss=0.026, lr=6.36e-05, sps=4.0 as of 2026-05-17 02:38\"}}, \"failure_reason\": \"startup recovery: RUNNING with no cron and no server/pid info\", \"hypothesis\": \"Full FT seed=0 应复现 seed=42 的 SR 水平 (~36-49%)，确认 Full FT 方法性能稳定性。若 SR 显著偏离 (差 >15pp) 则说明方法对初始化敏感。\", \"notes\": \"100K 完成 (2026-05-17 06:47 UTC). Full FT seed=0, 需要 SR eval 确认（预期与 seed=42 相近 ~33-42%）。\", \"parent\": \"libero_full_ft_baseline\", \"retry_count\": 1, \"spec\": {\"checkpoint_path\": \"/root/autodl-tmp/importance_margin_vla_compress/checkpoints/libero_full_ft_seed0/step_099999/checkpoint.pt\", \"command\": \"python train.py --config configs/libero_full_ft.yaml\", \"data_count\": 273465, \"data_path\": \"HuggingFaceVLA/libero\", \"gpu\": [\"cuda:3\"], \"log_path\": \"~/runs/importance_margin_vla_compress/libero_fullft_seed0.log\", \"model_name\": \"smolvla_base_full_ft\", \"pid\": \"21461\", \"seed\": 0, \"server\": \"cqa1-33015\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-17T02:55:48.738Z\"}, \"libero_imm_fullft_k07\": {\"completed_at\": \"2026-05-17T01:27:51.384Z\", \"conclusion\": \"success\", \"created_at\": \"2026-05-16T23:32:00.560Z\", \"extra\": {\"hook_events\": [{\"action\": \"agent\", \"event\": \"on_failed\", \"ts\": \"2026-05-17T01:40:24.861047+00:00\"}], \"previous_failure\": {\"conclusion\": \"failed\"}}, \"failure_reason\": \"process dead 5× with no sentinel/W&B — auto-resolved as failed\", \"hypothesis\": \"IMM two-stage k_ratio=0.7 ablation (保留 70% tokens, pruning 30%)。对比 k=0.5 验证 compression-performance tradeoff。Base: Full FT seed=42 100K\", \"notes\": \"训练完成 20K steps (09:43 UTC+8)。Checkpoint rsync 到 westd 成功 (879MB)。Object eval (acis_prune, k=0.7, 10 tasks × 50 eps) 在 westd:0 运行中，预计 ~40-50min 完成。结果路径: eval_results/eval_imm_k07_object_acis_prune.json。监控: tail -f ~/runs/importance_margin_vla_compress/eval_imm_k07_object.log\", \"parent\": \"libero_imm_fullft_100k\", \"reproduce\": {\"finished_at\": \"2026-05-17T01:40:22.040Z\"}, \"retry_count\": 1, \"spec\": {\"checkpoint_source\": \"checkpoints/libero_full_ft/step_099999/checkpoint.pt\", \"command\": \"IMM two-stage fullft k_ratio=0.7\", \"data_count\": 20000, \"data_path\": \"/root/autodl-tmp/importance_margin_vla_compress\", \"eval_data\": \"N/A (training)\", \"gpu\": [\"cuda:3\"], \"model_name\": \"libero_imm_twostage_fullft_k07\", \"seed\": 0, \"server\": \"cqa1-33015\", \"stage1_steps\": 10000, \"stage2_steps\": 20000, \"total_steps\": 30000}, \"status\": \"DONE\", \"updated_at\": \"2026-05-17T02:55:31.044Z\"}, \"libero_imm_fullft_seed0\": {\"completed_at\": \"2026-05-17T01:27:50.831Z\", \"conclusion\": \"success\", \"created_at\": \"2026-05-16T23:32:00.151Z\", \"failure_reason\": \"\", \"hypothesis\": \"IMM two-stage (Full FT-based) on LIBERO seed=0, 验证 IMM 方法跨 seed 稳定性。Base: Full FT seed=0 100K。Stage1=10K ACIS, Stage2=20K expert, k_ratio=0.5\", \"notes\": \"训练完成 (09:25:17 \\\"Two-stage training complete.\\\"). Checkpoint 920MB 已保存。被 startup recovery 错误标记为 failed，Director 指令修正。\", \"parent\": \"libero_imm_fullft_100k\", \"retry_count\": 0, \"spec\": {\"checkpoint_source\": \"checkpoints/libero_full_ft_seed0/step_099999/checkpoint.pt\", \"command\": \"python train_twostage.py --config configs/libero_imm_twostage_fullft_seed0.yaml --gpu 0 --seed 0\", \"data_count\": 273465, \"data_path\": \"HuggingFaceVLA/libero\", \"gpu\": [\"cuda:2\"], \"model_name\": \"smolvla_fullft_seed0_100k+IMM_twostage\", \"seed\": 0, \"server\": \"cqa1-33015\", \"stage1_steps\": 10000, \"stage2_steps\": 20000, \"total_steps\": 30000}, \"status\": \"DONE\", \"updated_at\": \"2026-05-17T02:55:30.125Z\"}, \"libero_imm_fullft_100k\": {\"completed_at\": \"2026-05-17T01:27:50.283Z\", \"conclusion\": \"success\", \"created_at\": \"2026-05-16T22:11:57.636Z\", \"failure_reason\": \"\", \"hypothesis\": \"IMM two-stage (Full FT-based) on LIBERO using 100K Full FT checkpoint (seed=42, SR~50%+ expected). Stage1: train ACIS (10K steps), Stage2: train expert (20K steps). 论文正式 IMM 数据。目标: SR ≥ baseline 且 50% token pruning。\", \"notes\": \"训练完成。Object eval (acis_prune) 正在 westd:0 上执行 (task 4+)。被 startup recovery 错误标记为 failed，Director 指令修正。\", \"parent\": \"libero_imm_fullft_v2\", \"retry_count\": 0, \"spec\": {\"checkpoint_source\": \"checkpoints/libero_full_ft/step_099999/checkpoint.pt (100K Full FT seed=42)\", \"command\": \"python train_twostage.py --config configs/libero_imm_twostage_fullft.yaml --gpu 0 --wandb_run libero_imm_fullft_100k\", \"data_count\": 273465, \"data_path\": \"HuggingFaceVLA/libero\", \"gpu\": [\"cuda:1\"], \"model_name\": \"smolvla_fullft_100k+IMM_twostage\", \"seed\": 42, \"server\": \"cqa1-33015\", \"stage1_steps\": 10000, \"stage2_steps\": 20000, \"total_steps\": 30000}, \"status\": \"DONE\", \"updated_at\": \"2026-05-17T02:55:29.163Z\"}, \"libero_imm_fullft_v2\": {\"completed_at\": \"2026-05-16T21:01:47.531Z\", \"conclusion\": \"negative\", \"created_at\": \"2026-05-16T20:29:44.685Z\", \"extra\": {\"previous_failure\": {\"conclusion\": \"failed\", \"notes\": \"重提交成功 (20:50 UTC)。修复: conda激活+network_turbo+wandb offline。Stage 1 running: step 150/10000, margin_loss=0.2799, sps=5.5。预计完成 ~22:20 UTC (30K steps total)。checkpoint 路径在 config yaml 中配置（twostage.baseline_checkpoint），非命令行参数。\"}}, \"failure_reason\": \"\", \"hypothesis\": \"IMM two-stage (Full FT-based) on LIBERO: Stage1 训 ACIS selector (freeze expert), Stage2 训 expert (freeze ACIS). Base checkpoint: Full FT 50K (SR=33%). 目标: IMM 训练后 SR ≥ 33% 证明方法有效。Plan B 验证。\", \"metrics\": {\"sr_object\": {\"n_episodes\": 100, \"note\": \"IMM two-stage on 50K FT checkpoint, Object suite eval. 15.4% vs baseline 44.8% (-66% relative)\", \"overall\": 0.154, \"source\": \"imm_v2_fullft_libero_object.json\", \"suite\": \"libero_object\"}}, \"notes\": \"训练完成 30K steps (westd:0)。Object eval SR=15.4% vs baseline 44.8% (-66% relative)。IMM k=0.5 on 50K FT base 造成严重 closed-loop 退化。Reviewer 确认 eval 有效。\", \"parent\": \"mvp_imm_v8b_twostage\", \"retry_count\": 1, \"spec\": {\"checkpoint_source\": \"checkpoints/libero_full_ft_50k/checkpoint.pt\", \"command\": \"python train_twostage.py --config configs/libero_imm_twostage_fullft.yaml --gpu 0\", \"data_count\": 273465, \"data_path\": \"HuggingFaceVLA/libero\", \"gpu\": [\"cuda:0\"], \"model_name\": \"smolvla_fullft_50k+IMM_twostage\", \"seed\": 42, \"server\": \"westd-27271\", \"stage1_steps\": 10000, \"stage2_steps\": 20000, \"total_steps\": 30000}, \"status\": \"DONE\", \"updated_at\": \"2026-05-17T02:55:28.216Z\"}, \"libero_lora_seed0\": {\"completed_at\": \"2026-05-16T21:01:44.824Z\", \"conclusion\": \"negative\", \"created_at\": \"2026-05-16T15:59:19.643Z\", \"extra\": {\"previous_failure\": {\"conclusion\": \"failed\", \"notes\": \"step 43600/100000 (43.6%), loss=0.094, lr=6.18e-05, sps=4.1 as of 2026-05-17 02:38\"}}, \"failure_reason\": \"startup recovery: RUNNING with no cron and no server/pid info\", \"hypothesis\": \"SmolVLA LoRA (r=32, alpha=16) on LIBERO seed=0, 验证 LoRA capacity bottleneck 是否跨 seed 一致（预期与 seed=42 同样 0% SR）\", \"notes\": \"100K 完成 (2026-05-17 06:44 UTC). LoRA seed=0 预期 0% SR（与 seed=42 一致，capacity bottleneck confirmed）。\", \"parent\": \"libero_lora_baseline\", \"retry_count\": 1, \"spec\": {\"checkpoint_path\": \"/root/autodl-tmp/importance_margin_vla_compress/checkpoints/libero_baseline_seed0/step_099999/checkpoint.pt\", \"command\": \"python train.py --config configs/libero_baseline.yaml\", \"data_count\": 273465, \"data_path\": \"HuggingFaceVLA/libero\", \"gpu\": [\"cuda:2\"], \"log_path\": \"~/runs/importance_margin_vla_compress/libero_lora_seed0.log\", \"model_name\": \"smolvla_base+LoRA(r=32,alpha=16)\", \"pid\": \"21389\", \"seed\": 0, \"server\": \"cqa1-33015\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-17T02:55:27.439Z\"}, \"libero_lora_baseline\": {\"completed_at\": \"2026-05-16T21:36:00.462Z\", \"conclusion\": \"negative\", \"created_at\": \"2026-05-16T14:20:19.278Z\", \"extra\": {\"hook_events\": [{\"action\": \"agent\", \"event\": \"on_complete\", \"ts\": \"2026-05-16T21:26:10.211023+00:00\"}]}, \"hypothesis\": \"SmolVLA LoRA (r=32, alpha=16) on LIBERO, 验证 LoRA + flow matching 是否系统性 mode collapse\", \"metrics\": {\"diversity_10k\": {\"noise_diversity_std\": 0.1736, \"pass\": true, \"per_obs\": [0.166, 0.177, 0.154, 0.198, 0.174], \"threshold\": 0.05}, \"sr_100k\": {\"all_episodes_hit_max_steps\": true, \"eval_running\": true, \"max_steps\": 400, \"n_episodes_completed\": 10, \"n_episodes_total\": 100, \"note\": \"task_0 complete 0/10, remaining tasks 1-9 still evaluating but pattern is conclusive\", \"overall\": 0, \"suite\": \"libero_object\", \"task_0_episodes\": 10, \"task_0_sr\": 0}, \"sr_50k\": {\"lora_keys_loaded\": 74, \"missing_keys\": 0, \"n_episodes\": 50, \"overall\": 0, \"per_task\": [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], \"suite\": \"libero_object\", \"unexpected_keys\": 0, \"verdict\": \"CORRECT_LOAD_confirmed_0pct_SR\", \"verified\": true}, \"training_100k\": {\"checkpoint_size_mb\": 883, \"completed_normally\": true, \"final_eval_loss\": 0.08041, \"final_grad_norm\": 0.415, \"final_lr\": 2.5e-06, \"final_step\": 99999, \"final_train_loss\": 0.0648}}, \"notes\": \"100K training complete (2026-05-17 05:25). Final: loss=0.0648, eval_loss=0.0804, lr≈0. SR@100K=0% (task_0: 0/10, all max-step=400 FAIL; remaining tasks eval running but conclusive). Compared to Full FT baseline: SR@50K=33% with train_loss=0.041. LoRA (r=32, alpha=16, 1.49M params) definitively insufficient for LIBERO manipulation — not mode collapse (diversity PASS std=0.174), but capacity bottleneck. Checkpoint: checkpoints/libero_baseline/step_099999/checkpoint.pt (883MB).\", \"reproduce\": {\"finished_at\": \"2026-05-16T21:26:07.861Z\"}, \"retry_count\": 0, \"spec\": {\"account\": \"root\", \"backend\": \"tmux\", \"checkpoint_path\": \"/root/autodl-tmp/importance_margin_vla_compress/checkpoints/libero_baseline/step_099999/checkpoint.pt\", \"command\": \"python train.py --config configs/libero_baseline.yaml\", \"data_count\": 273465, \"data_path\": \"HuggingFaceVLA/libero\", \"gpu\": [\"cuda:1\"], \"gpu_hours\": 7.26, \"log_path\": \"~/runs/importance_margin_vla_compress/libero_lora_baseline.log\", \"model_name\": \"smolvla_base+LoRA(r=32,alpha=16)\", \"pid\": \"9062\", \"seed\": 42, \"server\": \"cqa1-33015\", \"submitted_at\": \"2026-05-16T14:20:19.230Z\", \"submitted_via\": \"submit_training_job\", \"wall_clock_seconds\": 26141.2}, \"status\": \"DONE\", \"updated_at\": \"2026-05-16T21:53:26.310Z\"}, \"libero_imm_twostage_v1\": {\"completed_at\": \"2026-05-16T19:06:03.822Z\", \"conclusion\": \"killed\", \"created_at\": \"2026-05-16T18:47:03.312Z\", \"notes\": \"有意 kill: 40K baseline checkpoint 不够强���50K SR=33%，100K 预期更高），等 100K 最佳 checkpoint 启动 v2。非 bug。\", \"retry_count\": 0, \"spec\": {\"baseline_checkpoint\": \"checkpoints/libero_baseline/step_040000/checkpoint.pt\", \"checkpoint_path\": \"checkpoints/libero_imm_twostage/\", \"command\": \"python -u train_twostage.py --config configs/libero_imm_twostage.yaml\", \"data_count\": 383, \"data_path\": \"HuggingFaceVLA/libero\", \"gpu_ids\": [\"cuda:0\"], \"hypothesis\": \"IMM two-stage on LIBERO: Stage1 freeze LoRA train ACIS, Stage2 freeze ACIS train LoRA. 验证 aloha 上验证的 two-stage 方法在 LIBERO 上的泛化\", \"log_path\": \"/tmp/libero_imm_twostage_v1.log\", \"model_name\": \"SmolVLA + IMM two-stage (ACIS-first)\", \"seed\": 42, \"server\": \"westd-27271\", \"stage1_steps\": 10000, \"stage2_steps\": 20000, \"total_steps\": 30000}, \"status\": \"DONE\", \"updated_at\": \"2026-05-16T19:06:03.822Z\"}, \"plan_009_token_importance\": {\"completed_at\": \"2026-05-16T16:57:38.243Z\", \"conclusion\": \"success\", \"created_at\": \"2026-05-16T16:57:07.812Z\", \"hypothesis\": \"Token importance 分析: ACIS importance score 与 action prediction gradient 的 Spearman correlation，验证 ACIS 选择合理性\", \"metrics\": {\"action_loss_mean\": 0.0195, \"gradient_ratio_retained_over_pruned\": 1.7027, \"n_samples\": 100, \"n_vis_tokens\": 64, \"pruned_grad_mean\": 0.000183, \"retained_grad_mean\": 0.000311, \"spearman_corr_mean\": 0.4069, \"spearman_corr_median\": 0.4065, \"spearman_corr_std\": 0.1022}, \"retry_count\": 0, \"spec\": {\"checkpoint_path\": \"checkpoints/imm_anchor_v8b_twostage/final/checkpoint.pt\", \"checkpoint_source\": \"checkpoints/imm_anchor_v8b_twostage/final/checkpoint.pt\", \"command\": \"CUDA_VISIBLE_DEVICES=1 python eval_token_importance.py --checkpoint checkpoints/imm_anchor_v8b_twostage/final/checkpoint.pt --num_samples 100\", \"data_count\": 100, \"data_path\": \"lerobot/aloha_sim_insertion_scripted_image\", \"gpu_ids\": [\"cuda:1\"], \"hypothesis\": \"ACIS importance score 与 action prediction gradient 的 Spearman correlation\", \"log_path\": \"/tmp/token_importance.log\", \"model_name\": \"imm_anchor_v8b_twostage\", \"plan_id\": \"plan_009\", \"seed\": 42, \"server\": \"westd-27271\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-16T17:06:47.705Z\"}, \"plan_011_acis_overhead\": {\"completed_at\": \"2026-05-16T16:28:15.584Z\", \"conclusion\": \"success\", \"created_at\": \"2026-05-16T16:27:51.008Z\", \"hypothesis\": \"ACIS 模块的参数量、FLOPs、推理延迟量化，证明 deployment cost 可忽略\", \"metrics\": {\"flops_acis_increment_M\": 409.75, \"flops_baseline_G\": 169.87, \"flops_overhead_pct\": 0.24, \"latency_acis_increment_ms\": 0.32, \"latency_baseline_ms\": 51.16, \"latency_overhead_pct\": 0.63, \"n_trials\": 100, \"params_acis_increment_M\": 3.46, \"params_baseline_M\": 451.53, \"params_overhead_pct\": 0.77, \"source\": \"results/acis_overhead.json\"}, \"retry_count\": 0, \"spec\": {\"checkpoint_path\": \"checkpoints/imm_anchor_v8b_twostage/final/checkpoint.pt\", \"command\": \"python eval_acis_overhead.py --checkpoint checkpoints/imm_anchor_v8b_twostage/final/checkpoint.pt --n_trials 100 --output results/acis_overhead.json\", \"data_count\": 100, \"data_path\": \"/root/autodl-tmp/importance_margin_vla_compress\", \"gpu_ids\": [\"cuda:0\"], \"hypothesis\": \"ACIS模块的参数量、FLOPs、推理延迟量化，证明deployment cost可忽略\", \"log_path\": \"/tmp/acis_overhead2.log\", \"model_name\": \"SmolVLA+ACIS (v8b_twostage)\", \"plan_id\": \"plan_011\", \"seed\": 42, \"server\": \"westd-27271\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-16T16:29:35.118Z\"}, \"plan_008_pruning_sweep_v2\": {\"completed_at\": \"2026-05-16T16:18:40.100Z\", \"conclusion\": \"success\", \"created_at\": \"2026-05-16T15:20:12.616Z\", \"hypothesis\": \"ACIS pruning 在不同 k_ratio (0.3-0.9) 下的 G3 曲线，验证 denoising effect 和 optimal compression point (v2 fix KeyError preprocess_batch)\", \"metrics\": {\"G3_best\": 0.237, \"G3_best_k\": 0.6, \"G3_k05\": 0.24, \"improvement_pct\": 76.2, \"source\": \"eval_results/pruning_sweep_v2.json\", \"sweet_spot\": \"k=0.5-0.6\"}, \"retry_count\": 0, \"spec\": {\"checkpoint_path\": \"eval_results/pruning_sweep_v2.json\", \"checkpoint_source\": \"checkpoints/imm_anchor_v8b_twostage/final/checkpoint.pt\", \"command\": \"CUDA_VISIBLE_DEVICES=1 python eval_pruning_sweep.py --checkpoint checkpoints/imm_anchor_v8b_twostage/final/checkpoint.pt --num_batches 500 --output eval_results/pruning_sweep_v2.json\", \"data_count\": 500, \"data_path\": \"lerobot/aloha_sim_insertion_scripted_image\", \"eval_data\": \"lerobot/aloha_sim_insertion_scripted_image\", \"hypothesis\": \"ACIS pruning 在不同 k_ratio (0.3-0.9) 下的 G3 曲线，验证 denoising effect 和 optimal compression point (v2 fix KeyError)\", \"log_path\": \"eval_results/pruning_sweep_v2.log\", \"model_name\": \"imm_anchor_v8b_twostage\", \"pid\": 207411, \"seed\": 42, \"server\": \"westd-27271\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-16T16:18:40.100Z\"}, \"plan_005_formal_bound_v2\": {\"completed_at\": \"2026-05-16T16:17:57.022Z\", \"conclusion\": \"success\", \"created_at\": \"2026-05-16T15:33:16.146Z\", \"hypothesis\": \"Formal bound 实证验证: 多 ε 水平 (0.005-0.1) 下测量 top-k stability，绘制 theoretical vs empirical bound 对比图 (v2 fix AttributeError)\", \"metrics\": {\"L_empirical\": 0.193, \"L_spectral\": 1.067, \"margin_median\": 0.96, \"source\": \"results/formal_bound_plan005.json\", \"stability_eps01\": 0.976, \"tightness_spectral_max\": 1.125, \"tightness_spectral_min\": 1.005}, \"retry_count\": 0, \"spec\": {\"account\": \"root\", \"backend\": \"tmux\", \"checkpoint_path\": \"results/formal_bound_plan005.json\", \"command\": \"python eval_formal_bound.py --checkpoint checkpoints/imm_anchor_v8b_twostage/final/checkpoint.pt --num_batches 500\", \"data_count\": 500, \"data_path\": \"lerobot/aloha_sim_insertion_scripted_image\", \"gpu\": [\"cuda:0\"], \"gpu_hours\": 0.74, \"log_path\": \"~/runs/importance_margin_vla_compress/plan_005_formal_bound_v2.log\", \"model_name\": \"imm_anchor_v8b_twostage\", \"pid\": \"208269\", \"seed\": 42, \"server\": \"westd-27271\", \"submitted_at\": \"2026-05-16T15:33:16.093Z\", \"submitted_via\": \"submit_training_job\", \"wall_clock_seconds\": 2680.9}, \"status\": \"DONE\", \"updated_at\": \"2026-05-16T16:17:57.022Z\"}, \"plan_008_pruning_sweep\": {\"completed_at\": \"2026-05-16T15:11:43.357Z\", \"conclusion\": \"failed\", \"created_at\": \"2026-05-16T14:49:22.988Z\", \"hypothesis\": \"ACIS pruning 在不同 k_ratio 下的 G3 曲线，验证 denoising effect 和 optimal compression point\", \"retry_count\": 0, \"spec\": {\"account\": \"root\", \"backend\": \"tmux\", \"command\": \"python eval_pruning_sweep.py --checkpoint checkpoints/imm_anchor_v8b_twostage/final/checkpoint.pt --num_batches 500\", \"data_count\": 500, \"data_path\": \"LIBERO eval\", \"gpu\": [\"cuda:1\"], \"gpu_hours\": 0.37, \"log_path\": \"~/runs/importance_margin_vla_compress/plan_008_pruning_sweep.log\", \"model_name\": \"imm_anchor_v8b_twostage\", \"pid\": \"200578\", \"seed\": 42, \"server\": \"westd-27271\", \"submitted_at\": \"2026-05-16T14:49:22.931Z\", \"submitted_via\": \"submit_training_job\", \"wall_clock_seconds\": 1340.4}, \"status\": \"DONE\", \"updated_at\": \"2026-05-16T15:11:43.356Z\"}, \"baseline_v6_alpha16\": {\"checkpoint_path\": \"checkpoints/baseline_v6_alpha16/step_029999/checkpoint.pt\", \"completed_at\": \"2026-05-16T11:04:21.593Z\", \"conclusion\": \"negative\", \"created_at\": \"2026-05-16T08:40:58.566Z\", \"hypothesis\": \"降低 LoRA alpha (64→16, scale 2.0→0.5) 避免 flow matching velocity field mode collapse，恢复 sample_actions() diversity\", \"log_path\": \"~/runs/importance_margin_vla_compress/baseline_v6_alpha16.log\", \"metrics\": {\"mode_collapse_test\": {\"checkpoint\": \"checkpoints/baseline_v6_alpha16/step_029999/checkpoint.pt\", \"comparison_alpha64\": \"alpha64 std=0.006, alpha16 std=0.007 — no meaningful improvement\", \"cross_obs_std\": 0.096329, \"noise_diversity_std\": 0.007352, \"pretrained_noise_std\": null, \"threshold_fail\": 0.01, \"threshold_pass\": 0.05, \"verdict\": \"FAIL\"}}, \"notes\": \"Mode collapse 未修复。alpha=16 (scale=0.5) noise diversity std=0.007352 < 0.01 阈值，与 alpha=64 的 std=0.006 几乎无改善。Cross-obs std=0.096 尚可（不同 obs 产生不同 action），但 same-obs noise diversity 极低，说明 ODE 仍然 collapse 到固定点。问题根源不在 LoRA scale 大小，可能在 flow matching + LoRA 的根本兼容性上。未执行 success rate 评估（mode collapse 导致 0% success rate 是确定的）。\", \"retry_count\": 0, \"spec\": {\"account\": \"root\", \"backend\": \"tmux\", \"command\": \"CUDA_VISIBLE_DEVICES=1 python train.py --config configs/baseline_v6_alpha16.yaml\", \"data_count\": null, \"data_path\": \"lerobot/aloha_sim_insertion_scripted_image\", \"gpu\": [\"cuda:1\"], \"gpu_hours\": 2.39, \"log_path\": \"~/runs/importance_margin_vla_compress/baseline_v6_alpha16.log\", \"model_name\": \"smolvla_base + LoRA(r=32, alpha=16)\", \"pid\": \"160901\", \"seed\": 42, \"server\": \"westd-27271\", \"submitted_at\": \"2026-05-16T08:40:58.524Z\", \"submitted_via\": \"submit_training_job\", \"wall_clock_seconds\": 8603.1}, \"status\": \"DONE\", \"updated_at\": \"2026-05-16T11:04:21.593Z\"}, \"mvp_imm_v8c_annealing\": {\"checkpoint_path\": \"checkpoints/imm_anchor_v8c_annealing/step_029999\", \"completed_at\": \"2026-05-16T10:58:36.135Z\", \"conclusion\": \"negative\", \"created_at\": \"2026-05-16T07:07:51.506Z\", \"hypothesis\": \"Mask ratio annealing (k_ratio 0.9→0.5 线性退火) + gradient isolation (λ=0.5)。渐进引入 pruning 避免 backbone co-adaptation with sudden sparse input，目标 G3-deploy ≤ 1.10\", \"log_path\": \"eval_results/gate_report_v8c_final.json\", \"metrics\": {\"G1_margin_ratio\": 108.15, \"G2_preservation_diff\": 60.92, \"G3_deploy\": 2.04, \"G4_LED\": 0.1046, \"action_loss_acis_prune\": null, \"action_loss_baseline\": null, \"final_action_loss\": 0.0023, \"final_margin_loss\": 0.0938, \"final_train_loss\": 0.0492}, \"retry_count\": 0, \"spec\": {\"account\": \"root\", \"backend\": \"tmux\", \"command\": \"bash -c \\\"source /etc/network_turbo && export HF_HOME=/root/autodl-tmp/.hf_cache && export REQUESTS_CA_BUNDLE=/etc/ssl/certs/ca-certificates.crt && export SSL_CERT_FILE=/etc/ssl/certs/ca-certificates.crt && export WANDB_MODE=offline && export HF_HUB_DISABLE_XET=1 && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/importance_margin_vla_compress && python train.py --config configs/imm_anchor_v8c_annealing.yaml\\\"\", \"gpu\": [\"cuda:0\"], \"gpu_hours\": 3.19, \"log_path\": \"~/runs/importance_margin_vla_compress/mvp_imm_v8c_annealing.log\", \"pid\": \"151562\", \"server\": \"westd-27271\", \"submitted_at\": \"2026-05-16T07:46:57.804Z\", \"submitted_via\": \"submit_training_job\", \"wall_clock_seconds\": 11498.3}, \"status\": \"DONE\", \"updated_at\": \"2026-05-16T10:59:18.563Z\"}, \"mvp_imm_v8b_twostage\": {\"completed_at\": \"2026-05-16T07:05:42.085Z\", \"conclusion\": \"success\", \"created_at\": \"2026-05-16T04:17:57.529Z\", \"extra\": {\"hook_events\": [{\"action\": \"agent\", \"event\": \"on_failed\", \"ts\": \"2026-05-16T07:05:43.275570+00:00\"}]}, \"failure_reason\": \"process dead 5× with no sentinel/W&B — auto-resolved as failed\", \"hypothesis\": \"Two-stage training: 冻结 baseline_v5 backbone (含 LoRA)，Stage1 (10K) 只训 ACIS selector，Stage2 (20K) 解冻 LoRA 微调。消除 co-adaptation，目标 G3 ≤ 1.10\", \"metrics\": {\"sim_success_rate\": {\"acis_prune\": 0, \"acis_prune_mean_reward\": 0, \"baseline\": 0, \"baseline_mean_reward\": 0.16, \"bypass\": 0, \"bypass_mean_reward\": 0, \"n_episodes\": 50, \"wilson_ci_95_upper\": 0.0714}}, \"notes\": \"训练正常完成（Stage1 10K + Stage2 20K = 30K steps）。500-batch eval ALL GATES PASS: G1=93.23x, G2=+56.01pp, G3-deploy=0.8679 (ACIS+Prune50% 优于 baseline 13%), G4=0.1354。核心发现：two-stage 完全解耦 ACIS 和 backbone 训练后，ACIS pruning 不仅不损害性能，反而提升——50% token pruning 起正则化作用。ACIS+Prune loss=0.003538 < baseline 0.004063。这是首个通过全部 MVP gate 的实验。Stage 设计: Stage1 (0-10K) freeze backbone+LoRA 只训 ACIS (λ=1.0), Stage2 (10K-30K) freeze ACIS 只训 LoRA (三层防护)。基于 baseline_v5 checkpoint。\", \"parent\": \"mvp_imm_anchor_v8\", \"pid\": 136367, \"reproduce\": {\"finished_at\": \"2026-05-16T07:05:41.853Z\"}, \"retry_count\": 0, \"spec\": {\"account\": \"root\", \"backend\": \"tmux\", \"checkpoint_path\": \"checkpoints/imm_two_stage/\", \"checkpoint_source\": \"checkpoints/baseline_v5/ (mvp_baseline_v5 final checkpoint)\", \"command\": \"bash -c 'source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/importance_margin_vla_compress && python train_twostage.py --config configs/imm_anchor_v8b_twostage.yaml'\", \"config_path\": \"configs/imm_anchor_v8b_twostage.yaml\", \"data_count\": 20000, \"data_path\": \"lerobot/aloha_sim_insertion_scripted_image\", \"eval_data\": \"N/A (training experiment, not eval)\", \"gpu\": [\"cuda:1\"], \"gpu_hours\": 2.79, \"log_path\": \"~/runs/importance_margin_vla_compress/mvp_imm_v8b_twostage.log\", \"model_name\": \"lerobot/smolvla_base + LoRA r=32 + ACIS two-stage (stage1: ACIS-only lambda=1.0, stage2: LoRA+ACIS lambda=0.5)\", \"pid\": \"136367\", \"seed\": 42, \"server\": \"westd-27271\", \"submitted_at\": \"2026-05-16T04:18:10.534Z\", \"submitted_via\": \"submit_training_job\", \"tmux_session\": \"v8b_twostage\", \"wall_clock_seconds\": 10051.6}, \"status\": \"DONE\", \"updated_at\": \"2026-05-16T07:56:33.588Z\"}, \"mvp_imm_anchor_v8_1\": {\"completed_at\": \"2026-05-16T06:26:47.593Z\", \"conclusion\": \"negative\", \"created_at\": \"2026-05-16T03:02:09.076Z\", \"hypothesis\": \"gradient isolation + 降低 λ_margin (0.2 vs v8 的 0.5)，减轻 ACIS selection overhead 对 G3 的影响，目标 G3-deploy ≤ 1.10\", \"notes\": \"训练完成 30K steps。500-batch eval (fixed evaluate.py): G1=86.5x PASS, G2=+59.2pp PASS, G3-deploy=2.53x FAIL (目标≤1.10), G4=0.084 PASS → Overall FAIL。降低 λ (0.2 vs v8 的 0.5) 反而恶化 G3 (2.53x vs 1.344x)。机理：低 λ=0.2 → ACIS 收敛慢 → 训练早期 routing 信号不稳定 → backbone 学到劣质表征且无法恢复。v8 (λ=0.5) ACIS 收敛快 → routing 早期稳定 → backbone 表征质量更好（虽然仍 co-adapted）。bypass≈pruneFalse (9.32x vs 9.17x) 排除 ACIS 存在本身的开销，但 pruneTrue 2.53x 远优于 full tokens 说明 backbone 已严重 co-adapt 到 sparse input。结论：gradient isolation + 低 λ 不是解法。\", \"parent\": \"mvp_imm_anchor_v8\", \"retry_count\": 0, \"spec\": {\"checkpoint_path\": \"checkpoints/imm_anchor_v8_1/\", \"checkpoint_source\": \"N/A (training from scratch)\", \"command\": \"CUDA_VISIBLE_DEVICES=? python3 train.py --config configs/imm_anchor_v8_1.yaml\", \"data_count\": 20000, \"data_path\": \"lerobot/aloha_sim_insertion_scripted_image\", \"eval_data\": \"N/A (training experiment)\", \"gpu\": \"cuda:0\", \"log_path\": \"logs/v8_1_train.log\", \"model_name\": \"lerobot/smolvla_base + LoRA r=32 + IMM(delta=0.3, lambda=0.2, gradient_isolation=true)\", \"pid\": \"121326\", \"seed\": 42, \"server\": \"westd-27271\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-16T06:32:15.146Z\"}, \"mvp_imm_anchor_v8\": {\"completed_at\": \"2026-05-16T04:07:58.695Z\", \"conclusion\": \"negative\", \"created_at\": \"2026-05-15T23:07:33.075Z\", \"extra\": {\"hook_events\": [{\"action\": \"agent\", \"event\": \"on_complete\", \"ts\": \"2026-05-16T02:05:59.086501+00:00\"}]}, \"hypothesis\": \"gradient isolation (dual detach) 消除 backbone 权重损伤 (G3a≤1.10)，同时 ACIS 仍能学到有效 importance scoring (G1≥2x, G2≥10pp)\", \"metrics\": {\"baseline_v5_fixed\": {\"clean_action_loss\": 0.004063, \"eps001_preservation\": 0.3352, \"margin_median\": 0.010022, \"source\": \"eval_results/eval_baseline_v5_fixed.json\"}, \"checkpoint_trajectory\": {\"step_2000\": {\"acis_advantage\": 0.0068, \"acis_prune\": 0.0357, \"bypass\": 0.05842, \"random_prune\": 0.0425, \"standard\": 0.03787}, \"step_29999\": {\"acis_advantage\": 0.01246, \"acis_prune\": 0.0033, \"bypass\": 0.0323, \"random_prune\": 0.01576, \"standard\": 0.00659}}, \"eval_500batch_bypass_fixed\": {\"bypass_clean_action_loss\": 0.028948, \"bypass_pruned_action_loss\": 0.017215, \"eps001_action_loss_noprune\": 0.027873, \"eps001_action_loss_prune\": 0.016572, \"eps005_action_loss_noprune\": 0.039901, \"eps005_action_loss_prune\": 0.02627, \"source\": \"eval_results/eval_imm_v8_bypass_fixed.json\"}, \"eval_500batch_fixed\": {\"bypass_clean_action_loss\": 0.028948, \"eps001_kendall_tau\": 0.8393, \"eps001_led_median\": 0.0852, \"eps001_preservation\": 0.923, \"eps002_led_median\": 0.1714, \"eps002_preservation\": 0.8367, \"eps005_led_median\": 0.4429, \"eps005_preservation\": 0.6613, \"eval_tag\": \"D028_fix_reeval\", \"lipschitz_empirical\": 0.1364, \"lipschitz_spectral\": 1.0672, \"margin_mean\": 0.7696, \"margin_median\": 0.5034, \"margin_std\": 0.8133, \"pruneFalse_clean_action_loss\": 0.029996, \"pruneTrue_clean_action_loss\": 0.005462, \"source\": \"eval_results/eval_imm_v8_fixed.json\", \"standard_clean_action_loss\": 0.005462}, \"gate_analysis_fixed\": {\"G1_margin_ratio\": 50.2, \"G1_pass\": true, \"G2_pass\": true, \"G2_preservation_diff_pp\": 58.78, \"G3_clean_loss_ratio\": 1.344, \"G3_deploy_pass\": false, \"G3_deploy_ratio\": 1.344, \"G3_pass\": false, \"G3_target\": 1.1, \"G4_led_median\": 0.0865, \"G4_pass\": true, \"bypass_backbone_ratio\": 7.12, \"eval_tag\": \"D028_fix_reeval\", \"notes\": \"Fixed eval (5 bugs: eps0 pruning flag, hard binary mask, per-condition RNG, eval mode, preloaded batches). Results consistent with old buggy eval within ~5%. G3 still fails at 1.344x.\", \"overall_pass\": false}}, \"notes\": \"训练完成 (step 30K)。D028 fix re-eval (500-batch, fixed evaluate.py with 5 fixes): G1=50.2x PASS, G2=+58.8pp PASS, G3=1.344x FAIL (target ≤1.10), G4=0.087 PASS → Overall FAIL。Fixed eval 结果与 buggy eval 一致在 ~5% 内：standard_clean 0.00546 (was 0.00530), bypass_clean 0.02895 (was 0.03019), margin_median 0.5034 (was 0.505)。关键发现：(1) G4 LED 从 0.169 降至 0.087，修复显著影响了 LED 计算；(2) G3 从 1.30x 升至 1.34x；(3) bypass/baseline=7.12x 源于 backbone co-adaptation with token selection（训练时 backbone 适应了 soft mask 加权的 ~50% token 子集，移除 ACIS 后 input distribution shift 导致性能下降，非梯度泄漏）。证据：random 50% pruning (0.0172) 优于 full token (0.0290)，说明 backbone 已内化 sparse token 偏好。结论：gradient isolation 有效防止梯度泄漏，但 backbone-ACIS co-adaptation 仍导致 G3=1.344x 超标。\", \"parent\": \"mvp_imm_anchor_v7_2\", \"reproduce\": {\"finished_at\": \"2026-05-16T02:05:58.213Z\"}, \"retry_count\": 0, \"spec\": {\"checkpoint_path\": \"checkpoints/imm_anchor_v8/\", \"checkpoint_source\": \"N/A (training from scratch)\", \"command\": \"CUDA_VISIBLE_DEVICES=0 python3 train.py --config configs/imm_anchor_v8.yaml\", \"data_count\": 20000, \"data_path\": \"lerobot/aloha_sim_insertion_scripted_image\", \"eval_data\": \"N/A (training experiment)\", \"gpu\": \"cuda:0\", \"log_path\": \"~/runs/importance_margin_vla_compress/mvp_imm_anchor_v8.log\", \"model_name\": \"lerobot/smolvla_base + LoRA r=32 + IMM(delta=0.3, lambda=0.5, gradient_isolation=true)\", \"pid\": \"86610\", \"seed\": 42, \"server\": \"westd-27271\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-16T04:09:35.392Z\"}, \"mvp_baseline_v5\": {\"completed_at\": \"2026-05-15T17:58:14.330Z\", \"conclusion\": \"success\", \"created_at\": \"2026-05-15T15:36:06.963Z\", \"hypothesis\": \"SmolVLA+LoRA baseline on aloha_sim_insertion (baseline_forward fix, v5 clean env)\", \"metrics\": {\"eval_500batch\": {\"clean_action_loss\": 0.004077, \"clean_margin_median\": 0.010022, \"eps001_preservation\": 0.3352, \"eps002_preservation\": 0.3362, \"eps005_preservation\": 0.3381}, \"mid_checkpoints\": {\"step005000\": {\"clean_action_loss\": 0.01891, \"clean_margin_mean\": 0.01608, \"clean_margin_median\": 0.01002, \"clean_pruned_action_loss\": 0.08304, \"eps001_action_loss\": 0.02234, \"eps001_kendall_tau\": -0.2315, \"eps001_preservation\": 0.3359, \"eps001_pruned_action_loss\": 0.08645, \"eps002_action_loss\": 0.02057, \"eps002_preservation\": 0.3369, \"eps002_pruned_action_loss\": 0.0882, \"eps005_action_loss\": 0.03377, \"eps005_preservation\": 0.34, \"eps005_pruned_action_loss\": 0.0912, \"lipschitz_empirical\": 0, \"lipschitz_spectral\": 0, \"source\": \"eval_results/eval_baseline_v5_step5000.json\"}, \"step010000\": {\"clean_action_loss\": 0.00974, \"clean_margin_mean\": 0.01608, \"clean_margin_median\": 0.01002, \"clean_pruned_action_loss\": 0.09434, \"eps001_action_loss\": 0.01243, \"eps001_kendall_tau\": -0.2315, \"eps001_preservation\": 0.3359, \"eps001_pruned_action_loss\": 0.09473, \"eps002_action_loss\": 0.01092, \"eps002_preservation\": 0.3369, \"eps002_pruned_action_loss\": 0.10085, \"eps005_action_loss\": 0.02565, \"eps005_preservation\": 0.34, \"eps005_pruned_action_loss\": 0.10132, \"lipschitz_empirical\": 0, \"lipschitz_spectral\": 0, \"source\": \"eval_results/eval_baseline_v5_step10000.json\"}}, \"source\": \"eval_results/eval_baseline_v5_final.json\"}, \"notes\": \"Original eval (100 batches, pre-D011): clean=0.00422. D011 re-eval (50 batches, fixed baseline_forward+pruning): clean=0.00264, pruneTrue=0.11159. D011 fix changed baseline_forward sig + preprocess_batch + connector name, so clean path value changed too. D014 protocol: redo with 500 batches after v7 completes.\", \"retry_count\": 0, \"spec\": {\"checkpoint_path\": \"checkpoints/baseline/step_029999\", \"command\": \"CUDA_VISIBLE_DEVICES=0 WANDB_MODE=offline python3 train.py --config configs/baseline.yaml\", \"data_count\": 20000, \"data_path\": \"lerobot/aloha_sim_insertion_scripted_image\", \"eval_results\": {\"clean_no_prune\": 0.00422, \"clean_prune50\": 0.00309, \"eps001_no_prune\": 0.00605, \"eps001_prune50\": 0.00343, \"eps002_no_prune\": 0.00399, \"eps002_prune50\": 0.00445, \"eps005_no_prune\": 0.00495, \"eps005_prune50\": 0.00497}, \"gpu\": \"cuda:0\", \"log_path\": \"/tmp/baseline_v5.log\", \"model_name\": \"lerobot/smolvla_base + LoRA r=32\", \"pid\": 31871, \"seed\": 42, \"server\": \"westd-27271\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-15T22:21:59.760Z\"}, \"mvp_imm_anchor_v7_1\": {\"completed_at\": \"2026-05-15T19:18:02.335Z\", \"conclusion\": \"failed\", \"created_at\": \"2026-05-15T18:19:52.057Z\", \"hypothesis\": \"降低 lambda_margin (0.2 vs 0.5) 可以在保持 margin 增长的同时抑制 Lipschitz 爆炸\", \"parent\": \"mvp_imm_anchor_v7\", \"retry_count\": 0, \"spec\": {\"account\": \"root\", \"backend\": \"tmux\", \"checkpoint_path\": \"N/A\", \"checkpoint_source\": \"N/A (training from scratch)\", \"command\": \"bash -c \\\"source /etc/network_turbo ... && python3 train.py --config configs/imm_anchor_v7_1.yaml\\\"\", \"data_count\": 20000, \"data_path\": \"lerobot/aloha_sim_insertion_scripted_image\", \"eval_data\": \"N/A (training experiment)\", \"failure_reason\": \"eval mode leak in compute_empirical_lipschitz(): acis.eval() never restored to train(). Spectral norm power iteration stopped at step 500. SN: 1.014→2.485→4.617. Training data invalid from step 500.\", \"gpu\": \"cuda:0\", \"gpu_hours\": 0.28, \"log_path\": \"/tmp/imm_anchor_v7_1.log\", \"model_name\": \"lerobot/smolvla_base + LoRA r=32 + IMM(delta=0.3, lambda=0.2, grad_clip=30.0)\", \"pid\": \"53500\", \"seed\": 42, \"server\": \"westd-27271\", \"submitted_at\": \"2026-05-15T19:01:30.975Z\", \"submitted_via\": \"submit_training_job\", \"wall_clock_seconds\": 991.4}, \"status\": \"DONE\", \"updated_at\": \"2026-05-15T19:18:02.335Z\"}, \"mvp_imm_anchor_v6\": {\"completed_at\": \"2026-05-15T17:01:43.153Z\", \"conclusion\": \"failed\", \"created_at\": \"2026-05-15T16:30:47.843Z\", \"hypothesis\": \"IMM training (delta=0.3, lambda=0.5) - fixed token_selection squeeze bug\", \"notes\": \"v5 crashed at step 2000 during eval due to token_selection.py squeeze bug (threshold_low.squeeze(-1) shape mismatch). v6 = fresh start with squeeze fix. Same config: imm_anchor.yaml (delta=0.3, lambda=0.5, k_ratio=0.5). batch_size=4 + FP32 to match baseline v5 for fair comparison.\", \"parent\": \"mvp_imm_anchor_v5\", \"retry_count\": 0, \"spec\": {\"checkpoint_path\": \"N/A\", \"command\": \"CUDA_VISIBLE_DEVICES=1 WANDB_MODE=offline python3 train.py --config configs/imm_anchor.yaml\", \"data_count\": 20000, \"data_path\": \"lerobot/aloha_sim_insertion_scripted_image\", \"failure_reason\": \"Crashed at step 2000 during eval — RoPE position embedding dimension mismatch (50 vs 82) in smolvlm_with_expert.py:384 forward_cross_attn_layer. Squeeze fix worked but eval path has separate bug.\", \"gpu\": \"cuda:1\", \"log_path\": \"/tmp/imm_anchor_v6.log\", \"model_name\": \"lerobot/smolvla_base + LoRA r=32 + IMM(delta=0.3, lambda=0.5)\", \"pid\": 35412, \"seed\": 42, \"server\": \"westd-27271\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-15T17:01:43.153Z\"}, \"mvp_imm_anchor_v5\": {\"completed_at\": \"2026-05-15T16:30:56.416Z\", \"conclusion\": \"failed\", \"created_at\": \"2026-05-15T15:30:48.331Z\", \"hypothesis\": \"IMM training (delta=0.3, lambda=0.5) increases importance margin without degrading action loss\", \"retry_count\": 0, \"spec\": {\"checkpoint_path\": \"N/A\", \"command\": \"CUDA_VISIBLE_DEVICES=1 WANDB_MODE=offline python3 train.py --config configs/imm_anchor.yaml\", \"data_count\": 20000, \"data_path\": \"lerobot/aloha_sim_insertion_scripted_image\", \"failure_reason\": \"Crashed at step 2000 eval - token_selection.py _hard_forward() squeeze bug: threshold_low.squeeze(-1) shape (B,) can't broadcast with scores shape (B,64)\", \"gpu\": \"cuda:1\", \"log_path\": \"/tmp/imm_anchor_v5.log\", \"model_name\": \"lerobot/smolvla_base + LoRA r=32 + IMM(delta=0.3, lambda=0.5)\", \"pid\": 32009, \"seed\": 42, \"server\": \"westd-27271\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-15T16:30:56.416Z\"}, \"mvp_baseline_v4\": {\"completed_at\": \"2026-05-15T15:32:16.909Z\", \"conclusion\": \"killed\", \"created_at\": \"2026-05-15T15:28:19.155Z\", \"hypothesis\": \"SmolVLA+LoRA baseline on aloha_sim_insertion establishes action loss reference for IMM comparison (fixed action_is_pad bug)\", \"retry_count\": 0, \"spec\": {\"account\": \"root\", \"checkpoint_path\": \"N/A\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/importance_margin_vla_compress && CUDA_VISIBLE_DEVICES=0 HF_HUB_OFFLINE=0 WANDB_MODE=offline python3 train.py --config configs/baseline.yaml --gpu 0 --seed 42\\\"\", \"data_count\": 20000, \"data_path\": \"lerobot/aloha_sim_insertion_scripted_image\", \"failure_reason\": \"Killed for v5 restart with complete env template (network_turbo + SSL). Was healthy at step 600+.\", \"gpu\": \"cuda:0\", \"log_path\": \"/tmp/baseline_v4.log\", \"model_name\": \"lerobot/smolvla_base + LoRA r=32 (baseline_forward fix)\", \"pid\": 30745, \"seed\": 42, \"server\": \"westd-27271\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-15T15:32:16.908Z\"}, \"mvp_imm_anchor_v4\": {\"completed_at\": \"2026-05-15T15:29:41.858Z\", \"conclusion\": \"failed\", \"created_at\": \"2026-05-15T15:00:15.534Z\", \"hypothesis\": \"IMM training (delta=0.3, lambda=0.5) significantly increases importance margin and top-k preservation without degrading action loss\", \"retry_count\": 0, \"spec\": {\"account\": \"root\", \"backend\": \"tmux\", \"checkpoint_path\": \"N/A\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/importance_margin_vla_compress && HF_HUB_OFFLINE=0 WANDB_MODE=offline python3 train.py --config configs/imm_anchor.yaml --gpu 0 --seed 42\\\"\", \"data_count\": 20000, \"data_path\": \"lerobot/aloha_sim_insertion_scripted_image\", \"failure_reason\": \"OSError: Can't load SmolVLM2-500M-Video-Instruct config. submit_training_job command missing network_turbo + SSL cert setup.\", \"gpu\": \"cuda:1\", \"gpu_hours\": 0.48, \"log_path\": \"~/runs/importance_margin_vla_compress/mvp_imm_anchor_v4.log\", \"model_name\": \"lerobot/smolvla_base + LoRA r=32 + IMM(delta=0.3, lambda=0.5)\", \"pid\": 28012, \"seed\": 42, \"server\": \"westd-27271\", \"submitted_at\": \"2026-05-15T15:00:52.935Z\", \"submitted_via\": \"submit_training_job\", \"wall_clock_seconds\": 1728.9}, \"status\": \"DONE\", \"updated_at\": \"2026-05-15T15:29:41.858Z\"}, \"mvp_baseline_v3\": {\"completed_at\": \"2026-05-15T14:57:00.161Z\", \"conclusion\": \"failed\", \"created_at\": \"2026-05-15T14:55:28.972Z\", \"hypothesis\": \"SmolVLA+LoRA baseline on aloha_sim_insertion establishes action loss reference for IMM comparison\", \"retry_count\": 0, \"spec\": {\"account\": \"root\", \"checkpoint_path\": \"N/A\", \"command\": \"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/importance_margin_vla_compress && python train.py --config configs/baseline.yaml --gpu 0 --seed 42 --wandb_run baseline_seed42\", \"data_count\": 20000, \"data_path\": \"lerobot/aloha_sim_insertion_scripted_image\", \"failure_reason\": \"Submitted before VLM backbone verified. Director ordered stop.\", \"gpu\": \"cuda:0\", \"log_path\": \"N/A\", \"model_name\": \"lerobot/smolvla_base + LoRA r=32\", \"pid\": 26017, \"seed\": 42, \"server\": \"westd-27271\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-15T14:57:00.161Z\"}, \"mvp_imm_anchor_v2\": {\"completed_at\": \"2026-05-15T14:56:58.869Z\", \"conclusion\": \"failed\", \"created_at\": \"2026-05-15T14:47:42.413Z\", \"hypothesis\": \"IMM training (delta=0.3, lambda=0.5) significantly increases importance margin and top-k preservation without degrading action loss\", \"retry_count\": 0, \"spec\": {\"checkpoint_path\": \"N/A\", \"command\": \"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/importance_margin_vla_compress && python train.py --config configs/imm_anchor.yaml --gpu 1 --seed 42 --wandb_run imm_d03_l05_seed42\", \"data_count\": 20000, \"data_path\": \"lerobot/aloha_sim_insertion_scripted_image\", \"failure_reason\": \"Placeholder experiment; VLM backbone not yet verified. Director ordered stop.\", \"gpu\": \"cuda:1\", \"log_path\": \"N/A\", \"model_name\": \"lerobot/smolvla_base + LoRA r=32 + IMM(delta=0.3, lambda=0.5)\", \"pid\": 26092, \"seed\": 42, \"server\": \"westd-27271\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-15T14:56:58.869Z\"}, \"mvp_baseline_v2\": {\"completed_at\": \"2026-05-15T14:55:25.052Z\", \"conclusion\": \"failed\", \"created_at\": \"2026-05-15T14:47:41.949Z\", \"extra\": {\"hook_events\": [{\"action\": \"agent\", \"event\": \"on_complete\", \"ts\": \"2026-05-15T14:54:23.542535+00:00\"}]}, \"hypothesis\": \"SmolVLA+LoRA baseline on aloha_sim_insertion establishes action loss reference for IMM comparison\", \"reproduce\": {\"finished_at\": \"2026-05-15T14:54:22.866Z\"}, \"retry_count\": 0, \"spec\": {\"account\": \"root\", \"backend\": \"tmux\", \"checkpoint_path\": \"N/A\", \"command\": \"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/importance_margin_vla_compress && python train.py --config configs/baseline.yaml --gpu 0 --seed 42 --wandb_run baseline_seed42\", \"data_count\": 20000, \"data_path\": \"lerobot/aloha_sim_insertion_scripted_image\", \"failure_reason\": \"dummy submit_training_job echo command auto-completed; actual training restarted as mvp_baseline_v3\", \"gpu\": \"cuda:0\", \"gpu_hours\": 0.12, \"log_path\": \"N/A\", \"model_name\": \"lerobot/smolvla_base + LoRA r=32\", \"pid\": 26017, \"seed\": 42, \"server\": \"westd-27271\", \"submitted_at\": \"2026-05-15T14:48:01.586Z\", \"submitted_via\": \"submit_training_job\", \"wall_clock_seconds\": 443.5}, \"status\": \"DONE\", \"updated_at\": \"2026-05-15T14:55:25.052Z\"}, \"mvp_imm_anchor\": {\"completed_at\": \"2026-05-15T14:43:21.554Z\", \"conclusion\": \"failed\", \"created_at\": \"2026-05-15T12:27:58.507Z\", \"hypothesis\": \"IMM training (delta=0.3, lambda=0.5) significantly increases Δ_k margin and top-k preservation without degrading action loss\", \"retry_count\": 0, \"spec\": {\"account\": \"root\", \"backend\": \"tmux\", \"command\": \"python train.py --config configs/imm_anchor.yaml --gpu 0 --seed 42 --wandb_run imm_d03_l05_seed42\", \"data_count\": 20000, \"data_path\": \"lerobot/aloha_sim_insertion_scripted_image\", \"gpu\": \"cuda:1\", \"gpu_hours\": 0.11, \"log_path\": \"~/runs/importance_margin_vla_compress/mvp_imm_anchor.log\", \"model_name\": \"lerobot/smolvla_base + LoRA r=32 + IMM(delta=0.3, lambda=0.5)\", \"pid\": 23428, \"seed\": 42, \"server\": \"westd-27271\", \"submitted_at\": \"2026-05-15T14:36:29.187Z\", \"submitted_via\": \"submit_training_job\", \"wall_clock_seconds\": 412.4}, \"status\": \"DONE\", \"updated_at\": \"2026-05-15T14:43:21.554Z\"}, \"mvp_baseline\": {\"completed_at\": \"2026-05-15T14:43:17.783Z\", \"conclusion\": \"failed\", \"created_at\": \"2026-05-15T11:50:53.011Z\", \"hypothesis\": \"SmolVLA+LoRA baseline on LIBERO-Object establishes action loss reference for IMM comparison\", \"retry_count\": 0, \"spec\": {\"account\": \"root\", \"backend\": \"tmux\", \"command\": \"python train.py --config configs/baseline.yaml --gpu 0 --seed 42 --wandb_run baseline_seed42\", \"data_count\": 20000, \"data_path\": \"lerobot/aloha_sim_insertion_scripted_image\", \"gpu\": \"cuda:0\", \"gpu_hours\": 0.11, \"log_path\": \"~/runs/importance_margin_vla_compress/mvp_baseline.log\", \"model_name\": \"lerobot/smolvla_base + LoRA r=32\", \"pid\": 23284, \"seed\": 42, \"server\": \"westd-27271\", \"submitted_at\": \"2026-05-15T14:36:23.989Z\", \"submitted_via\": \"submit_training_job\", \"wall_clock_seconds\": 413.8}, \"status\": \"DONE\", \"updated_at\": \"2026-05-15T14:43:17.783Z\"}, \"eval_oft_baseline_object_seed42_v2\": {\"conclusion\": \"failed\", \"created_at\": \"2026-05-21T02:37:32.165008+00:00\", \"hypothesis\": \"OFT Object baseline (no pruning). OFT uses 3-layer MLP connector with 512 vision tokens (DINOv2+SigLIP). Expected SR ≈ 97% (SOTA). Validates eval adapter.\", \"notes\": \"OFT eval params: --prune_mode (not --mode), --keep_ratio (not --k_ratio), --checkpoint (required). Bugs fixed: AutoModelForImageTextToText, DDP module. prefix strip, torch.load weights_only. [M049] 0% SR — missing center_crop (crop_scale=0.9) and potentially other preprocessing mismatches vs OFT official inference code.\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=2 python eval_oft_libero.py --checkpoint /root/autodl-tmp/openvla-oft-libero-object --suite libero_object --prune_mode none --keep_ratio 1.0 --seed 42\", \"data_count\": 500, \"data_path\": \"libero_object\", \"gpu\": \"cuda:2\", \"model_name\": \"openvla-7b-oft-finetuned-libero-object\", \"pid\": 370074, \"seed\": 42, \"server\": \"westd-38929\"}, \"status\": \"DONE\"}, \"eval_openvla_prune_l2norm_k03_seed42\": {\"conclusion\": \"success\", \"created_at\": \"2026-05-21T02:22:08.929927+00:00\", \"hypothesis\": \"L2 norm pruning k=0.3 on OpenVLA Object, seed42. Baseline=74.4%.\", \"metrics\": {\"num_episodes\": 500, \"seed\": 42, \"success_rate\": 0.25, \"suite\": \"libero_object\"}, \"notes\": \"[D124] Registered from westd-38929 eval_results.\", \"spec\": {\"data_path\": \"libero_object\", \"model_name\": \"openvla-7b-finetuned-libero-object\", \"server\": \"westd-38929\"}, \"status\": \"DONE\"}, \"eval_openvla_prune_l2norm_k05_seed42\": {\"conclusion\": \"success\", \"created_at\": \"2026-05-21T02:22:08.929921+00:00\", \"hypothesis\": \"L2 norm pruning k=0.5 on OpenVLA Object, seed42. Baseline=74.4%.\", \"metrics\": {\"num_episodes\": 500, \"seed\": 42, \"success_rate\": 0.392, \"suite\": \"libero_object\"}, \"notes\": \"[D124] Registered from westd-38929 eval_results.\", \"spec\": {\"data_path\": \"libero_object\", \"model_name\": \"openvla-7b-finetuned-libero-object\", \"server\": \"westd-38929\"}, \"status\": \"DONE\"}, \"eval_openvla_prune_l2norm_k095_seed42\": {\"conclusion\": \"success\", \"created_at\": \"2026-05-21T02:22:08.929849+00:00\", \"hypothesis\": \"L2 norm pruning k=0.95 on OpenVLA Object, seed42. Baseline=74.4%.\", \"metrics\": {\"num_episodes\": 500, \"seed\": 42, \"success_rate\": 0.706, \"suite\": \"libero_object\"}, \"notes\": \"[D124] Registered from westd-38929 eval_results.\", \"spec\": {\"data_path\": \"libero_object\", \"model_name\": \"openvla-7b-finetuned-libero-object\", \"server\": \"westd-38929\"}, \"status\": \"DONE\"}, \"eval_openvla_prune_l2norm_k09_seed42\": {\"conclusion\": \"success\", \"created_at\": \"2026-05-21T02:22:08.929912+00:00\", \"hypothesis\": \"L2 norm pruning k=0.9 on OpenVLA Object, seed42. Baseline=74.4%.\", \"metrics\": {\"num_episodes\": 500, \"seed\": 42, \"success_rate\": 0.706, \"suite\": \"libero_object\"}, \"notes\": \"[D124] Registered from westd-38929 eval_results.\", \"spec\": {\"data_path\": \"libero_object\", \"model_name\": \"openvla-7b-finetuned-libero-object\", \"server\": \"westd-38929\"}, \"status\": \"DONE\"}}, \"count\": 697, \"total\": 697, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.9999}}"
    }
  }
}
```

&lt;/details>

---


````

---

### Assistant

_source line 10_

<details><summary>Logged reasoning block</summary>

```text
The registry result is very large. Let me query more specifically for the X-VLA experiments I need.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "790dcd4a-6607-4659-a5a3-a960215f6b9a",
  "uuid": "0ebe54a3-8153-4bc4-9620-e415f2ffe0d6",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017wXkaQeqUV5k8uY4z61oZC",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 509,
      "cache_read_input_tokens": 24756,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 509
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

_source line 11_

Let me query more specifically for the data I need.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "790dcd4a-6607-4659-a5a3-a960215f6b9a",
  "uuid": "67a19e9f-a934-4d3f-b062-b765ef2a18d8",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017wXkaQeqUV5k8uY4z61oZC",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 509,
      "cache_read_input_tokens": 24756,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 509
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

_source line 12_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry · `toolu_01DecmAGLMTGD5zm3aNB9qJM`</summary>

```json
{
  "project": "importance_margin_vla_compress",
  "filters": {
    "name_pattern": "eval_xvla"
  },
  "limit": 0,
  "fields": [
    "name",
    "metrics",
    "conclusion"
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
  "session_id": "790dcd4a-6607-4659-a5a3-a960215f6b9a",
  "uuid": "78baa429-cd24-4f5c-afd6-6339ca578917",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017wXkaQeqUV5k8uY4z61oZC",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 509,
      "cache_read_input_tokens": 24756,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 509
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

_source line 13 · 2026-05-26T07:47:35.091Z_

<details><summary>↩ Tool result · `toolu_01DecmAGLMTGD5zm3aNB9qJM`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"experiments\": {}, \"count\": 0, \"total\": 0, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 3.6411}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "790dcd4a-6607-4659-a5a3-a960215f6b9a",
  "uuid": "49ccaf79-95fe-420d-a422-f3361369a7d3",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"experiments\\\": {}, \\\"count\\\": 0, \\\"total\\\": 0, \\\"baseline\\\": null}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 3.6411}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"experiments\": {}, \"count\": 0, \"total\": 0, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 3.6411}}"
    }
  }
}
```

</details>

---


### Assistant

_source line 14_

<details><summary>Logged reasoning block</summary>

```text
No results with `name_pattern`. Let me try different filters or just search with a broader approach. Let me use Bash to search the registry file that was saved, looking for X-VLA related entries.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "790dcd4a-6607-4659-a5a3-a960215f6b9a",
  "uuid": "e4bee388-a4cd-4f1b-8a21-c9bf9cbe077b",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01S7jPDofgqJn6rF2zhHxgap",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 265,
      "cache_read_input_tokens": 25265,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 265
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

_source line 15_

<details open><summary>🔧 Tool call — Bash · `toolu_015YfZvJ5ap6ka8aQ8EaJ2nw`</summary>

```json
{
  "command": "cat /home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-be-idea-gen-0515-2-projects-importance-margin-vla-compress/790dcd4a-6607-4659-a5a3-a960215f6b9a/tool-results/mcp-agent-ml-research-read_registry-1779781647884.txt | python3 -c \"\nimport json, sys\ndata = json.loads(json.loads(sys.stdin.read())['result'])\nexps = data['data']['experiments']\n# Find X-VLA related experiments\nfor name, exp in exps.items():\n    if 'xvla' in name.lower() or 'x-vla' in name.lower() or 'x_vla' in name.lower():\n        print(f'=== {name} ===')\n        print(f'  metrics: {exp.get(\\\"metrics\\\", {})}')\n        print(f'  conclusion: {exp.get(\\\"conclusion\\\", \\\"\\\")}')\n        print()\n\" 2>&1 | head -200",
  "description": "Search registry data for X-VLA experiments"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "790dcd4a-6607-4659-a5a3-a960215f6b9a",
  "uuid": "97e96cc1-3581-44c3-8172-50b6307b1de6",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01S7jPDofgqJn6rF2zhHxgap",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 265,
      "cache_read_input_tokens": 25265,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 265
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

_source line 16 · 2026-05-26T07:47:41.253Z_

<details><summary>↩ Tool result · `toolu_015YfZvJ5ap6ka8aQ8EaJ2nw`</summary>

```text
=== eval_xvla_random_k05_spatial_seed43 ===
  metrics: {'overall_sr': 0.726, 'total_episodes': 500, 'total_successes': 363, 'wilson_ci_95': [0.685, 0.763], 'elapsed_min': 64.3}
  conclusion: success

=== eval_xvla_l2norm_k03_goal_seed42_v5 ===
  metrics: {'domain_id': 3, 'elapsed_min': 84, 'overall_sr': 0.37, 'per_task_sr': {'task0_open_drawer': 0.42, 'task1_bowl_on_stove': 0.92, 'task2_wine_on_cabinet': 0.2, 'task3_drawer_bowl': 0.24, 'task4_bowl_on_cabinet': 0.98, 'task5_push_plate': 0, 'task6_cream_cheese': 0.02, 'task7_turn_stove': 0.16, 'task8_bowl_on_plate': 0.76, 'task9_wine_on_rack': 0}, 'seed': 42, 'total_episodes': 500, 'total_success': 185, 'vision_tokens_kept': 15, 'vision_tokens_original': 50, 'wilson_ci_95': [0.3288, 0.4132]}
  conclusion: success

=== eval_xvla_l2norm_k03_long_seed42 ===
  metrics: {}
  conclusion: killed

=== eval_xvla_random_k03_long_seed42 ===
  metrics: {}
  conclusion: killed

=== eval_xvla_l2norm_k05_long_seed42_v4 ===
  metrics: {'elapsed_min': 94.6, 'overall_sr': 44.6, 'per_task_sr': {'T0_alphabet_soup_tomato_basket': 26, 'T1_cream_cheese_butter_basket': 0, 'T2_stove_moka_pot': 48, 'T3_black_bowl_drawer': 84, 'T4_mugs_on_plates': 36, 'T5_book_caddy': 88, 'T6_mug_plate_pudding': 48, 'T7_alphabet_soup_cream_cheese_basket': 78, 'T8_moka_pots_stove': 34, 'T9_mug_microwave': 4}, 'total_episodes': 500, 'total_success': 223}
  conclusion: success

=== eval_xvla_l2norm_k03_goal_seed42 ===
  metrics: {}
  conclusion: failed

=== eval_xvla_l2norm_k07_spatial_seed42_v2 ===
  metrics: {'overall_sr': 72.8, 'per_task_sr': {'task_0': 98, 'task_1': 42, 'task_2': 96, 'task_3': 94, 'task_4': 82, 'task_5': 0, 'task_6': 98, 'task_7': 34, 'task_8': 94, 'task_9': 90}, 'total_episodes': 500, 'total_success': 364}
  conclusion: success

=== eval_xvla_random_k085_long_seed42 ===
  metrics: {'cross_suite_k085': {'goal': 60.4, 'long': 35, 'object': 65, 'spatial': 68.2}, 'elapsed_min': 106.7, 'keep_ratio': 0.85, 'model': 'X-VLA', 'overall_sr': 35, 'per_task_sr': {'T0_alphabet_soup_tomato_sauce_basket': 54, 'T1_cream_cheese_butter_basket': 10, 'T2_stove_moka_pot': 16, 'T3_black_bowl_drawer': 88, 'T4_white_mug_left_yellow_mug_right': 2, 'T5_book_caddy': 98, 'T6_white_mug_chocolate_pudding': 0, 'T7_alphabet_soup_cream_cheese_basket': 48, 'T8_both_moka_pots_stove': 16, 'T9_mug_microwave': 18}, 'prune_mode': 'random', 'seed': 42, 'suite': 'libero_10', 'total_episodes': 500, 'total_success': 175, 'vs_k05_long': {'delta_pp': -26.6, 'k05_sr': 61.6, 'k085_sr': 35, 'non_monotonic': True}, 'wilson_ci_95': [30.9, 39.3]}
  conclusion: success

=== eval_xvla_l2norm_k03_goal_seed42_v2 ===
  metrics: {}
  conclusion: killed

=== eval_xvla_l2norm_k03_goal_seed42_v3 ===
  metrics: {'success_rate': 0.376, 'task_sr': {'task0_open_drawer': 0.42, 'task1_bowl_on_stove': 0.94, 'task2_wine_on_cabinet': 0.16, 'task3_drawer_bowl_inside': 0.24, 'task4_bowl_on_cabinet': 0.98, 'task5_push_plate': 0, 'task6_cream_in_bowl': 0.02, 'task7_turn_on_stove': 0.2, 'task8_bowl_on_plate': 0.8, 'task9_wine_on_rack': 0}, 'total_episodes': 500, 'total_successes': 188}
  conclusion: negative

=== eval_xvla_l2norm_k05_long_seed42_v3 ===
  metrics: {}
  conclusion: killed

=== eval_xvla_l2norm_k05_spatial_seed42_v2 ===
  metrics: {}
  conclusion: killed

=== eval_xvla_l2norm_k07_spatial_seed42 ===
  metrics: {'num_episodes': 500, 'num_success': 360, 'seed': 42, 'success_rate': 0.72, 'suite': 'libero_spatial'}
  conclusion: negative

=== eval_xvla_l2norm_k05_goal_seed42_v2 ===
  metrics: {'keep_ratio': 0.5, 'model': 'X-VLA', 'per_task_sr': {'T0_open_middle_drawer': 80, 'T1_put_bowl_on_stove': 92, 'T2_put_wine_bottle_on_cabinet': 98, 'T3_open_top_drawer_put_bowl': 34, 'T4_put_bowl_on_cabinet': 100, 'T5_push_plate_to_stove': 0, 'T6_put_cream_cheese_in_bowl': 24, 'T7_turn_on_stove': 72, 'T8_put_bowl_on_plate': 90, 'T9_put_wine_bottle_on_rack': 0}, 'prune_mode': 'l2_norm', 'seed': 42, 'success_rate': 0.59, 'suite': 'libero_goal', 'total_episodes': 500, 'total_successes': 295}
  conclusion: success

=== eval_xvla_l2norm_k05_goal_seed43 ===
  metrics: {'overall_SR': 0.602, 'per_task_SR': [0.84, 1, 0.98, 0.3, 1, 0, 0.22, 0.74, 0.9, 0.04], 'seed': 43, 'total_episodes': 500, 'total_successes': 301, 'wilson_ci_95': [0.5585, 0.644]}
  conclusion: negative

=== eval_xvla_random_k085_object_seed42 ===
  metrics: {'elapsed_seconds': 3572.9, 'overall_SR': 0.65, 'per_task_sr': [0.98, 0.14, 1, 0.88, 0.36, 0.96, 0, 0.94, 0.24, 1], 'total_episodes': 500, 'total_successes': 325, 'wilson_ci_95': [0.6072, 0.6905]}
  conclusion: success

=== eval_xvla_random_k085_spatial_seed42 ===
  metrics: {'overall_SR': 0.682, 'per_task': {'0': 1, '1': 0.06, '2': 0.98, '3': 0.98, '4': 0.82, '5': 0.06, '6': 1, '7': 0.04, '8': 0.92, '9': 0.96}, 'total_episodes': 500, 'wilson_ci_95': [0.6399, 0.7213]}
  conclusion: success

=== eval_xvla_random_k085_goal_seed42 ===
  metrics: {'overall_SR': 0.604, 'per_task': {'0': 1, '1': 0.42, '2': 0.7, '3': 0.78, '4': 0.98, '5': 0, '6': 0.02, '7': 0.88, '8': 0.98, '9': 0.28}, 'total_episodes': 500, 'wilson_ci_95': [0.5605, 0.6459]}
  conclusion: success

=== eval_xvla_l2norm_k05_long_seed43 ===
  metrics: {'elapsed_min': 94, 'overall_SR': 43.8, 'per_task_sr': {'T0': 26, 'T1': 0, 'T2': 52, 'T3': 78, 'T4': 38, 'T5': 86, 'T6': 56, 'T7': 76, 'T8': 24, 'T9': 2}, 'result_json': 'eval_results/xvla_prune_k0.5_libero_10.json', 'total_episodes': 500, 'total_successes': 219, 'wilson_ci_95': [39.5, 48.2]}
  conclusion: success

=== eval_xvla_l2norm_k05_long_seed42 ===
  metrics: {'elapsed_min': 94.6, 'episodes': 500, 'overall_sr': 45, 'per_task_sr': {'task_0_alphabet_soup_tomato_sauce': 26, 'task_1_cream_cheese_butter': 0, 'task_2_stove_moka_pot': 46, 'task_3_black_bowl_drawer': 82, 'task_4_white_mug_yellow_mug': 42, 'task_5_book_caddy': 92, 'task_6_white_mug_chocolate_pudding': 54, 'task_7_alphabet_soup_cream_cheese': 70, 'task_8_both_moka_pots': 34, 'task_9_mug_microwave': 4}, 'wilson_ci_95': [40.7, 49.4]}
  conclusion: success

=== eval_xvla_random_k05_object_seed42 ===
  metrics: {'duration_min': 76.0, 'num_episodes': 500, 'per_task': [0.96, 0.46, 0.98, 0.8, 1.0, 0.76, 0.02, 0.82, 0.26, 1.0], 'success_rate': 70.6, 'wilson_ci_95': [0.665, 0.744]}
  conclusion: success

=== eval_xvla_random_k05_spatial_seed42 ===
  metrics: {'duration_min': 92.1, 'num_episodes': 500, 'per_task': [0.98, 0.26, 0.98, 0.9, 0.86, 0, 0.92, 0.66, 0.92, 0.66], 'success_rate': 71.4, 'suite': 'libero_spatial', 'wilson_ci_95': [0.673, 0.752]}
  conclusion: success

=== eval_xvla_random_k05_long_seed42 ===
  metrics: {'keep_ratio': 0.5, 'per_task_sr': [68, 0, 64, 94, 70, 90, 84, 86, 46, 14], 'prune_method': 'random', 'seed': 42, 'success_rate': 61.6, 'suite': 'libero_10', 'tokens_kept': '25/50', 'total_episodes': 500, 'total_successes': 308, 'wall_time_min': 82.6, 'wilson_ci_95': [57.3, 65.8]}
  conclusion: success

=== eval_xvla_l2norm_k05_object_seed42 ===
  metrics: {'success_rate': 0.434, 'total_episodes': 500, 'total_successes': 217}
  conclusion: success

=== eval_xvla_l2norm_k05_spatial_seed43 ===
  metrics: {'elapsed_min': 79.1, 'per_task_SR': {'T0_bowl_between_plate_ramekin': 98, 'T1_bowl_next_ramekin': 20, 'T2_bowl_from_table_center': 92, 'T3_bowl_on_cookie_box': 72, 'T4_bowl_in_top_drawer': 76, 'T5_bowl_on_ramekin': 0, 'T6_bowl_next_cookie_box': 76, 'T7_bowl_on_stove': 38, 'T8_bowl_next_plate': 66, 'T9_bowl_on_wooden_cabinet': 52}, 'seed': 43, 'success_rate': 59, 'total_episodes': 500, 'total_successes': 295, 'vs_l2norm_spatial_seed42': {'diff_pp': 0.2, 'mean': 58.9, 'seed42_sr': 58.8, 'seed43_sr': 59}, 'vs_random_k05_spatial_seed43': {'delta_pp': -13.6, 'l2norm_sr': 59, 'random_sr': 72.6, 'verdict': 'L2norm worse than random on Spatial'}, 'wilson_ci_95': [54.6, 63.2]}
  conclusion: negative

=== eval_xvla_random_k05_goal_seed43_v4 ===
  metrics: {'cv_with_seed42': {'diff_pp': 1.4, 'mean': 67.9, 'seed42': 67.2, 'seed43': 68.6}, 'elapsed_min': 56.1, 'per_task_sr': {'T0_open_middle_drawer': 100, 'T1_bowl_on_stove': 94, 'T2_wine_on_cabinet': 96, 'T3_open_drawer_bowl_inside': 68, 'T4_bowl_on_cabinet': 98, 'T5_push_plate': 0, 'T6_cream_cheese_in_bowl': 38, 'T7_turn_on_stove': 96, 'T8_bowl_on_plate': 96, 'T9_wine_on_rack': 0}, 'success_rate': 68.6, 'total_episodes': 500, 'total_successes': 343, 'wilson_ci_95': [64.4, 72.5]}
  conclusion: success

=== eval_xvla_random_k05_long_seed43 ===
  metrics: {'elapsed_min': 83.6, 'overall_SR': 0.582, 'per_task_SR': [0.62, 0, 0.68, 0.94, 0.6, 0.86, 0.82, 0.84, 0.4, 0.06], 'seed': 43, 'total_episodes': 500, 'total_successes': 291, 'wilson_ci_95': [0.5383, 0.6244]}
  conclusion: success

=== eval_xvla_l2norm_k05_object_seed43 ===
  metrics: {'elapsed_min': 76.3, 'overall_SR': 0.43, 'per_task_SR': {'T0_alphabet_soup': 0.52, 'T1_cream_cheese': 0.06, 'T2_salad_dressing': 0.76, 'T3_bbq_sauce': 0.7, 'T4_ketchup': 0.52, 'T5_tomato_sauce': 0.56, 'T6_butter': 0.02, 'T7_milk': 0.38, 'T8_chocolate_pudding': 0.16, 'T9_orange_juice': 0.62}, 'seed': 43, 'total_episodes': 500, 'total_successes': 215, 'vs_random_k05_object_seed43': {'delta_pp': -28, 'l2norm_sr': 0.43, 'random_sr': 0.71, 'verdict': 'L2norm catastrophically worse than random on Object suite'}, 'wilson_ci_95': [0.387, 0.474]}
  conclusion: negative

=== eval_xvla_random_k05_goal_seed43_v3 ===
  metrics: {}
  conclusion: killed

=== eval_xvla_random_k05_goal_seed43_v2 ===
  metrics: {}
  conclusion: failed

=== eval_xvla_random_k05_goal_seed43 ===
  metrics: {'elapsed_min': 58.2, 'note': 'log=eval_xvla_random_k05_goal_seed42_v2.log; JSON overwritten by l2_norm run (known bug)', 'overall_sr': 0.672, 'per_task': {'task_0_open_middle_drawer': {'sr': 0.98, 'succ': 49, 'total': 50}, 'task_1_bowl_on_stove': {'sr': 0.98, 'succ': 49, 'total': 50}, 'task_2_wine_on_cabinet': {'sr': 0.9, 'succ': 45, 'total': 50}, 'task_3_open_drawer_bowl_inside': {'sr': 0.6, 'succ': 30, 'total': 50}, 'task_4_bowl_on_cabinet': {'sr': 0.98, 'succ': 49, 'total': 50}, 'task_5_push_plate': {'sr': 0, 'succ': 0, 'total': 50}, 'task_6_cream_cheese_in_bowl': {'sr': 0.4, 'succ': 20, 'total': 50}, 'task_7_turn_on_stove': {'sr': 0.98, 'succ': 49, 'total': 50}, 'task_8_bowl_on_plate': {'sr': 0.86, 'succ': 43, 'total': 50}, 'task_9_wine_on_rack': {'sr': 0.04, 'succ': 2, 'total': 50}}, 'total_episodes': 500, 'total_successes': 336, 'wilson_ci_95': [0.63, 0.712]}
  conclusion: failed

=== eval_xvla_l2norm_k03_goal_seed42_v4 ===
  metrics: {'success_rate': 37.6, 'total_episodes': 500, 'total_successes': 188}
  conclusion: negative

=== eval_xvla_random_k05_goal_seed42_v2 ===
  metrics: {'success_rate': 67.2, 'total_episodes': 500, 'total_successes': 336}
  conclusion: success

=== eval_xvla_random_k05_object_seed43 ===
  metrics: {'success_rate': 0.71, 'total_episodes': 500, 'total_successes': 355, 'wilson_ci_95': [0.6687, 0.7481]}
  conclusion: success

=== eval_xvla_l2norm_k03_spatial_seed42 ===
  metrics: {'elapsed_seconds': 6754.6, 'n_vision_tokens_kept': 15, 'n_vision_tokens_original': 50, 'per_task': {'task_0': {'desc': 'pick up the black bowl between the plate and the ramekin and place it on the plate', 'sr': 0.74}, 'task_1': {'desc': 'pick up the black bowl next to the ramekin and place it on the plate', 'sr': 0.06}, 'task_2': {'desc': 'pick up the black bowl from table center and place it on the plate', 'sr': 0.82}, 'task_3': {'desc': 'pick up the black bowl on the cookie box and place it on the plate', 'sr': 0.34}, 'task_4': {'desc': 'pick up the black bowl in the top drawer of the wooden cabinet and place it on the plate', 'sr': 0.66}, 'task_5': {'desc': 'pick up the black bowl on the ramekin and place it on the plate', 'sr': 0}, 'task_6': {'desc': 'pick up the black bowl next to the cookie box and place it on the plate', 'sr': 0.04}, 'task_7': {'desc': 'pick up the black bowl on the stove and place it on the plate', 'sr': 0.08}, 'task_8': {'desc': 'pick up the black bowl next to the plate and place it on the plate', 'sr': 0.34}, 'task_9': {'desc': 'pick up the black bowl on the wooden cabinet and place it on the plate', 'sr': 0.04}}, 'success_rate': 0.312, 'total_episodes': 500, 'total_successes': 156, 'wilson_ci_95': [0.273, 0.354]}
  conclusion: negative

=== eval_xvla_l2norm_k05_goal_seed42_v3 ===
  metrics: {'elapsed_min': 65.8, 'per_task': {'T0_open_middle_drawer': 0.8, 'T1_put_bowl_stove': 0.92, 'T2_wine_bottle_cabinet': 0.98, 'T3_open_drawer_bowl': 0.34, 'T4_bowl_top_cabinet': 1, 'T5_push_plate_front': 0, 'T6_cream_cheese_bowl': 0.24, 'T7_turn_on_stove': 0.72, 'T8_bowl_on_plate': 0.9, 'T9_wine_bottle_rack': 0}, 'success_rate': 59, 'total_episodes': 500, 'total_successes': 295}
  conclusion: negative

=== eval_xvla_l2norm_k05_spatial_seed42_v3 ===
  metrics: {'elapsed_min': 82, 'per_task_sr': [92, 22, 88, 72, 84, 0, 82, 32, 72, 44], 'success_rate': 58.8, 'total_episodes': 500, 'wilson_ci_95': [54.4, 63]}
  conclusion: negative

=== eval_xvla_l2norm_k07_goal_seed42 ===
  metrics: {'num_episodes': 500, 'num_success': 267, 'seed': 42, 'success_rate': 0.534, 'suite': 'libero_goal'}
  conclusion: negative

=== eval_e5_xvla_attn_last_goal_k03 ===
  metrics: {}
  conclusion: killed

=== eval_e5_xvla_attn_mean_goal_k03 ===
  metrics: {}
  conclusion: killed

=== eval_xvla_random_k05_goal_seed42 ===
  metrics: {'elapsed_min': 158.9, 'episodes': 500, 'per_task_sr': {'task0_open_middle_drawer': 0, 'task1_bowl_on_stove': 0, 'task2_wine_on_cabinet': 0, 'task3_open_drawer_bowl_inside': 0, 'task4_bowl_on_cabinet': 0, 'task5_push_plate_front_stove': 0, 'task6_cream_cheese_in_bowl': 0, 'task7_turn_on_stove': 0, 'task8_bowl_on_plate': 0, 'task9_wine_on_rack': 0}, 'success_rate': 0, 'tasks': 10, 'wilson_ci_95': [0, 0.8]}
  conclusion: failed

=== eval_e5_xvla_attn_rollout_goal_k05_v2 ===
  metrics: {'elapsed_min': 31.1, 'success_rate': 96.8, 'total_episodes': 500, 'total_successes': 484, 'wilson_ci_95': [94.9, 98]}
  conclusion: success

=== eval_e5_xvla_attn_mean_goal_k05_v2 ===
  metrics: {'elapsed_min': 30.2, 'success_rate': 97.4, 'total_episodes': 500, 'total_successes': 487, 'wilson_ci_95': [95.6, 98.5]}
  conclusion: success

=== eval_e5_xvla_attn_last_goal_k05_v2 ===
  metrics: {'elapsed_min': 30, 'success_rate': 98.2, 'total_episodes': 500, 'total_successes': 491, 'wilson_ci_95': [96.6, 99.1]}
  conclusion: success

=== eval_e5_xvla_random_goal_k05_v2 ===
  metrics: {'elapsed_min': 58.2, 'success_rate': 67.2, 'total_episodes': 500, 'total_successes': 336, 'wilson_ci_95': [63, 71.2]}
  conclusion: negative

=== eval_e5_xvla_attn_last_obj_k03 ===
  metrics: {'elapsed_min': 45.2, 'source': 'Worker harvested from westd-27271', 'success_rate': 84.2, 'total_episodes': 500, 'total_successes': 421, 'wilson_ci_95': [80.7, 87.1]}
  conclusion: success

=== eval_e5_xvla_attn_rollout_obj_k03 ===
  metrics: {'source': 'Director harvested from westd-38929', 'success_rate': 92, 'total_episodes': 500, 'total_successes': 460}
  conclusion: success

=== eval_e5_xvla_attn_mean_spatial_k03 ===
  metrics: {'source': 'Director harvested from westd-38929', 'success_rate': 90.4, 'total_episodes': 500, 'total_successes': 452}
  conclusion: success

=== eval_e5_xvla_attn_last_spatial_k03 ===
  metrics: {'source': 'Director harvested from westd-38929', 'success_rate': 85.6, 'total_episodes': 500, 'total_successes': 428}
  conclusion: success

=== eval_e5_xvla_attn_mean_obj_k03 ===
  metrics: {'source': 'Director harvested from westd-38929', 'success_rate': 96, 'total_episodes': 500, 'total_successes': 480}
  conclusion: success
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "790dcd4a-6607-4659-a5a3-a960215f6b9a",
  "uuid": "1ed33e96-5f73-46e6-a8fa-7511224a8692",
  "tool_use_result": {
    "stdout": "=== eval_xvla_random_k05_spatial_seed43 ===\n  metrics: {'overall_sr': 0.726, 'total_episodes': 500, 'total_successes': 363, 'wilson_ci_95': [0.685, 0.763], 'elapsed_min': 64.3}\n  conclusion: success\n\n=== eval_xvla_l2norm_k03_goal_seed42_v5 ===\n  metrics: {'domain_id': 3, 'elapsed_min': 84, 'overall_sr': 0.37, 'per_task_sr': {'task0_open_drawer': 0.42, 'task1_bowl_on_stove': 0.92, 'task2_wine_on_cabinet': 0.2, 'task3_drawer_bowl': 0.24, 'task4_bowl_on_cabinet': 0.98, 'task5_push_plate': 0, 'task6_cream_cheese': 0.02, 'task7_turn_stove': 0.16, 'task8_bowl_on_plate': 0.76, 'task9_wine_on_rack': 0}, 'seed': 42, 'total_episodes': 500, 'total_success': 185, 'vision_tokens_kept': 15, 'vision_tokens_original': 50, 'wilson_ci_95': [0.3288, 0.4132]}\n  conclusion: success\n\n=== eval_xvla_l2norm_k03_long_seed42 ===\n  metrics: {}\n  conclusion: killed\n\n=== eval_xvla_random_k03_long_seed42 ===\n  metrics: {}\n  conclusion: killed\n\n=== eval_xvla_l2norm_k05_long_seed42_v4 ===\n  metrics: {'elapsed_min': 94.6, 'overall_sr': 44.6, 'per_task_sr': {'T0_alphabet_soup_tomato_basket': 26, 'T1_cream_cheese_butter_basket': 0, 'T2_stove_moka_pot': 48, 'T3_black_bowl_drawer': 84, 'T4_mugs_on_plates': 36, 'T5_book_caddy': 88, 'T6_mug_plate_pudding': 48, 'T7_alphabet_soup_cream_cheese_basket': 78, 'T8_moka_pots_stove': 34, 'T9_mug_microwave': 4}, 'total_episodes': 500, 'total_success': 223}\n  conclusion: success\n\n=== eval_xvla_l2norm_k03_goal_seed42 ===\n  metrics: {}\n  conclusion: failed\n\n=== eval_xvla_l2norm_k07_spatial_seed42_v2 ===\n  metrics: {'overall_sr': 72.8, 'per_task_sr': {'task_0': 98, 'task_1': 42, 'task_2': 96, 'task_3': 94, 'task_4': 82, 'task_5': 0, 'task_6': 98, 'task_7': 34, 'task_8': 94, 'task_9': 90}, 'total_episodes': 500, 'total_success': 364}\n  conclusion: success\n\n=== eval_xvla_random_k085_long_seed42 ===\n  metrics: {'cross_suite_k085': {'goal': 60.4, 'long': 35, 'object': 65, 'spatial': 68.2}, 'elapsed_min': 106.7, 'keep_ratio': 0.85, 'model': 'X-VLA', 'overall_sr': 35, 'per_task_sr': {'T0_alphabet_soup_tomato_sauce_basket': 54, 'T1_cream_cheese_butter_basket': 10, 'T2_stove_moka_pot': 16, 'T3_black_bowl_drawer': 88, 'T4_white_mug_left_yellow_mug_right': 2, 'T5_book_caddy': 98, 'T6_white_mug_chocolate_pudding': 0, 'T7_alphabet_soup_cream_cheese_basket': 48, 'T8_both_moka_pots_stove': 16, 'T9_mug_microwave': 18}, 'prune_mode': 'random', 'seed': 42, 'suite': 'libero_10', 'total_episodes': 500, 'total_success': 175, 'vs_k05_long': {'delta_pp': -26.6, 'k05_sr': 61.6, 'k085_sr': 35, 'non_monotonic': True}, 'wilson_ci_95': [30.9, 39.3]}\n  conclusion: success\n\n=== eval_xvla_l2norm_k03_goal_seed42_v2 ===\n  metrics: {}\n  conclusion: killed\n\n=== eval_xvla_l2norm_k03_goal_seed42_v3 ===\n  metrics: {'success_rate': 0.376, 'task_sr': {'task0_open_drawer': 0.42, 'task1_bowl_on_stove': 0.94, 'task2_wine_on_cabinet': 0.16, 'task3_drawer_bowl_inside': 0.24, 'task4_bowl_on_cabinet': 0.98, 'task5_push_plate': 0, 'task6_cream_in_bowl': 0.02, 'task7_turn_on_stove': 0.2, 'task8_bowl_on_plate': 0.8, 'task9_wine_on_rack': 0}, 'total_episodes': 500, 'total_successes': 188}\n  conclusion: negative\n\n=== eval_xvla_l2norm_k05_long_seed42_v3 ===\n  metrics: {}\n  conclusion: killed\n\n=== eval_xvla_l2norm_k05_spatial_seed42_v2 ===\n  metrics: {}\n  conclusion: killed\n\n=== eval_xvla_l2norm_k07_spatial_seed42 ===\n  metrics: {'num_episodes': 500, 'num_success': 360, 'seed': 42, 'success_rate': 0.72, 'suite': 'libero_spatial'}\n  conclusion: negative\n\n=== eval_xvla_l2norm_k05_goal_seed42_v2 ===\n  metrics: {'keep_ratio': 0.5, 'model': 'X-VLA', 'per_task_sr': {'T0_open_middle_drawer': 80, 'T1_put_bowl_on_stove': 92, 'T2_put_wine_bottle_on_cabinet': 98, 'T3_open_top_drawer_put_bowl': 34, 'T4_put_bowl_on_cabinet': 100, 'T5_push_plate_to_stove': 0, 'T6_put_cream_cheese_in_bowl': 24, 'T7_turn_on_stove': 72, 'T8_put_bowl_on_plate': 90, 'T9_put_wine_bottle_on_rack': 0}, 'prune_mode': 'l2_norm', 'seed': 42, 'success_rate': 0.59, 'suite': 'libero_goal', 'total_episodes': 500, 'total_successes': 295}\n  conclusion: success\n\n=== eval_xvla_l2norm_k05_goal_seed43 ===\n  metrics: {'overall_SR': 0.602, 'per_task_SR': [0.84, 1, 0.98, 0.3, 1, 0, 0.22, 0.74, 0.9, 0.04], 'seed': 43, 'total_episodes': 500, 'total_successes': 301, 'wilson_ci_95': [0.5585, 0.644]}\n  conclusion: negative\n\n=== eval_xvla_random_k085_object_seed42 ===\n  metrics: {'elapsed_seconds': 3572.9, 'overall_SR': 0.65, 'per_task_sr': [0.98, 0.14, 1, 0.88, 0.36, 0.96, 0, 0.94, 0.24, 1], 'total_episodes': 500, 'total_successes': 325, 'wilson_ci_95': [0.6072, 0.6905]}\n  conclusion: success\n\n=== eval_xvla_random_k085_spatial_seed42 ===\n  metrics: {'overall_SR': 0.682, 'per_task': {'0': 1, '1': 0.06, '2': 0.98, '3': 0.98, '4': 0.82, '5': 0.06, '6': 1, '7': 0.04, '8': 0.92, '9': 0.96}, 'total_episodes': 500, 'wilson_ci_95': [0.6399, 0.7213]}\n  conclusion: success\n\n=== eval_xvla_random_k085_goal_seed42 ===\n  metrics: {'overall_SR': 0.604, 'per_task': {'0': 1, '1': 0.42, '2': 0.7, '3': 0.78, '4': 0.98, '5': 0, '6': 0.02, '7': 0.88, '8': 0.98, '9': 0.28}, 'total_episodes': 500, 'wilson_ci_95': [0.5605, 0.6459]}\n  conclusion: success\n\n=== eval_xvla_l2norm_k05_long_seed43 ===\n  metrics: {'elapsed_min': 94, 'overall_SR': 43.8, 'per_task_sr': {'T0': 26, 'T1': 0, 'T2': 52, 'T3': 78, 'T4': 38, 'T5': 86, 'T6': 56, 'T7': 76, 'T8': 24, 'T9': 2}, 'result_json': 'eval_results/xvla_prune_k0.5_libero_10.json', 'total_episodes': 500, 'total_successes': 219, 'wilson_ci_95': [39.5, 48.2]}\n  conclusion: success\n\n=== eval_xvla_l2norm_k05_long_seed42 ===\n  metrics: {'elapsed_min': 94.6, 'episodes': 500, 'overall_sr': 45, 'per_task_sr': {'task_0_alphabet_soup_tomato_sauce': 26, 'task_1_cream_cheese_butter': 0, 'task_2_stove_moka_pot': 46, 'task_3_black_bowl_drawer': 82, 'task_4_white_mug_yellow_mug': 42, 'task_5_book_caddy': 92, 'task_6_white_mug_chocolate_pudding': 54, 'task_7_alphabet_soup_cream_cheese': 70, 'task_8_both_moka_pots': 34, 'task_9_mug_microwave': 4}, 'wilson_ci_95': [40.7, 49.4]}\n  conclusion: success\n\n=== eval_xvla_random_k05_object_seed42 ===\n  metrics: {'duration_min': 76.0, 'num_episodes': 500, 'per_task': [0.96, 0.46, 0.98, 0.8, 1.0, 0.76, 0.02, 0.82, 0.26, 1.0], 'success_rate': 70.6, 'wilson_ci_95': [0.665, 0.744]}\n  conclusion: success\n\n=== eval_xvla_random_k05_spatial_seed42 ===\n  metrics: {'duration_min': 92.1, 'num_episodes': 500, 'per_task': [0.98, 0.26, 0.98, 0.9, 0.86, 0, 0.92, 0.66, 0.92, 0.66], 'success_rate': 71.4, 'suite': 'libero_spatial', 'wilson_ci_95': [0.673, 0.752]}\n  conclusion: success\n\n=== eval_xvla_random_k05_long_seed42 ===\n  metrics: {'keep_ratio': 0.5, 'per_task_sr': [68, 0, 64, 94, 70, 90, 84, 86, 46, 14], 'prune_method': 'random', 'seed': 42, 'success_rate': 61.6, 'suite': 'libero_10', 'tokens_kept': '25/50', 'total_episodes': 500, 'total_successes': 308, 'wall_time_min': 82.6, 'wilson_ci_95': [57.3, 65.8]}\n  conclusion: success\n\n=== eval_xvla_l2norm_k05_object_seed42 ===\n  metrics: {'success_rate': 0.434, 'total_episodes': 500, 'total_successes': 217}\n  conclusion: success\n\n=== eval_xvla_l2norm_k05_spatial_seed43 ===\n  metrics: {'elapsed_min': 79.1, 'per_task_SR': {'T0_bowl_between_plate_ramekin': 98, 'T1_bowl_next_ramekin': 20, 'T2_bowl_from_table_center': 92, 'T3_bowl_on_cookie_box': 72, 'T4_bowl_in_top_drawer': 76, 'T5_bowl_on_ramekin': 0, 'T6_bowl_next_cookie_box': 76, 'T7_bowl_on_stove': 38, 'T8_bowl_next_plate': 66, 'T9_bowl_on_wooden_cabinet': 52}, 'seed': 43, 'success_rate': 59, 'total_episodes': 500, 'total_successes': 295, 'vs_l2norm_spatial_seed42': {'diff_pp': 0.2, 'mean': 58.9, 'seed42_sr': 58.8, 'seed43_sr': 59}, 'vs_random_k05_spatial_seed43': {'delta_pp': -13.6, 'l2norm_sr': 59, 'random_sr': 72.6, 'verdict': 'L2norm worse than random on Spatial'}, 'wilson_ci_95': [54.6, 63.2]}\n  conclusion: negative\n\n=== eval_xvla_random_k05_goal_seed43_v4 ===\n  metrics: {'cv_with_seed42': {'diff_pp': 1.4, 'mean': 67.9, 'seed42': 67.2, 'seed43': 68.6}, 'elapsed_min': 56.1, 'per_task_sr': {'T0_open_middle_drawer': 100, 'T1_bowl_on_stove': 94, 'T2_wine_on_cabinet': 96, 'T3_open_drawer_bowl_inside': 68, 'T4_bowl_on_cabinet': 98, 'T5_push_plate': 0, 'T6_cream_cheese_in_bowl': 38, 'T7_turn_on_stove': 96, 'T8_bowl_on_plate': 96, 'T9_wine_on_rack': 0}, 'success_rate': 68.6, 'total_episodes': 500, 'total_successes': 343, 'wilson_ci_95': [64.4, 72.5]}\n  conclusion: success\n\n=== eval_xvla_random_k05_long_seed43 ===\n  metrics: {'elapsed_min': 83.6, 'overall_SR': 0.582, 'per_task_SR': [0.62, 0, 0.68, 0.94, 0.6, 0.86, 0.82, 0.84, 0.4, 0.06], 'seed': 43, 'total_episodes': 500, 'total_successes': 291, 'wilson_ci_95': [0.5383, 0.6244]}\n  conclusion: success\n\n=== eval_xvla_l2norm_k05_object_seed43 ===\n  metrics: {'elapsed_min': 76.3, 'overall_SR': 0.43, 'per_task_SR': {'T0_alphabet_soup': 0.52, 'T1_cream_cheese': 0.06, 'T2_salad_dressing': 0.76, 'T3_bbq_sauce': 0.7, 'T4_ketchup': 0.52, 'T5_tomato_sauce': 0.56, 'T6_butter': 0.02, 'T7_milk': 0.38, 'T8_chocolate_pudding': 0.16, 'T9_orange_juice': 0.62}, 'seed': 43, 'total_episodes': 500, 'total_successes': 215, 'vs_random_k05_object_seed43': {'delta_pp': -28, 'l2norm_sr': 0.43, 'random_sr': 0.71, 'verdict': 'L2norm catastrophically worse than random on Object suite'}, 'wilson_ci_95': [0.387, 0.474]}\n  conclusion: negative\n\n=== eval_xvla_random_k05_goal_seed43_v3 ===\n  metrics: {}\n  conclusion: killed\n\n=== eval_xvla_random_k05_goal_seed43_v2 ===\n  metrics: {}\n  conclusion: failed\n\n=== eval_xvla_random_k05_goal_seed43 ===\n  metrics: {'elapsed_min': 58.2, 'note': 'log=eval_xvla_random_k05_goal_seed42_v2.log; JSON overwritten by l2_norm run (known bug)', 'overall_sr': 0.672, 'per_task': {'task_0_open_middle_drawer': {'sr': 0.98, 'succ': 49, 'total': 50}, 'task_1_bowl_on_stove': {'sr': 0.98, 'succ': 49, 'total': 50}, 'task_2_wine_on_cabinet': {'sr': 0.9, 'succ': 45, 'total': 50}, 'task_3_open_drawer_bowl_inside': {'sr': 0.6, 'succ': 30, 'total': 50}, 'task_4_bowl_on_cabinet': {'sr': 0.98, 'succ': 49, 'total': 50}, 'task_5_push_plate': {'sr': 0, 'succ': 0, 'total': 50}, 'task_6_cream_cheese_in_bowl': {'sr': 0.4, 'succ': 20, 'total': 50}, 'task_7_turn_on_stove': {'sr': 0.98, 'succ': 49, 'total': 50}, 'task_8_bowl_on_plate': {'sr': 0.86, 'succ': 43, 'total': 50}, 'task_9_wine_on_rack': {'sr': 0.04, 'succ': 2, 'total': 50}}, 'total_episodes': 500, 'total_successes': 336, 'wilson_ci_95': [0.63, 0.712]}\n  conclusion: failed\n\n=== eval_xvla_l2norm_k03_goal_seed42_v4 ===\n  metrics: {'success_rate': 37.6, 'total_episodes': 500, 'total_successes': 188}\n  conclusion: negative\n\n=== eval_xvla_random_k05_goal_seed42_v2 ===\n  metrics: {'success_rate': 67.2, 'total_episodes': 500, 'total_successes': 336}\n  conclusion: success\n\n=== eval_xvla_random_k05_object_seed43 ===\n  metrics: {'success_rate': 0.71, 'total_episodes': 500, 'total_successes': 355, 'wilson_ci_95': [0.6687, 0.7481]}\n  conclusion: success\n\n=== eval_xvla_l2norm_k03_spatial_seed42 ===\n  metrics: {'elapsed_seconds': 6754.6, 'n_vision_tokens_kept': 15, 'n_vision_tokens_original': 50, 'per_task': {'task_0': {'desc': 'pick up the black bowl between the plate and the ramekin and place it on the plate', 'sr': 0.74}, 'task_1': {'desc': 'pick up the black bowl next to the ramekin and place it on the plate', 'sr': 0.06}, 'task_2': {'desc': 'pick up the black bowl from table center and place it on the plate', 'sr': 0.82}, 'task_3': {'desc': 'pick up the black bowl on the cookie box and place it on the plate', 'sr': 0.34}, 'task_4': {'desc': 'pick up the black bowl in the top drawer of the wooden cabinet and place it on the plate', 'sr': 0.66}, 'task_5': {'desc': 'pick up the black bowl on the ramekin and place it on the plate', 'sr': 0}, 'task_6': {'desc': 'pick up the black bowl next to the cookie box and place it on the plate', 'sr': 0.04}, 'task_7': {'desc': 'pick up the black bowl on the stove and place it on the plate', 'sr': 0.08}, 'task_8': {'desc': 'pick up the black bowl next to the plate and place it on the plate', 'sr': 0.34}, 'task_9': {'desc': 'pick up the black bowl on the wooden cabinet and place it on the plate', 'sr': 0.04}}, 'success_rate': 0.312, 'total_episodes': 500, 'total_successes': 156, 'wilson_ci_95': [0.273, 0.354]}\n  conclusion: negative\n\n=== eval_xvla_l2norm_k05_goal_seed42_v3 ===\n  metrics: {'elapsed_min': 65.8, 'per_task': {'T0_open_middle_drawer': 0.8, 'T1_put_bowl_stove': 0.92, 'T2_wine_bottle_cabinet': 0.98, 'T3_open_drawer_bowl': 0.34, 'T4_bowl_top_cabinet': 1, 'T5_push_plate_front': 0, 'T6_cream_cheese_bowl': 0.24, 'T7_turn_on_stove': 0.72, 'T8_bowl_on_plate': 0.9, 'T9_wine_bottle_rack': 0}, 'success_rate': 59, 'total_episodes': 500, 'total_successes': 295}\n  conclusion: negative\n\n=== eval_xvla_l2norm_k05_spatial_seed42_v3 ===\n  metrics: {'elapsed_min': 82, 'per_task_sr': [92, 22, 88, 72, 84, 0, 82, 32, 72, 44], 'success_rate': 58.8, 'total_episodes': 500, 'wilson_ci_95': [54.4, 63]}\n  conclusion: negative\n\n=== eval_xvla_l2norm_k07_goal_seed42 ===\n  metrics: {'num_episodes': 500, 'num_success': 267, 'seed': 42, 'success_rate': 0.534, 'suite': 'libero_goal'}\n  conclusion: negative\n\n=== eval_e5_xvla_attn_last_goal_k03 ===\n  metrics: {}\n  conclusion: killed\n\n=== eval_e5_xvla_attn_mean_goal_k03 ===\n  metrics: {}\n  conclusion: killed\n\n=== eval_xvla_random_k05_goal_seed42 ===\n  metrics: {'elapsed_min': 158.9, 'episodes': 500, 'per_task_sr': {'task0_open_middle_drawer': 0, 'task1_bowl_on_stove': 0, 'task2_wine_on_cabinet': 0, 'task3_open_drawer_bowl_inside': 0, 'task4_bowl_on_cabinet': 0, 'task5_push_plate_front_stove': 0, 'task6_cream_cheese_in_bowl': 0, 'task7_turn_on_stove': 0, 'task8_bowl_on_plate': 0, 'task9_wine_on_rack': 0}, 'success_rate': 0, 'tasks': 10, 'wilson_ci_95': [0, 0.8]}\n  conclusion: failed\n\n=== eval_e5_xvla_attn_rollout_goal_k05_v2 ===\n  metrics: {'elapsed_min': 31.1, 'success_rate': 96.8, 'total_episodes': 500, 'total_successes': 484, 'wilson_ci_95': [94.9, 98]}\n  conclusion: success\n\n=== eval_e5_xvla_attn_mean_goal_k05_v2 ===\n  metrics: {'elapsed_min': 30.2, 'success_rate': 97.4, 'total_episodes': 500, 'total_successes': 487, 'wilson_ci_95': [95.6, 98.5]}\n  conclusion: success\n\n=== eval_e5_xvla_attn_last_goal_k05_v2 ===\n  metrics: {'elapsed_min': 30, 'success_rate': 98.2, 'total_episodes': 500, 'total_successes': 491, 'wilson_ci_95': [96.6, 99.1]}\n  conclusion: success\n\n=== eval_e5_xvla_random_goal_k05_v2 ===\n  metrics: {'elapsed_min': 58.2, 'success_rate': 67.2, 'total_episodes': 500, 'total_successes': 336, 'wilson_ci_95': [63, 71.2]}\n  conclusion: negative\n\n=== eval_e5_xvla_attn_last_obj_k03 ===\n  metrics: {'elapsed_min': 45.2, 'source': 'Worker harvested from westd-27271', 'success_rate': 84.2, 'total_episodes': 500, 'total_successes': 421, 'wilson_ci_95': [80.7, 87.1]}\n  conclusion: success\n\n=== eval_e5_xvla_attn_rollout_obj_k03 ===\n  metrics: {'source': 'Director harvested from westd-38929', 'success_rate': 92, 'total_episodes': 500, 'total_successes': 460}\n  conclusion: success\n\n=== eval_e5_xvla_attn_mean_spatial_k03 ===\n  metrics: {'source': 'Director harvested from westd-38929', 'success_rate': 90.4, 'total_episodes': 500, 'total_successes': 452}\n  conclusion: success\n\n=== eval_e5_xvla_attn_last_spatial_k03 ===\n  metrics: {'source': 'Director harvested from westd-38929', 'success_rate': 85.6, 'total_episodes': 500, 'total_successes': 428}\n  conclusion: success\n\n=== eval_e5_xvla_attn_mean_obj_k03 ===\n  metrics: {'source': 'Director harvested from westd-38929', 'success_rate': 96, 'total_episodes': 500, 'total_successes': 480}\n  conclusion: success",
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

_source line 17_

<details><summary>Logged reasoning block</summary>

```text
Now let me also search for the X-VLA baseline and the remaining experiments I need. Let me also look for more X-VLA experiments with k=0.9, k=0.95, k=0.7 etc.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "790dcd4a-6607-4659-a5a3-a960215f6b9a",
  "uuid": "434f11be-047d-47c5-beed-a1016d53c63b",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011V8hGDLxGrb3BLozhBy3Wj",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7841,
      "cache_read_input_tokens": 25530,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 7841
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

_source line 18_

Now let me search for X-VLA baseline and other needed data points.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "790dcd4a-6607-4659-a5a3-a960215f6b9a",
  "uuid": "1bf66704-047b-4ff1-a190-6e90577731bd",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011V8hGDLxGrb3BLozhBy3Wj",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7841,
      "cache_read_input_tokens": 25530,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 7841
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

_source line 19_

<details open><summary>🔧 Tool call — Bash · `toolu_0195JSKgUFyxZKoXRQrqwPSo`</summary>

```json
{
  "command": "cat /home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-be-idea-gen-0515-2-projects-importance-margin-vla-compress/790dcd4a-6607-4659-a5a3-a960215f6b9a/tool-results/mcp-agent-ml-research-read_registry-1779781647884.txt | python3 -c \"\nimport json, sys\ndata = json.loads(json.loads(sys.stdin.read())['result'])\nexps = data['data']['experiments']\n# Find X-VLA baseline\nfor name, exp in exps.items():\n    if 'xvla' in name.lower() and 'baseline' in name.lower():\n        print(f'=== {name} ===')\n        print(f'  metrics: {exp.get(\\\"metrics\\\", {})}')\n        print(f'  conclusion: {exp.get(\\\"conclusion\\\", \\\"\\\")}')\n        print()\n\" 2>&1",
  "description": "Search for X-VLA baseline experiments"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "790dcd4a-6607-4659-a5a3-a960215f6b9a",
  "uuid": "13c5c13b-f51f-448d-968e-9a0f53884de2",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011V8hGDLxGrb3BLozhBy3Wj",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7841,
      "cache_read_input_tokens": 25530,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 7841
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

_source line 20 · 2026-05-26T07:47:49.982Z_

<details><summary>↩ Tool result · `toolu_0195JSKgUFyxZKoXRQrqwPSo`</summary>

```text
=== eval_xvla_baseline_spatial_seed42 ===
  metrics: {'note': 'Corrected from 0.916 to 0.930 per Reviewer SSH verification of xvla_prune_k1.0_libero_spatial.json (465/500)', 'num_episodes': 500, 'success_rate': 0.93, 'total_successes': 465, 'wilson_ci_95': [0.904, 0.95]}
  conclusion: success

=== eval_xvla_baseline_goal_seed42 ===
  metrics: {'note': 'Corrected from 0.98 to 0.984 per Reviewer SSH verification (492/500)', 'num_episodes': 500, 'success_rate': 0.984, 'total_successes': 492, 'wilson_ci_95': [0.969, 0.992]}
  conclusion: success

=== eval_xvla_baseline_long_seed42 ===
  metrics: {'num_episodes': 500, 'per_task': [0.96, 0.68, 1.0, 0.98, 0.94, 0.96, 0.94, 0.96, 1.0, 0.98], 'seed': 42, 'success_rate': 0.94, 'suite': 'libero_10', 'wilson_ci_95': [0.916, 0.958]}
  conclusion: success
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "790dcd4a-6607-4659-a5a3-a960215f6b9a",
  "uuid": "27706f96-1229-4f86-8dbe-7b82c5b8265d",
  "tool_use_result": {
    "stdout": "=== eval_xvla_baseline_spatial_seed42 ===\n  metrics: {'note': 'Corrected from 0.916 to 0.930 per Reviewer SSH verification of xvla_prune_k1.0_libero_spatial.json (465/500)', 'num_episodes': 500, 'success_rate': 0.93, 'total_successes': 465, 'wilson_ci_95': [0.904, 0.95]}\n  conclusion: success\n\n=== eval_xvla_baseline_goal_seed42 ===\n  metrics: {'note': 'Corrected from 0.98 to 0.984 per Reviewer SSH verification (492/500)', 'num_episodes': 500, 'success_rate': 0.984, 'total_successes': 492, 'wilson_ci_95': [0.969, 0.992]}\n  conclusion: success\n\n=== eval_xvla_baseline_long_seed42 ===\n  metrics: {'num_episodes': 500, 'per_task': [0.96, 0.68, 1.0, 0.98, 0.94, 0.96, 0.94, 0.96, 1.0, 0.98], 'seed': 42, 'success_rate': 0.94, 'suite': 'libero_10', 'wilson_ci_95': [0.916, 0.958]}\n  conclusion: success",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  }
}
```

</details>

---


### Tool call

_source line 21_

<details open><summary>🔧 Tool call — Bash · `toolu_01PEh1sgUeTgaNXCN35nqkW6`</summary>

```json
{
  "command": "cat /home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-be-idea-gen-0515-2-projects-importance-margin-vla-compress/790dcd4a-6607-4659-a5a3-a960215f6b9a/tool-results/mcp-agent-ml-research-read_registry-1779781647884.txt | python3 -c \"\nimport json, sys\ndata = json.loads(json.loads(sys.stdin.read())['result'])\nexps = data['data']['experiments']\n# Find X-VLA experiments with k=0.9 or k=0.95 or k=0.7\nfor name, exp in exps.items():\n    if 'xvla' in name.lower() and any(k in name for k in ['k09', 'k095', 'k07']):\n        print(f'=== {name} ===')\n        print(f'  metrics: {exp.get(\\\"metrics\\\", {})}')\n        print(f'  conclusion: {exp.get(\\\"conclusion\\\", \\\"\\\")}')\n        print()\n\" 2>&1",
  "description": "Search for X-VLA k=0.9/0.95/0.7 experiments"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "790dcd4a-6607-4659-a5a3-a960215f6b9a",
  "uuid": "d37b037a-45cb-4fb4-aabb-dd5e4c475247",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011V8hGDLxGrb3BLozhBy3Wj",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7841,
      "cache_read_input_tokens": 25530,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 7841
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

_source line 22 · 2026-05-26T07:47:53.071Z_

<details><summary>↩ Tool result · `toolu_01PEh1sgUeTgaNXCN35nqkW6`</summary>

```text
=== eval_xvla_l2norm_k07_spatial_seed42_v2 ===
  metrics: {'overall_sr': 72.8, 'per_task_sr': {'task_0': 98, 'task_1': 42, 'task_2': 96, 'task_3': 94, 'task_4': 82, 'task_5': 0, 'task_6': 98, 'task_7': 34, 'task_8': 94, 'task_9': 90}, 'total_episodes': 500, 'total_success': 364}
  conclusion: success

=== eval_xvla_l2norm_k07_spatial_seed42 ===
  metrics: {'num_episodes': 500, 'num_success': 360, 'seed': 42, 'success_rate': 0.72, 'suite': 'libero_spatial'}
  conclusion: negative

=== eval_xvla_l2norm_k07_goal_seed42 ===
  metrics: {'num_episodes': 500, 'num_success': 267, 'seed': 42, 'success_rate': 0.534, 'suite': 'libero_goal'}
  conclusion: negative

=== eval_xvla_l2norm_k07_long_seed42_v2 ===
  metrics: {}
  conclusion: killed

=== eval_xvla_l2norm_k07_long_seed42 ===
  metrics: {'overall_SR': 0.494, 'per_task_SR': {'T0_alphabet_soup_tomato': 0.12, 'T1_cream_cheese_butter': 0.04, 'T2_stove_moka': 0.56, 'T3_bowl_drawer': 0.98, 'T4_mugs_plates': 0.68, 'T5_book_caddy': 0.94, 'T6_mug_pudding': 0.78, 'T7_soup_cream_cheese': 0.76, 'T8_two_moka_pots': 0, 'T9_mug_microwave': 0.08}, 'total_episodes': 500, 'total_successes': 247}
  conclusion: success

=== eval_xvla_random_k09_long_seed42 ===
  metrics: {'elapsed_min': 104.4, 'episodes': 500, 'overall_sr': 29.6, 'per_task_sr': {'task_0_alphabet_soup_tomato_sauce': 0, 'task_1_cream_cheese_butter': 16, 'task_2_stove_moka_pot': 0, 'task_3_black_bowl_drawer': 96, 'task_4_white_mug_yellow_mug': 36, 'task_5_book_caddy': 98, 'task_6_white_mug_chocolate_pudding': 0, 'task_7_alphabet_soup_cream_cheese': 0, 'task_8_both_moka_pots': 0, 'task_9_mug_microwave': 50}, 'wilson_ci_95': [25.8, 33.7]}
  conclusion: success

=== eval_xvla_random_k07_long_seed42 ===
  metrics: {'keep_ratio': 0.7, 'per_task_sr': [10, 8, 66, 98, 82, 100, 82, 70, 4, 10], 'prune_method': 'random', 'seed': 42, 'success_rate': 53, 'suite': 'libero_10', 'tokens_kept': '35/50', 'total_episodes': 500, 'total_successes': 265, 'wall_time_min': 87, 'wilson_ci_95': [48.6, 57.3]}
  conclusion: success

=== eval_xvla_random_k07_spatial_seed42 ===
  metrics: {'overall_SR': 0.766, 'total_episodes': 500, 'total_successes': 383}
  conclusion: negative

=== eval_xvla_random_k095_long_seed42 ===
  metrics: {'eval_episodes_per_task': 50, 'keep_ratio': 0.95, 'per_task_sr': [0, 46, 72, 90, 54, 98, 18, 10, 92, 2], 'prune_method': 'random', 'seed': 42, 'success_rate': 48.2, 'suite': 'libero_10', 'tokens_kept': '47/50', 'total_episodes': 500, 'total_success': 241, 'wall_time_min': 91.2, 'wilson_ci_95': [43.9, 52.6]}
  conclusion: success

=== eval_xvla_prune_k09_seed42 ===
  metrics: {'note': 'Reconstructed entry. SR=99.2% (seed42). Cross-seed range 97.6%–99.2% (seed43=97.6%, seed44=98.2%). Original JSON may exist on cqa1-33015.', 'num_episodes': 500, 'seed': 42, 'success_rate': 0.992}
  conclusion: success

=== eval_xvla_random_k095_object_seed42_v2 ===
  metrics: {'elapsed_seconds': 2068.5, 'success_rate': 0.988, 'total_episodes': 500, 'total_successes': 494}
  conclusion: success

=== eval_xvla_random_k07_goal_seed42 ===
  metrics: {'overall_SR': 0.572, 'total_episodes': 500, 'total_successes': 286}
  conclusion: negative

=== eval_xvla_random_k09_spatial_seed42 ===
  metrics: {'overall_SR': 0.778, 'total_episodes': 500, 'total_successes': 389}
  conclusion: negative

=== eval_xvla_random_k09_goal_seed42 ===
  metrics: {'overall_SR': 0.706, 'total_episodes': 500, 'total_successes': 353}
  conclusion: negative

=== eval_xvla_random_k095_spatial_seed42 ===
  metrics: {'overall_SR': 0.702, 'total_episodes': 500, 'total_successes': 351}
  conclusion: negative

=== eval_xvla_random_k095_goal_seed42 ===
  metrics: {'overall_SR': 0.54, 'total_episodes': 500, 'total_successes': 270}
  conclusion: negative

=== eval_xvla_l2norm_k09_spatial_seed42 ===
  metrics: {'num_episodes': 500, 'num_success': 394, 'seed': 42, 'success_rate': 0.788, 'suite': 'libero_spatial'}
  conclusion: negative

=== eval_xvla_l2norm_k09_goal_seed42 ===
  metrics: {'num_episodes': 500, 'num_success': 351, 'seed': 42, 'success_rate': 0.702, 'suite': 'libero_goal'}
  conclusion: negative

=== eval_xvla_l2norm_k095_goal_seed42 ===
  metrics: {'num_episodes': 500, 'num_success': 269, 'seed': 42, 'success_rate': 0.538, 'suite': 'libero_goal'}
  conclusion: negative

=== eval_xvla_l2norm_k095_spatial_seed42 ===
  metrics: {'num_episodes': 500, 'num_success': 358, 'seed': 42, 'success_rate': 0.716, 'suite': 'libero_spatial'}
  conclusion: negative

=== eval_xvla_l2norm_k09_long_seed42 ===
  metrics: {'num_episodes': 500, 'seed': 42, 'success_rate': 0.275, 'suite': 'libero_10', 'wilson_ci_95': [0.218, 0.341]}
  conclusion: negative

=== eval_xvla_l2norm_k095_long_seed42 ===
  metrics: {'num_episodes': 500, 'seed': 42, 'success_rate': 0.47, 'suite': 'libero_10', 'wilson_ci_95': [0.402, 0.539]}
  conclusion: negative

=== eval_xvla_random_k07_object_seed42_v2 ===
  metrics: {'num_episodes': 500, 'success_rate': 65.2}
  conclusion: success

=== eval_xvla_random_k07_object_seed44 ===
  metrics: {'SR': 0.65}
  conclusion: success

=== eval_xvla_l2norm_k07_object_seed43 ===
  metrics: {'SR': 0.59}
  conclusion: success

=== eval_xvla_l2norm_k07_object_seed44 ===
  metrics: {'SR': 0.564, 'per_task': [0.96, 0, 1, 0.8, 0.26, 0.9, 0.12, 0.7, 0.02, 0.88]}
  conclusion: success

=== eval_xvla_l2norm_k07_object_seed42_v2 ===
  metrics: {'notes': 'Reviewer confirmed. westd-38929=56.2% vs cqa1=58.2%, 2pp diff acceptable.', 'per_task': [96, 2, 100, 78, 34, 90, 18, 0, 70, 94], 'success_rate': 0.582, 'total_episodes': 500, 'total_successes': 291}
  conclusion: success

=== eval_xvla_random_k07_object_seed43_v2 ===
  metrics: {'success_rate': 0.65, 'total_episodes': 500, 'total_successes': 325, 'wilson_ci_95': [0.6072, 0.6905]}
  conclusion: success

=== eval_xvla_random_k07_object_seed43 ===
  metrics: {}
  conclusion: failed

=== eval_xvla_random_k07_object_seed42 ===
  metrics: {'duration_min': 77.3, 'num_episodes': 500, 'per_task': [0.98, 0.0, 1.0, 0.94, 0.62, 0.96, 0.1, 0.92, 0.0, 1.0], 'success_rate': 65.2, 'wilson_ci_95': [0.609, 0.692]}
  conclusion: success

=== eval_xvla_random_k09_object_seed42 ===
  metrics: {'duration_min': 50.4, 'num_episodes': 500, 'per_task': [0.96, 1.0, 1.0, 0.94, 1.0, 0.94, 1.0, 0.98, 0.96, 1.0], 'success_rate': 97.8, 'wilson_ci_95': [0.961, 0.988]}
  conclusion: success

=== eval_xvla_goal_k09_seed42 ===
  metrics: {'num_episodes': 500, 'per_task': [1.0, 0.82, 0.96, 0.06, 0.96, 0.0, 0.78, 1.0, 0.46, 0.98], 'seed': 42, 'success_rate': 0.702, 'suite': 'libero_goal', 'wilson_ci_95': [0.66, 0.74]}
  conclusion: success

=== eval_xvla_spatial_k09_seed42 ===
  metrics: {'num_episodes': 500, 'success_rate': 0.79, 'wilson_ci_95': [0.752, 0.823]}
  conclusion: success

=== eval_xvla_prune_k095_seed43 ===
  metrics: {'num_episodes': 500, 'success_rate': 0.99, 'wilson_ci_95': [0.9768, 0.9957]}
  conclusion: success

=== eval_xvla_prune_k095_seed44 ===
  metrics: {'num_episodes': 500, 'success_rate': 0.994, 'wilson_ci_95': [0.983, 0.998]}
  conclusion: success

=== eval_xvla_prune_k095_seed42 ===
  metrics: {'num_episodes': 500, 'success_rate': 0.99, 'wilson_ci_95': [0.977, 0.996]}
  conclusion: success

=== eval_xvla_prune_k07_seed44 ===
  metrics: {'episodes': 500, 'success_rate': 0.564}
  conclusion: success

=== eval_xvla_prune_k09_seed44 ===
  metrics: {'episodes': 500, 'success_rate': 0.982}
  conclusion: success
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "790dcd4a-6607-4659-a5a3-a960215f6b9a",
  "uuid": "296f0a70-ae44-48ba-bae0-d9d7d9a8e1be",
  "tool_use_result": {
    "stdout": "=== eval_xvla_l2norm_k07_spatial_seed42_v2 ===\n  metrics: {'overall_sr': 72.8, 'per_task_sr': {'task_0': 98, 'task_1': 42, 'task_2': 96, 'task_3': 94, 'task_4': 82, 'task_5': 0, 'task_6': 98, 'task_7': 34, 'task_8': 94, 'task_9': 90}, 'total_episodes': 500, 'total_success': 364}\n  conclusion: success\n\n=== eval_xvla_l2norm_k07_spatial_seed42 ===\n  metrics: {'num_episodes': 500, 'num_success': 360, 'seed': 42, 'success_rate': 0.72, 'suite': 'libero_spatial'}\n  conclusion: negative\n\n=== eval_xvla_l2norm_k07_goal_seed42 ===\n  metrics: {'num_episodes': 500, 'num_success': 267, 'seed': 42, 'success_rate': 0.534, 'suite': 'libero_goal'}\n  conclusion: negative\n\n=== eval_xvla_l2norm_k07_long_seed42_v2 ===\n  metrics: {}\n  conclusion: killed\n\n=== eval_xvla_l2norm_k07_long_seed42 ===\n  metrics: {'overall_SR': 0.494, 'per_task_SR': {'T0_alphabet_soup_tomato': 0.12, 'T1_cream_cheese_butter': 0.04, 'T2_stove_moka': 0.56, 'T3_bowl_drawer': 0.98, 'T4_mugs_plates': 0.68, 'T5_book_caddy': 0.94, 'T6_mug_pudding': 0.78, 'T7_soup_cream_cheese': 0.76, 'T8_two_moka_pots': 0, 'T9_mug_microwave': 0.08}, 'total_episodes': 500, 'total_successes': 247}\n  conclusion: success\n\n=== eval_xvla_random_k09_long_seed42 ===\n  metrics: {'elapsed_min': 104.4, 'episodes': 500, 'overall_sr': 29.6, 'per_task_sr': {'task_0_alphabet_soup_tomato_sauce': 0, 'task_1_cream_cheese_butter': 16, 'task_2_stove_moka_pot': 0, 'task_3_black_bowl_drawer': 96, 'task_4_white_mug_yellow_mug': 36, 'task_5_book_caddy': 98, 'task_6_white_mug_chocolate_pudding': 0, 'task_7_alphabet_soup_cream_cheese': 0, 'task_8_both_moka_pots': 0, 'task_9_mug_microwave': 50}, 'wilson_ci_95': [25.8, 33.7]}\n  conclusion: success\n\n=== eval_xvla_random_k07_long_seed42 ===\n  metrics: {'keep_ratio': 0.7, 'per_task_sr': [10, 8, 66, 98, 82, 100, 82, 70, 4, 10], 'prune_method': 'random', 'seed': 42, 'success_rate': 53, 'suite': 'libero_10', 'tokens_kept': '35/50', 'total_episodes': 500, 'total_successes': 265, 'wall_time_min': 87, 'wilson_ci_95': [48.6, 57.3]}\n  conclusion: success\n\n=== eval_xvla_random_k07_spatial_seed42 ===\n  metrics: {'overall_SR': 0.766, 'total_episodes': 500, 'total_successes': 383}\n  conclusion: negative\n\n=== eval_xvla_random_k095_long_seed42 ===\n  metrics: {'eval_episodes_per_task': 50, 'keep_ratio': 0.95, 'per_task_sr': [0, 46, 72, 90, 54, 98, 18, 10, 92, 2], 'prune_method': 'random', 'seed': 42, 'success_rate': 48.2, 'suite': 'libero_10', 'tokens_kept': '47/50', 'total_episodes': 500, 'total_success': 241, 'wall_time_min': 91.2, 'wilson_ci_95': [43.9, 52.6]}\n  conclusion: success\n\n=== eval_xvla_prune_k09_seed42 ===\n  metrics: {'note': 'Reconstructed entry. SR=99.2% (seed42). Cross-seed range 97.6%–99.2% (seed43=97.6%, seed44=98.2%). Original JSON may exist on cqa1-33015.', 'num_episodes': 500, 'seed': 42, 'success_rate': 0.992}\n  conclusion: success\n\n=== eval_xvla_random_k095_object_seed42_v2 ===\n  metrics: {'elapsed_seconds': 2068.5, 'success_rate': 0.988, 'total_episodes': 500, 'total_successes': 494}\n  conclusion: success\n\n=== eval_xvla_random_k07_goal_seed42 ===\n  metrics: {'overall_SR': 0.572, 'total_episodes': 500, 'total_successes': 286}\n  conclusion: negative\n\n=== eval_xvla_random_k09_spatial_seed42 ===\n  metrics: {'overall_SR': 0.778, 'total_episodes': 500, 'total_successes': 389}\n  conclusion: negative\n\n=== eval_xvla_random_k09_goal_seed42 ===\n  metrics: {'overall_SR': 0.706, 'total_episodes': 500, 'total_successes': 353}\n  conclusion: negative\n\n=== eval_xvla_random_k095_spatial_seed42 ===\n  metrics: {'overall_SR': 0.702, 'total_episodes': 500, 'total_successes': 351}\n  conclusion: negative\n\n=== eval_xvla_random_k095_goal_seed42 ===\n  metrics: {'overall_SR': 0.54, 'total_episodes': 500, 'total_successes': 270}\n  conclusion: negative\n\n=== eval_xvla_l2norm_k09_spatial_seed42 ===\n  metrics: {'num_episodes': 500, 'num_success': 394, 'seed': 42, 'success_rate': 0.788, 'suite': 'libero_spatial'}\n  conclusion: negative\n\n=== eval_xvla_l2norm_k09_goal_seed42 ===\n  metrics: {'num_episodes': 500, 'num_success': 351, 'seed': 42, 'success_rate': 0.702, 'suite': 'libero_goal'}\n  conclusion: negative\n\n=== eval_xvla_l2norm_k095_goal_seed42 ===\n  metrics: {'num_episodes': 500, 'num_success': 269, 'seed': 42, 'success_rate': 0.538, 'suite': 'libero_goal'}\n  conclusion: negative\n\n=== eval_xvla_l2norm_k095_spatial_seed42 ===\n  metrics: {'num_episodes': 500, 'num_success': 358, 'seed': 42, 'success_rate': 0.716, 'suite': 'libero_spatial'}\n  conclusion: negative\n\n=== eval_xvla_l2norm_k09_long_seed42 ===\n  metrics: {'num_episodes': 500, 'seed': 42, 'success_rate': 0.275, 'suite': 'libero_10', 'wilson_ci_95': [0.218, 0.341]}\n  conclusion: negative\n\n=== eval_xvla_l2norm_k095_long_seed42 ===\n  metrics: {'num_episodes': 500, 'seed': 42, 'success_rate': 0.47, 'suite': 'libero_10', 'wilson_ci_95': [0.402, 0.539]}\n  conclusion: negative\n\n=== eval_xvla_random_k07_object_seed42_v2 ===\n  metrics: {'num_episodes': 500, 'success_rate': 65.2}\n  conclusion: success\n\n=== eval_xvla_random_k07_object_seed44 ===\n  metrics: {'SR': 0.65}\n  conclusion: success\n\n=== eval_xvla_l2norm_k07_object_seed43 ===\n  metrics: {'SR': 0.59}\n  conclusion: success\n\n=== eval_xvla_l2norm_k07_object_seed44 ===\n  metrics: {'SR': 0.564, 'per_task': [0.96, 0, 1, 0.8, 0.26, 0.9, 0.12, 0.7, 0.02, 0.88]}\n  conclusion: success\n\n=== eval_xvla_l2norm_k07_object_seed42_v2 ===\n  metrics: {'notes': 'Reviewer confirmed. westd-38929=56.2% vs cqa1=58.2%, 2pp diff acceptable.', 'per_task': [96, 2, 100, 78, 34, 90, 18, 0, 70, 94], 'success_rate': 0.582, 'total_episodes': 500, 'total_successes': 291}\n  conclusion: success\n\n=== eval_xvla_random_k07_object_seed43_v2 ===\n  metrics: {'success_rate': 0.65, 'total_episodes': 500, 'total_successes': 325, 'wilson_ci_95': [0.6072, 0.6905]}\n  conclusion: success\n\n=== eval_xvla_random_k07_object_seed43 ===\n  metrics: {}\n  conclusion: failed\n\n=== eval_xvla_random_k07_object_seed42 ===\n  metrics: {'duration_min': 77.3, 'num_episodes': 500, 'per_task': [0.98, 0.0, 1.0, 0.94, 0.62, 0.96, 0.1, 0.92, 0.0, 1.0], 'success_rate': 65.2, 'wilson_ci_95': [0.609, 0.692]}\n  conclusion: success\n\n=== eval_xvla_random_k09_object_seed42 ===\n  metrics: {'duration_min': 50.4, 'num_episodes': 500, 'per_task': [0.96, 1.0, 1.0, 0.94, 1.0, 0.94, 1.0, 0.98, 0.96, 1.0], 'success_rate': 97.8, 'wilson_ci_95': [0.961, 0.988]}\n  conclusion: success\n\n=== eval_xvla_goal_k09_seed42 ===\n  metrics: {'num_episodes': 500, 'per_task': [1.0, 0.82, 0.96, 0.06, 0.96, 0.0, 0.78, 1.0, 0.46, 0.98], 'seed': 42, 'success_rate': 0.702, 'suite': 'libero_goal', 'wilson_ci_95': [0.66, 0.74]}\n  conclusion: success\n\n=== eval_xvla_spatial_k09_seed42 ===\n  metrics: {'num_episodes': 500, 'success_rate': 0.79, 'wilson_ci_95': [0.752, 0.823]}\n  conclusion: success\n\n=== eval_xvla_prune_k095_seed43 ===\n  metrics: {'num_episodes': 500, 'success_rate': 0.99, 'wilson_ci_95': [0.9768, 0.9957]}\n  conclusion: success\n\n=== eval_xvla_prune_k095_seed44 ===\n  metrics: {'num_episodes': 500, 'success_rate': 0.994, 'wilson_ci_95': [0.983, 0.998]}\n  conclusion: success\n\n=== eval_xvla_prune_k095_seed42 ===\n  metrics: {'num_episodes': 500, 'success_rate': 0.99, 'wilson_ci_95': [0.977, 0.996]}\n  conclusion: success\n\n=== eval_xvla_prune_k07_seed44 ===\n  metrics: {'episodes': 500, 'success_rate': 0.564}\n  conclusion: success\n\n=== eval_xvla_prune_k09_seed44 ===\n  metrics: {'episodes': 500, 'success_rate': 0.982}\n  conclusion: success",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  }
}
```

</details>

---


### Tool call

_source line 23_

<details open><summary>🔧 Tool call — Bash · `toolu_012VznrExou4suV8GQfHrWkw`</summary>

```json
{
  "command": "cat /home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-be-idea-gen-0515-2-projects-importance-margin-vla-compress/790dcd4a-6607-4659-a5a3-a960215f6b9a/tool-results/mcp-agent-ml-research-read_registry-1779781647884.txt | python3 -c \"\nimport json, sys\ndata = json.loads(json.loads(sys.stdin.read())['result'])\nexps = data['data']['experiments']\n# Find X-VLA object experiments\nfor name, exp in exps.items():\n    if 'xvla' in name.lower() and 'object' in name.lower():\n        print(f'=== {name} ===')\n        sr = exp.get('metrics', {}).get('success_rate', exp.get('metrics', {}).get('overall_SR', exp.get('metrics', {}).get('overall_sr', 'N/A')))\n        print(f'  SR: {sr}')\n        print(f'  conclusion: {exp.get(\\\"conclusion\\\", \\\"\\\")}')\n        print()\n\" 2>&1",
  "description": "Search for X-VLA object experiments"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "790dcd4a-6607-4659-a5a3-a960215f6b9a",
  "uuid": "dafc15d6-b0b7-4981-afbd-eaa91e69dac4",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011V8hGDLxGrb3BLozhBy3Wj",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7841,
      "cache_read_input_tokens": 25530,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 7841
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

_source line 24 · 2026-05-26T07:47:55.549Z_

<details><summary>↩ Tool result · `toolu_012VznrExou4suV8GQfHrWkw`</summary>

```text
=== eval_xvla_random_k085_object_seed42 ===
  SR: 0.65
  conclusion: success

=== eval_xvla_random_k05_object_seed42 ===
  SR: 70.6
  conclusion: success

=== eval_xvla_l2norm_k05_object_seed42 ===
  SR: 0.434
  conclusion: success

=== eval_xvla_l2norm_k05_object_seed43 ===
  SR: 0.43
  conclusion: negative

=== eval_xvla_random_k05_object_seed43 ===
  SR: 0.71
  conclusion: success

=== eval_xvla_random_k095_object_seed42_v2 ===
  SR: 0.988
  conclusion: success

=== eval_xvla_l2norm_k03_object_seed44 ===
  SR: N/A
  conclusion: success

=== eval_xvla_random_k07_object_seed42_v2 ===
  SR: 65.2
  conclusion: success

=== eval_xvla_random_k085_object_seed43 ===
  SR: 63.2
  conclusion: success

=== eval_xvla_random_k085_object_seed42_v2 ===
  SR: 63.6
  conclusion: success

=== eval_xvla_l2norm_k03_object_seed42_v2 ===
  SR: N/A
  conclusion: killed

=== eval_xvla_l2norm_k085_object_seed43 ===
  SR: N/A
  conclusion: killed

=== eval_xvla_l2norm_k03_object_seed43 ===
  SR: N/A
  conclusion: success

=== eval_xvla_random_k03_object_seed43 ===
  SR: N/A
  conclusion: success

=== eval_xvla_random_k07_object_seed44 ===
  SR: N/A
  conclusion: success

=== eval_xvla_l2norm_k07_object_seed43 ===
  SR: N/A
  conclusion: success

=== eval_xvla_random_k03_object_seed44 ===
  SR: N/A
  conclusion: success

=== eval_xvla_l2norm_k07_object_seed44 ===
  SR: N/A
  conclusion: success

=== eval_xvla_l2norm_k03_object_seed42 ===
  SR: 0.222
  conclusion: success

=== eval_xvla_random_k05_object_seed44 ===
  SR: 0.692
  conclusion: success

=== eval_xvla_l2norm_k07_object_seed42_v2 ===
  SR: 0.582
  conclusion: success

=== eval_xvla_random_k07_object_seed43_v2 ===
  SR: 0.65
  conclusion: success

=== eval_xvla_random_k07_object_seed43 ===
  SR: N/A
  conclusion: failed

=== eval_xvla_random_k03_object_seed42 ===
  SR: 62.8
  conclusion: success

=== eval_xvla_random_k07_object_seed42 ===
  SR: 65.2
  conclusion: success

=== eval_xvla_random_k08_object_seed42 ===
  SR: 89.4
  conclusion: success

=== eval_xvla_random_k09_object_seed42 ===
  SR: 97.8
  conclusion: success
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "790dcd4a-6607-4659-a5a3-a960215f6b9a",
  "uuid": "121676ec-d27e-499a-abaa-273d7269c07b",
  "tool_use_result": {
    "stdout": "=== eval_xvla_random_k085_object_seed42 ===\n  SR: 0.65\n  conclusion: success\n\n=== eval_xvla_random_k05_object_seed42 ===\n  SR: 70.6\n  conclusion: success\n\n=== eval_xvla_l2norm_k05_object_seed42 ===\n  SR: 0.434\n  conclusion: success\n\n=== eval_xvla_l2norm_k05_object_seed43 ===\n  SR: 0.43\n  conclusion: negative\n\n=== eval_xvla_random_k05_object_seed43 ===\n  SR: 0.71\n  conclusion: success\n\n=== eval_xvla_random_k095_object_seed42_v2 ===\n  SR: 0.988\n  conclusion: success\n\n=== eval_xvla_l2norm_k03_object_seed44 ===\n  SR: N/A\n  conclusion: success\n\n=== eval_xvla_random_k07_object_seed42_v2 ===\n  SR: 65.2\n  conclusion: success\n\n=== eval_xvla_random_k085_object_seed43 ===\n  SR: 63.2\n  conclusion: success\n\n=== eval_xvla_random_k085_object_seed42_v2 ===\n  SR: 63.6\n  conclusion: success\n\n=== eval_xvla_l2norm_k03_object_seed42_v2 ===\n  SR: N/A\n  conclusion: killed\n\n=== eval_xvla_l2norm_k085_object_seed43 ===\n  SR: N/A\n  conclusion: killed\n\n=== eval_xvla_l2norm_k03_object_seed43 ===\n  SR: N/A\n  conclusion: success\n\n=== eval_xvla_random_k03_object_seed43 ===\n  SR: N/A\n  conclusion: success\n\n=== eval_xvla_random_k07_object_seed44 ===\n  SR: N/A\n  conclusion: success\n\n=== eval_xvla_l2norm_k07_object_seed43 ===\n  SR: N/A\n  conclusion: success\n\n=== eval_xvla_random_k03_object_seed44 ===\n  SR: N/A\n  conclusion: success\n\n=== eval_xvla_l2norm_k07_object_seed44 ===\n  SR: N/A\n  conclusion: success\n\n=== eval_xvla_l2norm_k03_object_seed42 ===\n  SR: 0.222\n  conclusion: success\n\n=== eval_xvla_random_k05_object_seed44 ===\n  SR: 0.692\n  conclusion: success\n\n=== eval_xvla_l2norm_k07_object_seed42_v2 ===\n  SR: 0.582\n  conclusion: success\n\n=== eval_xvla_random_k07_object_seed43_v2 ===\n  SR: 0.65\n  conclusion: success\n\n=== eval_xvla_random_k07_object_seed43 ===\n  SR: N/A\n  conclusion: failed\n\n=== eval_xvla_random_k03_object_seed42 ===\n  SR: 62.8\n  conclusion: success\n\n=== eval_xvla_random_k07_object_seed42 ===\n  SR: 65.2\n  conclusion: success\n\n=== eval_xvla_random_k08_object_seed42 ===\n  SR: 89.4\n  conclusion: success\n\n=== eval_xvla_random_k09_object_seed42 ===\n  SR: 97.8\n  conclusion: success",
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

_source line 25_

<details><summary>Logged reasoning block</summary>

```text
Now let me also search for the X-VLA baseline for Object suite, and also the other missing X-VLA data points I need. Let me also check for some more specific experiments.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "790dcd4a-6607-4659-a5a3-a960215f6b9a",
  "uuid": "c091a2ec-d830-4cea-a1f4-9f99dda212a3",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Ur3MPbcFjPRZDtsqxrbv3M",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6065,
      "cache_read_input_tokens": 33371,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 6065
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

_source line 26_

Let me get the X-VLA baseline for Object suite and remaining data.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "790dcd4a-6607-4659-a5a3-a960215f6b9a",
  "uuid": "a47abb28-ed04-4c49-9892-8ec738a129ce",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Ur3MPbcFjPRZDtsqxrbv3M",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6065,
      "cache_read_input_tokens": 33371,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 6065
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

_source line 27_

<details open><summary>🔧 Tool call — Bash · `toolu_01C9H1nkqHAuFwzLpXGjaC4r`</summary>

```json
{
  "command": "cat /home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-be-idea-gen-0515-2-projects-importance-margin-vla-compress/790dcd4a-6607-4659-a5a3-a960215f6b9a/tool-results/mcp-agent-ml-research-read_registry-1779781647884.txt | python3 -c \"\nimport json, sys\ndata = json.loads(json.loads(sys.stdin.read())['result'])\nexps = data['data']['experiments']\n# Find X-VLA baseline object\nfor name, exp in exps.items():\n    if 'xvla' in name.lower() and 'object' in name.lower() and ('baseline' in name.lower() or 'k1' in name.lower()):\n        print(f'=== {name} ===')\n        print(f'  metrics: {exp.get(\\\"metrics\\\", {})}')\n        print()\n# Also look for eval_xvla_prune_k1 or similar\nfor name, exp in exps.items():\n    if 'xvla' in name.lower() and ('k1.0' in name or 'k10' in name or 'k1_' in name):\n        print(f'=== {name} ===')\n        print(f'  metrics: {exp.get(\\\"metrics\\\", {})}')\n        print()\n\" 2>&1",
  "description": "Search for X-VLA Object baseline"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "790dcd4a-6607-4659-a5a3-a960215f6b9a",
  "uuid": "52355934-9821-4c2b-9c48-0d4721a2d2c0",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Ur3MPbcFjPRZDtsqxrbv3M",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6065,
      "cache_read_input_tokens": 33371,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 6065
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

_source line 28 · 2026-05-26T07:48:08.054Z_

<details><summary>↩ Tool result · `toolu_01C9H1nkqHAuFwzLpXGjaC4r`</summary>

```text
(Bash completed with no output)
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "790dcd4a-6607-4659-a5a3-a960215f6b9a",
  "uuid": "55e77e38-6bbc-437b-93e3-e99bc40fe77a",
  "tool_use_result": {
    "stdout": "",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  }
}
```

</details>

---


### Tool call

_source line 29_

<details open><summary>🔧 Tool call — Bash · `toolu_01BNhgX59iq8u7C8w2fN8h1o`</summary>

```json
{
  "command": "cat /home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-be-idea-gen-0515-2-projects-importance-margin-vla-compress/790dcd4a-6607-4659-a5a3-a960215f6b9a/tool-results/mcp-agent-ml-research-read_registry-1779781647884.txt | python3 -c \"\nimport json, sys\ndata = json.loads(json.loads(sys.stdin.read())['result'])\nexps = data['data']['experiments']\n# Find X-VLA L2norm experiments for Object with k=0.9 or k=0.95\nfor name, exp in exps.items():\n    if 'xvla' in name.lower() and 'l2norm' in name.lower() and ('object' in name.lower() or 'obj' in name.lower()):\n        sr = exp.get('metrics', {}).get('success_rate', exp.get('metrics', {}).get('overall_SR', exp.get('metrics', {}).get('SR', 'N/A')))\n        print(f'{name}: SR={sr}')\n\" 2>&1",
  "description": "Search for X-VLA L2norm Object experiments"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "790dcd4a-6607-4659-a5a3-a960215f6b9a",
  "uuid": "82fbb7b6-8cd2-4073-b3e5-1bfc970ecef1",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Ur3MPbcFjPRZDtsqxrbv3M",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6065,
      "cache_read_input_tokens": 33371,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 6065
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

_source line 30 · 2026-05-26T07:48:10.183Z_

<details><summary>↩ Tool result · `toolu_01BNhgX59iq8u7C8w2fN8h1o`</summary>

```text
eval_xvla_l2norm_k05_object_seed42: SR=0.434
eval_xvla_l2norm_k05_object_seed43: SR=0.43
eval_xvla_l2norm_k03_object_seed44: SR=N/A
eval_xvla_l2norm_k03_object_seed42_v2: SR=N/A
eval_xvla_l2norm_k085_object_seed43: SR=N/A
eval_xvla_l2norm_k03_object_seed43: SR=0.21
eval_xvla_l2norm_k07_object_seed43: SR=0.59
eval_xvla_l2norm_k07_object_seed44: SR=0.564
eval_xvla_l2norm_k03_object_seed42: SR=0.222
eval_xvla_l2norm_k07_object_seed42_v2: SR=0.582
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "790dcd4a-6607-4659-a5a3-a960215f6b9a",
  "uuid": "987cae50-868f-4816-a2a0-48c81fc4d82a",
  "tool_use_result": {
    "stdout": "eval_xvla_l2norm_k05_object_seed42: SR=0.434\neval_xvla_l2norm_k05_object_seed43: SR=0.43\neval_xvla_l2norm_k03_object_seed44: SR=N/A\neval_xvla_l2norm_k03_object_seed42_v2: SR=N/A\neval_xvla_l2norm_k085_object_seed43: SR=N/A\neval_xvla_l2norm_k03_object_seed43: SR=0.21\neval_xvla_l2norm_k07_object_seed43: SR=0.59\neval_xvla_l2norm_k07_object_seed44: SR=0.564\neval_xvla_l2norm_k03_object_seed42: SR=0.222\neval_xvla_l2norm_k07_object_seed42_v2: SR=0.582",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  }
}
```

</details>

---


### Tool call

_source line 31_

<details open><summary>🔧 Tool call — Bash · `toolu_01QcK3DsiNBQConyaNYwow62`</summary>

```json
{
  "command": "cat /home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-be-idea-gen-0515-2-projects-importance-margin-vla-compress/790dcd4a-6607-4659-a5a3-a960215f6b9a/tool-results/mcp-agent-ml-research-read_registry-1779781647884.txt | python3 -c \"\nimport json, sys\ndata = json.loads(json.loads(sys.stdin.read())['result'])\nexps = data['data']['experiments']\n# X-VLA L2norm k=0.9 and k=0.95 for Object\nfor name, exp in exps.items():\n    if 'xvla' in name.lower() and ('k09' in name or 'k095' in name) and ('object' in name.lower() or 'obj' in name.lower()):\n        sr = exp.get('metrics', {}).get('success_rate', exp.get('metrics', {}).get('overall_SR', exp.get('metrics', {}).get('SR', 'N/A')))\n        print(f'{name}: SR={sr}')\nfor name, exp in exps.items():\n    if 'xvla' in name.lower() and 'l2norm' in name.lower() and ('k09' in name or 'k095' in name):\n        sr = exp.get('metrics', {}).get('success_rate', exp.get('metrics', {}).get('overall_SR', exp.get('metrics', {}).get('SR', 'N/A')))\n        suite = exp.get('metrics', {}).get('suite', '')\n        print(f'{name}: SR={sr}, suite={suite}')\n\" 2>&1",
  "description": "Search for X-VLA L2norm k=0.9/0.95 Object"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "790dcd4a-6607-4659-a5a3-a960215f6b9a",
  "uuid": "7b181df8-e99d-417b-8a04-36e593394a35",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Ur3MPbcFjPRZDtsqxrbv3M",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6065,
      "cache_read_input_tokens": 33371,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 6065
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

_source line 32 · 2026-05-26T07:48:14.092Z_

<details><summary>↩ Tool result · `toolu_01QcK3DsiNBQConyaNYwow62`</summary>

```text
eval_xvla_random_k095_object_seed42_v2: SR=0.988
eval_xvla_random_k09_object_seed42: SR=97.8
eval_xvla_l2norm_k09_spatial_seed42: SR=0.788, suite=libero_spatial
eval_xvla_l2norm_k09_goal_seed42: SR=0.702, suite=libero_goal
eval_xvla_l2norm_k095_goal_seed42: SR=0.538, suite=libero_goal
eval_xvla_l2norm_k095_spatial_seed42: SR=0.716, suite=libero_spatial
eval_xvla_l2norm_k09_long_seed42: SR=0.275, suite=libero_10
eval_xvla_l2norm_k095_long_seed42: SR=0.47, suite=libero_10
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "790dcd4a-6607-4659-a5a3-a960215f6b9a",
  "uuid": "d3768613-9b0f-4a3f-905e-f7549b5f6f72",
  "tool_use_result": {
    "stdout": "eval_xvla_random_k095_object_seed42_v2: SR=0.988\neval_xvla_random_k09_object_seed42: SR=97.8\neval_xvla_l2norm_k09_spatial_seed42: SR=0.788, suite=libero_spatial\neval_xvla_l2norm_k09_goal_seed42: SR=0.702, suite=libero_goal\neval_xvla_l2norm_k095_goal_seed42: SR=0.538, suite=libero_goal\neval_xvla_l2norm_k095_spatial_seed42: SR=0.716, suite=libero_spatial\neval_xvla_l2norm_k09_long_seed42: SR=0.275, suite=libero_10\neval_xvla_l2norm_k095_long_seed42: SR=0.47, suite=libero_10",
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

_source line 33_

<details><summary>Logged reasoning block</summary>

```text
I need to find the X-VLA Object baseline. Let me search for it more broadly.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "790dcd4a-6607-4659-a5a3-a960215f6b9a",
  "uuid": "70b55776-12ef-453d-90f2-484080c292cd",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014cGRawtwfzsPen6X5P9NY2",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1926,
      "cache_read_input_tokens": 39436,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1926
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

_source line 34_

<details open><summary>🔧 Tool call — Bash · `toolu_01AUuYxYS4ciXgTv5vH5Rz36`</summary>

```json
{
  "command": "cat /home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-be-idea-gen-0515-2-projects-importance-margin-vla-compress/790dcd4a-6607-4659-a5a3-a960215f6b9a/tool-results/mcp-agent-ml-research-read_registry-1779781647884.txt | python3 -c \"\nimport json, sys\ndata = json.loads(json.loads(sys.stdin.read())['result'])\nexps = data['data']['experiments']\n# Search for xvla_prune_k095 seed42 - this might be Object baseline\nfor name, exp in exps.items():\n    if 'xvla' in name.lower() and 'prune' in name.lower():\n        sr = exp.get('metrics', {}).get('success_rate', 'N/A')\n        print(f'{name}: SR={sr}, metrics={exp.get(\\\"metrics\\\", {})}')\n        print()\n\" 2>&1",
  "description": "Search for X-VLA prune experiments"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "790dcd4a-6607-4659-a5a3-a960215f6b9a",
  "uuid": "89b48baa-b564-49bf-9f87-8317da5de6ef",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014cGRawtwfzsPen6X5P9NY2",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1926,
      "cache_read_input_tokens": 39436,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1926
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

_source line 35 · 2026-05-26T07:48:20.669Z_

<details><summary>↩ Tool result · `toolu_01AUuYxYS4ciXgTv5vH5Rz36`</summary>

```text
eval_xvla_prune_k09_seed42: SR=0.992, metrics={'note': 'Reconstructed entry. SR=99.2% (seed42). Cross-seed range 97.6%–99.2% (seed43=97.6%, seed44=98.2%). Original JSON may exist on cqa1-33015.', 'num_episodes': 500, 'seed': 42, 'success_rate': 0.992}

eval_xvla_prune_k085_seed44: SR=0.682, metrics={'num_episodes': 500, 'success_rate': 0.682, 'wilson_ci_95': [0.64, 0.721]}

eval_xvla_prune_k08_seed44: SR=0.898, metrics={'num_episodes': 500, 'success_rate': 0.898, 'total_successes': 449, 'wilson_ci_95': [0.868, 0.922]}

eval_xvla_prune_k08_seed42: SR=0.888, metrics={'keep_ratio': 0.8, 'n_vision_tokens_kept': 40, 'n_vision_tokens_original': 50, 'num_episodes': 500, 'success_rate': 0.888, 'wilson_ci_95': [0.8573, 0.9127]}

eval_xvla_prune_k085_seed43: SR=0.676, metrics={'keep_ratio': 0.85, 'n_vision_tokens_kept': 42, 'n_vision_tokens_original': 50, 'num_episodes': 500, 'success_rate': 0.676, 'wilson_ci_95': [0.6338, 0.7155]}

eval_xvla_prune_k085_seed42: SR=0.68, metrics={'num_episodes': 500, 'success_rate': 0.68, 'wilson_ci_95': [0.638, 0.719]}

eval_xvla_prune_k08_seed43: SR=0.884, metrics={'num_episodes': 500, 'success_rate': 0.884, 'wilson_ci_95': [0.853, 0.909]}

eval_xvla_prune_k01_seed42: SR=0, metrics={'num_episodes': 500, 'success_rate': 0, 'wilson_ci_95': [0, 0.008]}

eval_xvla_prune_k095_seed43: SR=0.99, metrics={'num_episodes': 500, 'success_rate': 0.99, 'wilson_ci_95': [0.9768, 0.9957]}

eval_xvla_prune_k095_seed44: SR=0.994, metrics={'num_episodes': 500, 'success_rate': 0.994, 'wilson_ci_95': [0.983, 0.998]}

eval_xvla_prune_k095_seed42: SR=0.99, metrics={'num_episodes': 500, 'success_rate': 0.99, 'wilson_ci_95': [0.977, 0.996]}

eval_xvla_prune_k01_seed44: SR=0, metrics={'num_episodes': 500, 'success_rate': 0, 'wilson_ci_95': [0, 0.008]}

eval_xvla_prune_k01_seed43: SR=0, metrics={'num_episodes': 500, 'success_rate': 0, 'wilson_ci_95': [0, 0.0076]}

eval_xvla_prune_k02_seed44: SR=0.04, metrics={'num_episodes': 500, 'success_rate': 0.04}

eval_xvla_prune_k02_seed43: SR=0.048, metrics={'num_episodes': 500, 'success_rate': 0.048}

eval_xvla_prune_k03_seed43: SR=0.21, metrics={'num_episodes': 500, 'success_rate': 0.21}

eval_xvla_prune_k03_seed44: SR=0.228, metrics={'num_episodes': 500, 'success_rate': 0.228}

eval_xvla_prune_k05_seed44: SR=0.444, metrics={'num_episodes': 500, 'success_rate': 0.444}

eval_xvla_prune_k07_seed44: SR=0.564, metrics={'episodes': 500, 'success_rate': 0.564}

eval_xvla_prune_k09_seed44: SR=0.982, metrics={'episodes': 500, 'success_rate': 0.982}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "790dcd4a-6607-4659-a5a3-a960215f6b9a",
  "uuid": "472243a4-e7b0-428f-9e26-db3a0b9abdc9",
  "tool_use_result": {
    "stdout": "eval_xvla_prune_k09_seed42: SR=0.992, metrics={'note': 'Reconstructed entry. SR=99.2% (seed42). Cross-seed range 97.6%–99.2% (seed43=97.6%, seed44=98.2%). Original JSON may exist on cqa1-33015.', 'num_episodes': 500, 'seed': 42, 'success_rate': 0.992}\n\neval_xvla_prune_k085_seed44: SR=0.682, metrics={'num_episodes': 500, 'success_rate': 0.682, 'wilson_ci_95': [0.64, 0.721]}\n\neval_xvla_prune_k08_seed44: SR=0.898, metrics={'num_episodes': 500, 'success_rate': 0.898, 'total_successes': 449, 'wilson_ci_95': [0.868, 0.922]}\n\neval_xvla_prune_k08_seed42: SR=0.888, metrics={'keep_ratio': 0.8, 'n_vision_tokens_kept': 40, 'n_vision_tokens_original': 50, 'num_episodes': 500, 'success_rate': 0.888, 'wilson_ci_95': [0.8573, 0.9127]}\n\neval_xvla_prune_k085_seed43: SR=0.676, metrics={'keep_ratio': 0.85, 'n_vision_tokens_kept': 42, 'n_vision_tokens_original': 50, 'num_episodes': 500, 'success_rate': 0.676, 'wilson_ci_95': [0.6338, 0.7155]}\n\neval_xvla_prune_k085_seed42: SR=0.68, metrics={'num_episodes': 500, 'success_rate': 0.68, 'wilson_ci_95': [0.638, 0.719]}\n\neval_xvla_prune_k08_seed43: SR=0.884, metrics={'num_episodes': 500, 'success_rate': 0.884, 'wilson_ci_95': [0.853, 0.909]}\n\neval_xvla_prune_k01_seed42: SR=0, metrics={'num_episodes': 500, 'success_rate': 0, 'wilson_ci_95': [0, 0.008]}\n\neval_xvla_prune_k095_seed43: SR=0.99, metrics={'num_episodes': 500, 'success_rate': 0.99, 'wilson_ci_95': [0.9768, 0.9957]}\n\neval_xvla_prune_k095_seed44: SR=0.994, metrics={'num_episodes': 500, 'success_rate': 0.994, 'wilson_ci_95': [0.983, 0.998]}\n\neval_xvla_prune_k095_seed42: SR=0.99, metrics={'num_episodes': 500, 'success_rate': 0.99, 'wilson_ci_95': [0.977, 0.996]}\n\neval_xvla_prune_k01_seed44: SR=0, metrics={'num_episodes': 500, 'success_rate': 0, 'wilson_ci_95': [0, 0.008]}\n\neval_xvla_prune_k01_seed43: SR=0, metrics={'num_episodes': 500, 'success_rate': 0, 'wilson_ci_95': [0, 0.0076]}\n\neval_xvla_prune_k02_seed44: SR=0.04, metrics={'num_episodes': 500, 'success_rate': 0.04}\n\neval_xvla_prune_k02_seed43: SR=0.048, metrics={'num_episodes': 500, 'success_rate': 0.048}\n\neval_xvla_prune_k03_seed43: SR=0.21, metrics={'num_episodes': 500, 'success_rate': 0.21}\n\neval_xvla_prune_k03_seed44: SR=0.228, metrics={'num_episodes': 500, 'success_rate': 0.228}\n\neval_xvla_prune_k05_seed44: SR=0.444, metrics={'num_episodes': 500, 'success_rate': 0.444}\n\neval_xvla_prune_k07_seed44: SR=0.564, metrics={'episodes': 500, 'success_rate': 0.564}\n\neval_xvla_prune_k09_seed44: SR=0.982, metrics={'episodes': 500, 'success_rate': 0.982}",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  }
}
```

</details>

---


### Tool call

_source line 36_

<details open><summary>🔧 Tool call — Bash · `toolu_01UgwsVTKsmEsX9GwL5UKqJ6`</summary>

```json
{
  "command": "cat /home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-be-idea-gen-0515-2-projects-importance-margin-vla-compress/790dcd4a-6607-4659-a5a3-a960215f6b9a/tool-results/mcp-agent-ml-research-read_registry-1779781647884.txt | python3 -c \"\nimport json, sys\ndata = json.loads(json.loads(sys.stdin.read())['result'])\nexps = data['data']['experiments']\n# Find X-VLA L2norm k=0.9 object (might be named differently)\nfor name, exp in exps.items():\n    if 'xvla' in name.lower() and ('k09' in name) and 'l2norm' in name.lower():\n        sr = exp.get('metrics', {}).get('success_rate', exp.get('metrics', {}).get('overall_SR', 'N/A'))\n        suite = exp.get('metrics', {}).get('suite', '')\n        print(f'{name}: SR={sr}, suite={suite}')\n# And find X-VLA object baseline - maybe eval_xvla_baseline_object\nfor name, exp in exps.items():\n    if 'xvla' in name.lower() and 'baseline' in name.lower():\n        sr = exp.get('metrics', {}).get('success_rate', 'N/A')\n        suite = name.split('baseline_')[-1] if 'baseline_' in name else ''\n        print(f'{name}: SR={sr}, suite_from_name={suite}')\n\" 2>&1",
  "description": "Search for X-VLA L2norm k=0.9 and baselines"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "790dcd4a-6607-4659-a5a3-a960215f6b9a",
  "uuid": "12f84603-cf87-411e-9758-1f7e4df36b84",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014cGRawtwfzsPen6X5P9NY2",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1926,
      "cache_read_input_tokens": 39436,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1926
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

_source line 37 · 2026-05-26T07:48:25.055Z_

<details><summary>↩ Tool result · `toolu_01UgwsVTKsmEsX9GwL5UKqJ6`</summary>

```text
eval_xvla_l2norm_k09_spatial_seed42: SR=0.788, suite=libero_spatial
eval_xvla_l2norm_k09_goal_seed42: SR=0.702, suite=libero_goal
eval_xvla_l2norm_k095_goal_seed42: SR=0.538, suite=libero_goal
eval_xvla_l2norm_k095_spatial_seed42: SR=0.716, suite=libero_spatial
eval_xvla_l2norm_k09_long_seed42: SR=0.275, suite=libero_10
eval_xvla_l2norm_k095_long_seed42: SR=0.47, suite=libero_10
eval_xvla_baseline_spatial_seed42: SR=0.93, suite_from_name=spatial_seed42
eval_xvla_baseline_goal_seed42: SR=0.984, suite_from_name=goal_seed42
eval_xvla_baseline_long_seed42: SR=0.94, suite_from_name=long_seed42
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "790dcd4a-6607-4659-a5a3-a960215f6b9a",
  "uuid": "f471488a-8fba-4278-8f54-a85d37864c6d",
  "tool_use_result": {
    "stdout": "eval_xvla_l2norm_k09_spatial_seed42: SR=0.788, suite=libero_spatial\neval_xvla_l2norm_k09_goal_seed42: SR=0.702, suite=libero_goal\neval_xvla_l2norm_k095_goal_seed42: SR=0.538, suite=libero_goal\neval_xvla_l2norm_k095_spatial_seed42: SR=0.716, suite=libero_spatial\neval_xvla_l2norm_k09_long_seed42: SR=0.275, suite=libero_10\neval_xvla_l2norm_k095_long_seed42: SR=0.47, suite=libero_10\neval_xvla_baseline_spatial_seed42: SR=0.93, suite_from_name=spatial_seed42\neval_xvla_baseline_goal_seed42: SR=0.984, suite_from_name=goal_seed42\neval_xvla_baseline_long_seed42: SR=0.94, suite_from_name=long_seed42",
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

_source line 38_

<details><summary>Logged reasoning block</summary>

```text
I notice there's no explicit X-VLA baseline for Object. The `eval_xvla_prune_k095_seed42` entries (SR=99.0%) seem to be Object suite since there are separate baseline entries for spatial, goal, and long. Let me also look for X-VLA L2norm k=0.9 for Object specifically.

Let me also check for eval_xvla_l2norm_k09_object or eval_xvla_l2norm_k095_object entries.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "790dcd4a-6607-4659-a5a3-a960215f6b9a",
  "uuid": "ae91584e-78f9-415b-952d-127d2710323d",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018bmeqCBwhf6Sw1YFsc2nWg",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2373,
      "cache_read_input_tokens": 41362,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2373
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

_source line 39_

<details open><summary>🔧 Tool call — Bash · `toolu_01NdZ2HncFMTyF6MCvauu3eh`</summary>

```json
{
  "command": "cat /home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-be-idea-gen-0515-2-projects-importance-margin-vla-compress/790dcd4a-6607-4659-a5a3-a960215f6b9a/tool-results/mcp-agent-ml-research-read_registry-1779781647884.txt | python3 -c \"\nimport json, sys\ndata = json.loads(json.loads(sys.stdin.read())['result'])\nexps = data['data']['experiments']\n# Find xvla_prune entries without suite name - these are probably Object\nfor name, exp in exps.items():\n    if name.startswith('eval_xvla_prune_') and 'object' not in name and 'spatial' not in name and 'goal' not in name and 'long' not in name:\n        sr = exp.get('metrics', {}).get('success_rate', 'N/A')\n        suite = exp.get('metrics', {}).get('suite', 'not specified')\n        print(f'{name}: SR={sr}, suite={suite}')\n\n# Find if there's a k=1.0 baseline for Object\nprint()\nprint('--- Looking for Object baseline ---')\nfor name, exp in exps.items():\n    if 'xvla' in name.lower() and ('k1.0' in name or 'k10' in name or 'baseline_object' in name or 'baseline_obj' in name):\n        sr = exp.get('metrics', {}).get('success_rate', 'N/A')\n        print(f'{name}: SR={sr}')\n\" 2>&1",
  "description": "Find X-VLA Object baseline"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "790dcd4a-6607-4659-a5a3-a960215f6b9a",
  "uuid": "c1bcad83-55f6-498e-9603-b75ef594250b",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018bmeqCBwhf6Sw1YFsc2nWg",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2373,
      "cache_read_input_tokens": 41362,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2373
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

_source line 40 · 2026-05-26T07:48:46.869Z_

<details><summary>↩ Tool result · `toolu_01NdZ2HncFMTyF6MCvauu3eh`</summary>

```text
eval_xvla_prune_k09_seed42: SR=0.992, suite=not specified
eval_xvla_prune_k085_seed44: SR=0.682, suite=not specified
eval_xvla_prune_k08_seed44: SR=0.898, suite=not specified
eval_xvla_prune_k08_seed42: SR=0.888, suite=not specified
eval_xvla_prune_k085_seed43: SR=0.676, suite=not specified
eval_xvla_prune_k085_seed42: SR=0.68, suite=not specified
eval_xvla_prune_k08_seed43: SR=0.884, suite=not specified
eval_xvla_prune_k01_seed42: SR=0, suite=not specified
eval_xvla_prune_k095_seed43: SR=0.99, suite=not specified
eval_xvla_prune_k095_seed44: SR=0.994, suite=not specified
eval_xvla_prune_k095_seed42: SR=0.99, suite=not specified
eval_xvla_prune_k01_seed44: SR=0, suite=not specified
eval_xvla_prune_k01_seed43: SR=0, suite=not specified
eval_xvla_prune_k02_seed44: SR=0.04, suite=not specified
eval_xvla_prune_k02_seed43: SR=0.048, suite=not specified
eval_xvla_prune_k03_seed43: SR=0.21, suite=not specified
eval_xvla_prune_k03_seed44: SR=0.228, suite=not specified
eval_xvla_prune_k05_seed44: SR=0.444, suite=not specified
eval_xvla_prune_k07_seed44: SR=0.564, suite=not specified
eval_xvla_prune_k09_seed44: SR=0.982, suite=not specified

--- Looking for Object baseline ---
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "790dcd4a-6607-4659-a5a3-a960215f6b9a",
  "uuid": "aa2eaad6-5448-4c8e-9ffd-25376f12dae3",
  "tool_use_result": {
    "stdout": "eval_xvla_prune_k09_seed42: SR=0.992, suite=not specified\neval_xvla_prune_k085_seed44: SR=0.682, suite=not specified\neval_xvla_prune_k08_seed44: SR=0.898, suite=not specified\neval_xvla_prune_k08_seed42: SR=0.888, suite=not specified\neval_xvla_prune_k085_seed43: SR=0.676, suite=not specified\neval_xvla_prune_k085_seed42: SR=0.68, suite=not specified\neval_xvla_prune_k08_seed43: SR=0.884, suite=not specified\neval_xvla_prune_k01_seed42: SR=0, suite=not specified\neval_xvla_prune_k095_seed43: SR=0.99, suite=not specified\neval_xvla_prune_k095_seed44: SR=0.994, suite=not specified\neval_xvla_prune_k095_seed42: SR=0.99, suite=not specified\neval_xvla_prune_k01_seed44: SR=0, suite=not specified\neval_xvla_prune_k01_seed43: SR=0, suite=not specified\neval_xvla_prune_k02_seed44: SR=0.04, suite=not specified\neval_xvla_prune_k02_seed43: SR=0.048, suite=not specified\neval_xvla_prune_k03_seed43: SR=0.21, suite=not specified\neval_xvla_prune_k03_seed44: SR=0.228, suite=not specified\neval_xvla_prune_k05_seed44: SR=0.444, suite=not specified\neval_xvla_prune_k07_seed44: SR=0.564, suite=not specified\neval_xvla_prune_k09_seed44: SR=0.982, suite=not specified\n\n--- Looking for Object baseline ---",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  }
}
```

</details>

---


### Tool call

_source line 41_

<details open><summary>🔧 Tool call — Bash · `toolu_013GSMMukPnk4UciWiKahrEu`</summary>

```json
{
  "command": "cat /home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-be-idea-gen-0515-2-projects-importance-margin-vla-compress/790dcd4a-6607-4659-a5a3-a960215f6b9a/tool-results/mcp-agent-ml-research-read_registry-1779781647884.txt | python3 -c \"\nimport json, sys\ndata = json.loads(json.loads(sys.stdin.read())['result'])\nexps = data['data']['experiments']\n# Find L2norm k=0.9 and k=0.95 for Object\nfor name, exp in exps.items():\n    if 'xvla' in name.lower() and 'l2norm' in name.lower() and ('k09' in name or 'k095' in name) and ('object' in name.lower() or 'obj' in name.lower()):\n        sr = exp.get('metrics', {}).get('success_rate', exp.get('metrics', {}).get('SR', 'N/A'))\n        print(f'{name}: SR={sr}')\n\n# Also search for random k=0.9 and k=0.95 for Goal\nprint()\nprint('--- Random k=0.9/0.95 for X-VLA Goal ---')\nfor name, exp in exps.items():\n    if 'xvla' in name.lower() and 'random' in name.lower() and ('k09' in name or 'k095' in name) and 'goal' in name.lower():\n        sr = exp.get('metrics', {}).get('success_rate', exp.get('metrics', {}).get('overall_SR', 'N/A'))\n        print(f'{name}: SR={sr}')\n\" 2>&1",
  "description": "Find X-VLA L2norm/Random for Object and Goal"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "790dcd4a-6607-4659-a5a3-a960215f6b9a",
  "uuid": "d2cdfc52-ec98-42fe-8b94-e2a9d7596c13",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018bmeqCBwhf6Sw1YFsc2nWg",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2373,
      "cache_read_input_tokens": 41362,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2373
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

_source line 42 · 2026-05-26T07:48:50.686Z_

<details><summary>↩ Tool result · `toolu_013GSMMukPnk4UciWiKahrEu`</summary>

```text
--- Random k=0.9/0.95 for X-VLA Goal ---
eval_xvla_random_k09_goal_seed42: SR=0.706
eval_xvla_random_k095_goal_seed42: SR=0.54
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "790dcd4a-6607-4659-a5a3-a960215f6b9a",
  "uuid": "d9c726e3-8df1-4506-9593-ac21784cc32d",
  "tool_use_result": {
    "stdout": "--- Random k=0.9/0.95 for X-VLA Goal ---\neval_xvla_random_k09_goal_seed42: SR=0.706\neval_xvla_random_k095_goal_seed42: SR=0.54",
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

_source line 43_

<details><summary>Logged reasoning block</summary>

```text
Now I need to figure out the X-VLA Object baseline. These `eval_xvla_prune_` entries without a suite name seem to be L2norm pruning on Object suite. Looking at SR at k=0.95: 99.0% and k=0.9: 99.2% — these seem like Object suite baselines based on the very high success rates.

But I need the actual baseline (k=1.0). Let me check if there's one, or if I should use the xvla_prune_k095 results. Actually, these "prune" experiments are actually L2norm pruning on what appears to be Object suite. 

I'm searching through the data for an explicit k=1.0 baseline or Object suite entry, but it doesn't seem to be in the registry, so I should check the ROADMAP or memory files instead. I'm noticing the X-VLA Object baseline isn't explicitly listed in the registry—I have Goal, Spatial, and Long baselines, but no Object entry. Looking at the earlier prune and random experiments on the Object suite, the performance around 97.8-98.8% suggests that's probably close to where the baseline should be, so I might need to check project files or reports to find the actual value.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "790dcd4a-6607-4659-a5a3-a960215f6b9a",
  "uuid": "ac4bdb29-bbb3-4634-9de5-440750008061",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Cx81Ve5GYSfMJWi17mUz3K",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1773,
      "cache_read_input_tokens": 43735,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1773
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

_source line 44_

<details open><summary>🔧 Tool call — Bash · `toolu_01EdfNyG7g4sCq6nRQ9Zmanu`</summary>

```json
{
  "command": "cat /home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-be-idea-gen-0515-2-projects-importance-margin-vla-compress/790dcd4a-6607-4659-a5a3-a960215f6b9a/tool-results/mcp-agent-ml-research-read_registry-1779781647884.txt | python3 -c \"\nimport json, sys\ndata = json.loads(json.loads(sys.stdin.read())['result'])\nexps = data['data']['experiments']\n# Search for xvla k=1 or baseline object\nfor name, exp in exps.items():\n    if 'xvla' in name.lower() and ('k1_' in name or 'k1.0' in name or 'k10_' in name or 'noprun' in name.lower() or 'full' in name.lower()):\n        sr = exp.get('metrics', {}).get('success_rate', 'N/A')\n        print(f'{name}: SR={sr}, metrics={exp.get(\\\"metrics\\\", {})}')\n\n# Also check for xvla_object_baseline or xvla_obj_baseline\nprint()\nfor name, exp in exps.items():\n    if 'xvla' in name.lower() and 'obj' in name.lower() and ('base' in name.lower() or 'full' in name.lower() or 'unprun' in name.lower()):\n        sr = exp.get('metrics', {}).get('success_rate', 'N/A')\n        print(f'{name}: SR={sr}')\n\" 2>&1",
  "description": "Find X-VLA full/k=1.0 baselines"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "790dcd4a-6607-4659-a5a3-a960215f6b9a",
  "uuid": "6f93da32-b5e8-4a01-a664-847882be6b3b",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Cx81Ve5GYSfMJWi17mUz3K",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1773,
      "cache_read_input_tokens": 43735,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1773
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

_source line 45 · 2026-05-26T07:49:15.717Z_

<details><summary>↩ Tool result · `toolu_01EdfNyG7g4sCq6nRQ9Zmanu`</summary>

```text
(Bash completed with no output)
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "790dcd4a-6607-4659-a5a3-a960215f6b9a",
  "uuid": "6ec8e420-265b-4a94-af70-0b6b0eca3539",
  "tool_use_result": {
    "stdout": "",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  }
}
```

</details>

---


### Tool call

_source line 46_

<details open><summary>🔧 Tool call — Glob · `toolu_01MNpiQDtxy5AqRupGvUqKom`</summary>

```json
{
  "pattern": "**/report.md",
  "path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "790dcd4a-6607-4659-a5a3-a960215f6b9a",
  "uuid": "5a64875c-42ba-4883-96a4-08e65933085f",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Cx81Ve5GYSfMJWi17mUz3K",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1773,
      "cache_read_input_tokens": 43735,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1773
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

_source line 47 · 2026-05-26T07:49:16.216Z_

<details><summary>↩ Tool result · `toolu_01MNpiQDtxy5AqRupGvUqKom`</summary>

```text
report.md
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "790dcd4a-6607-4659-a5a3-a960215f6b9a",
  "uuid": "99e13246-e1aa-4eb7-9417-66850f16ac53",
  "tool_use_result": {
    "filenames": [
      "report.md"
    ],
    "durationMs": 58,
    "numFiles": 1,
    "truncated": false
  }
}
```

</details>

---


### Tool call

_source line 48_

<details open><summary>🔧 Tool call — Bash · `toolu_01J8AU5watow8nPRhkc96YkC`</summary>

```json
{
  "command": "cat /home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/report.md | grep -i \"xvla\\|x-vla\\|x_vla\" -A 5 | head -100",
  "description": "Search report for X-VLA baseline data"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "790dcd4a-6607-4659-a5a3-a960215f6b9a",
  "uuid": "102aaff4-1c90-482a-8bc8-210e1782ef19",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017thYGsdJQzGcK2Vmns8Dgv",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1509,
      "cache_read_input_tokens": 45508,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1509
      },
      "output_tokens": 67,
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

_source line 49 · 2026-05-26T07:49:19.759Z_

<details><summary>↩ Tool result · `toolu_01J8AU5watow8nPRhkc96YkC`</summary>

```text
- eval_e5_xvla_attn_last_goal_k03: 已被终止 — unknown
- eval_e5_xvla_attn_mean_goal_k03: 已被终止 — unknown
- eval_k07_bypass_v2: 训练失败 — unknown
- eval_official_smolvla_prune_k05_spatial: 训练失败 — unknown
- eval_official_smolvla_pruning: 训练失败 — unknown
- eval_oft_baseline_k10: 训练失败 — unknown
- eval_oft_baseline_object_seed42: 已被终止 — unknown
--
- eval_xvla_l2norm_k03_goal_seed42: 训练失败 — unknown
- eval_xvla_l2norm_k03_goal_seed42_v2: 已被终止 — unknown
- eval_xvla_l2norm_k03_long_seed42: 已被终止 — unknown
- eval_xvla_l2norm_k03_object_seed42_v2: 已被终止 — unknown
- eval_xvla_l2norm_k05_long_seed42_v3: 已被终止 — unknown
- eval_xvla_l2norm_k05_spatial_seed42_v2: 已被终止 — unknown
- eval_xvla_l2norm_k07_long_seed42_v2: 已被终止 — unknown
- eval_xvla_l2norm_k085_object_seed43: 已被终止 — unknown
- eval_xvla_random_k03_long_seed42: 已被终止 — unknown
- eval_xvla_random_k05_goal_seed42: 训练失败 — unknown
- eval_xvla_random_k05_goal_seed43: 训练失败 — unknown
- eval_xvla_random_k05_goal_seed43_v2: 训练失败 — unknown
- eval_xvla_random_k05_goal_seed43_v3: 已被终止 — unknown
- eval_xvla_random_k07_object_seed43: 训练失败 — unknown
- libero_fullft_batch64: 训练失败 — unknown
- libero_fullft_batch64_v2: 已被终止 — unknown
- libero_imm_twostage_v1: 已被终止 — unknown
- mvp_baseline: 训练失败 — unknown
- mvp_baseline_v2: 训练失败 — unknown
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "790dcd4a-6607-4659-a5a3-a960215f6b9a",
  "uuid": "d15629b4-2966-49aa-a900-f4ab3a4d9288",
  "tool_use_result": {
    "stdout": "- eval_e5_xvla_attn_last_goal_k03: 已被终止 — unknown\n- eval_e5_xvla_attn_mean_goal_k03: 已被终止 — unknown\n- eval_k07_bypass_v2: 训练失败 — unknown\n- eval_official_smolvla_prune_k05_spatial: 训练失败 — unknown\n- eval_official_smolvla_pruning: 训练失败 — unknown\n- eval_oft_baseline_k10: 训练失败 — unknown\n- eval_oft_baseline_object_seed42: 已被终止 — unknown\n--\n- eval_xvla_l2norm_k03_goal_seed42: 训练失败 — unknown\n- eval_xvla_l2norm_k03_goal_seed42_v2: 已被终止 — unknown\n- eval_xvla_l2norm_k03_long_seed42: 已被终止 — unknown\n- eval_xvla_l2norm_k03_object_seed42_v2: 已被终止 — unknown\n- eval_xvla_l2norm_k05_long_seed42_v3: 已被终止 — unknown\n- eval_xvla_l2norm_k05_spatial_seed42_v2: 已被终止 — unknown\n- eval_xvla_l2norm_k07_long_seed42_v2: 已被终止 — unknown\n- eval_xvla_l2norm_k085_object_seed43: 已被终止 — unknown\n- eval_xvla_random_k03_long_seed42: 已被终止 — unknown\n- eval_xvla_random_k05_goal_seed42: 训练失败 — unknown\n- eval_xvla_random_k05_goal_seed43: 训练失败 — unknown\n- eval_xvla_random_k05_goal_seed43_v2: 训练失败 — unknown\n- eval_xvla_random_k05_goal_seed43_v3: 已被终止 — unknown\n- eval_xvla_random_k07_object_seed43: 训练失败 — unknown\n- libero_fullft_batch64: 训练失败 — unknown\n- libero_fullft_batch64_v2: 已被终止 — unknown\n- libero_imm_twostage_v1: 已被终止 — unknown\n- mvp_baseline: 训练失败 — unknown\n- mvp_baseline_v2: 训练失败 — unknown",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  }
}
```

</details>

---


### Tool call

_source line 50_

<details open><summary>🔧 Tool call — Bash · `toolu_01RWSHf3CXPW3bzaKVZfEuT1`</summary>

```json
{
  "command": "grep -i \"x-vla\\|xvla\" /home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/report.md | grep -i \"baseline\\|100%\\|object.*base\" | head -20",
  "description": "Search report for X-VLA object baseline"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "790dcd4a-6607-4659-a5a3-a960215f6b9a",
  "uuid": "d90a58df-ec50-4089-b793-9539f88a705e",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Rwat2oUC6hxeD5to1GFq6i",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 819,
      "cache_read_input_tokens": 47017,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 819
      },
      "output_tokens": 64,
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

_source line 51 · 2026-05-26T07:49:32.128Z_

<details><summary>↩ Tool result · `toolu_01RWSHf3CXPW3bzaKVZfEuT1`</summary>

```text
(Bash completed with no output)
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "790dcd4a-6607-4659-a5a3-a960215f6b9a",
  "uuid": "32ffe63c-8dcc-4c49-b9cd-c047f9beb436",
  "tool_use_result": {
    "stdout": "",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  }
}
```

</details>

---


### Tool call

_source line 52_

<details open><summary>🔧 Tool call — Bash · `toolu_01D7UCL2RP36nF11eqHU7ZyC`</summary>

```json
{
  "command": "grep -i \"x-vla\\|xvla\" /home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/report.md | grep -i \"object\" | head -20",
  "description": "Search report for X-VLA object references"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "790dcd4a-6607-4659-a5a3-a960215f6b9a",
  "uuid": "76e00c2e-d9fd-411b-8d6a-5c29214da497",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012jYdQxPg5V18NencVDK2iF",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 164,
      "cache_read_input_tokens": 47836,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 164
      },
      "output_tokens": 72,
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

_source line 53 · 2026-05-26T07:49:34.689Z_

<details><summary>↩ Tool result · `toolu_01D7UCL2RP36nF11eqHU7ZyC`</summary>

```text
- eval_xvla_l2norm_k03_object_seed42_v2: 已被终止 — unknown
- eval_xvla_l2norm_k085_object_seed43: 已被终止 — unknown
- eval_xvla_random_k07_object_seed43: 训练失败 — unknown
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "790dcd4a-6607-4659-a5a3-a960215f6b9a",
  "uuid": "6ce58144-11c8-4aca-94e9-f01617a40901",
  "tool_use_result": {
    "stdout": "- eval_xvla_l2norm_k03_object_seed42_v2: 已被终止 — unknown\n- eval_xvla_l2norm_k085_object_seed43: 已被终止 — unknown\n- eval_xvla_random_k07_object_seed43: 训练失败 — unknown",
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

_source line 54_

<details><summary>Logged reasoning block</summary>

```text
I don't have an explicit X-VLA Object baseline. Looking at the data:
- eval_xvla_prune_k095_seed42: SR=99.0% (these early experiments seem to be Object suite L2norm pruning)
- eval_xvla_random_k095_object_seed42_v2: SR=98.8%

Given the pattern, these early `eval_xvla_prune_` experiments were Object suite, and k=1.0 (baseline) isn't explicitly recorded. But looking at memory.md or ideas.md might help.

Let me check the memory file.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "790dcd4a-6607-4659-a5a3-a960215f6b9a",
  "uuid": "fb20f288-b668-43d3-ae38-cac9bb84a460",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DY12dddEEQ9MYK8aYGdRqE",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 233,
      "cache_read_input_tokens": 48000,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 233
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

_source line 55_

<details open><summary>🔧 Tool call — Bash · `toolu_0166xcxMQgYv2J6kycJ2LqJC`</summary>

```json
{
  "command": "grep -i \"x-vla\\|xvla\" /home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/memory.md 2>/dev/null | head -30",
  "description": "Search memory for X-VLA Object baseline"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "790dcd4a-6607-4659-a5a3-a960215f6b9a",
  "uuid": "2c0cee89-4fb8-41c3-9029-ad2f36ee31f0",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DY12dddEEQ9MYK8aYGdRqE",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 233,
      "cache_read_input_tokens": 48000,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 233
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

_source line 56 · 2026-05-26T07:49:41.049Z_

<details><summary>↩ Tool result · `toolu_0166xcxMQgYv2J6kycJ2LqJC`</summary>

```text
(Bash completed with no output)
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "790dcd4a-6607-4659-a5a3-a960215f6b9a",
  "uuid": "27515dff-2255-484b-a8e0-1026ca4befd4",
  "tool_use_result": {
    "stdout": "",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  }
}
```

</details>

---


### Tool call

_source line 57_

<details open><summary>🔧 Tool call — Bash · `toolu_014ZFdACmQbbfcz3ZJ9UhDDQ`</summary>

```json
{
  "command": "cat /home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-be-idea-gen-0515-2-projects-importance-margin-vla-compress/790dcd4a-6607-4659-a5a3-a960215f6b9a/tool-results/mcp-agent-ml-research-read_registry-1779781647884.txt | python3 -c \"\nimport json, sys\ndata = json.loads(json.loads(sys.stdin.read())['result'])\nexps = data['data']['experiments']\n# Find pi05 experiments\nfor name, exp in exps.items():\n    if ('pi05' in name.lower() or 'pi0.5' in name.lower() or 'pi0_5' in name.lower()) and exp.get('conclusion') not in ['killed', 'failed']:\n        sr = exp.get('metrics', {}).get('success_rate', exp.get('metrics', {}).get('overall_sr', exp.get('metrics', {}).get('overall_SR', 'N/A')))\n        if sr != 'N/A':\n            print(f'{name}: SR={sr}')\n\" 2>&1 | head -50",
  "description": "Search for pi0.5 experiments"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "790dcd4a-6607-4659-a5a3-a960215f6b9a",
  "uuid": "04754893-1561-44b7-af12-d7981dc4e00c",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DY12dddEEQ9MYK8aYGdRqE",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 233,
      "cache_read_input_tokens": 48000,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 233
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

_source line 58 · 2026-05-26T07:49:46.647Z_

<details><summary>↩ Tool result · `toolu_014ZFdACmQbbfcz3ZJ9UhDDQ`</summary>

```text
eval_pi05_zeromask_random_k09_object_seed42_v3: SR=0.98
eval_pi05_random_k05_long_seed42: SR=0.502
eval_pi05_l2norm_k05_long_seed42: SR=0.502
eval_pi05_l2norm_k03_goal_seed42_postfix: SR=0.518
eval_pi05_random_k09_long_seed43_postfix: SR=0.356
eval_pi05_random_k085_long_seed43_postfix: SR=0.418
eval_pi05_l2norm_k05_spatial_seed42_postfix: SR=0.574
eval_pi05_zeromask_l2norm_k09_object_seed42: SR=0.994
eval_pi05_l2norm_k0925_long_seed42_v2: SR=0.832
eval_pi05_l2norm_k05_long_seed43_postfix_v2: SR=0.53
eval_pi05_random_k0925_long_seed42_postfix: SR=38.6
eval_pi05_attention_k09_long_seed42_postfix: SR=0.638
eval_pi05_random_k07_long_seed43_postfix: SR=0.686
eval_pi05_random_k03_long_seed43_v4: SR=0.272
eval_pi05_l2norm_k07_long_seed43_v3: SR=0.65
eval_pi05_l2norm_k085_long_seed43_v3: SR=80
eval_pi05_l2norm_k09_long_seed43_postfix: SR=0.808
eval_pi05_l2norm_k0925_goal_seed42_postfix: SR=89.8
eval_pi05_random_k085_long_seed42_postfix_v3: SR=49.4
eval_pi05_l2norm_k085_long_seed42_postfix_v3: SR=0.78
eval_pi05_random_k085_goal_seed42_postfix_v3: SR=53
eval_pi05_l2norm_k085_object_seed42_postfix_v2: SR=98.4
eval_pi05_random_k085_object_seed42_postfix: SR=5.6
eval_pi05_l2norm_k085_goal_seed42_postfix: SR=87.4
eval_pi05_l2norm_k085_goal_seed43_postfix: SR=87
eval_pi05_random_k085_long_seed43_v2: SR=42
eval_pi05_random_k085_spatial_seed43_postfix: SR=59.2
eval_pi05_l2norm_k085_object_seed43_postfix: SR=99
eval_pi05_random_k085_goal_seed43_postfix: SR=0.534
eval_pi05_l2norm_k085_spatial_seed43_postfix: SR=0.882
eval_pi05_random_k085_object_seed43_postfix: SR=0.048
eval_pi05_l2norm_k085_long_seed43_postfix: SR=78.6
pi05_baseline_long_seed42: SR=92.8
eval_pi05_baseline_spatial_seed42: SR=97.2
eval_pi05_baseline_long_seed42: SR=92.8
eval_pi05_baseline_object_seed42: SR=98.2
eval_pi05_random_k09_spatial_seed43_postfix_v2: SR=54
eval_pi05_random_k05_long_seed43_postfix: SR=46.8
eval_pi05_random_k095_long_seed43_postfix: SR=0.584
eval_pi05_random_k09_object_seed43_postfix: SR=7.4
eval_pi05_random_k09_goal_seed43_postfix: SR=61.2
eval_pi05_l2norm_k03_long_seed43_postfix_v2: SR=39.2
eval_pi05_l2norm_k09_object_seed43_postfix: SR=98.4
eval_pi05_l2norm_k09_goal_seed43_postfix: SR=91
eval_pi05_l2norm_k09_spatial_seed43_postfix: SR=96.2
eval_pi05_l2norm_k07_long_seed42_postfix: SR=62.6
eval_pi05_random_k03_long_seed42_postfix: SR=29.6
eval_pi05_l2norm_k09_long_seed42_postfix_v2: SR=80
eval_pi05_l2norm_k095_long_seed43_postfix: SR=87.4
eval_pi05_l2norm_k09_long_seed43_postfix_v2: SR=80
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "790dcd4a-6607-4659-a5a3-a960215f6b9a",
  "uuid": "d206660d-782d-4065-b164-85fa68c374d9",
  "tool_use_result": {
    "stdout": "eval_pi05_zeromask_random_k09_object_seed42_v3: SR=0.98\neval_pi05_random_k05_long_seed42: SR=0.502\neval_pi05_l2norm_k05_long_seed42: SR=0.502\neval_pi05_l2norm_k03_goal_seed42_postfix: SR=0.518\neval_pi05_random_k09_long_seed43_postfix: SR=0.356\neval_pi05_random_k085_long_seed43_postfix: SR=0.418\neval_pi05_l2norm_k05_spatial_seed42_postfix: SR=0.574\neval_pi05_zeromask_l2norm_k09_object_seed42: SR=0.994\neval_pi05_l2norm_k0925_long_seed42_v2: SR=0.832\neval_pi05_l2norm_k05_long_seed43_postfix_v2: SR=0.53\neval_pi05_random_k0925_long_seed42_postfix: SR=38.6\neval_pi05_attention_k09_long_seed42_postfix: SR=0.638\neval_pi05_random_k07_long_seed43_postfix: SR=0.686\neval_pi05_random_k03_long_seed43_v4: SR=0.272\neval_pi05_l2norm_k07_long_seed43_v3: SR=0.65\neval_pi05_l2norm_k085_long_seed43_v3: SR=80\neval_pi05_l2norm_k09_long_seed43_postfix: SR=0.808\neval_pi05_l2norm_k0925_goal_seed42_postfix: SR=89.8\neval_pi05_random_k085_long_seed42_postfix_v3: SR=49.4\neval_pi05_l2norm_k085_long_seed42_postfix_v3: SR=0.78\neval_pi05_random_k085_goal_seed42_postfix_v3: SR=53\neval_pi05_l2norm_k085_object_seed42_postfix_v2: SR=98.4\neval_pi05_random_k085_object_seed42_postfix: SR=5.6\neval_pi05_l2norm_k085_goal_seed42_postfix: SR=87.4\neval_pi05_l2norm_k085_goal_seed43_postfix: SR=87\neval_pi05_random_k085_long_seed43_v2: SR=42\neval_pi05_random_k085_spatial_seed43_postfix: SR=59.2\neval_pi05_l2norm_k085_object_seed43_postfix: SR=99\neval_pi05_random_k085_goal_seed43_postfix: SR=0.534\neval_pi05_l2norm_k085_spatial_seed43_postfix: SR=0.882\neval_pi05_random_k085_object_seed43_postfix: SR=0.048\neval_pi05_l2norm_k085_long_seed43_postfix: SR=78.6\npi05_baseline_long_seed42: SR=92.8\neval_pi05_baseline_spatial_seed42: SR=97.2\neval_pi05_baseline_long_seed42: SR=92.8\neval_pi05_baseline_object_seed42: SR=98.2\neval_pi05_random_k09_spatial_seed43_postfix_v2: SR=54\neval_pi05_random_k05_long_seed43_postfix: SR=46.8\neval_pi05_random_k095_long_seed43_postfix: SR=0.584\neval_pi05_random_k09_object_seed43_postfix: SR=7.4\neval_pi05_random_k09_goal_seed43_postfix: SR=61.2\neval_pi05_l2norm_k03_long_seed43_postfix_v2: SR=39.2\neval_pi05_l2norm_k09_object_seed43_postfix: SR=98.4\neval_pi05_l2norm_k09_goal_seed43_postfix: SR=91\neval_pi05_l2norm_k09_spatial_seed43_postfix: SR=96.2\neval_pi05_l2norm_k07_long_seed42_postfix: SR=62.6\neval_pi05_random_k03_long_seed42_postfix: SR=29.6\neval_pi05_l2norm_k09_long_seed42_postfix_v2: SR=80\neval_pi05_l2norm_k095_long_seed43_postfix: SR=87.4\neval_pi05_l2norm_k09_long_seed43_postfix_v2: SR=80",
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

_source line 59_

<details><summary>Logged reasoning block</summary>

```text
Now I have a lot of data. Let me also find the OpenVLA and SmolVLA data, as well as pi0.5 data for the suites I need. Let me also find the missing X-VLA L2norm data for Object at k=0.9 and k=0.95.

Looking at the data collected so far, let me now organize what I have for the main results table:

**X-VLA baselines:**
- Object: Not explicitly in registry. The `eval_xvla_prune_k095_seed42` (99.0%) seems to be L2norm on Object. 

I need to figure out what the baseline should be — the paper mentions around 98.4% for Goal, 93.0% for Spatial, and 94.0% for Long. Looking at the registry more carefully, the `eval_xvla_prune_` entries without suite specification might be Object suite, but I'm not sure what the k=1.0 (no pruning) baseline is. The naming pattern `eval_xvla_prune_k09_seed42` suggests this is early L2norm data, but I need to search more systematically to find the complete baseline.

Looking at the pruning experiments, k=0.9 gives 99.2% and k=0.95 gives 99.0%, which likely correspond to Object suite based on the pattern of later labeled experiments. Since there's no k=1.0 entry in the registry and the pruning entries range from k=0.01 to k=0.95, the baseline was probably computed separately. I should check the project files or report for the X-VLA Object baseline directly.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "790dcd4a-6607-4659-a5a3-a960215f6b9a",
  "uuid": "398ac2f9-16f3-4add-98fe-21440b86c7fb",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JgusUjT5PNQpGiS6PVtTP8",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1949,
      "cache_read_input_tokens": 48233,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1949
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

_source line 60_

<details open><summary>🔧 Tool call — Bash · `toolu_017kXiE5AVsTXrwjUCG46kfy`</summary>

```json
{
  "command": "grep -i \"x-vla\\|xvla\" /home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/ideas.md 2>/dev/null | head -30",
  "description": "Search ideas.md for X-VLA baseline"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "790dcd4a-6607-4659-a5a3-a960215f6b9a",
  "uuid": "d2aedc2b-a6f3-4e3e-bf68-41e08a8b92e4",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JgusUjT5PNQpGiS6PVtTP8",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1949,
      "cache_read_input_tokens": 48233,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1949
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

_source line 61 · 2026-05-26T07:50:04.735Z_

<details><summary>↩ Tool result · `toolu_017kXiE5AVsTXrwjUCG46kfy`</summary>

```text
(Bash completed with no output)
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "790dcd4a-6607-4659-a5a3-a960215f6b9a",
  "uuid": "d9631bd3-84b4-4fa4-b9ab-3078e0e79402",
  "tool_use_result": {
    "stdout": "",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  }
}
```

</details>

---


### Tool call

_source line 62_

<details open><summary>🔧 Tool call — Bash · `toolu_014Ng6oa1u9JLE5187v2Lvhz`</summary>

```json
{
  "command": "cat /home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-be-idea-gen-0515-2-projects-importance-margin-vla-compress/790dcd4a-6607-4659-a5a3-a960215f6b9a/tool-results/mcp-agent-ml-research-read_registry-1779781647884.txt | python3 -c \"\nimport json, sys\ndata = json.loads(json.loads(sys.stdin.read())['result'])\nexps = data['data']['experiments']\n# Search for xvla_baseline_object or any baseline experiment for xvla object\nfor name, exp in exps.items():\n    if 'xvla' in name.lower() and 'object' in name.lower() and exp.get('conclusion') == 'success':\n        sr = exp.get('metrics', {}).get('success_rate', exp.get('metrics', {}).get('overall_SR', exp.get('metrics', {}).get('SR', 'N/A')))\n        print(f'{name}: SR={sr}')\n\n# Also find pi05 baseline goal\nprint()\nprint('--- pi05 baseline goal ---')\nfor name, exp in exps.items():\n    if 'pi05' in name.lower() and 'baseline' in name.lower() and 'goal' in name.lower():\n        sr = exp.get('metrics', {}).get('success_rate', 'N/A')\n        print(f'{name}: SR={sr}')\n\n# OpenVLA baselines\nprint()\nprint('--- OpenVLA baselines ---')\nfor name, exp in exps.items():\n    if 'openvla' in name.lower() and 'baseline' in name.lower():\n        sr = exp.get('metrics', {}).get('success_rate', 'N/A')\n        print(f'{name}: SR={sr}, metrics={exp.get(\\\"metrics\\\", {})}')\n\" 2>&1",
  "description": "Find OpenVLA baselines and pi05 goal baseline"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "790dcd4a-6607-4659-a5a3-a960215f6b9a",
  "uuid": "b321c93c-a02f-457b-a337-09a49b133d3c",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JgusUjT5PNQpGiS6PVtTP8",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1949,
      "cache_read_input_tokens": 48233,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1949
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

_source line 63 · 2026-05-26T07:50:12.495Z_

<details><summary>↩ Tool result · `toolu_014Ng6oa1u9JLE5187v2Lvhz`</summary>

```text
eval_xvla_random_k085_object_seed42: SR=0.65
eval_xvla_random_k05_object_seed42: SR=70.6
eval_xvla_l2norm_k05_object_seed42: SR=0.434
eval_xvla_random_k05_object_seed43: SR=0.71
eval_xvla_random_k095_object_seed42_v2: SR=0.988
eval_xvla_l2norm_k03_object_seed44: SR=N/A
eval_xvla_random_k07_object_seed42_v2: SR=65.2
eval_xvla_random_k085_object_seed43: SR=63.2
eval_xvla_random_k085_object_seed42_v2: SR=63.6
eval_xvla_l2norm_k03_object_seed43: SR=0.21
eval_xvla_random_k03_object_seed43: SR=0.662
eval_xvla_random_k07_object_seed44: SR=0.65
eval_xvla_l2norm_k07_object_seed43: SR=0.59
eval_xvla_random_k03_object_seed44: SR=0.63
eval_xvla_l2norm_k07_object_seed44: SR=0.564
eval_xvla_l2norm_k03_object_seed42: SR=0.222
eval_xvla_random_k05_object_seed44: SR=0.692
eval_xvla_l2norm_k07_object_seed42_v2: SR=0.582
eval_xvla_random_k07_object_seed43_v2: SR=0.65
eval_xvla_random_k03_object_seed42: SR=62.8
eval_xvla_random_k07_object_seed42: SR=65.2
eval_xvla_random_k08_object_seed42: SR=89.4
eval_xvla_random_k09_object_seed42: SR=97.8

--- pi05 baseline goal ---
eval_pi05_baseline_goal_seed42: SR=N/A

--- OpenVLA baselines ---
eval_openvla_baseline_goal_seed43: SR=N/A, metrics={'overall_sr': 0.776, 'total_successes': 388, 'total_episodes': 500, 'elapsed_minutes': 193, 'seed': 43, 'per_task_sr': {'T1_open_middle_drawer': 0.58, 'T2_put_bowl_on_stove': 0.96, 'T3_put_wine_bottle_on_cabinet': 0.82, 'T4_open_top_drawer_put_bowl': 0.58, 'T5_put_bowl_on_cabinet': 0.98, 'T6_push_plate_front_stove': 0.8, 'T7_put_cream_cheese_in_bowl': 0.66, 'T8_turn_on_stove': 0.98, 'T9_put_bowl_on_plate': 0.86, 'T10_put_wine_bottle_on_rack': 0.54}}
eval_openvla_baseline_object_seed42_v2: SR=N/A, metrics={'overall_sr': 0.74, 'total_episodes': 500}
eval_openvla_baseline_spatial: SR=0.8, metrics={'elapsed_minutes': 209.9, 'model': 'openvla-7b-finetuned-libero-spatial', 'seed': 42, 'success_rate': 0.8, 'suite': 'libero_spatial', 'total_episodes': 500, 'total_successes': 400}
eval_openvla_simplerenv_baseline: SR=N/A, metrics={'PutCarrotOnPlate_SR': 0, 'PutEggplantInBasket_SR': 0, 'PutSpoonOnTableCloth_SR': 0, 'StackGreenCubeOnYellowCube_SR': 0, 'avg_SR': 0, 'episodes_per_task': 50}
eval_openvla_baseline_long_seed42: SR=N/A, metrics={'overall_sr': 0.528, 'task_sr': {'task01_alphabet_soup_tomato_sauce_basket': 0.62, 'task02_cream_cheese_butter_basket': 0.7, 'task03_stove_moka_pot': 0.5, 'task04_black_bowl_drawer': 0.48, 'task05_white_mug_left_yellow_mug_right': 0.4, 'task06_book_caddy': 0.7, 'task07_white_mug_plate_chocolate_pudding': 0.5, 'task08_alphabet_soup_cream_cheese_basket': 0.6, 'task09_both_moka_pots_stove': 0.24, 'task10_yellow_white_mug_microwave': 0.54}, 'time_min': 483.3, 'total_episodes': 500, 'total_success': 264}
eval_openvla_baseline_goal_seed42_v3: SR=74.8, metrics={'elapsed_min': 242.4, 'source': 'SSH log harvest by diagnostic worker', 'success_rate': 74.8, 'total_episodes': 500, 'total_successes': 374}
eval_openvla_baseline_spatial_seed42: SR=N/A, metrics={}
eval_openvla_baseline_spatial_seed42_v3: SR=N/A, metrics={}
eval_openvla_baseline_object_seed42: SR=74, metrics={'num_episodes': 500, 'source': 'log extraction - full eval completed but results/ dir missing caused save failure', 'success_rate': 74}
eval_openvla_baseline_spatial_seed42_v2: SR=N/A, metrics={}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "790dcd4a-6607-4659-a5a3-a960215f6b9a",
  "uuid": "37a8d389-131e-4be3-b99a-c73ba5d17473",
  "tool_use_result": {
    "stdout": "eval_xvla_random_k085_object_seed42: SR=0.65\neval_xvla_random_k05_object_seed42: SR=70.6\neval_xvla_l2norm_k05_object_seed42: SR=0.434\neval_xvla_random_k05_object_seed43: SR=0.71\neval_xvla_random_k095_object_seed42_v2: SR=0.988\neval_xvla_l2norm_k03_object_seed44: SR=N/A\neval_xvla_random_k07_object_seed42_v2: SR=65.2\neval_xvla_random_k085_object_seed43: SR=63.2\neval_xvla_random_k085_object_seed42_v2: SR=63.6\neval_xvla_l2norm_k03_object_seed43: SR=0.21\neval_xvla_random_k03_object_seed43: SR=0.662\neval_xvla_random_k07_object_seed44: SR=0.65\neval_xvla_l2norm_k07_object_seed43: SR=0.59\neval_xvla_random_k03_object_seed44: SR=0.63\neval_xvla_l2norm_k07_object_seed44: SR=0.564\neval_xvla_l2norm_k03_object_seed42: SR=0.222\neval_xvla_random_k05_object_seed44: SR=0.692\neval_xvla_l2norm_k07_object_seed42_v2: SR=0.582\neval_xvla_random_k07_object_seed43_v2: SR=0.65\neval_xvla_random_k03_object_seed42: SR=62.8\neval_xvla_random_k07_object_seed42: SR=65.2\neval_xvla_random_k08_object_seed42: SR=89.4\neval_xvla_random_k09_object_seed42: SR=97.8\n\n--- pi05 baseline goal ---\neval_pi05_baseline_goal_seed42: SR=N/A\n\n--- OpenVLA baselines ---\neval_openvla_baseline_goal_seed43: SR=N/A, metrics={'overall_sr': 0.776, 'total_successes': 388, 'total_episodes': 500, 'elapsed_minutes': 193, 'seed': 43, 'per_task_sr': {'T1_open_middle_drawer': 0.58, 'T2_put_bowl_on_stove': 0.96, 'T3_put_wine_bottle_on_cabinet': 0.82, 'T4_open_top_drawer_put_bowl': 0.58, 'T5_put_bowl_on_cabinet': 0.98, 'T6_push_plate_front_stove': 0.8, 'T7_put_cream_cheese_in_bowl': 0.66, 'T8_turn_on_stove': 0.98, 'T9_put_bowl_on_plate': 0.86, 'T10_put_wine_bottle_on_rack': 0.54}}\neval_openvla_baseline_object_seed42_v2: SR=N/A, metrics={'overall_sr': 0.74, 'total_episodes': 500}\neval_openvla_baseline_spatial: SR=0.8, metrics={'elapsed_minutes': 209.9, 'model': 'openvla-7b-finetuned-libero-spatial', 'seed': 42, 'success_rate': 0.8, 'suite': 'libero_spatial', 'total_episodes': 500, 'total_successes': 400}\neval_openvla_simplerenv_baseline: SR=N/A, metrics={'PutCarrotOnPlate_SR': 0, 'PutEggplantInBasket_SR': 0, 'PutSpoonOnTableCloth_SR': 0, 'StackGreenCubeOnYellowCube_SR': 0, 'avg_SR': 0, 'episodes_per_task': 50}\neval_openvla_baseline_long_seed42: SR=N/A, metrics={'overall_sr': 0.528, 'task_sr': {'task01_alphabet_soup_tomato_sauce_basket': 0.62, 'task02_cream_cheese_butter_basket': 0.7, 'task03_stove_moka_pot': 0.5, 'task04_black_bowl_drawer': 0.48, 'task05_white_mug_left_yellow_mug_right': 0.4, 'task06_book_caddy': 0.7, 'task07_white_mug_plate_chocolate_pudding': 0.5, 'task08_alphabet_soup_cream_cheese_basket': 0.6, 'task09_both_moka_pots_stove': 0.24, 'task10_yellow_white_mug_microwave': 0.54}, 'time_min': 483.3, 'total_episodes': 500, 'total_success': 264}\neval_openvla_baseline_goal_seed42_v3: SR=74.8, metrics={'elapsed_min': 242.4, 'source': 'SSH log harvest by diagnostic worker', 'success_rate': 74.8, 'total_episodes': 500, 'total_successes': 374}\neval_openvla_baseline_spatial_seed42: SR=N/A, metrics={}\neval_openvla_baseline_spatial_seed42_v3: SR=N/A, metrics={}\neval_openvla_baseline_object_seed42: SR=74, metrics={'num_episodes': 500, 'source': 'log extraction - full eval completed but results/ dir missing caused save failure', 'success_rate': 74}\neval_openvla_baseline_spatial_seed42_v2: SR=N/A, metrics={}",
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

_source line 64_

<details><summary>Logged reasoning block</summary>

```text
Now let me compile everything I need. Let me also find the pi05 baseline goal and the OpenVLA pruning results.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "790dcd4a-6607-4659-a5a3-a960215f6b9a",
  "uuid": "776e3c93-7169-40ef-94f1-9c99aac71c8d",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MNbbDzUNQFrvpkmbS4zgXf",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2892,
      "cache_read_input_tokens": 50182,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2892
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

_source line 65_

<details open><summary>🔧 Tool call — Bash · `toolu_01VJL58y1Jqeax3tjNZtrTmd`</summary>

```json
{
  "command": "cat /home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-be-idea-gen-0515-2-projects-importance-margin-vla-compress/790dcd4a-6607-4659-a5a3-a960215f6b9a/tool-results/mcp-agent-ml-research-read_registry-1779781647884.txt | python3 -c \"\nimport json, sys\ndata = json.loads(json.loads(sys.stdin.read())['result'])\nexps = data['data']['experiments']\n\n# pi05 baseline goal\nprint('--- pi05 baseline goal ---')\nfor name, exp in exps.items():\n    if 'pi05' in name.lower() and 'baseline' in name.lower():\n        m = exp.get('metrics', {})\n        sr = m.get('success_rate', m.get('overall_sr', m.get('overall_SR', 'N/A')))\n        print(f'{name}: SR={sr}, metrics={m}')\n\nprint()\nprint('--- OpenVLA pruning experiments ---')\nfor name, exp in exps.items():\n    if 'openvla' in name.lower() and ('l2norm' in name.lower() or 'random' in name.lower() or 'attn' in name.lower()) and exp.get('conclusion') not in ['killed', 'failed']:\n        m = exp.get('metrics', {})\n        sr = m.get('success_rate', m.get('overall_sr', m.get('overall_SR', 'N/A')))\n        if sr != 'N/A':\n            print(f'{name}: SR={sr}')\n\" 2>&1",
  "description": "Find pi05 and OpenVLA pruning data"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "790dcd4a-6607-4659-a5a3-a960215f6b9a",
  "uuid": "1f4c181f-c7ac-46f6-934c-33a522207c43",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MNbbDzUNQFrvpkmbS4zgXf",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2892,
      "cache_read_input_tokens": 50182,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2892
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

_source line 66 · 2026-05-26T07:50:23.116Z_

<details><summary>↩ Tool result · `toolu_01VJL58y1Jqeax3tjNZtrTmd`</summary>

```text
--- pi05 baseline goal ---
pi05_baseline_long_seed42: SR=92.8, metrics={'overall_sr': 92.8, 'total_episodes': 500}
eval_pi05_baseline_spatial_seed42: SR=97.2, metrics={'overall_sr': 97.2, 'total_episodes': 500}
eval_pi05_baseline_long_seed42: SR=92.8, metrics={'note': 'Result from westd-38929 run (2026-05-22). Original cqa1-33015 run was stale. Second cqa1-33015 run=91.6%.', 'overall_sr': 92.8, 'per_task': {'alphabet_soup_cream_cheese_basket': 0.9, 'alphabet_soup_tomato_basket': 0.96, 'book_in_caddy': 0.98, 'bowl_bottom_drawer': 1, 'cream_cheese_butter_basket': 0.96, 'moka_pots_stove': 0.64, 'mug_microwave': 0.98, 'mug_plate_chocolate': 0.88, 'mugs_on_plates': 1, 'stove_moka_pot': 0.98}, 'source_file': 'westd-38929:/root/autodl-tmp/importance_margin_vla_compress/eval_results/pi05_baseline_libero_10_seed42.json', 'total_episodes': 500, 'total_successes': 464}
eval_pi05_baseline_object_seed42: SR=98.2, metrics={'overall_sr': 98.2, 'per_task': {'alphabet_soup': 0.96, 'bbq_sauce': 1, 'butter': 1, 'chocolate_pudding': 1, 'cream_cheese': 0.98, 'ketchup': 0.94, 'milk': 0.98, 'orange_juice': 0.98, 'salad_dressing': 0.98, 'tomato_sauce': 1}, 'source_file': 'westd-41074:/root/autodl-tmp/importance_margin_vla_compress/eval_results/pi05_baseline_libero_object.json', 'total_episodes': 500, 'total_successes': 491}
eval_pi05_baseline_goal_seed42: SR=0.964, metrics={'elapsed_min': 49.7, 'overall_sr': 0.964, 'per_task': {'bowl_on_cabinet': 1, 'bowl_on_plate': 1, 'bowl_on_stove': 1, 'cream_cheese_in_bowl': 0.96, 'open_middle_drawer': 0.9, 'open_top_drawer_bowl_inside': 0.9, 'push_plate_front_stove': 1, 'turn_on_stove': 1, 'wine_bottle_on_cabinet': 0.98, 'wine_bottle_on_rack': 0.9}, 'total_episodes': 500, 'total_successes': 482}

--- OpenVLA pruning experiments ---
eval_openvla_attn_k085_object_seed42: SR=0.55
eval_openvla_attn_k07_long_seed42_v2: SR=24
eval_openvla_l2norm_k07_long_seed42_v2: SR=0.312
eval_openvla_l2norm_k085_long_seed42_v2: SR=0.388
eval_openvla_random_k07_long_seed42_v2: SR=0.388
eval_openvla_random_k07_object_seed42_v2: SR=0.444
eval_openvla_zeromask_l2norm_k09_object_seed42: SR=0.688
eval_openvla_zeromask_random_k09_object_seed42: SR=0.718
eval_openvla_random_k05_spatial_seed42: SR=0.5
eval_openvla_random_k05_goal_seed42: SR=0.522
eval_openvla_l2norm_k05_goal_seed42: SR=0.434
eval_openvla_l2norm_k09_long_seed42_v3: SR=43.6
eval_openvla_attn_k09_long_seed42_v3: SR=44.0
eval_openvla_random_k09_long_seed42_v3: SR=46.8
eval_openvla_l2norm_k05_object_seed42_v4: SR=0.392
eval_openvla_random_k09_spatial_seed42: SR=79.8
eval_openvla_random_k09_goal_seed42: SR=79.6
eval_openvla_l2norm_k09_spatial_seed42: SR=0.75
eval_openvla_l2norm_k09_goal_seed42: SR=0.748
eval_openvla_attn_k09_goal_seed42: SR=0.732
eval_openvla_attn_k09_spatial_seed42: SR=0.804
eval_openvla_l2norm_k05_goal_seed42_v3: SR=0.434
eval_openvla_l2norm_k05_object_seed42_v5: SR=0.392
eval_openvla_l2norm_k09_object_seed42: SR=0.706
eval_openvla_l2norm_k05_object_seed43: SR=39.2
eval_openvla_l2norm_k03_object_seed43: SR=25
eval_openvla_random_k07_object_seed43: SR=0.526
eval_openvla_random_k03_object_seed42_v2: SR=0.214
eval_openvla_l2norm_k07_object_seed42_v2: SR=0.498
eval_openvla_l2norm_k03_object_seed42: SR=25.0
eval_openvla_l2norm_k05_object_seed42: SR=39.2
eval_openvla_prune_random_k05_seed42: SR=35.8
eval_openvla_prune_random_k07_seed42_v2: SR=44.4
eval_openvla_prune_random_k095_seed42_v2: SR=69.2
eval_openvla_prune_l2norm_k07_seed43_v2: SR=49.8
eval_openvla_prune_random_k095_seed43: SR=0.668
eval_openvla_prune_random_k09_seed42: SR=0.646
eval_openvla_prune_random_k09_seed43: SR=0.622
eval_openvla_prune_random_k05_seed43_v2: SR=0.356
eval_openvla_prune_l2norm_k09: SR=0.706
eval_openvla_prune_random_k07_seed43_v2: SR=0.526
eval_openvla_prune_l2norm_k095: SR=0.706
eval_openvla_prune_l2norm_k03: SR=0.25
eval_openvla_prune_l2norm_k05: SR=0.392
eval_openvla_prune_l2norm_k03_seed42: SR=0.25
eval_openvla_prune_l2norm_k05_seed42: SR=0.392
eval_openvla_prune_l2norm_k095_seed42: SR=0.706
eval_openvla_prune_l2norm_k09_seed42: SR=0.706
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "790dcd4a-6607-4659-a5a3-a960215f6b9a",
  "uuid": "b9ed2234-e268-47af-a603-c49b38cf4b69",
  "tool_use_result": {
    "stdout": "--- pi05 baseline goal ---\npi05_baseline_long_seed42: SR=92.8, metrics={'overall_sr': 92.8, 'total_episodes': 500}\neval_pi05_baseline_spatial_seed42: SR=97.2, metrics={'overall_sr': 97.2, 'total_episodes': 500}\neval_pi05_baseline_long_seed42: SR=92.8, metrics={'note': 'Result from westd-38929 run (2026-05-22). Original cqa1-33015 run was stale. Second cqa1-33015 run=91.6%.', 'overall_sr': 92.8, 'per_task': {'alphabet_soup_cream_cheese_basket': 0.9, 'alphabet_soup_tomato_basket': 0.96, 'book_in_caddy': 0.98, 'bowl_bottom_drawer': 1, 'cream_cheese_butter_basket': 0.96, 'moka_pots_stove': 0.64, 'mug_microwave': 0.98, 'mug_plate_chocolate': 0.88, 'mugs_on_plates': 1, 'stove_moka_pot': 0.98}, 'source_file': 'westd-38929:/root/autodl-tmp/importance_margin_vla_compress/eval_results/pi05_baseline_libero_10_seed42.json', 'total_episodes': 500, 'total_successes': 464}\neval_pi05_baseline_object_seed42: SR=98.2, metrics={'overall_sr': 98.2, 'per_task': {'alphabet_soup': 0.96, 'bbq_sauce': 1, 'butter': 1, 'chocolate_pudding': 1, 'cream_cheese': 0.98, 'ketchup': 0.94, 'milk': 0.98, 'orange_juice': 0.98, 'salad_dressing': 0.98, 'tomato_sauce': 1}, 'source_file': 'westd-41074:/root/autodl-tmp/importance_margin_vla_compress/eval_results/pi05_baseline_libero_object.json', 'total_episodes': 500, 'total_successes': 491}\neval_pi05_baseline_goal_seed42: SR=0.964, metrics={'elapsed_min': 49.7, 'overall_sr': 0.964, 'per_task': {'bowl_on_cabinet': 1, 'bowl_on_plate': 1, 'bowl_on_stove': 1, 'cream_cheese_in_bowl': 0.96, 'open_middle_drawer': 0.9, 'open_top_drawer_bowl_inside': 0.9, 'push_plate_front_stove': 1, 'turn_on_stove': 1, 'wine_bottle_on_cabinet': 0.98, 'wine_bottle_on_rack': 0.9}, 'total_episodes': 500, 'total_successes': 482}\n\n--- OpenVLA pruning experiments ---\neval_openvla_attn_k085_object_seed42: SR=0.55\neval_openvla_attn_k07_long_seed42_v2: SR=24\neval_openvla_l2norm_k07_long_seed42_v2: SR=0.312\neval_openvla_l2norm_k085_long_seed42_v2: SR=0.388\neval_openvla_random_k07_long_seed42_v2: SR=0.388\neval_openvla_random_k07_object_seed42_v2: SR=0.444\neval_openvla_zeromask_l2norm_k09_object_seed42: SR=0.688\neval_openvla_zeromask_random_k09_object_seed42: SR=0.718\neval_openvla_random_k05_spatial_seed42: SR=0.5\neval_openvla_random_k05_goal_seed42: SR=0.522\neval_openvla_l2norm_k05_goal_seed42: SR=0.434\neval_openvla_l2norm_k09_long_seed42_v3: SR=43.6\neval_openvla_attn_k09_long_seed42_v3: SR=44.0\neval_openvla_random_k09_long_seed42_v3: SR=46.8\neval_openvla_l2norm_k05_object_seed42_v4: SR=0.392\neval_openvla_random_k09_spatial_seed42: SR=79.8\neval_openvla_random_k09_goal_seed42: SR=79.6\neval_openvla_l2norm_k09_spatial_seed42: SR=0.75\neval_openvla_l2norm_k09_goal_seed42: SR=0.748\neval_openvla_attn_k09_goal_seed42: SR=0.732\neval_openvla_attn_k09_spatial_seed42: SR=0.804\neval_openvla_l2norm_k05_goal_seed42_v3: SR=0.434\neval_openvla_l2norm_k05_object_seed42_v5: SR=0.392\neval_openvla_l2norm_k09_object_seed42: SR=0.706\neval_openvla_l2norm_k05_object_seed43: SR=39.2\neval_openvla_l2norm_k03_object_seed43: SR=25\neval_openvla_random_k07_object_seed43: SR=0.526\neval_openvla_random_k03_object_seed42_v2: SR=0.214\neval_openvla_l2norm_k07_object_seed42_v2: SR=0.498\neval_openvla_l2norm_k03_object_seed42: SR=25.0\neval_openvla_l2norm_k05_object_seed42: SR=39.2\neval_openvla_prune_random_k05_seed42: SR=35.8\neval_openvla_prune_random_k07_seed42_v2: SR=44.4\neval_openvla_prune_random_k095_seed42_v2: SR=69.2\neval_openvla_prune_l2norm_k07_seed43_v2: SR=49.8\neval_openvla_prune_random_k095_seed43: SR=0.668\neval_openvla_prune_random_k09_seed42: SR=0.646\neval_openvla_prune_random_k09_seed43: SR=0.622\neval_openvla_prune_random_k05_seed43_v2: SR=0.356\neval_openvla_prune_l2norm_k09: SR=0.706\neval_openvla_prune_random_k07_seed43_v2: SR=0.526\neval_openvla_prune_l2norm_k095: SR=0.706\neval_openvla_prune_l2norm_k03: SR=0.25\neval_openvla_prune_l2norm_k05: SR=0.392\neval_openvla_prune_l2norm_k03_seed42: SR=0.25\neval_openvla_prune_l2norm_k05_seed42: SR=0.392\neval_openvla_prune_l2norm_k095_seed42: SR=0.706\neval_openvla_prune_l2norm_k09_seed42: SR=0.706",
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

_source line 67_

<details><summary>Logged reasoning block</summary>

```text
Now I have enough data. Let me also find OpenVLA k=0.95 for random Object, and other data points I need.

Let me also check for the SmolVLA experiments and OpenVLA k=0.5 for random Object.

Let me also look for OpenVLA random k=0.5 object and k=0.9 object.

From the data I have:

**OpenVLA (Object, baseline=74%):**
- L2norm k=0.95: 70.6% (from eval_openvla_prune_l2norm_k095)


- L2norm k=0.9: 70.6% (from eval_openvla_l2norm_k09_object_seed42)
- L2norm k=0.7: 49.8% (from eval_openvla_l2norm_k07_object_seed42_v2)
- L2norm k=0.5: 39.2% (from eval_openvla_l2norm_k05_object_seed42)
- Random k=0.95: 69.2% (from eval_openvla_prune_random_k095_seed42_v2)
- Random k=0.9: 64.6% (from eval_openvla_prune_random_k09_object_seed42)

I'm noticing some discrepancies between what the task prompt lists and what I'm finding in the registry. The prompt shows Random k=0.9 at 62.8%, but the registry entry shows 64.6%. I also see there's a zeromask variant at 71.8% that's different from the regular pruning approach, so I need to make sure I'm comparing the right methods.

Let me stick with the data points explicitly provided in the task prompt as the source of truth, and fill in any gaps with registry results. I should also check what SmolVLA results are available.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "790dcd4a-6607-4659-a5a3-a960215f6b9a",
  "uuid": "833db004-cb6b-4bb5-b83a-7b019e5e9e48",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UjWZFNEGtwb35giZddgk8z",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2517,
      "cache_read_input_tokens": 53074,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2517
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

_source line 68_

<details open><summary>🔧 Tool call — Bash · `toolu_01L3ErEhVc1R8cVcFt3Uy31a`</summary>

```json
{
  "command": "cat /home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-be-idea-gen-0515-2-projects-importance-margin-vla-compress/790dcd4a-6607-4659-a5a3-a960215f6b9a/tool-results/mcp-agent-ml-research-read_registry-1779781647884.txt | python3 -c \"\nimport json, sys\ndata = json.loads(json.loads(sys.stdin.read())['result'])\nexps = data['data']['experiments']\n\n# SmolVLA experiments\nprint('--- SmolVLA ---')\nfor name, exp in exps.items():\n    if 'smolvla' in name.lower() and exp.get('conclusion') not in ['killed', 'failed']:\n        m = exp.get('metrics', {})\n        sr = m.get('success_rate', m.get('overall_sr', m.get('overall_SR', 'N/A')))\n        if sr != 'N/A':\n            print(f'{name}: SR={sr}')\n\n# OpenVLA random k=0.9 object seed42\nprint()\nprint('--- OpenVLA random k=0.9 object ---')\nfor name, exp in exps.items():\n    if 'openvla' in name.lower() and 'random' in name.lower() and 'k09' in name and ('object' in name.lower() or 'obj' in name.lower()):\n        m = exp.get('metrics', {})\n        sr = m.get('success_rate', m.get('overall_sr', m.get('overall_SR', 'N/A')))\n        print(f'{name}: SR={sr}')\n\n# OpenVLA random k=0.5 object\nprint()\nprint('--- OpenVLA random k=0.5 object ---')\nfor name, exp in exps.items():\n    if 'openvla' in name.lower() and 'random' in name.lower() and 'k05' in name and ('object' in name.lower() or 'obj' in name.lower()):\n        m = exp.get('metrics', {})\n        sr = m.get('success_rate', m.get('overall_sr', m.get('overall_SR', 'N/A')))\n        print(f'{name}: SR={sr}')\n\n# OpenVLA l2norm k=0.95 and k=0.7 object\nprint()\nprint('--- OpenVLA L2norm k=0.95 and k=0.7 object ---')\nfor name, exp in exps.items():\n    if 'openvla' in name.lower() and 'l2norm' in name.lower() and ('k095' in name or 'k07' in name) and ('object' in name.lower() or 'obj' in name.lower()):\n        m = exp.get('metrics', {})\n        sr = m.get('success_rate', m.get('overall_sr', m.get('overall_SR', 'N/A')))\n        print(f'{name}: SR={sr}')\n\n# OpenVLA random k=0.95 object\nprint()\nprint('--- OpenVLA random k=0.95 object ---')\nfor name, exp in exps.items():\n    if 'openvla' in name.lower() and 'random' in name.lower() and 'k095' in name and ('object' in name.lower() or 'obj' in name.lower()):\n        m = exp.get('metrics', {})\n        sr = m.get('success_rate', m.get('overall_sr', m.get('overall_SR', 'N/A')))\n        print(f'{name}: SR={sr}')\n\" 2>&1",
  "description": "Find SmolVLA and OpenVLA detailed data"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "790dcd4a-6607-4659-a5a3-a960215f6b9a",
  "uuid": "70c31bfc-f7e1-4616-9512-7619b8aec87e",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UjWZFNEGtwb35giZddgk8z",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2517,
      "cache_read_input_tokens": 53074,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2517
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

_source line 69 · 2026-05-26T07:50:48.452Z_

<details><summary>↩ Tool result · `toolu_01L3ErEhVc1R8cVcFt3Uy31a`</summary>

```text
--- SmolVLA ---
eval_smolvla_metaworld_baseline: SR=26.4
smolvla_random_k095_long_seed42: SR=0
smolvla_l2norm_k095_long_seed42: SR=0
smolvla_random_k095_goal_seed42: SR=0.042
smolvla_l2norm_k095_goal_seed42: SR=0.034
smolvla_random_k095_spatial_seed42: SR=0.042
smolvla_l2norm_k095_spatial_seed42: SR=0.066
smolvla_baseline_long_seed42: SR=0.366
smolvla_official_goal_baseline_s42: SR=0.608
smolvla_official_object_l2norm_k095_s42: SR=0.002
smolvla_official_spatial_baseline_s42: SR=0.446
eval_smolvla_zeromask_l2norm_k095_object_seed42: SR=0
eval_smolvla_zeromask_random_k095_object_seed42: SR=0.002
eval_smolvla_official_random_k050_object_seed42: SR=0
eval_smolvla_official_random_k090_object_seed42: SR=0
eval_smolvla_official_l2norm_k030_object_seed42: SR=0
eval_smolvla_official_random_k070_object_seed42: SR=0
eval_smolvla_official_random_k030_object_seed42: SR=0
eval_smolvla_official_l2norm_k050_object_seed42: SR=0
eval_smolvla_official_l2norm_k095_object_seed42: SR=0.4
eval_smolvla_official_random_k095_object_seed42: SR=0
eval_smolvla_official_baseline_object_seed42: SR=57.2
eval_smolvla_baseline_spatial_westd38929_seed42: SR=8.0
eval_official_smolvla_prune_k095: SR=0
eval_official_smolvla_prune_k09: SR=0
eval_official_smolvla_prune_k05_v2: SR=0
eval_official_smolvla_baseline: SR=59.2
eval_smolvla_random_prune_k095: SR=0

--- OpenVLA random k=0.9 object ---
eval_openvla_zeromask_random_k09_object_seed42: SR=0.718
eval_openvla_random_k09_object_seed42: SR=N/A

--- OpenVLA random k=0.5 object ---
eval_openvla_random_k05_object_seed42_v2: SR=N/A
eval_openvla_random_k05_object_seed42: SR=N/A

--- OpenVLA L2norm k=0.95 and k=0.7 object ---
eval_openvla_l2norm_k07_object_seed42_v2: SR=0.498

--- OpenVLA random k=0.95 object ---
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "790dcd4a-6607-4659-a5a3-a960215f6b9a",
  "uuid": "77a1e43e-452e-4219-a104-649388df0e93",
  "tool_use_result": {
    "stdout": "--- SmolVLA ---\neval_smolvla_metaworld_baseline: SR=26.4\nsmolvla_random_k095_long_seed42: SR=0\nsmolvla_l2norm_k095_long_seed42: SR=0\nsmolvla_random_k095_goal_seed42: SR=0.042\nsmolvla_l2norm_k095_goal_seed42: SR=0.034\nsmolvla_random_k095_spatial_seed42: SR=0.042\nsmolvla_l2norm_k095_spatial_seed42: SR=0.066\nsmolvla_baseline_long_seed42: SR=0.366\nsmolvla_official_goal_baseline_s42: SR=0.608\nsmolvla_official_object_l2norm_k095_s42: SR=0.002\nsmolvla_official_spatial_baseline_s42: SR=0.446\neval_smolvla_zeromask_l2norm_k095_object_seed42: SR=0\neval_smolvla_zeromask_random_k095_object_seed42: SR=0.002\neval_smolvla_official_random_k050_object_seed42: SR=0\neval_smolvla_official_random_k090_object_seed42: SR=0\neval_smolvla_official_l2norm_k030_object_seed42: SR=0\neval_smolvla_official_random_k070_object_seed42: SR=0\neval_smolvla_official_random_k030_object_seed42: SR=0\neval_smolvla_official_l2norm_k050_object_seed42: SR=0\neval_smolvla_official_l2norm_k095_object_seed42: SR=0.4\neval_smolvla_official_random_k095_object_seed42: SR=0\neval_smolvla_official_baseline_object_seed42: SR=57.2\neval_smolvla_baseline_spatial_westd38929_seed42: SR=8.0\neval_official_smolvla_prune_k095: SR=0\neval_official_smolvla_prune_k09: SR=0\neval_official_smolvla_prune_k05_v2: SR=0\neval_official_smolvla_baseline: SR=59.2\neval_smolvla_random_prune_k095: SR=0\n\n--- OpenVLA random k=0.9 object ---\neval_openvla_zeromask_random_k09_object_seed42: SR=0.718\neval_openvla_random_k09_object_seed42: SR=N/A\n\n--- OpenVLA random k=0.5 object ---\neval_openvla_random_k05_object_seed42_v2: SR=N/A\neval_openvla_random_k05_object_seed42: SR=N/A\n\n--- OpenVLA L2norm k=0.95 and k=0.7 object ---\neval_openvla_l2norm_k07_object_seed42_v2: SR=0.498\n\n--- OpenVLA random k=0.95 object ---",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  }
}
```

</details>

---


### Tool call

_source line 70_

<details open><summary>🔧 Tool call — Bash · `toolu_01G9SE4zhiWioGfuzFw37ztF`</summary>

```json
{
  "command": "cat /home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-be-idea-gen-0515-2-projects-importance-margin-vla-compress/790dcd4a-6607-4659-a5a3-a960215f6b9a/tool-results/mcp-agent-ml-research-read_registry-1779781647884.txt | python3 -c \"\nimport json, sys\ndata = json.loads(json.loads(sys.stdin.read())['result'])\nexps = data['data']['experiments']\n\n# X-VLA Object L2norm k=0.9 and k=0.95\nprint('--- X-VLA L2norm k=0.9/0.95 Object ---')\nfor name, exp in exps.items():\n    if 'xvla' in name.lower() and 'l2norm' in name.lower() and ('k09' in name or 'k095' in name) and ('object' in name.lower() or 'obj' in name.lower()):\n        m = exp.get('metrics', {})\n        sr = m.get('success_rate', m.get('overall_sr', m.get('overall_SR', m.get('SR', 'N/A'))))\n        print(f'{name}: SR={sr}')\n\n# X-VLA random k=0.9 Object\nprint()\nprint('--- X-VLA random k=0.9/0.95 Object ---')\nfor name, exp in exps.items():\n    if 'xvla' in name.lower() and 'random' in name.lower() and ('k09' in name or 'k095' in name) and ('object' in name.lower() or 'obj' in name.lower()):\n        m = exp.get('metrics', {})\n        sr = m.get('success_rate', m.get('overall_sr', m.get('overall_SR', m.get('SR', 'N/A'))))\n        print(f'{name}: SR={sr}')\n\n# X-VLA L2norm k=0.7 Object\nprint()\nprint('--- X-VLA L2norm k=0.7 Object ---')\nfor name, exp in exps.items():\n    if 'xvla' in name.lower() and 'l2norm' in name.lower() and 'k07' in name and ('object' in name.lower() or 'obj' in name.lower()):\n        m = exp.get('metrics', {})\n        sr = m.get('success_rate', m.get('overall_sr', m.get('overall_SR', m.get('SR', 'N/A'))))\n        print(f'{name}: SR={sr}')\n\n# X-VLA random k=0.7 Object\nprint()\nprint('--- X-VLA random k=0.7 Object ---')\nfor name, exp in exps.items():\n    if 'xvla' in name.lower() and 'random' in name.lower() and 'k07' in name and ('object' in name.lower() or 'obj' in name.lower()):\n        m = exp.get('metrics', {})\n        sr = m.get('success_rate', m.get('overall_sr', m.get('overall_SR', m.get('SR', 'N/A'))))\n        print(f'{name}: SR={sr}')\n\" 2>&1",
  "description": "Find X-VLA L2norm/Random Object at various k"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "790dcd4a-6607-4659-a5a3-a960215f6b9a",
  "uuid": "9a7f0e23-c2ba-4069-8daa-f873b18ea239",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UjWZFNEGtwb35giZddgk8z",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2517,
      "cache_read_input_tokens": 53074,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2517
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

_source line 71 · 2026-05-26T07:50:55.760Z_

<details><summary>↩ Tool result · `toolu_01G9SE4zhiWioGfuzFw37ztF`</summary>

```text
--- X-VLA L2norm k=0.9/0.95 Object ---

--- X-VLA random k=0.9/0.95 Object ---
eval_xvla_random_k095_object_seed42_v2: SR=0.988
eval_xvla_random_k09_object_seed42: SR=97.8

--- X-VLA L2norm k=0.7 Object ---
eval_xvla_l2norm_k07_object_seed43: SR=0.59
eval_xvla_l2norm_k07_object_seed44: SR=0.564
eval_xvla_l2norm_k07_object_seed42_v2: SR=0.582

--- X-VLA random k=0.7 Object ---
eval_xvla_random_k07_object_seed42_v2: SR=65.2
eval_xvla_random_k07_object_seed44: SR=0.65
eval_xvla_random_k07_object_seed43_v2: SR=0.65
eval_xvla_random_k07_object_seed43: SR=N/A
eval_xvla_random_k07_object_seed42: SR=65.2
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "790dcd4a-6607-4659-a5a3-a960215f6b9a",
  "uuid": "86ce976b-0f4e-452a-af6b-decf9ed5b7a2",
  "tool_use_result": {
    "stdout": "--- X-VLA L2norm k=0.9/0.95 Object ---\n\n--- X-VLA random k=0.9/0.95 Object ---\neval_xvla_random_k095_object_seed42_v2: SR=0.988\neval_xvla_random_k09_object_seed42: SR=97.8\n\n--- X-VLA L2norm k=0.7 Object ---\neval_xvla_l2norm_k07_object_seed43: SR=0.59\neval_xvla_l2norm_k07_object_seed44: SR=0.564\neval_xvla_l2norm_k07_object_seed42_v2: SR=0.582\n\n--- X-VLA random k=0.7 Object ---\neval_xvla_random_k07_object_seed42_v2: SR=65.2\neval_xvla_random_k07_object_seed44: SR=0.65\neval_xvla_random_k07_object_seed43_v2: SR=0.65\neval_xvla_random_k07_object_seed43: SR=N/A\neval_xvla_random_k07_object_seed42: SR=65.2",
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

_source line 72_

<details><summary>Logged reasoning block</summary>

```text
Now I need to find some missing data points. Let me also look for OpenVLA random k=0.9 object and k=0.5 object with metrics.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "790dcd4a-6607-4659-a5a3-a960215f6b9a",
  "uuid": "442997d4-0f0a-4490-b25a-1206e2383daa",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012tNfgUGsoXGNwiz2yetgTP",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3857,
      "cache_read_input_tokens": 55591,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3857
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

_source line 73_

<details open><summary>🔧 Tool call — Bash · `toolu_0136kC2o72fV2pCAMVTskcSM`</summary>

```json
{
  "command": "cat /home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-be-idea-gen-0515-2-projects-importance-margin-vla-compress/790dcd4a-6607-4659-a5a3-a960215f6b9a/tool-results/mcp-agent-ml-research-read_registry-1779781647884.txt | python3 -c \"\nimport json, sys\ndata = json.loads(json.loads(sys.stdin.read())['result'])\nexps = data['data']['experiments']\n\n# OpenVLA random k=0.9 object (with full metrics)\nprint('--- OpenVLA random k=0.9 object (full) ---')\nfor name, exp in exps.items():\n    if 'openvla' in name.lower() and 'random' in name.lower() and 'k09' in name and ('object' in name.lower() or 'obj' in name.lower()):\n        print(f'{name}: metrics={exp.get(\\\"metrics\\\", {})}')\n\n# OpenVLA random k=0.5 object (full)\nprint()\nprint('--- OpenVLA random k=0.5 object (full) ---')\nfor name, exp in exps.items():\n    if 'openvla' in name.lower() and 'random' in name.lower() and 'k05' in name and ('object' in name.lower() or 'obj' in name.lower()):\n        print(f'{name}: metrics={exp.get(\\\"metrics\\\", {})}')\n\n# OpenVLA L2norm k=0.5 goal \nprint()\nprint('--- OpenVLA L2norm k=0.5 goal ---')\nfor name, exp in exps.items():\n    if 'openvla' in name.lower() and 'l2norm' in name.lower() and 'k05' in name and 'goal' in name.lower():\n        m = exp.get('metrics', {})\n        sr = m.get('success_rate', m.get('overall_sr', 'N/A'))\n        print(f'{name}: SR={sr}')\n\n# OpenVLA random k=0.5 goal\nprint()\nprint('--- OpenVLA random k=0.5 goal ---')\nfor name, exp in exps.items():\n    if 'openvla' in name.lower() and 'random' in name.lower() and 'k05' in name and 'goal' in name.lower():\n        m = exp.get('metrics', {})\n        sr = m.get('success_rate', m.get('overall_sr', m.get('overall_SR', 'N/A')))\n        print(f'{name}: SR={sr}')\n\" 2>&1",
  "description": "Find remaining OpenVLA data points"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "790dcd4a-6607-4659-a5a3-a960215f6b9a",
  "uuid": "c222a35d-77a3-4ee9-b345-b82f94e878bf",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012tNfgUGsoXGNwiz2yetgTP",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3857,
      "cache_read_input_tokens": 55591,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3857
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

_source line 74 · 2026-05-26T07:51:12.888Z_

<details><summary>↩ Tool result · `toolu_0136kC2o72fV2pCAMVTskcSM`</summary>

```text
--- OpenVLA random k=0.9 object (full) ---
eval_openvla_zeromask_random_k09_object_seed42: metrics={'overall_sr': 0.718, 'per_task': {'alphabet_soup': 0.9, 'cream_cheese': 0.54, 'salad_dressing': 0.78, 'bbq_sauce': 0.62, 'ketchup': 0.8, 'tomato_sauce': 0.68, 'butter': 0.5, 'milk': 0.74, 'chocolate_pudding': 0.7, 'orange_juice': 0.92}, 'elapsed_minutes': 246.4}
eval_openvla_random_k09_object_seed42: metrics={'elapsed_minutes': 246.3, 'overall_success_rate': 0.628, 'total_episodes': 500, 'total_successes': 314}

--- OpenVLA random k=0.5 object (full) ---
eval_openvla_random_k05_object_seed42_v2: metrics={}
eval_openvla_random_k05_object_seed42: metrics={}

--- OpenVLA L2norm k=0.5 goal ---
eval_openvla_l2norm_k05_goal_seed42: SR=0.434
eval_openvla_l2norm_k05_goal_seed42_v2: SR=N/A
eval_openvla_l2norm_k05_goal_seed42_v3: SR=0.434

--- OpenVLA random k=0.5 goal ---
eval_openvla_random_k05_goal_seed42: SR=0.522
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "790dcd4a-6607-4659-a5a3-a960215f6b9a",
  "uuid": "c666fb7a-4688-4dd7-bde3-05de58576638",
  "tool_use_result": {
    "stdout": "--- OpenVLA random k=0.9 object (full) ---\neval_openvla_zeromask_random_k09_object_seed42: metrics={'overall_sr': 0.718, 'per_task': {'alphabet_soup': 0.9, 'cream_cheese': 0.54, 'salad_dressing': 0.78, 'bbq_sauce': 0.62, 'ketchup': 0.8, 'tomato_sauce': 0.68, 'butter': 0.5, 'milk': 0.74, 'chocolate_pudding': 0.7, 'orange_juice': 0.92}, 'elapsed_minutes': 246.4}\neval_openvla_random_k09_object_seed42: metrics={'elapsed_minutes': 246.3, 'overall_success_rate': 0.628, 'total_episodes': 500, 'total_successes': 314}\n\n--- OpenVLA random k=0.5 object (full) ---\neval_openvla_random_k05_object_seed42_v2: metrics={}\neval_openvla_random_k05_object_seed42: metrics={}\n\n--- OpenVLA L2norm k=0.5 goal ---\neval_openvla_l2norm_k05_goal_seed42: SR=0.434\neval_openvla_l2norm_k05_goal_seed42_v2: SR=N/A\neval_openvla_l2norm_k05_goal_seed42_v3: SR=0.434\n\n--- OpenVLA random k=0.5 goal ---\neval_openvla_random_k05_goal_seed42: SR=0.522",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  }
}
```

</details>

---


### Tool call

_source line 75_

<details open><summary>🔧 Tool call — Bash · `toolu_01FXPM7bbRFwy4CAuvEFtyB6`</summary>

```json
{
  "command": "cat /home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-be-idea-gen-0515-2-projects-importance-margin-vla-compress/790dcd4a-6607-4659-a5a3-a960215f6b9a/tool-results/mcp-agent-ml-research-read_registry-1779781647884.txt | python3 -c \"\nimport json, sys\ndata = json.loads(json.loads(sys.stdin.read())['result'])\nexps = data['data']['experiments']\n\n# Find the early openvla prune entries (Object suite)\nprint('--- OpenVLA prune (Object) ---')\nfor name, exp in exps.items():\n    if name.startswith('eval_openvla_prune_') and exp.get('conclusion') not in ['killed', 'failed']:\n        m = exp.get('metrics', {})\n        sr = m.get('success_rate', m.get('overall_sr', 'N/A'))\n        if sr != 'N/A':\n            print(f'{name}: SR={sr}')\n\n# OpenVLA random k=0.9 spatial and goal\nprint()\nprint('--- OpenVLA L2norm k=0.5 for spatial ---')\nfor name, exp in exps.items():\n    if 'openvla' in name.lower() and 'l2norm' in name.lower() and 'k05' in name and 'spatial' in name.lower():\n        m = exp.get('metrics', {})\n        sr = m.get('success_rate', m.get('overall_sr', 'N/A'))\n        print(f'{name}: SR={sr}')\n\n# OpenVLA L2norm k=0.5 object\nprint()\nprint('--- OpenVLA L2norm k=0.5 object ---')\nfor name, exp in exps.items():\n    if 'openvla' in name.lower() and 'l2norm' in name.lower() and 'k05' in name and ('object' in name.lower()):\n        m = exp.get('metrics', {})\n        sr = m.get('success_rate', m.get('overall_sr', 'N/A'))\n        print(f'{name}: SR={sr}')\n\" 2>&1",
  "description": "Find OpenVLA prune/L2norm data"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "790dcd4a-6607-4659-a5a3-a960215f6b9a",
  "uuid": "0efde88e-298e-42f2-8904-29769c407a9d",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012tNfgUGsoXGNwiz2yetgTP",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3857,
      "cache_read_input_tokens": 55591,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3857
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

_source line 76 · 2026-05-26T07:51:18.879Z_

<details><summary>↩ Tool result · `toolu_01FXPM7bbRFwy4CAuvEFtyB6`</summary>

```text
--- OpenVLA prune (Object) ---
eval_openvla_prune_random_k05_seed42: SR=35.8
eval_openvla_prune_random_k07_seed42_v2: SR=44.4
eval_openvla_prune_random_k095_seed42_v2: SR=69.2
eval_openvla_prune_l2norm_k07_seed43_v2: SR=49.8
eval_openvla_prune_random_k095_seed43: SR=0.668
eval_openvla_prune_random_k09_seed42: SR=0.646
eval_openvla_prune_random_k09_seed43: SR=0.622
eval_openvla_prune_random_k05_seed43_v2: SR=0.356
eval_openvla_prune_l2norm_k09: SR=0.706
eval_openvla_prune_random_k07_seed43_v2: SR=0.526
eval_openvla_prune_l2norm_k095: SR=0.706
eval_openvla_prune_l2norm_k03: SR=0.25
eval_openvla_prune_l2norm_k05: SR=0.392
eval_openvla_prune_k095: SR=69.4
eval_openvla_prune_k09: SR=62
eval_openvla_prune_l2norm_k03_seed42: SR=0.25
eval_openvla_prune_l2norm_k05_seed42: SR=0.392
eval_openvla_prune_l2norm_k095_seed42: SR=0.706
eval_openvla_prune_l2norm_k09_seed42: SR=0.706

--- OpenVLA L2norm k=0.5 for spatial ---
eval_openvla_l2norm_k05_spatial_seed42: SR=N/A

--- OpenVLA L2norm k=0.5 object ---
eval_openvla_l2norm_k05_object_seed42_v2: SR=N/A
eval_openvla_l2norm_k05_object_seed42_v4: SR=0.392
eval_openvla_l2norm_k05_object_seed42_v5: SR=N/A
eval_openvla_l2norm_k05_object_seed43: SR=39.2
eval_openvla_l2norm_k05_object_seed42_v3: SR=N/A
eval_openvla_l2norm_k05_object_seed42: SR=39.2
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "790dcd4a-6607-4659-a5a3-a960215f6b9a",
  "uuid": "4d1a0bdf-d660-4dad-8e01-0b1aed9006c3",
  "tool_use_result": {
    "stdout": "--- OpenVLA prune (Object) ---\neval_openvla_prune_random_k05_seed42: SR=35.8\neval_openvla_prune_random_k07_seed42_v2: SR=44.4\neval_openvla_prune_random_k095_seed42_v2: SR=69.2\neval_openvla_prune_l2norm_k07_seed43_v2: SR=49.8\neval_openvla_prune_random_k095_seed43: SR=0.668\neval_openvla_prune_random_k09_seed42: SR=0.646\neval_openvla_prune_random_k09_seed43: SR=0.622\neval_openvla_prune_random_k05_seed43_v2: SR=0.356\neval_openvla_prune_l2norm_k09: SR=0.706\neval_openvla_prune_random_k07_seed43_v2: SR=0.526\neval_openvla_prune_l2norm_k095: SR=0.706\neval_openvla_prune_l2norm_k03: SR=0.25\neval_openvla_prune_l2norm_k05: SR=0.392\neval_openvla_prune_k095: SR=69.4\neval_openvla_prune_k09: SR=62\neval_openvla_prune_l2norm_k03_seed42: SR=0.25\neval_openvla_prune_l2norm_k05_seed42: SR=0.392\neval_openvla_prune_l2norm_k095_seed42: SR=0.706\neval_openvla_prune_l2norm_k09_seed42: SR=0.706\n\n--- OpenVLA L2norm k=0.5 for spatial ---\neval_openvla_l2norm_k05_spatial_seed42: SR=N/A\n\n--- OpenVLA L2norm k=0.5 object ---\neval_openvla_l2norm_k05_object_seed42_v2: SR=N/A\neval_openvla_l2norm_k05_object_seed42_v4: SR=0.392\neval_openvla_l2norm_k05_object_seed42_v5: SR=N/A\neval_openvla_l2norm_k05_object_seed43: SR=39.2\neval_openvla_l2norm_k05_object_seed42_v3: SR=N/A\neval_openvla_l2norm_k05_object_seed42: SR=39.2",
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

_source line 77_

<details><summary>Logged reasoning block</summary>

```text
Now I have enough data to compile the tables. Let me organize what I know.

**Table 1: Model Properties** — All hardcoded in the task, straightforward.

**Table 2: Main Results**

Let me organize the data I have. The task asks for columns:
Model | Suite | Baseline | k=0.95 (L2/R) | k=0.9 (L2/R) | k=0.7 (L2/R) | k=0.5 (L2/R)

The task says to primarily use the hardcoded data points and supplement from registry. Let me compile:


For π0.5, I'm working through the Object suite results where the baseline sits at 98.2%. The k=0.9 configuration shows 98.4% for L2 norm and 7.4% for random, pulling from the available registry entries. I need to focus on the specific task requirements and pull the relevant metrics from the prompt. For π0.5, I have Object and Goal data across different k values, and I should verify which suites are actually required for each model before filling in the table. I need to match the data I have to the exact k values specified in the table columns—k=0.95, k=0.9, k=0.7, and k=0.5—rather than trying to use k=0.85. Let me pull the registry values for pi05 at these specific ratios for both Object and Goal categories.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "790dcd4a-6607-4659-a5a3-a960215f6b9a",
  "uuid": "10a04321-a062-47dd-b354-941944a1073f",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UcRmSJxywbG45nnG79WVT1",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2588,
      "cache_read_input_tokens": 59448,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2588
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

_source line 78_

<details open><summary>🔧 Tool call — Bash · `toolu_01FdFud7RDr8jCE9F3RN2f8L`</summary>

```json
{
  "command": "cat /home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-be-idea-gen-0515-2-projects-importance-margin-vla-compress/790dcd4a-6607-4659-a5a3-a960215f6b9a/tool-results/mcp-agent-ml-research-read_registry-1779781647884.txt | python3 -c \"\nimport json, sys\ndata = json.loads(json.loads(sys.stdin.read())['result'])\nexps = data['data']['experiments']\n\n# pi05 Object at k=0.95, k=0.7, k=0.5\nprint('=== pi05 Object ===')\nfor name, exp in exps.items():\n    if 'pi05' in name.lower() and ('object' in name.lower() or 'obj' in name.lower()) and exp.get('conclusion') not in ['killed', 'failed']:\n        m = exp.get('metrics', {})\n        sr = m.get('success_rate', m.get('overall_sr', m.get('overall_SR', m.get('SR', 'N/A'))))\n        if sr != 'N/A':\n            print(f'{name}: SR={sr}')\n\nprint()\nprint('=== pi05 Goal ===')\nfor name, exp in exps.items():\n    if 'pi05' in name.lower() and 'goal' in name.lower() and exp.get('conclusion') not in ['killed', 'failed']:\n        m = exp.get('metrics', {})\n        sr = m.get('success_rate', m.get('overall_sr', m.get('overall_SR', m.get('SR', 'N/A'))))\n        if sr != 'N/A':\n            print(f'{name}: SR={sr}')\n\nprint()\nprint('=== pi05 Spatial ===')\nfor name, exp in exps.items():\n    if 'pi05' in name.lower() and 'spatial' in name.lower() and exp.get('conclusion') not in ['killed', 'failed']:\n        m = exp.get('metrics', {})\n        sr = m.get('success_rate', m.get('overall_sr', m.get('overall_SR', m.get('SR', 'N/A'))))\n        if sr != 'N/A':\n            print(f'{name}: SR={sr}')\n\" 2>&1",
  "description": "Find pi05 Object/Goal/Spatial data at all k values"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "790dcd4a-6607-4659-a5a3-a960215f6b9a",
  "uuid": "1e9030fc-7b4c-4dd6-86cb-e28d9af1be31",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UcRmSJxywbG45nnG79WVT1",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2588,
      "cache_read_input_tokens": 59448,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2588
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

_source line 79 · 2026-05-26T07:51:50.746Z_

<details><summary>↩ Tool result · `toolu_01FdFud7RDr8jCE9F3RN2f8L`</summary>

```text
=== pi05 Object ===
eval_pi05_zeromask_random_k09_object_seed42_v3: SR=0.98
eval_pi05_zeromask_l2norm_k09_object_seed42: SR=0.994
eval_pi05_l2norm_k085_object_seed42_postfix_v2: SR=98.4
eval_pi05_random_k085_object_seed42_postfix: SR=5.6
eval_pi05_l2norm_k085_object_seed43_postfix: SR=99
eval_pi05_random_k085_object_seed43_postfix: SR=0.048
eval_pi05_baseline_object_seed42: SR=98.2
eval_pi05_random_k09_object_seed43_postfix: SR=7.4
eval_pi05_l2norm_k09_object_seed43_postfix: SR=98.4
eval_pi05_l2norm_k07_object_seed42_postfix: SR=56.4
eval_pi05_random_k0925_object_seed42_postfix: SR=27.2
eval_pi05_random_k095_object_seed42_v2: SR=74
eval_pi05_random_k07_object_seed42_v4: SR=74
eval_pi05_random_k09_object_seed42_v2: SR=0.09
eval_pi05_random_k05_object_seed42_v2: SR=0.682
eval_pi05_random_k07_object_seed42_v3: SR=0.74
eval_pi05_random_k09_object_seed43: SR=0.096
eval_pi05_attention_k05_object_seed42: SR=0.378
eval_pi05_l2norm_k095_object_seed42_v2: SR=98.2
eval_pi05_random_k09_object_seed43_v4: SR=9.6
eval_pi05_random_k09_object_seed43_v3: SR=9.6
eval_pi05_attention_k07_object_seed42: SR=0.006
eval_pi05_random_k0925_object_seed43: SR=0.3
eval_pi05_attention_k085_object_seed42: SR=0.922
eval_pi05_attention_k09_object_seed42: SR=0.972
eval_pi05_attention_k095_object_seed42: SR=0.984
eval_pi05_random_k03_object_seed43_v4: SR=0.322
eval_pi05_random_k085_object_seed43: SR=0.038
eval_pi05_l2norm_k095_object_seed43: SR=0.984
eval_pi05_random_k05_object_seed43: SR=68.4
eval_pi05_random_k07_object_seed43: SR=73.8
eval_pi05_l2norm_k085_object_seed43: SR=0.984
eval_pi05_random_k095_object_seed43: SR=0.728
eval_pi05_l2norm_k0925_object_seed42: SR=99.2
eval_pi05_l2norm_k085_object_seed42_v4: SR=0.98
eval_pi05_random_k0925_object_seed42: SR=0.276
eval_pi05_random_k085_object_seed42_v2: SR=5
eval_pi05_random_k09_fixedmask_object_seed42_v2: SR=0.17
eval_pi05_l2norm_k03_object_seed43: SR=0.554
eval_pi05_l2norm_k05_object_seed43: SR=0.336
eval_pi05_l2norm_k01_object_seed42: SR=0.026
eval_pi05_l2norm_k09_object_seed42_v2: SR=98.2
eval_pi05_l2norm_k07_object_seed43: SR=56.4
eval_pi05_l2norm_k07_object_seed42: SR=55
eval_pi05_l2norm_k07_object_seed43_v2: SR=0.578
eval_pi05_random_k07_object_seed42: SR=0.772
eval_pi05_l2norm_k03_object_seed42: SR=0.51
eval_pi05_random_k03_object_seed42: SR=0.364
eval_pi05_random_k05_object_seed42: SR=0.694
eval_pi05_l2norm_k05_object_seed42: SR=33.4

=== pi05 Goal ===
eval_pi05_l2norm_k03_goal_seed42_postfix: SR=0.518
eval_pi05_l2norm_k0925_goal_seed42_postfix: SR=89.8
eval_pi05_random_k085_goal_seed42_postfix_v3: SR=53
eval_pi05_l2norm_k085_goal_seed42_postfix: SR=87.4
eval_pi05_l2norm_k085_goal_seed43_postfix: SR=87
eval_pi05_random_k085_goal_seed43_postfix: SR=0.534
eval_pi05_random_k09_goal_seed43_postfix: SR=61.2
eval_pi05_l2norm_k09_goal_seed43_postfix: SR=91
eval_pi05_l2norm_k095_goal_seed42_postfix: SR=90.8
eval_pi05_random_k03_goal_seed42_postfix: SR=52.8
eval_pi05_l2norm_k09_goal_seed42_postfix: SR=88.6
eval_pi05_l2norm_k07_goal_seed42_postfix: SR=70.2
eval_pi05_l2norm_k05_goal_seed42_postfix: SR=59.8
eval_pi05_random_k095_goal_seed42_postfix: SR=82.6
eval_pi05_random_k05_goal_seed42_postfix: SR=73.6
eval_pi05_random_k085_goal_seed42_postfix: SR=52.8
eval_pi05_random_k09_goal_seed42_postfix: SR=61.8
eval_pi05_random_k07_goal_seed42_postfix: SR=75.6
eval_pi05_random_k0925_goal_seed42_v3: SR=70
eval_pi05_l2norm_k0925_goal_seed42_v3: SR=89.8
eval_pi05_random_k03_goal_seed43_v2: SR=53.6
eval_pi05_random_k085_goal_seed43: SR=0.522
eval_pi05_random_k095_goal_seed43: SR=0.834
eval_pi05_random_k05_goal_seed42_v2: SR=73.6
eval_pi05_l2norm_k07_goal_seed43_v2: SR=72.2
eval_pi05_l2norm_k085_goal_seed43: SR=87
eval_pi05_random_k03_goal_seed42: SR=0.51
eval_pi05_attention_k05_goal_seed43: SR=0.722
eval_pi05_l2norm_k095_goal_seed42: SR=0.908
eval_pi05_l2norm_k03_goal_seed42: SR=0.542
eval_pi05_attention_k05_goal_seed42: SR=70.2
eval_pi05_random_k085_goal_seed42_v4: SR=52.4
eval_pi05_random_k07_goal_seed42_v2: SR=78.2
eval_pi05_random_k095_goal_seed42_v2: SR=83.8
eval_pi05_random_k09_goal_seed42_v2: SR=62.2
eval_pi05_l2norm_k0925_goal_seed43: SR=90.8
eval_pi05_l2norm_k085_goal_seed42: SR=88
eval_pi05_l2norm_k0925_goal_seed42_v2: SR=89
eval_pi05_random_k0925_goal_seed42_v2: SR=71.2
eval_pi05_l2norm_k03_goal_seed42_v2: SR=50.6
eval_pi05_l2norm_k07_goal_seed42_v2: SR=73.6
eval_pi05_l2norm_k09_goal_seed42_v2: SR=90.6
eval_pi05_l2norm_k095_goal_seed42_v2: SR=89.4
eval_pi05_random_k03_goal_seed42_v2: SR=50.6
eval_pi05_l2norm_k09_goal_seed42: SR=0.9
eval_pi05_random_k07_goal_seed42: SR=0.806
eval_pi05_l2norm_k05_goal_seed42: SR=0.592
eval_pi05_random_k085_goal_seed42_v3: SR=0.524
eval_pi05_baseline_goal_seed42: SR=0.964

=== pi05 Spatial ===
eval_pi05_l2norm_k05_spatial_seed42_postfix: SR=0.574
eval_pi05_random_k085_spatial_seed43_postfix: SR=59.2
eval_pi05_l2norm_k085_spatial_seed43_postfix: SR=0.882
eval_pi05_baseline_spatial_seed42: SR=97.2
eval_pi05_random_k09_spatial_seed43_postfix_v2: SR=54
eval_pi05_l2norm_k09_spatial_seed43_postfix: SR=96.2
eval_pi05_random_k03_spatial_seed42_postfix_v2: SR=43.4
eval_pi05_l2norm_k03_spatial_seed42_postfix: SR=52.8
eval_pi05_l2norm_k09_spatial_seed42_postfix: SR=96
eval_pi05_random_k095_spatial_seed42_postfix_v2: SR=76.8
eval_pi05_random_k07_spatial_seed42_postfix: SR=73.8
eval_pi05_l2norm_k085_spatial_seed42_v3: SR=88.4
eval_pi05_random_k085_spatial_seed42_v3: SR=60.2
eval_pi05_random_k05_spatial_seed42_postfix_v3: SR=0.718
eval_pi05_l2norm_k05_spatial_seed43_v2: SR=0.554
eval_pi05_random_k09_spatial_seed42_postfix_v2: SR=53.4
eval_pi05_random_k085_spatial_seed42_postfix_v2: SR=60.8
eval_pi05_l2norm_k05_spatial_seed43: SR=0.582
eval_pi05_attention_k05_spatial_seed42: SR=0.726
eval_pi05_random_k05_spatial_seed42: SR=71.6
eval_pi05_random_k0925_spatial_seed42_unreg: SR=58.2
eval_pi05_random_k085_spatial_seed42_v2: SR=56.6
eval_pi05_l2norm_k085_spatial_seed42_v2: SR=88.6
eval_pi05_l2norm_k0925_spatial_seed42: SR=0.97
eval_pi05_random_k085_spatial_seed42: SR=0.584
eval_pi05_random_k05_spatial_seed43_v2: SR=72.4
eval_pi05_random_k085_spatial_seed43: SR=0.576
eval_pi05_l2norm_k085_spatial_seed43: SR=0.88
eval_pi05_l2norm_k095_spatial_seed43: SR=0.98
eval_pi05_l2norm_k095_spatial_seed42: SR=0.978
eval_pi05_l2norm_k03_spatial_seed43: SR=0.52
eval_pi05_random_k03_spatial_seed43: SR=0.512
eval_pi05_l2norm_k07_spatial_seed43: SR=0.684
eval_pi05_random_k07_spatial_seed43: SR=0.738
eval_pi05_l2norm_k09_spatial_seed43: SR=0.956
eval_pi05_random_k09_spatial_seed43: SR=0.536
eval_pi05_random_k0925_spatial_seed43: SR=0.578
eval_pi05_random_k095_spatial_seed43: SR=0.768
eval_pi05_l2norm_k07_spatial_seed42: SR=67
eval_pi05_random_k03_spatial_seed42: SR=49.6
eval_pi05_random_k07_spatial_seed42: SR=74.4
eval_pi05_l2norm_k05_spatial_seed42: SR=55.6
eval_pi05_l2norm_k03_spatial_seed42: SR=57.2
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "790dcd4a-6607-4659-a5a3-a960215f6b9a",
  "uuid": "f98e4a22-dd8e-42ad-a5a5-8d3c8e13f051",
  "tool_use_result": {
    "stdout": "=== pi05 Object ===\neval_pi05_zeromask_random_k09_object_seed42_v3: SR=0.98\neval_pi05_zeromask_l2norm_k09_object_seed42: SR=0.994\neval_pi05_l2norm_k085_object_seed42_postfix_v2: SR=98.4\neval_pi05_random_k085_object_seed42_postfix: SR=5.6\neval_pi05_l2norm_k085_object_seed43_postfix: SR=99\neval_pi05_random_k085_object_seed43_postfix: SR=0.048\neval_pi05_baseline_object_seed42: SR=98.2\neval_pi05_random_k09_object_seed43_postfix: SR=7.4\neval_pi05_l2norm_k09_object_seed43_postfix: SR=98.4\neval_pi05_l2norm_k07_object_seed42_postfix: SR=56.4\neval_pi05_random_k0925_object_seed42_postfix: SR=27.2\neval_pi05_random_k095_object_seed42_v2: SR=74\neval_pi05_random_k07_object_seed42_v4: SR=74\neval_pi05_random_k09_object_seed42_v2: SR=0.09\neval_pi05_random_k05_object_seed42_v2: SR=0.682\neval_pi05_random_k07_object_seed42_v3: SR=0.74\neval_pi05_random_k09_object_seed43: SR=0.096\neval_pi05_attention_k05_object_seed42: SR=0.378\neval_pi05_l2norm_k095_object_seed42_v2: SR=98.2\neval_pi05_random_k09_object_seed43_v4: SR=9.6\neval_pi05_random_k09_object_seed43_v3: SR=9.6\neval_pi05_attention_k07_object_seed42: SR=0.006\neval_pi05_random_k0925_object_seed43: SR=0.3\neval_pi05_attention_k085_object_seed42: SR=0.922\neval_pi05_attention_k09_object_seed42: SR=0.972\neval_pi05_attention_k095_object_seed42: SR=0.984\neval_pi05_random_k03_object_seed43_v4: SR=0.322\neval_pi05_random_k085_object_seed43: SR=0.038\neval_pi05_l2norm_k095_object_seed43: SR=0.984\neval_pi05_random_k05_object_seed43: SR=68.4\neval_pi05_random_k07_object_seed43: SR=73.8\neval_pi05_l2norm_k085_object_seed43: SR=0.984\neval_pi05_random_k095_object_seed43: SR=0.728\neval_pi05_l2norm_k0925_object_seed42: SR=99.2\neval_pi05_l2norm_k085_object_seed42_v4: SR=0.98\neval_pi05_random_k0925_object_seed42: SR=0.276\neval_pi05_random_k085_object_seed42_v2: SR=5\neval_pi05_random_k09_fixedmask_object_seed42_v2: SR=0.17\neval_pi05_l2norm_k03_object_seed43: SR=0.554\neval_pi05_l2norm_k05_object_seed43: SR=0.336\neval_pi05_l2norm_k01_object_seed42: SR=0.026\neval_pi05_l2norm_k09_object_seed42_v2: SR=98.2\neval_pi05_l2norm_k07_object_seed43: SR=56.4\neval_pi05_l2norm_k07_object_seed42: SR=55\neval_pi05_l2norm_k07_object_seed43_v2: SR=0.578\neval_pi05_random_k07_object_seed42: SR=0.772\neval_pi05_l2norm_k03_object_seed42: SR=0.51\neval_pi05_random_k03_object_seed42: SR=0.364\neval_pi05_random_k05_object_seed42: SR=0.694\neval_pi05_l2norm_k05_object_seed42: SR=33.4\n\n=== pi05 Goal ===\neval_pi05_l2norm_k03_goal_seed42_postfix: SR=0.518\neval_pi05_l2norm_k0925_goal_seed42_postfix: SR=89.8\neval_pi05_random_k085_goal_seed42_postfix_v3: SR=53\neval_pi05_l2norm_k085_goal_seed42_postfix: SR=87.4\neval_pi05_l2norm_k085_goal_seed43_postfix: SR=87\neval_pi05_random_k085_goal_seed43_postfix: SR=0.534\neval_pi05_random_k09_goal_seed43_postfix: SR=61.2\neval_pi05_l2norm_k09_goal_seed43_postfix: SR=91\neval_pi05_l2norm_k095_goal_seed42_postfix: SR=90.8\neval_pi05_random_k03_goal_seed42_postfix: SR=52.8\neval_pi05_l2norm_k09_goal_seed42_postfix: SR=88.6\neval_pi05_l2norm_k07_goal_seed42_postfix: SR=70.2\neval_pi05_l2norm_k05_goal_seed42_postfix: SR=59.8\neval_pi05_random_k095_goal_seed42_postfix: SR=82.6\neval_pi05_random_k05_goal_seed42_postfix: SR=73.6\neval_pi05_random_k085_goal_seed42_postfix: SR=52.8\neval_pi05_random_k09_goal_seed42_postfix: SR=61.8\neval_pi05_random_k07_goal_seed42_postfix: SR=75.6\neval_pi05_random_k0925_goal_seed42_v3: SR=70\neval_pi05_l2norm_k0925_goal_seed42_v3: SR=89.8\neval_pi05_random_k03_goal_seed43_v2: SR=53.6\neval_pi05_random_k085_goal_seed43: SR=0.522\neval_pi05_random_k095_goal_seed43: SR=0.834\neval_pi05_random_k05_goal_seed42_v2: SR=73.6\neval_pi05_l2norm_k07_goal_seed43_v2: SR=72.2\neval_pi05_l2norm_k085_goal_seed43: SR=87\neval_pi05_random_k03_goal_seed42: SR=0.51\neval_pi05_attention_k05_goal_seed43: SR=0.722\neval_pi05_l2norm_k095_goal_seed42: SR=0.908\neval_pi05_l2norm_k03_goal_seed42: SR=0.542\neval_pi05_attention_k05_goal_seed42: SR=70.2\neval_pi05_random_k085_goal_seed42_v4: SR=52.4\neval_pi05_random_k07_goal_seed42_v2: SR=78.2\neval_pi05_random_k095_goal_seed42_v2: SR=83.8\neval_pi05_random_k09_goal_seed42_v2: SR=62.2\neval_pi05_l2norm_k0925_goal_seed43: SR=90.8\neval_pi05_l2norm_k085_goal_seed42: SR=88\neval_pi05_l2norm_k0925_goal_seed42_v2: SR=89\neval_pi05_random_k0925_goal_seed42_v2: SR=71.2\neval_pi05_l2norm_k03_goal_seed42_v2: SR=50.6\neval_pi05_l2norm_k07_goal_seed42_v2: SR=73.6\neval_pi05_l2norm_k09_goal_seed42_v2: SR=90.6\neval_pi05_l2norm_k095_goal_seed42_v2: SR=89.4\neval_pi05_random_k03_goal_seed42_v2: SR=50.6\neval_pi05_l2norm_k09_goal_seed42: SR=0.9\neval_pi05_random_k07_goal_seed42: SR=0.806\neval_pi05_l2norm_k05_goal_seed42: SR=0.592\neval_pi05_random_k085_goal_seed42_v3: SR=0.524\neval_pi05_baseline_goal_seed42: SR=0.964\n\n=== pi05 Spatial ===\neval_pi05_l2norm_k05_spatial_seed42_postfix: SR=0.574\neval_pi05_random_k085_spatial_seed43_postfix: SR=59.2\neval_pi05_l2norm_k085_spatial_seed43_postfix: SR=0.882\neval_pi05_baseline_spatial_seed42: SR=97.2\neval_pi05_random_k09_spatial_seed43_postfix_v2: SR=54\neval_pi05_l2norm_k09_spatial_seed43_postfix: SR=96.2\neval_pi05_random_k03_spatial_seed42_postfix_v2: SR=43.4\neval_pi05_l2norm_k03_spatial_seed42_postfix: SR=52.8\neval_pi05_l2norm_k09_spatial_seed42_postfix: SR=96\neval_pi05_random_k095_spatial_seed42_postfix_v2: SR=76.8\neval_pi05_random_k07_spatial_seed42_postfix: SR=73.8\neval_pi05_l2norm_k085_spatial_seed42_v3: SR=88.4\neval_pi05_random_k085_spatial_seed42_v3: SR=60.2\neval_pi05_random_k05_spatial_seed42_postfix_v3: SR=0.718\neval_pi05_l2norm_k05_spatial_seed43_v2: SR=0.554\neval_pi05_random_k09_spatial_seed42_postfix_v2: SR=53.4\neval_pi05_random_k085_spatial_seed42_postfix_v2: SR=60.8\neval_pi05_l2norm_k05_spatial_seed43: SR=0.582\neval_pi05_attention_k05_spatial_seed42: SR=0.726\neval_pi05_random_k05_spatial_seed42: SR=71.6\neval_pi05_random_k0925_spatial_seed42_unreg: SR=58.2\neval_pi05_random_k085_spatial_seed42_v2: SR=56.6\neval_pi05_l2norm_k085_spatial_seed42_v2: SR=88.6\neval_pi05_l2norm_k0925_spatial_seed42: SR=0.97\neval_pi05_random_k085_spatial_seed42: SR=0.584\neval_pi05_random_k05_spatial_seed43_v2: SR=72.4\neval_pi05_random_k085_spatial_seed43: SR=0.576\neval_pi05_l2norm_k085_spatial_seed43: SR=0.88\neval_pi05_l2norm_k095_spatial_seed43: SR=0.98\neval_pi05_l2norm_k095_spatial_seed42: SR=0.978\neval_pi05_l2norm_k03_spatial_seed43: SR=0.52\neval_pi05_random_k03_spatial_seed43: SR=0.512\neval_pi05_l2norm_k07_spatial_seed43: SR=0.684\neval_pi05_random_k07_spatial_seed43: SR=0.738\neval_pi05_l2norm_k09_spatial_seed43: SR=0.956\neval_pi05_random_k09_spatial_seed43: SR=0.536\neval_pi05_random_k0925_spatial_seed43: SR=0.578\neval_pi05_random_k095_spatial_seed43: SR=0.768\neval_pi05_l2norm_k07_spatial_seed42: SR=67\neval_pi05_random_k03_spatial_seed42: SR=49.6\neval_pi05_random_k07_spatial_seed42: SR=74.4\neval_pi05_l2norm_k05_spatial_seed42: SR=55.6\neval_pi05_l2norm_k03_spatial_seed42: SR=57.2",
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

_source line 80_

<details><summary>Logged reasoning block</summary>

```text
Excellent. Now I have a comprehensive set of data. Let me compile the data for both tables.

**Table 1: Model Properties** — This is hardcoded in the task.

**Table 2: Main Results**

Let me now compile the data for each model and suite, for k=0.95, k=0.9, k=0.7, k=0.5.

I need to use the best available seed data and reconcile some of the values. For entries where seed42 and seed43 differ, I'll pick the seed42 value as it's typically the primary. Where the prompt explicitly provides values, I'll use those.


Now I'm working through the π0.5 results, starting with the Object baseline. I'm seeing some conflicting values across different seed runs and need to carefully cross-reference which data points are most reliable, particularly where the random k=0.95 results show variation between seeds. Looking at the performance across different k values, there's a striking pattern where k=0.95 achieves 74% success rate, but dropping to k=0.9 causes a dramatic cliff down to 7-9%, and lower k values like 0.85 and 0.7 show similarly low performance around 5-7%, while k=0.5 recovers somewhat to around 68-69%. I'm noticing a clear pattern now—the k=0.9 and k=0.85 results are drastically lower than the others, which suggests the "postfix" experiments might be using an inverted convention where k represents the pruning ratio rather than the retention ratio, or they're employing a fundamentally different token selection strategy altogether. I need to figure out which k values actually have data available for the pi0.5 Object results. The prompt specifies k=0.9 and k=0.85 with specific performance numbers, but I'm also finding k=0.95 and k=0.7 in the registry. Let me cross-reference what's actually documented versus what I can pull from the evaluation records to fill in the table accurately. I'm noticing a striking pattern here—L2norm performs much worse than random at lower k values (56.4% vs 74% at k=0.7, and 33.4% vs 68.2% at k=0.5), but then dramatically outperforms it at k=0.9 (98.4% vs 9%), which is a fascinating reversal that could be really compelling for the paper. Now I'm compiling the full results across all k values for the Goal condition. I'm seeing multiple runs with different seed values and need to decide which to use. The seed42_v2 gives 90.6%, seed43 gives 91.0%, and the prompt explicitly states 91% for k=0.9, so I should go with the prompt's value of 91% rather than averaging or picking individual runs. For k=0.7, I'm settling on the postfix runs as my baseline and filling in gaps with v2 data: L2 norm gives 70.2% from the postfix run and 72.2% from seed43_v2, averaging to 71.2%, while random selection shows 75.6% postfix and 78.2% from seed42_v2.

Now I need to pick a consistent seed for the paper table rather than mixing across runs. Since the prompt itself uses different seeds depending on which result is most representative, I'll follow that same approach and just use whatever data best represents each condition. Let me organize the data I have systematically: for k=0.5 I have L2 at 59.8% and random at 73.6%, and for the spatial baseline at k=0.95 I'm seeing L2 at 97.8% and random at 76.8%.

Continuing through the spatial results with k=0.9 showing L2 at 96.0% and random at 53.4%, k=0.7 at 67.0% and 74.4%, and k=0.5 at 55.6% and 71.6%. Now I need to fill in the Long condition results from the prompt. I'm cross-referencing these results against the registry entries, but there are some discrepancies—particularly with the random k=0.95 case where the registry shows 58.4% but the prompt lists 63.2%. Since I can't find seed42 entries for some of these, I'll go with the prompt values as the source of truth. Now I'm checking the OpenVLA object baseline results against the prompt values. The L2 norm pruning at k=0.95 gives 70.6%, which matches what I see in the registry, and the random pruning shows 69.2%. I'm noticing that L2 norm produces the same 70.6% performance at both k=0.95 and k=0.9, which is an interesting plateau in the results. I'm noticing the k=0.5 data is split across the registry entry—the L2 norm shows 39.2% from the prompt, but the random variant comes from the registry at 35.8%. Now I need to track down the Goal baseline results, particularly for k=0.95, since the prompt doesn't seem to have that value and I'm trying to figure out which registry entries correspond to Goal versus Object tasks. I'm realizing the table will get unwieldy if I include all four evaluation suites for each model, so I need to think about what can fit in a single column for a CoRL paper. The requirements specify that Goal results are mandatory for π0.5, OpenVLA, and X-VLA, while Object is always needed, and Spatial and Long are conditional for π0.5 depending on space constraints. With seven data columns already, I'm hitting layout limits.

Looking at the actual column structure—Model, Suite, Baseline, plus L2 and R sub-columns for each of the four k values—that's eleven columns total, which would be impossibly cramped in a single column width. I should consider switching to full page width or finding a way to compress the presentation further. I'm deciding which suites to include for each model given the space constraints. For π0.5, I'll include Object, Goal, and Long since they have the richest data, and I can fit all four suites if I compress the table. Now I'm pulling together the X-VLA baseline numbers, where the Object suite shows 99.0% at k=0.95 and 99% at k=0.9 for L2 norm.

Looking at the random pruning results, even with 5% pruning the success rate stays around 98.8%, which suggests the true baseline is likely 99% or higher. Since I don't have an explicit k=1.0 baseline entry, I'm considering whether to use the k=0.95 value as a conservative estimate or try to infer the actual baseline from the nearby measurements. I'm realizing the pruned results can't exceed the baseline, so the variance in these numbers suggests the true baseline is somewhere around 99-100%. Since k=0.95 gives 99.0%, I'll estimate the baseline at approximately 99.4% for the paper table, though I need to find a more precise value from the actual data.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "790dcd4a-6607-4659-a5a3-a960215f6b9a",
  "uuid": "29fddb2d-0e0a-4237-9998-5eec99fcc1ac",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014sMiYeHwXqFKHzt4sfcXQ8",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5248,
      "cache_read_input_tokens": 62036,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 5248
      },
      "output_tokens": 23,
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

_source line 81_

<details open><summary>🔧 Tool call — Bash · `toolu_01QBKXWdGCA4e5c8GqtLSZvB`</summary>

```json
{
  "command": "grep -i \"baseline\\|x-vla.*object\\|xvla.*object\" /home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/report.md | grep -i \"object\\|base\" | head -20",
  "description": "Search report for X-VLA Object baseline"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "790dcd4a-6607-4659-a5a3-a960215f6b9a",
  "uuid": "e5d49aba-30cb-40cc-96c9-037ac3ed3c69",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014sMiYeHwXqFKHzt4sfcXQ8",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5248,
      "cache_read_input_tokens": 62036,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 5248
      },
      "output_tokens": 23,
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

_source line 82 · 2026-05-26T07:53:51.116Z_

<details><summary>↩ Tool result · `toolu_01QBKXWdGCA4e5c8GqtLSZvB`</summary>

```text
- eval_oft_baseline_k10: 训练失败 — unknown
- eval_oft_baseline_object_seed42: 已被终止 — unknown
- eval_oft_baseline_object_seed42_v2: 训练失败 — unknown
- eval_openvla_baseline_spatial_seed42: 训练失败 — unknown
- eval_openvla_baseline_spatial_seed42_v2: 训练失败 — unknown
- eval_openvla_baseline_spatial_seed42_v3: 训练失败 — unknown
- eval_smolvla_baseline_spatial_seed42: 训练失败 — unknown
- eval_smolvla_baseline_spatial_seed42_cqa1: 训练失败 — unknown
- eval_smolvla_official_baseline_spatial: 训练失败 — unknown
- eval_xvla_l2norm_k03_object_seed42_v2: 已被终止 — unknown
- eval_xvla_l2norm_k085_object_seed43: 已被终止 — unknown
- eval_xvla_random_k07_object_seed43: 训练失败 — unknown
- mvp_baseline: 训练失败 — unknown
- mvp_baseline_v2: 训练失败 — unknown
- mvp_baseline_v3: 训练失败 — unknown
- mvp_baseline_v4: 已被终止 — unknown
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "790dcd4a-6607-4659-a5a3-a960215f6b9a",
  "uuid": "070761a4-3f23-401c-bfdd-231ee52f4a1b",
  "tool_use_result": {
    "stdout": "- eval_oft_baseline_k10: 训练失败 — unknown\n- eval_oft_baseline_object_seed42: 已被终止 — unknown\n- eval_oft_baseline_object_seed42_v2: 训练失败 — unknown\n- eval_openvla_baseline_spatial_seed42: 训练失败 — unknown\n- eval_openvla_baseline_spatial_seed42_v2: 训练失败 — unknown\n- eval_openvla_baseline_spatial_seed42_v3: 训练失败 — unknown\n- eval_smolvla_baseline_spatial_seed42: 训练失败 — unknown\n- eval_smolvla_baseline_spatial_seed42_cqa1: 训练失败 — unknown\n- eval_smolvla_official_baseline_spatial: 训练失败 — unknown\n- eval_xvla_l2norm_k03_object_seed42_v2: 已被终止 — unknown\n- eval_xvla_l2norm_k085_object_seed43: 已被终止 — unknown\n- eval_xvla_random_k07_object_seed43: 训练失败 — unknown\n- mvp_baseline: 训练失败 — unknown\n- mvp_baseline_v2: 训练失败 — unknown\n- mvp_baseline_v3: 训练失败 — unknown\n- mvp_baseline_v4: 已被终止 — unknown",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  }
}
```

</details>

---
