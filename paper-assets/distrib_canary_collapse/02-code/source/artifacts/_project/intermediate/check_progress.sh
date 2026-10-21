#!/usr/bin/env bash
# check_progress.sh — MVP 实验进度检查脚本
# 在服务器上直接运行，输出各 rep 进度、GPU 状态、日志尾部、预估剩余时间

set -euo pipefail

# --- 颜色 ---
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
CYAN='\033[0;36m'
BOLD='\033[1m'
DIM='\033[2m'
RESET='\033[0m'

RESULTS_DIR="/root/autodl-tmp/distrib_canary_collapse/results/mvp"
LOG_DIR="$HOME/runs/distrib_canary_collapse"
TOTAL_GENS=10

header() {
    echo ""
    echo -e "${CYAN}═══════════════════════════════════════════════════${RESET}"
    echo -e "${BOLD}  $1${RESET}"
    echo -e "${CYAN}═══════════════════════════════════════════════════${RESET}"
}

# ============================================================
# 1. 每个 rep 的代数进度
# ============================================================
header "REP 进度"

for rep in 42 43 44; do
    rep_dir="${RESULTS_DIR}/rep_${rep}"
    if [[ ! -d "$rep_dir" ]]; then
        echo -e "  rep_${rep}: ${DIM}目录不存在${RESET}"
        continue
    fi

    latest_gen=$(ls -d "${rep_dir}"/gen_* 2>/dev/null | sort -t_ -k2 -n | tail -1 || true)
    if [[ -z "$latest_gen" ]]; then
        echo -e "  rep_${rep}: ${YELLOW}无 gen 目录${RESET}"
        continue
    fi

    gen_num=$(basename "$latest_gen" | sed 's/gen_//')
    has_metrics="no"
    has_synth="no"
    [[ -f "${latest_gen}/metrics.json" ]] && has_metrics="yes"
    [[ -d "${latest_gen}/synthetic_data" ]] && has_synth="yes"

    # 状态判定
    if [[ "$has_metrics" == "yes" ]]; then
        status="${GREEN}已完成${RESET}"
    elif [[ "$has_synth" == "yes" ]]; then
        status="${YELLOW}生成中${RESET}"
    else
        status="${YELLOW}训练中${RESET}"
    fi

    # 进度条
    if [[ "$has_metrics" == "yes" ]]; then
        completed=$((gen_num + 1))
    else
        completed=$gen_num
    fi
    pct=$((completed * 100 / TOTAL_GENS))
    bar_filled=$((pct / 5))
    bar_empty=$((20 - bar_filled))
    bar=$(printf '█%.0s' $(seq 1 $bar_filled 2>/dev/null) || true)
    bar_bg=$(printf '░%.0s' $(seq 1 $bar_empty 2>/dev/null) || true)

    echo -e "  rep_${rep}: gen ${BOLD}${gen_num}${RESET}/${TOTAL_GENS}  ${status}  [${GREEN}${bar}${DIM}${bar_bg}${RESET}] ${pct}%"
    echo -e "         metrics=${has_metrics}  synthetic_data=${has_synth}"
done

# ============================================================
# 2. GPU 利用率
# ============================================================
header "GPU 状态"

if command -v nvidia-smi &>/dev/null; then
    nvidia-smi --query-gpu=index,name,memory.used,memory.total,utilization.gpu,temperature.gpu \
        --format=csv,noheader 2>/dev/null | while IFS=, read -r idx name mem_used mem_total util temp; do
        # 去空格
        util=$(echo "$util" | tr -d ' %')
        temp=$(echo "$temp" | tr -d ' ')
        mem_used=$(echo "$mem_used" | tr -d ' ')
        mem_total=$(echo "$mem_total" | tr -d ' ')

        if [[ "$util" -gt 80 ]]; then
            color=$GREEN
        elif [[ "$util" -gt 20 ]]; then
            color=$YELLOW
        else
            color=$RED
        fi
        echo -e "  GPU ${idx}: ${name}  ${color}${util}%${RESET} util  ${mem_used}/${mem_total}  ${temp}°C"
    done
