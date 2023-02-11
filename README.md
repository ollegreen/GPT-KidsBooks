# Book-GPT

This next step in the road to writing books using transformers / autoregressive language models is to build a custom model focusing on generating text for books. Specifically: **kids books**.

*For context*: The first step was to use GPT-3 to write a kids book, see amazon link [here](https://www.amazon.co.uk/Bob-Robot-Exploring-Artificial-Intelligence-ebook/dp/B08GL2YWGY) and this link to the github [here](https://github.com/ollegreen/AI_Kindle_Kids_Book).

![bob](https://m.media-amazon.com/images/I/41xWl7EWyFL.jpg)

## Why build a GPT algorithm that focuses on books?

GPT algorithms are models that perform likelihood tests of what character to be next. It isn't the best at finding sources or truth, and can make up a fair amount of information with little to no visibility of the reliability of this information.

Therefore, let's use the main benefit of these models: their creativity. We will focus on trying to make an algorithm that is trained on non-factual data, in this case: kids stories.

### Considerations
