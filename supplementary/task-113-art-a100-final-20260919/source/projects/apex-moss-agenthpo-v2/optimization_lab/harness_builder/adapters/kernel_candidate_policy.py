"""Deterministic restricted language for KernelBench ``ModelNew`` candidates.

This is a policy gate, not a Python sandbox.  It deliberately accepts only the
small Torch/Triton surface used by the public P1/P2 candidates and is executed
again inside the trusted supervisor before any candidate import.  Unknown AST
nodes, call shapes and mutation targets fail closed.
"""

from __future__ import annotations

import ast
import hashlib
import json
import re
import stat
from dataclasses import dataclass
from pathlib import Path
from typing import Final


_MAX_SOURCE_BYTES: Final = 1_048_576
_MAX_AST_NODES: Final = 20_000
_MAX_FUNCTIONS: Final = 32
_MAX_CLASS_METHODS: Final = 16
_MAX_ARGUMENTS: Final = 32
_MAX_TEXT_LITERAL: Final = 4_096
_MAX_NUMBER: Final = 2**53
_SAFE_IDENTIFIER = re.compile(r"[A-Za-z_][A-Za-z0-9_]{0,127}")

_IMPORTS: Final = {
    "math": None,
    "torch": None,
    "torch.nn": "nn",
    "torch.nn.functional": "F",
    "triton": None,
    "triton.language": "tl",
}
_BANNED_NAMES: Final = frozenset(
    {
        "__builtins__",
        "breakpoint",
        "compile",
        "delattr",
        "dir",
        "eval",
        "exec",
        "getattr",
        "globals",
        "hasattr",
        "help",
        "input",
        "locals",
        "memoryview",
        "open",
        "print",
        "setattr",
        "vars",
        "__import__",
        "os",
        "sys",
        "pathlib",
        "subprocess",
        "threading",
        "multiprocessing",
        "socket",
        "ctypes",
        "inspect",
        "pickle",
    }
)
_BANNED_ATTRIBUTES: Final = frozenset(
    {
        "_C",
        "_base",
        "cuda",
        "data",
        "distributed",
        "fork",
        "from_file",
        "grad_fn",
        "load",
        "ops",
        "save",
        "set_device",
        "set_stream",
        "storage",
        "storage_offset",
        "stream",
        "typed_storage",
        "untyped_storage",
    }
)
_SAFE_BUILTIN_CALLS: Final = frozenset(
    {"abs", "float", "int", "len", "max", "min", "range", "tuple"}
)
_SAFE_MATH_CALLS: Final = frozenset(
    {"ceil", "exp", "floor", "log", "log2", "sqrt"}
)
_SAFE_TORCH_CALLS: Final = frozenset(
    {
        "empty",
        "empty_like",
        "exp",
        "full",
        "full_like",
        "logsumexp",
        "matmul",
        "mm",
        "ones",
        "ones_like",
        "relu",
        "sigmoid",
        "sum",
        "tensor",
        "zeros",
        "zeros_like",
    }
)
_TASK_TORCH_EXTENSIONS: Final = {
    "level1/21_Sigmoid.py": frozenset(),
    "level1/92_cumsum_exclusive.py": frozenset({"cat", "cumsum"}),
    "level1/97_ScaledDotProductAttention.py": frozenset(),
    "level2/45_Gemm_Sigmoid_LogSumExp.py": frozenset(),
    "level2/56_Matmul_Sigmoid_Sum.py": frozenset(),
    "level2/57_Conv2d_ReLU_HardSwish.py": frozenset({"clamp"}),
    "level2/67_Conv2d_GELU_GlobalAvgPool.py": frozenset(),
}
_SAFE_NN_CALLS: Final = frozenset(
    {
        "Conv2d",
        "GELU",
        "Hardswish",
        "LayerNorm",
        "Linear",
        "Parameter",
        "ReLU",
    }
)
_SAFE_NN_INIT_CALLS: Final = frozenset(
    {"constant_", "kaiming_uniform_", "ones_", "uniform_", "zeros_"}
)
_SAFE_FUNCTIONAL_CALLS: Final = frozenset(
    {"conv2d", "gelu", "hardswish", "layer_norm", "linear", "relu", "sigmoid"}
)
_TASK_FUNCTIONAL_EXTENSIONS: Final = {
    "level1/21_Sigmoid.py": frozenset(),
    "level1/92_cumsum_exclusive.py": frozenset(),
    "level1/97_ScaledDotProductAttention.py": frozenset(
        {"scaled_dot_product_attention"}
    ),
    "level2/45_Gemm_Sigmoid_LogSumExp.py": frozenset(),
    "level2/56_Matmul_Sigmoid_Sum.py": frozenset(),
    "level2/57_Conv2d_ReLU_HardSwish.py": frozenset(),
    "level2/67_Conv2d_GELU_GlobalAvgPool.py": frozenset(
        {"adaptive_avg_pool2d"}
    ),
}
_SAFE_TRITON_CALLS: Final = frozenset({"cdiv", "next_power_of_2"})
_CORE_SAFE_TL_CALLS: Final = frozenset(
    {
        "abs",
        "arange",
        "atomic_add",
        "atomic_cas",
        "atomic_xchg",
        "cdiv",
        "dot",
        "exp",
        "load",
        "maximum",
        "minimum",
        "num_programs",
        "program_id",
        "range",
        "rsqrt",
        "sigmoid",
        "static_range",
        "store",
        "sum",
        "where",
        "zeros",
    }
)
_TASK_TL_EXTENSIONS: Final = {
    "level1/21_Sigmoid.py": frozenset(),
    "level1/92_cumsum_exclusive.py": frozenset({"associative_scan", "cumsum"}),
    "level1/97_ScaledDotProductAttention.py": frozenset(
        {"advance", "exp2", "log", "make_block_ptr", "max", "trans"}
    ),
    "level2/45_Gemm_Sigmoid_LogSumExp.py": frozenset(
        {"advance", "exp2", "log", "make_block_ptr", "max", "trans"}
    ),
    "level2/56_Matmul_Sigmoid_Sum.py": frozenset({"trans"}),
    "level2/57_Conv2d_ReLU_HardSwish.py": frozenset(),
    "level2/67_Conv2d_GELU_GlobalAvgPool.py": frozenset({"erf", "tanh"}),
}
RESTRICTED_KERNEL_TASK_IDS: Final = tuple(_TASK_TL_EXTENSIONS)
_SAFE_TL_CALLS: Final = _CORE_SAFE_TL_CALLS | frozenset().union(
    *_TASK_TL_EXTENSIONS.values()
)
_SAFE_VALUE_METHODS: Final = frozenset(
    {
        "contiguous",
        "float",
        "flatten",
        "numel",
        "reshape",
        "sigmoid",
        "sum",
        "t",
        "to",
        "transpose",
        "type_as",
        "view",
    }
)
_TASK_VALUE_METHOD_EXTENSIONS: Final = {
    "level1/21_Sigmoid.py": frozenset(),
    "level1/92_cumsum_exclusive.py": frozenset(
        {"narrow", "select", "size", "unsqueeze"}
    ),
    "level1/97_ScaledDotProductAttention.py": frozenset(),
    "level2/45_Gemm_Sigmoid_LogSumExp.py": frozenset(),
    "level2/56_Matmul_Sigmoid_Sum.py": frozenset(),
    "level2/57_Conv2d_ReLU_HardSwish.py": frozenset(),
    "level2/67_Conv2d_GELU_GlobalAvgPool.py": frozenset({"squeeze"}),
}

