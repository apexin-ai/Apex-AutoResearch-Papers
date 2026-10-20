# SWE-bench Per-Test Data Pipeline 技术方案

## 1. 目标

从 SWE-bench Verified 构建 `(code_patch, individual_test) → pass/fail` 训练数据，验证假说 D007：classification vs generation 的优势在 repo-level 复杂度下才显现。

当前函数级数据（HumanEval/MBPP, 19K samples）上 classification ≈ generation（87.5% vs 87.51%），差异 <0.2pp。需要 repo-level 数据打破僵局。

---

## 2. 数据构建流程

### 2.1 获取 SWE-bench Verified 数据

```python
from datasets import load_dataset
ds = load_dataset("princeton-nlp/SWE-bench_Verified", split="test")
# 500 instances, 每条包含:
#   instance_id: str        (e.g. "django__django-16379")
#   repo: str               (e.g. "django/django")
#   base_commit: str        (检出的 commit hash)
#   patch: str              (gold patch diff)
#   test_patch: str         (验证测试的 diff)
#   FAIL_TO_PASS: str       (JSON list of test names)
#   PASS_TO_PASS: str       (JSON list of test names)
#   hints_text: str
#   created_at: str
#   version: str
#   environment_setup_commit: str
```

### 2.2 Docker 执行环境

使用 SWE-bench 官方 Docker harness（`swebench.harness`）：

```bash
pip install swebench
```

官方 harness 工作流：
1. 根据 `instance_id` 拉取/构建对应的 Docker 镜像（`swebench/sweb.eval.<repo>.<version>:latest`）
2. 在容器内检出 `base_commit`，应用 patch，运行测试
3. 收集 test results（JSON 格式，per-test pass/fail）

关键 API：
```python
from swebench.harness.run_evaluation import run_instances
from swebench.harness.test_spec import make_test_spec

# 构建 test spec
test_spec = make_test_spec(instance)

# 运行评估（会自动构建 Docker 容器、应用 patch、执行测试）
run_instances(
    predictions=[{"instance_id": id, "model_patch": patch}],
    instances=[instance],
    ...
)
```

### 2.3 生成 Wrong Patches

对每个 instance，需要生成多个错误 patch 以构建 negative 样本。

**变异源**：

| 来源 | 方法 | 预期 patches/instance |
|------|------|----------------------|
| Gold patch 变异 | 在 gold patch 上应用变异策略 | 4-8 |
| LLM 生成的错误 patches | 从 SWE-bench leaderboard 提交中收集 | 5-15 |
| 部分修复 | 只应用 gold patch 的部分 hunks | 1-3 |

### 2.4 Per-test 结果收集

对每个 `(instance, patch)` 组合：
1. 在 Docker 容器中应用 patch
2. 分别运行 FAIL_TO_PASS 和 PASS_TO_PASS 中的每个测试
3. 记录每个测试的：
   - pass/fail 状态
   - 错误信息（stderr/traceback，truncated to 500 chars）
   - 执行时间

```python
# 伪代码：per-test 收集
for test_name in fail_to_pass + pass_to_pass:
    result = run_single_test(container, test_name)
    record = {
        "instance_id": instance_id,
        "patch": patch_diff,
        "test_name": test_name,
        "test_type": "f2p" or "p2p",
        "passed": result.passed,
        "error_message": result.stderr[:500] if not result.passed else "",
        "execution_time_s": result.time
    }
```

---

## 3. 变异策略对比与推荐

### 方案 A: 合成变异

沿用 `build_data.py` 的 5 种变异策略，但适配 diff patch 格式：
- **operator_swap**: 在 patch 的 `+` 行中替换运算符
- **off_by_one**: 在 patch 的 `+` 行中移位整数字面量
- **return_value**: 修改 patch 中的返回值
- **boundary_removal**: 删除 patch 中的边界检查
- **variable_swap**: 替换 patch 中的变量名

**优点**: 可控、确定性、低成本
**缺点**: 变异太"假"——真实 LLM bug 不是简单的运算符替换。模型可能学到 shortcut（检测变异模式而非理解语义）

### 方案 B: 真实 LLM Patches

从以下来源收集模型生成的错误 patches：

1. **SWE-bench leaderboard 提交**: 多个 agent（Devin, AutoCodeRover, SWE-agent 等）的公开提交记录
2. **自行生成**: 用不同 LLM（GPT-4o, Claude, Qwen）生成 patches，部分会失败
3. **CoderForge / OpenHands trajectories**: 公开的 agent trajectory 数据

**优点**: 真实错误分布、错误多样性高、与实际部署场景一致
**缺点**: 收集成本高、patch 数量不均（热门 instance 多，冷门少）

### 方案 C: 混合（推荐）

