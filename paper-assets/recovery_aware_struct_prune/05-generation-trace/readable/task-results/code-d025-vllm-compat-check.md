# code d025 vllm compat check

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_d025-vllm-compat-check_20260515T092337_result.json`
- **Structured JSON:** [`ea73264aa3100ed1daa5.json`](../../sessions/ea/ea73264aa3100ed1daa5.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

所有信息已收集完毕。

---

## 产出报告

### 1. vLLM 兼容性结论：**不兼容**

- vLLM 0.18.1 已安装，但源码中**没有** `per_layer_intermediate_size` 支持
- 剪枝模型 `sft_rasp_20` 有非均匀 MLP：28 层 intermediate_size 从 8128 到 18944 不等
- vLLM 假设所有层 intermediate_size 相同，加载必定失败
- 另外 TRL 当前只支持 vLLM 0.11.0-0.17.1，0.18.1 也不在兼容范围内

### 2. 选择方案 B：无 vLLM，参数优化加速

### 3. v5 vs v4 参数对比

| 参数 | v4 | v5 | 说明 |
|------|-----|-----|------|
| `max_completion_length` | **2048** | **512** | GSM8K 解题 ~300 token 够用，2048 极度浪费 |
| `steps_per_generation` | _(未设)_ | **4** | 生成复用 4 步，生成开销摊薄 4x |
| `generation_batch_size` | _(未设)_ | _(可配)_ | 新增可选参数 |
| 其余参数 | 不变 | 不变 | beta=0.01, temp=0.4, rep_penalty=1.15 等全部保持 |

### 4. 预估加速比

- v4: **29 min/step** → 250 步 = **~120h (5 天)**
- v5 保守估计: **6-8 min/step** → 250 步 = **~25-33h (1-1.4 天)**
- 加速来源：
  - `max_completion_length 512`：生成长度上限缩短 4x → 生成阶段 ~2-4x 快
  - `steps_per_generation=4`：每 4 步才生成一次 → 生成开销摊薄 4x
  - 综合：**~4-5x 加速**

### 5. GPU 状态

| GPU | 进程 | 状态 |
|-----|------|------|
| cuda:0 | GRPO v4 (PID 339111) | 1/250 步，29min/step，100% util |
| cuda:1 | SFT standard_20 retrain (PID 239077) | 1145/1870 步 (61%)，~4s/step，**约 50 分钟后完成** |

### 6. Kill v4 + 启动 v5 命令（待审批）

```bash
# Step 1: Kill v4
kill 339111
# 等 5 秒确认退出
sleep 5 && nvidia-smi --query-compute-apps=pid,used_memory --format=csv,noheader

# Step 2: 启动 v5（通过 agent-ml submit_training_job 或手动）
source /root/miniconda3/etc/profile.d/conda.sh && conda activate base
cd /root/recovery_aware_struct_prune
bash scripts/run_grpo_stage2_v5_rasp.sh
```

### 7. 已创建文件

- `/root/recovery_aware_struct_prune/src/train_grpo_v5.py`
- `/root/recovery_aware_struct_prune/scripts/run_grpo_stage2_v5_rasp.sh`

**等待审批后执行 kill v4 + 启动 v5。** v4 只跑了 1 步，损失可忽略。

---
