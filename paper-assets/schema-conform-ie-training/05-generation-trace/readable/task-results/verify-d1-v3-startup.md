# verify d1 v3 startup

**schema conform ie training** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_verify_d1_v3_startup_20260513T045748_result.json`
- **Structured JSON:** [`d168a11c542223ddb704.json`](../../sessions/d1/d168a11c542223ddb704.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 检查结果汇总

### 1. GPU 状态
| GPU | 利用率 | 显存占用 |
|-----|--------|----------|
| cuda:0 | 58% | 22,109 / 97,887 MiB (eval_C_v2) |
| cuda:1 | **100%** | **65,110 / 97,887 MiB** (D1 v3 训练) |

### 2. D1 v3 训练进程
**存活** — 实际 PID 为 **70714**（非 70696），CPU 占用 443%，12:54 启动，正常运行中。

### 3. Patch 部署
全部 5 项 **已确认**：
- `DYGIEPP_TO_SCHEMA_REL_TYPE` → data_utils.py:79, 287
- `mapped_type` → data_utils.py:287, 288
- `_normalize_relation` → rewards.py:106, 141, 147
- `_arg_similarity` → rewards.py:120, 150, 151
- `threshold: float = 0.3` → rewards.py:132

### 4. D1 v3 训练日志
- 模型加载成功：Qwen3.5-9B，trainable 1.28%（116M / 9B params）
- wandb offline 模式运行
- 当前 **step 1/500**，~115s/step（刚启动约 4 分钟）
- 进度条仅显示 step 1，尚无 reward 明细打印 — **需要等更多 step 后才能确认 f1_correctness 中 relation 贡献是否非零**
- 无报错

### 5. eval_C_v2 状态
**仍在跑**（PID 65560，11:12 启动）：
- **scierc_test 已完成**（551 samples）：
  - f1_correctness: **0.2184**
  - entity_f1: 0.3949
  - relation_f1: **0.0000**（base model 零 relation 识别能力）
  - structural_validity: 0.9964
  - type_conformance: 0.9537
- **crossner_politics 进行中**：440/651（68%），~5s/sample，预计 ~17 分钟后完成
- 之后还有 crossner_science 待跑

### 6. 僵尸进程
**无** — 仅有 jupyter、tensorboard、eval_C_v2、D1 v3 训练及 wandb 相关进程，另有旧的 D1 v2 bash wrapper（67210/67214）残留但无实际计算负载。

---