```
每个 instance 的 patch 组成:
  1× gold patch (label: 各测试应有的真实标签)
  4× 合成变异 (基于 gold patch)
  ~8× LLM patches (从公开来源收集，可用则用)
  2× 部分修复 (gold patch 的 subset hunks)
  ≈ 15 patches/instance
```

**推荐理由**:
- 合成变异保底：确保每个 instance 都有足够 negative 样本，不依赖外部数据可用性
- LLM patches 提升真实性：反映实际部署场景的错误分布
- 部分修复覆盖 "almost right" 场景：这是 repair verifier 最需要判别的 case
- 混合策略下模型难以学到单一 shortcut

**LLM patch 收集优先级**:
1. SWE-bench 官方 predictions 目录——多个 agent 的 `.jsonl` 提交
2. SWE-bench-docker 的缓存结果
3. 自行用 Claude/GPT 生成（成本可控，每 instance ≈ $0.10）

---

## 4. Docker 执行细节

### 4.1 SWE-bench Docker Harness

SWE-bench 官方提供两种执行方式：

**方式 1: 官方 Python API（推荐）**
```python
from swebench.harness.run_evaluation import main as run_evaluation

run_evaluation(
    dataset_name="princeton-nlp/SWE-bench_Verified",
    predictions_path="predictions.jsonl",
    max_workers=4,        # 并行 Docker 容器数
    run_id="pertest_v1",
    timeout=300,          # 每个 instance 超时 (秒)
)
```

**方式 2: CLI**
```bash
python -m swebench.harness.run_evaluation \
    --dataset_name princeton-nlp/SWE-bench_Verified \
    --predictions_path predictions.jsonl \
    --max_workers 4 \
    --run_id pertest_v1
```

### 4.2 修改 harness 以收集 per-test 结果

官方 harness 返回 instance 级别的 resolved/unresolved，需要修改以获取 per-test 结果。

关键修改点（`swebench/harness/test_spec.py` 和 `grading.py`）：
- 解析 pytest/unittest output 获取每个 test case 的独立 pass/fail
- 官方 `get_eval_report()` 已返回 per-test 状态，只需确保输出包含 error messages

实际上 SWE-bench harness 的 `get_eval_report()` 已经返回：
```python
{
    "instance_id": "...",
    "FAIL_TO_PASS": {"test_name_1": "PASSED", "test_name_2": "FAILED"},
    "PASS_TO_PASS": {"test_name_3": "PASSED", ...}
}
```

所以 per-test 信息已有，只需额外捕获 error messages（从 Docker 容器日志中提取）。

### 4.3 执行时间估算

| 阶段 | 每 instance 耗时 | 500 instances 总计 |
|------|------------------|-------------------|
| Docker 镜像构建（首次） | 3-10 min | ~30h（可缓存） |
| 镜像拉取（已有 cache） | 0-30 sec | ~2h |
| 单个 patch 测试执行 | 30s-5min | — |
| 每 instance 15 patches × 执行 | ~15-30 min | ~125-250h 串行 |

**并行化**：4 并行容器 → ~31-62h wall-clock；8 并行 → ~16-31h

### 4.4 并行化策略

```python
# 按 instance 粒度并行（而非 patch 粒度），避免 Docker 镜像重复构建
from concurrent.futures import ProcessPoolExecutor

def process_instance(instance, patches):
    """在同一个容器内依次测试多个 patches"""
    container = build_or_pull_container(instance)
    results = []
    for patch in patches:
        container.reset_to_base()        # git checkout base_commit
        container.apply_patch(patch)
        per_test = container.run_tests()  # 返回 per-test results
        results.append(per_test)
    return results

with ProcessPoolExecutor(max_workers=4) as pool:
    futures = {pool.submit(process_instance, inst, patches): inst 
               for inst, patches in all_instances.items()}
```

### 4.5 资源需求

| 资源 | 需求 |
|------|------|
| Docker 镜像存储 | ~50-100 GB（覆盖 ~12 个 repo 的不同版本） |
| 临时容器磁盘 | ~10 GB/容器 × 并行数 |
| 内存 | ~2 GB/容器 × 并行数 |
| GPU | 不需要（纯 CPU 测试执行） |
| 网络 | 首次拉取镜像需要 ~50 GB 下载 |
| 总磁盘 | ≥ 200 GB 推荐 |

---

## 5. 数据格式设计

### 5.1 输入格式

```jsonl
{
  "instance_id": "django__django-16379",
  "repo": "django/django",
  "patch": "diff --git a/django/db/models/query.py ...\n+        ...",
  "test_name": "tests.queries.test_qs_combinators.QuerySetSetOperationTests.test_union_with_values",
  "test_type": "f2p",
  "test_code": "def test_union_with_values(self):\n    ...",
  "patch_source": "gold|mutation_operator_swap|llm_claude|partial_hunk1",
  "context_files": ["django/db/models/query.py"],
  "label": 0,
  "error_message": "AssertionError: <QuerySet []> != <QuerySet [{'id': 1}]>"
}
```

