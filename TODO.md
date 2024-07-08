# TODO

## Code

* add --api-key support, NAME_OF_KEY_TO_LOOK_FOR, no fall back
* add support for response_format
* fix arguments to handle strings OR files for command line options
* fix output and move to separate function
* JSON schema for output format, standardize on a single format with options for each backend
* handle error conditions (mostly rate limiting errors)
* can we fix the relative import path so this tool works as a command line tool? Do we simply need to make a seperate .py?
* max_retries (disable retries by default?)
* timeout (120 seconds?)

Future:

* add batch processing support (https://platform.openai.com/docs/api-reference/batch/object)
* for sub 1000 max_tokens put the "max_tokens: X" into the system prompt at the top
* figure out if we can generate JSON/markdown/etc responses in a more generic way (e.g. system prompt with exmaple output?)
* add option to wrap user data in JSON if it's not already JSON?
* add "use_latest" style option to the prompt/data inputs so it searches for the most recent prompt for example, this will also need a directory passed in when used as a library
* Break out API key code so it can be an env variable, a config file, IAM options
* How to handle multiple round conversations, JSON input?
* Additional tools/inputs (e.g. images)
* Context caching for longer prompts https://ai.google.dev/gemini-api/docs/caching

## Docs for items

### response_format

* "response_format" https://platform.openai.com/docs/api-reference/audio/createTranscription
* https://docs.anthropic.com/en/docs/control-output-format
* "response_mime_type" https://ai.google.dev/gemini-api/docs/api-overview#json

## Tests

* add pickling/unpickling capability to code for testing, both software, and tools using it
* add tests for dev
* add tests for CI/CD
* Investigate evals integration: https://github.com/openai/evals

## Infra

* move to poetry

## Future

* figure out GitHub trusted publishing to PyPi

## Specific notres

### JSON output:

## Future notes:

This library shouldn't be needed long term:

chatgpt:

To prevent these errors and improve model performance, when using gpt-4o, gpt-4-turbo, or gpt-3.5-turbo, you can set response_format to { "type": "json_object" } to enable JSON mode. When JSON mode is enabled, the model is constrained to only generate strings that parse into valid JSON object.

https://platform.openai.com/docs/guides/text-generation/json-mode

claude:

Not possible? Closest piece of documentation:

https://docs.anthropic.com/en/docs/test-and-evaluate/strengthen-guardrails/increase-consistency#example-standardizing-customer-feedback

gemini:

Use response_schema

https://ai.google.dev/gemini-api/docs/json-mode