if not (
    set(_TASK_TL_EXTENSIONS)
    == set(_TASK_TORCH_EXTENSIONS)
    == set(_TASK_FUNCTIONAL_EXTENSIONS)
    == set(_TASK_VALUE_METHOD_EXTENSIONS)
):  # pragma: no cover - import-time developer invariant.
    raise AssertionError("restricted Kernel task capability maps differ")

_POLICY_MANIFEST: Final = {
    "schema_version": 1,
    "policy_id": "hb-gen1-restricted-kernel-candidate-v1",
    "limits": {
        "source_bytes": _MAX_SOURCE_BYTES,
        "ast_nodes": _MAX_AST_NODES,
        "functions": _MAX_FUNCTIONS,
        "class_methods": _MAX_CLASS_METHODS,
        "arguments": _MAX_ARGUMENTS,
        "text_literal": _MAX_TEXT_LITERAL,
        "number_abs": _MAX_NUMBER,
    },
    "imports": sorted(_IMPORTS),
    "safe_builtin_calls": sorted(_SAFE_BUILTIN_CALLS),
    "safe_math_calls": sorted(_SAFE_MATH_CALLS),
    "safe_torch_calls": sorted(_SAFE_TORCH_CALLS),
    "task_torch_extensions": {
        task_id: sorted(values)
        for task_id, values in sorted(_TASK_TORCH_EXTENSIONS.items())
    },
    "safe_nn_calls": sorted(_SAFE_NN_CALLS),
    "safe_nn_init_calls": sorted(_SAFE_NN_INIT_CALLS),
    "safe_functional_calls": sorted(_SAFE_FUNCTIONAL_CALLS),
    "task_functional_extensions": {
        task_id: sorted(values)
        for task_id, values in sorted(_TASK_FUNCTIONAL_EXTENSIONS.items())
    },
    "safe_triton_calls": sorted(_SAFE_TRITON_CALLS),
    "safe_tl_calls": sorted(_SAFE_TL_CALLS),
    "safe_tl_libdevice_calls": ["erf"],
    "task_tl_extensions": {
        task_id: sorted(values) for task_id, values in sorted(_TASK_TL_EXTENSIONS.items())
    },
    "safe_value_methods": sorted(_SAFE_VALUE_METHODS),
    "task_value_method_extensions": {
        task_id: sorted(values)
        for task_id, values in sorted(_TASK_VALUE_METHOD_EXTENSIONS.items())
    },
    "top_level": "imports,static_constants,triton_jit_functions,one_ModelNew",
    "dunder_exception": "ModelNew.__init__ and exact super().__init__ only",
    "unknown_syntax": "reject",
}
RESTRICTED_KERNEL_CANDIDATE_POLICY_SHA256: Final = hashlib.sha256(
    json.dumps(_POLICY_MANIFEST, sort_keys=True, separators=(",", ":")).encode()
).hexdigest()


