# 诊断报告：plan_001_flat_nli_scoring

## 根因

**模块路径错误 + 缺少必选参数**。启动命令 `python -m freige.training.rsft_score_filter` 立即失败：`freige/training/` 包下只有空 `__init__.py`，实际脚本在项目根的 `training/rsft_score_filter.py`。此外 `--input_dir` 和 `--output_path` 两个必选参数均未传入。进程每次启动即崩溃，cron 检测到 5 次死亡。

## 日志证据

### 1. 无日志文件

```
$ ls ~/runs/faith-evidence-ie/plan_001_flat_nli_scoring.log
No such file or directory
```

预期日志不存在——进程启动即失败，且 stderr 未重定向到日志文件。

### 2. 模块不存在

```
$ python -m freige.training.rsft_score_filter --help
/root/miniconda3/bin/python: No module named freige.training.rsft_score_filter
```

### 3. 包结构确认

```
$ ls /root/autodl-tmp/freige/freige/training/
__init__.py   __pycache__/
# (空包，无 rsft_score_filter.py)

$ ls /root/autodl-tmp/freige/training/rsft_score_filter.py
# (文件在这里，正确模块路径是 training.rsft_score_filter)
```

### 4. 正确路径可用

```
$ python -m training.rsft_score_filter --help
usage: rsft_score_filter.py [-h] --input_dir INPUT_DIR --output_path OUTPUT_PATH [--scoring_mode {ced,flat_nli}] ...
```

需要 `--input_dir` 和 `--output_path` 两个必选参数。

### 5. 附：rsft_score_filter.log（另一次手动运行）

`~/runs/faith-evidence-ie/rsft_score_filter.log` 是另一次运行的日志，在 11500/21728 处无 traceback 中断（被外部 kill，可能 OOM 或手动终止），与本次 plan_001 cron 任务无关。

## 当前状态

**评分任务实际上已由分 shard 运行完成。** 4 个 shard 均成功产出：

| Shard | 总记录 | 选中 | 选中率 |
|-------|--------|------|--------|
| s0 | 5,560 | 687 | 12.4% |
| s1 | 5,552 | 688 | 12.4% |
| s2 | 5,568 | 689 | 12.4% |
| s3 | 5,272 | 655 | 12.4% |
| **合计** | **21,952** | **2,719** | **12.4%** |

输出位于 `/root/autodl-tmp/rsft_scored_s{0,1,2,3}/rsft_train.jsonl`。

## 修复建议

如需重跑（合并为单次运行），修正命令为：

```bash
cd /root/autodl-tmp/freige && \
python -m training.rsft_score_filter \
  --scoring_mode flat_nli \
  --input_dir /root/autodl-tmp/rsft_generations \
  --output_path /root/autodl-tmp/rsft_scored_plan001 \
  --top_k 3 \
  --f1_threshold 0.1 \
  2>&1 | tee ~/runs/faith-evidence-ie/plan_001_flat_nli_scoring.log
```

关键修改：
1. `freige.training.rsft_score_filter` → `training.rsft_score_filter`
2. 补上 `--input_dir` 和 `--output_path`
3. 重定向日志到预期路径

但 **如果下游只需要评分结果，分 shard 产出已可直接使用**，合并 4 个 `rsft_train.jsonl` 即可，无需重跑。
