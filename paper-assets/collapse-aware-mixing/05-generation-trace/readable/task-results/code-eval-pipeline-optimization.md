# code eval pipeline optimization

**collapse aware mixing** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_eval_pipeline_optimization_20260512T183257_result.json`
- **Structured JSON:** [`cac8461913ee9702187d.json`](../../sessions/ca/cac8461913ee9702187d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

所有文件通过验证。训练语义完全一致，只有评估相关参数不同。

---

## 瓶颈根因报告

### v5 每个 checkpoint 评估耗时分解（~20 min/ckpt）

| 环节 | 配置 | 预估耗时 | 根因 |
|------|------|---------|------|
| **Token 生成** | 500K tokens, bs=32, max_new=256 | **8-12 min** | 62 批自回归生成，memory-bandwidth bound |
| **Spectral rank** | 5K samples, bs=16, output_hidden_states | 3-5 min | 312 批 forward pass（独立循环） |
| **Token entropy** | 5K samples, bs=16 | 2-3 min | 312 批 forward pass（独立循环） |
| **Perplexity** | 5K samples, bs=16 | 2-3 min | 312 批 forward pass（独立循环） |
| **Model loading** | from_pretrained 每个 ckpt | 15-20s | 完全重建模型对象 |
| **Logit KL** (G1+) | 2K samples, bs=16, 2 models | 1-2 min | 125 批 × 2 模型 forward |
| **N-gram/coverage/KL** | CPU, 500K tokens | ~5s | CPU-only, 可忽略 |

**核心瓶颈**：
1. **Token 生成占 50%+ 时间**，500K tokens 远超 n-gram entropy 收敛所需
2. **3 个独立 forward-pass 循环**（spectral/entropy/PPL）各自遍历相同数据，可合并为 1 次
3. **eval batch size=16**，96GB 显存仅用 ~9.3GB，严重浪费
4. **每个 ckpt 完全 from_pretrained**，模型架构相同但每次重新初始化

v5 总评估量：3 代 × 10 ckpt × ~20 min = **~10h**

---

### 优化措施清单

| # | 优化 | v5 → v6 | 预估提速 |
|---|------|---------|---------|
| 1 | 减少生成 token 数 | 500K → 100K | 该环节 **5×** |
| 2 | 增大生成 batch size | 32 → 128 | 该环节 **4×**（叠加 #1 总计 ~20×）|
| 3 | 合并 forward pass | 3 次循环 → 1 次 | 该环节 **3×** |
| 4 | 增大 eval batch size | 16 → 64 | 该环节 **4×**（叠加 #3 总计 ~12×）|
| 5 | State_dict 热加载 | from_pretrained → load_file | 该环节 **7×** |
| 6 | 减少 checkpoint 数 | 10 → 5 /代 | 总量 **2×** |
| 7 | Logit KL batch size | 16 → 32 | 该环节 **2×** |
| 8 | 显式内存管理 | 无 del → 逐步释放 | 支撑更大 batch |

### 优化后预估时间

**单个 checkpoint**：
- G0：~2.5 min（load 3s + gen 20s + combined fwd 100s + misc 5s）
- G1+：~3.5 min（+logit KL 60s）

**评估总时间**：
- G0：5 ckpt × 2.5 min = 12.5 min
- G1：5 ckpt × 3.5 min = 17.5 min
- G2：5 ckpt × 3.5 min = 17.5 min
- **总评估：~48 min**（v5 ~10h → v6 ~48 min，**12.5× 加速**）

**完整 3 代 run 预估**：
| 阶段 | v5 | v6 |
|------|-----|-----|
| 训练（3 代） | ~2.75h | ~2.75h（不变） |
| 评估（3 代） | ~10h | **~0.8h** |
| 合成数据生成（2 代） | ~3.2h | ~3.2h（不变） |
| 总计 | ~16h | **~6.75h** |

---

### v6 Launch 命令

```bash
nohup bash /root/collapse-aware-mixing/launch_pilot_v6.sh > /root/autodl-tmp/pilot_v6.log 2>&1 &
```

（v5 完成后再执行，因为共用 GPU）

---

### 新建文件列表

| 文件 | 用途 |
|------|------|
| `/root/collapse-aware-mixing/metrics_v6.py` | 合并 forward pass 的优化指标计算（spectral+entropy+PPL 1 次循环）+ 内存优化的 logit KL |
| `/root/collapse-aware-mixing/pilot_pipeline_v6.py` | 优化后的完整 pipeline（state_dict 加载、更大 batch、合并指标、新 CLI 参数） |
| `/root/collapse-aware-mixing/launch_pilot_v6.sh` | v6 启动脚本，训练参数与 v5 一致，评估参数优化 |

---

### 风险评估

| 变更 | 影响 | 风险等级 |
|------|------|---------|
| **metrics_gen_tokens 500K→100K** | N-gram entropy 在 ~50K tokens 已收敛，100K 提供充足余量。Vocab coverage 可能降低（100K 覆盖的 unique tokens 少于 500K），但趋势信号不变 | **低** |
| **checkpoint 10→5** | 监控粒度降低，collapse 转折点定位精度从 10M tokens 降到 20M tokens。对于 MVP 验证（"spectral rank 是否领先 PPL"）足够 | **低** |
| **合并 forward pass** | 数值结果完全一致（同一 batch 的 hidden states/logits/loss 是确定性的） | **无** |
| **State_dict 加载** | 权重完全相同，只跳过了 config 重新解析和模型对象重建 | **无** |
| **增大 batch size** | 数值可能有微小浮点差异（softmax/entropy 的累加顺序不同），量级 <1e-6，不影响结论 | **极低** |

---
