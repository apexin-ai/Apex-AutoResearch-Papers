# c2_qw_n500 排查报告

**日期**: 2026-05-14 22:05 UTC
**服务器**: westd-22162

---

## Part A: 重复提交根因

### 当前进程全景（5 个 profiling 进程）

| PID | GPU | 模型 | 方法 | Output Dir | 启动方式 | 时间 |
|-----|-----|------|------|-----------|---------|------|
| 129684 | 0 | DeepSeek | importance | `/tmp/n500_smoke_test` | bare `bash -c` | 21:40 |
| 130124 | 0 | DeepSeek | importance | `profiling_output_n500_bf16_ds_imp_s015` | tmux `c2_n500_gpu0` | 21:41 |
| 130263 | 1 | DeepSeek | random | `profiling_output_n500_bf16_ds_rand_s015` | tmux `c2_n500_gpu1` | 21:41 |
| 131864 | 2 | Qwen | importance | `profiling_output_n500_bf16_qw_imp_s015` | screen `c2_qw_gpu2` | 21:52 |
| 132002 | 3 | Qwen | random | `profiling_output_n500_bf16_qw_rand_s015` | screen `c2_qw_gpu3` | 21:52 |

### 根因

**GPU 0 存在重复**: 烟雾测试（PID 129684）和正式实验（PID 130124）同时跑在 GPU 0 上。烟雾测试参数不同（max_new_tokens=512, max_problems=502, output 到 /tmp），是 setup worker 的验证步骤，未在正式提交前清理。两者 output dir 不同，**无数据污染**，但浪费 ~18GB 显存。

**GPU 2/3 未发现重复**: 当前各只有 1 个进程。

**三次独立提交的证据**:
1. `bash -c` 直接执行（21:40）— setup worker 烟雾测试
2. `tmux new-session`（21:41）— submit worker 提交 DeepSeek
3. `SCREEN -dmS`（21:52）— 另一个 worker 提交 Qwen（用了 screen 而非 tmux）

结论: **setup worker 留下了未清理的烟雾测试进程，submit worker 正常提交了正式实验。** 不是同一实验被提交两次，而是测试进程和正式进程并存。

### 建议操作

Kill 烟雾测试进程释放显存:
```bash
kill 129684
```

---

## Part B: Seed 检查

### 源码分析

`pacs/profiling/run_profiling.py` 第 53 行:
```python
SEED = 42
```

使用位置:
- L192: `torch.manual_seed(SEED)` — 控制模型随机性
- L203: `stratified_sample_math500(raw_data, seed=SEED)` — 控制数据采样
- L450: `bootstrap seed=SEED` — 控制统计重采样
- L504: `"seed": SEED` — 写入输出 metadata

**没有 `--seed` CLI 参数**，SEED=42 是硬编码常量。

### 结论

| 实验 | Seed | 来源 |
|------|------|------|
| c2_n500_deepseek | 42 | 源码硬编码 |
| c2_qw_n500 | 42 | 源码硬编码（同一份代码） |

**Seed 一致，无需重启。**

---

## 当前进度

| 实验 | 进度 | 预估总时间 |
|------|------|-----------|
| DeepSeek importance (GPU 0) | 22/500 | ~5h |
| DeepSeek random (GPU 1) | ~22/500 | ~5h |
| Qwen importance (GPU 2) | 15/500 | ~5.5h |
| Qwen random (GPU 3) | 15/500 | ~5.5h |

每个脚本包含 4 个 sparsity level（0.15/0.20/0.25/0.30）串行执行，当前都在第一个 s015 阶段。