else
    echo -e "  ${RED}nvidia-smi 不可用${RESET}"
fi

# ============================================================
# 3. 日志最后 5 行
# ============================================================
header "日志尾部"

for rep in 42 43 44; do
    log_file="${LOG_DIR}/mvp_v4_rep${rep}.log"
    if [[ -f "$log_file" ]]; then
        echo -e "  ${BOLD}--- rep_${rep} ---${RESET}"
        tail -5 "$log_file" | sed 's/^/    /'
    else
        echo -e "  rep_${rep}: ${DIM}日志不存在 (${log_file})${RESET}"
    fi
done

# ============================================================
# 4. 预估剩余时间
# ============================================================
header "预估剩余时间"

for rep in 42 43 44; do
    rep_dir="${RESULTS_DIR}/rep_${rep}"
    gen0_metrics="${rep_dir}/gen_0/metrics.json"
    [[ ! -f "$gen0_metrics" ]] && continue

    # 找最新已完成的 gen
    latest_completed=""
    latest_gen_num=0
    for d in "${rep_dir}"/gen_*; do
        [[ ! -d "$d" ]] && continue
        n=$(basename "$d" | sed 's/gen_//')
        if [[ -f "${d}/metrics.json" ]] && [[ "$n" -gt "$latest_gen_num" ]]; then
            latest_gen_num=$n
            latest_completed="$d"
        fi
    done

    if [[ -z "$latest_completed" ]] || [[ "$latest_gen_num" -eq 0 ]]; then
        echo -e "  rep_${rep}: ${DIM}数据不足，无法估算${RESET}"
        continue
    fi

    t_start=$(stat -c %Y "$gen0_metrics" 2>/dev/null || stat -f %m "$gen0_metrics" 2>/dev/null)
    t_latest=$(stat -c %Y "${latest_completed}/metrics.json" 2>/dev/null || stat -f %m "${latest_completed}/metrics.json" 2>/dev/null)

    elapsed=$((t_latest - t_start))
    completed_gens=$latest_gen_num
    remaining_gens=$((TOTAL_GENS - completed_gens - 1))

    if [[ "$completed_gens" -gt 0 ]] && [[ "$remaining_gens" -gt 0 ]]; then
        avg_per_gen=$((elapsed / completed_gens))
        eta_seconds=$((avg_per_gen * remaining_gens))
        eta_hours=$((eta_seconds / 3600))
        eta_mins=$(( (eta_seconds % 3600) / 60 ))
        echo -e "  rep_${rep}: 已完成 ${completed_gens} 代 (耗时 $((elapsed/3600))h$((elapsed%3600/60))m), 剩余 ${remaining_gens} 代, ETA ${BOLD}${eta_hours}h${eta_mins}m${RESET}"
    elif [[ "$remaining_gens" -le 0 ]]; then
        echo -e "  rep_${rep}: ${GREEN}已全部完成${RESET}"
    else
        echo -e "  rep_${rep}: ${DIM}数据不足，无法估算${RESET}"
    fi
done

# ============================================================
# 5. 进程存活检查
# ============================================================
header "进程状态"

procs=$(pgrep -a "iterative_train" 2>/dev/null || true)
if [[ -n "$procs" ]]; then
    echo "$procs" | while read -r line; do
        echo -e "  ${GREEN}●${RESET} $line"
    done
else
    echo -e "  ${RED}● 未发现 iterative_train 进程${RESET}"
fi

# tmux sessions
tmux_sessions=$(tmux list-sessions 2>/dev/null || true)
if [[ -n "$tmux_sessions" ]]; then
    echo ""
    echo -e "  ${BOLD}tmux sessions:${RESET}"
    echo "$tmux_sessions" | sed 's/^/    /'
else
    echo -e "  ${DIM}无 tmux session${RESET}"
fi

echo ""
echo -e "${DIM}检查时间: $(date '+%Y-%m-%d %H:%M:%S')${RESET}"
