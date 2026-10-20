#!/usr/bin/env bash
# Launch a vLLM OpenAI-compatible server with auto-detected GPU count
# and tool-call support.
#
# Usage:
#   ./setup_vllm.sh --model Qwen/Qwen3-32B [--port 8000] [--gpus auto] \
#                    [--tool-parser hermes] [--max-model-len 32768]

set -euo pipefail

MODEL=""
PORT=8000
GPUS="auto"
TOOL_PARSER=""
MAX_MODEL_LEN=""
EXTRA_ARGS=""

while [[ $# -gt 0 ]]; do
    case $1 in
        --model)       MODEL="$2";          shift 2 ;;
        --port)        PORT="$2";           shift 2 ;;
        --gpus)        GPUS="$2";           shift 2 ;;
        --tool-parser) TOOL_PARSER="$2";    shift 2 ;;
        --max-model-len) MAX_MODEL_LEN="$2"; shift 2 ;;
        --extra)       EXTRA_ARGS="$2";     shift 2 ;;
        *) echo "Unknown arg: $1"; exit 1 ;;
    esac
done

if [[ -z "$MODEL" ]]; then
    echo "Usage: $0 --model <model_id_or_path> [options]"
    exit 1
fi

# Auto-detect GPU count
if [[ "$GPUS" == "auto" ]]; then
    GPUS=$(nvidia-smi --list-gpus 2>/dev/null | wc -l)
    if [[ "$GPUS" -eq 0 ]]; then
        echo "ERROR: No GPUs detected"
        exit 1
    fi
fi
echo "Using $GPUS GPU(s) for tensor parallelism"

# Infer tool-call parser from model name if not specified
if [[ -z "$TOOL_PARSER" ]]; then
    case "$MODEL" in
        *Qwen*|*qwen*)       TOOL_PARSER="hermes" ;;
        *Llama*|*llama*)      TOOL_PARSER="llama3_json" ;;
        *DeepSeek*|*deepseek*) TOOL_PARSER="hermes" ;;
        *)                    TOOL_PARSER="hermes" ;;
    esac
    echo "Auto-selected tool parser: $TOOL_PARSER"
fi

# Build command
CMD="python -m vllm.entrypoints.openai.api_server \
    --model $MODEL \
    --port $PORT \
    --tensor-parallel-size $GPUS \
    --enable-auto-tool-choice \
    --tool-call-parser $TOOL_PARSER \
    --trust-remote-code"

if [[ -n "$MAX_MODEL_LEN" ]]; then
    CMD="$CMD --max-model-len $MAX_MODEL_LEN"
fi

if [[ -n "$EXTRA_ARGS" ]]; then
    CMD="$CMD $EXTRA_ARGS"
fi

echo "Starting vLLM server:"
echo "  $CMD"
echo ""

# Launch in background
$CMD &
SERVER_PID=$!

# Health check: wait up to 5 minutes
echo "Waiting for server to be ready (PID=$SERVER_PID) ..."
for i in $(seq 1 60); do
    if ! kill -0 "$SERVER_PID" 2>/dev/null; then
        echo "ERROR: Server process exited unexpectedly"
        exit 1
    fi
    if curl -s "http://localhost:$PORT/health" > /dev/null 2>&1; then
        echo ""
        echo "vLLM server ready at http://localhost:$PORT/v1"
        echo "  Model: $MODEL"
        echo "  GPUs:  $GPUS (tensor parallel)"
        echo "  PID:   $SERVER_PID"
        echo ""
        echo "To stop: kill $SERVER_PID"
        wait "$SERVER_PID"
        exit 0
    fi
    sleep 5
done

echo "ERROR: Server failed to become ready within 5 minutes"
kill "$SERVER_PID" 2>/dev/null
exit 1
