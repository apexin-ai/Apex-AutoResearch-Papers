# π0.5 VLA-only Object seed43 冲突结果核实

## 结论

**v1 (98.5%) 不是 bug，v2 (86.5%) 才是无效结果。**

- v1/r4 (98.5%) — 使用 `--n_action_steps 10` action chunking，干净完成 200 个 rollout，与同设置下 s42=100%、s44=99.5% 一致
- v2 (86.5%) — 同样的命令，但运行中发生 **CUDA OOM**，第一个任务 alphabet_soup 整批失败 (0/20)，cream_cheese 也降到 70%，**应判废**
- r3 (81.5%) — 使用 closed-loop 评估（**没有** `--n_action_steps`），与同设置下 s42=82%、s44=81% 一致

r3 与 r4 的差距 (≈17 pp) 是**评估范式差异**（closed-loop vs chunked open-loop），不是 bug。π0.5 设计上就是以 10-step action chunk 做开环预测，加 `--n_action_steps 10` 后接近"原生"评估方式。

**建议：不要把 r4 改成 86.5%。** v2 已确认是 OOM 崩溃产物，不可作为有效结果替换 v1。

## 证据

### 三种结果的来源

| 实验 | 服务器 | 日志 | 参数 (关键) | 结果 |
|------|--------|------|------------|------|
| r4 (=v1) | bjb1-18228 | `/tmp/eval_pi05_seed43_r4.log` | `K=1, n_action_steps=10` | **98.5% (197/200)** ✓ 干净 |
| r4 同步副本 | bjb2-28827 | `logs/eval-pi05-vla-only-object-s43.log` | `K=1, n_action_steps=10` | **98.5% (197/200)** ✓ 干净 |
| v2 (重跑) | bjb2-28827 | `logs/eval-pi05-vla-only-object-s43-v2.log` | `K=1, n_action_steps=10` | **86.5% (173/200)** ✗ OOM |
| r3 | bjb1-32546 | `logs/eval-pi05-vla-only-object-seed43-r3.log` | `K=1`, 无 `n_action_steps` | **81.5% (163/200)** ✓ 干净 |

### v2 的失效证据

`eval-pi05-vla-only-object-s43-v2.log` 中明确出现：
```
torch.OutOfMemoryError: CUDA out of memory. Tried to allocate 20.00 MiB.
GPU 0 has a total capacity of 23.52 GiB of which 21.75 MiB is free.
Process 388316 has 12.44 GiB memory in use.
```
- alphabet_soup 任务在 OOM 中崩溃（log 中没有正常的 success rate 行，结果为 0/20）
- cream_cheese 在 OOM 阴影下只拿到 70% (14/20)
- 后 8 个任务 OOM 退散后基本 95-100%
- 累加：0 + 14 + 19 + 20 + 20 + 20 + 20 + 20 + 20 + 20 = 173/200 = 86.5% ✓ 与日志一致

→ v2 是 OOM 拉低的废结果，不是模型真实表现。

### 三个 seed 的横向一致性证明 r4 不是 bug

| Seed | r3 (无 chunking) | r4 (chunking=10) |
|------|-----------------|------------------|
| 42 | 82.0% (164/200) | **100.0% (200/200)** |
| 43 | 81.5% (163/200) | **98.5% (197/200)** |
| 44 | 81.0% (162/200) | **99.5% (199/200)** |

r4 在三个 seed 上都是 98.5-100%，方差很小。这不是单 seed 偶发——是 chunked 评估范式下的稳定行为。如果 r4 是 bug，不可能在三个独立 seed 上都触发同样的高分。

### per-task SR 对比 (s43)

| Task | r3 (closed-loop) | r4 (chunking) |
|------|-----------------|---------------|
| alphabet_soup | 80% | 90% |
| cream_cheese | 95% | 100% |
| salad_dressing | 70% | 100% |
| bbq_sauce | 85% | 100% |
| ketchup | 80% | 100% |
| tomato_sauce | 60% | 100% |
| butter | 95% | 100% |
| milk | 80% | 100% |
| chocolate_pudding | 100% | 100% |
| orange_juice | 70% | 95% |

chunking 模式下，原本中等难度的任务 (salad/tomato/milk) 都拉到 100%。这与 π0.5 的训练假设一致：模型输出 10-step action chunk，闭环 re-query 反而引入抖动。

## 建议处理

1. **保留 r4 的 metrics 不变 (98.5%)** — 不要按 Director 的建议改成 86.5%
2. **v2 的 86.5% 应明确标记为 INVALID/OOM**
3. 论文/对比时需要选定一个评估范式：
   - 若 baseline 表 (其他方法、其他 seed) 都是 closed-loop → 引用 r3 (81.5%)
   - 若改用 chunked 评估 → 全部 seed 重跑用 r4 设置（s42=100, s43=98.5, s44=99.5）
4. 注意：r3 和 r4 的 baseline 数字不能混用——评估范式必须保持一致

## Action

- 不更新 eval-pi05-vla-only-object-seed43-r4 的 metrics（保留 98.5%）
- 在 conclusion 中补一句注明评估范式