class RestrictedKernelCandidateError(ValueError):
    """Candidate source is outside CandidateInvocationABI-v1."""


@dataclass(frozen=True)
class RestrictedKernelCandidateReport:
    source_sha256: str
    policy_sha256: str
    imports: tuple[str, ...]
    triton_kernels: tuple[str, ...]
    model_methods: tuple[str, ...]
    ast_node_count: int
    task_id: str | None


_ALLOWED_AST_TYPES: Final = (
    ast.Module,
    ast.Import,
    ast.ImportFrom,
    ast.alias,
    ast.Expr,
    ast.Constant,
    ast.Assign,
    ast.AnnAssign,
    ast.AugAssign,
    ast.Name,
    ast.Load,
    ast.Store,
    ast.BinOp,
    ast.UnaryOp,
    ast.BoolOp,
    ast.Compare,
    ast.IfExp,
    ast.Tuple,
    ast.List,
    ast.Slice,
    ast.Subscript,
    ast.Attribute,
    ast.FunctionDef,
    ast.ClassDef,
    ast.arguments,
    ast.arg,
    ast.Return,
    ast.If,
    ast.For,
    ast.Pass,
    ast.Call,
    ast.keyword,
    ast.Add,
    ast.Sub,
    ast.Mult,
    ast.Div,
    ast.FloorDiv,
    ast.Mod,
    ast.Pow,
    ast.BitAnd,
    ast.BitOr,
    ast.BitXor,
    ast.LShift,
    ast.RShift,
    ast.UAdd,
    ast.USub,
    ast.Not,
    ast.And,
    ast.Or,
    ast.Eq,
    ast.NotEq,
    ast.Lt,
    ast.LtE,
    ast.Gt,
    ast.GtE,
    ast.Is,
    ast.IsNot,
)


