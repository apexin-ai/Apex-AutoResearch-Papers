# 目录重命名安全性调查报告

**服务器**: bjb1-42106  
**调查时间**: 2026-05-14  
**目标**: 评估 `/root/structfuse` → `/root/structfuse-context` 重命名对运行中训练的影响

---

## 0. 发现：重命名已完成

调查发现目录重命名**已经执行**，当前状态：

```
/root/structfuse-context    # 实际目录（drwxr-xr-x）
/root/structfuse             # 符号链接 → /root/structfuse-context
```

两个训练进程的 cwd 均已指向 `/root/structfuse-context`：
- PID 73544: `/proc/73544/cwd -> /root/structfuse-context`
- PID 76627: `/proc/76627/cwd -> /root/structfuse-context`

---

## 1. 安全性判定：当前状态 — 安全 ✓

**符号链接 `/root/structfuse → /root/structfuse-context` 完全兜底了所有绝对路径引用。** 训练进程不会受影响。

关键依据：

| 检查项 | 结果 |
|--------|------|
| 进程 cwd | 均指向 `/root/structfuse-context` |
| 进程 fd（打开文件） | PID 73544: stdout/stderr → `/root/runs/structfuse-context/m2_full_qwen.log`（已用新路径）<br>PID 76627: wandb log → `/root/structfuse-context/wandb/...`（已用新路径） |
| 数据路径 | 全部在 `/root/autodl-tmp/structfuse/`，不受影响 |
| checkpoint 输出 | 全部在 `/root/autodl-tmp/structfuse/checkpoints/`，不受影响 |
| 日志输出 | `/root/runs/m2_full_qwen/` 和 `/root/runs/m2_full_starcoder/`，不受影响 |
| yaml/json/cfg 中的绝对路径 | 无 `/root/structfuse[^-]` 引用 |

**潜在风险点**：两个脚本中仍有绝对路径引用旧名称，但因符号链接存在，运行时可正常解析：

- `run_m2_full_qwen.sh:20` — `TRAIN_SCRIPT="/root/structfuse/training/train.py"`
- `run_m2_full_starcoder.sh:21` — `PROJECT_ROOT="/root/structfuse"`

脚本在每轮 run 的 loop 中使用 `python "${TRAIN_SCRIPT}"` 和 `python "${PROJECT_ROOT}/training/train.py"`，通过符号链接解析到正确位置，不会出错。

---

## 2. 仍引用 `/root/structfuse`（非 `-context`）的文件清单

### Shell 脚本
| 文件 | 行号 | 内容 |
|------|------|------|
| `run_m2_full_qwen.sh` | 20 | `TRAIN_SCRIPT="/root/structfuse/training/train.py"` |
| `run_m2_full_starcoder.sh` | 21 | `PROJECT_ROOT="/root/structfuse"` |

### Python 文件
| 文件 | 行号 | 内容 |
|------|------|------|
| `evaluation/linear_proxy.py` | 28 | `BM25_DIR = "/root/structfuse/mvp_data/bm25"` |
| `evaluation/linear_proxy.py` | 416 | `out_path = "/root/structfuse/evaluation/linear_proxy_results.json"` |
| `scripts/build_p2b_data.py` | 14 | `OUTPUT_DIR = "/root/structfuse/mvp_data/training_data"` |
| `scripts/eval_p2b.py` | 99 | `--model-name default="/root/structfuse/models/..."` |
| `scripts/eval_p2b.py` | 100 | `--val-file default="/root/structfuse/mvp_data/..."` |
| `scripts/eval_p2b_pooled.py` | 137 | `--model-name default="/root/structfuse/models/..."` |
| `scripts/eval_p2b_pooled.py` | 138 | `--val-file default="/root/structfuse/mvp_data/..."` |
| `scripts/run_50repo_overlap.py` | 26-27 | CodeQL query paths |
| `scripts/compute_full_z_percent.py` | 30 | `'/root/structfuse/results/...'` |
| `mvp_phase1.py` | 18 | `CODEQL_QUERIES = Path("/root/structfuse/...")` |
| `extraction/precompute_bm25.py` | 12-13 | REPOS_DIR / OUTPUT_DIR |

---

## 3. 建议方案

### 当前状态（方案 C 已就位）：符号链接兜底

重命名已完成且有符号链接，训练安全。**无需立即行动。**

### 后续清理（训练结束后）

训练跑完后，批量替换上述文件中的 `/root/structfuse/` → `/root/structfuse-context/`，然后删除符号链接：

```bash
# 批量替换（在 git repo 中操作）
sed -i 's|/root/structfuse/|/root/structfuse-context/|g' \
    run_m2_full_qwen.sh \
    run_m2_full_starcoder.sh \
    evaluation/linear_proxy.py \
    scripts/build_p2b_data.py \
    scripts/eval_p2b.py \
    scripts/eval_p2b_pooled.py \
    scripts/run_50repo_overlap.py \
    scripts/compute_full_z_percent.py \
    mvp_phase1.py \
    extraction/precompute_bm25.py

# 验证无遗漏
grep -rn '/root/structfuse[^-]' --include='*.py' --include='*.sh' .

# 确认后删除符号链接
rm /root/structfuse
```

### 是否可以现在删除符号链接？

**不行。** `run_m2_full_qwen.sh` 的 loop 每轮 run 都会重新解析 `TRAIN_SCRIPT="/root/structfuse/training/train.py"`，`run_m2_full_starcoder.sh` 每轮 run 都会解析 `PROJECT_ROOT="/root/structfuse"` 下的 `training/train.py`。删除符号链接会导致下一轮 run 找不到训练脚本而失败。
