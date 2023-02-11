# Book-GPT
## Problem statement:
You are a parent and you've had a long day at work. You come home and want to spend some quality time with your kid and read them a bedtime story so they go to sleep. After reading the same story multiple times, you want to personalise/customise the stories to link what your child has done today and celebrate their achievements. Since you need a bit of "alone time" with your partner, we are also keen about the story being less than 30 minutes of reading time.

Using Book-GPT and the dedicated website: you can now go onto the site and generate your custom kids book with a click of a few buttons.

## Project Context
This next step in the road to writing books using transformers / autoregressive language models is to build a custom model focusing on generating text for books. Specifically: **kids books**.

*For context*: The first step was to use GPT-3 to write a kids book, see amazon link [here](https://www.amazon.co.uk/Bob-Robot-Exploring-Artificial-Intelligence-ebook/dp/B08GL2YWGY) and this link to the github [here](https://github.com/ollegreen/AI_Kindle_Kids_Book).

![bob](https://m.media-amazon.com/images/I/41xWl7EWyFL.jpg)

## Why build a GPT algorithm that focuses on books?

GPT algorithms are models that perform likelihood tests of what character to be next. It isn't the best at finding sources or truth, and can make up a fair amount of information with little to no visibility of the reliability of this information.

Therefore, let's use the main benefit of these models: their creativity. We will focus on trying to make an algorithm that is trained on non-factual data, in this case: kids stories.

### Use-case, UX and flow:
The idea is for parents to quickly generate a kids book text based on prompts/categories, and easily have a story to tell the kids at night time.

To simplify deployment, we use streamlit to deploy the algorithm.



#### Future potential monetisation:
I don't want people to pay.
Instead we're looking at getting "credits", where you can generate 10 books for $2. This means that even if you are not fully satisfied with 8 out of 10 books, it's still only $1 per book, with a potential of getting 10 kids book for $2 (20 cents per book, which is pretty good imo).