def _dotted(node: ast.AST) -> str | None:
    parts: list[str] = []
    current = node
    while isinstance(current, ast.Attribute):
        parts.append(current.attr)
        current = current.value
    if not isinstance(current, ast.Name):
        return None
    parts.append(current.id)
    return ".".join(reversed(parts))


def _is_docstring(statement: ast.stmt) -> bool:
    return (
        isinstance(statement, ast.Expr)
        and isinstance(statement.value, ast.Constant)
        and isinstance(statement.value.value, str)
    )


class _PolicyVisitor(ast.NodeVisitor):
    def __init__(self, *, task_id: str | None) -> None:
        self.scope = "top"
        self.function_name: str | None = None
        self.imports: set[str] = set()
        self.triton_kernels: set[str] = set()
        self.model_methods: set[str] = set()
        self.model_attributes: set[str] = set()
        self.model_module_attributes: set[str] = set()
        self.known_constants: set[str] = set()
        self.task_id = task_id
        self.allowed_tl_calls = (
            _SAFE_TL_CALLS
            if task_id is None
            else _CORE_SAFE_TL_CALLS | _TASK_TL_EXTENSIONS[task_id]
        )
        self.allowed_torch_calls = _SAFE_TORCH_CALLS | (
            frozenset().union(*_TASK_TORCH_EXTENSIONS.values())
            if task_id is None
            else _TASK_TORCH_EXTENSIONS[task_id]
        )
        self.allowed_functional_calls = _SAFE_FUNCTIONAL_CALLS | (
            frozenset().union(*_TASK_FUNCTIONAL_EXTENSIONS.values())
            if task_id is None
            else _TASK_FUNCTIONAL_EXTENSIONS[task_id]
        )
        self.allowed_value_methods = _SAFE_VALUE_METHODS | (
            frozenset().union(*_TASK_VALUE_METHOD_EXTENSIONS.values())
            if task_id is None
            else _TASK_VALUE_METHOD_EXTENSIONS[task_id]
        )

    def reject(self, node: ast.AST, message: str) -> None:
        raise RestrictedKernelCandidateError(
            f"line {getattr(node, 'lineno', 0)}: {message}"
        )

    def generic_visit(self, node: ast.AST) -> None:
        if not isinstance(node, _ALLOWED_AST_TYPES):
            self.reject(node, f"unsupported AST node {type(node).__name__}")
        super().generic_visit(node)

    def visit_Module(self, node: ast.Module) -> None:
        classes = [item for item in node.body if isinstance(item, ast.ClassDef)]
        if len(classes) != 1 or classes[0].name != "ModelNew":
            self.reject(node, "module must define exactly one ModelNew class")
        functions = [item for item in node.body if isinstance(item, ast.FunctionDef)]
        if len(functions) > _MAX_FUNCTIONS:
            self.reject(node, "too many Triton functions")
        for statement in node.body:
            if isinstance(statement, (ast.Import, ast.ImportFrom, ast.FunctionDef, ast.ClassDef)):
                self.visit(statement)
            elif isinstance(statement, (ast.Assign, ast.AnnAssign)):
                self._visit_top_constant(statement)
            elif _is_docstring(statement):
                self.visit(statement)
            else:
                self.reject(statement, "top-level executable side effect is forbidden")

    def visit_Import(self, node: ast.Import) -> None:
        if len(node.names) != 1:
            self.reject(node, "each import must bind exactly one approved module")
        item = node.names[0]
        if item.name not in _IMPORTS:
            self.reject(node, f"import {item.name!r} is forbidden")
        expected_alias = _IMPORTS[item.name]
        if expected_alias is None:
            if item.asname is not None:
                self.reject(node, f"import alias for {item.name!r} differs")
        elif item.asname != expected_alias:
            self.reject(node, f"import {item.name!r} requires alias {expected_alias!r}")
        self.imports.add(item.name)

    def visit_ImportFrom(self, node: ast.ImportFrom) -> None:
        self.reject(node, "from-import is forbidden")

    def _visit_top_constant(self, node: ast.Assign | ast.AnnAssign) -> None:
        targets = node.targets if isinstance(node, ast.Assign) else [node.target]
        if len(targets) != 1 or not isinstance(targets[0], ast.Name):
            self.reject(node, "top-level constant target must be one name")
        name = targets[0].id
        if not _SAFE_IDENTIFIER.fullmatch(name) or "__" in name:
            self.reject(node, "unsafe top-level constant name")
        if not (name.isupper() or name.startswith("_")):
            self.reject(node, "top-level assignments must be named constants")
        value = node.value
        if value is None or not self._static_expression(value):
            self.reject(node, "top-level constant expression is not static")
        if isinstance(node, ast.AnnAssign) and node.annotation is not None:
            self.visit(node.annotation)
        self.known_constants.add(name)

    def _static_expression(self, node: ast.AST) -> bool:
        if isinstance(node, ast.Constant):
            self.visit_Constant(node)
            return not isinstance(node.value, str)
        if isinstance(node, ast.Name):
            return node.id in self.known_constants
        if isinstance(node, (ast.Tuple, ast.List)):
            return all(self._static_expression(item) for item in node.elts)
        if isinstance(node, ast.UnaryOp) and isinstance(node.op, (ast.UAdd, ast.USub)):
            return self._static_expression(node.operand)
        if isinstance(node, ast.BinOp) and isinstance(
            node.op, (ast.Add, ast.Sub, ast.Mult, ast.Div, ast.FloorDiv, ast.Mod)
        ):
            return self._static_expression(node.left) and self._static_expression(node.right)
        return False

    def visit_ClassDef(self, node: ast.ClassDef) -> None:
        if node.name != "ModelNew" or node.keywords or node.decorator_list:
            self.reject(node, "only undecorated ModelNew is allowed")
        if len(node.bases) != 1 or _dotted(node.bases[0]) not in {
            "nn.Module",
            "torch.nn.Module",
        }:
            self.reject(node, "ModelNew must inherit nn.Module")
        methods = [item for item in node.body if isinstance(item, ast.FunctionDef)]
        if len(methods) > _MAX_CLASS_METHODS:
            self.reject(node, "ModelNew has too many methods")
        names = {item.name for item in methods}
        if "__init__" not in names or "forward" not in names:
            self.reject(node, "ModelNew requires __init__ and forward")
        self.model_methods.update(names)
        for method in methods:
            if method.name != "__init__":
                continue
            for statement in method.body:
                if (
                    isinstance(statement, ast.Assign)
                    and len(statement.targets) == 1
                    and isinstance(statement.targets[0], ast.Attribute)
                    and isinstance(statement.targets[0].value, ast.Name)
                    and statement.targets[0].value.id == "self"
                    and isinstance(statement.value, ast.Call)
                    and _dotted(statement.value.func)
                    in {
                        "nn.Conv2d",
                        "nn.GELU",
                        "nn.Hardswish",
                        "nn.LayerNorm",
                        "nn.Linear",
                        "nn.ReLU",
                    }
                ):
                    self.model_module_attributes.add(statement.targets[0].attr)
        for statement in node.body:
            if isinstance(statement, ast.FunctionDef):
                previous_scope, previous_name = self.scope, self.function_name
                self.scope, self.function_name = "model", statement.name
                self._visit_function_body(statement, model=True)
                self.scope, self.function_name = previous_scope, previous_name
            elif _is_docstring(statement):
                self.visit(statement)
            else:
                self.reject(statement, "ModelNew body may contain only methods")

    def visit_FunctionDef(self, node: ast.FunctionDef) -> None:
        if self.scope != "top":
            self.reject(node, "nested functions are forbidden")
        if len(node.decorator_list) != 1 or _dotted(node.decorator_list[0]) != "triton.jit":
            self.reject(node, "top-level functions must use exactly @triton.jit")
        if not _SAFE_IDENTIFIER.fullmatch(node.name) or "__" in node.name:
            self.reject(node, "unsafe Triton function name")
        self.triton_kernels.add(node.name)
        previous_scope, previous_name = self.scope, self.function_name
        self.scope, self.function_name = "triton", node.name
        self._visit_function_body(node, model=False)
        self.scope, self.function_name = previous_scope, previous_name

    def _visit_function_body(self, node: ast.FunctionDef, *, model: bool) -> None:
        if node.decorator_list and model:
            self.reject(node, "ModelNew methods cannot be decorated")
        arguments = list(node.args.posonlyargs) + list(node.args.args) + list(node.args.kwonlyargs)
        if len(arguments) > _MAX_ARGUMENTS or node.args.vararg or node.args.kwarg:
            self.reject(node, "function signature is outside the bounded ABI")
        if model:
            if not arguments or arguments[0].arg != "self":
                self.reject(node, "ModelNew method must begin with self")
            if node.name.startswith("__") and node.name != "__init__":
                self.reject(node, "dunder ModelNew methods are forbidden")
        for argument in arguments:
            if not _SAFE_IDENTIFIER.fullmatch(argument.arg) or "__" in argument.arg:
                self.reject(argument, "unsafe argument name")
            if argument.annotation:
                self.visit(argument.annotation)
        for default in (*node.args.defaults, *node.args.kw_defaults):
            if default is not None:
                self.visit(default)
        if node.returns:
            self.visit(node.returns)
        for statement in node.body:
            self.visit(statement)

    def visit_Name(self, node: ast.Name) -> None:
        if not _SAFE_IDENTIFIER.fullmatch(node.id) or node.id in _BANNED_NAMES or "__" in node.id:
            self.reject(node, f"forbidden name {node.id!r}")

    def visit_Constant(self, node: ast.Constant) -> None:
        value = node.value
        if value is None or isinstance(value, bool):
            return
        if isinstance(value, (int, float)):
            if abs(value) > _MAX_NUMBER:
                self.reject(node, "numeric literal exceeds policy bound")
            return
        if isinstance(value, str) and len(value) <= _MAX_TEXT_LITERAL:
            return
        self.reject(node, "literal type or size is forbidden")

    def visit_Attribute(self, node: ast.Attribute) -> None:
        if "__" in node.attr:
            self.reject(node, "reflection and dunder access are forbidden")
        if node.attr in _BANNED_ATTRIBUTES or node.attr.startswith("_C"):
            self.reject(node, f"forbidden attribute {node.attr!r}")
        self.visit(node.value)

    def visit_Assign(self, node: ast.Assign) -> None:
        if self.scope == "top":
            self._visit_top_constant(node)
            return
        for target in node.targets:
            self._validate_assignment_target(target)
        self.visit(node.value)

    def visit_AnnAssign(self, node: ast.AnnAssign) -> None:
        if self.scope == "top":
            self._visit_top_constant(node)
            return
        self._validate_assignment_target(node.target)
        self.visit(node.annotation)
        if node.value is not None:
            self.visit(node.value)

    def visit_AugAssign(self, node: ast.AugAssign) -> None:
        self._validate_assignment_target(node.target, augmented=True)
        self.visit(node.op)
        self.visit(node.value)

    def _validate_assignment_target(self, node: ast.AST, *, augmented: bool = False) -> None:
        if isinstance(node, ast.Name):
            self.visit_Name(node)
            return
        if isinstance(node, (ast.Tuple, ast.List)) and not augmented:
            for item in node.elts:
                self._validate_assignment_target(item)
            return
        if isinstance(node, ast.Attribute) and isinstance(node.value, ast.Name) and node.value.id == "self":
            if "__" in node.attr or not _SAFE_IDENTIFIER.fullmatch(node.attr):
                self.reject(node, "unsafe self attribute assignment")
            self.model_attributes.add(node.attr)
            return
        self.reject(node, "module/global/tensor attribute mutation is forbidden")

    def visit_Call(self, node: ast.Call) -> None:
        if any(keyword.arg is None for keyword in node.keywords):
            self.reject(node, "dynamic **kwargs are forbidden")
        if isinstance(node.func, ast.Name):
            name = node.func.id
            if name == "super":
                if node.args or node.keywords:
                    self.reject(node, "super() arguments are forbidden")
            elif name in _SAFE_BUILTIN_CALLS:
                pass
            elif name in self.triton_kernels:
                self.reject(node, "Triton kernels must use an explicit launch grid")
            else:
                self.reject(node, f"unknown direct call {name!r}")
        elif isinstance(node.func, ast.Subscript):
            if not isinstance(node.func.value, ast.Name) or node.func.value.id not in self.triton_kernels:
                self.reject(node, "only a declared Triton kernel may use launch syntax")
            self.visit(node.func.slice)
        elif isinstance(node.func, ast.Attribute):
            dotted = _dotted(node.func)
            if dotted is not None:
                if dotted == "math." + node.func.attr:
                    allowed = node.func.attr in _SAFE_MATH_CALLS
                elif dotted == "torch." + node.func.attr:
                    allowed = node.func.attr in self.allowed_torch_calls
                elif dotted == "nn." + node.func.attr:
                    allowed = node.func.attr in _SAFE_NN_CALLS
                elif dotted == "nn.init." + node.func.attr:
                    allowed = node.func.attr in _SAFE_NN_INIT_CALLS
                elif dotted == "F." + node.func.attr:
                    allowed = node.func.attr in self.allowed_functional_calls
                elif dotted == "triton." + node.func.attr:
                    allowed = node.func.attr in _SAFE_TRITON_CALLS
                elif dotted == "tl." + node.func.attr:
                    allowed = self.scope == "triton" and node.func.attr in self.allowed_tl_calls
                elif dotted == "tl.libdevice.erf":
                    allowed = self.scope == "triton" and (
                        self.task_id is None
                        or self.task_id == "level2/67_Conv2d_GELU_GlobalAvgPool.py"
                    )
                elif dotted.startswith("self."):
                    parts = dotted.split(".")
                    allowed = self.scope == "model" and (
                        (
                            len(parts) == 2
                            and (
                                node.func.attr in self.model_module_attributes
                                or (
                                    node.func.attr in self.model_methods
                                    and node.func.attr not in {"__init__", "forward"}
                                )
                            )
                        )
                        or (
                            len(parts) > 2
                            and node.func.attr in self.allowed_value_methods
                        )
                    )
                else:
                    allowed = node.func.attr in self.allowed_value_methods
                if not allowed:
                    self.reject(node, f"unknown or forbidden call {dotted!r}")
            elif (
                node.func.attr == "__init__"
                and isinstance(node.func.value, ast.Call)
                and isinstance(node.func.value.func, ast.Name)
                and node.func.value.func.id == "super"
                and self.scope == "model"
                and self.function_name == "__init__"
            ):
                pass
            elif node.func.attr in self.allowed_value_methods:
                pass
            else:
                self.reject(node, f"unknown dynamic method call {node.func.attr!r}")
        else:
            self.reject(node, "dynamic callable expressions are forbidden")
        for argument in node.args:
            self.visit(argument)
        for keyword in node.keywords:
            self.visit(keyword.value)

    def visit_For(self, node: ast.For) -> None:
        self._validate_assignment_target(node.target)
        if self.scope == "triton":
            if not (
                isinstance(node.iter, ast.Call)
                and (
                    (isinstance(node.iter.func, ast.Name) and node.iter.func.id == "range")
                    or _dotted(node.iter.func) in {"tl.range", "tl.static_range"}
                )
            ):
                self.reject(node, "Triton loops require range/tl.range/tl.static_range")
        elif self.scope == "model":
            if not (
                isinstance(node.iter, ast.Attribute)
                and isinstance(node.iter.value, ast.Name)
                and node.iter.value.id == "self"
            ):
                self.reject(node, "host loops may iterate only over frozen self configuration")
        else:
            self.reject(node, "loop outside a candidate method is forbidden")
        self.visit(node.iter)
        for statement in node.body:
            self.visit(statement)
        if node.orelse:
            self.reject(node, "for-else is forbidden")

    def visit_Pass(self, node: ast.Pass) -> None:
        if self.scope != "model" or self.function_name != "__init__":
            self.reject(node, "pass is allowed only in ModelNew.__init__")


