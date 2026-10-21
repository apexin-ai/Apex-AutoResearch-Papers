# infra exp006 final dryrun

**Generational Depth Estimation of Recursive Synthetic Text: Measuring the Discrimination Boundary** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_infra_exp006_final_dryrun_20260513T163156_result.json`
- **Structured JSON:** [`82150943d6612033bb18.json`](../../sessions/82/82150943d6612033bb18.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**lm-eval dry-run 通过。** HellaSwag 评测成功，batch_size auto=64。

---

## exp-006 dry-run 结果汇总

### 1. run_exp006.sh 关键配置
| 参数 | 值 |
|------|-----|
| MODEL | `/root/autodl-tmp/.hf_cache/Qwen/Qwen2.5-1.5B-Instruct/Qwen/Qwen2___5-1___5B-Instruct` (1544M params, bf16) |
| DATA_DIR | `data/` (depth_0-5.jsonl + features.csv, 30000 samples) |
| OUTPUT_DIR | `outputs/exp006/` (自动创建) |
| Strategies | no-filter, binary-ours, binary-drayson, graduated, surprisal, dsir (6种) |
| Seeds | 42, 123, 456, 789, 1024 (5个) |
| Alphas | 0.1, 0.3, 0.5, 0.7, 0.9 (graduated only) |
| **Total runs** | **50** (~25min/run, 预计 ~21h) |

### 2. lm-eval 任务
- `mmlu`: 可用，数据集已缓存（val=1531, test=14042）
- `hellaswag`: 可用，数据集已缓存（val=10042）

### 3. dry-run 逐步结果
| 步骤 | 状态 | 说明 |
|------|------|------|
| Filtering | **PASS** | 4种策略验证通过，30000 samples 正确加载 |
| Model loading | **PASS** | 本地路径加载 1544M params，bf16 |
| lm-eval | **PASS** | hellaswag limit=2 完成，auto batch_size=64 |

### 4. 磁盘空间
- `/root/autodl-tmp`: **137GB 可用** / 150GB（9% used）
- 项目占 353MB，预估 exp-006 全部 adapter + eval 结果 ~3GB，**充足**

### 5. 发现并修复的问题（3个）
1. **MODEL 路径**：原值 `"Qwen/Qwen2.5-1.5B-Instruct"` 会触发网络下载（hub 缓存无此模型，是 modelscope 结构）→ **已改为本地绝对路径**
2. **缺少 network_turbo + 环境变量**：脚本未 source network_turbo，评测数据集下载会失败 → **已添加**
3. **HF_ENDPOINT=hf-mirror.com 阻塞数据集下载**：mirror 对数据集下载卡死 → **已移除**（模型已是本地路径，不需要 mirror）

### 6. 结论
**exp-006 可以无阻塞启动。** 所有关键组件验证通过，3 个阻塞性问题已修复。GPU 当前 4.6GB/24.5GB，exp-003 结束后全部可用。

---
