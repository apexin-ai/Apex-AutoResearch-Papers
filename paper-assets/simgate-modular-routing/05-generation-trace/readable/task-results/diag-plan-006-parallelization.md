# diag plan 006 parallelization

**Death Avoidance as the Dominant Routing Signal: A Counterfactual Analysis on ScienceWorld** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diag_plan-006-parallelization_20260515T151519_result.json`
- **Structured JSON:** [`3b455e7367a4e18e9c5c.json`](../../sessions/3b/3b455e7367a4e18e9c5c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

信息收集完毕，以下是评估结果。

---

## 当前进度

| Task | 状态 | Episodes |
|------|------|----------|
| identify-life-stages-1 | ✅ 完成 | 20/20 |
| lifespan-longest-lived | ⏳ 进行中 | 12/20 |
| find-non-living-thing | 未开始 | 0/20 |
| lifespan-longest-lived-then-shortest-lived | 未开始 | 0/20 |
| inclined-plane-determine-angle | 未开始 | 0/20 |
| chemistry-mix | 未开始 | 0/20 |

GPU 状态：GPU0 完全空闲（0 MiB），GPU1 满载（28013/32607 MiB）。

## 并行化可行性

**可以并行。** 三个关键点：

1. **`--task_types` 支持指定子集** — 逗号分隔，脚本按顺序遍历
2. **VLLM 支持双实例** — `LLMAgent` 通过 `CUDA_VISIBLE_DEVICES` 隔离 GPU，两个进程分别用 GPU0/GPU1，互不干扰（`tensor_parallel_size=1`，无端口冲突，vLLM 用进程内引擎而非 HTTP server）
3. **ScienceWorld 无共享资源** — 每次 `create_env()` 启动独立 JVM（py4j），无端口或状态冲突

## 并行化方案

**需要先 kill 当前进程**，否则 GPU1 进程会继续跑所有 6 个 task，和 GPU0 产生文件冲突。

脚本的 `--reuse_dirs` 参数可以扫描已有数据、自动跳过已完成 task 并续跑未完成的 task（deep_internal 模式下以 append 方式写文件）。

### 操作步骤

**Step 1: Kill 当前进程**
```bash
kill 485807
```

**Step 2: 启动 GPU1（续跑 + 前半段未开始的 task）**
```bash
cd /root/autodl-tmp/simgate-modular-routing && \
CUDA_VISIBLE_DEVICES=1 nohup python src/episode_level_collection.py \
    --task_types 'lifespan-longest-lived,find-non-living-thing,lifespan-longest-lived-then-shortest-lived' \
    --episodes 20 --gpu_id 0 --output_dir results/plan-006-deep-internal \
    --deep_internal --seed 42 \
    --reuse_dirs results/plan-006-deep-internal \
    > /tmp/plan006_gpu1.log 2>&1 &
```
- lifespan-longest-lived：扫描到 12 条已有数据，只收集剩余 8 条
- find-non-living-thing + lifespan-longest-lived-then-shortest-lived：各 20 条
- 合计 **48 episodes**

**Step 3: 启动 GPU0（后半段 task）**
```bash
cd /root/autodl-tmp/simgate-modular-routing && \
CUDA_VISIBLE_DEVICES=0 nohup python src/episode_level_collection.py \
    --task_types 'inclined-plane-determine-angle,chemistry-mix' \
    --episodes 20 --gpu_id 0 --output_dir results/plan-006-deep-internal \
    --deep_internal --seed 42 \
    > /tmp/plan006_gpu0.log 2>&1 &
```
- 合计 **40 episodes**

### 关键说明
- 两个进程写入同一 `output_dir`，但操作不同 task 子目录，无文件冲突
- `--gpu_id 0` 在两个命令中都是 0，因为 `CUDA_VISIBLE_DEVICES` 已经隔离了物理 GPU，进程内只看到 1 块卡
- identify-life-stages-1 已完成，无需重跑
- Seed 保持 42，variation_idx 分配 (`ep_idx % max_var`) 与原始单进程一致

### 预期加速
- 原方案：88 episodes 串行 → 瓶颈在 GPU1 的 48 episodes
- **加速约 1.8x**

是否执行？

---
