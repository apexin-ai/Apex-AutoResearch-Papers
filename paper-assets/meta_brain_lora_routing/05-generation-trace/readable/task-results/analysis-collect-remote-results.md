# analysis collect remote results

**Meta-Brain: Perturbation-Diagnostic Routing of LoRA Experts for Parameter-E cient VLA Robustness** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_collect_remote_results_20260517T012912_result.json`
- **Structured JSON:** [`0cfcae1ce90b8112d515.json`](../../sessions/0c/0cfcae1ce90b8112d515.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 汇总

### 远程 GPU/进程状态

| GPU | 显存占用 | 进程 | 状态 |
|-----|----------|------|------|
| 0 | 1MiB (空闲) | — | idle |
| 1 | 8780MiB | PID 493569: r48 eval | **运行中**，sensor_noise 阶段遇到 FileNotFoundError |
| 2 | 16004MiB | PID 736113 + 748780: `collect_activations_v3_real_v2.py` | 运行中 |
| 3 | 1MiB (空闲) | — | idle |

**tmux**: 无活跃 session

---

### r48 eval 问题

正在跑 sensor_noise (第7/8类)，但命中了缺失文件错误：
```
FileNotFoundError: '/root/LIBERO-plus/libero/libero/init_files/libero_spatial/..._initstate_0.pruned_init'
```
已完成 6 类，sensor_noise 部分完成但有跳过的 episodes。

---

### 完整对比表（所有已收集结果）

| 扰动类型 | Baseline | Universal r16 | Universal r48 (partial) | Visual Expert | Physical Expert (oracle) | Physical Expert (r16) | Spatial Expert |
|----------|----------|---------------|------------------------|---------------|--------------------------|----------------------|----------------|
| **nominal** | 60.0% | **65.0%** | 56.7% | 55.0% | 58.3% | 61.7% | 60.0% |
| **background_textures** | 78.3% | 78.3% | 71.7% | **75.0%** | — | — | — |
| **objects_layout** | 58.8% | **67.6%** | 58.8% | — | — | — | 61.8% |
| **robot_initial_states** | 22.6% | 20.8% | 18.9% | — | 26.4% | **28.3%** | — |
| **camera_viewpoints** | 68.4% | **70.2%** | 64.9% | 71.9% | — | — | — |
| **light_conditions** | 56.7% | **71.7%** | 56.7% | 61.7% | — | — | — |
| **sensor_noise** | 65.5% | 65.5% | running... | **67.3%** | — | — | — |
| **OVERALL** | ~58.6% | **~62.7%** | ~54.5% (6类) | 66.1% (5类) | 43.4% (2类) | — | 60.6% (2类) |

---

### 关键发现

1. **Universal r16 全面优于 Baseline**：nominal +5pp, objects_layout +8.8pp, light_conditions +15pp
2. **Universal r48 反而退步**：所有指标低于 r16，甚至低于 baseline。过拟合迹象明显
3. **Expert oracle 在专属领域有优势**：Visual expert camera_viewpoints 71.9% > r16 70.2%；Physical expert r16 的 robot_initial_states 28.3% > baseline 22.6%
4. **Expert nominal 降低**：Visual expert nominal 仅 55.0%（vs baseline 60.0%），说明 expert LoRA 在非目标领域有负面影响

### 新数据（本次收集）

- Visual Expert Oracle 5pt 完整结果 ✓ (09:24完成)
- Spatial Expert 完整结果 ✓ (09:26完成)
- Physical Expert Oracle 完整结果 ✓ (08:46完成)
- r48 eval 仍在进行中（sensor_noise 阶段出错）
- GPU2 上有 activation 收集进程在运行

---
