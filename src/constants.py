refine_text_prompt_base = '''Please generate a refined document of the
following document. And please ensure that
the refined document meets the following
criteria:
1. Ensure the refined version remains abstract and does not change the original meaning.
2. Retain all important elements, concepts, and relationships from the original document.
3. Do not add, remove, or modify information beyond what exists in the original content.
4. The refined version must be clear, concise, and easy to read, with no abbreviations or spelling errors.
5. Present the content in a structured, organized format for better readability.
Here is the content to refine: '''

knowlegde_extractor_prompt_base = '''You are a knowledge graph extractor, and your
task is to extract and return a knowledge
graph from a given text.Let’s extract it
step by step:
(1). Identify the entities in the text. An
entity can be a noun or a noun phrase that
refers to a real-world object or an
abstract concept. You can use a named
entity recognition (NER) tool or a part-of
-speech (POS) tagger to identify the
entities. No need to return the answer for this step.
(2). Identify the relationships between the
entities. A relationship can be a verb or
a prepositional phrase that connects two
entities. You can use dependency parsing
to identify the relationships. No need to return the answer for this step.
(3). Summarize each entity and relation as
short as possible and remove any stop
words. No need to return the answer for this step.
(4). The response of the knowledge graph must be the
triplet format given below:
(’head entity’, ’relation
’, ’tail entity’).
(5). Most importantly, if you cannot find any
knowledge, please just output: 'None'.
Here is the content: '''