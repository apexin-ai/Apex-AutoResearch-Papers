# ops westd kill eval and setup ragen eval

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_westd_kill_eval_and_setup_ragen_eval_20260522T090351_result.json`
- **Structured JSON:** [`08b1bd1b31a81bc60090.json`](../../sessions/08/08b1bd1b31a81bc60090.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

GPU 0 = 89.7 GB, 61% 利用率！Eval 正在积极运行。vLLM 生成中。测试成功启动！

总结：

### 产出

1. **所有 eval_checkpoint.py 进程已 kill** - 已杀掉 3 个 eval_checkpoint.py 进程 + 2 个孤立 vLLM::EngineCore (PID 478013, 489674)

2. **4 GPU 全部空闲后重新分配** - GPU 0 现在被 RAGEN eval 使用 (89.7 GB, 61%)，GPU 1/2/3 空闲

3. **RAGEN eval 启动方式**:
   ```bash
   cd /root/cost-verify-agent-rl/RAGEN && \
   python train.py --config-name &lt;config_name> [overrides...]
   ```
   关键点：
   - 使用 `train.py`（非 `ragen/eval.py`）作为入口，配合 `trainer.val_only: True` + `trainer.val_before_train: True`
   - 已有 OOD eval 专用配置文件（如 `_alfworld_sft_baseline_ood_eval_v2.yaml`、`_alfworld_exp029_seed5_ood_eval.yaml`）
   - GPU 可通过 hydra override 切换：`system.CUDA_VISIBLE_DEVICES="0"`

4. **先前 seed5/seed6 eval 参数**（从 config 文件确认一致）:
   - `agent_proxy.context_window_mode: full`
   - `agent_proxy.max_turn: 50`
   - `rollout.val_kwargs.temperature: 0.4, do_sample: True`
   - `es_manager.val.env_groups: 134` (134 OOD tasks, group_size=1)
   - `es_manager.val.env_configs.tags: ["AlfworldSG_OOD"]`

5. **测试 eval 成功启动**:
   - tmux session: `ragen_eval`
   - wandb run: `n6e4ylj1` (sft-baseline-ood-eval-v2)
   - Model: `qwen3_exp021_ragen_sft_v4` (1.72B params, Qwen3)
   - GPU 0, 89.7 GB, 61% 利用率，正在生成序列
   - 日志: `/root/autodl-tmp/logs/ragen_sft_ood_eval_test2.log`

---
