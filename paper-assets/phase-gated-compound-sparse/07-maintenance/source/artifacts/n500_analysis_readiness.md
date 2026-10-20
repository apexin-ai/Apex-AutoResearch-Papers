# n=500 分析脚本预验证报告

**时间**: 2026-05-15 12:00 UTC
**服务器**: westd-22162

## 1. 脚本状态

| 项目 | 状态 |
|------|------|
| 脚本路径 | `/root/autodl-tmp/pacs/analyze_n500_unified.py` |
| 文件大小 | 26519 bytes |
| 最后修改 | 2026-05-15 08:05 |
| 依赖 (scipy, numpy, json, csv, pathlib) | 全部满足 |
| `--help` 可执行 | OK |
| dry-run 测试 (`--dry-run --csv`) | 成功，输出 JSON + CSV |

**用法**: `python analyze_n500_unified.py [--model {deepseek,qwen,all}] [--dry-run] [--csv] [--latex]`

## 2. 数据文件状态

### 已完成 (12/16)

| 条件 | profiling_results.json |
|------|----------------------|
| `profiling_output_n500_bf16_ds_imp_s015` | done |
| `profiling_output_n500_bf16_ds_imp_s020` | done |
| `profiling_output_n500_bf16_ds_imp_s025` | done |
| `profiling_output_n500_bf16_ds_rand_s015` | done |
| `profiling_output_n500_bf16_ds_rand_s020` | done |
| `profiling_output_n500_bf16_ds_rand_s025` | done |
| `profiling_output_n500_bf16_qw_imp_s015` | done |
| `profiling_output_n500_bf16_qw_imp_s020` | done |
| `profiling_output_n500_bf16_qw_imp_s025` | done |
| `profiling_output_n500_bf16_qw_rand_s015` | done |
| `profiling_output_n500_bf16_qw_rand_s020` | done |
| `profiling_output_n500_bf16_qw_rand_s025` | done |

### 进行中 (4/16) — s030 全部在跑

| 条件 | 进度 | GPU |
|------|------|-----|
| `n500_bf16_qw_imp_s030` | 303/500 (~60%) | GPU 0 (screen c2_qw_gpu2) |
| `n500_bf16_qw_rand_s030` | 294/500 (~59%) | GPU 0 (screen c2_qw_gpu3) |
| `n500_bf16_ds_rand_s030` | 128/500 (~26%) | GPU 1 (tmux c2_n500_gpu1) |
| `n500_bf16_ds_imp_s030` | 82/500 (~16%) | GPU 0 (tmux c2_n500_gpu0) |

### 数据文件路径模式
```
/root/autodl-tmp/pacs/profiling_output_n500_bf16_{ds,qw}_{imp,rand}_{s015,s020,s025,s030}/profiling_results.json
```

## 3. 进程 / Session 状态

**Screen sessions** (2):
- `c2_qw_gpu2` — qw_imp_s030
- `c2_qw_gpu3` — qw_rand_s030

**Tmux sessions** (2):
- `c2_n500_gpu0` — ds_imp_s030
- `c2_n500_gpu1` — ds_rand_s030

**后台监控**: `check_completion_loop.sh` (PID 162290) 在运行

## 4. 运行命令（实验完成后）

```bash
source /root/miniconda3/etc/profile.d/conda.sh && conda activate base
cd /root/autodl-tmp/pacs
python analyze_n500_unified.py --model all --csv --latex
```

输出: `analysis_output/n500_unified.json` + `analysis_output/n500_unified.csv`

## 5. 潜在问题

- **无阻塞问题**: 脚本、依赖、已有数据均正常，dry-run 通过
- **等待 s030**: Qwen s030 预计还需 ~2-3h，DeepSeek s030 预计还需 ~5-6h
- `analysis_output/` 目录已存在（dry-run 时自动创建）
