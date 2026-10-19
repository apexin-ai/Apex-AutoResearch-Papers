#!/usr/bin/env python3
from __future__ import annotations

import argparse
import importlib.util
import json
import math
import random
import sys
import time
import types
from copy import deepcopy
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[3]
ART_UTILS = ROOT / "repositories/ART/examples/2048/utils.py"
DIRECTIONS = ["left", "right", "up", "down"]
MOVE_ORDERS = {
    "left_up_right_down": ["left", "up", "right", "down"],
    "up_left_right_down": ["up", "left", "right", "down"],
    "right_up_left_down": ["right", "up", "left", "down"],
    "down_left_right_up": ["down", "left", "right", "up"],
}


def load_art_utils() -> Any:
    if "dotenv" not in sys.modules:
        dotenv = types.ModuleType("dotenv")
        dotenv.load_dotenv = lambda *args, **kwargs: False
        sys.modules["dotenv"] = dotenv
    spec = importlib.util.spec_from_file_location("art_2048_utils", ART_UTILS)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"failed to load ART 2048 utils from {ART_UTILS}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


U = load_art_utils()


def board_tuple(game: dict[str, Any]) -> tuple[tuple[int, ...], ...]:
    return tuple(tuple(0 if cell is None else int(cell) for cell in row) for row in game["board"])


def clone_game(game: dict[str, Any]) -> dict[str, Any]:
    return {"id": game["id"], "board": deepcopy(game["board"])}


def move_without_random(game: dict[str, Any], direction: str) -> dict[str, Any] | None:
    nxt = clone_game(game)
    before = board_tuple(nxt)
    U.condense_board(nxt, U.Direction(direction))
    after = board_tuple(nxt)
    return None if after == before else nxt


def count_empty(game: dict[str, Any]) -> int:
    return sum(cell is None for row in game["board"] for cell in row)


def max_tile(game: dict[str, Any]) -> int:
    return max((cell or 0) for row in game["board"] for cell in row)


def potential_merges(game: dict[str, Any]) -> int:
    merges = 0
    board = game["board"]
    for r in range(4):
        for c in range(4):
            value = board[r][c]
            if value is None:
                continue
            if c + 1 < 4 and board[r][c + 1] == value:
                merges += 1
            if r + 1 < 4 and board[r + 1][c] == value:
                merges += 1
    return merges


def smoothness_penalty(game: dict[str, Any]) -> float:
    penalty = 0.0
    board = game["board"]
    for r in range(4):
        for c in range(4):
            value = board[r][c]
            if value is None:
                continue
            log_value = math.log2(value)
            for rr, cc in ((r + 1, c), (r, c + 1)):
                if rr < 4 and cc < 4 and board[rr][cc] is not None:
                    penalty += abs(log_value - math.log2(board[rr][cc]))
    return penalty


def corner_score(game: dict[str, Any]) -> float:
    weights = [
        [16, 8, 4, 2],
        [8, 4, 2, 1],
        [4, 2, 1, 0.5],
        [2, 1, 0.5, 0.25],
    ]
    score = 0.0
    for r, row in enumerate(game["board"]):
        for c, cell in enumerate(row):
            if cell is not None:
                score += math.log2(cell) * weights[r][c]
    return score


def heuristic(game: dict[str, Any], config: dict[str, Any]) -> float:
    tile = max(max_tile(game), 2)
    return (
        float(config["empty_weight"]) * count_empty(game)
        + float(config["merge_weight"]) * potential_merges(game)
        + float(config["max_tile_weight"]) * math.log2(tile)
        + float(config["corner_weight"]) * corner_score(game) / 32.0
        - float(config["smoothness_weight"]) * smoothness_penalty(game)
    )


def search_value(game: dict[str, Any], config: dict[str, Any], depth: int) -> float:
    if depth <= 0 or U.check_game_finished(game):
        return heuristic(game, config)
    best = -1e9
    for direction in MOVE_ORDERS[str(config["move_order"])]:
        nxt = move_without_random(game, direction)
        if nxt is None:
            continue
        best = max(best, heuristic(nxt, config) + 0.75 * search_value(nxt, config, depth - 1))
    return heuristic(game, config) if best == -1e9 else best


def choose_move(game: dict[str, Any], config: dict[str, Any]) -> str | None:
    depth = int(config["lookahead_depth"])
    best_move = None
    best_score = -1e9
    for direction in MOVE_ORDERS[str(config["move_order"])]:
        nxt = move_without_random(game, direction)
        if nxt is None:
            continue
        score = heuristic(nxt, config) + 0.75 * search_value(nxt, config, depth - 1)
        if score > best_score:
            best_score = score
            best_move = direction
    return best_move


def play_game(config: dict[str, Any], seed: int, max_moves: int) -> dict[str, Any]:
    random.seed(seed)
    game = U.generate_game()
    moves = 0
    while moves < max_moves and not U.check_game_finished(game):
        move = choose_move(game, config)
        if move is None:
            break
        U.apply_agent_move(game, f"<move>{move}</move>")
        moves += 1
    maximum = max_tile(game)
    return {
        "win": maximum >= int(U.WINNING_VALUE),
        "max_tile": maximum,
        "total_board_value": U.total_board_value(game),
        "moves": moves,
        "board": board_tuple(game),
    }


def evaluate(config: dict[str, Any], games: int, max_moves: int, seed: int) -> dict[str, Any]:
    game_results = [play_game(config, seed * 1000 + idx, max_moves) for idx in range(games)]
    wins = sum(1 for item in game_results if item["win"])
    return {
        "win_rate": wins / float(games),
        "wins": wins,
        "games": games,
        "max_moves": max_moves,
        "avg_max_tile": sum(item["max_tile"] for item in game_results) / float(games),
        "avg_total_board_value": sum(item["total_board_value"] for item in game_results) / float(games),
        "avg_moves": sum(item["moves"] for item in game_results) / float(games),
        "winning_value": int(U.WINNING_VALUE),
        "config": config,
        "seed": seed,
        "game_results": game_results,
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--results-dir", required=True)
    parser.add_argument("--lookahead-depth", type=int, default=1)
    parser.add_argument("--empty-weight", type=float, default=1.0)
    parser.add_argument("--merge-weight", type=float, default=0.5)
    parser.add_argument("--max-tile-weight", type=float, default=1.0)
    parser.add_argument("--corner-weight", type=float, default=0.0)
    parser.add_argument("--smoothness-weight", type=float, default=0.0)
    parser.add_argument("--move-order", choices=sorted(MOVE_ORDERS), default="left_up_right_down")
    parser.add_argument("--games", type=int, default=25)
    parser.add_argument("--max-moves", type=int, default=60)
    parser.add_argument("--seed", type=int, default=42)
    args = parser.parse_args()
    config = {
        "lookahead_depth": args.lookahead_depth,
        "empty_weight": args.empty_weight,
        "merge_weight": args.merge_weight,
        "max_tile_weight": args.max_tile_weight,
        "corner_weight": args.corner_weight,
        "smoothness_weight": args.smoothness_weight,
        "move_order": args.move_order,
    }
    started = time.time()
    result = evaluate(config, args.games, args.max_moves, args.seed)
    result["seconds"] = round(time.time() - started, 3)
    out_dir = Path(args.results_dir)
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "results.json").write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    print("RESULT_JSON " + json.dumps(result, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
