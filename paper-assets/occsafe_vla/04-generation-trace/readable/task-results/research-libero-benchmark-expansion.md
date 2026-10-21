# research libero benchmark expansion

**Does Auxiliary Spatial Supervision Make Vision-Language-Action Models Safer? A Factorial Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_libero_benchmark_expansion_20260527T155035_result.json`
- **Structured JSON:** [`cfc88e1e5c5dab14f179.json`](../../sessions/cf/cfc88e1e5c5dab14f179.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

信息收集完毕。以下是完整报告。

---

```
=== LIBERO Benchmark 扩展可行性报告 ===

1. 可用 Suite 列表

   Suite             | OXE Config | Transform | RLDS 数据 | Raw HDF5 | OCC Labels
   ------------------|------------|-----------|-----------|----------|------------
   libero_spatial    | ✅         | ✅        | ✅ 1.8G/16shard | ✅ /root/autodl-tmp/libero_datasets/libero_spatial | ✅ 9 task×50 demo
   libero_object     | ✅         | ✅        | ❌ 空壳 148K (32×4K) | ❌ 不存在 | ❌
   libero_goal       | ✅         | ✅        | ❌ 空壳 84K  | ❌ 不存在 | ❌
   libero_10         | ✅         | ✅        | ❌ 空壳 148K | ❌ 不存在 | ❌
   libero_90         | 仅 TASK_MAX_STEPS | ❌ 无 OXE config | ❌ | ❌ | ❌

   两台服务器 (10894, 34685) 状态完全一致：只有 libero_spatial 有实际数据。

2. 代码改动需求

   训练:
   - 切 dataset_name 即可 (--dataset_name libero_object_no_noops)
   - 需要对应的 dataset_statistics JSON (归一化参数)
   - OXE configs + transforms 已注册，无需代码改动

   Eval:
   - 切 --task_suite_name 即可
   - evaluate_safelibero.py 已支持 libero_spatial/object/goal/10/90
   - TASK_MAX_STEPS 已配好各 suite 的步数上限

   OCC Labels:
   - extract_occupancy.py 的 get_benchmark_info() 硬编码了 libero_spatial
   - 需改为参数化 suite 名 (约 3 行代码改动)
   - build_occ_index.py 也硬编码了 libero_spatial 路径

3. 数据下载/生成需求

   已有数据:
   - libero_spatial: RLDS ✅, raw HDF5 ✅, occ ✅ (完全就绪)

   缺失数据 (以 libero_object 为例):
   ① 下载 LIBERO raw HDF5 demos (从 LIBERO 官方)
      - 10 tasks × 50 demos, 约 2-5 GB
   ② regenerate_libero_dataset.py --libero_task_suite libero_object
      - 过滤 no-ops, 重渲染 256px → HDF5 no_noops
      - 需要 mujoco 渲染 (EGL), 预计 30-60 min
   ③ HDF5 → RLDS tfrecord 转换
      - 需要 RLDS dataset builder (LIBERO_Object/)
      - dlimp_openvla/rlds_converters/ 只有 bridge_dataset builder
      - 需要找到/创建 LIBERO 的 RLDS builder
      - 转换后需计算 dataset_statistics.json
   ④ OCC label 生成 (如果需要)
      - extract_occupancy.py 逐帧 mujoco 体素化, CPU 密集
      - ~10-30 ms/frame, 每 task 50 demo × ~100-200 frames
      - 10 tasks 预计 2-4 小时

4. OCC Label 生成

   流程: extract_occupancy.py --all → 逐 task 逐 demo 逐 frame:
   mujoco set_state → build_occupancy_3d (64³体素) → voxel_to_bev → 输出 (T,64,64) HDF5

   每个 suite: ~2-4 小时 (CPU-bound, 不需 GPU, 可后台运行)

   修改 extract_occupancy.py 支持新 suite:
   - get_benchmark_info() 中 benchmark.get_benchmark("libero_spatial") → 参数化
   - build_occ_index.py 同理

5. 推荐方案（按优先级）

   方案 A: 最快 — Vanilla-only 对比 (不需要 occ labels)
   - 只需 RLDS 训练数据 + eval
   - 仍需完成 ①②③ 流程, 最乐观 ~2-3 小时
   - 可验证: Vanilla baseline 在不同 suite 上的 TSR
   - 不能验证: gradient flow × norm type 交互效应

   方案 B: 完整 factorial 复现 (需要 occ labels)
   - 需完成 ①②③④, 加上 4 条件 × 训练时间
   - libero_object (10 task, 每 task 最多 280 step) 训练约 3-5h/条件
   - 总计 ~15-20h pipeline + training → 严重超 DDL

   方案 C: 利用已有 libero_spatial 数据做更多分析 (零数据准备)
   - 不同 seed 的 bootstrap CI
   - 更多 ablation (cutoff timing, loss weight)
   - 不算"扩展 benchmark"

   ★ 关键瓶颈: RLDS 转换
   - libero_object/goal/10 的 RLDS builder 不在代码库中
   - 只有 bridge_dataset 的 builder
   - 需要确认 openvla-oft 原始仓库是否提供 LIBERO RLDS builder
   - 或者 openvla-oft 团队是否有预转换的 RLDS 数据可直接下载

   ★ 建议立即确认:
   1. openvla-oft GitHub 是否提供预转换的 libero_object RLDS 数据
   2. 如果有，直接下载到两台服务器，跳过 ①②③
   3. OCC label 生成 (④) 可以在 34685 CPU 后台并行跑
```

---