**上下文策略（context_files）**：

完整 repo 太大（数万行），需要裁剪。方案：

| 策略 | 包含内容 | 预估 tokens |
|------|----------|-------------|
| Patch-only | 仅 diff 内容 | 200-800 |
| Patch + modified files | diff + 被修改文件全文 | 1K-5K |
| Patch + test + imports | diff + 测试代码 + 被修改文件的 import 链（1 层） | 2K-8K |
| Full repo snapshot | 整个 repo | 50K-500K（不可行） |

**推荐: Patch + modified files**，原因：
- Patch-only 信息太少，缺乏函数签名、类定义等上下文
- Import 链增加复杂度但 ROI 不高
- Modified files 通常 1-3 个，token 数可控
- 与 model 的 2048/4096 max_len 兼容（大多数情况 <4K tokens）

### 5.2 与现有格式兼容

现有 `train.jsonl` 格式：
```jsonl
{"code": "...", "test": "...", "label": 0/1, "source": "humaneval", "problem_id": "...", "mutation_type": "..."}
```

SWE-bench 格式映射：
```
code        → patch (diff 格式) + context_files (修改文件全文)
test        → test_code (单个测试函数)
label       → label (0/1)
source      → "swebench_verified"
problem_id  → instance_id
mutation_type → patch_source
```

统一格式（向后兼容）：
```jsonl
{
  "code": "<patch diff>\n\n--- Modified File: django/db/models/query.py ---\n<file content>",
  "test": "<single test function code>",
  "label": 0,
  "source": "swebench_verified",
  "problem_id": "django__django-16379",
  "mutation_type": "llm_claude",
  "error_message": "AssertionError: ...",
  "metadata": {
    "instance_id": "django__django-16379",
    "repo": "django/django",
    "test_name": "tests.queries...test_union_with_values",
    "test_type": "f2p",
    "patch_source": "llm_claude"
  }
}
```

### 5.3 Token 长度分析

基于 SWE-bench Verified 统计（Qwen tokenizer）：

| 字段 | P50 tokens | P90 tokens | P99 tokens |
|------|-----------|-----------|-----------|
| patch diff | 150 | 500 | 2000 |
| 修改文件全文（1个） | 800 | 3000 | 10000 |
| 测试函数代码 | 100 | 300 | 800 |
| error_message | 50 | 150 | 400 |
| **总计 (patch + file + test)** | **~1100** | **~3800** | **~13000** |

**Truncation 策略**：
- max_seq_len = 4096: 覆盖 ~P90，truncate 修改文件（保留 patch 相关函数 ± 50 行）
- max_seq_len = 8192: 覆盖 ~P97，几乎无需 truncation
- 文件级 truncation: 如果修改文件过长，只保留 patch hunk 周围 ±100 行上下文
- 对多文件 patch: 按 hunk 在文件中的位置排序，优先保留核心修改

---

## 6. 规模估算

### 6.1 样本数

```
500 instances
  × ~15 patches/instance (1 gold + 4 mutation + ~8 LLM + 2 partial)
  × ~10 tests/instance (median; range 1-50+, based on FAIL_TO_PASS + PASS_TO_PASS)
= ~75,000 total samples
```

分解：
- FAIL_TO_PASS tests: median 1-2/instance → 500 × 15 × 2 = 15,000
- PASS_TO_PASS tests: median 5-10/instance → 500 × 15 × 8 = 60,000
- 总计: ~75K samples（与 19K 函数级数据形成约 4:1 补充）

### 6.2 Label 分布预估

| Patch 类型 | F2P tests (预期) | P2P tests (预期) |
|-----------|-----------------|-----------------|
| Gold patch | ✓ pass (100%) | ✓ pass (~99%) |
| 合成变异 | ✗ fail (~70%) | ✓ pass (~90%) |
| LLM 错误 patch | ✗ fail (~80%) | ✓/✗ mixed (~85% pass) |
| 部分修复 | ✗ fail (~60%) | ✓ pass (~95%) |
| 无 patch (baseline) | ✗ fail (100%) | ✓ pass (100%) |

总体 pass/fail 比例估计: ~65% pass / 35% fail（P2P 测试大量 pass 拉高比例）
需要下采样 P2P pass 样本或加权，保持 ~50:50 平衡。

### 6.3 构建时间

| 阶段 | 时间 |
|------|------|
| 数据下载 + 预处理 | 1h |
| LLM patch 收集（从公开来源） | 2-4h |
| LLM patch 生成（自行生成，可选） | 4-8h + API 费用 |
| Docker 镜像构建/拉取 | 4-8h（首次）|
| 合成变异生成 | 0.5h |
| 测试执行（4 并行, 500 inst × 15 patches） | 24-48h |
| 结果汇总 + JSONL 构建 | 1h |
| **总计** | **~32-62h wall-clock** |

