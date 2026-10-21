from typing import List, Dict, Any, Optional
from openai import OpenAI
import os
import subprocess
import threading
import time
from concurrent.futures import ThreadPoolExecutor
import random
import json
import requests
from tqdm import tqdm
import copy
import signal
import atexit
import weakref
from typing import Literal
from swarm.gemini import gemini_chat_completion_openai_format
from swarm.claude import claude_chat_completion_openai_format
from swarm.constants import (OPENAI_MODELS, 
                             GEMINI_MODELS, 
                             CLAUDE_MODELS, 
                             FIREWORKS_MODELS,
                             OSS_MODELS, 
                             FUNCTION_CALLING_MODELS,
                             AVAILABLE_MODELS)
from swarm.util import *
from swarm.util import _generate_random_id
from dotenv import load_dotenv
load_dotenv()

# Global registry to keep track of all handler instances
_handler_instances = set()

def _cleanup_all_handlers():
    """Kill all registered handler processes."""
    for handler_ref in list(_handler_instances):
        handler = handler_ref()
        if handler is not None and handler.process is not None:
            try:
                handler.kill_process()
            except Exception as e:
                print(f"Error killing process: {e}")

# Register the cleanup function to be called when Python exits
atexit.register(_cleanup_all_handlers)

# Register signal handlers for common termination signals
def _signal_handler(sig, frame):
    print(f"\nReceived signal {sig}, cleaning up...")
    _cleanup_all_handlers()
    # Re-raise the signal after cleanup
    signal.signal(sig, signal.SIG_DFL)
    os.kill(os.getpid(), sig)

# Register handlers for common termination signals
signal.signal(signal.SIGINT, _signal_handler)   # Ctrl+C
signal.signal(signal.SIGTERM, _signal_handler)  # Termination request

