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


### For Development
Debug On Dify

1. **Prepare**
   ```bash
   #Create a python virtual environment
   python -m venv venv

   source venv/bin/activate
   pip install -r requirements.txt
   ```

2. **Configure**
   ```bash
   #see https://docs.dify.ai/plugin-dev-en/0222-creating-new-model-provider-extra#step-4%3A-debug-plugin
   cp .env.example .env
   vim .env
   ```

3. **Run**
   ```bash
   source venv/bin/activate
   python -m main
   ```

