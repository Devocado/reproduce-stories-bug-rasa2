# Reproduce stories bug Rasa 2.0.x

This repo has been create to reproduce a bug in the way Rasa 2 handles stories.

## The problem:
It is actually difficult to say what is happening here. It appears that Rasa 2.0.x is not able to predict the correct actions when the events before a story are different, where Rasa 1.10.x makes correct predictions.

This repo demonstrates two instances of this.
- In the first case, circling back to a certain point in a story (demonstrated in the first test) ends in Rasa 2.0.x falling back, while Rasa 1.10.x correctly follows the same path as before.
- In the second case, where a story does not overlap with other stories Rasa 2.0.x will not predict the correct actions when the intent which begins the story is triggered. Again, the second test fails in Rasa 2.0.x while passing in rasa 1.10.x

## Steps to reproduce:
- Train the assistant in Rasa 1.10.14.
- Run the tests

All tests will pass.

- Train the assistant in Rasa 2.0.x
- Run the tests

The first two tests will fail