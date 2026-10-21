#!/bin/bash
source /root/miniconda3/etc/profile.d/conda.sh && conda activate base
cd /root/symb_invariant_consensus

LOG=results/exp_folio_2x2/master.log
mkdir -p results/exp_folio_2x2
exec > >(tee -a "$LOG") 2>&1

echo "=== FOLIO 2x2 Master Script Started $(date) ==="

# --- Phase 1: Wait for Cell A extraction + Qwen3 trace generation ---

CELL_A_PID=491631
QWEN3_MVP_PID=491494
QWEN3_TRACE_PID=492050

echo "Waiting for:"
echo "  Cell A extraction PID=$CELL_A_PID"
echo "  Qwen3 run_full_mvp PID=$QWEN3_MVP_PID"
echo "  Qwen3 trace_gen_only PID=$QWEN3_TRACE_PID"

while true; do
    CELL_A_ALIVE=0; QWEN3_MVP_ALIVE=0; QWEN3_TRACE_ALIVE=0
    kill -0 $CELL_A_PID 2>/dev/null && CELL_A_ALIVE=1
    kill -0 $QWEN3_MVP_PID 2>/dev/null && QWEN3_MVP_ALIVE=1
    kill -0 $QWEN3_TRACE_PID 2>/dev/null && QWEN3_TRACE_ALIVE=1

    CELL_A_N=$(python3 -c "
import json
try:
    d=json.load(open('results/exp_folio_2x2/cell_a_mistral_mistral.json'))
    print(len(d.get('results',[])))
except: print('?')
" 2>/dev/null)
    QWEN3_N=$(ls results/exp_folio_2x2_qwen3/intermediates/folio_*.json 2>/dev/null | wc -l)

    echo "$(date +%H:%M) | CellA: ${CELL_A_N}/204 (alive=$CELL_A_ALIVE) | Qwen3 traces: ${QWEN3_N}/204 (mvp=$QWEN3_MVP_ALIVE, tgen=$QWEN3_TRACE_ALIVE)"

    if [ $CELL_A_ALIVE -eq 0 ] && [ $QWEN3_MVP_ALIVE -eq 0 ] && [ $QWEN3_TRACE_ALIVE -eq 0 ]; then
        echo "All Phase 1 processes finished at $(date)"
        break
    fi
    sleep 120
done

# Verify completeness
CELL_A_FINAL=$(python3 -c "
import json
d=json.load(open('results/exp_folio_2x2/cell_a_mistral_mistral.json'))
print(len(d.get('results',[])))
" 2>/dev/null)
QWEN3_FINAL=$(ls results/exp_folio_2x2_qwen3/intermediates/folio_*.json 2>/dev/null | wc -l)
echo "Phase 1 final counts: Cell A=$CELL_A_FINAL/204, Qwen3 traces=$QWEN3_FINAL/204"

if [ "$CELL_A_FINAL" -lt 204 ] 2>/dev/null; then
    echo "WARN: Cell A incomplete ($CELL_A_FINAL/204). Continuing anyway."
fi
if [ "$QWEN3_FINAL" -lt 204 ] 2>/dev/null; then
    echo "WARN: Qwen3 traces incomplete ($QWEN3_FINAL/204). Continuing anyway."
fi

echo "=== Phase 1 done. Starting Phase 2: Cells B, C, D ==="

# --- Phase 2: Cell B + C in parallel, then D ---

# Cell B: Mistral gen -> Qwen3 ext (port 8001, needs --qwen3-nothink)
echo "Starting Cell B (Mistral->Qwen3) + Cell C (Qwen3->Mistral) in parallel..."

python scripts/cross_model_extract.py \
  --traces-dir results/exp033_mistral_7b_folio204/intermediates/ \
  --api-base http://localhost:8001/v1 \
  --output results/exp_folio_2x2/cell_b_mistral_qwen3.json \
  --qwen3-nothink \
  --resume &
CELL_B_PID=$!
echo "Cell B PID=$CELL_B_PID"

# Cell C: Qwen3 gen -> Mistral ext (port 8004)
python scripts/cross_model_extract.py \
  --traces-dir results/exp_folio_2x2_qwen3/intermediates/ \
  --api-base http://localhost:8004/v1 \
  --output results/exp_folio_2x2/cell_c_qwen3_mistral.json \
  --resume &
CELL_C_PID=$!
echo "Cell C PID=$CELL_C_PID"

# Monitor B+C
while true; do
    B_ALIVE=0; C_ALIVE=0
    kill -0 $CELL_B_PID 2>/dev/null && B_ALIVE=1
    kill -0 $CELL_C_PID 2>/dev/null && C_ALIVE=1

    B_N=$(python3 -c "
import json
try:
    d=json.load(open('results/exp_folio_2x2/cell_b_mistral_qwen3.json'))
    print(len(d.get('results',[])))
except: print('0')
" 2>/dev/null)
    C_N=$(python3 -c "
import json
try:
    d=json.load(open('results/exp_folio_2x2/cell_c_qwen3_mistral.json'))
    print(len(d.get('results',[])))
except: print('0')
" 2>/dev/null)

    echo "$(date +%H:%M) | CellB: ${B_N}/204 (alive=$B_ALIVE) | CellC: ${C_N}/204 (alive=$C_ALIVE)"

    if [ $B_ALIVE -eq 0 ] && [ $C_ALIVE -eq 0 ]; then
        break
    fi
    sleep 120
done

wait $CELL_B_PID
B_EXIT=$?
wait $CELL_C_PID
C_EXIT=$?
echo "Cell B exit=$B_EXIT, Cell C exit=$C_EXIT at $(date)"

# Cell D: Qwen3 gen -> Qwen3 ext (port 8001, needs --qwen3-nothink)
echo "Starting Cell D (Qwen3->Qwen3)..."
python scripts/cross_model_extract.py \
  --traces-dir results/exp_folio_2x2_qwen3/intermediates/ \
  --api-base http://localhost:8001/v1 \
  --output results/exp_folio_2x2/cell_d_qwen3_qwen3.json \
  --qwen3-nothink \
  --resume
D_EXIT=$?
echo "Cell D exit=$D_EXIT at $(date)"

echo "=== Phase 2 done. Starting Phase 3: Metrics ==="

# --- Phase 3: Compute metrics using existing comprehensive script ---
python scripts/compute_folio_2x2_metrics.py
METRICS_EXIT=$?
echo "Metrics exit=$METRICS_EXIT"

echo "=== FOLIO 2x2 COMPLETE $(date) ==="
echo "SENTINEL_FOLIO_2X2_DONE"
