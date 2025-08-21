## dify-json-tools

**Author:** ameven
**Version:** 0.0.1
**Type:** tool

### Description

A dify plugin for processing json format data.

### Usage
- **Processing LLM response text**:

  A tool for processing LLM response text.
  When you fill text into `llm_resp_text` (a llm response text), like: `<think>I will print 'hello world'. </think> ```json{"result": "hello world"}``` `, you will get a json result:

  ```json
  {
    "think": "I will print 'hello world'.",
    "content": {
      "result": "hello world"
    }
  }
  ```