class RestrictedKernelCandidatePolicy:
    """Validate exact candidate bytes against the immutable v1 policy."""

    policy_sha256 = RESTRICTED_KERNEL_CANDIDATE_POLICY_SHA256

    def validate(
        self, source: str | bytes, *, task_id: str | None = None
    ) -> RestrictedKernelCandidateReport:
        if isinstance(source, str):
            raw = source.encode("utf-8")
        elif isinstance(source, bytes):
            raw = source
        else:
            raise TypeError("candidate source must be str or bytes")
        if task_id is not None and task_id not in _TASK_TL_EXTENSIONS:
            raise RestrictedKernelCandidateError("candidate task capability is not frozen")
        if not raw or len(raw) > _MAX_SOURCE_BYTES or b"\x00" in raw:
            raise RestrictedKernelCandidateError("candidate source size is invalid")
        try:
            text = raw.decode("utf-8")
        except UnicodeDecodeError as exc:
            raise RestrictedKernelCandidateError("candidate source must be UTF-8") from exc
        try:
            tree = ast.parse(text)
        except SyntaxError as exc:
            raise RestrictedKernelCandidateError(
                f"candidate syntax error: {exc.msg}"
            ) from exc
        node_count = sum(1 for _ in ast.walk(tree))
        if node_count > _MAX_AST_NODES:
            raise RestrictedKernelCandidateError("candidate AST exceeds policy bound")
        visitor = _PolicyVisitor(task_id=task_id)
        visitor.visit(tree)
        return RestrictedKernelCandidateReport(
            source_sha256=hashlib.sha256(raw).hexdigest(),
            policy_sha256=self.policy_sha256,
            imports=tuple(sorted(visitor.imports)),
            triton_kernels=tuple(sorted(visitor.triton_kernels)),
            model_methods=tuple(sorted(visitor.model_methods)),
            ast_node_count=node_count,
            task_id=task_id,
        )

    def validate_path(
        self, path: Path, *, task_id: str | None = None
    ) -> RestrictedKernelCandidateReport:
        path = Path(path)
        try:
            metadata = path.lstat()
        except OSError as exc:
            raise RestrictedKernelCandidateError("candidate path is missing") from exc
        if stat.S_ISLNK(metadata.st_mode) or not stat.S_ISREG(metadata.st_mode):
            raise RestrictedKernelCandidateError(
                "candidate path must be a regular non-symlink file"
            )
        try:
            raw = path.read_bytes()
        except OSError as exc:
            raise RestrictedKernelCandidateError("candidate path is unreadable") from exc
        return self.validate(raw, task_id=task_id)


__all__ = [
    "RESTRICTED_KERNEL_CANDIDATE_POLICY_SHA256",
    "RESTRICTED_KERNEL_TASK_IDS",
    "RestrictedKernelCandidateError",
    "RestrictedKernelCandidatePolicy",
    "RestrictedKernelCandidateReport",
]
