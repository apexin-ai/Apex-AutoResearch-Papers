# code exp012b fix and submit

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_exp012b-fix-and-submit_20260514T063237_result.json`
- **Structured JSON:** [`a5e4217be6a22d32f203.json`](../../sessions/a5/a5e4217be6a22d32f203.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

timeout 已经杀干净了，Ray 没有残留进程。

---

## 汇报

### 1. D010 代码修复状态 ✅
- **env.py**: `reward = self.config.score * float(won)` — 纯二值 reward，正确
- **config `format_penalty`**: `0` — 正确
- **config `group_size`**: `16`（train）/ `1`（eval）— 正确

### 2. vLLM `disable_mm_preprocessor_cache` 参数 ✅ 无需修复
- 仅存在于 `ragen/llm_agent/ap_webshop.py:57`（webshop 专用）
- `agent_proxy.py` 和 `train.py` 调用链中**不包含此参数**
- alfworld config 也不涉及 webshop
- **train.py 入口不会触发此 TypeError**

### 3. Dry-run 结果 ✅ 通过
- 配置解析成功，total_training_steps=30
- 训练集 3553 games，验证集 140 games 加载完成
- 从 `exp008_grpo/global_step_5` resume 成功（model/optimizer/rng/lr_scheduler 双 Rank 均加载）
- AlfredTWEnv 初始化启动
- vLLM engine 初始化完成（enforce eager, NCCL 2.27.5）
- **0 Traceback / TypeError / Error**
- 进程被 `timeout 120` 正常终止

### 4. 正确启动命令
```bash
source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && \
export TMPDIR=/root/autodl-tmp/tmp/ && mkdir -p $TMPDIR && \
export ALFWORLD_DATA=/root/autodl-tmp/alfworld && \
export CUDA_VISIBLE_DEVICES=0,1 && \
cd /root/cost-verify-agent-rl/RAGEN && \
python train.py --config-name _alfworld_exp012_reward_fix
```

可以提交 exp012b。

---