class OpenAIHandler:
    """Handles interactions with OpenAI and VLLM-based models."""
    
    def __init__(
        self,
        model_name: str,
        num_gpus: int = 1,
        gpu_memory_utilization: float = 0.9,
        temperature: float = 1.0,
        top_p: float = 1.0,
        max_tokens: int = 1024,
        lora_path: str = "",
        tool_calling: bool = False,
        dtype: str = "bfloat16",
    ) -> None:
        """
        Initialize the OpenAI handler.
        
        Args:
            model_name: Name of the model to use
            backend: Either "vllm" or "openai"
            num_gpus: Number of GPUs to use for VLLM
            gpu_memory_utilization: GPU memory utilization for VLLM
            temperature: Sampling temperature
            top_p: Top-p sampling parameter
            max_tokens: Maximum tokens to generate
            lora_path: Path to LoRA weights
            dtype: Data type for model weights
        """
        self.model_name = model_name # the short name of the model
        self.model_name_huggingface = model_name # the complete name of the model
        self.lora_path = lora_path
        self.temperature = temperature
        self.max_tokens = max_tokens
        self.top_p = top_p
        self.dtype = dtype
        self.tool_calling = tool_calling
        self.process = None
        
        # Add this instance to the global registry
        _handler_instances.add(weakref.ref(self))
        
        # Check model support with case-insensitive comparison
        if model_name in OPENAI_MODELS:
            self.backend = "openai"
        elif model_name in GEMINI_MODELS:
            self.backend = "gemini"
        elif model_name in CLAUDE_MODELS:
            self.backend = "claude"
        elif model_name in FIREWORKS_MODELS:
            self.backend = "fireworks"
        elif model_name in OSS_MODELS:
            self.backend = "vllm"
        else:
            raise ValueError(f"Model {model_name} is not supported.")
        print(f"Using {self.backend} backend.")
        
        # Initialize the backend and the client
        if self.backend == "vllm":
            self.model_name_huggingface = OSS_MODELS[model_name]
            self._init_vllm(num_gpus, gpu_memory_utilization)
        elif self.backend == "fireworks":
            self.model_name_huggingface = FIREWORKS_MODELS[model_name]
            self._init_fireworks()
        elif self.backend == "openai":
            self._init_openai()
        elif self.backend == "claude":
            self._init_claude()
        elif self.backend == "gemini":
            self._init_gemini()
        else:
            raise ValueError(f"Model {model_name} is not supported.")
        print(f"Initialized {self.backend} backend.")
    
    def __del__(self):
        """Destructor to ensure process is killed when object is garbage collected."""
        self.kill_process()
        # Remove this instance from the global registry
        for handler_ref in list(_handler_instances):
            if handler_ref() is self:
                _handler_instances.remove(handler_ref)
                break

    def _init_openai(self) -> None:
        """Initialize OpenAI backend."""
        from openai import Timeout
        kwargs = {"api_key": [REDACTED]"OPENAI_API_KEY")}
        base_url = os.getenv("OPENAI_BASE_URL")
        if base_url:
            kwargs["base_url"] = base_url
        kwargs["timeout"] = Timeout(120.0, connect=30.0)
        self.client = OpenAI(**kwargs)
    
    def _init_fireworks(self) -> None:
        self.client = OpenAI(
            base_url="https://api.fireworks.ai/inference/v1",
            api_key=[REDACTED]"FIREWORKS_API_KEY")
        )
    
    def _init_claude(self) -> None:
        self.client = claude_chat_completion_openai_format
    
    def _init_gemini(self) -> None:
        self.client = gemini_chat_completion_openai_format
    
    def _init_vllm(self, num_gpus: int, gpu_memory_utilization: float) -> None:
        """Initialize VLLM backend."""
        self.VLLM_PORT = random.randint(3000, 8000)
        self.client = OpenAI(
            base_url=f"http://localhost:{self.VLLM_PORT}/v1", 
            api_key="[REDACTED]"
        )

        # Prepare VLLM command
        vllm_cmd = [
            "vllm",
            "serve",
            str(self.model_name_huggingface),
            "--port", str(self.VLLM_PORT),
            "--dtype", str(self.dtype),
            "--tensor-parallel-size", str(num_gpus),
            "--gpu-memory-utilization", str(gpu_memory_utilization),
            "--trust-remote-code",
            "--max-model-len"
        ]
        
        # Add the max model length
        if "gemma" in self.model_name_huggingface.lower():
            vllm_cmd.append("4096")
        elif "mistral" in self.model_name_huggingface.lower():
            vllm_cmd.append("8192")
        elif "llama-3-" in self.model_name_huggingface.lower():
            vllm_cmd.append("32000")
        else:
            vllm_cmd.append("32000")

        # Check if LoRA is enabled  
        if self.lora_path:
            vllm_cmd.extend([
                "--enable-lora",
                "--lora-modules",
                f"sql-lora={self.lora_path}"
            ])

        # Start the server
        self.process = subprocess.Popen(
            vllm_cmd,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )

        # Wait for the server to start
        self._wait_for_server()

    def _wait_for_server(self, max_retries: int = 15, retry_delay: int = 30) -> None:
        """Wait for VLLM server to start."""
        stop_event = threading.Event()

        # Start logging threads
        for pipe in [self.process.stdout, self.process.stderr]:
            thread = threading.Thread(
                target=self._log_subprocess_output,
                args=(pipe, stop_event)
            )
            thread.start()

        # Wait for server
        for retry in range(max_retries):
            try:
                response = requests.get(f"http://localhost:{self.VLLM_PORT}/v1/models")
                if response.status_code == 200:
                    print("Server is ready!")
                    stop_event.set()
                    return
            except requests.exceptions.ConnectionError:
                print(f"Server is not ready yet. Trying {retry+1} times...")
                time.sleep(retry_delay)

        raise ConnectionError(f"Server not ready after {max_retries} retries.")

    @staticmethod
    def _log_subprocess_output(pipe, stop_event):
        """Log subprocess output until stop event is set."""
        for line in iter(pipe.readline, ""):
            if stop_event.is_set():
                break
            print(line, end="")
        pipe.close()

    def kill_process(self):
        """
        Kill the server process.
        """
        if self.process:
            try:
                self.process.terminate()
                # Give it a moment to terminate gracefully
                try:
                    self.process.wait(timeout=5)
                except subprocess.TimeoutExpired:
                    # Force kill if it doesn't terminate gracefully
                    self.process.kill()
                    self.process.wait()
                print(f"Server process for {self.model_name} terminated.")
            except Exception as e:
                print(f"Error terminating process: {e}")
            finally:
                self.process = None

    def _extract_thinking_from_content(self, completion: ChatCompletion) -> ChatCompletion:
        """Extract <think>xxx</think> content and store it in the thinking field of ChatCompletionMessage."""
        import re
        
        # Process each choice in the completion
        for choice in completion.choices:
            if choice.message.content:
                # Look for <think>xxx</think> patterns
                think_pattern = re.compile(r'<think>(.*?)</think>', re.DOTALL)
                matches = think_pattern.findall(choice.message.content)
                
                if matches:
                    # Extract the thinking content (join if multiple matches)
                    thinking_content = '\n'.join(matches)
                    # Store in thinking field
                    choice.message.thinking = thinking_content
                    # Remove the <think>xxx</think> pattern from content
                    choice.message.content = think_pattern.sub('', choice.message.content).strip()
                elif "</think>" in choice.message.content:
                    # split the content by </think>
                    thinking_content = choice.message.content.split("</think>")[0]
                    choice.message.thinking = thinking_content
                    choice.message.content = choice.message.content.split("</think>")[1].strip()
        return completion
    
    def format_message(self, message) -> dict:
        """
        Format the message to the correct format for all chat completion API.
        """
        # convert the message to a dict
        if not isinstance(message, dict):
            message = ChatCompletionMessage_to_dict(message)
        assert isinstance(message, dict), "Message must be a dict."
        
        # cache_control is only used in claude
        if "cache_control" in message:
            del message["cache_control"]
        
        # remove thinking process used in claude
        if "thinking" in message:
            del message["thinking"]
        if "thinking_signature" in message:
            del message["thinking_signature"]
        
        # openai format does not have tool_name
        if message["role"] == "tool":
            del message["tool_name"] 
        
        if message["role"] == "user":
            if "sender" in message:
                del message["sender"]
            if "tool_calls" in message:
                del message["tool_calls"]
                
        # remove the sender field
        if "sender" in message:
            del message["sender"]
            
        if "response_id" in message:
            del message["response_id"]
            
        # remove the unneeded fields for non-openai format messages
        if self.backend != "openai" and message["role"] == "assistant":
            if "function_call" in message:
                del message["function_call"]
            if "refusal" in message:
                del message["refusal"]
            if "audio" in message:
                del message["audio"]

        return message
    
    def response_completion(self, test_entry: dict, include_debugging_log: bool, tool_call_mode: Literal["fc", "prompt", "react", "act-only", "react-v"] = "fc"):
        """
        Response completion API from OpenAI o-series models
        Reference: https://platform.openai.com/docs/guides/reasoning
        """
        def format_tools(tools: List[dict]) -> List[dict]:
            """
            Format the tools for the response completion API.
            """
            formatted_tools = []
            for tool in tools:
                formatted_tool = {
                    "type": "function",
                    "name": tool["function"]["name"],
                    "description": tool["function"]["description"],
                    "parameters": tool["function"]["parameters"],
                }
                formatted_tools.append(formatted_tool)
            return formatted_tools
        
        max_tokens = max(test_entry.get("max_tokens", self.max_tokens), 2048)
        model_name = self.model_name_huggingface
        reasoning_effort = "medium"
        tools = test_entry.get("tools", None)
        formatted_tools = format_tools(tools)
        # reasoning effort is only supported for openai reasoning models
        if self.model_name_huggingface.split("-")[-1] in ["low", "medium", "high"]:
            model_name = self.model_name_huggingface.replace("-low", "").replace("-medium", "").replace("-high", "")
            reasoning_effort = self.model_name_huggingface.split("-")[-1]
            assert reasoning_effort in ["low", "medium", "high"], f"Reasoning effort {reasoning_effort} is not supported."
        
        # Format the messages into the correct format for all chat completion API
        norm_messages = copy.deepcopy(test_entry["messages"])        
        # First check if using previous_response_id
        last_response_id = None
        last_respond_turn = -1
        last_assistant_turn = -1
        for idx, message in enumerate(norm_messages):
            if message["role"] == "assistant":
                last_assistant_turn = idx
                if message.get("response_id", None):
                    last_response_id = message["response_id"]
                    last_respond_turn = idx
        # Then clean the messages after recording the last response ID
        norm_messages = [self.format_message(message) for message in norm_messages]

        if last_response_id:
            # put all the turns after the last response turn into the input
            # format the input messages
            input_messages = []
            for message in norm_messages[last_respond_turn+1:]:
                if message["role"] == "user":
                    input_messages.append({
                        "role": "user",
                        "content": message["content"]
                    })
                elif message.get("tool_call_id", None):
                    input_messages.append({
                        "type": "function_call_output",
                        "call_id": message["tool_call_id"],
                        "output": message["content"]
                    })
                elif message["role"] == "assistant":
                    raise ValueError("Assistant message is not allowed in the input.")
            
            print("Using previous response ID in response API!")
            response = self.client.responses.create(model=model_name, 
                                                    input=input_messages,
                                                    reasoning={"effort": reasoning_effort},
                                                    tools=formatted_tools,
                                                    max_output_tokens=max_tokens,
                                                    previous_response_id=last_response_id)
        elif last_assistant_turn == -1: # no previous assistant turn, so it is the first turn
            print("First turn without using previous response ID in response API!")
            # format the input messages
            input_messages = norm_messages
            response = self.client.responses.create(model=model_name, 
                                                    input=input_messages,
                                                    reasoning={"effort": reasoning_effort},
                                                    tools=formatted_tools,
                                                    max_output_tokens=max_tokens)            
        else:
            raise ValueError("Invalid test entry. Not the first turn and no response ID found.")
        
        # convert the response back to chat completion format
        response_id = response.id
        response_text = response.output_text
        output = response.output
        function_calls = []
        thinking = None
        thinking_signature = None
        for item in output:
            if item.type == "function_call":
                function_calls.append(
                    ChatCompletionMessageToolCall(
                        id=item.call_id,
                        type='function',
                        function=Function(
                            name=item.name,
                            arguments=item.arguments
                        )
                    )
                )
            elif item.type == "reasoning":
                thinking = item.summary if item.summary else ""
                thinking_signature = item.id
        
        message = ChatCompletionMessage(
            role='assistant',
            content=response_text,
            thinking=thinking,
            thinking_signature=thinking_signature,
            response_id=response_id, # record the response id for the next turn
            tool_calls=function_calls if function_calls else None
        )
        
        # Create the choice
        choice = Choice(
            finish_reason='stop' if hasattr(response, 'stop_reason') and response.stop_reason == 'end_turn' 
                        else getattr(response, 'stop_reason', 'stop'),
            index=0,
            logprobs=None,
            message=message
        )
        choices = [choice]
        
        # Create usage details
        if hasattr(response, 'usage'):
            # Handle both OpenAI and Claude usage formats
            usage_obj = response.usage.to_dict()
            completion_tokens = usage_obj["output_tokens"]
            prompt_tokens = usage_obj["input_tokens"]
            total_tokens = usage_obj["total_tokens"]
            reasoning_tokens = usage_obj["output_tokens_details"]["reasoning_tokens"]
            
            usage = CompletionUsage(
                completion_tokens=completion_tokens,
                prompt_tokens=prompt_tokens,
                total_tokens=total_tokens,
                completion_tokens_details=CompletionTokensDetails(),
                prompt_tokens_details=PromptTokensDetails()
            )

        # Create the complete ChatCompletion object
        completion = ChatCompletion(
            id=response.id,
            choices=choices,
            created=int(time.time()),
            model=response.model,
            object='chat.completion',
            system_fingerprint=f'fp_{_generate_random_id(8)}',
            usage=usage
        )
        return {"idx": test_entry.get("idx", 0), "completion": completion}
    
    def chat_completion(self, test_entry: dict, include_debugging_log: bool, tool_call_mode: Literal["fc", "prompt", "react", "act-only", "react-v"] = "fc"):
        """
        OSS models have a different inference method.
        They need to spin up a server first and then send requests to it.
        It is more efficient to spin up the server once for the whole batch, instead of for each individual entry.
        So we implement batch_inference method instead.
        """        
        # format the messages into the correct format for all chat completion API
        norm_messages = copy.deepcopy(test_entry["messages"])
        if self.backend in ["openai", "vllm", "fireworks", "gemini"]:
            for idx, message in enumerate(norm_messages):
                norm_messages[idx] = self.format_message(message)
        
        # Create base parameters for completion request
        chat_completion_params = {
            "model": self.model_name_huggingface,
            "messages": norm_messages,
            "temperature": test_entry.get("temperature", self.temperature),
            "n": test_entry.get("n", 1),
            "top_p": test_entry.get("top_p", self.top_p),
            "max_tokens": test_entry.get("max_tokens", self.max_tokens),
            "logprobs": test_entry.get("logprobs", False),
            "stop": test_entry.get("stop", None)
        }
                
        ######################################################################
        # TOOL CALLING: Different ways to call tools and take actions
        ######################################################################
        tools = test_entry.get("tools", None)
        if not tools:
            if self.backend in ["openai", "vllm", "fireworks"]:
                completion = self.client.chat.completions.create(**chat_completion_params)
            elif self.backend in ["gemini", "claude"]:
                completion = self.client(**chat_completion_params)
            else:
                raise ValueError(f"Model {self.model_name_huggingface} is not supported.")
            # Process completion to extract thinking content
            completion = self._extract_thinking_from_content(completion)
            return {"idx": test_entry.get("idx", 0), "completion": completion}
        
        ######################################################################
        # FC or Prompt-based tool calling
        ######################################################################
        if tool_call_mode == "fc":
            assert self.model_name in FUNCTION_CALLING_MODELS[self.backend], f"Model {self.model_name} is not supported for tool calling."
            chat_completion_params["tools"] = tools
            if self.backend in ["openai", "vllm"]:
                if not any(_ in self.model_name_huggingface for _ in ["o1", "o3", "o4"]):
                    chat_completion_params["parallel_tool_calls"] = test_entry.get("parallel_tool_calls", False)
                if self.model_name_huggingface in ["gpt-5", "gpt-5-mini", "gpt-5-nano"]:
                    # Replace max_tokens with max_completion_tokens
                    max_completion_tokens = chat_completion_params.get("max_tokens", 1024)
                    del chat_completion_params["max_tokens"]
                    del chat_completion_params["temperature"]
                    del chat_completion_params["top_p"]
                    chat_completion_params["max_completion_tokens"] = max_completion_tokens
                completion = self.client.chat.completions.create(**chat_completion_params)
            elif self.backend in ["fireworks"]:
                # Does not support "strict" field in tool description
                norm_tools = copy.deepcopy(tools)
                for tool in norm_tools:
                    if "strict" in tool["function"]:
                        del tool["function"]["strict"]
                chat_completion_params["tools"] = norm_tools
                completion = self.client.chat.completions.create(**chat_completion_params)
            elif self.backend in ["gemini", "claude"]:
                completion = self.client(**chat_completion_params)
            else:
                raise ValueError(f"Model {self.model_name_huggingface} is not supported.")
            return {"idx": test_entry.get("idx", 0), "completion": completion}
        
        
        # Prompt-based tool calling (react or act-only), 
        # Need input formatter and output parser, and change into FC format    
        elif tool_call_mode in ["react", "act-only", "react-v"]:            
            if self.backend in ["openai", "vllm", "fireworks"]:
                chat_completion_func = self.client.chat.completions.create
            elif self.backend in ["gemini", "claude"]:
                chat_completion_func = self.client
            else:
                raise ValueError(f"Model {self.model_name_huggingface} is not supported.")
            
            # Call ReAct tool calling with planning mode if specified
            from swarm.ReAct import ReAct_tool_calling
            completion = ReAct_tool_calling(
                chat_completion_func=chat_completion_func,
                chat_completion_params=chat_completion_params,
                messages=norm_messages,
                tools=tools,
                reasoning=(tool_call_mode != "act-only"),
                verification=(tool_call_mode == "react-v")
            )
            return {"idx": test_entry.get("idx", 0), "completion": completion}
        
        else:
            raise ValueError(f"Tool call mode {tool_call_mode} is not supported.")

    def text_completion(self, test_entry: dict, include_debugging_log: bool):
        """
        OSS models have a different inference method.
        They need to spin up a server first and then send requests to it.
        It is more efficient to spin up the server once for the whole batch, instead of for each individual entry.
        So we implement batch_inference method instead.
        """
        # Fix: Use the correct method for creating a completion request
        completion = self.client.completions.create(
            model=self.model_name_huggingface,
            prompt=test_entry["prompt"],
            echo=False,
            temperature=test_entry.get("temperature", self.temperature),
            n=test_entry.get("n", 1),
            top_p=test_entry.get("top_p", self.top_p),
            max_tokens=test_entry.get("max_tokens", self.max_tokens),
            logprobs=test_entry.get("logprobs", False),
        )
        return {"idx": test_entry.get("idx", 0), "completion": completion}

    def inference(
        self, test_entry: dict, include_debugging_log: bool, mode: str = "chat", tool_call_mode: str = "fc"
    ):
        if mode == "reasoning":
            return self.response_completion(test_entry, include_debugging_log, tool_call_mode)
        elif mode == "chat":
            return self.chat_completion(test_entry, include_debugging_log, tool_call_mode)
        elif mode == "text":
            return self.text_completion(test_entry, include_debugging_log)
        else:
            raise ValueError(f"Mode {mode} is not supported.")

    def batch_inference(
        self,
        test_entries: List[dict],
        include_debugging_log: bool,
        mode: str = "chat",
        num_workers: int = 8,
    ) -> List[List[str]]:
        # Once the server is ready, make the completion requests
        results = []
        futures = []
        with ThreadPoolExecutor(max_workers=num_workers) as executor:
            # with tqdm(total=len(test_entries)) as pbar:
            for idx, test_case in enumerate(test_entries):
                test_case["idx"] = idx
                future = executor.submit(
                    self.inference,
                    test_case,
                    include_debugging_log,
                    mode,
                )
                futures.append(future)

            for future in futures:
                # This will wait for the task to complete, so that we are always writing in order
                result = future.result()
                results.append(result)
                # pbar.update()
                
        # reorder the results based on the original order
        results = sorted(results, key=lambda x: x["idx"])
        results = [res["completion"] for res in results]
        return results



