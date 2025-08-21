from collections.abc import Generator
from typing import Any

from dify_plugin import Tool
from dify_plugin.entities.tool import ToolInvokeMessage

import json
class ProcessingLLMRespTextTool(Tool):
    def _invoke(self, tool_parameters: dict[str, Any]) -> Generator[ToolInvokeMessage]:
        input: str = tool_parameters.get("llm_resp_text", "")
        try:
            if input.startswith('<think>'):
                i = input.find('</think>')
                think = input[7:i]
                input = input[i + 8:]
            else:
                think = ''

            input = input.strip()
            if input.startswith('```json'):
                input = input.removeprefix('```json').removesuffix('```')
            else:
                input = input.strip('```')
            input = input.strip()

            yield self.create_json_message({
                "think": think,
                "content": json.loads(input),
            })
        except Exception as e:
            raise e