### 6.4 存储需求

| 内容 | 大小 |
|------|------|
| Docker 镜像缓存 | ~80 GB |
| 原始测试日志 | ~5 GB |
| 最终 train.jsonl | ~200 MB |
| 中间文件（patches, metadata） | ~500 MB |
| **总计** | **~86 GB** |

---

## 7. 风险和难点

### 7.1 Docker 环境构建失败

**问题**: SWE-bench 约 5-10% 的 instance 因依赖问题 Docker 构建失败。
**缓解**:
- 使用 SWE-bench 官方预构建镜像（`ghcr.io/swe-bench/`），已解决大部分依赖问题
- 失败 instance 跳过，记录失败原因。500 中预期可用 ~450+
- 不要自行构建镜像，用官方提供的

### 7.2 测试超时

**问题**: 某些测试（特别是 sympy、matplotlib 相关）执行时间长。
**缓解**:
- 单测试超时设 60s（而非整个 test suite）
- 超时标记为 `label=0, error_message="TIMEOUT"`
- 记录超时率，如果某 instance 超时率 >50% 考虑排除

### 7.3 特殊系统依赖

**问题**: 部分 repo 需要特殊系统包（如 `scikit-learn` 需要 BLAS, `matplotlib` 需要 GUI 后端）。
**缓解**: SWE-bench 官方镜像已处理。实际上 SWE-bench Verified 的 500 个 instance 集中在以下 12 个 repo：
- django, flask, sympy, scikit-learn, matplotlib, requests, sphinx, pytest, astropy, pylint, xarray, pydicom
- 官方镜像对这 12 个 repo 支持良好

### 7.4 Label Noise (Flaky Tests)

**问题**: 部分测试非确定性（依赖时间、随机数、网络等）。
**缓解**:
- 对 gold patch 执行 3 次，确认全部 pass（不 pass 的排除该测试）
- 对每个 `(patch, test)` 执行 2 次取多数票
- SWE-bench *Verified* 已做人工验证，flaky test 比例应低于 2%

### 7.5 Per-test 解析困难

**问题**: 不同 repo 使用不同测试框架（pytest vs unittest vs nose），输出格式不同。
**缓解**:
- SWE-bench harness 已标准化测试执行方式，统一使用 pytest
- `get_eval_report()` 已解析 per-test 结果
- 只需额外从日志中提取 error messages

### 7.6 Token 长度超限

**问题**: 少数 instance（P99）的修改文件 >10K tokens，超出模型 max_len。
**缓解**:
- 分级 truncation: 先裁剪文件到 hunk ±100 行，再裁剪到 ±50 行
- 如果仍超限，只保留 patch diff + test code（退化为 patch-only 模式）
- 记录 truncation 比例，分析对 label 准确性的影响

---

## 8. 实施路线（仅参考，不执行）

```
Phase 1 (Day 1-2): 数据准备
├── 下载 SWE-bench Verified dataset
├── 收集公开 LLM predictions (SWE-bench leaderboard)
├── 编写合成变异器（适配 diff 格式）
└── 编写 partial-hunk 生成器

Phase 2 (Day 2-4): Docker 执行
├── 设置 Docker 环境，拉取官方镜像
├── 修改 harness 收集 per-test results + error messages
├── 小规模测试（10 instances × 5 patches）验证流程
└── 全量执行（500 instances × 15 patches, 4 并行）

Phase 3 (Day 5): 数据后处理
├── 汇总 per-test 结果到 JSONL
├── 构建 context（patch + modified files）
├── Token 长度分析 + truncation
├── Label 平衡（下采样 P2P pass）
└── Train/val/test split（按 repo 分层，防泄漏）

Phase 4 (Day 6): 验证
├── 数据 sanity check（label 分布、token 分布、per-repo 统计）
├── 用现有模型做 zero-shot 评估
└── 确认数据格式与训练脚本兼容
```

---

## 9. 关键决策点（需 Director 确认）

1. **变异策略**: 推荐方案 C（混合），但如果想快速出结果，方案 A（纯合成变异）可在 1-2 天内完成，跳过 LLM patch 收集
2. **Context 粒度**: 推荐 patch + modified files。如果 token 超限严重，退化为 patch-only
3. **Train/test split**: 按 repo 分还是随机分？按 repo 分更严格（测试跨 repo 泛化），但 12 个 repo 分布不均
4. **是否合并函数级数据**: 混合训练（19K 函数级 + 75K repo 级）还是分开训练？混合可能 hurt（分布差异大），建议先分开，ablation 后决定
5. **执行环境**: home-1x5090 有 Docker 支持吗？需要确认。如果没有，需要另开一台有 Docker 的机器专门跑数据构建
