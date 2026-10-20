# ops gpu check and cleanup

**Phase-Modulated Compound Sparsity Severity in 7B-Scale Mathematical Reasoning Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_gpu_check_and_cleanup_20260514T153339_result.json`
- **Structured JSON:** [`9dd169a7dd8df6a959fd.json`](../../sessions/9d/9dd169a7dd8df6a959fd.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部数据收集完毕。汇报如下：

---

## GPU 实际占用

| GPU | 进程 | PID | 显存 | 实验 |
|-----|------|-----|------|------|
| **0** | DeepSeek imp s015 | 130124 | 26854 MiB | c2_n500_deepseek |
| **1** | DeepSeek rand s015 | 130263 | 30598 MiB | c2_n500_deepseek |
| **2** | Qwen imp s015 | 131864 | 27824 MiB | c2_qw_n500 |
| **2** | **Llama imp s020** | **142944** | **20228 MiB** | **c3_llama** |
| **3** | Qwen rand s015 | 132002 | 28436 MiB | c2_qw_n500 |
| **3** | **Llama rand s020** | **142708** | **20386 MiB** | **c3_llama** |

每张卡 97GB 总量。GPU 2 用了 48066 MiB (49%), GPU 3 用了 48836 MiB (50%)。显存没有爆，但 GPU 利用率 89%/93%——**c2_qw_n500 和 c3_llama 确实在争抢 GPU 2+3 的算力**。

## GPU 争抢影响

- 显存层面：尚有余量，不会 OOM
- 算力层面：两个实验共享计算单元，互相拖慢。c3_llama 命令行没传 `--gpu` 参数，默认吃了 GPU 2+3（和 c2_qw 撞上）

## 重复进程

PID 132389, 132392 **已不存在**（ps 返回 exit code 1），无需手动 kill。

## 实验进度

| 实验 | 子任务 | 进度 | GPU |
|------|--------|------|-----|
| c2_n500_deepseek | imp s015 | **197/500** (39%) | 0 |
| c2_n500_deepseek | rand s015 | **221/500** (44%) | 1 |
| c2_qw_n500 | imp s015 | **170/500** (34%) | 2 |
| c2_qw_n500 | rand s015 | **176/500** (35%) | 3 |
| c3_llama | importance s020 | **3/50** (6%) | 2 |
| c3_llama | random s020 | **4/50** (8%) | 3 |

## 数据污染判断

**无污染风险。** 脚本在完成全部问题后才写入单个 `profiling_results.json`，当前所有 n500 输出目录均为空。重复进程在写入前已死亡。

## 需要决策

c3_llama (50 题，刚开始) 和 c2_qw_n500 (500 题，约 1/3) 共享 GPU 2+3，互相减速。选项：
1. **杀掉 c3_llama** (PID 142944, 142708)，等 c2_qw 跑完后再重启——c2_qw 还需很久，优先保证它的速度
2. **保持现状**——显存够用，c3_llama 只有 50 题会先跑完，之后 c2_qw 独占
3. **杀掉 c3_llama 并迁移到 GPU 0 或 1**——但那两张卡也在跑 c2_deepseek

建议选 2：c3_llama 50 题量小，估计 1-2 小时内完成，之后 GPU 2+3 自动释放给 c2_qw。

---