if __name__ == "__main__":
    
    tools = [
    {
        "type": "function",
        "function": {
            "name": "get_delivery_date",
            "description": "Get the delivery date for a customer's order. Call this whenever you need to know the delivery date.'",
            "parameters": {
                "type": "object",
                "properties": {
                    "order_id": {
                        "anyOf": [
                            {
                                "type": "string",
                                "description": "The customer's order ID.",
                            },
                            {
                                "type": "object",
                                "description": "The order person and name in the format of YYYY-MM-DD.",
                                "properties": {
                                    "order_person": {
                                        "type": "string",
                                        "description": "The order person.",
                                    },
                                    "order_name": {
                                        "type": "string",
                                        "description": "The name of the order.",
                                    }
                                },
                            }
                        ]
                    },
                },
                "required": ["order_id"],
            },
        }
        },
    {
        "type": "function",
        "function": {
            "name": "set_reminder",
            "description": "Get the delivery date for a customer's order. Call this whenever you need to know the delivery date.'",
            "parameters": {
                "type": "object",
                "properties": {
                    "reminder_time": {
                        "type": "string",
                        "description": "The time to set the reminder in the format of YYYY-MM-DD.",
                    },
                    "reminder_content": {
                        "type": "string",
                        "description": "The content of the reminder.",
                    },
                },
                "required": ["reminder_time", "reminder_content"],
            },
        }
    }
    ]

    messages = [
        {
            "role": "system",
            "content": "You are a helpful customer support assistant. Use the supplied tools to assist the user."
        },
        {
            "role": "user",
            "content": "Hi, can you tell me the delivery date for my order? The order person is John Doe and the order name is Dominos Pizza. Also, set a reminder for me to check the order at that time."
        },
        # {
        #     "role": "assistant",
        #     "content": None,
        #     "thinking": "",
        #     "tool_calls": [
        #         {
        #             "id": "call_sNcq3LV89bWJCWgZvJpCac7I",
        #             "function": {
        #                 "arguments": "{\"order_person\":\"John Doe\",\"order_name\":\"Dominos Pizza\"}",
        #                 "name": "get_delivery_date"
        #             },
        #             "type": "function"
        #         },
        #     ],
        #     "response_id": "resp_681c43a70440819195651a76d75f3def02f8ecc0cd0ebd91"
        # },
        # {
        #     "role": "tool",
        #     "tool_call_id": "call_6pITl9bo8BF4OzvckSXkQVQh",
        #     "tool_name": "get_delivery_date",
        #     "content": "2024-12-12"
        # }
    ]
    
    # model_name = "claude-3-7-sonnet-20250219-thinking"
    model_name = "qwen2.5-14b-instruct"
    # model_name = "gpt-4.1-mini"
    # model_name = "o4-mini"
    model = OpenAIHandler(
        model_name=model_name,
        temperature=0.0,
        top_p=0.01,
        tool_calling=True,
        num_gpus=2,
        gpu_memory_utilization=0.9,
    )
    
    test_entry = {
        "messages": messages,
        "tools": tools,
        "n": 1,
    }

    print(model.inference(test_entry, include_debugging_log=True, 
                          mode="chat", tool_call_mode="react"))
    # print(model.response_completion(test_entry, include_debugging_log=True, tool_call_mode="fc"))
    model.kill_process()

    
